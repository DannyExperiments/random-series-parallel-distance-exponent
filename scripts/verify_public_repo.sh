#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$repo_root"

required=(
  README.md STATUS.md PROBLEM_AND_PROOF.md CITATION.cff AI_DISCLOSURE.md
  PROVENANCE.md CLAIMS_EVIDENCE_MATRIX.md REPRODUCIBILITY.md MANIFEST.md
  SHA256SUMS.txt LICENSE_STATUS.md SECURITY.md CONTRIBUTING.md
  proof/CANONICAL_REPAIRED_PROOF_V1.md
  formalization/FORMALIZATION_FEASIBILITY.md
  paper/manuscript.tex paper/references.bib
  paper/CLAIM_SCOPE_AND_LIMITATIONS.md paper/SOURCE_COMPARISON.md
  paper/HOSTILE_MANUSCRIPT_AUDIT_PROMPT.md paper/BUILD.md
  paper/BUILD_STATUS.md paper/BUILD_LOG.txt paper/SOURCE_QA.md
  paper/PDF_PREFLIGHT.md paper/manuscript.pdf
  audits/public_safe_reports/PRIORITY_AUDIT_EXACT_RESULT_2026-08-09.md
  audits/public_safe_reports/PRIORITY_AUDIT_ARCHITECTURE_2026-08-09.md
  scripts/build_evidence_bundle.py scripts/update_hashes.py
  release/EVIDENCE_BUNDLE.zip release/EVIDENCE_BUNDLE.sha256
  release/RELEASE_ASSET_SHA256SUMS.txt
  release/BADGE_ACTIVATION.md release/HUMAN_RELEASE_CHECKLIST.md
  release/RELEASE_NOTES_v1.0.0.md
)

for path in "${required[@]}"; do
  test -f "$path" || { echo "missing required file: $path" >&2; exit 1; }
done

if find . -type l -not -path './.git/*' -print -quit | grep -q .; then
  echo "public repository verification: FAIL symlink present" >&2
  exit 1
fi
if find . -type f -not -path './.git/*' \( -path '*/__pycache__/*' -o -name '*.pyc' -o -name '*.pyo' \) -print -quit | grep -q .; then
  echo "public repository verification: FAIL generated Python cache present" >&2
  exit 1
fi

expected_inventory="$(mktemp)"
ledger_inventory="$(mktemp)"
find . -type f -not -path './.git/*' -not -name 'SHA256SUMS.txt' -print \
  | sed 's#^\./##' | LC_ALL=C sort > "$expected_inventory"
cut -c 67- SHA256SUMS.txt | LC_ALL=C sort > "$ledger_inventory"
if ! cmp -s "$expected_inventory" "$ledger_inventory"; then
  echo "public repository verification: FAIL checksum inventory mismatch" >&2
  diff -u "$expected_inventory" "$ledger_inventory" >&2 || true
  exit 1
fi

shasum -a 256 -c SHA256SUMS.txt
python3 -B scripts/build_evidence_bundle.py --check
python3 verification/src/verify_claim_boundaries.py
bash scripts/scan_public_tree.sh

echo "public repository verification: PASS"
