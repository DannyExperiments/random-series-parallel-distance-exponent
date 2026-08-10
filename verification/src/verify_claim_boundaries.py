import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

required = {
    "README.md": [
        "p\\in(1/2,1)",
        "The identity",
        "belongs to prior work",
        "fresh hostile source-level audit",
        "No Lean or Aristotle badge is authorized",
        "10.5281/zenodo.21875135",
        "exact designated source",
        "visually inspected page by",
        "f5c3e0bb888a4e4b796b90729a6fc1cfa0581e96",
        "immutable Version",
    ],
    "STATUS.md": [
        "DOI_DEPOSITED",
        "POST_DOI_METADATA_CLOSURE",
        "PASS_HIGH_CONFIDENCE",
        "PRIORITY_AUDIT_PASS_QUALIFIED",
        "FORMALIZATION_NOT_ATTEMPTED",
        "MANUSCRIPT_PASS",
        "PUBLIC_TIMESTAMPED",
        "ALL_RIGHTS_RESERVED",
    ],
    "CLAIMS_EVIDENCE_MATRIX.md": [
        "False attribution; forbidden",
        "Not established",
        "Source QA and hostile source audit `PASS`",
        "passed visual preflight",
    ],
    "paper/BUILD_STATUS.md": [
        "TEX_SOURCE_QA: PASS",
        "PINNED_PRIVATE_GITHUB_CI_BUILD: FAILED_NONMATHEMATICAL_OPERATOR_DECLARATIONS_REPAIRED",
        "CURRENT_EXACT_SOURCE_RERUN: PASS",
        "PDF_COMPILED: YES",
        "PDF_VISUAL_PREFLIGHT: PASS",
        "PUBLIC_DEFAULT_BRANCH_PDF_STATUS: PASS",
        "PUBLIC_DEFAULT_BRANCH_BADGE_ELIGIBLE: YES",
        "PUBLIC_DEFAULT_BRANCH_BADGE_ANONYMOUS_TEST: PASS",
    ],
    "CITATION.cff": [
        "version: 1.0.0",
        "date-released: 2026-08-10",
        'doi: "10.5281/zenodo.21875135"',
        'name: "DannyExperiments"',
    ],
    "LICENSE_STATUS.md": [
        "No repository-wide reuse license is granted. All rights are reserved.",
    ],
    "release/HUMAN_RELEASE_CHECKLIST.md": [
        "Repository visibility changed to public and anonymously verified.",
        "passed both workflows on its exact PR head",
        "all rights reserved.",
    ],
    "release/RELEASE_NOTES_v1.0.0.md": [
        "Release notes for Version 1.0.0",
        "p\\in(1/2,1)",
        "immutable Version 1.0.0 tag and GitHub release",
    ],
    "release/DOI_DEPOSIT.md": [
        "10.5281/zenodo.21875135",
        "10.5281/zenodo.21875134",
        "f88c264981224c2e2b28478564e2b5db82668d4d",
        "All six files were anonymously downloaded",
    ],
}

for relative, needles in required.items():
    text = (ROOT / relative).read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text:
            raise SystemExit(f"missing required boundary in {relative}: {needle}")

readme = (ROOT / "README.md").read_text(encoding="utf-8")
allowed_badges = {
    "verify.yml": (
        "[![Verify public evidence](https://github.com/DannyExperiments/"
        "random-series-parallel-distance-exponent/actions/workflows/verify.yml/"
        "badge.svg?branch=main)](https://github.com/DannyExperiments/"
        "random-series-parallel-distance-exponent/actions/workflows/verify.yml)"
    ),
    "pdf.yml": (
        "[![PDF build](https://github.com/DannyExperiments/"
        "random-series-parallel-distance-exponent/actions/workflows/pdf.yml/"
        "badge.svg?branch=main)](https://github.com/DannyExperiments/"
        "random-series-parallel-distance-exponent/actions/workflows/pdf.yml)"
    ),
    "doi": (
        "[![DOI](https://zenodo.org/badge/DOI/10.5281/"
        "zenodo.21875135.svg)](https://doi.org/10.5281/zenodo.21875135)"
    ),
}


def verify_visible_readme_images(readme_text: str) -> None:
    uncommented = re.sub(r"<!--.*?-->", "", readme_text, flags=re.DOTALL)
    for workflow, badge in allowed_badges.items():
        if uncommented.count(badge) != 1:
            raise SystemExit(f"missing or duplicated authorized badge: {workflow}")

    # Enforce an exact allowlist of complete, visible badge tokens rather than
    # trying to recognize badge providers or filename conventions.  After the
    # three approved image-plus-target tokens are removed, any remaining
    # Markdown image opener catches inline, reference-style,
    # collapsed-reference, and shortcut images; any remaining HTML <img>
    # catches quoted or unquoted src forms.  HTML comments were removed above,
    # so dormant examples do not count as visible.
    unauthorized_image_surface = uncommented
    for badge in allowed_badges.values():
        unauthorized_image_surface = unauthorized_image_surface.replace(badge, "", 1)

    # Reject the opener even when it is preceded by backslashes.  In
    # CommonMark an even run of backslashes can leave the exclamation mark
    # active, so a one-character negative lookbehind is not a safe visibility
    # test.  This repository has no need to display image-syntax examples.
    if re.search(r"!\[", unauthorized_image_surface):
        raise SystemExit("README contains an unauthorized visible Markdown image token")
    if re.search(r"<img\b", unauthorized_image_surface, flags=re.IGNORECASE):
        raise SystemExit("README contains an unauthorized visible HTML <img> element")


verify_visible_readme_images(readme)

citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
if "date-released: 2026-08-10" not in citation:
    raise SystemExit("current-main CITATION.cff must record the actual release date")
if 'doi: "10.5281/zenodo.21875135"' not in citation:
    raise SystemExit("CITATION.cff must record the Version 1.0.0 DOI")


def digest(relative: str) -> str:
    return hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()


immutable_hashes = {
    "release/RELEASE_ASSET_SHA256SUMS.txt":
        "264254aa4e81f4cfaa2ee69f7aa0660d078231c8ced55d282bcff5033cd007be",
    "release/RELEASE_NOTES_v1.0.0.md":
        "827036f1ec850871672fa287f22e2f33d0ec75d60ba537a2ae6c40d5896f6a1d",
    "paper/manuscript.pdf":
        "b7756646862ca72ca317fbf50995f1827da84bc2debb4329b362c4180fb70964",
    "paper/manuscript.tex":
        "64c61b552b757c2f1c3aa9030056d09f7f742c0cb2e74aed176de70da57c4796",
    "paper/references.bib":
        "bbc56040625376099bb490813ed2a8adb0556e0466d5d6158713b91cdd85cd51",
    "proof/CANONICAL_REPAIRED_PROOF_V1.md":
        "19e1a565f0db943dea5ecb8b0e25eceb6a8c670c996265cd9a78b859d8666077",
}
for relative, expected in immutable_hashes.items():
    actual = digest(relative)
    if actual != expected:
        raise SystemExit(
            f"immutable mathematical/release artifact changed: {relative}: {actual}"
        )

forbidden = [
    "we prove delta(1/2)=0",
    "first proof of question 9.6",
    "definitively new",
    "fully lean verified",
    "human peer-reviewed",
    "public_candidate_pass_visibility_pending",
    "visibility_pending",
    "public_default_branch_badge_eligible: no",
    "public_default_branch_badge: withheld",
    "badges remain deliberately withheld",
    "public-default-branch badge remains closed",
]

for path in ROOT.rglob("*"):
    if not path.is_file() or path.name == "SHA256SUMS.txt":
        continue
    if path.resolve() == Path(__file__).resolve():
        continue
    if any(part.startswith(".") for part in path.relative_to(ROOT).parts):
        continue
    try:
        text = path.read_text(encoding="utf-8").lower()
    except UnicodeDecodeError:
        continue
    for phrase in forbidden:
        if phrase in text:
            raise SystemExit(f"forbidden overclaim in {path.relative_to(ROOT)}: {phrase}")

print("claim-boundary verification: PASS")
