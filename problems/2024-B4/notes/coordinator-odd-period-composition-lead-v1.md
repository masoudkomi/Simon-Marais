# A further odd-period route beyond the frozen even-inner candidate

2026-10-17 UTC. **Research lead / candidate deduction - unverified.**
Root constructor. This note does NOT change the frozen NJ-v2 target or
its two queued whole audits. No new peer NJ finding has been read.
No computation, CAS or sample supplied this argument. No novelty or
full annual claim. Before promotion this needs a complete frozen
submission and TWO OTHER whole audits, not a local extension check.

Use EXACT accepted GK notation q=2^k>=4,A,B,P_i,E_i,F=P2. The
frozen NJ-v2 proposes exclusion for every EVEN inner index. The
following route appears to cover every inner r having an odd prime
divisor ell of q²-1, including many ODD r. It is a separate proposed
strengthening and is not an accepted theorem or an instruction to
switch either reviewer off its current complete target.

Choose an odd prime ell dividing q²-1, and a primitive ell-th root
lambda in F_(q²). Put a=lambda+lambda^-1 and c=a+1. Then a!=0
and a,c lie in Fq: lambda is in Fq* if ell|q-1, and lambda^q
=lambda^-1 if ell|q+1. Thus c!=1, and

    A(c)=c+1=a, B(c)=1,
    A(c)^(q^(2i+1))=a, B(c)^(q^(2i+1))=1.

All point values P_i(c) satisfy the constant recurrence
v_(i+2)=a v_(i+1)+v_i, with v0=1,v1=c. The derivatives satisfy
the SAME recurrence with d0=0,d1=1, since every Frobenius-power
coefficient has derivative zero. The transfer matrix

    M0=[a 1;1 0]

has distinct eigenvalues lambda,lambda^-1, so M0^ell=I. For every
positive r divisible by ell this gives

    P_r(c)=1, P_(r+1)(c)=c,
    P_r'(c)=0, P_(r+1)'(c)=1.                     (OP1)

The exact local order at c is q. To see this without a tame inference,
write Z=T-c. For every recurrence with i>=1 the exponent is at least
q³, so modulo Z^(q³), P_i for i>=1 is a constant linear combination

    P_i(c+Z)=alpha_i F(c+Z)+beta_i(c+Z) mod Z^(q³).

The pairs start (alpha1,beta1)=(0,1),(alpha2,beta2)=(1,0) and
evolve by the invertible constant recurrence with determinant1.
Thus the pair (alpha_r,beta_r) cannot be zero. By OP1 its derivative
is alpha_r a+beta_r=0, so alpha_r!=0. F has no terms of degree
2,...,q-1 about c, derivative F'(c)=a, and its coefficient at Z^q
is (c+1)^(q²-2q+1)!=0, exactly by its displayed binary exponents.
After constant and linear subtraction, its first term is at q.
As q³>q, the claimed order of P_r(c+Z)-1 is exactly q.          (OP2)

Fix such r and put N=q^(2r+1). Consider advancing the recurrence
from the pair (P_(r+1),P_r) by ell steps. Modulo Z^(N+2), only
the FIRST coefficient perturbation, at index i=r, can matter: every
subsequent exponent is at least q²N>N+1. That first perturbation is

    epsilon=(A^N-a)P_(r+1)+(B^N-1)P_r.

It has order>=N. Its coefficient at N+1 is

    A'(c)^N P_(r+1)'(c)+B'(c)^N P_r'(c)
          =A'(c)^N!=0,

since A'=B'=(T+1)^(q-2) and OP1 applies. Frobenius powers have
no other N+1 term. The remaining ell-2 propagation steps multiply
this perturbation by U_(ell-2), where U0=1,U1=a and
U_(j+2)=aU_(j+1)+U_j. The exact expression

    U_j=(lambda^(j+1)+lambda^(-j-1))/(lambda+lambda^-1)

gives U_(ell-2)=1. Because the unperturbed ell-step transfer is
M0^ell=I, we obtain

    ord_Z(P_(r+ell)(c+Z)-P_r(c+Z))>=N,
    [Z^(N+1)] of that difference =A'(c)^N!=0.       (OP3)

Advancing by further blocks of ell changes coefficients first at
larger exponents. Hence OP3's SAME nonzero N+1 coefficient and
order>=N persist for P_s-P_r whenever s>r and ell divides s-r.
This is the key step still needing a fully explicit whole-audit
reconstruction of the transfer indices; it is not an extrapolation
from ell3 or the T0 recurrence.

For a hypothetical P_s=H(P_r), integer degrees force r|s. Indeed
write s=br+t,0<=t<r and Q=q²; modulo E_r=(Q^r-1)/(Q-1), Q^r=1
and E_s=E_t. If t>0 then0<E_t<E_r, which contradicts E_r|E_s.
Thus for r divisible by ell any larger s permitted by degrees
has ell|(s-r), as required by OP3. Smaller s fail by degree;
s=r forces H=T by injectivity.

Set K(Y)=H(Y)-Y. If K is nonzero, OP2/OP3 give that its exact
order at Y=1 is at least N/q=q^(2r). Expand there. The term of
order q^(2r), if present, is a Frobenius power and has only exponents
divisible by q^(2r) after substitution of P_r(c+Z)-1. It cannot
produce N+1. All higher terms have order at least N+q>N+1.
Thus a composition would give ZERO coefficient at N+1, contrary
to OP3. If K=0 the contradiction is immediate. The argument allows
inseparable H and vanishing initial allowed coefficients.

If every step survives full independent review, this proves the
same fixed-family whole-divisor exclusion as NJ2 for inner indices
with an odd prime factor in q²-1. It does NOT cover an odd r coprime
to q²-1, so it does not establish the tempting all-r theorem.
It does not prove irreducibility, rule out individual components,
or classify arbitrary official n. Even a valid extension remains
an auxiliary-family result. The only proposed external inputs are
the already accepted GK identities/degrees and CP1 for a later
whole-divisor transfer; no new source theorem is imported.
