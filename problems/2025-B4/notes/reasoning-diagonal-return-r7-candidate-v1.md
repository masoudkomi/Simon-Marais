# Actual cofactor order and an ordinary quadratic remainder

18 October 2026 UTC. **Candidate proof - unverified.** Sole NEW constructor:
`/root/review_2021_reasoning_j15_r2` (A). TWO OTHER initially blind ENTIRE
WHOLE audits and coordinator reconciliation are required. Requested inherited
gpt-6.1-sol/max; independent effective-setting readback is unavailable.

This concerns only the actual signed prime-diagonal portion of official
2025 B4(b). No preliminary (a), full annual classification, universal upper
height bound, Jacobi realization, or novelty claim is made.

## 1. Exact ordinary domain and proposed advance

Put

    Phi_p(T)=1+T+...+T^(p-1).

Throughout, p>=37 is PRIME, X,Y are ORDINARY integers, |X|>=2, and

    Phi_p(X)=Y^p,              p divides X(X+1).                    (S)

The official degree here is p-1 and the perfect-power exponent is p. Condition
p|X(X+1) defines the sector being studied; it is not a reduction of every
official solution to this sector. Both signs of X and both possible centers
are retained. There is a unique a in {0,-1} with p|X-a. Define

    s=v_p(X-a),  epsilon=sign(X-a),  c=|X-a|/p^s.

Thus c is a positive ordinary integer, p does not divide c, and
X=a+epsilon*c*p^s. We shall rederive s>=2 without a Jacobi or class-number
assumption. All valuations below are ordinary rational-prime valuations.

The new information is about the MASS of a particular actual factor of c,
rather than another necessary residue for c of bounded size. Define

    g=gcd(c,Y-1),              b=c/g.                              (1)

The proof shows that this is a COPRIME, full-prime-power partition: primes of
g have ord_ell(Y)=1, while primes of b have ord_ell(Y)=p. In particular,
primes congruent1 modp can occur in EITHER part. Calling g the part supported
on primes not congruent1 modp would be false.

The proposed claims are as follows.

**DR7A (exact ordinary partition).** We have Y>1, Y<|X|, s>=2, and
v_p(Y-1)=s-1. The factors in (1) are coprime unitary factors of c, with

    g=gcd(c,Y-1),   b=gcd(c,Phi_p(Y)),   gcd(g,b)=1,
    b=product_(ell|c, ord_ell(Y)=p) ell^(v_ell(c)),
    b=1 mod(2p).                                                   (2)

Empty products are1. No existence assertion for actual solutions is implicit.

**DR7B (a nonzero INTEGER quadratic remainder).** Set

    h=s-1,  Q=g*p^h,  m=(Y-1)/Q,  K=(p-1)/2,
    L=epsilon*b-m                  if a=0,
    L=-epsilon*K*b-m               if a=-1.

Then Q,m are positive ordinary integers, h>=1, p does not divide m, and

    0<m<p*b,       J=L/Q is an integer,       p does not divide J. (3)

In particular J is NONZERO. More precisely,

    2J=-1 modp       if a=0,
    8J=-1 modp       if a=-1.                                      (4)

Equivalently these are the actual ordinary identities

    Y=1+X/p-J*Q^2                         if a=0,
    Y=1-K*(X+1)/p-J*Q^2                   if a=-1.                (5)

The divisions in (5) are by an actual divisor of X or X+1. These are not
identities obtained by assigning a formal p-adic representative to Y.

**DR7C (cofactor mass).** The following strict inequalities hold:

| Actual case | Proved inequality |
| --- | --- |
| a=0, either epsilon | Q<2b |
| a=-1, epsilon=-1 (X=-c*p^s-1) | Q<4b |
| a=-1, epsilon=+1 (X=c*p^s-1) | Q<4(3p-1)b/(p+1)<12b |

Consequently, uniformly in every actual s and ordinary c,

    b^2 > c*p^(s-1)/12,             c > p^(s-1)/12.                (6)

The sharper case-specific versions are b^2>c*p^(s-1)/kappa and
c>p^(s-1)/kappa, where kappa is respectively2,4, or4(3p-1)/(p+1).
This constrains the unitary order-p factor when c is unbounded.

**DR7D (a whole unbounded-cofactor family is excluded).** We have b>1.
Hence an actual prime ell divides c with

    ord_ell(Y)=p,       ell=1 mod(2p),       ell>=2p+1,             (7)

and therefore c>=b>=2p+1. In particular there is no solution in (S) whose
cofactor c is supported entirely on primes not congruent1 modp, regardless
of their sizes, numbers, or exponents. More generally any actual order-p
part b failing the appropriate inequality in DR7C is impossible.

The pure-X prime-factor conclusion overlaps published work; the complete
argument here is supplied independently and its priority is not asserted.
The neighboring center and the quantitative factor balance are the useful
targets of this checkpoint. The proof does not bound b above or remove
the remaining large-order-p-factor sector.

## 2. Ordinary size and the exact p-depth

Let U=|X|>=2. Since p is odd, Phi_p(X)>1 for both signs. For X=U,

    Phi_p(U)=(U^p-1)/(U-1)<U^p.

For X=-U,

    Phi_p(-U)=(U^p+1)/(U+1)<U^p.

Thus Y is the positive integer p-th root, 1<Y<U. This also rules out any
signed choice of a negative Y in (S).

We have Phi_p(0)=Phi_p(-1)=1. The first derivative is1 at0. At-1,
differentiating (T-1)Phi_p(T)=T^p-1 gives

    1-2Phi_p'(-1)=p,       Phi_p'(-1)=-K.

Both derivatives are p-units. Therefore, for a=0 or-1,

    Phi_p(X)-1=(X-a) A_a(X),       A_a in Z[T],
    A_0(0)=1,      A_-1(-1)=-K,
    v_p(Phi_p(X)-1)=s.                                          (8)

Reduction of (S) modulo p gives Y^p=1 modp, hence Y=1 modp. Write
v_p(Y-1)=h>=1. In the expansion of (1+(Y-1))^p-1, the linear term
has valuation h+1. Terms of degrees2,...,p-1 have valuation at least
1+2h>1+h; the degree-p term has valuation ph>h+1. Thus

    v_p(Y^p-1)=h+1=s,          h=s-1>=1.                         (9)

This elementary proof concerns e=0 and the two stated centers; it does
not recertify a broader published cyclotomic depth theorem or center1.

## 3. Extracting the whole prime powers of c

Let ell be any prime divisor of c. Then ell!=p and

    Y^p=Phi_p(X)=Phi_p(a)=1 (mod ell),

so Y is nonzero modulo ell,
and its multiplicative order is either1 orp.

If the order is1, then

    Phi_p(Y)=p (mod ell)

is an ell-unit. Since c divides Phi_p(X)-1=Y^p-1, it follows that

    v_ell(Y-1)>=v_ell(c).

If the order is p, then ell does not divide Y-1; the same factorization
Y^p-1=(Y-1)Phi_p(Y) gives v_ell(Phi_p(Y))>=v_ell(c). These alternatives
prove every full-prime-power statement in (2), including coprimality;
one cannot replace this by merely partitioning the distinct primes.

For completeness the order-p valuation is exact. At center0, A_0(0)=1
in (8), so every ell|X has v_ell(Phi_p(X)-1)=v_ell(X). At center-1,
an order-p prime has p|ell-1, so ell>=2p+1 and cannot divide K. Thus
A_-1(-1)=-K is again an ell-unit, yielding the same equality with X+1.
Since ell is p-free in c and ell does not divide Y-1, in both cases

    v_ell(Phi_p(Y))=v_ell(c)       whenever ell|b.                (10)

An order-p prime has p|ell-1 by the order of the finite group F_ell^*.
It is odd, and p is odd; hence2p divides ell-1. Multiplying these actual
prime powers proves b=1 mod2p, including the possible empty product.

## 4. The full integer polynomial and its unique lowest valuation

The definition of g and (9) show that Q=g*p^h divides Y-1, so m in
DR7B is a positive integer with p not dividing m. Also

    X=a+epsilon*p*b*Q.

For a=0, U=p*b*Q. For a=-1, U=p*b*Q-epsilon. Since Y<U and both
are integers, Y-1<U-1<=p*b*Q in all cases; equality in the last bound
can only concern the bound for epsilon=-1, not Y-1. Thus 0<m<p*b.

For an INDETERMINATE T, form the ordinary integer polynomial

    F(T)=Phi_p(a+epsilon*p*b*T)-(1+m*T)^p in Z[T].                (11)

It has F(0)=0 and F(Q)=0. Write c_j=[Z^j]Phi_p(a+Z), which are
integers and vanish for j>=p. In particular c_1=1 for a=0 and
c_1=-K for a=-1. Thus

    F(T)=p*L*T+sum_(j=2..p-1) B_j*T^j-m^p*T^p,
    B_j=c_j*(epsilon*p*b)^j-binomial(p,j)*m^j.                  (12)

Every B_j is divisible by p. Since binomial(p,2)=p*K and p does not
divide m,

    B_2/p=-K*m^2 modp,          v_p(B_2)=1.                     (13)

The first summand in B_2 is divisible by p^2; no value of c_2 or extra
unit assumption on a Taylor coefficient is needed.

Evaluate F(Q)/Q=0. Among all terms OTHER than pL, the unique term of
least p-valuation is B_2*Q, with valuation1+h. Indeed

    v_p(B_j*Q^(j-1))>=1+(j-1)h>1+h       for3<=j<=p-1,
    v_p(m^p*Q^(p-1))=(p-1)h>1+h.

The last strict inequality uses p>=5 and h>=1. Consequently cancellation
forces

    L!=0,              v_p(L)=h.                               (14)

Separately, (12) evaluated at Q and divided by Q shows Q|pL in Z.
Since p does not divide g, this implies g|L. Combining that fact with
(14) proves Q=g*p^h divides L. Hence J=L/Q is a nonzero INTEGER
and v_p(J)=0. In particular, divisibility by p alone would not have
been an adequate ordinary lower bound for J.

Now divide F(Q)=0 by p*Q^2, using L=JQ. Every resulting term is an
integer. For the leading term of degree p, this uses

    v_p(Q^(p-2)/p)=(p-2)h-1>=2.

The terms with3<=j<=p-1 also vanish modulo p. Equations (12)-(13) give

    J=K*m^2 modp.                                               (15)

Since p|L, one has m=epsilon*b modp at0 and
m=-epsilon*K*b=epsilon*b/2 modp at-1. Because b=1 modp, (15)
becomes precisely (4). Dividing by2 or8 HERE is in F_p; no ordinary
half of an odd cofactor has been used. Finally mQ=Y-1 and L=JQ
give the actual identities (5).

## 5. Ordinary size of J and the factor-balance inequalities

If a=0, then2J+1 is a nonzero multiple of p. Hence

    |J|>=(p-1)/2=K.

If also J<0, then -2|J|+1 is a negative multiple of p and therefore

    |J|>=(p+1)/2.                                               (16)

At a=-1,8J+1 is a nonzero multiple of p. Thus

    J>0 implies J>=(p-1)/8,
    J<0 implies |J|>=(p+1)/8.                                  (17)

These are real lower bounds on ACTUAL nonzero integers. No choice of
a convenient positive representative is being imposed on J.

We apply (16)-(17) to the following complete cases.

* a=0, epsilon=+1: L=b-m lies strictly between -(p-1)b and b,
  using0<m<pb. Thus |L|<(p-1)b. Together with |J|>=K and
  |L|=Q|J|, this gives Q<2b.
* a=0, epsilon=-1: L=-b-m<0 and |L|<(p+1)b. Now J<0, so the
  stronger bound |J|>=(p+1)/2 in (16) again gives Q<2b.
* a=-1, epsilon=+1: L=-Kb-m<0 and
  |L|<(p+K)b=(3p-1)b/2. The negative-sign bound in (17) gives
  Q<4(3p-1)b/(p+1)<12b.
* a=-1, epsilon=-1: L=Kb-m. If J>0, then L<Kb and
  J>=(p-1)/8, yielding Q<4b. If J<0, then
  |L|<(p-K)b=(p+1)b/2 and |J|>=(p+1)/8, again giving Q<4b.
  J=0 was already excluded in (14), before this sign split.

All inequalities are strict; the integer endpoint m=pb was excluded
by the actual inequality Y<U. This proves the table in DR7C. Multiplying
g*p^h<kappa*b by b and using c=gb gives

    c*p^h<kappa*b^2.

As b<=c, it also gives c>p^h/kappa. Uniformly kappa<12 except
the cases with still smaller constants2 and4, so (6) follows.

## 6. The unbounded-cofactor exclusion and comparison with old scopes

If b=1, then Q=g*p^h>=p>=37. But DR7C gives Q<12, a contradiction.
Thus b>1. Every prime factor of b satisfies (7), and (2) gives
b>=2p+1; since b divides c, the same lower bound holds for c.
This is independent of any a priori bound on c or s. No prime table,
CAS, finite search, ideal principality, or external height result is used.

For the center0 conclusion, published Bugeaud--Mignotte--Roy and signed
Bennett--Levin restrictions already establish related prime-divisor
conditions. Those results are attributed context, not imports of an
uninspected proof. The neighboring factor and quantitative balance are
proved above. No assertion of prior absence or mathematical priority follows.

Current accepted RD3 gives c>p^(s-2), while DR6 gives a logarithmic
cofactor bound, c2 exclusion, and finite parameters for each bounded c.
The present hand argument supplies a different constraint on the actual
unitary order-p factor, and the stronger depth bound c>p^(s-1)/12 in
this p>=37 sector. At s=2, c>=2p+1 is the more useful conclusion;
at s>=3 the factor-balance inequality continues uniformly without a cap.
These comparisons do NOT import those accepted proofs into this proof.

The remaining gap is concrete: neither this argument nor the cited
accepted scopes bounds the actual order-p part b above. In particular
large b with small g is consistent with these necessary conditions.
No formal choice of such numbers is asserted to solve (S), and a
congruence lift is not an ordinary integer solution. To obtain an annual
exclusion, one would still need an additional applicable restriction on
the large actual factors of gcd(c,Phi_p(Y)), or a different global bridge.

## 7. Proof/source/role boundaries

The operative proof in Sections2--6 is elementary integer-polynomial
algebra and finite-group order, with every valuation estimate supplied.
Only the displayed actual equation and domain (S) are mathematical premises.
There is no arbitrary formal Jacobi generator, norm-to-contact inference,
all-generator phase bound, class-number hypothesis, or hidden positivity
assumption on J. No source theorem is extended from distinct to equal primes.

FULL current accepted DR6 and RD bodies and authority MD/JSON were read,
along with the official local statement and current mutable research map.
The old formal higher-trace warning is only failed-route context. Its
unverified formal example is neither an actual Jacobi counterexample nor
a premise. Actual primary reading limits/URLs and failed retrievals are
recorded in the source companion. No full external proof or priority
audit beyond those exact limits is claimed.

A authored accepted DR6 and previously audited RD/BR/RS and other2025
packets. Those older roles are disclosed and are not independent
recertification of those accepted inputs. Root supplied only the generic
research question and no NEW DR7 proof inference; A is excluded from
the TWO OTHER whole reviews required for every new claim here.

No mathematical program, finite scan, CAS, old/source executable or
certificate replay was used. Only documentary hashing/JSON/file assembly
is permitted in the companion administrative code. All old files remain
unchanged; authorized weekly reset1792874445 only,90% TOTAL ceiling with
integration reserve. The separate NEW2021R20 peer embargo was preserved.
