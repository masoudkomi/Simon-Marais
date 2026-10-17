# R9 failed routes, boundary checks and remaining obstruction

2026-10-17 UTC. **Candidate proof - unverified.** The following records
conceptual work and exact hand diagnostics, not a mathematical scan.

## 1. Four rational witnesses are not four total polynomial roots

The actual degree20 branch has fourteen carrier roots in addition to
0,1,r,s. They are unramified neither locally nor by assumption, and
they need not be real. A theorem about a polynomial with only four
TOTAL roots, or with ALL roots real/rational, cannot eliminate it.
Likewise f/g is a degree-six rational factor but has no established
CA property for its own derivatives. Reusing the already accepted
global degree14 carrier would add no new inference.

The productive replacement is R9A: Hermite--Birkhoff interpolation
places constraints at four selected real nodes without asking that
the rest of the roots be real. Its theorem is invoked only in the
proved conservative/Pólya direction. An incidence matrix with odd
supported runs need not be realizable or singular at the actual nodes.

## 2. Why the four-run obstruction alone does not eliminate a cubic

Here is ONE hand-written formal assignment, not a search. Consider
the first m4 row and suppose the ordinary interior pair is{0,s}.
Use the fixed entries f(0)=f(s)=f(r)=f(1)=f'(0)=f'(s)=0, and select:

    order: 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
    value: r 1 r 1 r 0 0 0  s  1  0  1  s  1  1  1  r  1

This respects the displayed low supports, the preceding H6(r)=0
and the cubic's actual triple at8,9,10. In the0 row, the positive
interior runs are7--9 and12; in the s row they are10 and14. All
four are odd. Their initial0--1 blocks do not count. Thus the new
run lower bound is not by itself a combinatorial contradiction to
the already forced m4 incidences. The assignment does NOT provide
the coefficients, establish any unspecified zero/nonzero value,
verify all other accepted restrictions or realize a polynomial over
Q19 or Q. No sufficiency, actual solution or lift is inferred.

R9B is stronger than merely finding four entries in a convenient
word: the bound holds for EVERY choice, so at least four orders must
have no endpoint witness available. Their gcds can share the same
interior value or involve both. This still does not force four new
essential single-root orders.

## 3. High19-adic collision depth gives no ordinary ordering

Fix nu=1 and a putative cubic depth Delta=7. The rational numbers

    r=19, delta=19^7, s=38+19^7

obey v(r)=v(s)=1, s/r=2 mod19 and v(s-2r)=7. Their ordinary order
is0<1<r<s, so the interior pair is{1,r}. On the other hand take

    r=-19, N=(19^6-1)/2,
    delta=19^7/N, s=38/(19^6-1).

Then N is an integer19-unit, delta=s-2r, and the SAME three
valuation conditions hold. This time r<0<s<1, so the interior pair
is{0,s}. Both are elementary rational diagnostics ONLY; neither is
claimed to occur in a CA polynomial. They show why the explicit
four noncenter-only orders in R9B require the stated ordinary
geometry case and cannot be inferred from the cubic congruence.

## 4. The derivative of the even part is stronger, but finite depth survives

Initially one might try the older estimate for W(r^2) again. That
estimate underlies R8's cubic relation and does not distinguish its
four surviving forms. Using the exact ACTUAL double root in the
identity for W'(r^2) does distinguish zero from finite displacement.
All four cubic forms have nonzero Q''(1), forcing W' nonzero and
the exact depth in R9C. The reflection preserves that depth; it
does not turn it into an inconsistency.

At sigma=nu the strict comparison fails. The first and later terms
of W' can tie. No unique-leading-term claim is made there. This
boundary belongs to the deeper weighted range, not to the cubic
calculation with sigma<nu. Under T4, W' can vanish, and exact
delta0 remains compatible with the identity. For finite delta the
depth only satisfies a lower bound Delta>=e nu.

## 5. Minimum depth and global height remain distinct

The accepted selected-witness bound nu<=10 does not bound the
largest coefficient valuation, displacement depth or global rational
height. R9C obtains an upper depth ONLY after assuming an actual
cubic alternative and proving its exact formula. No such bound
exists here for T4. Rational numbers with large19-adic valuations
can have unbounded numerators and denominators at other primes.
A global rational-height theorem is not supplied by compactness,
finitely many residue masks, or a tame local carrier.

## 6. Literature routes retained with exact limitations

Massri's degree20 three-recycled-root theorem concerns a cover by
three values. Removing an essential member from the accepted four
values has not been justified. Its reported finite resultant work
is attributed and is not rerun or extended to four values here.
Marashdeh's single-nonzero-root descent obstruction and two-element
support cases do not classify this four-value, many-coefficient
branch. Claimed universal CA solutions encountered in search are
not accepted premises.

CLO's all-roots-rational/unramified theorem cannot be weakened to
rational recycled values; the degree14 ramification is explicit.
Known prime5 corrections remain in force. No dyadic stability,
automatic normality, simultaneous residue lift or arbitrary local
path to rational polynomial is inserted.

The remaining target is an ACTUAL rational/global contradiction
compatible with all derivative equations. R9 narrows its necessary
geometry and depth; it does not supply that contradiction. No CAS,
mask table, larger parameter scan, mathematical program or author
certificate replay was run in investigating these routes.
