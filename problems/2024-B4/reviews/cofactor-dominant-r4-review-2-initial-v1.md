# OTHER initially blind ENTIRE WHOLE dominant R4 review R2

2026-10-18 UTC. Reviewer C, `/root/review_2017_coarsening_r1`.
This is the complete independent reconstruction of R4A--R4E and ALL48
DC obligations. It is not a promotion. Root is sole NEW constructor
and is excluded from the two independent reviewer count. No corresponding
NEW A R4 report, findings, files, hashes or metadata was accessed before
this ENTIRE initial report and all its companions were frozen.

Exact main: `notes/cofactor-dominant-r4-candidate-v1.md`,14524 bytes,
SHA256 `b6c454eba513c0ebb364f4b53393741c8737239c5b03c75fc2a0ac000871e365`.
Exact eleven-file constructor freeze:3054 bytes, SHA256
`1d0c4e90c0b75a2417539401d4350e13dd29c9d3030fc06074f4cff18358371b`.
I read every constructor file, including the two earlier unverified
seed/source notes, ALL48 obligations, failures/worklog, sources,
administrative code and all metadata. Neither seed is a proof premise.

## 1. Verdict, official scope and independence

I found no substantive defect, required mathematical repair or advisory
in the stated R4A--R4E scope. All48 ledger rows pass their exact domains.
The proof establishes its unique-component conclusion before using
cofactor invariance; it does not presume every absolute factor is
F2-defined, or apply an irreducible genus inequality to a reduced union.
The local and global group arguments have the claimed orbit sizes,
and the final square completion retains the necessary negative term.

The only official target is 2024 B4(b), coefficientwise factorization
over F2. The field for geometric factors is K=F2bar. Put

    Q=2^s, s>=3; ell=Q-1; q=Q^k, k>=1;
    n=ell*q+1; N=ell*q-2;
    A=(ell-2)(ell+1); p=ell-1; a=(ell+2)/p.

Here p is a positive ordinary integer, NOT a prime or the characteristic.
The homogeneous quotient phi has degree N and is nonzero. Its factors
are homogeneous by least/greatest degree additivity. Excluding absolute
reducibility excludes any two positive-degree F2 factors, and such F2
factors lift coefficientwise to integer polynomials in the official
statement. This is not a polynomial-function question. All exponents
here are well above the n=1/3 zero/unit endpoints; nothing new about
those endpoints or preliminary part(a) is asserted.

My older roles include independent CG/FS/FP/structural reviews and
CP/sector3 construction elsewhere. Those accepted inputs are separately
identified; this is not a fresh independent self-review of old
constructed mathematics. I did not supply any NEW R4 inference. The
complete accepted CG main and acceptance scope were read. Only CG1/CG2
are imported; CG3's quartic conclusion, the pending cubic submission
and its reviewers are not used. The root cubic parent is a byte-bound
administrative ancestor, not a mathematical dependency.

## 2. Exact operative accepted geometry and inequalities

Write `W=X+Y+Z`, `R=(X+Y)(Y+Z)(Z+X)`,
`f=X^n+Y^n+Z^n+W^n`, `phi=f/R`. Accepted CG1 says phi is reduced
and has no absolute line factors. Its complete projective singularity
set has the ordinary central point P=(1:1:1), the noncentral prescribed
diagonal points, and the off-diagonal points. Every listed point has
all four coordinates X,Y,Z,W nonzero in F_Q, and at an off-diagonal
point these four values are pairwise distinct. The central tangent
cone is squarefree, multiplicity q-2, with none of the three prescribed
diagonal directions. At `(b:1:1)`, b in F_Q* minus1, the squarefree
cone has degree q and, in coordinates X=b+x,Y=1+y,Z=1, is a nonzero
scalar times

    x^q+x*y^(q-1)+(b+1)y^q.

In particular y=0 is not a tangent. Off-diagonal multiplicity is q+1
and its cone too is squarefree. Thus the initial cone of any factor
partitions a subset of distinct tangent lines, with no repetitions.

For ANY smaller proper reduced product U of degree e, `0<e<=N/2`,
let m be its central multiplicity, S its total noncentral diagonal
multiplicity, V its total off-diagonal multiplicity and

    S=3(e-m), D=(ell-3)e+2m-V.

CG2 gives the SAME positive ordinary integer D>=1 and

    P(e)=e^2-Ne+(A/4)(q+1)^2>=0,
    D*B<=T-aD^2/A,
    B=q+1-2ell*e/A, T=p(e-e^2/A).

I checked the UNSIMPLIFIED last inequality in accepted CG section6,
not just the weaker final upper bound. These hold for reduced products
of several absolute components, not merely irreducible U. The accepted
proof retains the classical c-1 correction component by component,
then uses no absolute lines to bound the number c of components by e/2.
Its exact contact/Bezout list includes projective points and factors
missing P. R4 has no additional tangent/contact hypothesis to supply.

## 3. R4A: every smaller factor has degree below A

Assume `q>=2ell+7`. Set `e0=(ell-2)q/2`; then
`N/2-e0=q-1>0`. Direct expansion gives

    P(e0)=(ell-2)/4[-q^2+2(ell+3)q+ell+1].

The bracket equals `-ell-6` at `q=2ell+7`. Its derivative
`-2q+2ell+6` is strictly negative thereafter. On `e<=N/2`,
`P'(e)=2e-N<=0`; hence every `e in[e0,N/2]` would have P(e)<0.
The actual smaller factor must therefore satisfy e<e0, which gives

    B>q+1-ell*q/(ell+1)=q/(ell+1)+1>0.

As D>0 and a,A>0, the unsimplified inequality implies
`T>=DB+aD^2/A>0` BEFORE division or comparison with D. Since
`T=p e(1-e/A)` and p,e>0, it follows that `e<A`.

This is a universal bound for EACH actual smaller proper product U.
There was no choice of a least-degree component, F2 definition, central
passage, orbit divisibility, irreducible cofactor assumption or pending
cubic theorem in the inference.

## 4. R4B: proper grouping, unique large component and descent

Assume also `N>=3A-2`. If every absolute component had degree<=N/2,
R4A would make each such integer degree at most A-1. Accumulate distinct
components until their combined degree d first reaches A. Total degree
N>=A makes this possible. The preceding degree and the last component
are each <=A-1, so `A<=d<=2A-2`. The complementary degree is
`N-d>=3A-2-(2A-2)=A`. Thus both products are nonconstant and their
smaller degree lies in `[A,N/2]`, contradicting R4A applied to that
actual reduced union. This closes the grouping step even when d itself
exceeds N/2; the smaller complement was explicitly allowed.

Hence an absolute irreducible component G of degree>N/2 exists. It is
unique by degree addition. Its complement H has degree `e<N/2`; if
positive it is a proper product to which R4A applies, so e<A. If H=1,
e=0<A too. Therefore `deg G=N-e>N-A`. Reducedness is used throughout
to make products of distinct components and to retain the accepted
CG2 input for those products.

Coefficient Frobenius preserves phi and the degrees of its absolute
components. Uniqueness gives `sigma(G)=cG`. Normalize one nonzero
monomial coefficient of G to1. The same coefficient of sigma(G) is1,
forcing c=1. Hence every G coefficient is fixed under squaring and
lies in F2. In `phi=GH`, Frobenius and cancellation then give
`sigma(H)=H`, so H is also F2-defined. This does not use a division
algorithm over a wrongly chosen coefficient field.

In particular, in this size regime absolute reducibility is equivalent
to F2 reducibility: if reducible then H has positive degree, and G,H
are its two positive-degree F2 factors. The reverse implication holds
over any field extension. In the irreducible case H=1 is permitted and
there is no spurious positive-degree cofactor.

## 5. Exact S4 action, including polynomial scalars

Permuting four coordinate forms X,Y,Z,W with their relation
`X+Y+Z+W=0` defines an invertible F2 linear substitution on any three
coordinates. Any three are independent; the inverse permutation gives
the inverse substitution. The four forms are distinct, so this is the
faithful S4 action. The numerator f is fixed. The three factors of R
are the three pair partitions: e.g. `X+Y=Z+W`. Permuting the four
forms merely permutes these three displayed factors. In characteristic2
there is no sign, so R is fixed EXACTLY, not just as a divisor.
Cancelling R from transformed f=R phi proves exact invariance of phi.

A substitution M preserves the unique large divisor and gives
`G(MX)=c_M G(X)`. Both polynomials now have F2 coefficients. At the
monomial normalized to1 in G, their scalar relation shows a nonzero
coefficient equal to c_M in the transformed polynomial. Thus c_M is
in F2*, which is `{1}`. This proves exact G invariance and, by
cancellation, exact H invariance. Merely preserving the divisor would
not have sufficed before the descent/normalization step; the submitted
proof performs these steps in the correct order.

## 6. R4C: actual invariant cofactor and integer divisibility

Assume H is nonconstant. Its tangent set at every singular point is a
subset of the distinct lines of the accepted ordinary cone. An element
of the point stabilizer preserves that subset because H is invariant.
Its multiplicity is the cardinality of the subset; multiplicity zero
is the empty subset. The following counts are in ordinary integers,
not arithmetic in F2.

At P, the transposition X<->Y acts by `(x,y)->(y,x)`. A fixed
projective direction in characteristic2 must have x=y: an eigenvalue
of the involution squares to1, hence is1. This sole direction is one
of the excluded diagonal tangents. The selected tangent set therefore
breaks into free pairs, so m is even, including m=0.

For a noncentral diagonal point write `P_b=(b:1:1)`, b!=0,1. The
four values are `(b,1,1,b)`. A projective stabilizer can multiply this
multiset by c only if it preserves its two values (c=1) or swaps them
(c=b with b^2=1). The latter would force b=1 in characteristic2 and
is excluded. Thus its stabilizer consists of the two independent swaps
of the equal pairs, with order4, and its orbit has size24/4=6.

Local calculations give more than this orbit count. In the stated
chart, swapping X and W gives `(x,y)->(x+y,y)`. Swapping Y and Z
and then normalizing Z to1 gives

    x'=(x+b*y)/(1+y), y'=y/(1+y),

whose tangent action is `(x,y)->(x+b*y,y)`. The only direction not
represented by finite slope u=x/y is y=0; it is not a cone line.
The two actions on the remaining slopes are translations by1 and b.
Since b is neither0 nor1, the additive group `{0,1,b,1+b}` has order4
and acts freely. Each invariant selected tangent subset therefore has
size divisible by4. Multiplicity is constant within each six-point
S4 orbit, so each such orbit contributes a multiple of24 to S. Thus
`24|S`, and the exact accepted identity `S=3(e-m)` gives `8|(e-m)`.
No assumption of a common multiplicity between different orbits appears.

At an off-diagonal singular point the four coordinate values are nonzero
and pairwise distinct by CG1. If a projective stabilizer multiplies this
four-element set by c, each nonzero element has a free multiplication
orbit whose length is the order of c. That order divides4, so c^4=1.
In characteristic2 this implies c=1. Distinctness then forces the
permutation to be the identity. Hence every off-diagonal orbit has
size24, and H's invariant multiplicities give `24|V`. This proves only
constant multiplicity WITHIN each orbit, which is all that is needed.

Finally `ell-3=Q-4` is divisible by4, m is even and V is divisible by24.
Thus the SAME `D=(ell-3)e+2m-V` is divisible by4. CG2 already supplied
D>=1 as an ordinary integer for this actual H; therefore D>=4. The
argument does not grant D>=4 to an arbitrary non-invariant factor.

## 7. R4D: complete square and strict threshold

For this H, the earlier argument gives B>0 and T>0. Divide the
unsimplified inequality by D>0, then use D>=4 and T>0:

    B<=T/D-aD/A<=T/4-4a/A.

Consequently

    q+1<=(p/4+2ell/A)e-(p/(4A))e^2-4a/A
        <=(pA+8ell)^2/(16pA)-4a/A.

This is the global REAL maximum of a concave quadratic. No attainable
integer maximizing degree is asserted, and using a larger real domain
can only make the upper bound valid. Expanding its value gives

    pA/16+ell+4[ell^2-(ell+2)]/(pA)
       =pA/16+ell+4/p,

because `A=ell^2-ell-2`. Hence reducibility requires exactly

    q<=pA/16+ell-1+4/p.

Only its STRICT reverse proves absolute irreducibility here; equality
is not excluded. Dropping the negative `-aD/A` term earlier would lose
the claimed exact constant, so its retention has been checked explicitly.

## 8. R4E: uniform parameter implications and limits

For Q>=8,k>=2, `q>=Q^2>2Q+5=2ell+7`. Also

    N-(3A-2)>=(Q-1)Q^2-3Q(Q-3)
              =Q(Q^2-4Q+9)>0.

Thus both size hypotheses hold for EVERY stated k>=2, not just the
examples. At Q=16, `ell=15,p=14,A=208`, and the threshold is exactly
`182+14+2/7=196+2/7`, below q>=256. Therefore every
`n=15*16^k+1`, k>=2, has whole absolutely irreducible phi. This is
a whole-polynomial conclusion, not merely existence of an F2-defined
absolute component.

At Q=8 the same threshold is `15+6+2/3=21+2/3`, below q>=64,
recovering an already accepted special family rather than creating a
new one. For general Q>=8,k>=3 the threshold is

    Q(Q-2)(Q-3)/16+Q-2+4/(Q-2)
       <Q^3/16+Q<Q^3<=q.

Both strict inequalities hold for the full interval Q>=8. This general
k>=3 consequence is derived here and does NOT use the pending cubic
packet even if that packet eventually proves an overlapping conclusion.
The unique-large-component and e<A cofactor reduction still applies
for all k>=2. It does not force absolute irreducibility for general
s>=5,k=2, and a failed sufficient threshold does not prove reducibility.
The k=1 branch does not meet the first size condition and is not covered.
Other odd parts and the full annual classification remain open.

## 9. Sources, boundary checks and review conclusion

The complete accepted CG body and MD/JSON acceptance/metadata were
checked in their exact scope. The classical multiplicity theorem is
used there on each irreducible component; its reduced correction is
retained before the absence-of-lines bound. I freshly read Fulton's
ENTIRE section5.4 Theorem2 proof, Problem5.25 and complete AppendixA.
The adjoint proof uses a nonzero derivative and Bezout over an
algebraically closed perfect field; irreducibility ensures some
derivative is nonzero in characteristic2. No characteristic-zero
Hessian or generic-tangent theorem is imported. These are classical
foundations, not new claims or an independent recertification of all
older proof inputs. Exact source read limits are in the companion.

The Frobenius source note is correctly an UNAPPLIED lead: property(A),
its separable generically finite root map and strict exponent condition
are additional hypotheses. I checked the cited original section5
statements and complete operative proofs. The new symmetry argument
does not need any of them. The primary HM component/whole distinction
and proper-divisor qualification remain binding, but no HM theorem
is invoked here. Férard2017's operative body remains unread; no
priority or absence-of-prior-art claim follows.

All projective points, factors not passing P, zero selected multiplicities,
the irreducible H=1 case, reduced unions, nontrivial polynomial scalars,
and the strict/equality numerical boundary have been retained. No finite
field scan, CAS, factorization program, optimizer or source/author rerun
supplied a step. The stated R4A--R4E conclusions pass this ENTIRE whole
audit, subject only to the required second OTHER initial and complete
coordinator reconciliation. The annual answer and novelty remain open.
