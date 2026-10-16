# 2021 B4 research log

Status: first investigation checkpoint, 2026-10-16. No full solution claimed.
All proposed arguments remain **candidate proof - unverified**. No candidate
has received the two required independent adversarial audits.

Requested worker setting: `gpt-6.1-sol`, reasoning `max`. This was explicitly
requested through the launch interface by the coordinator. Verified effective
model/effort readback was unavailable; the request is not a verified readback.
The coordinator monitors authoritative account-wide weekly telemetry and owns
Git checkpoints. This worker made no commits, pushes, installs, or shared-file
edits, and spawned no agents.

## Statement checks

See statement.md and official PDF. The contest requires a rational shared root
for each derivative, not merely a nonconstant gcd over Q. The latter is a
strictly weaker general formulation; known general positive results apply to
the contest but a statement about arbitrary rational coefficients alone does
not erase the shared-root field requirement. Part (a)'s prime-degree result is
used only as attributed context; it was not investigated or reproduced.

## Approaches and results

### Present-day status audit

The literature record does not justify labeling all degrees solved. The active
Ghosh preprint claims all degrees, but an August 2026 research preprint
explicitly withholds independent verification. The 2015 Battiston and 2017
Dobrowolski universal-proof claims are withdrawn for acknowledged errors. The
accepted Ghosh finiteness paper is a different work. Source versions, dates,
publication distinctions and the 20-versus-24 frontier discrepancy are saved
in references.md. No specific flaw in Ghosh's current proof was established
by this initial pass. It would be misleading to call it refuted or accepted.

### Route 1: integral normalization and local arithmetic

The rational witness tuple admits a centered monic integral normalization with
primitive integer witnesses. The proof uses a triangular Hasse recurrence,
without integrality assumptions on nonwitness roots. A sufficient local test
then asks for absence of nontrivial centered polynomials over F_p with shared
F_p-roots. This potentially needs less than absence over the algebraic closure,
but no new successful prime was established. Both reductions, with explicit
hypotheses, are candidate lemmas in proof.md.

The easiest attempted primes fail concretely: for both d=20 and 24 and every
p in {2,3,5,7,11}, the saved exact run finds x^d-x^m over F_p with the required
Hasse conditions at 0 and 1. This is a known bad-prime mechanism, attributed
in proof.md. Thus rationality of the witnesses does not itself eliminate
small-field failures. A higher p-adic lifting obstruction remains possible;
the finite-field examples were not claimed to lift to Q or Q_p.

### Route 2: exact elimination for two lower terms

For a centered trinomial x^d+A x^a+B x^b, H_b and the shared-root equality
express A,B in terms of its nonzero witness v. The other active condition at
u gives two power equations for t=u/v. A binomial-ratio equality is necessary
even for complex t. The candidate derivation is in notes/two-support.md.
An exact Fraction-arithmetic script checks all exponent pairs in degrees
20,24,28,30: respectively 153,231,325,378 pairs, no equality. This removes
rational-height bounds for the scanned trinomial family, but is finite
computational evidence and is not an unrestricted support theorem. It is
related to the two-support result in Marashdeh's preprint; no novelty claimed.

The obstruction is structural: the next family has three lower terms and up
to three nonzero witness values. Two active conditions no longer determine
both coefficients as functions of a single ratio. General resultants or
Groebner computations have not been run, since their cost needs a separately
monitored plan.

### Route 3: sparse integer-witness interpolation search

The triangular Hasse equations reconstruct coefficients exactly for any fixed
support and witness tuple. For d=20,24,28,30, all supports of at most three
lower terms and all nonzero witnesses in {-2,-1,1,2} were considered. Gcd and
reflection symmetries skip equivalent tuples. In total 544616 tuples were
visited, 237112 were solved after those filters; none satisfied all shared
polynomial-root equations. Each discovered finite-field example was also
independently checked by direct evaluation of every Hasse derivative.

These are exact arithmetic searches, not numerical root approximations. They
cannot exclude witnesses of larger normalized height, more than three lower
terms, or general complex coefficient configurations. The support restriction
and witness-height restriction are independent and both are recorded in the
script and exact output.

### Route 4: real geometry and high derivatives (not completed)

After centering, the coefficient of x^(d-2) must be
-binom(d,2) s_(d-2)^2 because that Hasse derivative is quadratic and its
witness is rational. This gives a square constraint and a nonpositive
coefficient. It does not imply that all roots of f are real. Neither Rolle's
theorem nor a sum-of-squares argument can be applied to all roots from the
contest's rational shared witnesses alone. Even the real-root version of
Casas-Alvero should not be casually asserted solved: the primary Draisma-de
Jong exposition explicitly invited progress on that subcase. This route was
stopped at the precise missing implication instead of assuming real-rootedness.

## Next steps

1. Obtain two fresh independent adversarial audits of the candidate reductions
   if the coordinator wishes to promote any lemma. One reviewer must reconstruct
   the full argument. Reviewers must not see one another's first reports.
2. Verify the binomial-ratio elimination with an independent symbolic
   reconstruction; decide whether a general inequality adds value beyond the
   attributed 2026 support theorem.
3. For a focused new-degree attempt, test higher p-adic lifting constraints on
   normalized primitive witnesses. The displayed small-field examples explain
   why mod-p emptiness at the smallest primes is unavailable.
4. A type-three scenario elimination in degree 20 is substantially more
   targeted than unrestricted coefficient search. Before attempting it, check
   new primary-source claims and bound the computation's runtime.
