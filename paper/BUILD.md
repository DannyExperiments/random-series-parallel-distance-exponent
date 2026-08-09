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
`tectonic-format-latex.tex` is absent from the cache. No local resource bundle
was fetched. The pinned GitHub Actions workflow supplied the clean build gate.
The exact current source passed private-branch run `31290623765`; its PDF has
been frozen and inspected as recorded in `PDF_PREFLIGHT.md`. No PDF badge is
authorized before the workflow passes on the public default branch.
