# A spectral characterization of the random series-parallel distance exponent

[![Verify public evidence](https://github.com/DannyExperiments/random-series-parallel-distance-exponent/actions/workflows/verify.yml/badge.svg?branch=main)](https://github.com/DannyExperiments/random-series-parallel-distance-exponent/actions/workflows/verify.yml)
[![PDF build](https://github.com/DannyExperiments/random-series-parallel-distance-exponent/actions/workflows/pdf.yml/badge.svg?branch=main)](https://github.com/DannyExperiments/random-series-parallel-distance-exponent/actions/workflows/pdf.yml)

No Lean or Aristotle badge is authorized: no scope-matched theorem is kernel
checked. No DOI badge is authorized before an immutable release is archived
and its DOI resolves.

[Paper production status](paper/README.md) ·
[Paper PDF](paper/manuscript.pdf) ·
[TeX](paper/manuscript.tex) ·
[Exact problem](PROBLEM_AND_PROOF.md) ·
[Canonical proof](proof/CANONICAL_REPAIRED_PROOF_V1.md) ·
[Mathematical audit](audits/public_safe_reports/MATHEMATICAL_AUDIT_STATUS.md) ·
[Priority audit](audits/public_safe_reports/PRIORITY_AUDIT_STATUS.md) ·
[Reproduce](REPRODUCIBILITY.md) ·
[Evidence bundle](release/EVIDENCE_BUNDLE.zip) ·
[Formalization status](formalization/README.md) ·
[Release notes](release/RELEASE_NOTES_v1.0.0.md) ·
[Citation](CITATION.cff)

Itai Benjamini's Question 9.6 asks for the shape of the expected-distance
exponent in a random hierarchical series-parallel graph. For every fixed
\(p\in(1/2,1)\), this repository gives an exact spectral and variational
characterization: the exponential growth factor is the attained maximal
eigenvalue of an explicit sum/min operator on normalized decreasing quantile
profiles. The same value is given by matching lower and upper
Collatz--Wielandt formulas and by a compatible invariant-measure formula.

## Original problem

Start with one edge joining two distinguished vertices. At each generation,
replace every current edge independently by two edges in series with
probability \(p\), or by two parallel edges with probability \(1-p\). Let
\(\Delta_n\) be the distance between the distinguished endpoints and write

\[
  \mathbb E\Delta_n=\exp(n\delta(p)+o(n)).
\]

Question 9.6 in Itai Benjamini, “Euclidean vs. Graph Metric,” asks for the
shape of \(\delta\) on \([1/2,1]\). The residual problem isolated here is to
determine \(\delta(p)\) for every \(p\in(1/2,1)\).

Authoritative source: *Erdős Centennial*, Bolyai Society Mathematical Studies
25 (2013), 35--57, DOI
[`10.1007/978-3-642-39286-3_2`](https://doi.org/10.1007/978-3-642-39286-3_2).

## Main theorem

For each fixed \(p\in(1/2,1)\), the proof defines an explicit order-preserving,
positively homogeneous sum/min operator \(T_p\) on decreasing quantile
profiles and a compact normalized profile set \(K_p\). It proves that

\[
  \rho(p)=e^{\delta(p)}
\]

is the attained maximal eigenvalue of \(T_p\) on the admissible class. It also
proves exact lower and upper Collatz--Wielandt formulas and a compatible
invariant-measure variational formula.

The theorem treats only the open interval. The identity
\(\delta(1/2)=0\) belongs to prior work, and \(\delta(1)=\log 2\) is
elementary. Those endpoint facts and the interior theorem together give a
closed-interval characterization. The critical theorem is not claimed as a
new contribution here.

[Canonical repaired proof](proof/CANONICAL_REPAIRED_PROOF_V1.md) ·
[Designated manuscript TeX](paper/manuscript.tex) ·
[Current status](STATUS.md) ·
[Deterministic evidence bundle](release/EVIDENCE_BUNDLE.zip)

## Verification status

- **Mathematics:** an adversarial referee first returned `REPAIRABLE`, with the
  headline preserved. The identified Jensen normalization repair and domain
  clarifications were incorporated. A fresh hostile source-level audit then
  reconstructed the repaired current manuscript against the canonical proof
  and returned `PASS` with high confidence and no invalid inference.
- **Priority:** three documented search lanes through 2026-08-09 found no
  identical or stronger all-interior model-specific characterization. The
  result is classified as apparently new with moderate confidence, not as
  historically first; generic nonlinear spectral machinery is prior art.
- **Computation:** none is load-bearing; the proof is symbolic.
- **Formalization:** feasibility and a small Aristotle/Lean dependency packet
  are supplied, but no theorem in this repository is kernel checked.
- **Manuscript:** the exact designated source passed both the pinned
  private-branch PDF workflow and the public-`main` PDF workflow. Its four-page
  A4 PDF was retrieved, frozen, text-scanned, and visually inspected page by
  page after a nonmathematical display-spacing repair; preflight passed.
- **Review:** no human specialist or journal peer review is claimed.

The repository is publicly accessible. At the exact pre-release base commit
`f5c3e0bb888a4e4b796b90729a6fc1cfa0581e96`, `Verify public evidence` run
`31302269010` and `PDF build` run `31302269014` passed. Both badge images and
targets were then tested anonymously and reported the public `main` branch as
passing. Branch protection is active on `main`; an immutable Version 1.0.0 tag
and release, release-asset re-download verification, and DOI deposit remain
distinct gates; see [STATUS.md](STATUS.md).

## Repository map

- `proof/`: the exact repaired mathematical draft and scope contract.
- `audits/public_safe_reports/`: sanitized audit status; no private receipts.
- `paper/`: designated manuscript TeX and inspected PDF, source QA, exact
  claim-scope comparison, hostile audit prompt, build record, and PDF preflight.
- `formalization/`: feasibility, dependencies, and a narrowly scoped request.
- `verification/`: deterministic integrity and claim-boundary checks.
- `release/`: deterministic evidence bundle, release-asset hashes, notes, and
  activation gates.

## Automation badges

The two displayed badges report evidence/integrity verification and clean PDF
reconstruction on public `main`. Both workflows passed at the exact
pre-release base commit `f5c3e0bb888a4e4b796b90729a6fc1cfa0581e96` in
runs `31302269010` and `31302269014`; their badge images and target pages were
anonymously tested. The exact activation record and the required release-head
recheck are in
[`release/BADGE_ACTIVATION.md`](release/BADGE_ACTIVATION.md). No Lean,
Aristotle, or DOI badge is displayed.

## Authorship, citation, and licensing

Citation metadata uses the established public author convention
`DannyExperiments`. No repository-wide reuse license is granted; all rights
are reserved. See [CITATION.cff](CITATION.cff),
[AI_DISCLOSURE.md](AI_DISCLOSURE.md), and
[LICENSE_STATUS.md](LICENSE_STATUS.md).
