# Second independent architecture and priority-collision audit

## RW-10000069: expected-distance exponent in a random series--parallel graph

**Search cutoff:** 9 August 2026
**Audit lane:** theorem-architecture and historical-priority collision only
**Mathematical correctness:** not adjudicated in this report
**Exact-result conclusion:** no earlier theorem located that directly implies the complete model-specific characterization
**Architecture conclusion:** substantial prior art; the generic nonlinear Perron--Frobenius, Collatz--Wielandt, perturbation, and invariant-measure mechanisms are not new
**Provisional classification:** `APPARENTLY_NEW_MODEL_SPECIFIC_ASSEMBLY_WITH_SUBSTANTIAL_GENERIC_ARCHITECTURE_PRIOR_ART`
**Confidence:** moderate, conditional on correctness

## Executive determination

This search was deliberately different from an exact-title or exact-result audit. It asked whether an abstract theorem from nonlinear Perron--Frobenius theory, homogeneous order-preserving maps, recursive distributional equations, quantile dynamics, hierarchical random metrics, or ergodic optimization already yields the claimed characterization for the Bernoulli sum/minimum recursion.

The search found a **serious architecture collision**. Long-established theory already supplies, under suitable cone and compactness hypotheses:

1. eigenvectors at a nonlinear cone spectral radius;
2. lower and upper Collatz--Wielandt characterizations;
3. positive perturbation followed by compactness as an eigenvector-extraction method; and
4. maximization of continuous observables over invariant measures of compact continuous dynamics.

The closest general sources are Akian--Gaubert--Nussbaum and Horst Thieme, especially Thieme's 2024 monograph. Those sources prevent any defensible claim that the candidate introduces a new nonlinear Perron--Frobenius theorem, a new Collatz--Wielandt principle, a new positive-perturbation method, or a new generic invariant-measure duality.

No located source, however, verifies the decisive hypotheses for the particular mixed sum/minimum quantile operator and then identifies its cone-dynamical quantity with

\[
\lim_{n\to\infty}\bigl(\mathbb E\Delta_n\bigr)^{1/n}.
\]

The part that may be new is therefore narrower and model-specific: the normalized second-moment invariant, the compact profile class, the gate-tree Jensen comparison, and the two-sided identification of the resulting eigenvalue and variational quantities with the expected-distance growth factor of this random graph.

No public theorem located through the cutoff directly supplied that complete bridge. The safest conclusion is:

> Conditional on correctness, the candidate appears to give a new model-specific application and assembly of established nonlinear spectral and ergodic machinery. Absolute historical priority is not claimed.

This conclusion is **not** a correctness certificate, a peer-review determination, or a finding that the abstract architecture is new.

## 1. Exact candidate claims compared

The model begins from one edge. At each generation every edge is independently replaced by two edges in series with probability \(p\), or by two parallel edges with probability \(1-p\). If \(\Delta_n\) is endpoint distance, then

\[
\Delta_{n+1}\overset d=
\begin{cases}
\Delta_n^{(1)}+\Delta_n^{(2)},&\text{with probability }p,\\
\min\{\Delta_n^{(1)},\Delta_n^{(2)}\},&\text{with probability }1-p,
\end{cases}
\]

with independent copies on the right, and \(m_n=\mathbb E\Delta_n\).

For each fixed \(p\in(1/2,1)\), the candidate claims:

- existence of \(\rho(p)=\lim_n m_n^{1/n}=\inf_n m_n^{1/n}\), with \(\delta(p)=\log\rho(p)\);
- an exact decreasing-quantile operator \(T_p\);
- a compact, invariant, mean-one profile class
  \[
  K_p=\left\{Q\ge0:\ Q\text{ decreasing},\ \int_0^1Q=1,\ \int_0^1Q^2\le(2p-1)^{-1}\right\};
  \]
- an attained profile \(Q_p\in K_p\) satisfying \(T_pQ_p=\rho(p)Q_p\);
- maximality and the stated lower and upper Collatz--Wielandt formulas;
- a maximum over invariant measures of the normalized profile dynamics; and
- the corresponding continuous ergodic dual.

The candidate does not claim eigenprofile uniqueness, convergence of every normalized orbit, or an elementary scalar formula for \(\delta(p)\). These exclusions are important: several neighboring theories prove uniqueness or convergence under assumptions not established here, whereas other theories give only abstract spectral radii without identifying the particular orbit that begins at the deterministic unit profile.

## 2. The closest nonlinear spectral theorems

### 2.1 Akian--Gaubert--Nussbaum

Marianne Akian, Stephane Gaubert, and Roger Nussbaum, *A Collatz--Wielandt characterization of the spectral radius of order-preserving homogeneous maps on cones*, arXiv:1112.5968:

- <https://arxiv.org/abs/1112.5968>
- archival DOI: <https://doi.org/10.48550/arXiv.1112.5968>

Their setting is a positively homogeneous, order-preserving self-map of a cone in a Banach space. Under normality, regularity, and a quasi-compactness condition expressed through an essential spectral radius, they identify nonlinear spectral radii, give a Collatz--Wielandt formula, and obtain eigenvectors at the spectral radius. Their proof also uses perturbed fixed-point constructions and compactness.

This is the closest abstract collision with the candidate's eigenprofile and Collatz--Wielandt sections. It is not, on the evidence located, a one-line proof of the candidate:

1. the ordinary positive cone in \(L^1\) has empty norm interior, so an interior-cone formula cannot simply be copied to the candidate's state space;
2. the candidate establishes compactness only for a normalized, moment-bounded family of decreasing profiles, not quasi-compactness of \(T_p\) on an ambient cone;
3. an abstract cone spectral radius need not automatically equal the growth rate of the particular deterministic initial orbit or \(\lim m_n^{1/n}\); and
4. the candidate's admissible upper-test class, including its essential lower bound, must still be checked against the hypotheses and conclusions of the abstract theorem.

Thus Akian--Gaubert--Nussbaum is mandatory architecture prior art, but no direct implication of the entire model-specific theorem was found.

### 2.2 Thieme's eigenvector and Collatz--Wielandt theory

Horst R. Thieme's work develops a closely overlapping infinite-dimensional theory:

- *Eigenvectors and eigenfunctionals of homogeneous order-preserving maps*, arXiv:1302.3905: <https://arxiv.org/abs/1302.3905>;
- *Spectral radii and Collatz--Wielandt numbers for homogeneous order-preserving maps and the monotone companion norm*, DOI <https://doi.org/10.1007/978-3-319-27842-1_26>;
- *Eigenfunctionals of homogeneous order-preserving maps with applications to sexually reproducing populations*, DOI <https://doi.org/10.1007/s10884-015-9463-9>;
- *Eigenvectors of homogeneous order-bounded order-preserving maps*, DOI <https://doi.org/10.3934/dcdsb.2017053>.

Thieme proves, under compact-power, essential-compactness, order-boundedness, or related hypotheses, the existence of positive eigenvectors associated with cone spectral radii and develops lower and upper Collatz--Wielandt bounds. His eigenvector proofs include the same broad pattern used by the candidate: add a small positive forcing term, obtain fixed points or eigenvectors, and pass to a compact limit.

This makes the perturbation architecture prior art. It does not by itself verify that the mixed sum/minimum quantile operator has the required global cone compactness/order-boundedness properties, nor does it identify its abstract spectral radius with the expected distance of the random graph.

### 2.3 Thieme's 2024 monograph: the strongest unresolved collision check

Horst R. Thieme, *Discrete-Time Dynamics of Structured Populations and Homogeneous Order-Preserving Operators*, Mathematical Surveys and Monographs 281, American Mathematical Society, 2024:

- AMS record and table of contents: <https://bookstore.ams.org/SURV/281>
- AMS preview: <https://www.ams.org/bookstore/pspdf/surv-281-prev.pdf>
- DOI: <https://doi.org/10.1090/surv/281>

The monograph's table of contents includes homogeneous operators, spectral radii, order-bounded operators, eigenvectors of pseudo-compact homogeneous operators, eigenfunctionals, nonlinear dynamics, and state spaces of measures. It is the broadest single architecture source located and should be treated as mandatory prior art.

The accessible preview and metadata did not reveal an application to the Bernoulli sum/minimum quantile recursion or to the expected distance of the random series--parallel graph. A complete theorem-by-theorem inspection of the monograph was not available in this lane. In particular, the chapters on spectral radii, pseudo-compact eigenvectors, eigenfunctionals, and nonlinear dynamics remain the most important unresolved architecture source gap.

That gap lowers confidence from high to moderate. It does not presently establish a collision, but it prevents a strong historical-priority claim.

## 3. Why the generic theorems do not yet duplicate the model-specific bridge

The following matrix records the closest overlap.

| Candidate component | Generic prior art | Directly supplied by generic theory? | Remaining model-specific work |
|---|---|---:|---|
| Positive homogeneity and order preservation | Classical nonlinear Perron--Frobenius theory | Yes, as a framework | Verify them for the exact quantile operator |
| Eigenvector at spectral radius | Akian--Gaubert--Nussbaum; Thieme | Only under additional cone/compactness hypotheses | Construct an invariant compact normalized class and verify continuity |
| Positive perturbation plus compact limit | Thieme and related cone fixed-point proofs | Yes, as a method | Show perturbed maps preserve the exact class and identify the limiting eigenvalue |
| Lower/upper Collatz--Wielandt values | Akian--Gaubert--Nussbaum; Thieme | Under their hypotheses and test classes | Match the candidate's \(K_p\), positive-lower-bound class, and original growth rate |
| Invariant-measure maximum | Standard ergodic optimization | Yes for a continuous observable on compact dynamics | Show the observable is continuous and its maximum equals \(\delta(p)\) |
| Quantile representation of the recursion | One-dimensional probability/optimal transport | Generic representation is known | Derive the exact mixed sum/minimum operator |
| Uniform normalized \(L^2\) bound | No identical model statement located | No | Use the sum/minimum anti-correlation identity to obtain \((2p-1)^{-1}\) |
| Domination by the original expected-distance orbit | No abstract theorem located that supplies it here | No | Establish the concave gate-tree Jensen inequality |
| Equality with \(\lim m_n^{1/n}\) | Not automatic from an abstract cone spectral radius | No | Prove both inequalities and identify the candidate eigenvalue with \(\rho(p)\) |

The candidate should therefore not be presented as a new general nonlinear spectral theorem. Its potentially new contribution is a verification-and-identification theorem for one exact stochastic recursion.

## 4. Recursive distributional equations and quantile dynamics

### 4.1 General RDE theory

Aldous and Bandyopadhyay, *A survey of max-type recursive distributional equations*, DOI <https://doi.org/10.1214/105051605000000142>, is foundational prior art for treating recursive laws as dynamical operators. It provides terminology and general questions concerning fixed points, endogeny, and iteration. It does not state the candidate's mixed Bernoulli sum/minimum growth-rate theorem.

Smoothing-transform sources were also checked, including:

- *The functional equation of the smoothing transform*, arXiv:0906.3133, DOI <https://doi.org/10.1214/11-AOP670>;
- *Fixed points of inhomogeneous smoothing transforms*, arXiv:1007.4509, DOI <https://doi.org/10.1080/10236198.2011.589514>.

Those theories concern additive or infimum-type transforms under different coefficient structures. No theorem located in them treats the candidate's randomly selected sum-or-minimum gate and then identifies the expected-distance exponent with the stated compact-profile spectral quantities.

### 4.2 The exact sum/minimum binary-tree recursion

Antonio Auffinger and Dylan Cable, *Pemantle's min-plus binary tree*, arXiv:1709.07849:

- <https://arxiv.org/abs/1709.07849>
- archival DOI: <https://doi.org/10.48550/arXiv.1709.07849>

This paper uses the same merge-or-retain-the-minimum binary-tree operation. It determines the critical large-depth behavior and records supercritical growth information, but it does not provide the candidate's every-\(p\in(1/2,1)\) eigenprofile, Collatz--Wielandt, or invariant-measure characterization. It is nevertheless exact-recursion prior art and should be cited prominently.

### 4.3 Hierarchical random metrics

Khristoforov, Kleptsyn, and Triestino, *Stationary random metrics on hierarchical graphs via \((\min,+)\)-type recursive distributional equations*:

- <https://arxiv.org/abs/1310.6116>
- DOI <https://doi.org/10.1007/s00220-016-2650-7>.

They construct stationary laws and convergence after rescaling for hierarchical graph metrics, including uniqueness under density hypotheses. The combinatorial brick, multiplicative-cascade randomness, normalization, and hypotheses differ from the Bernoulli series/parallel distance recursion. Their theorem therefore does not directly duplicate the candidate. It is important neighboring prior art because it shows that fixed laws and exponential renormalization for hierarchical min-plus metrics are not novel ideas.

The RDE for the mean-field traveling-salesman problem was also checked:

- Khandwawala, *Solutions to recursive distributional equations for the mean-field TSP and related problems*, <https://arxiv.org/abs/1405.1316>.

That work studies a different law operator and shift normalization. No collision with the present expected-distance/CW statement was found.

## 5. Branching random graphs and first-passage context

The exact graph model and its distance recursion are prior art, including:

- Hambly and Jordan, *A random hierarchical lattice: the series-parallel graph*, DOI <https://doi.org/10.1239/aap/1093962236>;
- Benjamini, *Euclidean vs. Graph Metric*, DOI <https://doi.org/10.1007/978-3-642-39286-3_2>;
- Chen, Derrida, Duquesne, and Shi, *The distance on the slightly supercritical random series--parallel graph*, DOI <https://doi.org/10.1017/apr.2025.10023>.

The 2025/2026 Chen--Derrida--Duquesne--Shi paper proves the sharp asymptotic close to \(p=1/2\). It does not state an attained quantile eigenprofile or a Collatz--Wielandt/invariant-measure identity for every fixed interior parameter. Recent critical work on resistance and related recursive systems was also screened; no exact all-interior distance theorem of the candidate's form was found.

This distinction matters. The new-looking bridge, if correct, is not a new graph model, new recursion, new phase transition, new existence proof for the exponential rate, or new critical asymptotic.

## 6. Ergodic optimization and invariant-measure duality

Oliver Jenkinson, *Ergodic Optimization*, DOI <https://doi.org/10.3934/dcds.2006.15.197>, surveys the standard compact-dynamical principle that a continuous observable attains its maximal invariant-measure average and describes equivalent variational formulations.

Consequently, once the candidate has a compact state space \(K_p\), a continuous normalized dynamics \(N_p\), and a continuous observable \(f_p\), the abstract existence of maximizing invariant measures and the continuous coboundary dual are generic. Those statements should not be advertised as new abstract ergodic theory.

The model-specific issue is instead the equality

\[
\max_{\Pi:(N_p)_*\Pi=\Pi}\int f_p\,d\Pi=\delta(p),
\]

which depends on the candidate's comparison with the original expected-distance recursion. No source located supplies that equality for this model.

## 7. DOI, arXiv, citation-chain, and author-page search record

### 7.1 Search routes

The audit used exact formulas, architecture phrases, and neighboring terminology across:

- arXiv records and full text;
- Crossref and DataCite DOI/metadata queries;
- OpenAlex forward-citation records;
- publisher and institutional pages;
- AMS book metadata and preview materials;
- author publication pages; and
- general web indexing for discovery, followed by primary-source inspection when available.

Representative queries included:

- `recursive distributional equation Collatz Wielandt`;
- `quantile eigenprofile nonlinear Perron Frobenius`;
- `series parallel graph expected distance spectral radius`;
- `invariant measure distance exponent hierarchical graph`;
- `mixed sum minimum RDE eigenvalue`;
- `order preserving homogeneous quantile operator`;
- `random series parallel 2p-1 distance`; and
- `sum min recursion invariant measure`.

No exact-result collision was returned by the Crossref or DataCite combinations inspected. Exact and near-exact arXiv searches likewise produced no theorem that completes the candidate's model-specific bridge.

### 7.2 Forward citations

The accessible OpenAlex forward-citation sets for Akian--Gaubert--Nussbaum, Thieme's homogeneous-map work, and the Aldous--Bandyopadhyay RDE survey were screened by title, venue, abstract where present, and relevant source text. The nonlinear spectral citations were concentrated in population dynamics, stochastic games, substitutions, and other order-preserving systems. The RDE citations recovered the expected smoothing-transform, hierarchical-metric, min-plus-tree, and exact series--parallel sources. No citing work located stated the candidate's complete all-interior theorem.

Citation indexes are incomplete and can lag recent work. This result is evidence, not a completeness certificate.

### 7.3 Author and institutional pages

Available publication pages for nonlinear Perron--Frobenius authors and primary pages for the exact graph-model authors were checked. No model-specific collision was found. Author-page coverage was uneven, and no direct correspondence was conducted.

## 8. Required prior-art additions before public release

The current candidate bibliography observed in this lane was too narrow for the architecture actually used. At minimum, a public manuscript should cite and accurately distinguish:

1. Akian--Gaubert--Nussbaum, arXiv:1112.5968;
2. Thieme's 2024 AMS monograph, DOI 10.1090/surv/281;
3. Thieme's 2016 Collatz--Wielandt chapter, DOI 10.1007/978-3-319-27842-1_26, or another precise Thieme eigenvector source used in the comparison;
4. Aldous--Bandyopadhyay, DOI 10.1214/105051605000000142;
5. Auffinger--Cable, arXiv:1709.07849;
6. Khristoforov--Kleptsyn--Triestino, DOI 10.1007/s00220-016-2650-7; and
7. Jenkinson, DOI 10.3934/dcds.2006.15.197.

These additions should accompany explicit language that the general spectral, perturbative, RDE, and ergodic mechanisms are prior art. Whether a specific abstract theorem can replace part of the self-contained proof is a mathematical-referee question, not a novelty question.

## 9. What remains potentially new

Subject to proof correctness and the unresolved source gaps, the following combined bridge was not located earlier:

1. encode the exact Bernoulli sum/minimum recursion as a homogeneous monotone operator on decreasing quantiles;
2. derive the exact normalized second-moment transformation and the invariant bound \((2p-1)^{-1}\);
3. obtain a compact invariant mean-one profile class in \(L^1\);
4. compare arbitrary normalized-profile iterations with the original graph recursion through the concave gate-tree Jensen inequality;
5. extract an eigenprofile and prove that its eigenvalue is exactly \(\lim m_n^{1/n}\), rather than merely an abstract cone spectral radius;
6. identify both stated Collatz--Wielandt values with that same expected-distance rate; and
7. identify the invariant-measure maximum with \(\delta(p)\).

The possible novelty is the **complete model-specific assembly and speed-identification bridge**, not its abstract components.

## 10. Public-safe status language

### Recommended architecture paragraph

> The proof uses established ideas from recursive distributional equations, nonlinear Perron--Frobenius theory, Collatz--Wielandt formulas for homogeneous order-preserving maps, compact perturbation arguments, and ergodic optimization. Its contribution is model-specific: an exact normalized moment bound and compact quantile state space, a Jensen comparison with the original random-graph recursion, and an identification of the resulting spectral and invariant-measure quantities with the expected-distance exponent.

### Recommended novelty paragraph

> A documented architecture and priority search current through 9 August 2026 located no earlier theorem carrying out this complete model-specific identification for the Bernoulli series/parallel distance recursion. Conditional on mathematical correctness, the assembly appears new. The abstract nonlinear spectral, recursive-distributional, perturbative, and ergodic mechanisms are prior art, and absolute historical priority is not claimed.

### Claims that should not appear

- “a new nonlinear Perron--Frobenius theorem”;
- “a new Collatz--Wielandt principle”;
- “a new compact-perturbation proof method”;
- “the first invariant-measure variational principle”;
- “the first recursive distributional equation for this graph”;
- “the first fixed law or exponential renormalization on a hierarchical graph”;
- “a closed-form shape of \(\delta(p)\)”;
- “uniqueness of the eigenprofile” or “global convergence”;
- “the generic theory automatically proves the graph theorem”;
- “first proof,” “definitive historical priority,” or “officially solved.”

## 11. Unresolved gaps

1. **Thieme 2024:** full theorem-level review of the AMS monograph chapters on spectral radii, pseudo-compact eigenvectors, eigenfunctionals, and nonlinear dynamics remains outstanding.
2. **Subscription databases:** complete MathSciNet and zbMATH reviews and cited-by networks were not available in this lane.
3. **Recent indexing:** Crossref, DataCite, OpenAlex, and arXiv indexing can lag accepted, posted, or newly published work.
4. **Terminology drift:** an equivalent theorem could appear under population-dynamics, nonlinear cone-spectral, risk-sensitive control, smoothing-transform, or hierarchical-metric terminology not captured by the queries.
5. **Unpublished material:** private manuscripts, seminar notes, accepted-but-unindexed papers, and correspondence cannot be excluded.
6. **Author confirmation:** no relevant author, proposer, or specialist was contacted.
7. **Non-English and non-DOI literature:** coverage was incomplete.
8. **Proof gate:** this lane did not validate the moment identity, compactness, Jensen domination, perturbation limit, or either speed inequality.
9. **Problem-scope gate:** whether a spectral/variational characterization fully answers the informal word “shape” in the original question remains a separate editorial judgment.

## 12. Confidence assessment

| Finding | Confidence |
|---|---|
| Generic nonlinear PF and Collatz--Wielandt architecture is prior art | High |
| Positive perturbation plus compactness is prior art | High |
| Generic compact-dynamical invariant-measure optimization is prior art | High |
| Exact graph model and sum/minimum recursion are prior art | High |
| No located abstract theorem directly implies the complete candidate as stated | Moderate |
| Model-specific bridge appears new, conditional on correctness | Moderate |
| Absolute historical priority | Unknown and not claimed |

## 13. Final adjudication

```text
AUDIT_CUTOFF: 2026-08-09
AUDIT_TYPE: SECOND_INDEPENDENT_ARCHITECTURE_PRIORITY_COLLISION_SEARCH
MATHEMATICAL_CORRECTNESS: NOT_ADJUDICATED_IN_THIS_LANE
GENERIC_NONLINEAR_PF_PRIOR_ART: YES
GENERIC_COLLATZ_WIELANDT_PRIOR_ART: YES
GENERIC_POSITIVE_PERTURBATION_PRIOR_ART: YES
GENERIC_INVARIANT_MEASURE_DUALITY_PRIOR_ART: YES
EXACT_GRAPH_MODEL_PRIOR_ART: YES
EXACT_SUM_MIN_RECURSION_PRIOR_ART: YES
DIRECT_ABSTRACT_THEOREM_IMPLYING_COMPLETE_CANDIDATE: NOT_LOCATED
IDENTICAL_MODEL_SPECIFIC_BRIDGE: NOT_LOCATED
STRONGEST_COLLISION_SOURCE: THIEME_2024_MONOGRAPH_AND_AKIAN_GAUBERT_NUSSBAUM
PROVISIONAL_CLASSIFICATION: APPARENTLY_NEW_MODEL_SPECIFIC_ASSEMBLY_WITH_SUBSTANTIAL_GENERIC_ARCHITECTURE_PRIOR_ART
NOVELTY_CONFIDENCE: MODERATE_CONDITIONAL_ON_CORRECTNESS
ARCHITECTURE_NOVELTY: LOW
MODEL_SPECIFIC_BRIDGE_NOVELTY: MODERATE
ABSOLUTE_PRIORITY: UNKNOWN_NOT_CLAIMED
REPOSITORY_EDIT_AUTHORIZED: NO
```
