# A ramified phase criterion and an actual cofactor ideal, R10

2026-10-18 UTC. **Candidate proof - unverified.** Constructor C,
`/root/review_2017_coarsening_r1`. Requested inherited gpt-6.1-sol/max;
effective-setting readback is unavailable. TWO OTHER initially blind
ENTIRE WHOLE audits and coordinator reconciliation are required. No new
Diophantine exclusion, improved published height theorem, numerical
prime bound, annual classification or priority claim is made.

## 0. The actual question and the four statements

The open problem is 2025 B4(b), with ordinary signed integers in
`1+X+...+X^n=Y^q`, `n,q>=2`. Here the term count is a prime p and
the official degree is p-1. The diagonal equation considered below is

    Phi_p(X)=Y^p, p>=5 prime, X in Z, |X|>=2.                 (D)

This is a restricted part of the annual problem. Y is positive and >1.
No reduction of every annual solution to(D) is supplied. In particular,
distinct exponent and composite term-count cases are not eliminated.

Let K=Q(zeta_p), O=Z[zeta_p], j be complex conjugation, Kplus=K^j,
and P=(zeta-1). Set e=p-1 and normalize v_P(zeta-1)=1, so v_P(p)=e.
For a fractional ideal A, square brackets mean its ordinary ideal
class in Cl(K), not a selected generator. The extra global hypothesis

    (C)  [A]=[jA]                                              (1)

will ALWAYS be displayed when used. It is not assumed for all solutions.
It follows, for example, from the class-number hypothesis used in the
distinct-exponent source, but is not a consequence of local solvability.

The proposed results are:

* **R10A, a local statement without a Diophantine assumption.** In
  L=Q_p(zeta), for every X in Z_p, put
  `r_X=(X-zeta)/(X-zeta^-1)`. Then

      r_X in mu_p * L^(times p)
          iff X=0,1,or-1 modulo p^2.                           (2)

  The unique exponent a modulo p in `r_X=zeta^a*gamma^p` is2
  at center0 and1 at either center1 or-1; a possible sign at
  center1 is itself a p-th power. In particular r_X is NEVER
  an untwisted p-th power in L for X in Z_p. At every residual
  X=0 or-1 modulo p^2, the correctly twisted local root exists.

* **R10B, denominator clearing.** An exact power root of a ratio of
  coprime integral characteristic ideals produces two integral ideals
  whose product is the characteristic difference. No fractional
  generator is silently treated as integral. This proves the
  principality implication in R10C using the actual linear difference.

* **R10C, the distinct-exponent interface.** Suppose
  `Phi_p(X)=Y^q`, p>=5 and q odd primes, p!=q, |X|>=2, and
  X!=1 modulo p. Let `A^q=(X-zeta)`. Under(C), A is principal
  and `X-zeta=epsilon*rho^q` with rho integral and epsilon a
  real unit. This conclusion is already part of the published
  Chen--Mihailescu argument. The proof here exposes the actual
  denominator/difference step, rather than importing a general
  assertion about pairwise disjoint representatives of real classes.

* **R10D, the diagonal replacement.** For an ACTUAL(D) satisfying(C),
  R10A forces a unique center a in{0,-1} with

      X-a=sign*c*p^s, c>0, p not dividing c, s>=2.              (3)

  There are canonical coprime integral ideals J,H in O, both p-free,
  fixed by j, with

      J*H=(c), [J]=[jA], [H]=[jA]^(p-1).                      (4)

  Both descend to integral coprime ideals Jplus,Hplus of Kplus,
  with product(c). Their construction uses the SAME actual A and X.
  It is not a formal choice of prime factors realizing a solution.
  Moreover

      N_K(J) < 2^(p-1)*Y / p^[1+(s-1)(p-1)],                 (5)
      Y > p^[1+(s-1)(p-1)] / 2^(p-1).                       (6)

  If[A]!=1, both descended ideals are nonprincipal, and the right
  side in(6) can be multiplied by(p-1)^2. This is a conditional
  lower restriction, not claimed stronger than published bounds.
  In particular an ideal class survives inside the ACTUAL centered
  cofactor. It is not forced to be trivial by the local phase argument.

Accepted DR8 gives a much richer ordinary cofactor/order partition in
its stated additional sector p|X(X+1), p>=37. It supplies no uniform
upper support bound. The present ideal factorization does not identify
J or H with DR8's ordinary factors g,b,T,R_d, and does not add an
unproved compatibility assertion between those partitions. C reviewed
DR8 as an OTHER nonconstructor; this is not a new independent audit of
that accepted input. Older R6/R9 construction roles are also disclosed.
All new proofs below are hand arguments; no mathematical computation
or finite search is a premise.

## 1. Local units, with a proof of the exact depth used

Write pi=zeta-1. The Eisenstein polynomial Phi_p(1+T) shows that
L has residue field F_p, O_L=Z_p[zeta], and p is a unit times pi^e.
Let U_t=1+pi^t O_L. We need exactly

    U_1=mu_p*U_2,  U_t^p=U_(t+e) for t>=2,
    L^(times p) intersect U_1=U_(p+1).                        (7)

For the first identity, zeta^a=1+a*pi modulo pi^2. Its p choices
exhaust U_1/U_2. The intersection mu_p intersect U_2 is{1}.

For completeness the second identity needs no unproved convergence
assertion. If z has valuation t>=2, the term p*z in
`(1+z)^p-1` has valuation e+t, strictly smaller than every other
term: for2<=k<p the binomial coefficient has valuation e, and
`p*t>e+t`. Thus the valuation increases by exactly e.
Surjectivity can be seen by a contraction. Given u in U_(t+e),
write z=pi^t w and solve

    w=(u-1)/(p*pi^t)
        -sum_(k=2..p-1) [binom(p,k)/p]*pi^[t(k-1)]*w^k
        -[pi^[t(p-1)]/p]*w^p.                                (8)

The constant is integral. Every nonconstant coefficient on the
right has positive pi-valuation: for the last one it is e(t-1)>0.
It is therefore a strict contraction of the complete ring O_L,
so has a unique fixed point. This proves surjectivity and uniqueness
inside U_t.

Finally an arbitrary unit is its Teichmuller representative times
a member of U_1. The p-th power map is a bijection on the residue
roots of unity of order p-1. If its p-th power has residue1, that
representative is1. The first two assertions in(7), and zeta^p=1,
give the last. In particular a nontrivial zeta^a in U_1/U_2 is
not a p-th power. No assertion about a rational-base expansion or
an independent phase controller is involved.

## 2. R10A: the complete local phase calculation

First assume X!=1 modulo p. Reduce modulo pO_L. This ring is
`F_p[t]/(t^(p-1))`, t=pi. The p-th power of ANY unit in it is
constant. If `r_X=zeta^a*gamma^p`, then r_X has residue1, so
the constant is1. Writing x for X modulo p, d=x-1!=0, we obtain

    d+(d-1)t-t^2=(1+t)^a*(d+x*t) modulo t^(p-1).             (9)

The coefficient of t gives `d*a=-2`. The coefficient of t^2
then holds automatically. The coefficient of t^3 on the right is

    a(a-1)*[d(a-2)+3x]/6 = x*a(a-1)/6.                     (10)

It must vanish. The denominator6 is invertible since p>=5, and
a!=0. Hence x=0 or a=1. In the latter case d=-2, so x=-1.
The forced exponents are respectively a=2 and a=1. For p=5
the coefficient t^3 is still present; no p>5 assumption is hidden.

For x=0 put s=v_p(X) if X!=0. The exact identity is

    r_X/zeta^2=(1-X*zeta^-1)/(1-X*zeta),
    r_X/zeta^2-1=X*(zeta-zeta^-1)/(1-X*zeta).                 (11)

The second expression has valuation s*e+1. The denominator is a
unit and zeta-zeta^-1 has valuation1. At s=1 the valuation is p,
which is below p+1 in(7); at s>=2 it is at least2p-1, so a p-th
root exists. X=0 itself gives normalized value1.

For x=-1 write delta=X+1. Then

    r_X/zeta=(X-zeta)/(zeta*X-1),
    r_X/zeta-1=delta*(1-zeta)/(zeta*X-1).                   (12)

Its valuation is v_p(delta)*e+1 unless delta=0. The same argument
gives the threshold v_p(delta)>=2, with normalized value1 at X=-1.

It remains to handle X=1 modulo p, where the denominator used in(9)
is not a unit. Write delta=X-1. Direct cancellation gives

    r_X/(-zeta)=(1-delta/pi)/(1+delta*zeta/pi),
    r_X/(-zeta)-1=-delta*(1+zeta)
                       /[pi*(1+delta*zeta/pi)].              (13)

For delta!=0 the valuation is v_p(delta)*e-1. This is at least
p-2>=3, so the coefficient modulo pi^2 forces the phase exponent1
(the sign-1 is a p-th power). At depth1 it is p-2<p+1; at depth
at least2 it is2p-3 or greater, hence at least p+1. At X=1 the
normalized value is1. This proves both implications of(2).

Uniqueness of the exponent follows also directly from
`mu_p intersect L^(times p)={1}`, proved in(7). The only exponents
which occur are1 and2, both nonzero modulo p. Thus the untwisted
ratio is never a p-th power for X in Z_p. This does NOT assert the
same for arbitrary nonintegral X in Q_p or arbitrary two-variable
fractions whose second coefficient is divisible by p.

At the two residual ordinary centers allowed by DR8, (11)--(12)
also prove sharp LOCAL sufficiency for every permitted X, regardless
of the size or prime factorization of c. It supplies no global root
in K and no ordinary Diophantine solution.

## 3. R10B: an integral ideal lemma behind the ratio calculation

Let F be a number field, alpha,beta nonzero coprime algebraic
integers, and let B,D be coprime integral ideals with

    (alpha)=B^r, (beta)=D^r, alpha/beta=gamma^r,
    r>=2, alpha!=beta.                                     (14)

There is no integrality assumption on gamma. Unique prime-ideal
factorization gives `(gamma)=B/D`. Define

    I=(gamma-1)*D,
    H=(1+gamma+...+gamma^(r-1))*D^(r-1).                    (15)

These are nonzero integral ideals and

    I*H=(alpha-beta),
    every prime common to I,H lies above a divisor of r.     (16)

Here and below `(number)*ideal` denotes an ordinary fractional ideal
product, not an unjustified multiplication of two divisibilities.

Proof. At a prime of D with exponent d>0, gamma has valuation-d.
The valuations of gamma-1 and the sum in(15) are exactly-d and
-(r-1)d, since their least-valuation terms are unique. Clearing
the displayed denominators leaves valuation0 in both I,H. At a
prime of B both expressions are units. Elsewhere gamma is a unit
and the expressions are integral. This proves integrality; their
product follows from the geometric-series identity in(14).
If a prime divides I, it is not a prime of D and gamma=1 there.
The sum is then r modulo that prime, proving the final assertion.
Neither factor vanishes because alpha/beta!=1. This proves the lemma.

In particular I is an integral divisor of(alpha-beta) and its class
is[D]. If(alpha-beta) is supported at ONE principal prime ideal,
then I is principal, and D and B are principal. Merely saying that
an arbitrary ideal has no conjugation-fixed prime factors would not
prove this conclusion; the actual difference in(14) does the work.

## 4. Extracting the ratio under the exact class hypothesis

Suppose p,q are odd primes, p>=5, and

    Phi_p(X)=Y^q, |X|>=2, X!=1 modulo p.                     (17)

Put alpha=X-zeta, r=alpha/jalpha. Its p-1 conjugates are pairwise
coprime integral ideals: their differences have support only at P,
while alpha is a unit at P. Since their product is(Y)^q, every
valuation of(alpha) is divisible by q. Thus there is a unique
integral ideal A with

    A^q=(alpha), N_K(A)=Y>1, A+jA=O, P not dividing A.       (18)

Here q is odd and Phi_p(X)>1 at either sign, so Y>1. In the
diagonal case X=1 modulo p is impossible anyway: expansion at1
gives v_p(Phi_p(X))=1, inconsistent with a p-th power. This is
the open-(b) valuation interface, not a reproduction of preliminary(a).

Assume(C). Choose a fractional number b with `(b)=A/jA`.
There is a unit epsilon with `b^q=r*epsilon`. Consequently

    (b/jb)^q=r^2*(epsilon/jepsilon).                         (19)

The quotient epsilon/jepsilon is an integral unit with every complex
modulus1. Kronecker's elementary lemma makes it a root of unity:
the integer minimal polynomials of its powers have bounded
coefficients. There are finitely many such polynomials and finitely
many roots of them, so two powers coincide. The roots of unity in
Q(zeta_p) are mu_(2p). Reduction
at P gives epsilon/jepsilon=1 modulo P, excluding the minus sign;
write the quotient zeta^b0.

Choose integers u,v with2u+qv=1 and set
`gamma0=(b/jb)^u*r^v`. Then

    gamma0*jgamma0=1, gamma0^q=r*zeta^(u*b0).                 (20)

If q!=p, the q-th power map on mu_p is bijective. Divide gamma0
by a suitable root of unity to obtain an EXACT root gamma^q=r,
still with gamma*jgamma=1. Conversely such a root implies(C)
by taking its ideal. No principal generator of A has been presumed.

If q=p, (20) instead gives

    r=zeta^a*gamma^p, gamma*jgamma=1                         (21)

for some a modulo p. Conversely(21) implies(C). Thus(C) is exactly
the global twisted-root condition for the actual diagonal ideal.
Local solvability of(21) does not imply(C).

The roots-of-unity fact used above can also be checked from the
cyclotomic discriminant: only p ramifies in K, so roots with other
odd prime order or order4 are excluded; a primitive p^2-th root
has degree p(p-1)>[K:Q]. Signs supply the remaining order2 factor.
The discriminant assertion follows from
`Phi_p'(zeta^a)=p*zeta^[a(p-1)]/(zeta^a-1)` and its product.

## 5. R10C: why the distinct-exponent principality step works

For q!=p, use the exact gamma from(20) in R10B with B=A,
D=jA, alpha=X-zeta, beta=X-zeta^-1 and exponent q. The difference
alpha-beta=zeta^-1-zeta generates P: all conjugates of1-zeta
generate that same unique prime. Thus I is a power of the principal
ideal P, necessarily exponent0 or1 since I*H=P. It is principal.
Therefore jA and A are principal.

Choose an integral generator rho of A. Then alpha=epsilon*rho^q
with epsilon a unit. As above epsilon/jepsilon=zeta^b0. Replace
rho by zeta^t*rho with2*q*t=b0 modulo p. The remaining unit
has quotient with its conjugate1, so belongs to O_(Kplus)^times.
This proves R10C, including the integral-generator assertion.

The published hypothesis q not dividing
`|Cl(K)/image(Cl(Kplus))|` implies(C): the class[A] is killed
by q, so its image in that quotient is zero; every lifted real
class is conjugation invariant. This is an implication of the
EXACT source hypothesis, not an identification of an arbitrary
ideal representative with its conjugate. The source's exclusion
theorem has additional distinct-prime and signed-small-p limits;
none of its later exclusion arguments is imported here.

## 6. R10D: the canonical actual diagonal cofactor ideals

Now assume(D) and(C). By(21) and R10A, X=0 or-1 modulo p^2;
the X=1 residue has already been excluded in(18). The ordinary
center a and s,c in(3) are therefore well-defined, finite and unique.
For center0 choose k=1; for center-1 choose k=(p+1)/2. In both
cases2k is the forced exponent of zeta in(21). Let

    alpha'=zeta^-k*(X-zeta), pi_k=zeta^-k-zeta^k.

The exact identities are

    alpha'/jalpha'=gamma^p,
    alpha'-jalpha'=(X-a)*pi_k.                              (22)

For k=1 the constant terms cancel; for2k=1 modulo p they combine
with the X term into X+1. Each pi_k generates P and has absolute
norm p. Multiplication by zeta does not change the characteristic
ideal A. Equations(22) expose the centered integer which would be
lost in a mistaken transfer of the source's unit argument.

There are exactly p choices of gamma, differing by mu_p. Its
residue is1 since gamma^p has residue1. By(7) exactly one choice
belongs to U_2. Use that choice. Equations(11)--(12) give

    v_P(gamma^p-1)=s*e+1,
    v_P(gamma-1)=(s-1)*e+1.                                (23)

The valuation identity in(7) justifies the second equality; no
arbitrary choice of a root with valuation1 has been used.

Apply R10B to(22), and denote its two ideals by I,H0. Their
P-valuations are exactly(s-1)e+1 and e. Define

    J=I/(pi_k*p^(s-1)), H=H0/(p).                           (24)

They are integral and p-free: the divisions remove exactly the
P-valuations and introduce no other denominator prime. Equations
(16),(22) give

    J*H=(c), gcd(J,H)=O.                                   (25)

Away from p, common primes were excluded in(16); after(24) neither
ideal has a prime over p. Repeated prime powers in c are retained.
The ideal classes are those in(4), because the factors removed
in(24) are principal and[A]^p=1.

There is also genuine real descent. Since gamma*jgamma=1 and
`(gamma)=A/jA`, conjugation leaves
`I=(gamma-1)jA` invariant. For H0 the geometric sum is multiplied
by gamma^[-(p-1)] under conjugation, which cancels the conjugation
of(jA)^(p-1). Thus I,H0,J,H are all fixed as IDEALS. Only p can
ramify in K/Kplus; J,H are p-free. A conjugation-invariant ideal
at a split real prime has equal exponents at the two primes, and
at an inert real prime is already its extension. Hence J,H descend
to integral ideals Jplus,Hplus. Their coprimality and product(c)
descend prime by prime. No assertion that a conjugation-invariant
NUMBER is integral or generates these ideals is substituted here.

The normalization gamma in U_2 is unique among the p global roots,
so(24) is independent of the initially chosen b,u,v. These ideals
are canonical once the actual solution, zeta and the center are fixed.

At every complex embedding, |sigma(gamma)|=1. Also gamma!=-1:
its p-th power has residue1. Thus every |sigma(gamma-1)|<2, and

    N_K(I)=|N_K(gamma-1)|*Y <2^e*Y.                         (26)

Since `|N_K(pi_k*p^(s-1))|=p^[1+(s-1)e]`, (5) follows. The
nonzero integral ideal J has norm at least1, proving(6).

If[A]!=1, neither J nor H is principal, so neither real descended
ideal is the unit ideal. For a real prime away from p the residue
degree f is the order of its rational prime modulo{1,-1} in
F_p^times. Its norm is therefore1 or-1 modulo p. The norm of
each p-free real ideal is also1 or-1 modulo p. A nonunit such
ideal has norm at least p-1. Consequently N_K(J)=N_(Kplus)(Jplus)^2
is at least(p-1)^2, proving the stated strengthened version of(6).

One exact class-support consequence is worth keeping: if every
prime ideal of Kplus over a divisor of c is principal, then[A]=1.
If[A]!=1, an actual nonprincipal real prime over c must occur in
Jplus. In particular, if every rational prime of c is inert in
Kplus, those prime ideals are simply(ell) and hence principal,
forcing[A]=1. This does not exclude an actual solution with[A]=1;
no such missing implication is presumed.

## 7. What this does and does not repair

The source-led useful distinction is now exact. At distinct q, the
root-of-unity correction is absorbed, and a characteristic difference
with just the principal prime P forces principality. At q=p, an
untwisted ratio root is locally impossible even at every hypothetical
ordinary solution. The forced twist changes that difference to
`(X-a)*pi_k`; its entire cofactor ideal survives in(24)--(25).
Declaring either factor a unit would discard the actual centered
integer. The fully explicit local converse shows that deeper scalar
P-adic approximation of this ratio alone cannot rule out any of
the residual X classes. Global(C), simultaneous orders and ordinary
reachability of a Diophantine solution remain separate requirements.

The new actual ideal is not a substitute for the missing DR8
global implication. It gives no upper bound on c, b, e or the
number of R_d; it does not force the real class to vanish; it does
not construct a solution when the local root exists. Nor does a
lower bound in(6) conflict with an unevaluated or much larger upper
bound. Published stronger diagonal bounds and class-number results
remain visible; the older chapter and the later Appendix are not
newly certified by this packet. No classification follows from a
formal factor allocation or an arbitrary principal-ideal example.

The operative primary-source reading and its literal limitations
are recorded separately. The complete 2026 paper was read in web
PDF text, including its operative arguments, rather than importing
its abstract. Its exclusion theorem is not a premise of R10A--D.
The hand proofs here isolate the short phase/ideal interface only.
The method belongs to classical cyclotomic/Kummer algebra and to
the cited Nagell--Ljunggren literature; no novel-method claim is made.
