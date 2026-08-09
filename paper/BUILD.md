# Paper build contract

Current designated source:

```text
paper/manuscript.tex
paper/references.bib
```

Use `amsart`, `a4paper`, and one-inch margins. Use no author entry until the
human approves authorship. Keep the abstract to at most six sentences and
make the actual problem and answer clear on page one.

The intended offline build command, once the required Tectonic resource bundle
is available, is:

```bash
cd paper
tectonic --only-cached --keep-logs --keep-intermediates manuscript.tex
```

The local cached-only attempt failed before manuscript parsing because
`tectonic-format-latex.tex` is absent from the cache. Fetching the official
resource bundle has not been authorized and was not attempted. A future clean
build must record the exact tool and resource versions, produce zero unresolved
citations/references and zero layout warnings, pass page-by-page visual
inspection, and match the audited scope. No PDF badge is authorized before the
workflow passes on the public default branch.
