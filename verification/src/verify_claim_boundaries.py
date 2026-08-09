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
        "d79230cdb87d1438c97281d0c940f8e1a352642c",
        "immutable Version",
    ],
    "STATUS.md": [
        "PUBLIC_CANDIDATE_RUNNING",
        "PUBLIC_MAIN_CI_PASS_METADATA_CLOSURE_PENDING",
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
        'name: "DannyExperiments"',
    ],
    "LICENSE_STATUS.md": [
        "No repository-wide reuse license is granted. All rights are reserved.",
    ],
    "release/HUMAN_RELEASE_CHECKLIST.md": [
        "Repository visibility changed to public and anonymously verified.",
        "both workflows re-pass on its exact public-`main` commit",
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
uncommented_readme = re.sub(r"<!--.*?-->", "", readme, flags=re.DOTALL)
badge_lines = [
    line for line in uncommented_readme.splitlines() if "badge.svg" in line
]
if len(badge_lines) != 2:
    raise SystemExit(f"expected exactly two visible README badges, found {len(badge_lines)}")
for workflow in ("verify.yml", "pdf.yml"):
    expected = f"actions/workflows/{workflow}/badge.svg?branch=main"
    target = f"actions/workflows/{workflow})"
    if not any(expected in line and target in line for line in badge_lines):
        raise SystemExit(f"missing visible public-main badge and target: {workflow}")
if any(
    token in line.lower()
    for line in badge_lines
    for token in ("lean", "aristotle", "doi")
):
    raise SystemExit("unauthorized Lean, Aristotle, or DOI badge displayed")

citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
if "date-released:" in citation:
    raise SystemExit("pre-release CITATION.cff must not claim a release date")

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
