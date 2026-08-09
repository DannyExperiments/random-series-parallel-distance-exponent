# Build status

```text
TEX_SOURCE_QA: PASS
TECTONIC_BINARY: PRESENT (0.16.9)
LOCAL_TEX_RESOURCE_BUNDLE: MISSING
CACHED_ONLY_COMPILE: BLOCKED
PINNED_PRIVATE_GITHUB_CI_BUILD: FAILED_NONMATHEMATICAL_OPERATOR_DECLARATIONS_REPAIRED
CURRENT_EXACT_SOURCE_RERUN: PENDING
PDF_COMPILED: NO
PDF_PAGE_COUNT: NOT_AVAILABLE
PDF_VISUAL_PREFLIGHT: NOT_RUN
```

The cached-only attempt stopped before parsing the manuscript because the
local Tectonic resource cache does not contain `tectonic-format-latex.tex`.
This is an environment/runtime blocker, not a TeX or mathematical failure.

The repository's pinned, read-only private GitHub Actions workflow reached TeX
and exposed two command-declaration typos.  Both were repaired without changing
any theorem, formula, hypothesis, or proof step.  The exact current source
awaits a clean hosted rerun.  No final PDF, build-pass badge, or visual-preflight
claim is authorized yet.
