# A spectral characterization of the random series-parallel distance exponent

<!--
Activate this badge only after the repository exists publicly and the named
workflow passes on its default branch:

[![Verify public evidence](https://github.com/DannyExperiments/random-series-parallel-distance-exponent/actions/workflows/verify.yml/badge.svg)](https://github.com/DannyExperiments/random-series-parallel-distance-exponent/actions/workflows/verify.yml)

No Lean badge is authorized: no scope-matched theorem is kernel checked.
No PDF badge is authorized: no compiled or visually inspected PDF exists.
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
- **Priority:** a documented search through 2026-08-09 found no identical or
  stronger all-interior model-specific characterization. The result is
  classified as apparently new with moderate confidence, not as historically
  first.
- **Computation:** none is load-bearing; this is a symbolic proof candidate.
- **Formalization:** feasibility and a small Aristotle/Lean dependency packet
  are supplied, but no theorem in this repository is kernel checked.
- **Manuscript:** `paper/manuscript.tex` is the designated private candidate
  and its source QA and hostile source-level audit pass. No PDF exists;
  compilation and page-by-page visual
  preflight remain pending exact approval for the missing Tectonic resource
  bundle.
- **Review:** no human specialist or journal peer review is claimed.

This directory is a **private local public-candidate skeleton**, not a public
release. It must not be made public until the remaining release gates listed
in [STATUS.md](STATUS.md) are deliberately cleared and the human owner
approves authorship, licensing, visibility, and DOI metadata.

## Repository map

- `proof/`: the exact repaired mathematical draft and scope contract.
- `audits/public_safe_reports/`: sanitized audit status; no private receipts.
- `paper/`: designated private manuscript TeX, source QA, exact claim-scope
  comparison, hostile audit prompt, and explicit PDF-build blocker. No PDF is
  present.
- `formalization/`: feasibility, dependencies, and a narrowly scoped request.
- `verification/`: deterministic integrity and claim-boundary checks.
- `release/`: release notes and activation gates, with no release assets yet.

## Citation and licensing

Citation metadata is provisional because authorship is unresolved. No license
has been granted. See [CITATION.cff](CITATION.cff) and
[LICENSE_STATUS.md](LICENSE_STATUS.md).
