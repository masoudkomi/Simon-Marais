# Coefficient Frobenius on actual cofactor singularity orbits

18 October 2026 UTC. **Candidate proof - unverified.** Root is sole
NEW constructor and is EXCLUDED from the independent reviewer count.
TWO OTHER initially blind ENTIRE WHOLE audits and full coordinator
reconciliation are required. No mathematical executable was used.

## 0. Significance, exact setting and proposed claims

Only the open part2024 B4(b) is investigated. The associated quotient
is the plane curve occurring in the APN power-function literature.
An absolutely irreducible component suffices for several asymptotic
APN applications, but does not answer the official question about
factorization of the WHOLE polynomial. The separately accepted R4
argument constructs an actual small F2-defined invariant cofactor if
reducibility occurs. Its singularities permit two commuting finite
actions: the four-coordinate permutations and coefficient Frobenius.
This proposed extension uses their interaction to strengthen an
ordinary-integer intersection obstruction. It would decide another
infinite exponent family, without claiming the annual classification,
an APN classification, or novelty.

Let **s be an ordinary prime with s>=5**, let k>=2 be an integer, and put

    Q=2^s, ell=Q-1, q=Q^k, n=ell*q+1,
    N=ell*q-2, A=(ell-2)(ell+1), p=ell-1, a=(ell+2)/p.

The symbol p is an ORDINARY positive integer Q-2, not an assumed prime;
the field characteristic is2. The primality assumption applies to s.
Over K=F2bar write W=X+Y+Z, R=(X+Y)(Y+Z)(Z+X),
f=X^n+Y^n+Z^n+W^n, phi=f/R. Degrees and multiplicities below are
ordinary integers. Frobenius F on points means coordinate squaring,
not the q-power tangent identity or a change of the definition field.

The exact accepted mathematical inputs are CG1/CG2 and R4A--R4C,
with the current accepted bodies/MD/JSON authority bound in the
companion. They were read in full. The first two R4 size conditions
hold for EVERY k>=2; they are checked again below. Under reducibility
R4 gives the ACTUAL nonconstant cofactor H over F2, exactly S4-invariant,
of degree0<e<A and e<N/2. Put

    m=m_P(H), S=sum(non-P diagonal multiplicities), t=e-m=S/3,
    V=sum(off-diagonal multiplicities),
    D=(ell-3)e+2m-V=p*m+(p-2)*t-V.

R4 supplies m even,24|S,8|t,24|V, and the SAME positive integer4|D.
CG1 supplies the complete projective singularity set in F_Q, all four
coordinates nonzero, with off-diagonal coordinates pairwise distinct.
CG2 supplies the unsimplified inequality for this actual smaller H.

**R5A.** On the set of S4-orbits of non-P diagonal singularities,
coefficient Frobenius has NO fixed orbit, and EVERY orbit has length s.
Consequently24*s divides S, and8*s divides t.

**R5B.** On the set of S4-orbits of off-diagonal singularities,
coefficient Frobenius likewise has NO fixed orbit and every orbit has
length s. Consequently24*s divides V. Multiplicities may differ
between different combined orbits.

**R5C.** The SAME actual positive integer D is divisible by4*s;
in particular D>=4*s. Thus reducibility implies

    q <= p*A/(16*s)+ell-1+4*s/p.                 (R5-bound)

Only the STRICT reverse excludes reducibility. Under the stated prime-s,
k>=2 hypotheses it proves absolute irreducibility whenever that strict
test holds. No equality conclusion or converse is asserted.

**R5D.** At s=5,Q32 the threshold is378+2/3<1024. Hence the WHOLE
phi is absolutely irreducible for EVERY

    n=31*32^k+1, k>=2.

The general sufficient test need not decide k2 for other prime s.
Composite s, s3, k1 and other exponent families receive no new blanket
claim. The full annual answer and priority remain unresolved.

## 1. Actual domain, commuting actions and invariant multiplicities

For every Q>=8,k>=2, q>=Q^2>2Q+5=2ell+7. Also

    N-(3A-2)>=(Q-1)Q^2-3Q(Q-3)
              =Q*(Q^2-4Q+9)>0.

The accepted R4 unique-component and exact F2/S4 descent therefore
apply in the full present domain. If phi is absolutely irreducible
there is nothing to exclude; assume reducibility and use its ACTUAL
nonconstant H. We do not assign a positive D to H=1.

Every listed projective point is F_Q-rational by CG1, so F^s fixes it
projectively. The S4 substitutions have F2 coefficients, and hence F
commutes with them. Thus F induces a permutation of each S4 orbit set,
whose order divides the prime s. Its cycles have length1 or s. These
are orbits of POINTS modulo S4, not Frobenius orbits of polynomial factors.

The polynomial H has F2 coefficients. Coordinate squaring is a field
automorphism of K; applying it to a translated local equation preserves
the least nonzero total degree and hence preserves local multiplicity.
Projective rescaling and changing the nonzero affine normalization
multiply the homogeneous equation by a unit and also preserve that
degree. Consequently H has constant multiplicity on a combined F/S4
orbit. No assertion about equality on different combined orbits is made.

## 2. Noncentral diagonal orbit calculation in full

By the exact accepted geometry any such point is S4-equivalent to
P_b=(b:1:1), b in F_Q* minus1, with four values(b,1,1,b).
Its S4 orbit contains six points and each local H multiplicity r_b
is divisible by4, by the two distinct tangent translations in R4.
The local4 condition is retained; an orbit count alone cannot replace it.

Two standard points P_b,P_c are in the SAME S4 orbit if and only if
c=b or c=b^-1. To verify the necessary direction, the two repeated
coordinate values must be matched, up to a common projective scalar.
Preserving their order gives c=b; interchanging the two values and
normalizing the repeated1 gives c=b^-1. These cases are sufficient:
the first is the identity, and interchanging the two equal pairs,
followed by rescaling, gives the second. Values b0/1 were excluded,
so there is no coincident-value exception.

Now F(P_b)=P_(b^2). If its S4 orbit were fixed, b^2 would be b or
b^-1. The first forces b1 (since b!=0). The second gives b^3=1.
Since s is odd,2^s-1 is2 modulo3. The order3 cannot divide Q-1;
the finite cyclic group F_Q* therefore has no nontrivial cube root
of unity. This too forces b1, excluded. No diagonal S4 orbit is fixed.
Since F's order on the orbit set divides the prime s, EVERY such
cycle has length exactly s.

In one cycle, all s six-point S4 orbits have the SAME r_b because
H is F2-defined. Its total contribution to S is6*s*r_b, divisible
by24*s. Sum over the disjoint cycles, allowing zero multiplicities,
to obtain24*s|S. As S=3t EXACTLY, this gives8*s|t. This proves R5A.
No division in characteristic2 or equality across unrelated b-orbits
is used.

## 3. Off-diagonal orbit calculation and the projective scalar issue

R4 proves each off-diagonal S4 stabilizer is trivial. Recall why this
holds projectively: a scalar preserving the four-element NONZERO set
of distinct coordinate values has order d, every multiplicative orbit
has length d, and d divides4. In characteristic2 this forces that
scalar1, and distinctness then forces the permutation to be the
identity. Thus every such S4 orbit has24 points.

Suppose F fixed one of these S4 orbits. Choose a point P on it and
sigma in S4 such that F(P)=sigma(P) as PROJECTIVE points. Commutation
gives F^s(P)=sigma^s(P). But P is F_Q-rational and F^s(P)=P. The
trivial stabilizer implies sigma^s is the identity PERMUTATION. The
order of sigma divides24, while the prime s>=5 is coprime to24.
Thus sigma itself is the identity, so F(P)=P projectively.

There is no off-diagonal point with this last property. Normalize
one of its nonzero coordinates Z to1. Projective squaring-fixedness
then reads (x^2:y^2:1)=(x:y:1), forcing x,y in F2. All four
coordinates are nonzero, so x=y=Z=W=1, which is the central point,
and in particular they are not pairwise distinct. This contradicts
the off-diagonal hypothesis. The proof did not replace projective
fixedness by coordinate fixedness before choosing the normalization.

There are therefore no fixed off-diagonal S4 orbits. Their F cycles
have length s. Each cycle comprises24*s distinct points with the
same H multiplicity, yielding a contribution divisible by24*s to V.
Summing gives24*s|V, including V=0. This proves R5B.

## 4. The SAME integer D and a sign-correct general threshold

Because s is an odd prime, Fermat's congruence gives2^s=2 modulo s.
For completeness, multiplication by2 permutes the nonzero residue
classes modulo s; comparing their products gives2^(s-1)=1 modulo s,
and multiplying by2 proves the assertion. Therefore s divides
p=Q-2. From the EXACT expression

    D=p*m+(p-2)*t-V

and R5A/R5B, s divides D. Accepted R4 independently gives4|D for
this SAME actual H. Since gcd(4,s)=1,4*s divides D. Accepted CG2
gives D>0, hence D>=d where d=4*s. This is an ordinary-integer
argument, with no inverse of s or4 taken in the characteristic2 field.

Set B=q+1-2ell*e/A and T=p(e-e^2/A) as in R4. That proof gives
B>0,T>0. CG2's unsimplified inequality is

    D*B <= T-a*D^2/A.

For ANY positive lower bound d<=D, divide by D>0 and use both signs:

    B <= T/D-a*D/A <= T/d-a*d/A.

It follows that

    q+1 <= (p/d+2ell/A)e -p*e^2/(d*A)-a*d/A
         <= p*A/(4*d)+ell+d/p.                  (1)

The second line maximizes a concave quadratic over ALL real e.
Its value follows by expanding

    d*A/(4*p)*(p/d+2ell/A)^2-a*d/A
      =p*A/(4*d)+ell+d*(ell^2-ell-2)/(p*A)
      =p*A/(4*d)+ell+d/p.

Here A=ell^2-ell-2. Maximizing over a larger real domain is a valid
upper bound for each actual integer e; no attainable vertex is
asserted. With d=4*s and subtracting1, (1) is the R5-bound. Its
strict reverse contradicts any actual nonconstant H, proving whole
absolute irreducibility. Equality remains undecided. This proves R5C.

## 5. The exact Q32 family and what is left

At s5, Q32,ell31,p30,A29*32=928, and d20. Direct rational arithmetic
gives

    p*A/(16*s)+ell-1+4*s/p
       =27840/80+30+20/30
       =378+2/3 <1024 <= q.

The size conditions in Section1 already hold for every k>=2, so the
strict threshold excludes every actual cofactor in this infinite
family. The quotient has positive degree and is nonzero. Absolute
irreducibility over K excludes two positive-degree F2 factors; such
factors are precisely the nonconstant coefficientwise reductions of
the official integer-polynomial factors. The cancellation f=R*phi
takes place in a polynomial domain. No reverse descent assumption is
required for this final exclusion. This proves the proposed R5D.

For other prime s the R5 test remains merely sufficient. For example,
its leading scale Q^3/(16s) need not be below Q^2. This note supplies
no blanket k2 theorem for all prime s. For composite s, the F cycles
need not have length1 or s; for s3 a permutation can have order3
and the diagonal cube-root obstruction changes. No such case is
silently included. k1 was excluded from the outset. All other annual
cases and possible published overlap remain unresolved.

## 6. Source and independence boundaries

CG1/CG2 and R4 are separately accepted exact inputs, not labels
assigned by this constructor alone. Their full bodies and authority
were read; no new whole re-review of older constructed mathematics
is claimed here. The new orbit calculations, Fermat congruence and
quadratic maximum are entirely written above; no source theorem or
mathematical program supplies a hidden step.

The original official(b) was freshly opened. The publisher's original
Férard2017 abstract and bibliographic page, plus its institution's
publication listing, were freshly inspected for literature overlap.
The operative2017 body remains UNREAD behind the displayed subscription
preview, and the listing is not a full text. No purchase, subscription,
contact, access bypass or conclusion of novelty/source absence follows.
The original2014 publisher abstract addresses a different residue
regime; it is context only. HM's proper-divisor COMPONENT theorem and
the recent Frobenius/Gauss source are not invoked. More precise reading
limits and failed extensions are recorded in the companions.

No OTHER agent supplied a NEW R5 inference. Root's prior authorship
of CG/R4, and later reading of their already frozen peer audits, are
disclosed. Root cannot count as an OTHER reviewer of this NEW packet.
TWO OTHER ENTIRE initially blind whole audits must finish with ALL
reports/ledgers/sources/logs/code/metadata before corresponding new
peer findings/files/hashes/metadata are released. Only complete
coordinator reconciliation may promote the exact partial claims.
