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
PUBLIC_DEFAULT_BRANCH_BADGE_ELIGIBLE: NO
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
public PDF badge remains unauthorized until the workflow passes on the public
default branch.
