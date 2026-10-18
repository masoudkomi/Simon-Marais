# Genuine failed routes and the remaining cut-mass problem

2026-10-18 UTC. **Candidate proof - unverified.** The positive counterexample proofs are CN1--CN3 in the full main file. This record keeps the attempted implications separate from those proofs. No larger count, finite history search or numerical tightening was substituted for a missing inference.

## 1. From cut spread to cut number

The accepted staircase has two widely separated midpoint cuts and uniformly bounded range-3 pieces. It therefore already defeats a spread estimate, but does not defeat an estimate for the NUMBER of cuts. Repeating the old staircase observation would not advance the question. I did not count its spread as new progress.

The first genuine attempted bridge was a pointwise bound such as `k_n(X)<=C*(L_3(u)+L_3(v)+1)`, or at least a sublinear bound whenever both confined-piece lengths are small. Accepted CR would turn a valid suitable estimate into information about the mean. This was a plausible new route, not a known lemma. CN2 now gives actual BALANCED outputs with `k_(28560m)>=34m+1` but `L_3(u)<=27`, `L_3(v)<=19`. It disproves this route, including a uniform sublinear error plus any finite function of those two confined-piece statistics.

Trying a larger FIXED range does not cure it: the full ruler-word construction chooses a larger fixed height h and gives the same obstruction for every prescribed finite range r. The periods may depend on r. This does not say one finite period works against all ranges, and does not disprove every adaptive range depending on the output length.

## 2. False synchronization-rate intuition

Before finding the explicit schedules, I considered whether two periodic tapes whose full height ranges exceed the leash width must have a unique positive synchronization rate. A single wide oscillation appears to force the other tape to oscillate too. That local intuition does not control nested oscillations. The elementary pairs `(E_j,O_(j-1))` and `(E_j,O_j)` have two compatible adjacent height levels; zero-index right factors can be consumed while the left tape waits. Iterating this mechanism through the finite ruler word yields actual rates `(1,1)` and `(1,2)` at arbitrarily large full ranges of BOTH periods. Thus no uniqueness claim survives. I did not prove a general torus theorem and do not invoke one.

An intermediate informal idea that feasible antidiagonal cuts might share one height level would not by itself bound the number of separated returns. It was not proved and is not needed by the counterexample. Bare antidiagonal height equalities were never promoted to legal cuts; all new cuts have explicit full schedules.

## 3. Signature and visiting-order route

Original sources were consulted as research leads, not as guarantees of uniqueness; exact read scopes are recorded separately. The needed universal alignment uniqueness was not established, and CN1 supplies the two actual rates instead. No published theorem is contradicted or used to prove the construction. The histories require no perturbation.

The useful next question is whether a high cut count forces a SHORT DESCRIPTION of a multiscale ambiguity structure. That would be an additional entropy argument. A visiting-order existence theorem alone does not count distinct output pairs, and I have not proved a compression of the full high-cut class.

## 4. A commutative flat is not entropy mass

The constructed macrocontexts A,B commute as outputs and generate `N^2` injectively. Reordering many A/B history blocks can create numerous literal histories of ONE output. Counting those histories as strings would repeat the main overcounting danger in this problem. Even the complete flat has only M+1 outputs at degree LM. Its actual probability and its contribution to the cut mean are exponentially small, by CN3. Thus its linear fibres neither prove a critical regime nor refute a sublinear actual mean.

In particular the result blocks a proposed deterministic containment of the high-cut set in a long-confined-piece set. It does NOT refute the possibility that the high-cut set has vanishing probability under the actual uniform measure. The latter is exactly the remaining issue.

## 5. Other considered bridges that did not close

I reconsidered bounded joining only as an alternative direction. The old note already gives an actual obstruction to all bridges of length at most 2 and only finite evidence about length 3. No unrestricted short-bridge construction was obtained here. The separate `Fstar={RR(LR)^kLL}` countermodel is an old unverified research note about a DIFFERENT language, not an actual-context counterexample or a new theorem imported into CN1--CN3. Its role is to warn that generic non-overlap and ratio information alone cannot select the actual defect.

Likewise, pressure convexity, the existing pointwise bidegree capacity bound, and confinement rarity do not themselves prove differentiability at zero. Recasting the missing cut-count estimate as pressure differentiability would not solve it. No such assertion is made.

## 6. An exact remaining target rather than a renamed solution

For every fixed epsilon>0, define `H_(n,epsilon)={X in R_(2n):k_n(X)>=epsilon*n}`. The elementary bounded-variable equivalence in the main proof shows that

```
|H_(n,epsilon)|/c_(2n) -> 0 for EVERY epsilon>0
```

would be equivalent to sublinear mean cut count and would exclude the finite-second-moment critical regime. A strict entropy bound for H would suffice, but is stronger than necessary. This is a TARGET, not a theorem established by this return.

Any proposed cover/coding argument must include the periodic ladders in CN2, distinguish actual outputs from visiting orders or histories, and bound the description cost of all periods/levels it introduces. The present proof checks the negligible mass only of its specified flat. It does not show that every high-cut output contains such a flat, that periods have bounded length, or that general high-cut outputs are periodic. Those are concrete unresolved inferences. Neither a canonical grammar, a finite-state closure, an exact pressure equation nor an exact numerical lambda has been derived.

The constructive checkpoint is therefore a new actual pointwise obstruction, with its full schedules and quantitative balanced example, plus an explicit mass barrier. Its status remains candidate-unverified pending two other complete whole audits.
