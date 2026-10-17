# Initially blind whole R6 review2

2026-10-17 UTC. Reviewer `review_2022_complexity_r2`; requested
gpt-6.1-sol/max, independently verified effective-setting readback
unavailable. Target: COMPLETE17290-byte
`notes/reasoning-return-r6-candidate-v1.md`, SHA256
`ad49ac369ce903131ad496b0e0f70fe2b966dca7507490860449bdde36eb7594`,
and its entire eight-artifact freeze, all36 obligations, source/log
records and exact accepted premises.

**Disposition: no substantive defect identified in R6A–R6C in their
stated restricted scopes.** I reconstruct the Euler estimate, exact
quadratic cancellation, both actual even-witness cases, adjacent odd
obstruction, nonzero nonunit essential constant, first-break fork and
five-pair application below. No repair is requested. This is a scoped
independent audit recommendation, not coordinator acceptance, a whole
repeated-root exclusion, or a degree20/annual solution.

I did not construct R6, provide its quadratic comparison, or receive
its proof from a peer reviewer. I previously reviewed the separately
accepted seven return-r3 bodies as whole R1, the later R5 packet as
whole R2, and earlier single-center context. Those are OLD roles,
not construction of R6. I read complete accepted bodies and scopes
again for the present interfaces; I do not claim to rerun or freshly
recertify the old large finite certificates. Root's NEW R6 report,
ledger, source checks and conclusions remain UNREAD until this complete
initial report/ledger/source/integrity freeze. No future2017 global-value
packet or its new review is a premise.

## 1. Official hypothesis and reset of every branch condition

The actual official2021 Paper B page2 requires rational coefficients
and an ACTUAL RATIONAL common root for each derivative order. Other
roots need not be rational or real. Only(b) is investigated; no
prime-degree preliminary proof is reproduced.

The new setting is degree20 at prime19, rational affine normalization,
J15, zero multiplicity EXACTLY2, and the sole-H3 low pattern
H3(1)=0, H2(1)!=0, H4(1)!=0. The center1 is simple. The accepted Newton
body gives fourteen fractional root slots of valuation1/14, two slots
at zero, the simple center and three further small slots. Accepted
D1/D3 puts these last slots in Q19 with equal positive INTEGER
valuation nu. One slot r is simple and rational, and the SAME actual
r shares H2 and H4. The other two slots reduce to2r after division
by the scale; equal residues do not make them one root.

R6 adds the genuine repeated-root hypothesis that those two slots
are one double root s. If s were not rational, only0,1,r could be
rational roots, contrary to accepted T1's four distinct rational
witness requirement. Thus s is rational. Its ratio s/r reduces to2,
so s differs from0,r,1. Rational division now, and only now, gives

    f=X²(X-r)(X-s)²(X-1)g,  deg g=14,

with g over Q and Eisenstein locally at19. This quotient is not a
generic local factor assumed rational. It has no rational root.
The rational root set is exactly{0,1,r,s}. Accepted G1, or the full
accepted R5C argument, also excludes EVERY algebraic root of g from
EVERY derivative. That last input is needed for the full-gcd assertion,
not just for selecting rational witnesses.

I checked R5C's local/global interface: the14-slot local Eisenstein
factor divides the global minimal polynomial; low derivatives have
nonzero scaled Hasse evaluations. For a degree14 carrier the only
degree-equality derivative would have monic X13 coefficient-14,
whereas the Eisenstein factor's coefficient is divisible19. Thus no
extra nonrational common root enters the final gcd. The residual factor
is not asserted Casas–Alvero.

## 2. Euler estimate and all displacement endpoints

Put e=2m, j=20-e and assume precisely the preceding ladder
H2(r)=H4(r)=...=H_(e-2)(r)=0. The even Taylor part is

    E(T)=T^(2m)A_m(T²),
    A_m(Z)=h_e+h_(e+2)Z+...+Z^(10-m).

Here h_e=H_e(f)(r), h20=1; all intervening even coefficients belong
to19Z19 because the MONIC normalized derivative D_j is integral before
reduction and binom(20,j) has valuation1. No division by19 is performed
inside the residue field.

For B=(X-1)g, its constant term has valuation1, degrees1..13 have
a19 factor, degree14 is a unit and degree15 is monic. At2r, the
constant uniquely has valuation1. In B'(2r), the two high-degree
terms have valuations at least13nu and14nu; all lower terms retain
their19 factor. Hence v(B(2r))=1 and B'/B at2r is integral. Thus for
U=X²(X-r)B,

    U(2r)=4r³B(2r)!=0, v(U(2r))=3nu+1,
    eta=U'(2r)/U(2r)=2/r+an integral element.

Let delta=s-2r. If nonzero, Delta=v(delta)>nu; its zero case is
retained separately. Using f(0)=f'(0)=0 and f=(X-s)²U gives

    E(r)=delta²U(2r)/2,
    E'(r)=delta²U'(2r)/2-delta U(2r).

The minus sign is correct: differentiating the reflected term introduces
it, and2r-s=-delta. Subtracting(2m/r)E(r) yields

    2r^(2m+1)A_m'(r²)
       =-delta U(2r)[1+delta(m/r-eta/2)].

For finite delta the bracket is a unit, as the added term has valuation
at least Delta-nu>0. For3<=m<=8, A_m has degree at least2. Its
nonleading differentiated coefficients have a19 factor and its leading
term at r² has a positive r-power. Therefore v(A_m'(r²))>=1. The
Euler identity also makes that derivative nonzero in the finite-delta
case. Equating valuations gives

    Delta=(2m-2)nu-1+v(A_m'(r²)) >=(2m-2)nu,
    v(A_m(r²))=2Delta+(3-2m)nu+1 >=(2m-1)nu+1.

If delta=0, the first reflection equation instead gives A_m(r²)=0;
there is no division by delta or assignment of a finite valuation to it.
Every nonconstant nonleading term of A_m(r²) has valuation>=2nu+1,
and the leading term has valuation>=4nu>=2nu+1. Subtracting gives
v(h_e)>=2nu+1 and v(D_j(r))>=2nu. Expanding D_j(r) around0 with
integral coefficients then gives v(a_j)>=nu. This last bound uses no
extra coefficient unit hypothesis.

These inequalities include nu1 and all finite Delta>nu, with no upper
bound on either. R5's minimum selected-witness depth10 is never used
as a maximum root/displacement bound.

## 3. R6A: exact even value and every actual-witness split

Assume3<=m<=7 and u=a_(j-2) a unit. Then
h_(e+2)/19 reduces to beta_(j-2)u, a nonzero residue. In A_m(r²)
the term h_(e+2)r² has valuation2nu+1; all later nonleading terms
have valuation>=4nu+1. The top term has valuation jnu>=6nu,
strictly higher even at nu1,m7. A_m(r²) has still higher valuation
or is zero. Consequently h_e must cancel this first nonconstant term:

    v(h_e)=2nu+1,
    D_j(r)/(ur²)=-c mod19,
    c=beta_(j-2)/beta_j
      =j(j-1)/[(2m+1)(2m+2)] in F19*.

The exact binomial ratio fixes both the normalization and sign.
Every denominator is a19-unit. This is a tied-two-term cancellation,
not an invalid use of a unique least Taylor weight.

If H_e has no rational noncenter common root, the official hypothesis
supplies1 as its sole rational common-root value. Its constant a_j
has valuation>=nu and is NONZERO: a_j=0 would make0 a common root.
The carrier input and simplicity of1 then give full monic gcd X-1.
This handles one entire case without choosing a noncenter witness.

Otherwise choose an actual rational even witness w. Nonvanishing of
h_e rules out r, so the complete possibilities are w0 and ws. In
both cases v(r-w)=nu, including ws because s/r reduces to2. Write

    D_j(X)=a_j+j a_(j-1)X+b uX²+sum_(l>=3)c_l X^l,
    b=j(j-1)/2, c_l integral.

The difference quotient between r and w has valuation nu. Its
expansion is j a_(j-1)+bu(r+w)+terms of valuation>=2nu. A value
v(a_(j-1))<nu would be its uniquely smaller term, impossible. Thus
v(a_(j-1))>=nu. The actual root equation gives v(a_j)>=2nu; at w0
it gives a_j=0 exactly. No converse to that last observation is needed.

After X=rz and division by ur², the integral initial quadratic is

    Q(z)=C+j ellbar z+bz²,
    C=a_j/(ur²) mod19, ellbar=a_(j-1)/(ur) mod19,
    Q(1)=-c.

Higher terms vanish since their scaled valuations are at least
(l-2)nu>0. The case w0 gives Q(0)=0 and j ellbar=-b-c. The case
ws gives Q(2)=0 and j ellbar=c-3b. The latter uses s/r=2 only as
a residue; it never replaces the actual rational s by2r.

Suppose the adjacent H_(e+1) had an actual rational noncenter common
root zeta. Its only possibilities are0,r,s. Thus y=zeta/r reduces
to0,1,2. The monic normalized derivative D_(j-1), divided by ur,
reduces at zeta to ellbar+(j-1)y; all terms of degree>=2 vanish.
Its zero equation combined with the preceding quadratic gives

    w0: y=rho_m=1/2+1/[(2m+1)(2m+2)],
    ws: y=2-rho_m.

I reconstructed the finite obstruction by directly inverting each
product, rather than relying on the constructor's exceptional-set table:

|m|Product mod19|Its inverse|rho_m|2-rho_m|
|---|---|---|---|---|
|3|18|18|9|12|
|4|14|15|6|15|
|5|18|18|9|12|
|6|11|7|17|4|
|7|12|8|18|3|

All entries in the last two columns are outside{0,1,2}. This is
a complete five-case HAND certificate for the actual bounded m range,
not enumeration used to infer an unbounded valuation statement. The
equivalent exceptional product residues are-2,2,2/3, namely17,2,7.
Both routes give the same contradiction to the odd noncenter witness.

The official odd witness must therefore be1. Also the quadratic
equations ALONE give ellbar=-(j-1)rho_m or-(j-1)(2-rho_m).
These are nonzero by the table, without assuming an odd witness
exists. Hence v(a_(j-1))=nu exactly. This checks the NONZERO NONUNIT
constant claim as well as sole-center existence. Again G1/R5C and
simple1 give the full monic gcd X-1 over an algebraic closure.

The automatic unit-constant center at e+2 is different: u itself
prevents0,r,s as roots of D_(j-2). R6A finds an EARLIER center with
nonunit constant. It does not advertise that trivial unit-center
observation as the new restriction.

## 4. R6B/R6C: first break, exact accepted composition and coefficient pairs

Accepted R5D has no additional unit hypothesis. In the full sole-H3
ACTUALLY repeated2R branch it excludes the five equations
H6(r)=H8(r)=H10(r)=H12(r)=H14(r)=0 together. I checked that its two
accepted premises match: RC2 rules out center1 for H18 under precisely
that full ladder (including the exact delta0 case); full rational
witnesses then supply a noncenter H18 root, which PN4 forbids in
precisely that repeated-root/ladder setting. No PN certificate rerun,
new parity assumption, or missing actual repetition is substituted.

Thus the first broken even equation occurs at some m0 in3,...,7.
All earlier even equations hold, including the original H2/H4 input,
so the general Euler estimate applies there.

At that break, absence of an even rational noncenter witness gives
the even essential center and nonzero a_j of valuation>=nu. If such
a witness exists and a_(j-1) were a unit, accepted TA1 would force
that ACTUAL witness to r and hence the broken equation to vanish.
Its preceding ladder, unit LINEAR coefficient and witness-existence
hypotheses are all present, so this is a valid contrapositive even
if the center is another witness too. Therefore a_(j-1) is nonunit.
If a_(j-2) is also nonunit, the double-nonunit alternative holds;
otherwise R6A supplies the odd essential center with exact constant
valuation nu. This proves R6B's fork. Its alternatives may overlap,
and neither is unconditionally excluded.

For m3,4,5,6,7 the pair(a_(j-1),a_(j-2)) is respectively

    (a13,a12),(a11,a10),(a9,a8),(a7,a6),(a5,a4).

The five OR-unit assumptions exclude the second fork alternative
at whichever first break actually occurs. The essential order is
e or e+1, hence6<=k<=15, and its normalized constant is nonzero
with finite valuation>=nu. This is R6C. The paired assumptions are
a Boolean weakening of all five odd units, not a theorem that every
surviving polynomial satisfies them. The old R5E conclusion remains
even-only under its stronger all-odd-unit hypothesis; no even-only
conclusion is claimed here under the weaker OR hypotheses.

## 5. Adversarial endpoints, source boundaries and remaining gaps

At m8, (17*18) mod19=2, giving rho=1. I checked the displayed local
quadratic6z(z-2), ellbar=-3 and odd linear3(y-1): Q(1)=-6, and
the odd scaled root y1 is the noncenter r, not the original center1.
These are consistent LOCAL residue equations. They are not a local or
rational lift satisfying every derivative; under full witnesses the
preceding H14 ladder is already excluded by R5D. The candidate correctly
does not extend its five-product obstruction through that endpoint.

I challenged finite and exact displacement separately, zero coefficients,
all valuation ties, w0 versus ws, a possible noncenter witness coexisting
with the center, normalized versus ordinary derivatives, the maximum
allowed m, nu1, nonrational carrier conjugates, and repeated-root
multiplicities in the gcd. The stated proof handles them. No extra
assumption of rationality from Q19 membership or actual s=2r was used.

Original CLO normalization/monic-derivative passages were directly
checked, together with its all-roots-rational/unramified-field restriction.
That theorem cannot be imported here: the degree14 cluster has fractional
valuation1/14. Marashdeh's centered support and full displayed TheoremB
have the one-nonzero-recycled-root/nonvanishing boundary, not this
four-rational-value conclusion. R6 imports no theorem from that preprint.
The accepted prime5 correction and narrow Ghosh source-objection
register remain context; neither closes the universal problem or is
newly recertified here. Actual source-read limits are listed separately.

The first-break fork still leaves an essential nonunit center OR two
successive nonunit coefficients. The OR hypotheses are not established
universally. Distinct2R slots, other low centers, multiplicity3, lowerJ,
all full masks and degree20 remain outside the new conclusion. No
counterexample, ordinary rational lift, source refutation, larger cutoff,
novelty or complete classification has been obtained.

All36 author obligations and48 review inference checks are recorded
in the full ledger. No mathematical program, CAS, scan, old author
rerun or certificate replay was used. Administrative hashes preserve
the exact candidate and earlier own artifacts, including the completed
2022R5 construction and2020r4 repair. No new R6 peer finding was read
before this entire initial report/ledger/source/manifest freeze.
