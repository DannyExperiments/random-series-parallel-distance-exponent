# Formalization lane

No theorem in this repository is formally verified. The full analytic proof
depends on distributional quantiles, Wasserstein continuity, compactness in
\(L^1\), Helly/Vitali arguments, Schauder fixed points, and ergodic
optimization; a complete Lean formalization is a substantial project.

The recommended first target is a partial supporting kernel containing the
finite-tree concavity/Jensen block inequality and the algebraic normalized
second-moment invariant. Passing it would justify only a badge labelled
`Partial logical-core Lean check`, never `Lean verified` or `Lean core
theorem` for the headline.

See `FORMALIZATION_FEASIBILITY.md`, `DEPENDENCY_MAP.md`, `THEOREM_SCOPE.md`,
and `aristotle/ARISTOTLE_CORE_PROMPT.md`.
