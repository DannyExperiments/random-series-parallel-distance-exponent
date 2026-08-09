# Aristotle / Lean partial-core request

Formalize a narrowly scoped supporting kernel for the attached repaired proof
of the random series-parallel distance-exponent characterization. Do not claim
to formalize the headline theorem.

## Target A: finite sum/min tree Jensen core

Define a finite full binary tree whose internal nodes are labelled `add` or
`min`, and its evaluation on nonnegative real leaf values. Prove that the
evaluation is coordinatewise monotone, positively homogeneous, and concave.
Deduce the finite-dimensional Jensen statement for independent integrable
nonnegative mean-one leaves. State the resulting abstract normalized-leaf
block inequality explicitly, including the normalization and homogeneity
factor.

## Target B: normalized second-moment algebra

For real parameters with `1/2 < p < 1`, put `q = 1-p`. Formalize the algebraic
implication used in the manuscript: from the exact first/second-moment update
and the anti-correlation premise `C*M <= A*S`, with `M=1`, `0 <= A <= 1`, and
nonnegative quantities, prove

```text
S(next_normalized) <= (S + 1) / (2*p)
```

and hence invariance of `S <= 1/(2*p-1)`. Also prove the scalar shift lemma

```text
(s + 2*c*m + c^2)/(m+c)^2 <= s/m^2
```

under `0 < m`, `0 <= c`, and `m^2 <= s`.

## Scope and requirements

- Use an explicitly pinned Lean and Mathlib version.
- No `sorry`, `admit`, `unsafe`, custom `axiom`, or unproved custom `opaque`.
- Eliminate division by proving denominators positive and cross-multiplying.
- Do not assume the anti-correlation integral theorem as an axiom; if its
  measure-theoretic proof is not completed, expose it as an explicit input to
  the algebraic lemma and label the result partial.
- Do not claim quantile continuity, compactness, Schauder, an eigenprofile,
  Collatz--Wielandt, or a solution of Question 9.6.

Return one ZIP containing all Lean/Lake source, `lean-toolchain`,
`lakefile.lean`, `lake-manifest.json`, README, exact theorem-scope report,
clean build log, no-placeholder scan, `#print axioms` output, manifest, and
SHA-256 ledger.
