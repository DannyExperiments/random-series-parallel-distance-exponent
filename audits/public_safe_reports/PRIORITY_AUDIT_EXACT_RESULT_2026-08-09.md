# Fresh literature and historical-priority audit

## RW-10000069: expected-distance exponent in a random series--parallel graph

**Audit cutoff:** 9 August 2026, Asia/Bangkok time
**Audit lane:** literature, status, and historical priority only
**Mathematical correctness:** not adjudicated in this report
**Search classification:** `APPARENTLY_NEW`, conditional on correctness
**Novelty confidence:** moderate

## Executive determination

A fresh source search located no earlier public theorem for the exact Bernoulli series/minimum recursion which, for every fixed \(p\in(1/2,1)\), simultaneously:

1. identifies the exponential growth factor of the expected endpoint distance with an attained eigenvalue of the exact decreasing-quantile operator;
2. proves the stated lower and upper Collatz--Wielandt formulas on the specified mean-one, moment-bounded profile class; and
3. proves the compatible invariant-measure variational maximum for the mean-normalized law dynamics.

The candidate's **assembly is potentially new**, but many of its ingredients and all of its surrounding problem history are prior art. In particular, the graph model, the sum/min recursive distributional equation, submultiplicative existence of the expected-distance exponent, the phase transition, the critical value, the sharp slightly-supercritical asymptotic, general recursive-distributional-equation theory, nonlinear Perron--Frobenius/Collatz--Wielandt theory, and ergodic optimization are not new.

No public result located in this audit states or immediately implies the candidate's exact all-interior, model-specific bridge. The defensible status is therefore:

> **Conditional on mathematical correctness, the model-specific spectral and variational characterization appears new. Absolute historical priority is not claimed.**

This audit found no basis for stronger language such as “the first proof,” “closed form,” “complete historical priority,” or “officially solved.”

## 1. Exact candidate scope used for comparison

The audit compared the canonical repaired proof and current release candidate, not early exploratory variants. The model begins with one edge. Every edge is independently replaced at each generation by two edges in series with probability \(p\), or by two parallel edges with probability \(1-p\). If \(\Delta_n\) is endpoint distance, then

\[
\Delta_{n+1}\overset d=
\begin{cases}
\Delta_n^{(1)}+\Delta_n^{(2)},&\text{with probability }p,\\
\min\{\Delta_n^{(1)},\Delta_n^{(2)}\},&\text{with probability }1-p,
\end{cases}
\]

where the copies are independent, and \(m_n=\mathbb E\Delta_n\).

For each \(p\in(1/2,1)\), the candidate claims:

- \(\rho(p)=\lim_n m_n^{1/n}=\inf_n m_n^{1/n}\) and \(\delta(p)=\log\rho(p)\);
- a mean-one decreasing quantile profile \(Q_p\), with a uniform second-moment bound, satisfying \(T_pQ_p=\rho(p)Q_p\);
- maximality of \(\rho(p)\) among normalized admissible eigenprofiles;
- exact lower and upper Collatz--Wielandt formulas for \(\rho(p)\); and
- an invariant-measure formula
  \[
  \delta(p)=\max_{\Pi:\,(N_p)_*\Pi=\Pi}\int\log d(Q)\,d\Pi(Q)
  \]
  for the compact mean-normalized profile dynamics.

The candidate expressly does **not** claim uniqueness of the eigenprofile, convergence of every normalized orbit, or an elementary scalar formula for \(\delta(p)\). Those exclusions materially affect the priority comparison.

## 2. Original problem and present status

### 2.1 Authoritative problem source

Itai Benjamini's chapter *Euclidean vs. Graph Metric* describes the exact series--parallel random graph and asks in Question 9.6 for the shape of \(p\mapsto\delta(p)\) on \([1/2,1]\), with particular attention to the critical value at \(p=1/2\).

- Author manuscript: <https://www.wisdom.weizmann.ac.il/~itai/erdos5.pdf>
- Published chapter DOI: <https://doi.org/10.1007/978-3-642-39286-3_2>

The chapter was published in *Erdős Centennial* (2013), pages 35--57. The model itself predates that question.

### 2.2 Model origin

The earliest exact-model public source located was Jonathan Jordan's 2003 Oxford D.Phil. thesis, followed by the Hambly--Jordan journal article in 2004.

- Jordan thesis record: <https://ora.ox.ac.uk/objects/uuid%3A3d5d122e-6c32-48c5-ae80-68c095a7131b>
- Thesis DOI: <https://doi.org/10.5287/ora-zbpjq2npa>
- Hambly--Jordan repository record: <https://ora.ox.ac.uk/objects/uuid%3Afd21bacf-d2a5-4ff1-b130-e303bf008494>
- Hambly--Jordan DOI: <https://doi.org/10.1239/aap/1093962236>

These sources establish that the hierarchical graph, its law recursion, law-dynamical viewpoint, phase behavior, and fixed-point questions are prior art. Hambly--Jordan also studies first-passage distance and notes unresolved growth/fixed-point questions. It does not state the candidate's normalized eigenprofile, exact two-sided Collatz--Wielandt formulas, or invariant-measure identity for the expected exponent.

### 2.3 Current endpoint and near-critical results

The central current-status source is Chen, Derrida, Duquesne, and Shi, *The distance on the slightly supercritical random series--parallel graph*.

- Publisher article: <https://www.cambridge.org/core/journals/advances-in-applied-probability/article/distance-on-the-slightly-supercritical-random-seriesparallel-graph/6905B80BCE4DAD97DA9CDECCB48AE924>
- Publisher PDF: <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/6905B80BCE4DAD97DA9CDECCB48AE924/S0001867825100232a.pdf/distance_on_the_slightly_supercritical_random_seriesparallel_graph.pdf>
- DOI: <https://doi.org/10.1017/apr.2025.10023>

The article was published online on 9 September 2025 and appears in *Advances in Applied Probability* 58(1), March 2026, pages 80--121. It:

- states the exact sum/min recursion;
- obtains existence of the expected exponential rate by submultiplicativity;
- records positivity above \(1/2\) and zero rate at and below \(1/2\); and
- proves the sharp slightly-supercritical asymptotic
  \[
  \delta(1/2+\varepsilon)\sim \frac{\pi}{\sqrt6}\sqrt{\varepsilon}.
  \]

It does not state the candidate's all-interior quantile eigenprofile, Collatz--Wielandt, or invariant-measure formulas. Text searches of the publisher article for “Collatz,” “eigen,” and “invariant measure” found no such theorem.

At \(p=1\), the graph is deterministic: \(\Delta_n=2^n\), hence \(\delta(1)=\log 2\). This endpoint is elementary.

### 2.4 Adjacent 2025--2026 developments

Two recent sources were inspected because their terminology and authors overlap closely:

- Chen, Duquesne, and Shi, *Hipster random walks, random series-parallel graph and random homogeneous systems*: <https://arxiv.org/abs/2511.16880>
- Peter Morfe, *Analysis of a class of recursive distributional equations including the resistance of the series-parallel graph*: <https://arxiv.org/abs/2511.11036>

The first concerns critical random homogeneous systems and, for the graph application, critical effective resistance. The second develops a critical/near-critical PDE route for recursive systems including resistance. Neither gives the fixed-supercritical expected-distance characterization claimed here.

The critical min-plus tree literature was also checked:

- Auffinger and Cable, *Pemantle's min-plus binary tree*: <https://arxiv.org/abs/1709.07849>

That work is direct critical prior art for the sum/min operation, but its theorem is not an all-\(p\) characterization of \(\lim n^{-1}\log\mathbb E\Delta_n\).

## 3. Exact-result collision search

### 3.1 Search families

The search used exact and variant terminology drawn from the theorem rather than relying only on the problem title. Representative queries included:

- `random series-parallel graph Collatz-Wielandt distance`
- `series-parallel graph eigenprofile distance exponent`
- `random series-parallel normalized law invariant measure`
- `expected distance series-parallel recursive distribution exponent`
- `Bernoulli sum min quantile eigenfunction`
- `delta(p) random series-parallel graph`
- `Question 9.6 Euclidean vs Graph Metric solution`
- `nonlinear Perron-Frobenius sum min recursion`
- `stationary random metrics hierarchical graph min plus`

Exact-title and formula searches were run over general web indexing, arXiv, publisher pages, author and institutional repositories, Crossref, DataCite, OpenAlex, GitHub, Zenodo, and MathOverflow. Search snippets were used only for discovery; substantive comparisons were made against primary PDFs, publisher pages, arXiv records, or institutional records when available.

### 3.2 DOI and metadata registries

The Crossref records for the directly relevant papers were checked live:

- <https://api.crossref.org/works/10.1017%2Fapr.2025.10023>
- <https://api.crossref.org/works/10.1239%2Faap%2F1093962236>

As of the cutoff, Crossref reported zero citing works for the 2025/2026 Chen--Derrida--Duquesne--Shi paper. OpenAlex likewise reported zero citations for its work record:

- <https://api.openalex.org/works/https://doi.org/10.1017/apr.2025.10023>

The 24 OpenAlex-indexed works citing Hambly--Jordan were screened. The directly relevant entries were Benjamini, Auffinger--Cable, and Chen--Derrida--Duquesne--Shi; none of the citing titles or inspected sources contained the candidate's theorem. Crossref and DataCite query combinations involving `series-parallel`, `distance exponent`, `Collatz-Wielandt`, `eigenprofile`, `normalized law`, and `invariant measure` produced no exact collision.

Registry citation counts are incomplete, especially for very recent preprints, so the zero count is supporting evidence rather than a priority certificate.

### 3.3 Exact-result finding

No public source located through the cutoff states an identical theorem. No public source was located that is strictly stronger in this exact model and would make the candidate an immediate corollary.

The nearest exact-model paper, Chen--Derrida--Duquesne--Shi, proves precise local information near the critical parameter but not a global spectral or variational characterization for each fixed \(p\in(1/2,1)\). The candidate and that paper are therefore complementary in form: one gives sharp near-critical asymptotics; the other claims an exact all-interior characterization without an elementary closed form.

## 4. Architecture prior art

The candidate's vocabulary overlaps several mature theories. That overlap must be disclosed, but it does not by itself yield the candidate's theorem.

| Component | Prior-art status | Closest source | Why it does not automatically imply the candidate |
|---|---|---|---|
| Sum/min law recursion | Known | Jordan 2003; Hambly--Jordan 2004 | Same model and recursion, weaker fixed-point/rate conclusions |
| RDE as a map on laws | Known | Aldous--Bandyopadhyay 2005 | General framework; no model-specific compact normalized class or speed identification |
| Existence of expected rate | Known | Chen et al. 2025/2026 | Submultiplicativity gives the rate, not the eigenprofile or variational formulas |
| Critical and near-critical behavior | Known | Auffinger--Cable; Chen et al. | Parameter-local conclusions rather than fixed-supercritical characterization |
| Nonlinear PF / Collatz--Wielandt | Known | Gaubert--Gunawardena; Akian--Gaubert--Nussbaum | Abstract theorems require cone, compactness, positivity, or quasi-compactness hypotheses not verified merely by citation |
| Stationary hierarchical min-plus metrics | Known | Khristoforov--Kleptsyn--Triestino | Different hierarchical operator, multiplicative-cascade law, normalization, and density assumptions |
| Maximization over invariant measures | Known | Jenkinson and ergodic optimization | Generic compact-dynamical variational structure; the exact bridge to \(\mathbb E\Delta_n\) is model-specific |
| Candidate's complete bridge | No identical source located | This candidate | Requires the exact moment bound, compact invariant set, eigenprofile extraction, two-sided comparison, and speed identification |

Primary architecture sources checked include:

- Aldous and Bandyopadhyay, *A survey of max-type recursive distributional equations*, DOI <https://doi.org/10.1214/105051605000000142>
- Gaubert and Gunawardena, *The Perron--Frobenius theorem for homogeneous, monotone functions*, DOI <https://doi.org/10.1090/S0002-9947-04-03470-1>
- Akian, Gaubert, and Nussbaum, *A Collatz--Wielandt characterization of the spectral radius of order-preserving homogeneous maps on cones*: <https://arxiv.org/abs/1112.5968>
- Khristoforov, Kleptsyn, and Triestino, *Stationary random metrics on hierarchical graphs via (min,+)-type recursive distributional equations*: <https://arxiv.org/abs/1310.6116>, DOI <https://doi.org/10.1007/s00220-016-2650-7>
- Jenkinson, *Ergodic Optimization*: <https://www.aimsciences.org/article/doi/10.3934/dcds.2006.15.197>, DOI <https://doi.org/10.3934/dcds.2006.15.197>

The priority-sensitive contribution is not the abstract existence of these theories. It is the candidate's self-contained verification that the exact random-graph operator fits a compact normalized profile dynamics and that all three numerical characterizations equal the original expected-distance growth factor.

## 5. Component-by-component priority assessment

| Candidate statement | Priority finding through cutoff | Confidence |
|---|---|---|
| The random series--parallel model | Known since at least 2003/2004 | High |
| The sum/min distance RDE | Known | High |
| \(\rho=\lim m_n^{1/n}=\inf m_n^{1/n}\) | Known mechanism; explicitly used in current exact-model work | High |
| \(\delta(1/2)=0\) | Known | High |
| Sharp \(p\downarrow1/2\) asymptotic | Known, Chen et al. | High |
| \(\delta(1)=\log2\) | Elementary | High |
| Compact moment-bounded normalized quantile state space used here | No identical exact-model statement located | Moderate |
| Attained principal quantile eigenprofile for every \(p\in(1/2,1)\) | No identical exact-model statement located | Moderate |
| Exact lower and upper Collatz--Wielandt formulas in the stated classes | No identical exact-model statement located | Moderate |
| Compatible invariant-measure maximum equal to \(\delta(p)\) | No identical exact-model statement located | Moderate |
| Uniqueness/global normalized-orbit convergence | Not claimed and not established by this audit | High |
| Elementary closed form for \(\delta(p)\) | Not claimed and not located | High |

## 6. How the result relates to Benjamini's wording

Question 9.6 asks for the “shape” of the function. That phrase does not prescribe what form a satisfactory answer must take. The candidate claims an exact spectral and variational characterization, not an elementary formula, explicit numerical graph, differentiability theorem, or monotonicity/convexity classification.

Accordingly, the safest problem-status description is:

> The theorem supplies an exact all-interior spectral and variational characterization of the expected-distance exponent. Together with prior critical results and the elementary \(p=1\) endpoint, it addresses the residual interior part of Benjamini's Question 9.6 in a spectral/variational sense.

It is less safe to say without qualification that it “completely determines the shape” or gives a “closed form.”

## 7. Public-safe language

### Recommended full status paragraph

> A documented literature and metadata search current through 9 August 2026 located no earlier public theorem for this exact random series--parallel model that identifies the expected-distance growth factor throughout \(p\in(1/2,1)\) as an attained nonlinear quantile-operator eigenvalue and simultaneously proves the stated Collatz--Wielandt and invariant-measure variational formulas. The graph model, sum/min recursion, existence of the expected exponential rate, critical and near-critical results, and the abstract RDE, nonlinear Perron--Frobenius, Collatz--Wielandt, and ergodic-optimization machinery are prior art. Conditional on mathematical correctness, the model-specific characterization appears new; absolute historical priority is not claimed.

### Recommended short introduction wording

> We are not aware of a previous all-interior spectral or variational characterization of this expected-distance exponent. Our contribution is model-specific: it connects the classical sum/min recursion to a compact normalized quantile dynamics, an attained principal eigenprofile, exact Collatz--Wielandt formulas, and an invariant-measure maximum.

### Recommended problem-status wording

> For \(p\in(1/2,1)\), the result gives an exact spectral and variational characterization of the exponent. Combined with the known critical result and the elementary \(p=1\) endpoint, it addresses Benjamini's Question 9.6 on the full interval in this characterization sense.

### Claims that should not appear

- “first proof” or “earliest solution”;
- “the problem was entirely untouched”;
- “we introduce the random series--parallel model or its RDE”;
- “we introduce nonlinear Perron--Frobenius, Collatz--Wielandt, or ergodic optimization”;
- “closed-form formula for \(\delta(p)\)”;
- “the eigenprofile is unique”;
- “all normalized laws converge”;
- “the result is peer reviewed, accepted, or officially recorded as a solution”;
- “the literature search proves priority”; or
- “the generic abstract theorems alone prove the model-specific statement.”

## 8. Unresolved source gaps

1. Full subscription-only MathSciNet reviews and complete cited-by networks were not available.
2. zbMATH Open metadata was searchable, but complete subscription-level citation graphs and reviews were not available.
3. Google Scholar coverage is opaque and was used only for discovery, not as a completeness certificate.
4. Crossref, DataCite, and OpenAlex can lag or omit very recent preprints, conference notes, book chapters, and non-DOI works.
5. No direct correspondence was conducted with Benjamini, Hambly, Jordan, Chen, Derrida, Duquesne, Shi, Auffinger, Cable, or other specialists.
6. Unpublished manuscripts, private communications, accepted-but-unindexed papers, seminar notes, and work posted on the cutoff date cannot be excluded.
7. Non-English sources or results using terminology far from “series--parallel,” “sum/min,” “quantile eigenprofile,” or “Collatz--Wielandt” may evade the search.
8. An equivalent abstract theorem could be buried in infinite-dimensional nonlinear operator theory under different notation. The closest general sources found still require a nontrivial model-specific application.
9. This report does not certify the proof. A false theorem can be novel; correctness and priority remain separate gates.

## 9. Confidence statement

- Original source, model provenance, and exact wording: **high**.
- Scope of Hambly--Jordan, Auffinger--Cable, and Chen--Derrida--Duquesne--Shi: **high**.
- The recursion, rate-existence mechanism, endpoint results, and generic architecture being prior art: **high**.
- No identical or stronger public exact-model theorem located: **moderate**.
- `APPARENTLY_NEW` classification, conditional on proof correctness: **moderate**.
- Absolute historical priority: **unknown and not claimed**.

## 10. Final adjudication

```text
AUDIT_CUTOFF: 2026-08-09
ORIGINAL_STATEMENT_VERIFIED: YES
ORIGINAL_SOURCE: Benjamini, Euclidean vs. Graph Metric, Question 9.6
MODEL_ORIGIN_PRIOR_ART: YES — Jordan 2003; Hambly–Jordan 2004
EXPECTED_RATE_EXISTENCE_PRIOR_ART: YES
CRITICAL_AND_NEAR_CRITICAL_RESULTS_PRIOR_ART: YES
EXACT_ALL_INTERIOR_EIGENPROFILE_RESULT_LOCATED: NO
EXACT_ALL_INTERIOR_COLLATZ_WIELANDT_RESULT_LOCATED: NO
EXACT_ALL_INTERIOR_INVARIANT_MEASURE_FORMULA_LOCATED: NO
EARLIER_IDENTICAL_RESULT: NONE LOCATED
EARLIER_STRONGER_RESULT: NONE LOCATED
NOVELTY_CLASSIFICATION: APPARENTLY_NEW, CONDITIONAL ON CORRECTNESS
NOVELTY_CONFIDENCE: MODERATE
ABSOLUTE_PRIORITY_CLAIM: NO
PROOF_CORRECTNESS_ADJUDICATED: NO
```

## Search execution note

The audit was executed independently against the canonical repaired proof and current release candidate. The earlier supplied priority package was inspected only after the fresh exact-result, citation-chain, DOI, arXiv, and architecture searches had been completed; it was used as a completeness cross-check, not as the source of this verdict.
