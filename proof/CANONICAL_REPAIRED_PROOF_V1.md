# Exact spectral characterization of the distance exponent

**Document status:** director-repaired mathematical draft V1, dated
2026-08-09. This draft preserves the three frozen discovery returns and
incorporates the local repairs identified by two internal audits and one
external adversarial referee. A fresh hostile source-level audit subsequently
reconstructed the designated current manuscript against this canonical proof
and returned `PASS` with high confidence and no invalid inference.

## 1. Original question and exact scope

The authoritative source is Itai Benjamini, *Euclidean vs. Graph Metric*,
Question 9.6, author manuscript dated 2012 and published in *Erdos
Centennial*, Bolyai Society Mathematical Studies 25 (2013), 35--57,
DOI `10.1007/978-3-642-39286-3_2`. The literal question asks for the shape of

\[
  p\in[1/2,1]\longmapsto \delta(p),
\]

and asks in particular whether \(\delta(1/2)=0\).

The new argument below treats every fixed \(p\in(1/2,1)\). The critical
identity \(\delta(1/2)=0\) and the sharp slightly-supercritical asymptotic are
already known from the 2025 result recorded in the source packet. At \(p=1\),
the distance is deterministically \(2^n\), so \(\delta(1)=\log 2\). Thus the
new interior theorem, the known critical theorem, and the trivial right
endpoint together give an exact characterization on the full closed interval.
The new proof alone must not be credited with the \(p=1/2\) theorem.

Throughout the proof, fix \(p\in(1/2,1)\) and write \(q=1-p\).

## 2. Model and closed quantile state

Let \(\Delta_n\) be the endpoint distance after \(n\) generations, starting
from \(\Delta_0=1\). Root decomposition gives the exact recursion

\[
\Delta_{n+1}\mathrel{\overset d=}
\begin{cases}
\Delta_n^{(1)}+\Delta_n^{(2)},&\text{with probability }p,\\
\min\{\Delta_n^{(1)},\Delta_n^{(2)}\},&\text{with probability }q,
\end{cases}
\tag{2.1}
\]

where the two copies are independent. Put \(m_n=\mathbb E\Delta_n\).

For a nonnegative integrable random variable \(X\), let \(Q_X\) denote its
decreasing quantile on \((0,1)\). For a nonnegative decreasing integrable
profile \(Q\), take independent \(U,V\sim\mathrm{Unif}(0,1)\) and an
independent \(B\sim\mathrm{Bernoulli}(p)\), and define

\[
H_{p,Q}=B\bigl(Q(U)+Q(V)\bigr)+(1-B)Q(\max\{U,V\}).
\tag{2.2}
\]

Because \(Q\) is decreasing,
\(Q(\max\{U,V\})=\min\{Q(U),Q(V)\}\). Define \(T_pQ\) to be the decreasing
quantile of \(H_{p,Q}\). Then

\[
Q_n:=T_p^n\mathbf 1
\]

is exactly the decreasing quantile of \(\Delta_n\), and

\[
m_n=M(Q_n),\qquad M(Q):=\int_0^1Q(u)\,du.
\tag{2.3}
\]

The map \(T_p\) is positively homogeneous and order preserving. It is also
continuous in \(L^1\). Indeed, using the same \(B,U,V\) for two profiles and
the one-dimensional quantile representation of \(W_1\),

\[
\|T_pQ-T_pR\|_1
=W_1(\mathcal L(H_{p,Q}),\mathcal L(H_{p,R}))
\le 2\|Q-R\|_1.
\tag{2.4}
\]

## 3. Headline theorem

Define

\[
K_p=\left\{Q:\ Q\ge0\text{ is decreasing},\ M(Q)=1,
\ \int_0^1Q(u)^2\,du\le\frac1{2p-1}\right\}.
\tag{3.1}
\]

### Theorem 3.1 (interior spectral characterization)

For every \(p\in(1/2,1)\), the limit

\[
\rho(p)=\lim_{n\to\infty}m_n^{1/n}
=\inf_{n\ge1}m_n^{1/n}
\tag{3.2}
\]

exists and satisfies \(\delta(p)=\log\rho(p)\). Moreover, there exists
\(Q_p\in K_p\) such that

\[
T_pQ_p=\rho(p)Q_p.
\tag{3.3}
\]

The number \(\rho(p)\) is the maximal eigenvalue among nonnegative, nonzero,
integrable decreasing profiles, after normalization to mean one. No uniqueness
of the eigenprofile is asserted. It has the exact Collatz--Wielandt
characterizations

\[
\rho(p)=
\max\left\{\alpha\ge0:\ \exists Q\in K_p,
\ T_pQ\ge\alpha Q\text{ a.e.}\right\},
\tag{3.4}
\]

and

\[
\rho(p)=
\inf\left\{\beta>0:\ \exists Q\in K_p,
\ \operatorname*{ess\,inf}Q>0,
\ T_pQ\le\beta Q\text{ a.e.}\right\}.
\tag{3.5}
\]

Consequently, (3.4) or (3.5), together with the explicit one-step operator
(2.2), determines \(\delta(p)\) for every interior parameter without using
\(\delta\) in the definition of the right-hand side.

## 4. Jensen domination and the repaired block inequality

Fix a depth-\(n\) gate-labelled binary tree \(\tau\). Let
\(\Phi_\tau(x_1,\ldots,x_{2^n})\) be its endpoint-distance evaluation, using
addition at a series gate and minimum at a parallel gate. The map
\(\Phi_\tau\) is coordinatewise nondecreasing, positively homogeneous, and
concave. The last assertion follows inductively because sums and pointwise
minima preserve concavity.

If \(Y_1,\ldots,Y_{2^n}\) are independent with mean one, Jensen's inequality
gives

\[
\mathbb E\Phi_\tau(Y_1,\ldots,Y_{2^n})
\le \Phi_\tau(1,\ldots,1).
\tag{4.1}
\]

Averaging over the gate labels yields, for every mean-one profile \(Q\),

\[
M(T_p^nQ)\le m_n.
\tag{4.2}
\]

Here is the normalization omitted in the raw instance-3 return. For depth-
\(k\) leaf distances define

\[
Y_i=\frac{\Delta_k^{(i)}}{m_k},\qquad \mathbb EY_i=1.
\]

Using (4.1) and positive homogeneity,

\[
\begin{aligned}
m_{n+k}
&=\mathbb E_\tau\mathbb E
  \Phi_\tau(\Delta_k^{(1)},\ldots,\Delta_k^{(2^n)})\\
&=m_k\,\mathbb E_\tau\mathbb E
  \Phi_\tau(Y_1,\ldots,Y_{2^n})\\
&\le m_k\,\mathbb E_\tau\Phi_\tau(1,\ldots,1)
=m_km_n.
\end{aligned}
\tag{4.3}
\]

Thus \(\log m_n\) is subadditive. Also

\[
(2p)^n\le m_n\le(1+p)^n,
\tag{4.4}
\]

because the mean multiplier lies between \(2p\) and \(1+p\). Fekete's
lemma proves (3.2). Since the model normalization is
\(m_n=\exp(n\delta(p)+o(n))\), it follows that
\(\delta(p)=\log\rho(p)\).

## 5. The repaired normalized second-moment invariant

For a decreasing profile define

\[
S(Q)=\int_0^1Q(u)^2\,du,
\quad
A(Q)=2\int_0^1uQ(u)\,du,
\quad
C(Q)=2\int_0^1uQ(u)^2\,du.
\tag{5.1}
\]

If \(M(Q)=1\), then \(A(Q)=\mathbb E\min(X_1,X_2)\), where the \(X_i\)
are iid with quantile \(Q\). Hence

\[
0\le A(Q)\le1.
\tag{5.2}
\]

The exact moment identities are

\[
M(T_pQ)=d(Q):=2p+qA(Q),
\tag{5.3}
\]

and

\[
S(T_pQ)=2pS(Q)+2p+qC(Q).
\tag{5.4}
\]

The load-bearing anti-correlation inequality is

\[
C(Q)M(Q)\le A(Q)S(Q).
\tag{5.5}
\]

Indeed,

\[
\begin{aligned}
A(Q)S(Q)-C(Q)M(Q)
=\int_0^1\!\int_0^1
(u-v)Q(u)Q(v)(Q(v)-Q(u))\,du\,dv\ge0,
\end{aligned}
\tag{5.6}
\]

because \(Q\) is decreasing. For \(M(Q)=1\), (5.3)--(5.6) give

\[
S\left(\frac{T_pQ}{d(Q)}\right)
\le\frac{S(Q)}{d(Q)}+\frac{2p}{d(Q)^2}
\le\frac{S(Q)+1}{2p}.
\tag{5.7}
\]

Since \(d(Q)\ge2p>0\), every normalization denominator is nonzero. The bound
\(1/(2p-1)\) is invariant under (5.7), so \(K_p\) is invariant under the
mean-normalized map \(N_pQ=T_pQ/d(Q)\). Starting from \(Q=\mathbf1\) proves
the corrected finite-depth estimate

\[
\boxed{
\frac{\mathbb E[\Delta_n^2]}{(\mathbb E\Delta_n)^2}
\le\frac1{2p-1}
}
\qquad(n\ge0).
\tag{5.8}
\]

Equation (5.8), not its reciprocal, is the canonical replacement for the
flattened equation (15) in the raw response.

## 6. Compactness

The set \(K_p\) is nonempty, convex, and compact in \(L^1(0,1)\). For a
decreasing mean-one profile,

\[
Q(u)\le\frac1u\qquad(u>0).
\]

Helly selection on every \([\eta,1]\), followed by a diagonal argument,
gives an almost-everywhere convergent subsequence. The uniform \(L^2\) bound
implies uniform integrability:

\[
\int_EQ\le |E|^{1/2}\left(\int_0^1Q^2\right)^{1/2}
\le\sqrt{\frac{|E|}{2p-1}}.
\]

Vitali's theorem upgrades the convergence to \(L^1\). The mean is preserved,
and Fatou's lemma preserves the \(L^2\) bound. Continuity of \(T_p\), of
\(d(Q)\), and the bound \(d(Q)\ge2p\) show that \(N_p:K_p\to K_p\) is
continuous.

No compactness uniform as \(p\downarrow1/2\) is claimed; the defining
second-moment constant diverges at the critical point.

## 7. Perturbed fixed points and the principal eigenprofile

For \(\varepsilon>0\), define

\[
T_{p,\varepsilon}Q=T_pQ+\varepsilon M(Q)\mathbf1,
\qquad
N_{p,\varepsilon}Q=
\frac{T_{p,\varepsilon}Q}{M(T_{p,\varepsilon}Q)}.
\tag{7.1}
\]

If a nonnegative random variable has mean \(m\), second moment \(s\), and is
shifted by \(c\ge0\), then

\[
\frac{s+2cm+c^2}{(m+c)^2}\le\frac{s}{m^2},
\tag{7.2}
\]

because the cross-multiplied difference is
\(c(2m+c)(s-m^2)\ge0\). Thus \(N_{p,\varepsilon}\) is a continuous self-map
of \(K_p\). Schauder's theorem yields \(Q_\varepsilon\in K_p\) and
\(\lambda_\varepsilon>0\) such that

\[
T_{p,\varepsilon}Q_\varepsilon
=\lambda_\varepsilon Q_\varepsilon,
\qquad M(Q_\varepsilon)=1.
\tag{7.3}
\]

Here “strongly positive” means only the explicit lower bound

\[
Q_\varepsilon\ge c_\varepsilon\mathbf1,
\qquad c_\varepsilon=\frac{\varepsilon}{\lambda_\varepsilon}>0.
\tag{7.4}
\]

Order preservation and homogeneity imply

\[
\lambda_\varepsilon^nQ_\varepsilon
=T_{p,\varepsilon}^nQ_\varepsilon
\ge c_\varepsilon T_p^n\mathbf1.
\tag{7.5}
\]

After integrating and taking \(n\)-th roots, (7.5) gives
\(\lambda_\varepsilon\ge\rho(p)\).

Compactness gives a sequence \(\varepsilon_j\downarrow0\) for which
\(Q_{\varepsilon_j}\to Q_p\) in \(L^1\) and
\(\lambda_{\varepsilon_j}\to\lambda\). Passing to the limit in (7.3) gives

\[
T_pQ_p=\lambda Q_p.
\tag{7.6}
\]

The scalar subsequence exists because
\(\lambda_\varepsilon=M(T_pQ_\varepsilon)+\varepsilon
=d(Q_\varepsilon)+\varepsilon\), and hence
\(2p+\varepsilon\le\lambda_\varepsilon\le1+p+\varepsilon\).

The preceding comparison gives \(\lambda\ge\rho(p)\). Conversely, iterating
(7.6) and using (4.2) gives

\[
\lambda^n=M(T_p^nQ_p)\le m_n,
\]

so \(\lambda\le\rho(p)\). Hence \(\lambda=\rho(p)\), proving (3.3).
This construction does not assume convergence of the actual orbit
\(N_p^n\mathbf1\).

## 8. Maximality and Collatz--Wielandt formulas

An admissible eigenprofile is a nonnegative, nonzero, integrable decreasing
profile, rescaled to have mean one. If \(T_pQ=\lambda Q\), then (4.2) gives
\(\lambda^n\le m_n\), hence \(\lambda\le\rho(p)\). The profile \(Q_p\)
attains equality. This proves maximality of the numerical eigenvalue, not
uniqueness of its eigenprofile.

If \(Q\in K_p\) and \(T_pQ\ge\alpha Q\), iteration and (4.2) imply
\(\alpha^n\le m_n\), so \(\alpha\le\rho(p)\). Equality is attained by
\(Q_p\), proving (3.4).

For the upper formula, suppose \(Q\in K_p\),
\(Q\ge c\mathbf1\) a.e. for some \(c>0\), and \(T_pQ\le\beta Q\). Then

\[
cT_p^n\mathbf1\le T_p^nQ\le\beta^nQ.
\]

After integration, \(cm_n\le\beta^n\), and therefore
\(\rho(p)\le\beta\). Conversely, the perturbed fixed points satisfy

\[
T_pQ_\varepsilon
=\lambda_\varepsilon Q_\varepsilon-\varepsilon\mathbf1
\le\lambda_\varepsilon Q_\varepsilon,
\]

with \(\operatorname*{ess\,inf}Q_\varepsilon>0\), and every cluster value of
\(\lambda_\varepsilon\) is \(\rho(p)\). This proves (3.5).

If ratio notation is used, define

\[
c_-(Q)=\sup\{\alpha:\ T_pQ\ge\alpha Q\text{ a.e.}\}.
\]

Equivalently, this is the essential infimum of \((T_pQ)/Q\) on
\(\{Q>0\}\); points at which \(Q=0\) impose no lower constraint. Upper
ratios are used only under \(\operatorname*{ess\,inf}Q>0\). These conventions
remove every zero-denominator ambiguity.

## 9. Compatible invariant-measure characterization

This section records the independent characterization returned by the blind
lane and reconstructed by the external referee. It is compatible with, but
not needed for, the headline spectral proof.

Let \(\mathcal I_p\) be the Borel probability measures on \(K_p\) invariant
under \(N_p\), and let \(f_p(Q)=\log d(Q)\). Then

\[
\delta(p)=
\max_{\Pi\in\mathcal I_p}\int_{K_p}f_p(Q)\,d\Pi(Q).
\tag{9.1}
\]

Indeed, for \(Q_j=N_p^j\mathbf1\),

\[
\log m_N=\sum_{j=0}^{N-1}f_p(Q_j).
\]

Every weak limit of the empirical occupation measures is invariant and has
average \(\delta(p)\). Conversely, for any mean-one \(Q\), homogeneity gives

\[
\log M(T_p^nQ)=\sum_{j=0}^{n-1}f_p(N_p^jQ).
\]

Integrating against an invariant \(\Pi\) and applying (4.2) yields

\[
n\int f_p\,d\Pi\le\log m_n.
\]

Taking the infimum over \(n\) proves the reverse inequality in (9.1).
For the eigenprofile, \(N_pQ_p=Q_p\), so the Dirac mass at \(Q_p\) attains
the maximum. This does not imply that every maximizing invariant measure is
a fixed-point mass.

The equivalent continuous ergodic dual is

\[
\delta(p)=
\inf_{h\in C(K_p)}\max_{Q\in K_p}
\bigl(f_p(Q)+h(N_pQ)-h(Q)\bigr).
\tag{9.2}
\]

Weak duality follows by integrating against invariant measures. For strong
duality, fix \(c>\delta(p)\). Compactness implies that for some \(N\), every
\(N\)-step Birkhoff sum is at most \(Nc\); otherwise empirical orbit
segments would yield an invariant measure with average at least \(c\). Put

\[
F_j(Q)=\sum_{i=0}^{j-1}f_p(N_p^iQ),
\qquad
h(Q)=\max_{0\le j<N}(F_j(Q)-jc).
\]

Then \(f_p+h\circ N_p-h\le c\). Letting \(c\downarrow\delta(p)\) proves
(9.2).

## 10. Boundary synthesis and exact answer to Question 9.6

The repaired theorem has the following exact scope.

1. **Interior, new candidate:** for every \(p\in(1/2,1)\), equations
   (3.2)--(3.5) determine \(\delta(p)\).
2. **Critical endpoint, prior work:** \(\delta(1/2)=0\). The present
   compactness proof does not extend there because \(1/(2p-1)\) diverges.
3. **Right endpoint, elementary:** \(\Delta_n=2^n\) at \(p=1\), hence
   \(\delta(1)=\log2\).

Therefore the **new proof alone resolves the residual interior problem**.
When combined with the already-known critical theorem and the elementary
right endpoint, it gives a complete exact characterization on
\([1/2,1]\), which resolves the literal Question 9.6 in the characterization
sense accepted by the frozen terminal certificate. It does not give an
elementary closed formula in \(p\), nor does it separately prove monotonicity,
convexity, uniqueness of the eigenprofile, or global convergence of normalized
laws.

## 11. Audited endpoint extension

The interior eigenprofile also yields, as \(p\uparrow1\),

\[
\delta(p)=\log2-\frac{1-p}{2}+O((1-p)^{3/2}).
\tag{11.1}
\]

To see this, normalize \(\mathbb EX_p=1\) and write
\(R_p=\mathbb EX_p^2\le1/(2p-1)\). Then

\[
\mathbb E\min(X_1,X_2)
=1-\frac12\mathbb E|X_1-X_2|
\ge1-\sqrt{\frac{R_p-1}{2}}
\ge1-\sqrt{\frac{1-p}{2p-1}}.
\]

Taking means in the eigen-equation gives

\[
1+p-\frac{(1-p)^{3/2}}{\sqrt{2p-1}}
\le\rho(p)\le1+p,
\]

and logarithmic expansion proves (11.1). This extension is not needed for
the resolution of the original question.

## 12. Explicit exclusions

Nothing in this proof establishes any of the following:

- uniqueness of \(Q_p\);
- convergence of \(N_p^n\mathbf1\) for every interior \(p\);
- support of every maximizing invariant measure on a fixed point;
- an elementary scalar formula for \(\delta(p)\);
- a compactness argument at \(p=1/2\).

The high-parameter contraction and finite-depth error estimates in the
adversarial discovery return remain separate extensions until they receive
dependency-specific audit. They are not used above.

```text
CORE_SOLUTION_SURVIVES: YES
ORIGINAL_PROBLEM_RESOLVED_AT_PACKET_SCOPE: YES
LITERAL_QUESTION_9_6_STATUS: NEW_ARGUMENT_RESOLVES_INTERIOR; COMBINED_WITH_PRIOR_CRITICAL_RESULT_AND_TRIVIAL_P_EQUALS_1_ENDPOINT, FULL_CLOSED_INTERVAL_CHARACTERIZATION
CANONICAL_HEADLINE_THEOREM: Theorem 3.1
PRIMARY_CHARACTERIZATION: nonlinear eigenprofile plus Collatz-Wielandt formulas
SECONDARY_CHARACTERIZATION: invariant-measure maximum and ergodic dual
ALL_IDENTIFIED_LOCAL_REPAIRS_INCORPORATED: YES
FIRST_UNPROVED_INFERENCE: NONE IN THE REPAIRED DRAFT; FRESH HOSTILE SOURCE-LEVEL AUDIT: PASS_HIGH_CONFIDENCE
```
