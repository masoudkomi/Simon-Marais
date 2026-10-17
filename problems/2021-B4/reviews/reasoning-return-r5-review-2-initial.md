# Whole initially blind R5A–R5E audit R2

2026-10-17 UTC. Reviewer `review_2022_complexity_r2`. **Independent audit of a candidate proof; no promotion.** No substantive objection found to the five statements in their exact scopes. This is not a proof of degree20, all J15 cases or the annual classification.

The complete 20083-byte candidate, thirty obligations, worklog, source audit, source JSON, constructor self-check and administrative freeze script were read. All seven exact accepted return-r3 mathematical texts, the complete direct prerequisite bodies and acceptance scopes were reread. Actual primary passages were checked as detailed in the source record. Constructor `review_2017_coarsening_r1` wrote R5; root clarified its proposed triple-block counting and is not an independent reviewer. I supplied no R5 construction step. Earlier roles include whole return-r3 audit R1 and the single-center audits; those are disclosed context, not authorship of R5. No new peer R5 findings were read before the complete initial freeze. Requested `gpt-6.1-sol`/`max`; independent effective-setting readback unavailable.

## Domain, normalization and exact dependencies

The official 2021 B4(b) requires a polynomial over Q and, separately for every derivative order, an actual rational common root. A gcd over Q need not supply a rational root. The unused roots may be nonrational, ramified and nonreal. No preliminary prime-degree proof is undertaken.

For a hypothetical nontrivial example of degree d=p+1, p≥5, accepted rational normalization gives

\[
f=X^d-dX^{d-1}+\sum_{j=2}^{d-2}\binom dj a_jX^{d-j},\quad
a_j\in\mathbb Z_{(p)},\quad f(0)=f'(0)=f(1)=0.
\]

The affine change is rational: its repeated-root and center inputs are rational, and the simple center differs from the repeated root. The full accepted normalization body checks the p-integrality and that 1 is the unique unit-valuation root; every other nonzero root has positive valuation. Only rational such roots are assigned positive INTEGER valuations.

The exact monic derivative is

\[
D_j=H_{d-j}(f)/\binom dj
=\sum_{k=0}^j\binom jk a_kX^{j-k},\quad a_0=1,a_1=-1.
\]

This is an equality over Q before any residue reduction. For 2≤j≤p−1, binom(p+1,j) has p-valuation one: its numerator has exactly one factor p and its denominator j! has none. Therefore β_j=binom(d,j)/p is an ordinary integer. H_1 can use 0, and D_1=X−1 fixes the center; no derivative outside the required range is smuggled into the selector.

Accepted Newton theory supplies the long edge with multiplicities. Accepted T1/T3 supply the rational witness-count and triple-zero consequences. Accepted return-r3 supplies RC2 and TA1 with their actual root, ladder, unit and rationality hypotheses; accepted PN4 supplies a separately established incompatibility. The full accepted bodies and their historical-label overrides were checked. None of the new arguments imports an unreviewed R5 packet as a premise, and no finite certificate was rerun.

## R5A: integer identity for every selected-center pattern

Choose any actual rational witness w_j for each j=2,...,d−2 and put w_1=1. Let I consist of 1 and exactly those indices at which the selected witness is 1. This is not the unit support of the a_j modulo p. A center may be chosen even when its coefficient is nonunit, and a noncenter may be chosen when the center is also available. Every parity pattern of I is allowed.

The collapsed b_j are ordinary integers: b_0=1, b_j=0 off I, and b_j=−Σ_(k<j) binom(j,k)b_k on I. In particular b_1=−1. Put F_I(Z)=Σ_(j=0)^(d−2)b_j binom(Z,j). Adding a new largest selected index m leaves all earlier coefficients fixed and gives

\[
b_m=-F_{I\setminus\{m\}}(m),\qquad
F_I(Z)=F_{I\setminus\{m\}}(Z)
-F_{I\setminus\{m\}}(m)\binom Zm.
\]

The published classical recurrence is

\[
d(I;Z)=\binom Zm d(I\setminus\{m\};m)-d(I\setminus\{m\};Z).
\]

Its actual-count domain is integer length greater than m; the smaller set has maximum less than m, so its evaluation at m is legitimate. The concatenation proof chooses the first m values, imposes the smaller descent set in that block and makes the remainder increasing; the join either has a descent or not. Polynomial extension then justifies the identity in Z. Starting with F_empty=d(empty;Z)=1, induction gives exactly

\[
F_I(Z)=(-1)^{|I|}d(I;Z).
\]

There is no complement, reversal, support change or loss of an even index. At length d>max I, the count is strictly positive. A direct realization assigns successively smaller blocks of values to the ascending runs specified by I, increasing inside each run. Every join is a descent, with no unwanted internal descent.

At Z=d, the first two terms are 1−d=−p. The remaining terms are pΣ β_jb_j. Thus

\[
pq_I=F_I(d)=(-1)^{|I|}d(I;d)\ne0,
\quad q_I=-1+\sum_{j=2}^{d-2}\beta_jb_j\in\mathbb Z\setminus\{0\}.
\]

This establishes nonzero integer status for EVERY combinatorial selector, not nonvanishing modulo p.

If no selected witness other than 0 and 1 existed, the exact triangular equations D_j(w_j)=0 would force a_j=b_j for all indices. The center equation would then give F_I(d)=f(1)=0, contradicting positivity. Hence the set defining ν_w is nonempty. Its elements are valuations of actual nonzero rational noncenter witnesses, so their minimum is a finite positive integer. Zero is omitted from this minimum.

Inductively a_j−b_j lies in p^(ν_w)Z_(p). At a center step, subtract the two triangular recurrences and use the previous coefficient congruences. At a noncenter step b_j=0; every term for a_j has the positive exponent w_j^(j−k), so its valuation is at least ν_w. If w_j=0, that term vanishes exactly. All earlier coefficients and binomials are p-integral.

Finally f(1)=0 is the exact divided equation −1+Σ β_ja_j=0. Subtracting gives q_I=Σ β_j(b_j−a_j), whence p^(ν_w) divides q_I in Z_(p), and therefore in Z because q_I is an integer. Multiplication by p gives p^(ν_w+1) dividing d(I;d). This extra exponent is retained. R5A closes the old q_0≠0 qualification only when q_0 is precisely this same collapsed selector constant; the accepted D5 definition has that form.

## R5B: disjoint-block count and the precise minimum bound

For a fixed descent set at length n=3s+t, t∈{0,1,2}, partition POSITIONS into s triples and a possible last singleton or pair. After assigning an unordered value set to each block, each triple has six equipotent relative orders. The internal sign patterns ++,+−,−+,−− permit respectively 1,2,2,1 orders. Thus at most two per triple remain. A last pair permits one of its two orders. Interblock comparisons are simply ignored, enlarging the count.

Equivalently there are n!/((3!)^s 2^[t=2]) ways to assign the block value sets and at most 2^s allowed internal arrangements per assignment. Hence

\[
1\le d(I;n)\le U_n=\frac{n!}{3^s2^{[t=2]}}
\]

whenever the given I is an actual descent set of length n. Independence is used only for disjoint blocks after allocating values. There is no false independence assumption for neighboring, overlapping comparisons. The bound includes the n=2 endpoint.

Since p^(ν_w+1) divides the positive count at d=p+1, that power is no larger than U_d. If K_p is the largest integer with p^(K_p)≤U_d, then ν_w≤v_p(q_I)≤K_p−1. This uses absolute size of the count, not the sign of q_I.

At degree20, six triples and one pair yield U_20=20!/1458=1668657070080000. The displayed arithmetic checks by multiplication: 1458U_20=2432902008176640000=20!. Also 19^6=47045881, whose square is 19^12=2213314919066161>U_20. Therefore ν_w+1 cannot reach twelve, and 1≤ν_w≤10. No table of maximal descent counts or computational search is needed.

This is a bound on the LEAST valuation among selected actual noncenter witnesses for every selector. It does not bound the largest selected valuation, every polynomial root, unused roots, denominators at other primes, global height or a collision difference. “Positive” here concerns p-adic valuation, not a real sign of the rational witness. A cover using only 0,1 and roots in 19^11Z_(19) is impossible. In an equal-valuation J15 branch every eligible nonzero rational noncenter witness has that common valuation ν, so the guaranteed nonempty set has ν_w=ν≤10. With unequal valuations, no such identification is asserted.

## R5C: symbolic unrecycled global carrier

Put J=max{j:v_p(a_j)=0}, h=d−J, e=J−1 and assume J≥d/2. Existence of J follows from the divided center equation: otherwise its reduction is −1=0. Here e≥2, 2≤h<p and e≤p−2.

For ordinary coefficients c_l, the point (h,1) and (p,0) have supporting line L(l)=(p−l)/e. For h<l<p, L(l)<1≤v(c_l). For 2≤l<h, v(c_l)≥2 or the coefficient vanishes, whereas

\[
L(l)\le(p-2)/e<2
\]

because e≥(p−1)/2. The zero constant/linear coefficients do not create points, and the leading coefficient at d=p+1 has valuation zero above L(d)<0. Thus only h and p lie on this edge. The Newton theorem gives exactly e roots of valuation 1/e, with multiplicity.

That root multiset is invariant under the absolute Galois group over Q_p. Its monic product g therefore lies in Q_p[X]. A nonleading coefficient is a symmetric sum of products of a positive number of roots, each summand having positive valuation. It has positive valuation in Q_p, hence integral valuation at least one. The constant term has exact valuation e/e=1. Thus g is Eisenstein, irreducible and separable in characteristic zero. This also rules out concealed repeated roots in that cluster; multiplicities were not assumed absent when forming it.

Choose π in an extension with π^e=p. The weighted coefficient exponents of P(T)=π^(-p)f(πT) are nonnegative and zero only at h,p, by the same strict inequalities. More explicitly low l≥2 have 2e+l−p≥1 at the extreme J=d/2, so no overlooked negative valuation occurs there. Its reduction is

\[
\overline P=-T^p+\lambda T^h,\qquad \lambda=c_h/p\bmod p\ne0.
\]

At a cluster root α, T_0=α/π is a unit and its residue satisfies T_0^e=λ. For every 1≤k≤h, Hasse scaling and reduction give

\[
H_k(f)(\alpha)=\pi^{p-k}H_k(P)(T_0),\quad
\overline{H_k(P)(T_0)}=\lambda\binom hk\overline T_0^{h-k}\ne0.
\]

Here binom(p,k) vanishes modulo p and binom(h,k) is a unit because h<p. Hence v_p(H_k(f)(α))=(p−k)/e exactly, excluding all these derivatives.

Let Q be the monic rational minimal polynomial of α. It divides f, and g divides Q over Q_p because g is α's local minimal polynomial. Thus all e cluster roots belong to this ONE rational irreducible Q, whose degree M≥e. No claim is made that g itself lies in Q[X] when M>e. Any global conjugate of α shared with a rational derivative would force Q to divide that derivative. For k≥h+1, deg H_k=d−k≤e. If M>e, degree excludes it. If M=e, only k=h+1 is unresolved by degree. In that case Q=g over Q_p, and equality with the monic normalized derivative would force

\[
Q=D_e=X^e-eX^{e-1}+\cdots.
\]

But g's X^(e−1) coefficient is divisible by p, while −e is a unit. This excludes the last case. For larger k the derivative degree is strictly smaller. The lower/upper derivative ranges meet without a gap, including h=2, the extreme J=d/2 and the largest possible J. Therefore gcd(Q,H_k(f))=1 for EVERY required order. This excludes every global conjugate, not only the original local cluster points.

It follows that every gcd(f,H_k(f)) divides R=f/Q and deg R≤d−e=h+1. This does not assert that R's own derivatives satisfy the CA conditions. At J15,m=3, accepted T3 gives a rational degree14 quotient after removal of the four rational values with multiplicities; its roots are exactly this cluster. R5C excludes that quotient, so all common-root values in that corollary are rational. This is a support statement, not an exclusion of m=3.

## R5D: the exact RC2 and PN4 conjunction

The setup is precisely normalized d20,p19,J15,m2, H3(1)=0 and H2(1),H4(1) nonzero. Accepted D3 gives the actual rational simple r sharing H2,H4, valuation ν≥1, and two other slots with residue 2R. R5D requires those TWO ACTUAL SLOTS to coincide at a double d_0; equal residues alone do not suffice.

T1 forces d_0 rational: the fractional cluster has no rational root, and otherwise only 0,1,r could cover derivatives. The resulting rational root set is exactly {0,1,r,d_0}, and d_0/r≡2 mod19 makes these distinct. Both exact d_0=2r and finite displacement are included in the setup.

Add the five equations L: H6(r)=H8(r)=H10(r)=H12(r)=H14(r)=0. The accepted RC2 body has exactly this full rational-witness setting and L as hypotheses. In particular its complete top-derivative argument rules out H18(1)=0 uniformly for ν and both displacement cases; it is not a statement deduced just from its surviving finite depths. Thus an actual rational H18 common witness supplied by the contest must be noncenter.

Accepted PN4 excludes exactly this repeated-root sole-H3 setting together with L and an actual rational noncenter H18 witness. Its route is PP2⇒the even-nonunit/H3 conditions of PN3⇒the joint-endpoint contradiction PN2. PN4 does not need an extra odd-unit assumption. Its PP2 proof independently derives the even nonunits and does not use RC2, so the new combination is not circular.

All PN4 hypotheses are now present. Contradiction proves L impossible. In particular the old RC2 necessary depths15,16 do not become realizations after the additional independent PN constraint is imposed. The old conclusions remain byte-identical and were not retroactively rewritten. Distinct 2R slots, a missing ladder equation, other low centers, m3 and lower J are not included.

## R5E: five units and an exact full gcd

Keep that full repeated-root setup without L, and assume only a5,a7,a9,a11,a13 are units. Suppose every one of H6,H8,H10,H12,H14 had a rational noncenter common witness. Start with H2(r)=H4(r)=0 and apply accepted TA1 at m=3,4,5,6,7. Its required coefficient a_(19−2m) is respectively a13,a11,a9,a7,a5, exactly the five assumed units. Each step supplies the preceding even equations for the next one.

The content of TA1 is stronger than a residue match. Its repeated-root Euler identity yields v(H_(2m)(r))≥2ν+1, hence v(D_(20−2m)(r))≥2ν. The unit linear coefficient makes D_j(x)−D_j(y) a unit times x−y for x,y∈19Z_19. The alternative noncenter f-values 0 and d_0 are both at distance of valuation ν from r; neither can be a zero since 2ν>ν. Therefore the stipulated actual witness is r and its derivative value is exactly zero. TA1 permits the center also to be available and both exact/finite displacement, so no center-priority assumption is inserted here.

The five applications give L, contrary to R5D. Some one of those derivatives consequently has no rational noncenter common root. The contest still gives a rational common root; it must be 1, its sole rational common-root value.

For the stronger full-gcd claim, all other root values lie either in {0,r,d_0} or in the degree14 rational carrier obtained by dividing f by X²(X−1)(X−r)(X−d_0)². R5C (or accepted G1) excludes every carrier root from every derivative. Thus there are no additional nonrational common roots for the selected order. Since 1 is a simple root of f, the monic gcd is exactly X−1, and extending the field adds no roots of coprime rational factors. No a3 unit, H16 transfer or three-value cover is used; these belonged to the different old TA2 route.

## Boundaries, attempted shortcuts and disposition

The descendant count may be highly p-divisible while positive; the new argument never asserts q_I is a unit or that finite divisibility suffices to lift. A selected-center pattern is not PN's restricted odd unit support. The bound ten concerns the minimum of a cover, not collision depth15/16 or all roots. The local carrier proof does not make its residual factor CA or the entire polynomial rationally split. Repeated residue does not imply repeated value, and a repeated value does not supply L without the actual-witness/unit transfer hypotheses. Five units are assumptions, not established universal facts. Sole higher center is a compatibility requirement, not a contradiction by itself.

The source's one-nonzero-recycled-root/MacMahon mechanism and the earlier project carrier/transfer mechanisms are attributed. No all-roots-rational theorem, all-real interpolation, prime5 shortcut, universal-proof claim or prime-degree theorem on the degree19 critical-value polynomial closes a missing step. The complete current audit has 54 inference checks covering all thirty obligations. No mathematical program, scan, CAS, mask enumeration or source-certificate rerun was used. No substantive repair is requested. Only the coordinator, after both initially blind whole audits, may accept this scoped candidate.
