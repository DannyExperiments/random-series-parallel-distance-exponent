# Badge activation record

The README in this post-DOI closure tree displays exactly three badges:

- `Verify public evidence` for `.github/workflows/verify.yml`; and
- `PDF build` for `.github/workflows/pdf.yml`; and
- `DOI` for the immutable Version 1.0.0 archive.

Activation gate: `PASS` for the exact pre-release public-`main` base commit
`f5c3e0bb888a4e4b796b90729a6fc1cfa0581e96`.

- `Verify public evidence` run `31302269010`: `PASS`.
- `PDF build` run `31302269014`: `PASS`.
- Anonymous badge-image test: `PASS` for both badges.
- Anonymous target-page test: `PASS` for both workflow links.
- Branch binding: explicit `branch=main` in each badge image URL.

The post-DOI metadata-only PR must pass both workflows on its exact head before
protected merge. The public `main` badge images and targets must be rechecked
after that merge.

The DOI badge, version DOI `10.5281/zenodo.21875135`, concept DOI
`10.5281/zenodo.21875134`, and Zenodo record returned HTTP 200 anonymously.
All six Zenodo files match the immutable GitHub release assets. No Lean or
Aristotle badge is authorized: no scope-matched theorem has been rebuilt and
kernel checked.
