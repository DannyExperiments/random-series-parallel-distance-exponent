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
        "exact designated source",
        "visually inspected page by",
        "f5c3e0bb888a4e4b796b90729a6fc1cfa0581e96",
        "immutable Version",
    ],
    "STATUS.md": [
        "PUBLIC_MAIN_CI_PASS_RELEASE_PENDING",
        "PRE_RELEASE_METADATA_REPAIR_RUNNING",
        "PASS_HIGH_CONFIDENCE",
        "PRIORITY_AUDIT_PASS_QUALIFIED",
        "FORMALIZATION_NOT_ATTEMPTED",
        "MANUSCRIPT_PASS",
        "IMMUTABLE_RELEASE_PENDING",
        "DOI_PENDING",
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
        "date-released: 2026-08-09",
        'name: "DannyExperiments"',
    ],
    "LICENSE_STATUS.md": [
        "No repository-wide reuse license is granted. All rights are reserved.",
    ],
    "release/HUMAN_RELEASE_CHECKLIST.md": [
        "Repository visibility changed to public and anonymously verified.",
        "passes both workflows on its exact PR head",
        "all rights reserved.",
    ],
    "release/RELEASE_NOTES_v1.0.0.md": [
        "Release notes for Version 1.0.0",
        "p\\in(1/2,1)",
        "immutable Version 1.0.0 tag and GitHub release",
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
}


def verify_visible_readme_images(readme_text: str) -> None:
    uncommented = re.sub(r"<!--.*?-->", "", readme_text, flags=re.DOTALL)
    for workflow, badge in allowed_badges.items():
        if uncommented.count(badge) != 1:
            raise SystemExit(f"missing or duplicated authorized badge: {workflow}")

    # Enforce an exact allowlist of complete, visible badge tokens rather than
    # trying to recognize badge providers or filename conventions.  After the
    # two approved image-plus-target tokens are removed, any remaining
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
if "date-released: 2026-08-09" not in citation:
    raise SystemExit("Version 1.0.0 CITATION.cff must record the release date")

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
