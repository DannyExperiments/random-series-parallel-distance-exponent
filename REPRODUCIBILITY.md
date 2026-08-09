# Reproducibility

The default repository check is offline and installs nothing:

```bash
bash scripts/verify_public_repo.sh
```

It verifies the checksum ledger, required files, claim-boundary language, and
the absence of common private-path, raw-chat, credential, key, and email
patterns. It establishes repository integrity, not mathematical correctness.

There is no load-bearing computation. The mathematical object to inspect is
the symbolic draft in `proof/CANONICAL_REPAIRED_PROOF_V1.md`.

The designated private manuscript source is `paper/manuscript.tex`, and its
source-level QA passes. No PDF is present. The cached-only Tectonic attempt is
recorded in `paper/BUILD_LOG.txt`; it stopped before TeX parsing because the
resource cache is incomplete. `paper/BUILD.md` and `.github/workflows/pdf.yml`
define the future clean-build gate after exact resource-fetch approval.

No Lean build is currently available. The files in `formalization/` define a
future partial target; they do not contain or claim a proof.
