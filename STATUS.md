# Status

Status date: 2026-08-09.

Current state: `PUBLIC_MAIN_CI_PASS_RELEASE_PENDING`.

Public repository gate: `PRE_RELEASE_METADATA_REPAIR_RUNNING`.

| Dimension | State | Exact meaning |
|---|---|---|
| Headline theorem | `CANONICAL_REPAIRED_PROOF_V1` | The residual interior \(p\in(1/2,1)\) is characterized by an attained nonlinear eigenvalue and exact variational formulas. |
| Mathematical audit | `PASS_HIGH_CONFIDENCE` | After the initial `REPAIRABLE` verdict and incorporated local repairs, a fresh hostile source-level audit reconstructed the repaired manuscript against the canonical proof and found no invalid inference. |
| Literal Question 9.6 | `COMBINED_CHARACTERIZATION` | The new argument treats the interior; prior work supplies \(p=1/2\); \(p=1\) is elementary. |
| Critical endpoint | `PRIOR_RESULT` | This work does not claim to prove \(\delta(1/2)=0\) for the first time. |
| Priority | `PRIORITY_AUDIT_PASS_QUALIFIED` | Three documented lanes through 2026-08-09 found no identical or stronger all-interior characterization. The model-specific assembly is `APPARENTLY_NEW` with moderate confidence; substantial generic nonlinear Perron--Frobenius and Collatz--Wielandt architecture is prior art, and absolute priority is not established. |
| Novelty language | `APPARENTLY_NEW_MODERATE_QUALIFIED` | Allowed only with the explicit cutoff and negative-search limitations. |
| Computation | `NOT_LOAD_BEARING` | The proof is symbolic. No finite experiment is represented as proof. |
| Manuscript | `MANUSCRIPT_PASS` | The exact designated source passed private-branch CI and the public-`main` PDF workflow. The frozen four-page A4 PDF passed text/privacy checks and page-by-page visual preflight after the audited nonmathematical display-spacing repair. |
| Formalization | `FORMALIZATION_NOT_ATTEMPTED` | A dependency report and request packet exist; no Lean theorem has been proved. |
| Human review | `PENDING` | No specialist or journal referee report is claimed. |
| Repository visibility | `PUBLIC_ANONYMOUS_ACCESS_PASS` | The repository and its default `main` branch were opened successfully without authentication. |
| Public-main CI | `PASS_AT_F5C3E0B` | `Verify public evidence` run `31302269010` and `PDF build` run `31302269014` passed at the exact pre-release public-`main` base commit `f5c3e0bb888a4e4b796b90729a6fc1cfa0581e96`. The metadata-only repair head must pass the same two checks before merge and release. |
| Automation badges | `ACTIVE_PUBLIC_MAIN_PASS` | Exactly the verify and PDF badges are displayed in this closure tree; both image URLs and target pages were anonymously tested against public `main`. No Lean, Aristotle, or DOI badge is authorized. |
| Branch protection | `CONFIRMED_ACTIVE` | Authenticated GitHub settings show protection for `main`, with pull requests, the two required status checks, up-to-date branches, conversation resolution, linear history, administrator non-bypass, and force-push/deletion prevention enabled. |
| Publication | `IMMUTABLE_RELEASE_PENDING` | No Version 1.0.0 tag or GitHub release has been created, and no release asset has been re-downloaded from an immutable release. |
| DOI | `DOI_PENDING` | No DOI has been deposited or claimed. |
| Authorship | `DANNYEXPERIMENTS_APPROVED` | Citation metadata follows the owner's established public convention. |
| License | `ALL_RIGHTS_RESERVED` | No repository-wide reuse license is granted. |

## Remaining release steps

1. Require both workflows to pass on the exact metadata-repair PR head, then
   review and merge it through the protected branch.
2. Create the immutable Version 1.0.0 tag and GitHub release from the exact
   audited assets, then re-download every asset and verify its SHA-256 hash.
3. Only after that verification, advance to `PUBLIC_TIMESTAMPED_NO_DOI`.
4. Deposit and resolve the DOI, then add it in a metadata-only protected
   update.
5. Obtain separate approval before any external problem-page notice.

Current machine state: `PASS_HIGH_CONFIDENCE`,
`PRIORITY_AUDIT_PASS_QUALIFIED`, `MANUSCRIPT_PASS`, and
`PUBLIC_MAIN_CI_PASS_RELEASE_PENDING`, with public visibility, CI, and branch
protection independently
recorded as above. None may be strengthened merely because this repository's
integrity check passes. No Lean or Aristotle badge is authorized.
