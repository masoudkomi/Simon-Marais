# FS1–FS5: OTHER initially blind ENTIRE WHOLE review R2

2026-10-18 UTC. Reviewer `/root/review_2017_coarsening_r1` (C).
Requested inherited gpt-6.1-sol/max; independently verified effective
readback unavailable. Review of a **candidate proof - unverified**.
Only the coordinator may promote a scoped result after BOTH OTHER whole
initials and reconciliation. This report, ALL48 ledger rows, issues,
sources, log, administrative code and ALL metadata freeze before any NEW
corresponding A report, finding, source, ledger, hash or metadata is opened.
The initial completion message discloses identity only until the other
entire initial is confirmed frozen.

## 1. Exact submission, independence and conclusion of this audit

I reviewed the ENTIRE nine-file constructor packet, including its code
and all JSON, for `notes/cofactor-symmetry-r1-candidate-v1.md`, 14531 bytes,
SHA256 `77eb040ac77e255d3b8e8b38e47d6329857fc8af0d31eeb49cd0880b2763fbc1`.
Its freeze is 2406 bytes, SHA256
`2fdb3fc025f2bf89e6d3bdf060373103fecf428db8ff4f407f170bed86bab327`.
The ledger below covers all 48 author obligations, in order. No constructor
program, mathematical program, CAS, field enumeration, factor scan,
certificate or old numerical test was run.

**Whole-review finding:** I found no substantive defect or required
mathematical repair in FS1–FS5 within their stated domains. The two orbit
arguments, reduced-component correction, positive integer obstruction and
real optimization admit the full reconstruction below. One harmless
operational timestamp inconsistency is recorded separately, with no proof
or source consequence. No conclusion about a complete annual answer or
priority follows from this review.

Root is the sole NEW constructor and cannot count as an independent
reviewer. I supplied no new problem-specific inference. Before the new
submission was frozen, I prepared only named old-input/source readings,
as requested. I was an earlier independent reviewer of the accepted FP
and structural packets, and authored older CP1/sector-three work. None of
those older roles constructs this new symmetry/genus argument; equally,
this is not advertised as a fresh independent recertification of my own
old work. No CP1 or sector-three conclusion is a premise here.

## 2. Official domain and exact accepted inputs

The [official 2024 Paper B, B4(b)](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf)
asks for coefficientwise factorization over F2 with two factors of
positive degree. We work in polynomial rings, not polynomial functions
on a finite set. With K the algebraic closure of F2, define

    q=8^k, k>=2; n=7q+1; N=7q-2;
    W=X+Y+Z;
    R=(X+Y)(Y+Z)(Z+X);
    f=X^n+Y^n+Z^n+W^n; phi=f/R.

The exponent is odd, with four binary ones. In particular q>=64. The
q=8/n=57 endpoint and the a=0,1 endpoints of the later corollary are
outside the claim. No preliminary construction is reproduced.

I read the complete accepted FP body and both acceptance records. Its
exact imported conclusions are: phi is squarefree; its entire projective
singular set is 43 ordinary points; P=(1:1:1) has multiplicity q-2;
18 other prescribed-diagonal points have multiplicity q; 24 off-diagonal
points have multiplicity q+1. Its three exact diagonal restrictions give,
for every factor U of degree e and P-multiplicity m, the identity

    sum_(six other singularities on each diagonal) m_A(U)=e-m.

There is one absolute irreducible component G of degree at least 5q-10,
unique in that range and normalized over F2. Its complementary cofactor
H is also F2-defined, reduced, and has degree e<=2q+8. FP explicitly
allowed H to be nonconstant; its own scope cannot be used to assume
the new conclusion. Its extra six-line inequality FP0 is not needed
for FS's integer obstruction.

Accepted T1 excludes ALL absolute line factors when n is odd with binary
weight at least three. I read its complete proof, including arbitrary
algebraic-closure line coefficients, the zero-denominator cases and
removal of the three simple R factors. It applies to this four-bit n,
so it controls absolute component degrees, not merely F2 degrees.

I also read the complete accepted NF body and both authority records.
NF3 supplies whole absolute irreducibility for n=7*2^a+1, a>=2,
3 not dividing a, using one of its two exact Frobenius-neighbor
hypotheses. It explicitly supplies nothing for 3 dividing a. These
accepted bodies/authorities are fingerprinted in the compact baseline;
their actual scopes, rather than older review conclusions, are the inputs.

## 3. FS1: the actual factors have exact four-form symmetry

Identify the three-dimensional affine vector space with the subspace
x1+x2+x3+x4=0 in K^4. The four coordinate restrictions are X,Y,Z,W.
Every coordinate permutation preserves that subspace and has its inverse
there; it induces an invertible F2-linear substitution of X,Y,Z.
The restrictions are distinct linear forms, so a permutation acting
trivially would fix each coordinate restriction and is the identity.
The action is faithful even in characteristic two. The vector represented
by P is (1,1,1,1), and is fixed.

The numerator is invariant. There are precisely three unordered
two-pair partitions of four positions. On the sum-zero subspace the two
pair sums in each partition agree, and their three values are exactly
X+Y, X+Z, Y+Z. Consequently the permutation group permutes the three
factors of R, with no sign or scalar. Thus phi is fixed exactly.

For any substitution sigma, sigma(G) is an absolute irreducible factor
of phi with the same degree as G. Uniqueness in the accepted large range
forces sigma(G)=cG with c nonzero. This conclusion is about the actual
large component, not about all components forming one orbit. Since G
and sigma(G) have F2 coefficients, compare a position where G has
coefficient 1: sigma(G) has coefficient c there, and this is a nonzero
element of F2. Therefore c=1. Cancelling G in the domain K[X,Y,Z]
from sigma(phi)=phi fixes H exactly too.

## 4. FS2: reconstructing both multiplicity orbits

Represent points by four coordinates with sum zero, modulo common
nonzero scalar. By the complete FP list, the nontrivial prescribed-
diagonal points are permutations of (b,b,1,1), with b in F8* minus {1}.

For a fixed b, placing the two b entries in a two-element subset of
the four positions gives six tuples. A scalar relating two such tuples
either preserves the two values, hence is 1 and preserves the positions,
or exchanges the values. The latter would require scalar b and b^2=1.
In the odd-order group F8*, b^2=1 forces b=1, excluded. The six points
are distinct and form an S4 orbit. Replacing b by b^-1 produces the
same orbit after rescaling and exchanging the two pairs; conversely a
projective permutation equivalence can only preserve or exchange the
two values. Thus inverse pairs label exactly three disjoint six-point
S4 orbits, totalling 18 points.

Choose a generator of the cyclic group F8*. Squaring acts on the
three nonzero exponent pairs modulo sign as

    {1,6} -> {2,5} -> {4,3} -> {1,6}.

This is a hand group calculation, not a finite-field scan. An F2-defined
polynomial has the same local multiplicity at a point and its coordinatewise
square: Frobenius is a field automorphism and transports every translated
coefficient and every vanishing order. Combining this with exact S4
invariance of H makes all 18 multiplicities the same integer u>=0.
S4 alone would not justify that conclusion; the candidate correctly
includes coefficient Frobenius.

For an off-diagonal point all four coordinates are distinct, nonzero,
and lie in F8. Their unordered set S has four elements and sum zero.
Choose a in S. Translation by a gives {0,s,t,s+t}, since the other
three translated entries sum zero. Distinct nonzero s,t are independent
over F2, so this is a two-dimensional linear subspace translated back.
Because S has no zero, it is the nonzero coset of that subspace.

A three-dimensional F2 vector space has seven nonzero linear functionals;
each is surjective, and two have the same two-dimensional kernel only
if they differ by a nonzero scalar, which over F2 is 1. Hence there
are exactly seven such subspaces and seven cosets not containing zero.
Multiplication by F8* acts on these seven cosets. A nonidentity scalar
has order seven; its orbits on nonzero elements all have size seven.
It cannot preserve a four-element set. The action on the seven cosets
is therefore free and transitive. Given any two ordered off-diagonal
tuples, first scale their unordered sets to coincide, then permute
the four entries to identify them. Scaling does not change a projective
point. Thus all 24 off-diagonal projective points form ONE S4 orbit.
As an independent count, seven sets times 4! orderings, divided by
seven free scalar normalizations, equals 24. All their H multiplicities
are one integer v>=0. No transitivity of individual absolute factors
is used in either multiplicity argument.

## 5. Exact local/global intersection identity and integer algebra

Let m=m_P(H). Each of the three prescribed lines has six of the
18 nontrivial diagonal points. The accepted exact contact identity
therefore gives e=m+6u. This remains true when m=0 or u=0.

G and H are coprime because phi is squarefree. Every common projective
zero is singular on phi and hence is one of the 43 listed points.
At any such point the initial cones of G and H partition a product
of distinct tangent lines, so the cones are coprime. The local
intersection is exactly the product of the two multiplicities, including
zero if one factor is a unit. Projective Bezout, not affine Bezout,
therefore gives the equality

    e(7q-2-e)=m(q-2-m)+18u(q-u)+24v(q+1-v).       (A)

I expanded both sides after substituting m=e-6u. The right side minus
left side is

    -6qe+12qu+24qv+12u+12eu-54u^2+24v-24v^2.

Dividing this zero integer by 6 and collecting gives

    D=e-2u-4v;
    qD=2u(e+1)-9u^2+4v-4v^2.                    (B)

All variables here are ordinary integer degrees or multiplicities;
no division by 6 in the coefficient field occurs. At this point D
is an integer of unspecified sign. The proof must not assume its
positivity merely from the displayed definition.

## 6. FS3: the multiplicity bound and its REDUCED correction

The exact general source is [Fulton, Algebraic Curves, §5.4 Theorem 2](https://math.stanford.edu/~conrad/145Page/handouts/algcurves.pdf),
printed page 60, together with §5.2 and §5.3. I read the complete
operative proof and Problem 5.25, not only the statement. Its input
is an irreducible projective plane curve over the algebraically closed
standing field. It bounds the sum of binomial multiplicities by its
arithmetic genus. The nearby Hessian and generic-projection assertions
have separate characteristic restrictions and are not used. Appendix A
was read completely. The following reconstruction makes the relevant
characteristic-two step explicit.

For an irreducible homogeneous C of degree d>=2, at least one partial
derivative is nonzero. Otherwise every monomial exponent is even in
each variable, and perfection of K makes C a square, a contradiction.
The nonzero derivative has smaller degree, hence is coprime to C.
Its local multiplicity is at least m_A(C)-1. Bezout yields the initial
bound S:=sum_A binom(m_A(C),2)<=d(d-1)/2; the singular set is finite.

The space of forms of degree d-1 has dimension M=d(d+1)/2.
An imposed local multiplicity m-1 costs at most m(m-1)/2 linear
conditions, by translated monomial coefficients. Set r=M-1-S>=0,
and choose r distinct smooth points away from the singular set.
Impose those additional r simple conditions. At most S+r=M-1
conditions leave a nonzero form B of degree d-1. C cannot divide B.
Their intersection has degree d(d-1), and the chosen local conditions
give

    d(d-1)>=2S+r=S+M-1.

Hence S<=(d-1)(d-2)/2. This uses no characteristic-zero Hessian,
division by a field element 2, genus-one normal form, or unproved
generic projection in positive characteristic. The fractions count
integer dimensions. The argument also handles nonordinary singularities.

Now factor the actual H over K into DISTINCT absolute irreducibles
H_1,...,H_c with degrees d_j. Reducedness is essential and follows
from accepted FP squarefreeness. T1 applies over K, so every d_j>=2,
and c<=e/2. Individual H_j need not descend to F2.

At a point A let m_j=m_A(H_j), allowing m_j=0. Multiplicities add,
and the integer binomial identity gives

    binom(sum_j m_j,2)=sum_j binom(m_j,2)+sum_(i<j)m_i*m_j.

Apply the irreducible bound separately to each H_j. For each distinct
pair H_i,H_j, the sum of m_i*m_j is bounded by their total intersection
d_i*d_j. The latter is projective Bezout; transversality is not needed
for this inequality. Consequently

    sum_A binom(m_A(H),2)
      <= sum_j (d_j-1)(d_j-2)/2 + sum_(i<j)d_i*d_j
       = (e^2-3e+2c)/2
       = (e-1)(e-2)/2+c-1
      <= e(e-2)/2.                                  (C)

This is exactly the reduced-component correction missing from an
incorrect direct application of the irreducible genus formula to H.
It works for reducible H, including conic components and odd e.
For odd e the relaxed inequality c<=e/2 is merely weaker than its
integer floor and is safe. A degree-one H is already excluded by T1.

Every singularity of H is singular on phi; retaining just the 43
nonnegative summands in (C) is in any case sufficient. Thus

    m(m-1)+18u(u-1)+24v(v-1)<=e^2-2e.

With m=e-6u the left side minus the right side is

    -12eu+54u^2+e-12u+24v^2-24v = e-6qD,

the last equality following from (B). Therefore qD>=e/6. Under
the contradiction hypothesis H nonconstant, e>0 and q>0, so D>0.
It is an integer, hence D>=1. This supplies the previously unavailable
sign and discrete lower bound without any irreducibility assumption
on H or assumption that H passes P.

## 7. FS4: reconstructing the global real optimization

Eliminate v from (B) by 4v=e-2u-D. Hand expansion gives

    qD=-10u^2+(3e-D)u+e-D-(e-D)^2/4.

For all real u, the first two terms are at most (3e-D)^2/40.
This is a global upper bound even if the maximizing u is negative,
nonintegral, or incompatible with the actual multiplicity constraints.
Subtracting the remaining square gives

    qD<=(-e^2+14eD-9D^2)/40+e-D,
    D(q+1-7e/20)<=e-e^2/40-9D^2/40
                          <=10-(e-20)^2/40<=10.    (D)

No upper bound was substituted into a decreasing quadratic branch.
Accepted e<=2q+8 gives

    q+1-7e/20 >= 3q/10-9/5 >= 87/5 > 10

at the smallest permitted q=64, with an increasing lower bound for
larger q. The bracket is positive, and D>=1 was proved before it
is used. Thus the left side of (D) is at least 87/5, a contradiction.
The argument includes u=0, v=0, m=0, unequal component degrees,
Frobenius-nontrivial individual components and any possible H with
1<=e<=2q+8. Dropping the constraints u<=q, v<=q+1 only enlarges
the optimization domain, which cannot invalidate the contradiction.

It follows that H is constant. Since G is an absolute irreducible
component, phi is absolutely irreducible as a WHOLE, rather than
merely having one absolute F2-defined component.

## 8. FS5, boundary cases and limits

For a>=2 with 3 not dividing a, NF3 supplies the conclusion. For
3 dividing a and a!=3, a=3k with k>=2, so q=2^a=8^k and FS4
applies. Together these prove precisely the proposed family
n=7*2^a+1, a>=2, a!=3, conditional only on acceptance of this new
submission. At a=3 the FP small-cofactor degree-gap hypothesis used
here does not apply; the final bracket is also not sufficiently
large at q=8. There is no inference closing that endpoint. The
excluded a=0,1 and n=1,3 boundaries are never brought into an
optimization requiring a positive-degree curve.

Absolute irreducibility implies ordinary F2 irreducibility, so this
restricted infinite family cannot furnish the official two positive-
degree factors. A converse is neither needed nor claimed. No statement
that all odd exponents, all four-bit exponents, or all remaining annual
cases are classified has been justified. The general geometric method
is classical and attributed; neither this review nor its source check
certifies priority for the family.

## 9. Integrity, closed challenges and review boundary

The separate ledger has all48 author IDs exactly once. The issue file
records the attacks on Frobenius/scalars, orbit splitting, reduced
components, characteristic two, factor units and maximum signs; each
is closed by the proof above. There is no mathematical repair request.
I noted a single 17:27 versus 07:27 timestamp inconsistency in the
constructor's historical operational paragraph. All exact freeze and
meter records identify the intended 07:27 recovery; no mathematical
or source inference uses that incidental text.

The administrative freezer checks the nine exact constructor artifacts,
the 18 named old-input fingerprints, our compact immutable prior
manifest and necessary metadata, accepted-copy identities and all48
labels. It does not execute the constructor code or test mathematics.
No NEW corresponding peer prefix is opened or hashed. Earlier complete
records are bound by compact parent identity without recopying their
growing inventory. Source reads and limits are in the separate source
file. No Git/shared/old/cache bytes were written. Findings are withheld
from parent/peer comparison until the required entire initial boundaries
close; report storage and administrative hashes do not promote a theorem.
