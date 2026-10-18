# ENTIRE initially blind OTHER WHOLE R1: Runge R3, BR1–BR5

2026-10-18 UTC. Reviewer A, `/root/review_2021_reasoning_j15_r2`.
This is a complete independent review recommendation, not coordinator
promotion. Requested inherited gpt-6.1-sol/max; effective readback unavailable.

I reconstruct all five claims and ALL60 obligations. I find **zero substantive
defects and zero required author repairs**, with eight closed interpretation,
source and scope notes in the separate issue log. My recommendation is to
accept only the exact scoped BR1–BR5 conclusions, including **nonnegative
INTEGER weights** in BR1 and BR5. The general 2025 problem remains open.

B is the sole new constructor and cannot count as a reviewer. Root contributed
to the older accepted quotient and is excluded from the independent count for
this assignment. I reviewed the older accepted RS and RG packets and other
2025 work; that role supplies neither new authorship nor fresh independent
recertification of those premises. I did not construct or supply a new BR
inference. No corresponding C NEW R3 finding, report, source, code, hash or
metadata was opened or inventoried through this ENTIRE freeze. Findings remain
withheld until root confirms BOTH complete initially blind reviews.

## 1. Domain and exact operative arithmetic

The official open question is part(b). This submission treats only

    Phi_p(X) = 1+X+...+X^(p-1) = Y^p,
    p>=37 prime, X,Y ordinary integers, |X|>=2.

Its degree is p-1, not p. Both signs of X remain. There is no generalized
e1 assertion, smaller-prime result, off-diagonal classification or preliminary
part(a) investigation. I checked the original official(b) and local statement.

I read the complete accepted RS body/authority, the complete accepted R6 body
with particular reconstruction of its operative section5, and the complete RG
body/authority. The current acceptance pointers are exact. RS supplies the
chosen actual integer theta, the quotient and its arithmetic monic basis. R6
supplies the characteristic ideal and normalized, exactly untwisted beta.
The accepted analytic support bounds are not newly reproved or used for a
numerical conclusion here. RG is context, not a replacement proof.

Write D=p-1, K=Q(zeta_p), O=Z[zeta_p], lambda=1-zeta_p, and use DIRECT
sigma_a indices. For h=theta-N the actual coefficients are -1,0,1. The set
S of coefficient2 positions is disjoint from -S, has 3<=r<=D/2, and has
sum S=0 mod p. In particular h is nonzero. The direct F condition is not the
inverse M1 condition; both are used in their accepted scopes.

The actual ideal identities are

    (X-zeta)=Aideal^p, Norm(Aideal)=Y>1,
    (beta)=Aideal^theta, beta^p=Phi_p(X) A(X)/B(X),
    beta=1 mod lambda^2, all |sigma_a beta|=Y.

Conjugates of Aideal are pairwise coprime, nonunit ideals supported at split
primes ell=1 mod p. Multiplying the conjugate ideals gives (Y), not an assumed
principal pth root of (X-zeta). Thus for V=beta/Y,

    (V)=Aideal^(theta-N), V^p=A(X)/B(X), V*jV=1.

A nonzero coefficient of h has a prime in its corresponding nonunit conjugate
ideal, and no other conjugate contributes at that prime. Its valuation in
(V) is nonzero. Consequently V is not ANY root of unity. This is an actual
specialized-ideal proof; generic Kummer independence by itself would not
justify it. It does not remove the old linear-delta zero branch.

Since p does not divide X-1, reduction modulo p gives Phi_p(X)=1. Hence
Y=1 mod p. It follows that V=1 mod lambda^2. Write V-1=lambda^t u. The
nonunit-ideal argument makes t finite. Conjugation acts trivially on the
residue field and takes lambda to -zeta^-1 lambda, while

    j(V-1)/(V-1)=-1/V.

Taking residues gives (-1)^t=-1. Therefore t is odd and >=3. For c!=0,
1-zeta^c has valuation1 and cannot cancel V-1; B(X) is a lambda-unit.
These establish all actual arithmetic inputs of BR1 without pretending that
the unitary V is an algebraic integer.

## 2. BR1: all finite primes, nonvanishing, and the exact norm exponent

The weight domain is nonnegative integers, as explicitly specified by
obligation R3O-14 and the polynomial Q in section2. The introductory word
“weights” must retain that domain. No arbitrary real exponent is a polynomial
or an algebraic-integer assertion.

Let Q(Z)=product_c (Z-zeta^c)^w_c, d=sum w_c>0. Then Q^p is in O[Z]
and has degree pd. For each monomial Z^(lp+i), 0<=i<p, the relation
V^p=A/B gives

    B^d V^(lp)=A^l B^(d-l),
    B^d V^(lp+i)=A^l B^(d-l-1) b_i  (i>0),
    b_i=B V^i, b_i^p=A^i B^(p-i).

The first line has l<=d; the second has l<=d-1. Every exponent is therefore
nonnegative, including the top term A^d at degree pd. Since the b_i satisfy
monic equations over O[T], the whole function is integral over O[T]. Its
actual value at T=X in Z and V in K lies in O_K. This counts all primes,
including those above Y and p. It uses no arithmetic deck projection, inverse
of p or B, or unspecified denominator-clearing integer.

Every root of Q is a pth root of unity. The actual ideal proof above gives
Q(V)!=0 for every nonzero weight vector. Thus F_w=B(X)^d Q(V)^p is a
nonzero algebraic integer. Its exact local valuation is

    v_lambda(F_w)=p[sum_(c!=0)w_c+t w_0]
                 =p[d+(t-1)w_0].

There is one prime above p and its residue degree is1. The ideal norm formula
therefore gives v_p(Norm F_w)=v_lambda(F_w), with NO division by D. Other
finite valuations are nonnegative by integrality. Taking an archimedean Dth
root later is the only place where division by D occurs.

Finally jB=A and j(V-zeta^c)=-zeta^-c V^-1(V-zeta^c). Raising each factor
to p w_c removes the zeta factor, while A^d V^(-pd)=B^d. Since p is odd,

    jF_w=(-1)^d F_w.

Odd d gives an anti-real element; the proof consistently uses the full K/Q
norm rather than a mistakenly real-subfield norm. The parity also agrees
with the exact lambda valuation because t-1 is even.

## 3. BR2: conjugate-curve branches and quantitative estimates

Each factor in A*/B* is nonzero on the unit disk. The normalized logarithm
there gives a unique analytic pth root q_a with q_a(0)=1. At real z of either
sign, the numerator and denominator are conjugate, so |q_a(z)|=1. Differentiating
its logarithm gives 2r terms, each bounded by 1/(1-|z|); hence

    |q'_a(z)|<=2r/[p(1-|z|)],
    |q_a(1/X)-1|<=(2r/p)(-log(1-1/U))
                 <=2r/[p(U-1)], U=|X|.

These estimates are on the full real segment from0 to1/X. They do not
assume X positive or choose a real pth root independently at every embedding.

The ratio sigma_a V/q_a(1/X) is a unique pth root of unity; writing its
exponent as a*c_a defines the normalized label. Complex conjugation gives
q_-a=conj(q_a) and then c_-a=c_a. It would be wrong to put a minus sign on
the normalized label. Thus occupancies n_c are even and sum to D, without
forcing the active set to have one or two labels.

At embedding a, exactly the factors with root label c_a receive the small
bound, while all other factors have modulus<=2 and |sigma_a B(X)|<=(U+1)^r.
Writing W=sum n_c w_c and multiplying all D embeddings gives

    p^[p(d+(t-1)w_0)]
      <=(U+1)^(rdD) 2^(pdD) [r/(p(U-1))]^(pW).

For unit weights on any H covering all active labels, EVERY embedding has a
small factor. Its common bound is

    L_H=(U+1)^(rh) [2^h r/(p(U-1))]^p.

Taking the Dth root of the norm lower bound gives equation(8). Padding H with
unused labels is legitimate, including padding it with0. All coefficients
remain in ONE K-polynomial; there is no embedding-by-embedding change of
the auxiliary function. Conjugate curves, rather than automorphisms of one
fixed-coefficient curve, are the correct interpretation throughout.

## 4. BR3: coherent and two-label consequences

For U=2 the two possible Phi values lie strictly between1 and2^p, so they
cannot be the pth power of an integer Y>1. Thus U>=3 in the stated sector.

For a coherent label use h=1. Since r<=D/2 and 2r/p<1, every conjugate
has modulus strictly below (U+1)^(D/2)/(U-1)^p. Its logarithmic derivative
is D/[2(U+1)]-p/(U-1)<0 for U>=3, and its value at3 is1/2. This contradicts
the nonzero integral norm. No unproved phase-count theorem is needed.

For h=2, put v=U-1 and kappa=2+(t-1)epsilon. If v<=2D, the desired strict
upper bound follows already from U<=2p-1. If v>2D, r<=D/2 and 4r/p<2 yield

    p^(p*kappa/D) < 2^p (1+2/v)^D/v
                   < 2^p/(v-2D).

The second comparison follows from binom(D,j)<=D^j and a strict geometric
tail comparison, whose denominator is positive in this branch. Since p/D>1,
the lower term exceeds p^kappa. Rearrangement is precisely

    U<2p-1+2^p/p^[2+(t-1)epsilon].

For epsilon1, t>=3 allows the weaker p^4 denominator. The inequalities are
strict at the claimed endpoint, and neither the argument nor its conclusion
says that every actual solution has at most two labels.

## 5. BR4: BOTH residual centers, and the one-sided exact refinement

Suppose p divides X(X+1), and choose its unique center a0 in{0,-1}. The
ordinary integer s=v_p(X-a0) is finite. From Y=1 mod p, Y>1 and the binomial
valuation of Y^p-1, that value has p-valuation v_p(Y-1)+1>=2.

At0, Phi_p(X)-1=X(1+...+X^(p-2)) has valuation s. At-1, the identity
Phi_p(X)-1=X(X^D-1)/(X-1), with X and X-1 p-units, reduces the valuation
to that of X^2-1: the remaining geometric sum has D/2 terms and reduces to
D/2!=0 mod p. Thus again it is s. Consequently s>=2 and U>=p^2-1,
retaining either sign of X and no upper bound on s.

I independently expanded a single factor with Z=T-1:

    (T-zeta^a)/(T-zeta^-a)
      =1+(2a/Z)lambda+[a/Z+2a^2/Z^2]lambda^2 mod lambda^3.

The cross terms in the product turn the quadratic sum into
S1/Z+2S1^2/Z^2. Since p divides S1, the whole R(T)-1 is coefficientwise
in lambda^3 after expansion at either center. The local denominators have
unit constants there. Crucially the constants vanish EXACTLY:

    R(0)=zeta^(2S1)=1, R(-1)=zeta^S1=1.

Thus substitution of X-a0, of lambda valuation Ds, gives
v_lambda(R(X)-1)>=3+Ds. For u=V-1 with valuation t>=3, the term p u in
(1+u)^p-1 has uniquely least valuation D+t. The middle terms have D+i t
and the last term p t>D+t. Therefore

    t>=3+D(s-1)>=p+2.

For the sharper center0 statement, E=sum_S(zeta^a-zeta^-a) is nonzero:
its coefficient vector has constant0 and nonconstant entries -1,0,1, while
the sole rational relation of degree<=p-1 is a multiple of Phi_p. The direct
moment puts E in lambda^2, and anti-reality makes its valuation e odd, so
e>=3. If e>=D, membership in pO and the integral power basis would force
the constant coefficient -h_(p-1), and then each h_a-h_(p-1), to be0 mod p.
All h_a would be0, impossible. Hence e<=D-1=p-2.

At0 the exact derivative R'(0)=E. Higher Taylor coefficients have valuation
>=3. Their evaluated terms have valuation>=3+2Ds, strictly greater than
e+Ds, because e<=p-2 and s>=2. The linear term is the unique minimum:

    v_lambda(R(X)-1)=e+Ds, t=e+D(s-1).

No upper derivative order at-1 is inferred. The common lower bound there
is proved independently and is sufficient for the residual consequence.

For H covering all actual labels AND0, assume hr<p and 2^h<=ph. Then
hr<=D and C=2^h r/p<2^h/h<=p. With v=U-1>=p^2-2>2D, the common bound is

    |sigma_a F_H|<=C^p (U+1)^D/(U-1)^p
                  <p^p/(v-2D)<p^p.

Here v-2D>=p(p-2)>1. But the exact local norm lower bound is
p^[p(h+t-1)]>=p^[p(p+h+1)]>p^(pD), contrary to the product of all D upper
bounds. This proves the exact residual obstruction.

If h<=floor(log_2 p), its numerical side condition holds. A residual active
set of size<=2 including0 has hr<=2r<=D and is excluded. If neither of two
labels is0, adding0 gives h<=3; the same contradiction follows under3r<p.
Thus the remaining two-label alternative has neither0 and has3r>=p. This
is a necessary condition, not a realization or a complete residual exclusion.

## 6. BR5 and attempted overextensions

The accepted RS quotient has simple T poles at its p infinity points. At Q_b,
V=zeta^b q_1(1/T), and q'_1(0)=-E/p!=0. Thus V-zeta^b has exact order1,
every other root factor is a unit, and B has pole order r. This proves the
EXACT order p w_b-rd, including zero weights and nonpositive resulting orders.
Every conjugate of E is nonzero, so the same calculation works on the
conjugate curves with their normalized labels c_a.

The sum of these orders is p sum n_c w_c-rD sum w_c. It is positive for
some nonnegative integer weight vector exactly when max n_c>rD/p: a maximum
label alone suffices, and a weighted maximum proves necessity. Since
r-1<rD/p<r for0<r<p, occupancies all<=r-1 make every nonzero weighted
choice have negative aggregate order.

I tested the following possible false extensions explicitly against the proof:
V integral from its complex moduli; specialization nonzero from generic Kummer
independence; arithmetic integrality from a 1/p deck projection; division of
the p-norm valuation by D; c_-a=-c_a; residual depth s=1; equality in R(a0)
replaced by a congruence; an exact derivative upper bound transported to-1;
a universal two-label theorem; and a claim about all integral functions from
the weighted-root boundary. None is required or asserted in the scoped proof.
The all-label product also checks the order formula: F=(A-B)^p has the
predicted pole p(r-1), because E!=0 supplies the first degree drop.

The source attribution is classical Runge. The new model-specific proof is
explicit and does not invoke a general covering theorem without an actual
K-lift or an unread height/class-number theorem. The original primary read
limits are in the source ledger. No mathematical code, scan, CAS, table,
certificate replay or author script contributed to this audit.

## 7. Disposition

ALL60 rows close in the exact ordinary-integer, actual-lift domain. The
integrality/nonzero/local-order bridge is complete, and the residual and
small-label consequences follow with their stated strict endpoints. The
eight closed notes preserve domains rather than add a missing premise.
No unrestricted label bound, support bound independent of p, improved general
height, old linear-delta nonvanishing, all-generator theorem, prime bound,
annual classification, external validation or priority follows. Coordinator
promotion requires the other ENTIRE initially blind whole audit and full
reconciliation; this review alone does not change status.
