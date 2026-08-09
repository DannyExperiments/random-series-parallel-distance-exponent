# Release assets

This directory contains deterministic public-safe evidence and the exact
Version 1.0.0 release plan. It is not itself a published release.

The planned immutable release asset set is:

- `paper/manuscript.pdf` — exact frozen four-page PDF;
- `paper/manuscript.tex` — designated source;
- `SHA256SUMS.txt` — complete repository ledger; and
- `release/EVIDENCE_BUNDLE.zip` — deterministic sanitized evidence subset.

`EVIDENCE_BUNDLE.sha256` records the archive hash.
`RELEASE_ASSET_SHA256SUMS.txt` records the PDF, TeX, and evidence-bundle hashes.
The builder synthesizes an internal bundle manifest, checksum ledger, and
replay README and is checked by the repository verification workflow.

The mathematical, priority, manuscript, formalization-status, privacy, and
deterministic-replay gates are complete. Exact private-main merge, public
visibility, public-main CI, badge activation, branch-protection confirmation,
the immutable release, DOI deposit, and any external notice remain separate
steps.
