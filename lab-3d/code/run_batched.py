"""
run_batched.py
==============
Run all 99 verifications in batches, saving intermediate results after each batch.
This avoids the issue of long-running processes being killed mid-execution.

Each batch is saved to results/data/batches/batch_NN.json. After all batches
complete, the batches are merged into verification_report.json and
verification_summary.md.
"""
import json
import sys
import time
import gc
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from python.run_monumental import VERIFICATIONS, _to_jsonable, _safe

REPORT_DIR = HERE.parent / "results" / "data"
BATCH_DIR = REPORT_DIR / "batches"
BATCH_DIR.mkdir(parents=True, exist_ok=True)


def run_batch(batch_id: str, only_ids: list) -> dict:
    """Run a batch of verifications by ID, save to disk, return summary."""
    print(f"\n=== Batch {batch_id}: {len(only_ids)} verifications ===")
    results = []
    t_start = time.time()
    for vid in only_ids:
        ver = next((v for v in VERIFICATIONS if v["id"] == vid), None)
        if ver is None:
            print(f"  {vid}: NOT FOUND")
            continue
        print(f"  [{vid}] {ver['name']} ... ", end="", flush=True)
        t0 = time.time()
        result, err = _safe(ver["fn"])
        elapsed = time.time() - t0
        if err:
            print(f"ERROR ({elapsed:.1f}s)")
            results.append({
                "id": vid, "name": ver["name"], "status": "error",
                "error": err.splitlines()[0], "elapsed_seconds": elapsed,
            })
        else:
            print(f"OK ({elapsed:.1f}s)")
            entry = {
                "id": vid, "name": ver["name"], "status": "ok",
                "description": ver["desc"],
                "result": _to_jsonable(result),
                "elapsed_seconds": elapsed,
            }
            # Generate plot if applicable
            if ver["plot_fn"]:
                try:
                    plot_path = ver["plot_fn"](result)
                    if plot_path:
                        entry["plot"] = plot_path
                except Exception as e:
                    entry["plot_error"] = f"{type(e).__name__}: {e}"
            results.append(entry)
        gc.collect()
    elapsed_total = time.time() - t_start
    n_ok = sum(1 for r in results if r["status"] == "ok")
    n_err = sum(1 for r in results if r["status"] == "error")
    print(f"  Batch {batch_id} done: {n_ok} OK, {n_err} errors, {elapsed_total:.1f}s")

    # Save batch
    batch_path = BATCH_DIR / f"batch_{batch_id}.json"
    with open(batch_path, "w", encoding="utf-8") as f:
        json.dump({
            "batch_id": batch_id,
            "verifications": results,
            "n_ok": n_ok, "n_error": n_err,
            "elapsed_seconds": elapsed_total,
        }, f, indent=2, ensure_ascii=False, default=str)
    print(f"  Saved: {batch_path}")
    return {"n_ok": n_ok, "n_error": n_err, "elapsed": elapsed_total}


def merge_batches():
    """Merge all batch_NN.json files into a single report."""
    all_results = []
    total_elapsed = 0
    batch_files = sorted(BATCH_DIR.glob("batch_*.json"))
    print(f"\n=== Merging {len(batch_files)} batches ===")
    for bf in batch_files:
        with open(bf) as f:
            b = json.load(f)
        all_results.extend(b["verifications"])
        total_elapsed += b["elapsed_seconds"]
    n_ok = sum(1 for r in all_results if r["status"] == "ok")
    n_err = sum(1 for r in all_results if r["status"] == "error")
    n_plots = sum(1 for r in all_results if "plot" in r)

    report = {
        "title": "AB-Cloud Monograph Verification — Monumental Edition",
        "total_verifications": len(VERIFICATIONS),
        "results": all_results,
        "plots": [r["plot"] for r in all_results if "plot" in r],
        "summary": {
            "total_run": len(all_results),
            "n_ok": n_ok,
            "n_error": n_err,
            "n_plots": n_plots,
            "elapsed_seconds": total_elapsed,
        },
    }
    # Save full report
    report_path = REPORT_DIR / "verification_report.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False, default=str)
    print(f"Report saved: {report_path}")

    # Save markdown summary
    md_path = REPORT_DIR / "verification_summary.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# AB-Cloud Monograph Verification — Monumental Edition\n\n")
        f.write(f"- Total verifications: {report['total_verifications']}\n")
        f.write(f"- Run: {report['summary']['total_run']}\n")
        f.write(f"- OK: {report['summary']['n_ok']}\n")
        f.write(f"- Errors: {report['summary']['n_error']}\n")
        f.write(f"- Plots: {report['summary']['n_plots']}\n")
        f.write(f"- Elapsed: {report['summary']['elapsed_seconds']:.1f}s\n\n")
        f.write("## Results\n\n")
        f.write("| ID | Name | Status | Description |\n")
        f.write("|----|------|--------|-------------|\n")
        for r in all_results:
            desc = r.get("description", "")
            f.write(f"| {r['id']} | {r['name']} | {r['status']} | {desc} |\n")
    print(f"Summary saved: {md_path}")
    return report


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=str, default=None,
                        help="Run a specific batch (e.g., '01' for V01-V20)")
    parser.add_argument("--merge", action="store_true",
                        help="Merge all existing batch files into final report")
    parser.add_argument("--batch-size", type=int, default=10,
                        help="Number of verifications per batch (default 10)")
    args = parser.parse_args()

    all_ids = [v["id"] for v in VERIFICATIONS]
    n_total = len(all_ids)

    if args.merge:
        merge_batches()
        return

    if args.batch:
        # Run a specific batch by letter/number
        batch_size = args.batch_size
        batch_idx = int(args.batch) - 1
        start = batch_idx * batch_size
        end = min(start + batch_size, n_total)
        batch_ids = all_ids[start:end]
        run_batch(f"{args.batch}", batch_ids)
        return

    # Otherwise: list batches to run
    batch_size = args.batch_size
    n_batches = (n_total + batch_size - 1) // batch_size
    print(f"Total verifications: {n_total}")
    print(f"Batch size: {batch_size}")
    print(f"Number of batches: {n_batches}")
    print(f"To run all batches sequentially:")
    for i in range(1, n_batches + 1):
        start = (i - 1) * batch_size
        end = min(start + batch_size, n_total)
        print(f"  python -m python.run_batched --batch {i:02d}")
    print(f"\nAfter all batches: python -m python.run_batched --merge")


if __name__ == "__main__":
    main()
