# Badge activation record

The README in this local closure tree displays exactly two badges:

- `Verify public evidence` for `.github/workflows/verify.yml`; and
- `PDF build` for `.github/workflows/pdf.yml`.

Activation gate: `PASS` for public-`main` commit
`d79230cdb87d1438c97281d0c940f8e1a352642c`.

- `Verify public evidence` run `31295518511`: `PASS`.
- `PDF build` run `31295518480`: `PASS`.
- Anonymous badge-image test: `PASS` for both badges.
- Anonymous target-page test: `PASS` for both workflow links.
- Branch binding: explicit `branch=main` in each badge image URL.

This local metadata/evidence closure is a new tree. After it is merged, both
workflows and both anonymous badge tests must be repeated before the closure
commit is described as public-main-CI-passed.

No Lean or Aristotle badge is authorized. The repository contains only a
formalization-feasibility report and request packet; no scope-matched theorem
has been rebuilt and kernel checked. No DOI badge is authorized until a DOI
resolves to hash-verified immutable release assets.
