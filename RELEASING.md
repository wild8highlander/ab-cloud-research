# Release Guide — ab-cloud-research

This document describes the process for creating releases of the AB-Cloud Research repository. All releases follow [Semantic Versioning](https://semver.org) and are automatically deposited to Zenodo for DOI assignment.

---

## Versioning Scheme

We follow **Semantic Versioning 2.0.0** with research-specific extensions:

```
MAJOR.MINOR.PATCH

MAJOR — Fundamental change to research results or proof methodology
MINOR — New verification, new proof, or significant numerical result
PATCH — Bug fix, documentation update, or minor improvement
```

### Research-Specific Interpretation

| Change Type | Version Bump | Example |
|-------------|-------------|---------|
| New mathematical result | MINOR | Additional theorem about NSE |
| New formal proof | MINOR | Lean 4 proof of AB-Cloud property |
| New verification language | MINOR | Add Idris verification |
| Fix to proof/computation | PATCH | Correct boundary condition in NSE |
| Refinement of constants | PATCH | Higher-precision computation of *b* |
| Refutation/retraction | MAJOR | Withdrawal of a claimed result |

---

## Pre-Release Checklist

Before creating a release, verify:

- [ ] **All CI workflows pass** on `main` branch
- [ ] **CHANGELOG.md** is updated with all changes since last release
- [ ] **CITATION.cff** `version` and `date-released` are updated
- [ ] **.zenodo.json** `version` and `publication_date` are updated
- [ ] **pyproject.toml** version is updated
- [ ] **Documentation** is built and deployed successfully
- [ ] **All verifications pass**: `make verify-all && make verify-extended`
- [ ] **No security vulnerabilities** in CodeQL or Dependabot alerts
- [ ] **ORCID** is correct in CITATION.cff and .zenodo.json
- [ ] **Zenodo metadata** is complete and accurate

---

## Release Process

### 1. Update Version and Metadata

```bash
# Set the new version
NEW_VERSION="1.0.0"

# Update CITATION.cff
sed -i "s/^version: .*/version: \"${NEW_VERSION}\"/" CITATION.cff
sed -i "s/^date-released: .*/date-released: \"$(date +%Y-%m-%d)\"/" CITATION.cff

# Update .zenodo.json
jq --arg v "$NEW_VERSION" '.version = $v' .zenodo.json > .zenodo.json.tmp && mv .zenodo.json.tmp .zenodo.json
jq --arg d "$(date +%Y-%m-%d)" '.publication_date = $d' .zenodo.json > .zenodo.json.tmp && mv .zenodo.json.tmp .zenodo.json

# Update pyproject.toml
sed -i "s/^version = .*/version = \"${NEW_VERSION}\"/" pyproject.toml
```

### 2. Update CHANGELOG.md

Move items from `[Unreleased]` to the new version section:

```markdown
## [1.0.0] - 2026-08-20

### Added
- New formal proof of AB-Cloud spectral gap in Lean 4
- Higher-precision computation of correction b (50 digits)

### Changed
- Improved convergence rate in NSE time-stepper

### Fixed
- Corrected CMake build flags for Rust verification
```

### 3. Commit and Tag

```bash
git add -A
git commit -m "release: v${NEW_VERSION}"
git tag -a "v${NEW_VERSION}" -m "Release v${NEW_VERSION}"
git push origin main --follow-tags
```

### 4. Create GitHub Release

The **Release Drafter** workflow automatically creates a draft release. Alternatively, create manually:

1. Go to [Releases](https://github.com/wild8highlander/ab-cloud-research/releases/new)
2. Select the tag `v${NEW_VERSION}`
3. Title: `v${NEW_VERSION}`
4. Copy changelog entries as description
5. Attach any release artifacts (compiled docs, verification reports)
6. Publish the release

### 5. Zenodo DOI

When a GitHub release is published, the **Zenodo workflow** automatically:

1. Archives the repository snapshot on Zenodo
2. Assigns a new DOI (or version DOI for existing concept)
3. Updates the Zenodo badge in the README

**Current Zenodo DOIs:**

| Type | DOI | URL |
|------|-----|-----|
| **Version DOI** (v1.0.0) | `10.5281/zenodo.21825394` | https://doi.org/10.5281/zenodo.21825394 |
| **Concept DOI** (all versions) | `10.5281/zenodo.21825393` | https://doi.org/10.5281/zenodo.21825393 |

For future releases, Zenodo will automatically assign a new version DOI under the same concept DOI.

---

## Post-Release

- [ ] **Verify Zenodo deposit** — Check https://zenodo.org/records/21825394
- [ ] **Update DOI badges** — Current version DOI: `10.5281/zenodo.21825394`, concept DOI: `10.5281/zenodo.21825393`
- [ ] **Announce** — Post to relevant mailing lists, forums, or social media
- [ ] **Update documentation** — Ensure docs site reflects the new version
- [ ] **Close milestone** — Close the corresponding GitHub milestone

---

## Emergency Release (Hotfix)

For critical fixes (e.g., security vulnerability, incorrect proof):

```bash
# Create hotfix branch from the release tag
git checkout -b hotfix/v1.3.1 v1.0.0

# Apply the fix
# ... edit files ...

# Commit, tag, and push
git commit -m "fix(security): patch critical vulnerability"
git tag -a "v1.3.1" -m "Hotfix v1.3.1"
git push origin hotfix/v1.3.1 --follow-tags

# Merge back to main
git checkout main
git merge hotfix/v1.3.1
git push origin main
```
