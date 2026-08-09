# Formalization feasibility

## Assessment

- **Headline theorem:** low-to-moderate short-term feasibility.
- **Finite-tree Jensen and submultiplicativity core:** moderate feasibility.
- **Normalized moment algebra:** high feasibility.
- **Compactness, Schauder extraction, and quantile operator continuity:** low
  short-term feasibility and likely the dominant library burden.
- **Invariant-measure maximum and ergodic dual:** low-to-moderate feasibility
  after the compact dynamical system is formalized.

## Recommended staged target

Stage 1 should kernel-check only:

1. evaluation of any finite binary tree whose gates are addition or minimum is
   coordinatewise monotone, positively homogeneous, and concave;
2. the normalized-leaf Jensen implication yielding the abstract block bound;
3. the anti-correlation integral identity for decreasing profiles, if
   available library support makes this practical;
4. the purely algebraic normalized-second-moment update and invariance of
   \((2p-1)^{-1}\);
5. the scalar shift inequality used by the perturbed fixed-point map.

This is materially relevant because it covers both repairs that generated the
post-audit draft. It does **not** prove compactness, existence of an
eigenprofile, the Collatz--Wielandt formulas, or the original problem.

## Dependency risks

- A literal implementation of decreasing quantiles and the one-dimensional
  Wasserstein identity may require new library infrastructure.
- Helly selection and Vitali convergence in the exact \(L^1\) setting may not
  be packaged at the required level.
- Schauder's theorem may need a custom specialization to the compact convex
  subset of \(L^1\).
- Statement equivalence between a random-variable law and quantile profile
  must not be assumed by an axiom.

No Lean workflow or badge should be activated until downloaded source builds
cleanly under pinned versions, contains no placeholders or custom axioms, and
is independently scope-matched.
