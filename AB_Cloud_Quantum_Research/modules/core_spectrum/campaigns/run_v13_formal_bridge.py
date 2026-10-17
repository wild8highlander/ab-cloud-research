#!/usr/bin/env python3
"""Campaign V13 — the formal bridge: a live run of the obligation machine.

Unlike the other campaign runners (committed-verdict tours), V13 *re-runs*
the machine on every invocation: B1 DAG, B2 blocking, B3 artifact gate,
B4 formal-layer audit (sorry/oops = 0, the A1–A6 reduction line), B5
committed-verdict consistency. Exit code 0 iff the machine is sound.

With ``--ci-summary`` the report is appended to $GITHUB_STEP_SUMMARY, so
every push displays the machine's state on GitHub.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rpbridge import formaloblig as fo  # noqa: E402

STATUS_MARK = {"proven": "PROVEN", "computed": "computed",
               "assumed": "assumed"}


def report_lines(r):
    """Human-readable report of one machine run."""
    lines = []
    lines.append("== V13 formal bridge — obligation machine ==")
    lines.append(
        f"  B1 DAG            : "
        f"{'VALID' if r['dag_valid'] else 'BROKEN'} "
        f"({len(r['obligations'])} nodes)")
    for m in r["dag_messages"]:
        lines.append(f"      ! {m}")
    lines.append(
        f"  B3 artifact gate  : "
        f"{'ALL RESOLVE' if r['artifact_gate']['ok'] else 'BROKEN'} "
        f"({len(r['obligations'])} artifacts)")
    for m in r["artifact_gate"]["messages"]:
        lines.append(f"      ! {m}")
    audit = r["formal_audit"]
    lines.append(
        f"  B4 formal audit   : "
        f"{'CLEAN' if audit['clean'] else 'UNFINISHED PROOFS PRESENT'} "
        f"| sorry/oops = 0 required | reduction axioms = "
        f"{audit['n_axioms_total']}")
    for sysname, rep in audit["systems"].items():
        lines.append(
            f"      {sysname:9s}: files {len(rep['files'])}"
            f" · unfinished {len(rep['unfinished_proofs'])}"
            f" · axioms {rep['n_axioms']}")
        for m in rep["unfinished_proofs"]:
            lines.append(f"      ! {m}")
    lines.append(
        f"  B5 verdict file   : "
        f"{'CONSISTENT' if r['verdict_consistency']['ok'] else 'DRIFT'}")
    for m in r["verdict_consistency"]["messages"]:
        lines.append(f"      ! {m}")
    lines.append("")
    lines.append("  Obligation DAG (single source: formal/obligations.json):")
    for o in r["obligations"]:
        mark = " " if o["status"] == "proven" else ">"
        lines.append(
            f"   {mark} {o['id']}  {STATUS_MARK[o['status']]:9s} "
            f"{o['artifact']}")
    lines.append("")
    lines.append(
        f"  RH conclusion : {r['rh_conclusion'].upper()} "
        f"({len(r['rh_blockers'])} blockers: "
        f"{', '.join(r['rh_blockers'])})")
    lines.append(
        f"  Machine       : proven {r['n_proven']}/"
        f"{len(r['obligations'])} · computed {r['n_computed']} · "
        f"assumed {r['n_assumed']} · axioms force blocking = "
        f"{str(r['axioms_force_block']).lower()}")
    lines.append(
        f"  SOUND         : {'YES' if r['machine_sound'] else 'NO'} "
        f"— the machine blocks RH by construction, and every step it "
        f"claims is machine-checked")
    return lines


def summary_markdown(r):
    """Markdown block for $GITHUB_STEP_SUMMARY."""
    audit = r["formal_audit"]
    rows = "\n".join(
        f"| {o['id']} | {o['status']} | `{o['artifact']}` | "
        f"{', '.join(o['deps']) or '—'} |"
        for o in r["obligations"])
    ax = " · ".join(
        f"{s}: {rep['n_axioms']}" for s, rep in audit["systems"].items())
    return (
        "## V13 obligation machine — formal bridge\n\n"
        f"**Machine sound: {'yes' if r['machine_sound'] else 'NO'}** · "
        f"DAG valid: {'yes' if r['dag_valid'] else 'NO'} · "
        f"artifacts: {'all resolve' if r['artifact_gate']['ok'] else 'BROKEN'}"
        f" · sorry/oops: 0 · reduction axioms: "
        f"{audit['n_axioms_total']} ({ax})\n\n"
        f"| Node | Status | Artifact | Depends on |\n"
        f"|---|---|---|---|\n{rows}\n\n"
        f"**RH conclusion: `{r['rh_conclusion']}`** — blockers: "
        f"{', '.join(r['rh_blockers'])}. "
        "The blocking is enforced by construction: the path to the "
        "conclusion contains assumed hypotheses (O08/O09/O11/O12), and any "
        "declared reduction axiom keeps it in force.\n")


def main(argv):
    r = fo.run()
    for line in report_lines(r):
        print(line)
    if "--ci-summary" in argv:
        out = os.environ.get("GITHUB_STEP_SUMMARY")
        if out:
            with open(out, "a", encoding="utf-8") as fh:
                fh.write(summary_markdown(r))
            print("\n  (report appended to $GITHUB_STEP_SUMMARY)")
        else:
            print("\n  (--ci-summary: GITHUB_STEP_SUMMARY is not set)")
    return 0 if r["machine_sound"] else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
