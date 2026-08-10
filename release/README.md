# Release record

This directory records the immutable Version 1.0.0 release, its frozen asset
ledger, the published DOI deposit, and the deterministic current-`main` public
evidence bundle.

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

Version 1.0.0 is published at
<https://github.com/DannyExperiments/random-series-parallel-distance-exponent/releases/tag/v1.0.0>.
Its six assets are archived at version DOI
<https://doi.org/10.5281/zenodo.21875135>; the collection concept DOI is
<https://doi.org/10.5281/zenodo.21875134>. All six archived files match the
immutable GitHub assets byte for byte. See [`DOI_DEPOSIT.md`](DOI_DEPOSIT.md).

The generic `EVIDENCE_BUNDLE.zip` on current `main` is regenerated when public
metadata changes. It does not replace the immutable Version 1.0.0 evidence
asset, whose exact hash remains frozen in `RELEASE_ASSET_SHA256SUMS.txt` and at
the DOI record. The frozen Version 1.0.0 release notes retain their
pre-publication wording as part of that archived evidence. Only the external
problem-page notice remains pending.
