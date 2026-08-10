# Build status

```text
TEX_SOURCE_QA: PASS
TECTONIC_BINARY: PRESENT (0.16.9)
LOCAL_TEX_RESOURCE_BUNDLE: MISSING
CACHED_ONLY_COMPILE: BLOCKED
PINNED_PRIVATE_GITHUB_CI_BUILD: FAILED_NONMATHEMATICAL_OPERATOR_DECLARATIONS_REPAIRED
FIRST_REPAIRED_PRIVATE_CI_BUILD: PASS
FIRST_REPAIRED_PRIVATE_CI_RUN: 31290444831
VISUAL_LAYOUT_REPAIR: EQUATIONS_11_AND_12_SPLIT_WITHOUT_MATHEMATICAL_CHANGE
CURRENT_EXACT_SOURCE_RERUN: PASS
CURRENT_EXACT_SOURCE_COMMIT: e8792f6c110975c54d9a2baf6af4813393060c0c
CURRENT_EXACT_SOURCE_RUN: 31290623765
PDF_COMPILED: YES
PDF_SHA256: b7756646862ca72ca317fbf50995f1827da84bc2debb4329b362c4180fb70964
PDF_PAGE_COUNT: 4
PDF_PAGE_SIZE: A4
PDF_VISUAL_PREFLIGHT: PASS
PUBLIC_DEFAULT_BRANCH_COMMIT: d79230cdb87d1438c97281d0c940f8e1a352642c
PUBLIC_DEFAULT_BRANCH_PDF_RUN: 31295518480
PUBLIC_DEFAULT_BRANCH_PDF_JOB: Rebuild manuscript PDF
PUBLIC_DEFAULT_BRANCH_PDF_STATUS: PASS
PUBLIC_DEFAULT_BRANCH_BADGE_ELIGIBLE: YES
PUBLIC_DEFAULT_BRANCH_BADGE_ANONYMOUS_TEST: PASS
IMMUTABLE_RELEASE_TAG: v1.0.0
IMMUTABLE_RELEASE_COMMIT: f88c264981224c2e2b28478564e2b5db82668d4d
IMMUTABLE_RELEASE_PUBLISHED_AT: 2026-08-10T14:42:50Z
VERSION_DOI: 10.5281/zenodo.21875135
DOI_FILE_PARITY: PASS_ALL_6_ASSETS
```

The cached-only attempt stopped before parsing the manuscript because the
local Tectonic resource cache does not contain `tectonic-format-latex.tex`.
This is an environment/runtime blocker, not a TeX or mathematical failure.

The repository's pinned, read-only private GitHub Actions workflow first exposed
two command-declaration typos.  Both were repaired without changing any
theorem, formula, hypothesis, or proof step.  The repaired source then built
cleanly, after which page-by-page inspection motivated one nonmathematical
display-spacing repair. The exact current source then passed the hosted rerun.
Its four-page A4 artifact was retrieved, frozen, and inspected page by page;
no clipping, overlap, malformed display, or unreadable glyph was found. The
unchanged source later passed the public-default-branch workflow at the commit
and run recorded above, after which the PDF badge image and target were tested
anonymously. The immutable Version 1.0.0 PDF was subsequently archived at the
version DOI and matched byte for byte. This post-DOI update changes metadata
only and does not modify the manuscript or frozen PDF.
