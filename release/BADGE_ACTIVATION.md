# Badge activation record

The README in this local closure tree displays exactly two badges:

- `Verify public evidence` for `.github/workflows/verify.yml`; and
- `PDF build` for `.github/workflows/pdf.yml`.

Activation gate: `PASS` for the exact pre-release public-`main` base commit
`f5c3e0bb888a4e4b796b90729a6fc1cfa0581e96`.

- `Verify public evidence` run `31302269010`: `PASS`.
- `PDF build` run `31302269014`: `PASS`.
- Anonymous badge-image test: `PASS` for both badges.
- Anonymous target-page test: `PASS` for both workflow links.
- Branch binding: explicit `branch=main` in each badge image URL.

The metadata-only release repair must pass both workflows on its exact PR head
before merge and tagging. The public `main` badge images and targets must be
rechecked after that protected merge.

No Lean or Aristotle badge is authorized. The repository contains only a
formalization-feasibility report and request packet; no scope-matched theorem
has been rebuilt and kernel checked. No DOI badge is authorized until a DOI
resolves to hash-verified immutable release assets.
