#!/usr/bin/env python3
"""Build or check the deterministic sanitized public evidence bundle."""

from __future__ import annotations

import argparse
import hashlib
import io
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "release/EVIDENCE_BUNDLE.zip"
SIDECAR = ROOT / "release/EVIDENCE_BUNDLE.sha256"
PREFIX = "RW-10000069_PUBLIC_EVIDENCE_V1/"
FIXED_TIME = (1980, 1, 1, 0, 0, 0)

ALLOWLIST = (
    "README.md",
    "STATUS.md",
    "PROBLEM_AND_PROOF.md",
    "CITATION.cff",
    "AI_DISCLOSURE.md",
    "PROVENANCE.md",
    "CLAIMS_EVIDENCE_MATRIX.md",
    "REPRODUCIBILITY.md",
    "LICENSE_STATUS.md",
    "SECURITY.md",
    "proof/CANONICAL_REPAIRED_PROOF_V1.md",
    "audits/README.md",
    "audits/public_safe_reports/MATHEMATICAL_AUDIT_STATUS.md",
    "audits/public_safe_reports/PRIORITY_AUDIT_STATUS.md",
    "audits/public_safe_reports/PRIORITY_AUDIT_EXACT_RESULT_2026-08-09.md",
    "audits/public_safe_reports/PRIORITY_AUDIT_ARCHITECTURE_2026-08-09.md",
    "verification/README.md",
    "verification/src/verify_claim_boundaries.py",
    "formalization/README.md",
    "formalization/FORMALIZATION_FEASIBILITY.md",
    "formalization/DEPENDENCY_MAP.md",
    "formalization/THEOREM_SCOPE.md",
    "formalization/lean/README.md",
    "formalization/aristotle/ARISTOTLE_CORE_PROMPT.md",
    "formalization/aristotle/ARISTOTLE_SUBMISSION_RECEIPT.md",
    "paper/manuscript.tex",
    "paper/manuscript.pdf",
    "paper/references.bib",
    "paper/README.md",
    "paper/BUILD.md",
    "paper/BUILD_STATUS.md",
    "paper/BUILD_LOG.txt",
    "paper/PDF_PREFLIGHT.md",
    "paper/SOURCE_COMPARISON.md",
    "paper/SOURCE_QA.md",
    "paper/CLAIM_SCOPE_AND_LIMITATIONS.md",
    "paper/HOSTILE_MANUSCRIPT_AUDIT_PROMPT.md",
    "release/README.md",
    "release/BADGE_ACTIVATION.md",
    "release/DOI_DEPOSIT.md",
    "release/HUMAN_RELEASE_CHECKLIST.md",
    "release/RELEASE_ASSET_SHA256SUMS.txt",
    "release/RELEASE_NOTES_v1.0.0.md",
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def replay_readme() -> bytes:
    return b"""# Replay the public evidence bundle

This archive is a deterministic, sanitized evidence subset. It contains no raw
chat transcript, private receipt, local path, credential, or third-party source
PDF. After extraction, change into `RW-10000069_PUBLIC_EVIDENCE_V1` and run:

```bash
shasum -a 256 -c BUNDLE_SHA256SUMS.txt
python3 verification/src/verify_claim_boundaries.py
```

The checksum command verifies the exact archived bytes. The Python check audits
the theorem and status boundaries. Neither command substitutes for mathematical
review, peer review, or proof-assistant verification.
"""


def manifest(member_names: list[str]) -> bytes:
    lines = [
        "# Public evidence bundle manifest",
        "",
        "Bundle ID: `RW-10000069_PUBLIC_EVIDENCE_V1`.",
        "",
        "Every archived member is a regular file with a fixed ZIP timestamp and",
        "mode. `BUNDLE_SHA256SUMS.txt` hashes every member except itself.",
        "",
        "## Members",
        "",
    ]
    lines.extend(f"- `{name}`" for name in sorted(member_names))
    return ("\n".join(lines) + "\n").encode("utf-8")


def build_bytes() -> bytes:
    missing = [relative for relative in ALLOWLIST if not (ROOT / relative).is_file()]
    if missing:
        raise SystemExit("missing bundle members: " + ", ".join(missing))

    payloads = {relative: (ROOT / relative).read_bytes() for relative in ALLOWLIST}
    payloads["REPLAY_README.md"] = replay_readme()
    names = sorted([*payloads, "BUNDLE_MANIFEST.md", "BUNDLE_SHA256SUMS.txt"])
    payloads["BUNDLE_MANIFEST.md"] = manifest(names)
    payloads["BUNDLE_SHA256SUMS.txt"] = "".join(
        f"{sha256(payloads[name])}  {name}\n"
        for name in sorted(payloads)
    ).encode("utf-8")

    buffer = io.BytesIO()
    with zipfile.ZipFile(
        buffer, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for name in sorted(payloads):
            info = zipfile.ZipInfo(PREFIX + name, FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, payloads[name])
    return buffer.getvalue()


def sidecar_text(bundle: bytes) -> str:
    return f"{sha256(bundle)}  EVIDENCE_BUNDLE.zip\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    bundle = build_bytes()
    sidecar = sidecar_text(bundle)
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_bytes() != bundle:
            raise SystemExit("EVIDENCE_BUNDLE_OUT_OF_DATE")
        if not SIDECAR.is_file() or SIDECAR.read_text(encoding="utf-8") != sidecar:
            raise SystemExit("EVIDENCE_BUNDLE_SIDECAR_OUT_OF_DATE")
        print("DETERMINISTIC_EVIDENCE_BUNDLE: PASS")
        return

    OUTPUT.write_bytes(bundle)
    SIDECAR.write_text(sidecar, encoding="utf-8")
    print(f"WROTE {OUTPUT.relative_to(ROOT)}")
    print(f"SHA256 {sha256(bundle)}")


if __name__ == "__main__":
    main()
