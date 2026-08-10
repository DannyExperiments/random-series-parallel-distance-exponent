# Public release manifest

Generated from the sanitized allowlist. Raw/private evidence is excluded.

- `.gitattributes`
- `.github/workflows/pdf.yml`
- `.github/workflows/publish-v1.0.0.yml`
- `.github/workflows/verify.yml`
- `.gitignore`
- `AI_DISCLOSURE.md`
- `CITATION.cff`
- `CLAIMS_EVIDENCE_MATRIX.md`
- `CONTRIBUTING.md`
- `LICENSE_STATUS.md`
- `MANIFEST.md`
- `PROBLEM_AND_PROOF.md`
- `PROVENANCE.md`
- `README.md`
- `REPRODUCIBILITY.md`
- `SECURITY.md`
- `SHA256SUMS.txt`
- `STATUS.md`
- `audits/README.md`
- `audits/public_safe_reports/MATHEMATICAL_AUDIT_STATUS.md`
- `audits/public_safe_reports/PRIORITY_AUDIT_ARCHITECTURE_2026-08-09.md`
- `audits/public_safe_reports/PRIORITY_AUDIT_EXACT_RESULT_2026-08-09.md`
- `audits/public_safe_reports/PRIORITY_AUDIT_STATUS.md`
- `formalization/DEPENDENCY_MAP.md`
- `formalization/FORMALIZATION_FEASIBILITY.md`
- `formalization/README.md`
- `formalization/THEOREM_SCOPE.md`
- `formalization/aristotle/ARISTOTLE_CORE_PROMPT.md`
- `formalization/aristotle/ARISTOTLE_SUBMISSION_RECEIPT.md`
- `formalization/lean/README.md`
- `paper/BUILD.md`
- `paper/BUILD_LOG.txt`
- `paper/BUILD_STATUS.md`
- `paper/CLAIM_SCOPE_AND_LIMITATIONS.md`
- `paper/HOSTILE_MANUSCRIPT_AUDIT_PROMPT.md`
- `paper/PDF_PREFLIGHT.md`
- `paper/README.md`
- `paper/SOURCE_COMPARISON.md`
- `paper/SOURCE_QA.md`
- `paper/manuscript.tex`
- `paper/manuscript.pdf`
- `paper/references.bib`
- `proof/CANONICAL_REPAIRED_PROOF_V1.md`
- `release/BADGE_ACTIVATION.md`
- `release/HUMAN_RELEASE_CHECKLIST.md`
- `release/README.md`
- `release/EVIDENCE_BUNDLE.sha256`
- `release/EVIDENCE_BUNDLE.zip`
- `release/RELEASE_ASSET_SHA256SUMS.txt`
- `release/RELEASE_NOTES_v1.0.0.md`
- `scripts/build_evidence_bundle.py`
- `scripts/scan_public_tree.sh`
- `scripts/update_hashes.py`
- `scripts/verify_public_repo.sh`
- `verification/README.md`
- `verification/logs/README.md`
- `verification/src/verify_claim_boundaries.py`

`SHA256SUMS.txt` hashes every regular file except itself. The manuscript TeX is
the designated release source and has source QA and hostile source-level audit
`PASS`. The exact private-branch build and frozen four-page PDF passed visual
preflight. The same source passed the public-default-branch PDF workflow, and
the verify and PDF badges were activated after anonymous testing. The release
workflow requires both final-`main` checks at the exact tag target, publishes
only the allowlisted hash-checked assets, and verifies the immutable release,
tag target, and re-downloaded assets. The immutable release and DOI remain
pending until that workflow completes.
