# Initially blind whole R7 audit R2

2026-10-17 UTC. Reviewer `/root/review_2022_complexity_r2`.
Requested `gpt-6.1-sol` / `max`; independently verified effective
settings unavailable. **Initial independent review, not promotion.**

I reconstructed the COMPLETE new R7A--R7D argument, all36 constructor
obligations, its cubic diagnostic, full source/log/failure records and
the exact accepted premises in their stated scopes. I found no
substantive mathematical defect in this partial submission. No repair
is requested. This conclusion is frozen before reading ANY new R7
peer report, issue ledger, conclusion or coordinator comparison.

This review does not exclude either side of the fork, the actual
double-root branch, any whole J15 mask, degree20 or the annual problem.
It does not establish a rational lift or novelty. The full report,
48-inference issue ledger, source-read record and integrity manifest
are one initial checkpoint; a summary alone is not the review.

## Independence and exact objects

The main target is `notes/reasoning-return-r7-candidate-v1.md`,
17704 bytes, SHA256
`8f4d1f71930b82e029066c4f4d249489c34e70b731e80a11458c833223fc18a6`.
The constructor freeze is `notes/reasoning-return-r7-freeze-v1.json`,
3391 bytes, SHA256
`d29dc9823b24ae2df97ee1c506cb8fe8881a2ec2d82a206e2a7411566df7afa8`.
All nine constructor artifacts and every declared metadata row are
checked separately by the new metadata-only reviewer script.

I did NOT construct NEW R7 or supply its weighted proof, triple or
coordinate argument. I previously reviewed the seven R3 packets,
single-center material, R5 and R6. Those roles are disclosed: older
accepted inputs retain their separate status; this is not a fresh
independent recertification of their old finite computations. The
constructor's earlier R3/R6 authorship and root's broad coverage lead
are also disclosed in the target. This report does not adjudicate
another reviewer's eligibility from a summary; the coordinator must
ensure the second audit meets the protocol independently.

My own immediately prior 2020 R5 and 2025 UW constructions remain
frozen. They are unrelated mathematical targets, not R7 proof inputs.
Their exact preservation, and all247 prior own frozen paths, is
verified in this checkpoint. Only the new assigned R7-review2 prefix
is written; no shared, old, candidate, Git or other-owner edits occur.

## 1. Official and accepted hypothesis reconstruction

The official2021 B4 hypothesis requires f in Q[X] and an ACTUAL
RATIONAL common root with each order1 through d-1. The other roots
may be nonreal or nonrational. Part(b), for d>=2, is the only
researched target. No preliminary prime-degree proof is reproduced.

Here d20,p19, J15, zero multiplicity EXACTLY two, and the only
center equation among H2,H3,H4 is H3(1)=0. Every a_j is19-integral
in the monic normalized derivative convention. The EXTRA assumption
is an ACTUAL double small root s, not merely two equal reduced
residues. Accepted J15 D1/D3 give the rational simple root r,
v(r)=nu>=1, v(s)=nu and s/r=2 modulo19. The Newton cluster has
fourteen slots of valuation1/14; none can be rational.

Before s is known rational, the only possible rational root values
apart from s are0,1,r. If s were not rational, these three would
cover all derivatives, contradicting accepted T1. Therefore s is
rational. The actual rational root set is exactly{0,1,r,s}, with
four distinct values and multiplicities2,1,1,2 respectively. Actual
rational division then gives

    f=X²(X-r)(X-s)²(X-1)g,

with rational monic degree14 g. Its local Eisenstein shape follows
from the fractional roots. Accepted G1 or R5C excludes its WHOLE
global root set from EVERY derivative, not only the local cluster.
Thus the same four values are the complete common-root possibilities
even over Qbar. Center1 is simple, so its being the sole common-root
value is equivalent here to full monic gcd X-1. No such multiplicity
assertion is made for the double roots0,s.

I read complete accepted R5/R6 and J15 bodies and scopes, the full
rational normalization body, Newton register and linked full body,
T1 register and full coverage proof. R5D is an exact accepted
conjunction of RC2 and PN4, restricted to this ACTUAL double/sole-H3
setting. It supplies a FIRST break in H6,H8,H10,H12,H14 at r.
It is not an unrestricted repeated-root exclusion. No large old
certificate was rerun or newly claimed independently certified.

## 2. Euler estimate independently checked, with both displacement cases

Put e=2m, j=20-e, 3<=m<=7 and suppose all preceding even Hasse
values at r vanish. Let h_k=H_k(f)(r), and set

    E(T)=[f(r+T)+f(r-T)]/2=T^e W(T²).

The constant vanishes because f(r)=0. Each nonleading even Taylor
coefficient is divisible by19; h20=1. This follows from the exact
normalized polynomial, with beta_j=binom(20,j)/19 a unit for every
2<=j<=18. The factorial numerator has one factor19 and neither
denominator does. Reductions occur AFTER taking the characteristic-
zero monic derivative, so no nonunit is inverted in F19.

Write B=(X-1)g and U=X²(X-r)B. At2r one has v(B(2r))=1 and
B'(2r)/B(2r) integral, hence

    U(2r)=4r³B(2r), v(U(2r))=3nu+1,
    eta=U'(2r)/U(2r)=2/r+B'(2r)/B(2r).

These divisions are nonzero: the constant term of B uniquely has
valuation1 at2r; every other evaluated term has higher valuation.
With delta=s-2r, using f(0)=f'(0)=0 gives exactly

    E(r)=delta² U(2r)/2,
    E'(r)=delta² U'(2r)/2-delta U(2r).

Subtract eE(r)/r from the derivative of T^e W(T²). The result is

    2r^(e+1) W'(r²)
      =-delta U(2r)[1+delta(m/r-eta/2)].

For delta!=0, v(delta)>nu since s/r=2 modulo19. The bracket is a
unit. The derivative W'(r²) is divisible by19: all its nonleading
coefficients have that factor, and its leading term has a positive
power of r² because degW=10-m>=3. The identity also proves W'
nonzero in this case. Thus

    v(delta)>=(e-2)nu,
    v(W(r²))=2v(delta)+(3-e)nu+1 >=(e-1)nu+1.

If delta=0, E(r)=0 directly gives W(r²)=0, without division by
delta. Both cases imply v(h_e)>=2nu+1, v(D_j(r))>=2nu and
v(a_j)>=nu by the normalized Taylor expansion. This reconstructs
the inherited input at arbitrary nu. The old selected-minimum bound
nu<=10 is neither needed nor converted into a displacement bound.

## 3. R7A: the strict weighted comparison is valid

Let u=a_(j-2) be NONZERO and tau=v(u)<nu, allowing tau>0.
Integrality makes tau an integer>=0. Since D_(j-2)(r)=u+O(r),
its valuation is exactly tau, and division by u leaves residue1.
The next even contribution h_(e+2)r² therefore has valuation

    2nu+tau+1 <=3nu.

Every later nonleading even term is at least4nu+1, the leading
one has valuation j*nu>=6nu, and W(r²) is zero or at least5nu+1.
There is exactly one possible cancellation partner at the first
weight: h_e. It follows that

    v(h_e)=2nu+tau+1,
    D_j(r)/(u r²)=-c modulo19,
    c=j(j-1)/[(e+1)(e+2)].

All displayed factors are19-units; the binomial ratio is computed
over Q first. In particular h_e!=0, so r is unavailable as its
common-root witness.

If there is no rational noncenter common root for H_e, the official
hypothesis supplies1; the constant a_j has depth>=nu and is nonzero
because a_j=0 would make0 a common root. This is already the required
nonunit essential center, with full gcd X-1 by Section1.

Otherwise choose an ACTUAL common witness w. It is0 or s, and
v(r-w)=nu in both cases. In

    D_j(X)=a_j+j a_(j-1)X+b u X²+sum_(l>=3)c_l X^l,
    b=j(j-1)/2,

the quotient [D_j(r)-D_j(w)]/(r-w) has valuation nu+tau. Its
quadratic contribution has at least that depth and its higher terms
have depth>=2nu>nu+tau. Thus a_(j-1) has depth>=nu+tau. Evaluating
at w gives a_j depth>=2nu+tau, including a_j=0 when w=0.
This PROVES integrality before defining the two scaled residues.

After X=r z and division by u r² all higher terms have excess
depth at least nu-tau>0. The quadratic Q has Q(1)=-c and either
Q(0)=0 or Q(2)=0. Writing its linear part as j*lbar*z gives

    w0: j*lbar=-b-c;
    ws: j*lbar=c-3b.

If the adjacent derivative H_(e+1) also used a noncenter zeta,
then y=zeta/r modulo19 is0,1 or2. Its degree-(j-1) normalized
polynomial, divided by u r, reduces to lbar+(j-1)y=0.
Solving gives y=rho or2-rho, where

    rho=1/2+1/[(2m+1)(2m+2)].

The residue set{0,1,2} is invariant under y->2-y. Its compatibility
would require the product denominator to equal -2,2 or2/3, i.e.
17,2 or7 modulo19. The actual five products reduce to

    56->18, 90->14, 132->18, 182->11, 240->12.

No candidate survives. This is a complete symbolic five-case check,
not an extrapolation or program. Both rho and2-rho are also nonzero,
so lbar!=0 and v(a_(j-1))=nu+tau EXACTLY. The adjacent order has
sole common root1 and gcd X-1. All conclusions of R7A follow.

The strict boundary is used twice: dominance of u over O(r), and
vanishing of cubic/higher terms after scaling. It is not cosmetic.
At tau=nu-1 the excess is still at least1, so the closest valid
integer endpoint is covered. u=0 is not silently assigned a finite tau.

## 4. R7B and R7C: the complete weighted first-break fork

Accepted R5D gives the least m0 in3..7 with h_(2m0)!=0. The
preceding ladder holds by minimality, so the Euler estimates above
apply. If the even order has no noncenter witness, the essential-
center alternative follows as in Section3. If it has one, r is
unavailable by definition of this break, so again w=0 or s.

If v(a_(j-2))<nu, R7A supplies the other alternative. In the
remaining case, INCLUDING a_(j-2)=0, D_(j-2)(r) has depth>=nu.
The next even contribution is at least3nu+1; every later
nonleading contribution is at least4nu+1 and the leading term is
at least6nu>=3nu+1. The value of W is still higher or zero.
Consequently v(h_e)>=3nu+1 and v(D_j(r))>=3nu.

Its quotient by r-w has depth>=2nu. Every contribution other
than the linear coefficient has that depth: the quadratic term
uses v(a_(j-2))>=nu and the higher ones use at least two factors
of small roots. Since j is a unit, v(a_(j-1))>=2nu follows.
The equation D_j(w)=0 then gives v(a_j)>=3nu. At w0 the constant
is exactlyzero. This proves the ENTIRE triple alternative, with
infinity allowed, rather than merely two nonunits.

The cases exhaust all possibilities. They need not be mutually
exclusive; no contradiction for the triple or essential center is
asserted. The argument does not use R6's unit coefficient theorem
in place of its own new weighted proof.

For R7C, j-1 runs over13,11,9,7,5 and j-2 over the five preceding
even indices. The hypothesis on EACH pair says its odd coefficient
has depth<2nu OR its even coefficient has depth<nu. The pair selected
by the first break therefore cannot satisfy the first two bounds
of the triple. The first alternative follows, at k=e or e+1 in6..15.
Old OR-unit assumptions imply these inequalities; the claimed
weakening is logical, with no assertion that the illustrative deeper
coefficient array is realized by a full rational polynomial.

## 5. R7D: exact exchange of rational double-root frames

Let a=1-s, a19-unit, and F(Y)=a^-20 f(s+aY). This is an ACTUAL
rational affine change. It swaps the two double-root origins,
fixes1, and sends the simple root r and old zero to

    r'=(r-s)/a, s'=-s/a.

Since s/r=2 modulo19, both new values have valuationnu and s'/r'
has residue2. Direct subtraction gives

    s'-2r'=delta/a.

In particular the exact-zero displacement and arbitrary finite
depth are preserved. The fourteen fractional roots retain valuation
1/14: subtracting a number of strictly larger valuationnu cannot
alter theirs, and division is by a unit. The transformed roots have
the exact same rationality/multiplicity pattern.

H_k(F)(Y)=a^(k-20)H_k(f)(s+aY). Thus the sole low center,
preceding even ladder and first break are preserved at r'.
Extracting the coefficient of Y^(20-j) over Q gives exactly

    a'_j=a^-j D_j(s).

In particular a'_0=1, a'_1=(s-1)/(1-s)=-1. All a'_j are
19-integral and reduce to a_j because s is divisible by19 and a
reduces to1. Therefore J15 and the whole unit mask are unchanged.
The new constant/linear coefficients vanish because s is actually
a double root, not because of a residue comparison.

At the next exchange a'=1-s'=1/a. Composing the arguments gives
s+a(s'+a'Y)=Y and the scalar prefactors multiply to1, so the
second operation returns f EXACTLY. This is an involution of frames,
not a claimed symmetry F=f.

Under the triple, the first three terms of D_j(s) have depths
>=3nu and the remainder starts at s³. For D_(j-1)(s), the first
two terms have depth>=2nu and the remainder starts at s². For
D_(j-2)(s), its constant has depth>=nu and the remainder starts
at s. All omitted coefficients are integral. Thus the triple is
preserved in one direction; the exact involution and same nu give
the reverse. Changing the rational origin therefore supplies no
contradiction for this remaining alternative.

## 6. Minimal cover, exact gap indices and the cubic boundary

T1 concerns a minimum rational COVER, not only a count of rational
roots somewhere. Among exactly four eligible values, each must be
the sole common-root value at some derivative: otherwise remove
that value and select witnesses from the other three at all orders.

The low supports are exact. H1 uses{0,s} from multiplicities and
the separable carrier. J15 D3's low reductions give H2:{r},
H3:{1},H4:{r}. For H5, c5 has valuation1 and is the uniquely
lowest term at every small rational root; the degree19/20 terms
carry the extra binomial19 factor. Hence H5:{1}. H19:{1}
because it is the centroid linear polynomial. Thus0 and s must
each be sole values at DIFFERENT orders in6..18. Their corresponding
indices j0,js lie in2..14 and are different. Characteristiczero and
the nonzero normalization scalar give exactly

    a_(j0)=0, D_(j0)(s)!=0;
    D_(js)(s)=0, a_(js)!=0,

with values at r and1 nonzero as well. Double-root gcds can have
multiplicity one or two. The old RC3 already contains the cover
mechanism under its stronger long ladder; R7 correctly does not
claim this observation as new or align the two gap indices.

Finally I recomputed the cubic diagnostic by hand. At m3,j14,
binom14,2=91=15 and binom14,3=364=3 modulo19, so the stated
scaled residues give Q=4z²+3z³. Its values are

    Q(0)=Q'(0)=0, Q(1)=7, H2(Q)(1)=4+9=13.

Since56=18 and2/18=17 in F19, 7+17*13=228=12*19.
The normalization factor can also be checked directly from
D14''/[14*13] and the exact next-even binomial ratio. This is
the leading even cancellation. It gives a consistent cubic INITIAL
jet at tau=nu, where truncation to a quadratic is invalid. It is
not a rational counterexample, a Q19 lift or a complete Euler/witness
system, and R7A--R7D do not use it as a proof premise.

## 7. Source and counterexample audit conclusion

I checked actual primary official wording, CLO's normalized derivative
equation7, §3.4 equations9--10/Lemma17, type/coverage definitions,
and Proposition19 with its unramified qualification. The fourteen
fractional roots explicitly violate the stronger theorem's all-root
hypothesis; that theorem is not imported. Marashdeh's support/vacuity
definition and TheoremB identify the one-nonzero-recycled-root scope,
which is not enlarged to this four-value problem. Its C/D support
statements also do not supply the missing multi-root conclusion.
The source record states actual read scopes rather than pretending
the entire external literature proof chain was reconstructed.

I attacked zero coefficients, positive tau, its strict/equality boundary,
delta0 and arbitrarily deep finite delta, repeated versus residue-only
slots, simple versus double gcd multiplicities, same-index gap claims,
both directions of the frame exchange, and possible carrier witnesses.
The submitted proof handles these cases in its stated domain. No
counterexample or substantive missing inference was found there.

The principal remaining mathematical gaps are already explicit:
neither the nonunit essential center nor the invariant deep triple
is excluded, and no global rational compatibility or lifting theorem
is obtained. These limits are not defects in the submitted partial
claims. No promotion is made by this reviewer. Both independent
whole initials and coordinator reconciliation remain the required gate.
