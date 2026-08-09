# Exact problem and proof architecture

## The model

Start from a single edge with distinguished endpoints. Independently replace
each edge at each generation by two edges in series with probability \(p\),
or two parallel edges with probability \(1-p\). If \(\Delta_n\) is the
endpoint distance, then

\[
\Delta_{n+1}\overset d=
\begin{cases}
\Delta_n^{(1)}+\Delta_n^{(2)},&\text{with probability }p,\\
\min\{\Delta_n^{(1)},\Delta_n^{(2)}\},&\text{with probability }1-p,
\end{cases}
\]

for independent copies. For \(p>1/2\), established model analysis defines
\(\delta(p)\) by

\[
\mathbb E\Delta_n=\exp(n\delta(p)+o(n)).
\]

The residual problem is to determine \(\delta(p)\) for every
\(p\in(1/2,1)\). The critical endpoint is not part of the new proof.

## Candidate theorem

Let \(T_p\) send a nonnegative decreasing quantile profile to the decreasing
quantile of the one-step sum/min mixture. The repaired candidate proves:

> For every \(p\in(1/2,1)\), \(\rho(p)=e^{\delta(p)}\) is the attained maximal
> mean-normalized eigenvalue of \(T_p\) on an explicit compact profile class.
> It equals exact lower and upper Collatz--Wielandt values and an exact
> invariant-measure variational value.

No eigenprofile uniqueness, global normalized-orbit convergence, elementary
closed formula, or critical compactness theorem is claimed.

## Load-bearing proof chain

1. **Quantile closure.** The distributional recursion becomes a continuous,
   order-preserving, homogeneous operator \(T_p\) on decreasing profiles.
2. **Normalized Jensen inequality.** Every fixed gate-labelled tree is a
   coordinatewise increasing concave homogeneous function. Normalizing each
   leaf to mean one before Jensen gives
   \(m_{n+k}\le m_nm_k\).
3. **Exponential speed.** Submultiplicativity and Fekete's lemma give
   \(\rho(p)=\lim m_n^{1/n}=\inf m_n^{1/n}\) and
   \(\delta(p)=\log\rho(p)\).
4. **Moment invariant.** Exact moment identities and an anti-correlation
   inequality give
   \(\mathbb E\Delta_n^2/(\mathbb E\Delta_n)^2\le(2p-1)^{-1}\).
5. **Compact normalized state.** Monotonicity and the uniform second-moment
   bound yield compactness in \(L^1\) by Helly selection and uniform
   integrability.
6. **Perturbed fixed points.** A strictly positive perturbation and Schauder's
   theorem produce normalized eigenprofiles; compactness removes the
   perturbation.
7. **Spectral identification.** Order comparison and the normalized Jensen
   bound force the limiting eigenvalue to be exactly \(\rho(p)\).
8. **Variational formulas.** Iteration yields the Collatz--Wielandt bounds;
   occupation measures give the compatible invariant-measure maximum and
   ergodic dual.

The complete repaired argument is frozen at
[`proof/CANONICAL_REPAIRED_PROOF_V1.md`](proof/CANONICAL_REPAIRED_PROOF_V1.md).
The repaired proof was reconstructed in a fresh hostile source-level audit
against the designated manuscript and returned `PASS`, with no invalid
inference and high confidence; see
[`audits/public_safe_reports/MATHEMATICAL_AUDIT_STATUS.md`](audits/public_safe_reports/MATHEMATICAL_AUDIT_STATUS.md).
