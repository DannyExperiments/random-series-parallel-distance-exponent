# Verification

`verification/src/verify_claim_boundaries.py` checks required status language
and rejects common overclaims. `scripts/scan_public_tree.sh` checks for common
private-data and credential patterns. `scripts/verify_public_repo.sh` runs both
after validating `SHA256SUMS.txt`.

These checks prove integrity and claim hygiene only.
