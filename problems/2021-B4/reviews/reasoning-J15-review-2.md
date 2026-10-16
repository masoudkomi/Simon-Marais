# Blind whole-argument review 2: J15, double zero

2026-10-16 UTC. **Independent adversarial review; no promotion by this
reviewer.** Reviewed the frozen `reasoning-J15-double-root-candidate-v1.md`,
SHA-256 `e3da7a889e5937722546dab2596fdb2140597066584487ce15fb8c4e4fd8bbff`.
Reviewer: `review_2021_reasoning_j15_r2`. Requested model/reasoning:
gpt-6.1-sol / max, conveyed by the coordinator assignment. Verified
effective-setting readback: unavailable, recorded separately from the
request.

I reconstructed all D1–D5, the coefficient sign, the exact discriminant
identity and the low-order rational family. I found no unresolved
substantive mathematical objection and request no repair. This finding
concerns only the stated analytic restrictions in degree 20, J=15,
multiplicity two at zero; the coordinator alone can accept them after the
second independent audit. Neither J15 as a whole nor degree 20 is solved.

The initial report, issue dispositions and source checks were completed
without reading the other J15 reviewer's files, conclusions or messages.
I did not construct the candidate, consult the residue-intuition table,
edit the candidate, run an enumeration, or use a CAS. Earlier accepted
dependency proofs and their acceptance registers were read as explicit
dependencies; their large finite certificate streams were not rerun here.

## Scope and dependency audit

The official [2021 Paper B, page 2](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf)
requires rational coefficients and a rational common root separately for
each derivative order. The candidate keeps these quantifiers. It never
assumes that all polynomial roots are rational, real, or distinct. Only
B4(b) is investigated; no preliminary proof is reproduced.

I read the accepted rational-normalization packet and
`reviews/witness-acceptance.md`; the Newton packet, its reviewed register
and `reviews/newton-acceptance.md`; the whole small-cluster degeneration
proof and `reviews/degeneration-acceptance.md`; and the whole T1–T3
three-rational-witness proof with `reviews/three-witness-acceptance.md`.
The input-validation JSON records fingerprints and verifies the supplied
candidate manifest.

The imported T1 is a restriction on a **cover by rational recycled
values**, not merely a lower bound on the number of complex roots. It
therefore ensures at least four distinct rational roots for this
candidate. T3 restricts the normalized zero multiplicity to two or three;
the present assumption selects two. No triple-zero quotient is imported.
The 1,493,024-family certificate is an already accepted dependency of T1,
not a new computation in this review.

For clarity, I also reconstructed the needed Newton count. The J=15
supporting line through (5,1) and (19,0) is (19-k)/14. All ordinary
coefficient points other than those endpoints lie strictly above it:
for 6≤k≤18 their valuations are at least one; for 2≤k≤4 they are at
least two while the line is less than two; the leading point (20,0)
also lies above it. Its width fourteen counts fourteen slots of valuation
1/14. The segment from (19,0) to (20,0) supplies the simple center 1.
Strictness of the first supporting line makes the remaining three
nonzero slots have valuation greater than 1/14, besides the two zeros.
Integral valuations of rational numbers exclude all fourteen long-edge
slots from the rational cover. Two distinct small roots must consequently
be rational.

The multiplicity convention was checked directly in
[Stoll, Theorem 3.6, page 16](https://www.mathe2.uni-bayreuth.de/stoll/teaching/pAdicAnalysis-WS2015/Skript-pAdicAnalysis-pub-print.pdf).
For the width-one lemma I independently obtain, after multiplying the
k-th Hasse derivative by u^k and dividing by its leading minimum term,
the residue binom(i+1,k)−binom(i,k)=binom(i,k−1). All uses below have
i∈{2,3,4}<19 and 1≤k≤i+1, so that residue is nonzero. The theorem's
hypotheses, including exactly two minimum exponents, are met by the
displayed initial forms, rather than inferred from simplicity alone.

I checked the normalization and the relevant published hypotheses in
[CLO, §3.4 and Lemma 17](https://arxiv.org/pdf/1208.5404): the rational
affine change uses the rational first-derivative witness and the distinct
rational center. The normalized coefficients are 19-integral, the center
is simple, and all other nonzero roots have positive valuation. Their
Definition 1 uses Hasse derivatives over an algebraically closed field;
Theorem 4 makes 19 good in degree five, as needed by the earlier
degeneration dependency. The two-recycled-value input was checked in
[Draisma–de Jong, Proposition 6, printed pages 31–32](https://www.ems-ph.org/journals/newsletter/pdf/2011-06-80.pdf).
That statement concerns the selected common roots. The separately
corrected degree-family assertion in that article is not used.

## D1: local splitting and coefficients

Fix the unique extension of the 19-adic valuation to an algebraic closure
of Q_19. Its absolute Galois group preserves each valuation cluster and
the root multiset. Removing one copy of each of two distinct rational
small roots leaves one small slot, so every local automorphism fixes its
value. Characteristic zero then gives that value in Q_19. If the third
slot repeats one of the first two roots, it was fixed already. Thus all
three small slots have positive integral valuations, and ν=min ν_i≥1.
This argument proves local rationality only. Global conjugates can have
different valuations at a selected place; no conclusion that the third
root is in Q follows or is needed.

After the five local small factors and X−1 are removed, the degree-14
monic quotient g has all roots of valuation 1/14. Its coefficient of
degree 14−t has valuation at least t/14>0, or is zero. Since it belongs
to Q_19, every nonleading coefficient is in 19 Z_19. The constant
coefficient has valuation exactly one, being a product of fourteen
roots. This is Eisenstein over Z_19, without asserting a quotient over
Q. For B=(X−1)g one obtains v(b_0)=1, b_i∈19 Z_19 for 1≤i≤13,
b_14≡−1 and b_15=1.

Multiplication of X^2(X^3−s_1X^2+s_2X−s_3) by B gives precisely

    c_2=−b_0s_3,
    c_3=b_0s_2−b_1s_3,
    c_4=−b_0s_1+b_1s_2−b_2s_3,
    c_5=b_0−b_1s_1+b_2s_2−b_3s_3,
    c_6=b_1−b_2s_1+b_3s_2−b_4s_3.

Here v(s_t)≥tν. Consequently v(c_5)=1 and the three lower normalized
coefficient bounds in D1 hold after division by 19β_j, a scalar of
valuation one. Dividing the last two equations by b_0 shows
c_5/b_0≡1 and c_6/b_0≡b_1/b_0 mod 19. Thus

    c_6/c_5 ≡ b_1/b_0 ≡ β_14 a_14/(β_15 a_15) mod 19.

This is the positive c_6/c_5 relation for three small factors. It is not
the relation in the triple-zero/two-small-factor situation. No valuation
equality is inferred when the residue vanishes. Also c_2≠0, including
every repeated-small-root case, because b_0,u,v,w are nonzero.

## D2: all unequal-valuation partitions

Here is an explicit integrality justification for every rescaling. At a
scale q=19^t, factor each shallower root as
−u_i(1−qT/u_i), and factor q from every root at least as deep as t.
After dividing by b_0 times these constants and the appropriate power
of q, all resulting coefficients are integral. Indeed B(qT)/b_0 is
integral and reduces to 1: its coefficients through degree thirteen
are integral after division by b_0, while its degrees fourteen and
fifteen gain more than the lost valuation one from q. Shallower-root
factors reduce to 1; deeper roots reduce to zero. This gives the exact
initial forms below. Hasse differentiation commutes with this scaling
and coefficient reduction. Roots shallower than a chosen inner scale
are handled by their own width-one exclusion.

*One outer root and two inner roots.* At the outer scale the initial
form is T^4(T−U). H_4=5T−U is nonzero at 0 and U, excluding all
noncenter H_4 witnesses. The two nonzero coefficient exponents 4,5
give the width-one hypothesis at the outer root, excluding it also for
H_2 and H_3. If the two inner valuations tie, the inner form is
T^2(T−V)(T−W). H_2 at 0 is VW≠0, and at V,W is
V(3V−2W), W(3W−2V). A noncenter H_2 witness thus needs
W/V∈{11,7}. H_3 at 0,V,W is −(V+W),3V−W,3W−V,
needing W/V∈{18,3,13}. The two sets are disjoint. At least one of
H_2,H_3 also uses the center.

*Three distinct valuations.* The intermediate form is T^3(T−V), whose
H_3 values at 0,V are −V and 3V. Together with the outer width-one
exclusion this forces H_3 to the center. The three nonzero roots lie
on the successive width-one edges with endpoint exponents (4,5),
(3,4), (2,3); each excludes H_2. Zero cannot witness H_2 since c_2≠0.
Thus all three low derivatives use the center in this case.

*Two equally outer roots and one deeper root.* The outer form is
T^3(T−U)(T−V). The deeper width-one edge has exponents 2,3 and
excludes the deeper root for H_2,H_3. Zero fails H_2; it also fails
H_3 since b_0uv is the unique term of minimum valuation in c_3.
Evaluating at the outer roots gives respectively
U^2(4U−3V), V^2(4V−3U) for H_2 and
3U(2U−V), 3V(2V−U) for H_3. H_4 has values
4U−V,4V−U there and −(U+V) at 0 or the deeper root. The necessary
ratio sets are {14,15}, {2,10}, {18,4,5}, pairwise disjoint in F_19.
At most one low derivative has any noncenter witness. This completes
the partition argument; neither distinct residues nor distinct actual
roots within a tied cluster was assumed.

## D3: one actual witness from the repeated residue pattern

If only H_3 among the low derivatives uses the center, D2 forces equal
valuations. The reduction is the split polynomial
F=T^5−sT^4+tT^3−zT^2 with z≠0. At a nonzero cubic root R, direct
substitution of R^3=sR^2−tR+z in H_2 gives
R(9R^2−5sR+2t). H_3 and H_4 give 10R^2−4sR+t and 5R−s.
The H_2 witness cannot reduce to zero because H_2(F)(0)=−z.

If an H_4 witness reduces to zero, s=0. For an H_2 witness R,
t=−9R^2/2; the other roots have sum −R and product −7R^2/2.
Their discriminant is 15R^2. The nonzero squares of F_19 are
{1,4,9,16,6,17,11,7,5}, excluding 15, a contradiction to splitting.

Otherwise let S be an H_4 witness residue, so s=5S. The other two
residues A,B have sum 4S. An H_2 witness among those would solve
7A^2−17SA+8S^2=0, whose discriminant is 65S^2=8S^2; 8 is also
nonsquare. The quadratic has nonzero leading coefficient and S≠0,
so there is no degenerate exception. No root difference was divided out.
H_2 must therefore use S. Its equation forces t=8S^2 and then
AB=4S^2 with A+B=4S, yielding A=B=2S.

There is exactly one root slot with residue S. Both actual rational
H_2 and H_4 witnesses must lie in that slot, so they are the same actual
root r, which is rational over Q. This inference would fail if it only
identified equal residues in a multiple slot; uniqueness supplies the
needed exact conclusion. The other two slots may coincide, and their
Q-rationality is never used. H_3 at 0,S,2S has the nonzero residues
8S^2,−2S^2,8S^2. All zero and repeated-root edge cases are included.

## D4: exact equations, sign and parity

Let A=a/r, B=b/r and C(T)=B_res(rT)/B_res(r). The denominator has
valuation one. For k=1,2,3 every term in H_k(B_res)(r) is divisible
by 19: the coefficients through degree thirteen have that factor,
and the last two terms have valuation at least (14−k)ν≥11.
Thus c_k=r^k H_k(B_res)(r)/B_res(r) belongs to 19^{kν} Z_19.

The factor (T−1) in f(rT) converts H_2(f)(r)=H_4(f)(r)=0 exactly
to H_1(PC)(1)=H_3(PC)(1)=0. There is no dropped factorial or
nonunit reduction. For P=T^4−sT^3+tT^2 and L=P(1), the first
equation is 2−s+(2+c_1)L=0. Substituting this into the second gives

    D L=2+c_1,
    D=2+4c_1+2c_1^2+c_1c_2−c_3 ≡2 mod 19.

The denominator is a unit throughout, including c_1=0 and repeated
roots. Hence s=2+(2+c_1)^2/D and
t=1+(2+c_1)(3+c_1)/D. An independent short expansion is

    s^2−4t=(2+c_1)((2+c_1)^3−4D)/D^2
          =(2+c_1)(c_1^3−2c_1^2−4c_1(1+c_2)+4c_3)/D^2.

This is precisely (*). Since c_1∈q Z_19, c_2∈q^2 Z_19,
c_3∈q^3 Z_19 and q=19^ν, it reduces to −2c_1 mod q^2. The
negative sign follows both from this expansion and the positive
three-factor coefficient ratio checked in D1.

If a_14 is a unit, H_1(B_res)(r)/B_res(r) has the nonzero residue
b_1/b_0=β_14a_14/(β_15a_15). Thus v(c_1)=ν and every other term
in (*) has strictly greater valuation. The square (A−B)^2 is nonzero
of valuation ν. Its valuation must be even, and after division by
19^ν its residue is the nonzero square
−2Rβ_14a_14/(β_15a_15). In particular ν=1 is impossible. If a=b,
this unit subcase is automatically impossible; outside it (*) still
allows zero and no parity assertion is made.

## D5: direct center-constant valuation bound

The exact normalized derivative identity is
D_j=H_{20−j}(f)/binom(20,j), a polynomial in Z_(19)[X] with
coefficients binom(j,k)a_k. Thus its common roots coincide with the
ordinary derivative roots over Q before any reduction. Solving its
value at a selected witness w_j gives the stated recursion, with no
division by an unknown or a root difference.

Choose the center whenever available. Every other rational witness is
zero or a small root in 19^ν Z_19; the long-edge cluster is unavailable
and a non-Q root cannot be chosen. Induction gives a_j≡a_j^0 mod q:
at a noncenter position all terms in its recursion contain w_j to a
positive power, while at a center position the differences are integral
linear combinations of earlier differences. The zero-replacement
coefficients a_j^0 are actually integers.

The exact equation f(1)/19=−1+Σβ_ja_j=0 now gives q_0≡0 mod q.
For q_0≠0 this is ν≤v_19(q_0); q_0=0 yields no finite bound and
is expressly outside that implication. Also a_14≡a_14^0 mod 19.
The corollary with v(q_0)=1 and a_14^0 a unit consequently forces
ν=1 and then contradicts D4. It excludes only a multiplicity-two
realization of that canonical mask. The author correctly requires a
separate multiplicity-three exclusion before deleting a whole J15 mask.
No enumeration total is a consequence of this review.

## Explicit family: analytic verification and limitation

For any nonzero rational r∈19 Z_(19), d=1−r is a nonzero unit and
L=20−19r. The displayed P_r,Q_r and B_r are rational polynomials.
Modulo 19, Q_r=X^5−X^7, so H_3(Q_r)(1)=−25 is a unit and the
definition of K(r) never has a vanishing denominator in this domain.

The high-degree product is
X^2(X−r)^15(X−2r)^2(X−L). Its X^19 coefficient is exactly −20.
Its X^18 coefficient is 380r−192r^2; all other deviations from the
r=0 product have a factor r^2. Because 19 divides 380 and r, these
deviations are divisible by 19^2. The added degree-seven term divided
by 19 has the same reduction as X^7. At r=0, therefore,
H_3(P_0)(1)/19=60−1020+35=−925 and H_3(Q_0)(1)=−25,
giving K≡−37≡1 mod 19. In particular K is integral and nonzero.

The exact identity 1−L=−19d gives B_r(1)=0. Its reduction is
X^14(X−1), and B_r(0) has valuation one since its constant term
19K dominates the terms containing r^2 or r^14. Consequently
g_r=B_r/(X−1) is monic degree fourteen and Eisenstein over Z_(19).
It has no Q_19 root; the rational root set of f_r is exactly
{0,1,r,2r}, with 1 simple. All binomial-normalized a_j are integral
because f_r mod 19=X^19(X−1). The coefficient of X^5 has valuation
one, and the coefficients of X^2,X^3,X^4 have larger valuations, so
J=15. The coefficient of X^2 is nonzero, giving exact multiplicity two
at zero. These statements hold for arbitrary allowed rational r, not
just an integer example or a finite search.

At r the first and third Hasse derivatives of B_r vanish: the high
factor has multiplicity fourteen and the correction is quadratic in
X−r. The remaining factor X^2(X−2r)^2 is even about r. Thus
H_2(f_r)(r)=H_4(f_r)(r)=0 exactly. The chosen K forces H_3(f_r)(1)=0.
The divided center residues are independently

    H_2(f_r)(1)/19 ≡ (10−180+21)+(−37)(10−21)=258≡11,
    H_4(f_r)(1)/19 ≡ (255−4080+35)+(−37)(5−35)=−2680≡−1.

Hence H_2 and H_4 really fail at the center. Also B_r'(r)=0 implies
b_1/b_0≡0, and D1's ratio then gives a_14≡0; the family belongs
to the nonunit branch. Here A=B=2 and c_1=c_3=0, so (*) gives zero
exactly, rather than a forced odd valuation.

This is an unrestricted analytic family for the **low-order** conditions.
It does not impose every normalized derivative equation and hence does
not supply a canonical full derivative mask or a Casas–Alvero
counterexample. It refutes the attempted inference from the repeated
residue collision alone to a contradiction, but not any stated D1–D5.

## Disposition and resources

No proof repair, further enumeration, height search or CAS test is
required by this audit. The unresolved branches are exactly the limits
stated by the author: other equal-valuation low-center patterns, the
nonunit branch beyond (*), multiple low center equations, multiplicity
three, and lower J. No claim is made that retained masks lift.

At 2026-10-16 21:49:26 UTC, the authoritative account-wide codex
10080-minute window reported 17% total used, reset 1792745187. This is
below the 90% total-used cutoff; no separately billed API was used.
All writes are confined to this review's assigned filename prefix.
The proof, unrelated work, shared status files and Git state were not
modified. Source links and input/output fingerprints are frozen with
the report. Full papers were read through the web tool; no third-party
PDF was added to tracked files.
