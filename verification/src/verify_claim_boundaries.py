from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

required = {
    "README.md": [
        "p\\in(1/2,1)",
        "The identity",
        "belongs to prior work",
        "fresh hostile source-level audit",
        "No Lean badge is authorized",
        "exact designated source",
        "visually inspected page by page",
    ],
    "STATUS.md": [
        "PUBLIC_CANDIDATE_PASS_VISIBILITY_PENDING",
        "PASS_HIGH_CONFIDENCE",
        "PRIORITY_AUDIT_PASS_QUALIFIED",
        "FORMALIZATION_NOT_ATTEMPTED",
        "MANUSCRIPT_PASS_PRIVATE",
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
        "PUBLIC_DEFAULT_BRANCH_BADGE_ELIGIBLE: NO",
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
        "Visibility changed to public and anonymously verified.",
        "all rights reserved.",
    ],
    "release/RELEASE_NOTES_v1.0.0.md": [
        "Release notes for Version 1.0.0",
        "p\\in(1/2,1)",
    ],
}

for relative, needles in required.items():
    text = (ROOT / relative).read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text:
            raise SystemExit(f"missing required boundary in {relative}: {needle}")

forbidden = [
    "we prove delta(1/2)=0",
    "first proof of question 9.6",
    "definitively new",
    "fully lean verified",
    "human peer-reviewed",
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
