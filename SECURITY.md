# Security Policy

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them privately using one of the following methods:

### Preferred: GitHub Security Advisories

1. Go to the [Security Advisories](https://github.com/wild8highlander/ab-cloud-research/security/advisories) page
2. Click **"New advisory"**
3. Fill in the details of the vulnerability
4. Submit as **"Private"** — this creates a confidential channel with the maintainer

### Alternative: Email

Send a detailed report to [aslan08_05@mail.ru](mailto:aslan08_05@mail.ru) with the subject line:

```
[SECURITY] ab-cloud-research: <short summary>
```

Please include:

- A description of the issue and its impact;
- Step-by-step reproduction instructions (workflow file, script, command);
- Any logs or artifacts that help reproduce the problem.

## Scope

This repository is a research codebase (Julia suite, Python 3D lab,
10-language verification scripts). Security-relevant surfaces include:

- **GitHub Actions workflows** (`.github/workflows/*.yml`) — e.g. script
  injection through untrusted input, pull_request_target misuse;
- **Verification scripts** executed locally (`verification/`, `lab-3d/`) —
  e.g. path handling of user-supplied ζ-zero data files;
- ** MkDocs site build** (`docs/`, `mkdocs.yml`).

## What is in scope vs out of scope

| In scope | Out of scope |
|---|---|
| Workflow injection / privilege escalation | "Scientific correctness" of the numerics (use Issues) |
| Malicious dependency changes (Dependabot watches these) | Social engineering of the Author |
| Scripts executing unintended code on local runs | Reports about third-party services (Zenodo, shields.io) |

## Supported versions

| Version | Supported |
|---|---|
| 1.0.x | ✅ |
| < 1.0 | ❌ (pre-release history lives in the parent repository) |

## Response timeline

- Acknowledgement: within 7 days
- Triage and fix plan: within 30 days
- Credit is given to reporters in the release notes (unless anonymity is requested).
