# J16 digits independent reconstruction, before constructor data

2026-10-16 UTC. Reviewer R1, not a constructor. This derivation and the
first verifier source were saved before reading constructor programs,
result JSON, branch serialization, or certificate chunks. Only the two
frozen candidate notes and accepted input proof packets were read.
Requested setting: gpt-6.1-sol/max. Effective setting unavailable.

The accepted T2 gives f=Z^2(Z-u)(Z-v)B, B=(Z-1)g with g monic
degree 15, Eisenstein at 19. Thus b0 has valuation 1 and b1,b2,b3
have valuation at least 1. Expanding gives

    c2=b0*u*v,
    c3=-b0*(u+v)+b1*u*v,
    c4=b0-b1*(u+v)+b2*u*v.

In particular c4/19 is a unit, c2 has valuation 1+v(u)+v(v), and
c3 has valuation at least 1+min(v(u),v(v)). Division of the c3
identity by 19^(1+nu) gives (R), including when exactly one leading
residue is zero. If v(u)=r<v(v)=s, the three low coefficient points
are (2,1+r+s),(3,1+r),(4,1), giving the two separate width-one
edges with no additional points on either supporting line. The accepted
lemma excludes u as an H1--H4 witness and v as an H1--H3 witness.
Both c2 and c3 are nonzero, so H2,H3 must use 1. Reversal exchanges
the two small roots.

If exactly one center is available, both valuations equal nu. After
scaling by c4*19^(4nu), reduction is
F=T^4-(U+V)T^3+UVT^2. Direct Hasse differentiation gives
H3(F)=4T-(U+V), with values -(U+V),3U-V,3V-U at 0,U,V;
H2(F)=6T^2-3(U+V)T+UV, with values U(3U-2V),V(3V-2U)
at U,V. Its value at zero is UV, a unit. These are exactly the two
sole-center restrictions. Neither derivation assumes distinct residues.

For a selected derivative D_j(w_j)=0 the coefficient of a_j is 1,
so a_j=-sum_{k<j} binom(j,k)*a_k*w_j^(j-k), a0=1,a1=-1.
All coefficient polynomials lie in Z[u,v]. At (0,0), noncenter a_j^0
is zero; center a_j^0 is the complete lower-coefficient sum. At a
noncenter position only k=j-1 is linear, with coefficient
-j*a_(j-1)^0 in the selected variable. Inactive positions therefore
have identically zero first derivative modulo 19. At centers the
linear coefficients obey the corresponding complete linear recurrence.
This proves compression onto the active ternary labels, with every
omitted ternary label independently restorable afterward. Disjoint
bit sets specify all assignments, including labels never used.

The divided center equation is Ptilde=-1+sum beta_j*a_j. Its
constant q0 must have valuation at least the minimum valuation nu,
since all its nonconstant terms do. It is necessary to check q0 is
nonzero for every mask; the verifier enumerates all binary masks itself
and then computes these constants exactly. The a17 and a18 constant
prerequisites follow by reduction modulo q=19^nu. To precision q*19,
a_j=a_j^0+q*(A_j*X+B_j*Y); every quadratic term has valuation at
least 2nu>=nu+1. Substituting in Ptilde, c2, and (R) gives precisely
the three first digit equations. Enumerating all 19^2 leading pairs,
discarding (0,0), and applying the sole-center conditions covers all
possible minimum valuations. The canonical-center convention justifies
using the contrapositive absence of a center equation for each sole flag.

For the second digit, divide F=f/Z^2 by Z^2-sZ+t. Direct reduction
gives rem(Z^2)=sZ-t and rem(Z^3)=(s^2-t)Z-st. Therefore

    R0=c2-t*c4-s*t*c5+...,
    R1=c3+s*c4+(s^2-t)*c5+... .

After u=qX,v=qY the vector
E=(Ptilde/q,R0/(19*q*beta18),R1/(19*q)) is integral over Z_19
under the checked constant prerequisites. For Ptilde this follows
from q|q0. For R0,R1 it follows from q|a18^0,a17^0, the fact
a_j-a_j^0 belongs to (u,v), and the explicit 19 in c2,...,c18.
The exceptional top coefficients first occur with degrees 17 (R0)
and 16 (R1), hence contribute q^16/19 and q^15/19 after division.
These are integral and divisible by 19 for nu>=1.

Modulo 19 the only nonconstant terms of E are the same three linear
rows as the candidate states: sum beta*A, A18, and beta17*A17+C4,
where C4=beta16*a16^0. Every degree >=2 term has coefficient
divisible by 19, including in R1 the dependence of a16 on X,Y.
The Jacobian is therefore constant modulo 19. Taylor's identity at
(U,V)+19*(U2,V2) yields the necessary affine system with constants
E(U,V)/19 mod 19; no nonsingularity or unique lift is needed.

The independent scalar verifier computes every term of the exact
normalized recurrence modulo M=19^(nu+2), building its actual modular
multipliers without an assumed degree truncation. It then constructs
all ordinary coefficients of f/Z^2 modulo N=19^(nu+3) and performs
full monic quadratic division. This suffices because c2,...,c18
have the explicit factor 19 and the two exceptional coefficients are
known exactly. R0,R1 modulo N determine their quotients by
19^(nu+2) modulo 19, and Ptilde modulo M determines its quotient by
19^(nu+1) modulo 19. The verifier checks divisibility before division.

For comparison with the written formulas, nu=1 retains -t*c4 in
R0, giving a18/19^2-(beta16*a16^0/beta18)*UV in E2/19.
Nu=2 makes that correction zero modulo 19. In R1, nu=1 retains
q*beta15*a15*((U+V)^2-UV) in E3 modulo 19^2; nu=2 removes it.
The complete division independently includes all these terms and all
higher terms, so a missing correction would appear as a row mismatch.

Rank is determined by Gaussian elimination of the augmented 3-by-3
matrix over F19. Rank deficiency is not a rejection criterion: only a
zero coefficient row with nonzero right side is inconsistent. Both
small roots' labels are allowed to be absent, used repeatedly, or to
have equal residues in both-center cases. Zero residue for one root
is retained exactly in both-center cases and does not mean that root
itself is zero: it represents a larger valuation.

No actual counterexample is established by a consistent branch, and
this computation is evidence for a finite necessary-condition reduction,
not for the unrestricted annual classification.
