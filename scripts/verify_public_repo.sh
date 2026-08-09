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
)

for path in "${required[@]}"; do
  test -f "$path" || { echo "missing required file: $path" >&2; exit 1; }
done

shasum -a 256 -c SHA256SUMS.txt
python3 verification/src/verify_claim_boundaries.py
bash scripts/scan_public_tree.sh

echo "public repository verification: PASS"
