# Badge activation

The README contains two badges inside an HTML comment:

- `Verify public evidence` for `.github/workflows/verify.yml`; and
- `PDF build` for `.github/workflows/pdf.yml`.

Activate them only after both workflows pass on public `main`. Then inspect the
repository from an anonymous browser session and click-test both the badge
image and target link. The URLs must report the default branch, not the review
branch.

No Lean or Aristotle badge is authorized. The repository contains only a
formalization-feasibility report and request packet; no scope-matched theorem
has been rebuilt and kernel checked.
