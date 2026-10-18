# Root OTHER initially blind whole R7 review1

2026-10-18 UTC. Initial independent review, not acceptance. C solely
constructed NEW R7 and is excluded. Root supplied no new proof inference.
A is the other whole reviewer. No corresponding NEW A R7 finding, file,
hash or metadata has been accessed. Root's older CG/R4/R5 authorship and
R6 review role are disclosed, not independent recertification of those
old inputs. Entire author13 packet and ALL64 obligations have been read,
including working draft, failures, sources, worklog, code and ALL metadata.

The proposed theorem is whole absolute irreducibility for n=ell*2^i+1,
ell≥3 odd, i≥2, gcd(i,ord_ell(2))=1. This excludes the official ordinary
F2 product for those exponents, not a converse or full classification.
No original JW1993/Férard theorem body or priority claim is imported.

## Whole independent reconstruction

Let q=2^i, m=ord_ell(2), E=F_(2^m). Odd ell ensures that order exists;
ell≥3 makes m≥2. Every ell-th root belongs to E, also for composite ell.
Since gcd(i,m)=1, E∩F_q=F2. Binary weight of ell*q+1 is wt(ell)+1≥3,
so accepted T1 excludes every absolute line. I read the complete current
T1–T4 accepted body and structural MD/JSON, including the point evaluations;
only T1 and those evaluations are operative. R6 reducedness is reproduced
in the new main and reconstructed directly below; unrelated R4/R5 degree
bounds, Frobenius grouping and three-bit classifications supply no step.

The numerator is nonzero since X^(n−1)Y has coefficient one. Its three
homogeneous partials are (X^ell+W^ell)^q and their Y/Z analogues. A common
projective gradient zero cannot have W=0; putting W=1 confines all three
coordinates to ell-th roots. Thus this locus is finite. A repeated factor
would divide all three partials and give an infinite projective curve,
contradiction. The numerator and its quotient phi are reduced.

Any intersection of factors is singular on phi; f=R phi then makes f
and its affine partials zero, even on R. At (a:b:1), with l=a+b+1,
the derivative equations give a^ell=b^ell=l^ell=u. Evaluating f gives
u^q+1=0, hence u=1. Thus a,b,l are nonzero elements of E. At infinity
off R, f_Z=(X+Y)^(n−1) is nonzero, so phi is smooth. At the three R
vertices phi=1: differentiation of f=R phi gives matching unit derivatives
(Y at (1:0:0), X at (1:1:0), and coordinate symmetry). This checks the
whole projective locus, not an affine-only gradient claim.

The elementary local product lemma is sound. If G starts with c L^t,
t≥2, and its next term is not divisible by L, two vanishing factors
would start with positive powers L^r,L^s, r+s=t. Their degree t+1 product
term is divisible by L, contradiction. This applies to arbitrary singular
factors and is unchanged by a local unit; it does not itself assert
global irreducibility.

On a noncentral diagonal (b:1:1), b∈E and b≠1 imply b∉F_q. Thus
c=b+1 and B0=1+b^(1−q) are nonzero. I expanded the exact denominator
as c²y+c y²+x²y+xy² and the first two numerator terms as
B0 y^q and y[b^(−q)x^q+b^(−q)x y^(q−1)+(1+b^(−q))y^q].
Division gives order q−1, pure tangent y^(q−1), and next term with
nonzero x^q coefficient b^(−q)/c². The quadratic denominator correction
changes only its y^q coefficient. Therefore the tangent does not divide
the next term, and the local lemma prevents two components meeting there.
Coordinate symmetry covers all three diagonals. q≥4 supplies the required
local order, with all denominators checked before division.

Off R, the four elements a,b,1,l are pairwise distinct. Define A,B by
A^q=a^(1−q)+l^(1−q), B^q=b^(1−q)+l^(1−q). Frobenius is bijective over
the algebraic closure, so these exist uniquely. If A=B=0, then a/l,b/l
and 1/l lie in F_q; hence a,b,l∈E∩F_q=F2 and all equal 1, impossible.
Individual A or B may be zero and are not divided by.

The numerator begins with L^q, L=Ax+By, followed by
a^(−q)x^(q+1)+b^(−q)y^(q+1)+l^(−q)(x+y)^(q+1).
The nonzero tangent direction is (B,A). Clearing the nonzero denominator
a^q b^q l^q in its evaluation leaves
T=B(b+b^q)+A(a+a^q). Direct expansion gives the B coefficient
b*l^q+l*b^q+a*b^q+b*a^q=b*(b+1)^q+(b+1)*b^q=b+b^q;
interchange a,b for the A coefficient. Raising T to q gives
a+b+a^(q²−q+1)+b^(q²−q+1)+l^(1−q)[(a+b)^q+(a+b)^(q²)].
Using a+b=l+1 reduces this exactly to 1+a^d+b^d+l^d, d=q²−q+1.
This independently checks both algebraic identities, their constants,
zero-coefficient boundaries and the full denominator.

The published Kasami APN theorem applies on E because gcd(i,m)=1.
Its parameter can be reduced to a positive residue modulo m: Frobenius
gives the same function, including zero, and the residue is nonzero.
If T=0, the four distinct elements a,b,1,l all solve the SAME equation
z^d+(z+c0)^d=a^d+b^d, c0=a+b=1+l≠0. This contradicts the two-solution
bound. Thus the next numerator term is nonzero on the tangent L=0.
Division by unit R changes that term only by a multiple of L^q and
cannot cancel its restriction. The local lemma excludes every off-R
intersection. The finite-field theorem is used at actual singular points,
not to confuse polynomial irreducibility with a function identity.

At P=(1:1:1), the numerator's degree-q term cancels and its next term is
x^q y+x y^q. Dividing by xy(x+y) gives order q−2 and cone
(x^(q−1)+y^(q−1))/(x+y). It has exactly the q−2 distinct directions
indexed by F_q minus F2. Reduced phi, if reducible, can be split into
coprime positive-degree homogeneous U,V. Their central cones partition
this squarefree cone, so their local intersection is r*s, where r,s
are their multiplicities at P. A factor avoiding P has multiplicity
zero and local intersection zero. No other intersection is possible,
including infinity. Projective Bézout therefore gives deg(U)deg(V)=r*s.

For any nonconstant divisor H, multiplicity at P is at most deg H.
Equality, in coordinates P=(0:0:1), makes every monomial independent
of Z; H is then a binary form and splits into absolute lines. T1 excludes
this, so both multiplicities are strictly below the corresponding degrees.
Their product is strictly below deg(U)deg(V), including the zero cases,
contradiction. This proves the entire proposed criterion, not just one
F2-defined absolute component or a genus claim for a reducible curve.

For ell=2^s−1, order m=s follows because no smaller positive 2^t−1
can be divisible by ell. Taking i=2 and odd s≥3 yields n=2^(s+2)−3.
No n13 claim is introduced: ell3,i2 violates the gcd hypothesis. i1,
ell1,n1/n3 and binary-weight-two boundaries are outside this packet.
Failure of gcd(i,m)=1 is failure of this proof, not actual reducibility.
Whole absolute irreducibility excludes even nonhomogeneous positive-degree
ordinary F2 products in the official coefficientwise question.

## Operative source checks and disposition

Fresh original official B4 setup/(b) checked. Fresh Carlet–Kim–Mesnager
definitions, standing hypothesis, reduction passages, Lemma4 and COMPLETE
operative odd proof/first even proof were read through line784. Even m
forces odd parameter; its published MCM Lemma5 is an explicit input.
Original underlying Lemma4/5 proofs were not freshly audited; the later
alternative even discussion is unused. This is a published theorem import,
not a new elementary APN theorem or a claimed entire ten-page proof audit.

Fresh Fulton Section3.3 theorem/proof/properties2419–2624 and ENTIRE
Section5.3 Bézout proof3829–3924 were read. Coprime tangent cones, no
common component, algebraically closed field and the unit case meet
their exact hypotheses in characteristic two. No Hessian, separable Gauss
map or characteristic-zero tangent theorem is needed. Rest of the book
and author's AppendixA read are not adopted as a fresh whole root read.

No substantive defect or repair found; ALL64 pass in their exact scopes.
Six closed notes retain whole-vs-component, pure-cone next-term division,
finite-field/gcd/source branch, infinity, factors avoiding P and priority
limits. Findings are withheld until BOTH entire initial reviews and all
final readbacks/separate verifications are explicitly confirmed complete.
No mathematical executable,CAS,scan,routine test,author/source or old
certificate replay supplied the audit. General annual classification,
published overlap and external validation remain open or unclaimed.
