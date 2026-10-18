# Independent whole R5 audit 2: coefficient Frobenius and the actual cofactor

18 October 2026 UTC. Reviewer B, `/root/review_2022_complexity_r2`.
Requested inherited gpt-6.1-sol/max; independently verified effective
readback unavailable. This ENTIRE initially blind audit covers R5A--R5D,
ALL32 obligations, the complete nine-file submission, exact operative
accepted inputs, sources, administrative code and ALL metadata. It is
not a review of endpoints alone and does not promote the candidate.

## Whole disposition and exact reviewed version

**PASS the stated mathematical partials, with one nonblocking editorial
arithmetic correction explicitly recorded in CFR5R2-N1.** There is no
substantive mathematical defect, required mathematical author repair or
unresolved mathematical objection. The printed assertion that `2^s-1`
is `2 modulo3` for odd s is false: its residue is1. The required
conclusion `3 does not divide 2^s-1` is correct, and the complete orbit
argument below proves it with the correct residue. I have not edited
the candidate or silently treated that printed equality as true.

Exact main: `notes/cofactor-Frobenius-r5-candidate-v1.md`,12486B,
SHA256 `ff29bb1757d3f24229cb138bdfcca02b4d45c457200afc2ecc78104918c823ee`.
Exact constructor freeze: `notes/cofactor-Frobenius-r5-freeze-v1.json`,
3932B,SHA256 `cda866d3b82dfe335c78643d15d857e21bcda5439c2ecf308956281b02a8b545`.
Both are in `problems/2024-B4/`. The eight payloads and the freeze
were fully read, including the source/failure records and metadata-only
Python. The author baseline's23 guard paths and all eight payload
fingerprints were independently checked by NEW metadata-only reading;
no author script was executed. The complete audit ledger reconstructs
every CF-01--CF-32 inference.

Root alone constructed this NEW R5 proof and is excluded. I supplied
no new R5 construction inference. My older roles include independent
reviews of the accepted structural, CP/GK, even-inner, Hermitian,
component-saturation, sector3, three-bit, neighbor-Frobenius, CG and
cubic-cofactor packets. In particular I was an old whole CG reviewer.
Those separately accepted results are imported in their exact scopes,
not freshly self-recertified by citing my own older conclusions. I did
not construct R4. No corresponding NEW R5 review1 finding, report,
ledger, source, code, hash or metadata was opened. Its conclusions
are not a premise. Completion is sent as IDENTITY ONLY until both
entire whole initials have been confirmed frozen.

## 1. Official domain and the actual factor to which the proof applies

The complete local statement and fresh official PaperB page2 definition/
(b) were checked. The question concerns coefficientwise congruence of
integer polynomials, equivalently two positive-degree F2 factors of the
whole nonzero homogeneous quotient. It is not a question about values
on F2 points or the existence of an APN component. No preliminary(a)
proof is investigated or reproduced.

Here s is an ORDINARY prime>=5, Q=2^s, ell=Q-1, q=Q^k with INTEGER
k>=2, and n=ell*q+1. Thus n is a positive odd integer, with binary
weight s+1. The ordinary integers

    N=ell*q-2, A=(ell-2)(ell+1)=ell^2-ell-2,
    p=ell-1=Q-2, a=(ell+2)/p

are positive; p is NOT an assumed prime or the characteristic. Over
the algebraic closure of F2, phi=f/R is nonzero and homogeneous of
degree N. The coefficient X^(n-1)Y of f is1, so no zero-polynomial
case is hidden. The n1/n3 and small binary-weight boundaries are
outside the family. A nonzero homogeneous polynomial's factors are
homogeneous by comparing least/greatest degrees, so an arbitrary
nonhomogeneous presentation in the official question does not escape
the factor analysis.

I read COMPLETE current accepted CG and R4 bodies and their current
acceptance MD/JSON/integrity records. R5 uses CG1/CG2 and R4A--R4C,
not CG3, the pending/new cubic theorem or an unread Frobenius theorem.
The accepted copies' full mathematical suffixes were checked exactly
against their original frozen candidates. Their older submission
labels do not negate the scoped acceptance headers/authorities.

The R4 hypotheses hold uniformly:

    q>=Q^2>2Q+5=2ell+7,
    N-(3A-2)>=(Q-1)Q^2-3Q(Q-3)
              =Q(Q^2-4Q+9)>0.

I reconstructed the applicable R4 chain from its complete body. CG2's
factor-degree constraint excludes e in [(ell-2)q/2,N/2], making
B=q+1-2ell*e/A strictly positive. In the UNSIMPLIFIED second inequality,
D>0 then forces T=p(e-e^2/A)>0, hence e<A for EVERY smaller proper
factor, including reduced unions. Grouping components up to degree A
under N>=3A-2 gives a unique absolute component G of degree>N/2.
Its complementary H has degree e<A and e<N/2. Normalizing a coefficient
forces G, then H, to be F2-defined. The four-coordinate S4 action is
defined over F2, fixes f and the three pair-partition factors of R
exactly, and fixes G,H exactly after the same scalar check.

If phi is reducible, this H is ACTUAL and nonconstant, with e>0.
If H=1 instead, phi is already absolutely irreducible and no positive
D is assigned to H. This distinction is respected throughout R5.
No hypothetical formal distribution is substituted for the actual H.

## 2. Geometry, old divisibilities and multiplicity under Frobenius

CG1's COMPLETE projective list consists of the central point P,
noncentral diagonal points and off-diagonal points, all F_Q-rational
with all FOUR coordinates X,Y,Z,W nonzero. Thus Z can be normalized
to1 at every point in question. No omitted points at infinity or
zero-coordinate stabilizers are introduced. Its ordinary cones let
H select subsets of distinct tangent directions. CG1's exact line
contact identity gives S=3(e-m), without requiring m>0.

I checked the operative R4 local arguments, rather than reading its
divisibilities as unexplained labels. At P, the transposition of X,Y
pairs all allowed tangents, since its sole fixed projective direction
is a prescribed diagonal and absent from the cone. Hence m is even.
At P_b=(b:1:1), b in F_Q* minus1, the equal-pair stabilizer has order4
and the S4 orbit has six points. Its two first-order actions on the
finite tangent parameter u=x/y are u->u+1 and u->u+b. For b!=0,1
these give a free additive four-group; the excluded direction y0
cannot contribute. Thus each local multiplicity r_b is a multiple
of4, and each six-point orbit contributes a multiple of24 to S.
At an off-diagonal point the four coordinate values are distinct
and nonzero. A projective scalar permuting them has multiplicative
order dividing4, hence is1 in characteristic2. The stabilizer is
trivial and the orbit has24 points. Therefore the R4 inputs give

    m even, 24|S, t=e-m=S/3 with8|t, 24|V,
    D=(ell-3)e+2m-V>0 and4|D.

The positivity is CG2's same actual ordinary integer: its reduced-
union bound retains c-1 and gives qD>=e>0. No irreducible genus bound
is incorrectly applied directly to the cofactor product. Zero local
multiplicities, m0 and V0 are all permitted.

Let F denote coordinate squaring. All S4 matrices have F2 coefficients,
so F commutes with S4. Since every listed point is F_Q-rational,
F^s fixes it projectively. Thus the induced permutation on either
S4-orbit set has cycles of length1 or the ORDINARY prime s.

Multiplicity preservation is semilinear, not a claim about the
derivative of the inseparable squaring morphism. In normalized affine
coordinates write H(P+(u,v))=sum a_ij u^i v^j. Because H has F2
coefficients, the local equation at F(P) has coefficients a_ij^2.
An automorphism of the coefficient field preserves which coefficients
are zero and the least total degree. Projective normalization changes
the local equation only by a unit and an invertible chart change.
Hence multiplicities are constant on each combined F/S4 orbit.
Substituting u^2,v^2 would double orders and is NOT the argument.
No equality between unrelated combined orbits is used.

## 3. R5A: all diagonal cycles and the printed residue typo

The repeated four-coordinate values of P_b are (b,1,1,b). Matching
two such multisets up to a common projective scalar shows that
P_b,P_c are S4-equivalent exactly when c=b or b^-1. The first is
the identity case; interchanging the two equal pairs and rescaling
gives the second. There is no third case because there are only the
two distinct repeated values, and b0/b1 were excluded.

Since F(P_b)=P_(b^2), a fixed S4 orbit would require b^2=b or b^-1.
The first gives b1. The second gives b^3=1. For odd s,

    2^s == 2 modulo3, so 2^s-1 == 1 modulo3.

Thus3 does not divide Q-1 and F_Q* has no nontrivial cube root; again
b1, excluded. This closes the fixed-orbit exclusion for every allowed
s. Section2 of the submission prints residue2 for Q-1 instead of1.
The explicit allowed example s5 gives31==1, not2. This is recorded
as a nonblocking editorial error, not suppressed and not a new theorem
counterexample. The required nondivisibility and ALL subsequent claims
hold with the corrected one-line arithmetic.

Every diagonal S4 orbit therefore lies in a length-s F cycle. Along
one such cycle the local multiplicity is a common r_b divisible4;
the cycle contains6s points, so contributes6s*r_b, a multiple of24s.
Summing disjoint cycles, including those with multiplicity0, gives
24s|S. The EXACT identity S=3t gives8s|t as ordinary integers.
This proves the whole R5A assertion, not just a count of point orbits.

## 4. R5B: projective fixedness and all off-diagonal cycles

Suppose an off-diagonal S4 orbit were F-fixed. For some permutation
sigma, F(P)=sigma(P) projectively. Commutation permits induction
F^j(P)=sigma^j(P). At j=s, F^s(P)=P, so sigma^s fixes P. The
projective stabilizer was shown TRIVIAL, hence sigma^s is the identity
permutation. The order of sigma divides24, and gcd(s,24)=1 for prime
s>=5; therefore sigma is the identity and F(P)=P projectively.

Only now normalize the nonzero Z coordinate to1. The equality
(x^2:y^2:1)=(x:y:1) forces x,y in F2. Nonzero x,y and nonzero W
then force all four coordinates to1. This is the central point, not
an off-diagonal point. Thus there are no F-fixed off-diagonal orbits.
Using a projective scalar before normalization would not justify
coordinatewise fixedness; the candidate correctly avoids that step.

Every remaining cycle has exactly s orbits, each of24 points, with
one common local H multiplicity. Each contribution to V is therefore
a multiple of24s, giving24s|V, including V0. This proves R5B.

## 5. R5C: the same positive integer and both signs in the maximum

Fermat's elementary product argument for the ordinary prime s gives
2^s==2 modulo s, so s divides p=Q-2. Since e=m+t, the actual D is

    D=p*m+(p-2)*t-V.

R5A/B make t,V divisible by s. Hence s|D. R4's separate4|D and
gcd(4,s)=1 make4s|D. CG2 gives D>0; consequently D>=d=4s. This
does not combine two bounds attached to different factors, and no
division by s takes place in the characteristic2 coefficient field.

For the same H, R4 has B>0,T>0 and the unsimplified CG2 inequality

    D*B <= T-a*D^2/A, B=q+1-2ell*e/A,
    T=p(e-e^2/A), a=(ell+2)/p>0.

Divide by D>0. Since T>0 and D>=d, both comparisons have the required
direction:

    B <= T/D-a*D/A <= T/d-a*d/A.

Therefore

    q+1 <= (p/d+2ell/A)e-p*e^2/(d*A)-a*d/A.

The coefficient of e^2 is strictly negative. Its global REAL maximum
is

    d*A/(4p)*(p/d+2ell/A)^2-a*d/A
      =p*A/(4d)+ell+d*(ell^2-ell-2)/(p*A)
      =p*A/(4d)+ell+d/p.

Maximizing over a larger real domain is an upper bound; no actual
integer degree need attain the vertex. Taking d4s and subtracting1
gives the proposed NECESSARY reducibility bound

    q <= p*A/(16s)+ell-1+4s/p.

Only the STRICT reverse excludes a cofactor, hence proves absolute
irreducibility of the whole phi. Equality and failure of this sufficient
test remain undecided. In particular replacing T by a negative quantity
or dropping the negative D term would not establish this same bound;
the candidate makes neither error.

## 6. R5D, scope boundaries and attempts to break the argument

For s5, Q32, ell31,p30,A928 and d20. The exact threshold is

    30*928/80+30+20/30=348+30+2/3=378+2/3.

It is strictly below1024<=q for EVERY k>=2. The two size hypotheses
were already verified for all such k. Thus the stated entire family
n=31*32^k+1 has absolutely irreducible whole phi. Cancelling the
nonzero prescribed factor R in the polynomial domain translates this
to exclusion of the official two positive-degree F2 factors. No
extension-field factor is incorrectly promoted or descended here;
absolute irreducibility is already the stronger exclusion.

The following adversarial boundaries were checked explicitly:

* s3 permits order3 permutations, so its omission is essential; no
  off-diagonal coprimality argument is extended there.
* Composite s can have proper nontrivial cycles; the proof does not
  assume only1/s cycles outside the prime-s domain.
* k1 is not covered by the uniform size hypotheses. No statement
  about it, n57 or all small-k exponents follows.
* Other prime s,k2 are not blanket excluded. At s7 the leading term
  alone is18000>128^2, so failure of the sufficient inequality cannot
  imply reducibility or an arithmetic contradiction.
* H=1, e0, m0 and local multiplicity0 are correctly distinguished.
  Repeated/nonhomogeneous factors do not produce exceptions because
  accepted CG gives a reduced nonzero homogeneous phi.
* Invariant multiplicities are required only along ACTUAL combined
  orbits. No arbitrary extension-field cofactor or global uniformity
  premise is silently inserted.
* The published APN/component literature is not used to decide the
  whole quotient. The Férard2017 operative criterion remains unread,
  so priority/overlap and the full annual classification stay open.

The full source-check record specifies what was freshly read and what
is an accepted import. A false residue value is the only printed
arithmetic error found. It has the explicit harmless correction above;
no counterexample to R5A--R5D was found by the whole hand reconstruction.
No mathematical executable, CAS, field scan, optimizer, routine test,
source/author program or old certificate/freezer rerun was used.

## 7. Preservation and handoff

Only NEW `reviews/cofactor-Frobenius-r5-review-2-*` files are written.
The prefix was confirmed unused. My immediate immutable parent is the
ENTIRE2020 ToddR12 freeze plus ten payloads; its677 old own paths are
bound transitively, without historical inventory recopy. Accepted
CG/R4 historical summaries are bound by current immutable authority,
not recursively replayed. All current required fingerprints, complete
new metadata readback and a separate postverify precede the completion
identity. Administrative checks protect bytes and labels, not mathematics.

The separate source JSON records a fresh direct same-batch account-wide
25%TOTAL reading at10:24:30UTC, reset1792874445, with ordinary usage
allowed and matching legacy/by-limit records. Only that human-authorized
window may be used through90%TOTAL, retaining integration reserve.
Effective model settings are not inferred from requested launch settings.

The coordinator must read BOTH complete whole audits/ALL ledgers/issues/
sources/logs/code/ALL metadata before any scoped promotion. My nonblocking
editorial note must remain visible. Initial files stay immutable; any
substantive author change would need the versioned repair and both
affected reaudits required by the protocol. No annual or novelty claim,
external validation, absolute certainty or automatic budget extension
is made by this audit.
