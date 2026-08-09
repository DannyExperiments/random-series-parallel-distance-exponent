# Manuscript lane

`manuscript.tex` is the designated private manuscript candidate. It follows
the PRZ presentation standard: `amsart`, A4 paper, one-inch margins, no author
entry, and a five-sentence abstract. Its first page states the original
question, the new interior scope `p in (1/2,1)`, the direct characterization,
the prior credit for `p=1/2`, and the elementary `p=1` endpoint.

Source-level formatting, scope, and privacy QA pass. The pinned private-branch
workflow built the exact current source; `manuscript.pdf` is the retrieved,
frozen four-page A4 artifact and passed page-by-page visual preflight. The
local cached-only Tectonic attempt remains documented as an environment-only
failure. Public-default-branch CI and anonymous badge testing remain separate
release gates.

Read `CLAIM_SCOPE_AND_LIMITATIONS.md`, `SOURCE_COMPARISON.md`, `SOURCE_QA.md`,
and `BUILD_STATUS.md` before treating the source as a release candidate. The
frozen PDF is beside the exact TeX source and its preflight is recorded in
`PDF_PREFLIGHT.md`.
