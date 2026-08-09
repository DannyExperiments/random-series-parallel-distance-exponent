# A spectral characterization of the random series-parallel distance exponent

<!--
Activate these badges only after the repository exists publicly and the named
workflows pass on its public default branch:

[![Verify public evidence](https://github.com/DannyExperiments/random-series-parallel-distance-exponent/actions/workflows/verify.yml/badge.svg)](https://github.com/DannyExperiments/random-series-parallel-distance-exponent/actions/workflows/verify.yml)
[![PDF build](https://github.com/DannyExperiments/random-series-parallel-distance-exponent/actions/workflows/pdf.yml/badge.svg)](https://github.com/DannyExperiments/random-series-parallel-distance-exponent/actions/workflows/pdf.yml)

No Lean badge is authorized: no scope-matched theorem is kernel checked.
The PDF is compiled and visually inspected, but its badge remains hidden until
the same workflow passes on the public default branch.
-->

This private staging repository presents a repaired proof candidate for the
remaining interior part of Itai Benjamini's Question 9.6: for every
\(p\in(1/2,1)\), the expected-distance exponent is characterized as an
attained nonlinear spectral value, with exact Collatz--Wielandt and
invariant-measure formulas.

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

## Candidate result

For each fixed \(p\in(1/2,1)\), the proof defines an explicit order-preserving,
positively homogeneous sum/min operator \(T_p\) on decreasing quantile
profiles and a compact normalized profile set \(K_p\). It proves that

\[
  \rho(p)=e^{\delta(p)}
\]

is the attained maximal eigenvalue of \(T_p\) on the admissible class. It also
proves exact lower and upper Collatz--Wielandt formulas and a compatible
invariant-measure variational formula.

The new argument treats only the open interval. The identity
\(\delta(1/2)=0\) belongs to prior work, and \(\delta(1)=\log 2\) is
elementary. Those endpoint facts and the interior candidate together give a
closed-interval characterization; the critical theorem is not claimed as a
new contribution here.

[Exact problem and proof outline](PROBLEM_AND_PROOF.md) ·
[Repaired proof candidate](proof/CANONICAL_REPAIRED_PROOF_V1.md) ·
[Paper (PDF)](paper/manuscript.pdf) ·
[Designated manuscript TeX](paper/manuscript.tex) ·
[Status](STATUS.md) ·
[Formalization feasibility](formalization/FORMALIZATION_FEASIBILITY.md) ·
[Reproducibility](REPRODUCIBILITY.md)

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
- **Computation:** none is load-bearing; this is a symbolic proof candidate.
- **Formalization:** feasibility and a small Aristotle/Lean dependency packet
  are supplied, but no theorem in this repository is kernel checked.
- **Manuscript:** the exact designated source passed the pinned private-branch
  PDF workflow. Its four-page A4 PDF was retrieved, frozen, text-scanned, and
  visually inspected page by page after a nonmathematical display-spacing
  repair; preflight passed.
- **Review:** no human specialist or journal peer review is claimed.

This directory is a **private public-candidate repository**, not a public
release. It must not be made public until the remaining release gates listed
in [STATUS.md](STATUS.md) are deliberately cleared and the human owner
approves licensing, visibility, and DOI metadata.

## Repository map

- `proof/`: the exact repaired mathematical draft and scope contract.
- `audits/public_safe_reports/`: sanitized audit status; no private receipts.
- `paper/`: designated manuscript TeX and inspected PDF, source QA, exact
  claim-scope comparison, hostile audit prompt, build record, and PDF preflight.
- `formalization/`: feasibility, dependencies, and a narrowly scoped request.
- `verification/`: deterministic integrity and claim-boundary checks.
- `release/`: release notes and activation gates, with no release assets yet.

## Citation and licensing

Citation metadata uses the established public author convention
`DannyExperiments` but retains a private-candidate version and no DOI. No
license has been granted. See [CITATION.cff](CITATION.cff) and
[LICENSE_STATUS.md](LICENSE_STATUS.md).
