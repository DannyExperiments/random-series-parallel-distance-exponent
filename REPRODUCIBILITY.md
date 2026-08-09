# Reproducibility

The default repository check is offline and installs nothing:

```bash
bash scripts/verify_public_repo.sh
```

It verifies the checksum ledger, required files, claim-boundary language, and
the absence of common private-path, raw-chat, credential, key, and email
patterns. It establishes repository integrity, not mathematical correctness.

The same command checks that `release/EVIDENCE_BUNDLE.zip`, its sidecar, and
the release-asset ledger are byte-for-byte reproducible. To check that layer
directly, run:

```bash
python3 -B scripts/build_evidence_bundle.py --check
```

The archive contains an internal manifest, SHA-256 ledger, and replay README.
It is a public-safe subset; raw audit transcripts and private receipts remain
outside the repository.

There is no load-bearing computation. The mathematical object to inspect is
the symbolic draft in `proof/CANONICAL_REPAIRED_PROOF_V1.md`.

The designated source is `paper/manuscript.tex`. The pinned private-branch
workflow built the exact source successfully in run `31290623765`; the same
source then passed the public-`main` PDF workflow in run `31295518480` at
commit `d79230cdb87d1438c97281d0c940f8e1a352642c`. The retrieved private-branch
artifact was frozen as `paper/manuscript.pdf` (SHA-256
`b7756646862ca72ca317fbf50995f1827da84bc2debb4329b362c4180fb70964`),
text-scanned, and inspected page by page; see `paper/PDF_PREFLIGHT.md`. This
public-default-branch pass authorized the displayed PDF badge, whose image and
target were anonymously tested. The present local metadata/evidence closure
must receive its own remote checks after a later push and merge.

No Lean build is currently available. The files in `formalization/` define a
future partial target; they do not contain or claim a proof.
