# DR7 OTHER initially blind WHOLE1 reconstruction

18 October2026 UTC. Root did not construct NEW DR7. A is its sole
constructor and excluded. ALL48 obligations and the ENTIRE14-file author
packet were read and independently reconstructed. Findings remain
EMBARGOED until BOTH ENTIRE initial freezes, FULL final model readbacks,
SEPARATE verifications and root's explicit BOTH confirmation. No NEW peer
filename, finding, file, hash, metadata or conclusion commentary accessed.

## Domain and ordinary quantities

The official open part(b) asks for all signed integer quadruples. This
packet studies only degree p-1, exponent p, p>=37 prime, ordinary
|X|>=2, Phi_p(X)=Y^p, with the ADDITIONAL p|X(X+1). There is no
claim every official solution enters this sector. Exactly one center
a=0 or-1 has p|X-a; its exact depth s and positive p-free c with
X=a+epsilon*c*p^s are well-defined. Both ordinary signs are retained.

For U=|X|, Phi_p(U)=(U^p-1)/(U-1) and Phi_p(-U)=(U^p+1)/(U+1)
are strictly between1 and U^p for U>=2. In the first case U2 still
gives2^p-1<2^p. In the second,1<U^(p+1) gives the strict upper
inequality. Odd p therefore forces1<Y<U, with Y a positive integer.

At0, Phi'=1. At-1, differentiating(T-1)Phi=T^p-1 gives
1-2Phi'(-1)=p, hence Phi'(-1)=-(p-1)/2=-K. Both are p-units.
Thus Phi_p(X)-1=(X-a)A_a(X) has exact valuation s. The actual
equation modulo p makes Y=1 modp. If h=v_p(Y-1)>=1, the linear
term of Y^p-1 has valuation h+1, the interior terms at least1+2h,
and the top term ph>h+1. Hence s=h+1>=2, with no imported depth
theorem or Jacobi/class-number assumption.

## Exact unitary partition, including every prime power

For each ell|c, ell!=p and Y^p=1 mod ell. Thus its actual order is
1 or p. At order1, Phi_p(Y)=p mod ell is a unit, even for ell2;
the entire c-power in Y^p-1 lies in Y-1. At order p, Y-1 is a
unit and that entire power lies in Phi_p(Y). Therefore

    g=gcd(c,Y-1), b=c/g=gcd(c,Phi_p(Y)), gcd(g,b)=1

are unitary factors, not just a partition of distinct primes. Order1
primes congruent1 modp can remain in g. Every prime of b has
p dividing ell-1, and ell is odd; consequently ell=1 mod2p and
b=1 mod2p, including the empty product1.

The optional exact order-p valuation is also correct: at0 the quotient
A_0(0)=1 is an ell-unit; at-1 the quotient value-K is an ell-unit
because ell>=2p+1>K. Since ell does not divide Y-1, the valuation
of Phi_p(Y) is then exactly v_ell(c). No LTE formula at2 is needed.

## The ordinary integer remainder

Put Q=g*p^h and m=(Y-1)/Q. Coprimality of g and p and the exact
depth show Q divides Y-1 over Z, m>0 and p does not divide m.
The exact substitution is X=a+epsilon*p*b*Q. At0, U=pbQ; at-1,
U=pbQ-epsilon. Since Y<U are integers, Y-1<pbQ in every case,
including the negative neighboring branch. Thus0<m<pb strictly.

For the INDETERMINATE T use the full ordinary integer polynomial

    F(T)=Phi_p(a+epsilon*p*b*T)-(1+mT)^p.

Both0 and actual Q are roots. Writing c_j for the Taylor coefficients
of Phi_p at a, its linear coefficient is pL with
L=epsilon*b-m at0 and L=-epsilon*K*b-m at-1. The remaining
coefficients are

    B_j=c_j(epsilon*p*b)^j-binom(p,j)m^j, 2<=j<=p-1,

with final term-m^p*T^p. Every B_j is divisible by p. In particular
B_2/p=-K*m² modp is a unit: the first summand has a factor p²,
so c_2 need not be a unit.

In F(Q)/Q=0, B_2 Q has valuation1+h. Every interior j>=3 term
has valuation at least1+(j-1)h>1+h. The top term has valuation
(p-1)h>1+h; already p5,h1 gives the strict inequality. It is the
UNIQUE least-valuation nonlinear term. Cancellation therefore requires
L nonzero with v_p(L)=h exactly.

Separately the same integer polynomial identity gives Q|pL. As g
is p-free this gives g|L. Combining it with the exact p-depth gives
Q=gp^h|L. Hence J=L/Q is an ACTUAL NONZERO INTEGER, a p-unit.
Neither a rational number of denominator p nor a formal p-adic
representative would suffice for the next size argument.

Divide the complete F(Q)=0 by pQ². Every term is integral; the top
term contains Q^(p-2)/p with valuation(p-2)h-1>=2. Interior terms
j>=3 vanish modulo p. Thus J=K*m² modp. From p|L one has
m=epsilon*b modp at0 and m=epsilon*b/2 modp at-1. Since b=1
modp, this gives2J=-1 or8J=-1 modp respectively. These modular
halves are in F_p; no ordinary half of an odd cofactor is selected.
Substitution into mQ=Y-1 yields both displayed ordinary quadratic
identities with X/p or(X+1)/p actual integers.

## All sign-sensitive size bounds

At0 the nonzero integer2J+1 is a multiple of p. Thus |J|>=K;
if J<0,2|J|-1>=p and |J|>=(p+1)/2. At-1 the nonzero integer
8J+1 similarly gives J>=(p-1)/8 when positive and
|J|>=(p+1)/8 when negative. No convenient positive residue is
substituted for actual J.

At0,epsilon+, L=b-m lies in(-(p-1)b,b), so |L|<(p-1)b and
Q=|L|/|J|<2b. At0,epsilon-, L=-b-m<0 with |L|<(p+1)b;
the stronger negative-J bound again gives Q<2b.

At-1,epsilon+, L=-Kb-m<0 with magnitude<(3p-1)b/2. The
negative-J lower bound gives Q<4(3p-1)b/(p+1)<12b. At-1,
epsilon-, L=Kb-m may have either sign. If positive,L<Kb and
J>=(p-1)/8 give Q<4b. If negative,|L|<(p+1)b/2 and
|J|>=(p+1)/8 again give Q<4b. J0 was excluded before this split.
All endpoints remain strict because m<pb.

Multiplication by positive b gives cp^h<kappa*b², with c=gb.
Using b<=c also gives c>p^h/kappa. Uniform kappa<12 yields
b²>cp^(s-1)/12 and c>p^(s-1)/12. No cap on c or s was used.
If b1, Q=gp^h>=p>=37 contradicts Q<12. Therefore an ACTUAL
prime ell|b|c has order p, is1 mod2p and is at least2p+1.
This excludes arbitrary unbounded cofactor support containing no prime
1 modp; it does not exclude the remaining large b sector.

## Comparison, sources and adversarial boundaries

The new proof's only operative premise is the original ordinary equation
with its stated sector. Old RD/DR6 are comparison, not theorem imports.
I freshly read both complete current authority MDJSON pairs. Their full
mathematical bodies were historical whole reads, not new recertification
here. The old formal higher-trace warning is unverified context and is
not a Jacobi counterexample or proof premise. I supplied no NEW DR7 step.

Fresh official B4 setup/(b) confirms degree versus term-count convention
and signed variables. Fresh original BMR introduction/Theorem1(H)/order
consequence confirms positive-X overlap. Fresh Bennett--Levin signed
Proposition1 and theorem context confirms signed pure-X overlap. Neither
source's deep proof/computation/aggregated constituents is newly audited
or used. No new Mihailescu Lemma7/class-height proof read is claimed;
constructor limits remain its own. No distinct-prime source is applied
diagonally. Source methods and known conclusions are attributed; priority
and exhaustive overlap are unestablished.

I challenged partial-prime-power gcd splitting, order1 primes1 modp,
ell2, negative X/Y, linear-sign errors, L0, the top term, Q|L versus
Q|pL, residue representative choice and both J signs at the negative
neighbor. All are resolved within the frozen submission. No hypothesis
was silently added. The known p3 exceptions are outside p>=37; the
valuation estimates explicitly need p>=5 and b1 exclusion uses p>=37.

ALL48 pass in exact scope; zero substantive defects or author repairs,
eight closed notes. Large actual b, other sectors/exponents and annual
classification remain OPEN. Formal surviving parameters do not construct
an ordinary solution. No mathematical program, scan/CAS/test, source/
author routine or old certificate replay ran. Administrative code binds
bytes/labels only. Full final all-file readback/freeze and SEPARATE
verify must precede findings release; coordinator acceptance still needs
the second OTHER ENTIRE audit and full reconciliation.
