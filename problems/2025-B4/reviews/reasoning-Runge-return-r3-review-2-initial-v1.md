# OTHER initially blind ENTIRE WHOLE Runge R3 review R2

2026-10-18 UTC. Reviewer C, `/root/review_2017_coarsening_r1`.
This is an independent reconstruction of NEW BR1--BR5 and ALL60
obligations, not promotion. The submitted candidate remains unverified
until the coordinator reconciles TWO OTHER complete whole reviews.

The exact target is `notes/reasoning-Runge-return-r3-candidate-v1.md`,
23038 bytes, SHA256
`5ccc04e72574187d1959efff22852dbbc5cca41e701afbaeebc9f97adbdf64a0`.
Its ten-file constructor freeze is 8661 bytes, SHA256
`6a010ee19e90b4a07373f64dd375e9df7e6c8d4aee9ec7af001d8410e5bb461a`.
I read the ENTIRE main, ALL60 obligations, failures, both source records,
worklog, administrative freezer, baseline, validation and freeze. I did
not read any corresponding NEW A R3 review, findings, files, hashes or
metadata before this ENTIRE initial checkpoint.

## 1. Verdict, exact domain and independence

I found no substantive defect in the explicitly specified integer-weight
BR1--BR5 argument. All sixty obligations are reconstructed in the separate
ledger. One closed scope note, R3R2-N1, is that the first display introducing
weights says only `w_c>=0`; the existing obligation R3O-14 expressly says
nonnegative INTEGER weights, and section2 defines a polynomial of degree
`d=sum w_c`. The certified domain is `w_c in Z_{>=0}`, `d>0`, throughout.
Repeating “integer” in BR1 would make the first statement self-contained.
No extension to real exponents is certified. This is not a missing
mathematical premise elsewhere in the frozen packet.

The annual problem is 2025 B4(b), all integer solutions of
`1+X+...+X^n=Y^q`, `n,q>=2`. Here the application is ONLY

    Phi_p(X)=Y^p, p>=37 prime, X,Y ordinary integers, |X|>=2,

with official degree `n=p-1`. Both signs of X remain. This does not settle
the full prime-diagonal problem, unrestricted primes, generalized e1,
off-diagonal exponents, or the annual question. Nothing below supplies a
uniform bound on support or on the number of actual phases. No actual
solution or surviving signature is constructed.

B constructed NEW R3 and is excluded as reviewer. Root's earlier RS
quotient contribution is not new R3 construction. My OLD R6/RG/R9/FS
authorship and older RS/UW review roles are disclosed: this review is an
independent audit of the NEW functions, valuations, norm estimates and
sector consequences, not an independent recertification of my own old
accepted inputs. The exact accepted RS body/authority and R6 section5/
authority are the operative imports. RG fixed-p finiteness is context.
I do not replace a new inference by a prior conclusion.

## 2. Actual arithmetic interface and nonzero values

Use direct indices `sigma_a(zeta)=zeta^a`, `j=sigma_-1`, `D=p-1`,
`lambda=1-zeta`, `K=Q(zeta)`, `O=Z[zeta]`. Fix the ACTUAL eligible
`theta=sum n_a sigma_a` from accepted RS/UW, with coefficients in
`{0,1,2}`, `theta+jtheta=2N`, augmentation D, direct moment zero and
the separately specified nonzero inverse M1. These two moments are not
interchanged. For `S={a:n_a=2}`, accepted RS gives

    3<=r=|S|<=D/2, S intersect -S empty, sum_S a=0 mod p.

Set `A(T)=prod_S(T-zeta^a)`, `B=jA`, `R=A/B`, `U=|X|`.
The accepted actual Jacobi input supplies an algebraic integer beta,
`beta^p=Phi_p(X)R(X)`, `beta=1 mod lambda^2`, all conjugate absolute
values Y, and characteristic ideals

    (X-zeta)=mathfrakA^p, Norm(mathfrakA)=Y>1,
    (beta)=mathfrakA^theta.

Their conjugates are pairwise coprime and supported at completely split
primes `ell=1 mod p`. Thus the product of all conjugate ideals is `(Y)`.
In particular, for `V=beta/Y`,

    (V)=mathfrakA^(theta-N), V^p=R(X), V*jV=1.

The first equation does not choose a principal pth root of an ideal.
The coefficient vector of `theta-N` is nonzero and contains a positive
coefficient. At a prime of the corresponding conjugate of mathfrakA,
coprimality prevents cancellation with another conjugate ideal. Its
valuation in `(V)` is positive. Consequently `(V)` is not the unit
ideal, V is not any root of unity, and every product of factors
`V-zeta^c` is nonzero. This argument survives specialization because it
uses the actual characteristic ideals, rather than generic independence
in a function field. V may have other negative valuations; unitary
complex values do not make it integral.

The identity `beta*jbeta=Y^2` follows already at the chosen complex
embedding and therefore in K. Modulo p, the accepted `p not dividing
X-1` gives `Phi_p(X)=(X-1)^D=1`; Fermat gives `Y^p=Y`, hence `Y=1
mod p`. Y is positive, since p is odd and `Phi_p(X)>1` for either sign
in this domain. Thus `V=1 mod lambda^2`. As V is not 1,
`t=v_lambda(V-1)` is finite and at least2. Conjugation acts on a leading
lambda term by `(-1)^t` modulo lambda, whereas

    j(V-1)/(V-1)=-1/V=-1 mod lambda.

Since p is odd, t is odd and at least3. For c nonzero the exact valuation
of `1-zeta^c` is1, so

    v_lambda(V-zeta^c)=1 (c!=0), v_lambda(V-1)=t.

Also B(X) is a lambda-unit. These statements use finite-place
normalization `v_lambda(lambda)=1`, `v_lambda(p)=D`.

## 3. BR1: the whole arithmetic integrality argument

For nonnegative integer weights of positive sum d, put

    Q(Z)=prod_c(Z-zeta^c)^(w_c) in O[Z],
    F_w=B(X)^d Q(V)^p.

I checked the entire polynomial, not just its leading term. The accepted
arithmetic basis elements `b_i=B(T)V^i`, `1<=i<p`, satisfy the monic
equation `b_i^p=A^i B^(p-i)` over O[T], hence are integral over O[T].
For a term of degree `j=kp+i` of `Q(Z)^p`, with `0<=i<p`, the exact
identities are

    B^d V^j=A^k B^(d-k)                 if i=0,
    B^d V^j=A^k B^(d-k-1)b_i           if i>0.

Because `j<=pd`, the first case has `k<=d` and the second `k<=d-1`.
There is no negative exponent, including the endpoint `j=pd`, which
is exactly `A^d`. Every term is integral over O[T]; a sum is integral.
Specializing T to the ordinary integer X and the actual V gives a
value in K integral over O, hence in its integrally closed ring O.
This handles every finite prime, including primes above Y and p.
No character projection by `1/p`, inverse B or omitted S-prime has
entered the coefficient ring. This proof also handles zero weights,
large d and `d>=p` without an extra degree restriction.

The value is nonzero by section2. Its exact local valuation is
`p[d+(t-1)w_0]`. There is one prime above p of residue degree1, so the
p-valuation of the rational norm is this exact integer, NOT this integer
divided by D. Since the norm is a nonzero ordinary integer,

    |Norm F_w| >= p^[p(d+(t-1)w_0)].

Finally `jB=A` and
`j(V-zeta^c)=-zeta^-c V^-1(V-zeta^c)`. Raising to the indicated
multiples of p eliminates roots of unity, and `V^p=A/B` cancels the
remaining factor. Therefore `jF_w=(-1)^d F_w`. Odd d is anti-real;
the proof correctly retains all D embeddings and an absolute norm.

## 4. BR2: actual conjugate labels, both signs and all embeddings

In the disk `|z|<1`, all factors `1-zeta^(ab)z` are nonzero. Their
normalized logarithms define the unique analytic pth root q_a with
constant1 of `sigma_a A*/sigma_a B*`. For real z, numerator and
denominator are conjugates; `|q_a(z)|=1`. Logarithmic differentiation
gives `|q'_a(z)|<=2r/[p(1-|z|)]` along the real segment. Integrating
to `1/X`, positive or negative, gives

    |q_a(1/X)-1| <= (2r/p)(-log(1-1/U))
                    <=2r/[p(U-1)].

The actual `sigma_a V` has the same pth power as this root. Its quotient
is exactly one pth root of unity, uniquely written `zeta^(a c_a)`.
The factor a is essential: conjugating the identity changes both a
and its exponent sign, and gives `c_-a=c_a`. Thus every multiplicity
`n_c=#{a:c_a=c}` is even and their sum is D. This is not a free choice
of a phase vector or an automorphism of one fixed-coefficient curve;
the source curves are conjugated together with their coefficients.

At embedding a, the factor indexed by c_a has the small bound just
derived; every other factor is at most2. Also `|sigma_a B(X)|<=
(U+1)^r`. Multiplying the resulting bounds over all D embeddings gives,
with `W=sum_c n_c w_c`, exactly

    p^[p(d+(t-1)w_0)]
      <=(U+1)^(rdD) 2^(pdD) [r/(p(U-1))]^(pW).

The factor of2 in the small bound cancels the corresponding removed
factor of2 in the other-factor product, which explains the displayed
constant. There is no independence assumption on labels. If H contains
every active label, its indicator weights give at EVERY embedding

    |sigma_a F_H| <=(U+1)^(rh)[2^h r/(p(U-1))]^p.

Taking the Dth root of the norm lower bound yields the candidate's
inequality(8). H may contain unused labels: each embedding still has
its one small factor. This padding is used legitimately later.

## 5. BR3: exact small-label consequences

The two possibilities U=2 are excluded just within this diagonal sector:
`Phi_p(2)=2^p-1` and `Phi_p(-2)=(2^p+1)/3` lie strictly between1 and
`2^p`. No positive integer Y>1 has its pth power there. Hence U>=3.

For a single active label, choose H of size1. Since `2r/p<1` and
`r<=D/2`, each conjugate F_H has modulus strictly smaller than

    (U+1)^(D/2)/(U-1)^p <=4^(D/2)/2^p=1/2.

The function decreases for U>=3 because its logarithmic derivative
is `D/[2(U+1)]-p/(U-1)<0`. The nonzero algebraic integer norm cannot
have all these factors of modulus below1. This excludes a coherent
normalized branch for the actual theta and actual lift.

For at most two labels, take |H|=2 and write `v=U-1`,
`kappa=2+(t-1)epsilon`, `epsilon=1_(0 in H)`. If `v<=2D`, the claimed
strict bound already follows from `U<=2p-1`. If `v>2D`, then `4r/p<2`
and `2r<=D` give

    p^(p*kappa/D) <2^p(1+2/v)^D/v <2^p/(v-2D).

The last inequality follows by bounding each coefficient of the finite
binomial sum by `D^j` and comparing with the infinite geometric sum
of ratio `2D/v<1`. The omitted positive tail ensures strictness.
Since `p*kappa/D>kappa`, rearrangement gives precisely

    U<2p-1+2^p/p^kappa.

For a zero label, t>=3 makes the denominator at least p^4; otherwise
the uniform two-label denominator is p^2. No assertion that arbitrary
actual signatures have at most two labels was made or used.

## 6. BR4: residual ordinary-integer information

Suppose `p|X(X+1)`. There is exactly one center `a0=0,-1` and finite
`s=v_p(X-a0)`. The nonzero integer Y-1 is divisible by p, so elementary
LTE gives `v_p(Y^p-1)=v_p(Y-1)+1>=2`. At center0,
`Phi_p(X)-1=X(1+...+X^(p-2))` has valuation s. At center-1,

    Phi_p(X)-1=X(X^D-1)/(X-1)

has valuation s too: X/(X-1) is a unit and factoring through
`(X^2)^(D/2)-1` leaves quotient congruent to the p-unit D/2. Thus
s>=2, and for both signs `U>=p^s-1>=p^2-1`.

I independently expanded each factor in lambda. With `Z=T-1`,
`S1=sum_S a` using representatives1 through p-1, one obtains

    R(T)=1+(2S1/Z)lambda
           +(S1/Z+2S1^2/Z^2)lambda^2 mod lambda^3.

For example, one factor contributes `2a/Z` and `a/Z+2a^2/Z^2`;
the cross terms supply `4 sum_(a<b)ab/Z^2`, yielding the stated square
of S1. As p divides S1 and `v_lambda(p)=D>=36`, both displayed error
coefficients vanish modulo lambda^3. At either center all denominators
have unit constant term, so this holds coefficientwise in the local
Taylor ring. In addition the constant terms are EXACTLY
`R(0)=zeta^(2S1)=1`, `R(-1)=zeta^S1=1`. This exact equality, not a
mere congruence, removes the constant term and gives after convergent
substitution

    v_lambda(R(X)-1)>=3+Ds.

For `u=V-1` of valuation t>=3, the unique smallest term of
`(1+u)^p-1` is pu, of valuation D+t. The middle terms have D+it,
and the last has pt; both are strictly larger. Hence

    t>=3+D(s-1)>=p+2.

At center0, set `E=sum_S(zeta^a-zeta^-a)`. Its coefficient vector
has entries -1,0,1, constant0 and nonzero support. The sole rational
relation of degree<=D is a multiple of Phi_p, so E is nonzero.
The direct moment zero makes its linear lambda coefficient vanish
mod p; anti-reality makes its finite valuation odd. Thus e>=3.
If e>=D, then E belongs to pO. Rewriting zeta^D in the integral basis
`1,...,zeta^(D-1)` first forces h_D=0 mod p from the constant term,
then forces every other h_a=0 mod p. This contradicts the nonzero
-1/0/1 vector. Therefore `3<=e<=p-2`, e odd.

The exact derivative `R'(0)=E` has valuation e. Every higher Taylor
coefficient has valuation at least3, so when `v_lambda(X)=Ds`, the
linear term has valuation e+Ds, strictly below `3+2Ds`. It is the
unique minimum. This gives `t=e+D(s-1)` at center0. No corresponding
upper bound for the derivative at center-1 is needed or claimed.

Now choose H containing all actual labels AND zero, with size h. If
`hr<p` and `2^h<=ph`, integrality gives `hr<=D`, and
`C=2^h r/p<2^h/h<=p`. With `v=U-1>=p^2-2>2D`, the common bound above
becomes at every embedding

    |sigma_a F_H| <=C^p(v+2)^D/v^p
                   <p^p/(v-2D)<p^p.

Here `v-2D>=p(p-2)>1`; the same finite geometric comparison is valid.
The norm upper bound is therefore `<p^(pD)`. However the exact local
valuation, because zero belongs to H, gives

    |Norm F_H|>=p^[p(h+t-1)]
                  >=p^[p(p+h+1)]>p^(pD),

a contradiction. Thus the residual necessary product restriction is
correct. For `h<=floor(log_2 p)`, its numerical condition is automatic.
At most two labels including zero have `hr<=2r<=D` and are excluded.
If zero is absent, adding it costs at most h=3; the same proof excludes
`3r<p`. Together with the coherent-label exclusion, any surviving
residual at-most-two-label solution must have exactly two nonzero
labels and `3r>=p`. This is a necessary condition, not a construction
or elimination of the surviving sector.

## 7. BR5, operative source checks and remaining gap

On the accepted quotient, infinity consists of p unramified K-rational
points Q_b; T has simple pole. At Q_b,
`V=zeta^b q_1(1/T)` and `q'_1(0)=-E/p!=0`. Thus `V-zeta^b` has exact
order1, while every other root factor is a unit. B has pole order r.
For the integer weights this proves `ord_Qb F_w=p w_b-rd`, including
zero weights and negative resulting orders. On conjugate curves E
remains nonzero; pulling back the actual labels gives aggregate order

    p sum_c n_c w_c-rD sum_c w_c.

A positive aggregate exists in this family exactly when some
`n_c>rD/p`: concentrate unit weight at a maximizer for sufficiency,
and use the weighted maximum for necessity. Because `0<r<p`,
`r-1<rD/p<r`. Thus `n_c<=r-1` for all c makes every nonzero weighted
aggregate negative. This does not prohibit general Riemann--Roch
functions, other finite-prime uses, or actual points.

I checked primary Levin2008 Theorems1.2--1.3 and the ENTIRE operative
section2, including the definitions, Lemma2.1 and the full proof of
Theorem2.1. Its integral-scaling/field/place hypotheses are not silently
waived. The new proof supplies explicit integral functions and proves
their nonzero values itself; it does not apply a cover theorem without
an actual lift or import a numerical height bound. I also read the
ENTIRE operative Jacobi section2.2 in the author-posted diagonal chapter,
including its matched order-p character, sign/ideal formula, Lemma2 and
lambda^2 normalization. R6 is the separately accepted implementation of
that interface. No later class-number or claimed height theorem is used.
Fresh Bennett--Levin reading is context; it is not a new premise.
The separate source record states exact read ranges and unread limits.

The proposed actual-sector exclusions and finite reductions therefore
pass this whole review. They remain classical product-formula/Runge
arguments with explicit model-specific calculations, with priority
unestablished. The missing general arithmetic bridge is unchanged:
there is no uniform bound on r or the actual normalized label count,
no forced label multiplicity beyond pairing, no unrestricted positive
aggregate, and no uniform prime bound. No old linear-generator or
all-generator exclusion follows. Only the coordinator may promote the
stated scope after reconciling the other complete independent review.
