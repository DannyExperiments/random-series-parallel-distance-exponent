# Release assets

This directory contains deterministic public-safe evidence and the exact
Version 1.0.0 release-staging plan. The repository is public and its two
default-branch workflows passed at commit
`d79230cdb87d1438c97281d0c940f8e1a352642c`, but no immutable tag or GitHub
release exists yet.

The five payloads named and hashed by `RELEASE_ASSET_SHA256SUMS.txt` are:

- `paper/manuscript.pdf`, staged as
  `random-series-parallel-distance-exponent-v1.0.0.pdf`;
- `paper/manuscript.tex`, staged as
  `random-series-parallel-distance-exponent-v1.0.0.tex`;
- `paper/references.bib`, staged as `references.bib`;
- `CITATION.cff`, staged as `CITATION.cff`; and
- `release/EVIDENCE_BUNDLE.zip`, staged as
  `random-series-parallel-distance-exponent-public-evidence-v1.0.0.zip`.

`EVIDENCE_BUNDLE.sha256` records the archive hash.
`RELEASE_ASSET_SHA256SUMS.txt` records all five payload hashes.
The builder synthesizes an internal bundle manifest, checksum ledger, and
replay README and is checked by the repository verification workflow.

The mathematical, priority, manuscript, formalization-status, privacy, and
deterministic-replay gates are complete. Public visibility, public-main CI for
the pre-closure tree, and badge activation are recorded as passed. CI for the
new closure tree, branch-protection confirmation, the immutable release,
post-publication asset re-download verification, DOI deposit, and any external
notice remain separate steps.
