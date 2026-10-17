# Repeated small roots: an Euler reflection identity and a finite collision depth

2026-10-17 UTC. **Candidate proof - unverified.** Constructor:
review_2021_reasoning_j15_r2. Requested gpt-6.1-sol/max; independent
effective readback unavailable. Two fresh independent nonconstructor
whole audits are required. No full J15 mask, repeated-root branch,
nonunit branch, degree20 solution, annual classification or novelty is
claimed. No mathematical program, enumeration, CAS or digit tree was
used. The finite symbolic alternatives below are the proof's actual
rational witness options, not a search for higher masks.

This packet is independent of the earlier unreviewed return and mirror
packets. Their bytes are preserved. Some exact top-derivative algebra is
rederived here, with explicit error bounds, rather than imported as an
accepted theorem.

## Accepted inputs and precise proposed conclusions

Use the accepted J15 multiplicity-two normalization and sole-H3
conclusion D3:

    f=X^20-20X^19+sum_(j=2)^18 binom(20,j)a_j X^(20-j),
    a_j in Z_(19), f(0)=f'(0)=f(1)=0,
    J=max{j:v(a_j)=0}=15, ord_0 f=2;
    H3(f)(1)=0, H2(f)(1)!=0, H4(f)(1)!=0.

Here v=v_19 with v(19)=1. H_k is the Hasse derivative. The rational
root1 is simple. There is a rational simple small root r, v(r)=nu>=1,
sharing H2,H4. The two other small slots have valuation nu and
scaled residue2R, where R=r/19^nu mod19 is nonzero. Fourteen other
slots have valuation1/14. Accepted T1 requires at least four distinct
rational witness values.

In this packet assume the two2R slots coincide at one value d, a
double root. T1 then forces d to be rational: the fractional slots
cannot be rational, and otherwise only0,1,r could be rational witnesses.
Thus the rational root set is exactly

    {0,1,r,d},       d/r=2 mod19.

Set delta=d-2r. Its valuation k is greater than nu if delta!=0;
write k=infinity when delta=0.

**Proposed RC1, without an extra even-derivative ladder.**
If delta!=0 then

    v(delta)>=4nu.

More generally, if the even Taylor part at r starts at degree2m,
3<=m<=9, write it E(T)=T^(2m) A(T^2). Then an exact Euler identity
below determines k from A'(r^2), including cases in which the
least Taylor coefficient weights are tied.

**Proposed RC2, with the explicit additional hypothesis**

    H6(r)=H8(r)=H10(r)=H12(r)=H14(r)=0.              (L)

If f satisfies all the rational witness conditions, then

    nu=1, delta!=0, and v(delta) is either15 or16.   (C)

Moreover H18 cannot use the center1. In particular the exact mirrored
case d=2r is impossible under(L). This is a restricted necessary
condition. No existence, complete mask exclusion or general
repeated-root exclusion is asserted.

**Proposed RC3.** Under the same hypotheses as RC2, both0 and d must
be sole RATIONAL common-root values of different derivative orders
belonging to

    {7,9,11,13,15,16,17,18}.

In particular at least one of a2,a3,a4,a5,a7,a9,a11,a13 is exactly
zero. This concerns rational supports, not an unproved assertion
about the complete derivative gcd over an algebraic closure.

The only proof inputs are accepted D1/D3, the normalization and T1.
The all-roots-rational CLO theorem is not an input.

## 1. Reflection at a simple small witness

Accepted D1 gives

    f=(X-d)^2 U, U=X^2(X-r)B, B=(X-1)g,

where g is local monic Eisenstein of degree14. Here d is rational as
just proved, so ordinary rational division is available, but no such
division is used to justify the general accepted D1 theorem.

Write B=sum b_i X^i. D1 says v(b0)=1, v(b_i)>=1 for1<=i<=13,
b14=-1 mod19 and b15=1. Consequently

    v(B(2r))=1,
    B'(2r)/B(2r) is integral.

The constant b0 uniquely dominates B(2r). Every differentiated term
is still divisible by19: the degree14,15 terms have respectively
valuation at least13nu,14nu, and the others have an explicit19.
In particular

    U(2r)=4r^3 B(2r), v(U(2r))=3nu+1,
    eta:=U'(2r)/U(2r)=2/r+B'(2r)/B(2r),
    v(eta)=-nu.                                     (1)

Let h_e=H_e(f)(r) and E(T)=[f(r+T)+f(r-T)]/2.
Since h0=h2=h4=0,

    E(T)=sum_(e even,6<=e<=20) h_e T^e,
    h20=1, h_e in19 Z19 for e<=18.                  (2)

The divisibility follows directly by Hasse differentiation of the
binomial normalization at integral r; binom(20,e) has valuation1
for2<=e<=18.

Both0 and d are double roots, but2r need not be a root. Exact
evaluation at2r gives

    E(r)=delta^2 U(2r)/2,
    E'(r)=delta^2 U'(2r)/2-delta U(2r).              (3)

The first identity uses f(0)=0, and the second uses f'(0)=0, with the
minus sign in differentiating f(r-T). They do not divide by delta.

If E=T^(2m)A(T^2), subtract (2m/r) times the first equality from
the second:

    2r^(2m+1) A'(r^2)
      =-delta U(2r) [1+delta(m/r-eta/2)].            (4)

The bracket is a unit because k>nu. Therefore delta=0 implies
A'(r^2)=0, and if delta!=0 then

    k=(2m-2)nu-1+v(A'(r^2)),                        (5)
    v(A(r^2))=2k+(3-2m)nu+1.                       (6)

When delta=0, equation(3) additionally gives A(r^2)=0.
Conversely (4) shows A'(r^2)=0 forces delta=0 in this setting.

For m=3, A'=h8+2h10 r^2+...+7r^12 is divisible by19.
Indeed every nonleading coefficient has that factor, and the last
term has valuation12nu>=1. Formula(5) proves k>=4nu, RC1.
More generally, for3<=m<=8 it proves k>=(2m-2)nu.
For m=9 the monic A is linear, A'=1, so k=16nu-1 if delta!=0;
delta=0 is then impossible. These are exact necessary valuations,
not an inference from finitely many lifts.

## 2. The longer ladder and its uniform error

Assume(L). Then

    E(T)=T^16(h16+h18 T^2+T^4).

Equation(4) and (3) yield, with e0:=h16+h18 r^2+r^4,

    2r^17(h18+2r^2)
      =-delta U(2r)[1+delta(8/r-eta/2)],             (7)
    e0=delta^2 U(2r)/(2r^16).                       (8)

For delta!=0 these imply

    k=14nu-1+v(h18+2r^2)>=14nu,
    v(e0)=2k-13nu+1>=15nu+1.                       (9)

For delta=0 they instead give h18=-2r^2, h16=r^4 and e0=0.
We use the same lower bound on v(e0) in that case.

The normalized TOP derivatives, with their exact signs, are

    D2=H18/190=X^2-2X+a2,
    D3=H17/1140=X^3-3X^2+3a2 X+a3,
    D4=H16/4845=X^4-4X^3+6a2 X^2+4a3 X+a4.          (10)

In particular the D4 linear coefficient has the plus sign.
Set c=2/51, since190/4845=2/51. Throughout

    h18=190 D2(r),
    h16=-h18 r^2-r^4+e0,
    a4=h16/4845-r^4+4r^3-6a2 r^2-4a3 r.            (11)

The error e0 is much smaller than every leading term used below.
This is the required quantified replacement for silently setting
d=2r.

## 3. H18 at the center is impossible

Suppose H18 uses1. Then a2=1 exactly and

    h18=190(r-1)^2, v(h18)=1.
    v(h16)=2nu+1, v(D4(r))=2nu.

The latter follows from(11), since2nu+1<4nu and e0 has valuation
at least15nu+1. Formula(11) also makes a4 nonunit.

If a3 is a unit, D3 has no root in19Z19. H17 must use1, forcing
a3=-1 exactly. On19Z19, D4(x)-D4(y) is a unit times x-y.
Its value at r has valuation2nu>nu, so neither0 nor d can be a
zero; r is not a zero either. But D4(1)=a4-1 is nonzero.
There is no H16 rational witness. Thus a3 is nonunit.

Now H17 cannot use1 because D3(1)=1+a3 is a unit.
Let its witness be zeta in{0,r,d}, and write lambda=zeta/r mod19,
so lambda is0,1 or2. Its exact equation is

    a3=-zeta^3+3zeta^2-3zeta.                       (12)

H16 cannot use1 because D4(1)=3+4a3+a4 is a unit, and cannot
use r because h16!=0. Write its witness xi=0 or d and
mu=xi/r mod19, equal to0 or2. Divide D4(xi) by r^2 and reduce
modulo19. Equation(11), c=2/51=6 mod19 and(12) give

    mu=0: 12(lambda-1)=0,
    mu=2: 12(1-lambda)=0.

Hence lambda=1, so the actual H17 witness is r and

    a3=-r^3+3r^2-3r.                               (13)

Let Q0=D4(0)/r^2, and approximate D4(d)/r^2 by
Q2=D4(2r)/r^2. From(11),(13), their exact main terms are

    Q0=304/51+(4/51-8)r
         +(3-2/51-1/4845)r^2 + error,
    Q2=304/51+(4/51-16)r
         +(11-2/51-1/4845)r^2 + error.              (14)

The e0 error after division has valuation at least13nu.
The replacement d by2r in the integral D4 changes its value by
valuation at least k, and after division by r^2 by at least12nu.
Thus every error in(14) has valuation at least12nu. This holds
also for delta=0 with the corresponding replacement error zero.

If nu>=2, the constant304/51 has valuation1, and all other terms
have valuation at least2: the possible denominator4845 contributes
only-1, leaving2nu-1>=3. Neither Q0 nor Q2 can vanish.

If nu=1, write r=19R with R a19-adic unit and divide(14) by19.
For mu=0 or2, respectively, a zero would require

    10+4R-12R^2=0 or10-4R-12R^2=0 mod19.

After division by2 the discriminant is124=10 mod19.
The nonzero squares modulo19 are
{1,4,9,16,6,17,11,7,5};10 is not among them.
Again neither root exists. Thus H18 cannot use1, for ANY nu>=1.

## 4. Every valuation nu>=2 is impossible

H18 must use a rational noncenter z in{0,r,d}. Therefore

    a2=2z-z^2, a2/r=kappa mod19,
    kappa in{0,2,4}.                               (15)

Assume nu>=2. If z=r then h18=0 and h16=-r^4+e0 is nonzero.
If z=0 or d, then v(D2(r))=nu, v(h18)=nu+1, and
v(h16)=3nu+1<4nu. Thus h16 is always nonzero, and
v(D4(r))>=3nu. Formula(11) makes a4 nonunit.

If a3 is a unit, H17 can only use1, giving a3=2 mod19.
The integral D4 is injective on19Z19, with a unit linear
difference. Since D4(r) has valuation greater than nu, neither0
nor d is a zero; r is not a zero. The center is not a zero either,
since D4(1)=-3+4a3=5 mod19. This contradiction makes a3 nonunit.

H17 must therefore use zeta in{0,r,d}; let lambda=zeta/r mod19,
in{0,1,2}. Its equation gives

    a3/r^2=3lambda(lambda-kappa) mod19.

H16 cannot use1 or r, so its witness xi is0 or d; write mu=0 or2.
Divide D4(xi)=0 by r^3. In(11) the term-r^4/4845 has valuation
4nu-1>3nu, and e0/4845 has larger valuation too. Reduction gives

    L=4(1-mu^3)+6kappa(mu^2-1)
        +12lambda(lambda-kappa)(mu-1)
        -(2/51)(kappa-2)=0 mod19.                  (16)

The possible d-to2r replacement errors have valuation at least
k-3nu>=11nu after this division. For mu=0, (16) simplifies to

    L=16-12lambda^2+12kappa(lambda-1).

For mu=2 it is the negative of this expression.
If lambda=1, L=4 is nonzero. If lambda=0, a zero would require
kappa=4/3=14 mod19; if lambda=2, it would require
kappa=8/3=9 mod19. Neither belongs to{0,2,4}.
No witness option remains. Consequently nu=1.

This argument uses only the three possible rational root residues;
there is no enumeration of full derivative masks or higher digits.

## 5. Depth at least17, including exact mirroring, is impossible

Now nu=1. By(15), v(h18)>=2; if delta!=0, (9) gives k>=15.
We exclude k>=17 and also delta=0 in the same argument.
For delta=0 use the convention that all delta and e0 errors below
are zero.

Put h=96/95 and epsilon=h18+2r^2. From(7)--(9),

    v(epsilon)>=4, v(e0)>=22,
    a2=2r-h r^2+rho2, v(rho2)>=3,
    h16=r^4+rho16, v(rho16)>=6.                   (17)

For finite k>=17, v(epsilon)=k-13, v(e0)=2k-12;
for delta=0, epsilon=e0=0. In particular a2,a4 are nonunit,
h16 is nonzero of valuation4, and D4(r) has valuation3.

If a3 is a unit, H17 must use1, forcing a3=2 mod19.
D4 is injective on19Z19 and its value at r has valuation3>1.
It has none of0,r,d as a zero, while D4(1)=5 mod19.
Thus a3 is nonunit.

Consequently H17 uses zeta in{0,r,d}, and H16 uses xi=0 or d.
Replace zeta by lambda*r with lambda in{0,1,2}, and xi by
mu*r with mu in{0,2}. These replacements have error of valuation
at least17, before any divisions. The H17 equation and(17) give

    a3=3lambda(lambda-2)r^2
         +lambda(3h-lambda^2)r^3 + error,
    v(error)>=4.                                  (18)

Eliminating a4 by(11), inserting(17),(18), and dividing D4(xi)
by r^3 gives

    C(lambda,mu)+r A(lambda,mu)=0 mod19^2,           (19)

where the EXACT rational main terms are

    C=4(1-mu^3)+12(mu^2-1)
         +12lambda(lambda-2)(mu-1),
    A=mu^4-1+1/4845-6h(mu^2-1)
         +4lambda(3h-lambda^2)(mu-1).               (20)

To check the modulus in(19): the a2 error contributes valuation
at least3+2-3=2; the a3 error at least4+1-3=2;
the h16/4845 error at least6-1-3=2.
The zeta/xi replacements have still higher valuation.
Thus the error really is divisible by19^2.

H18 cannot use r, since h18=-2r^2+epsilon has valuation2.
It uses0 or d. In the first case its equation and(17) imply

    r=95/48 mod19^3;

in the second, comparison with D2(2r) implies

    r=95/142 mod19^3.                              (21)

Indeed 2r-h r^2=-h r(r-95/48), with h*r a unit;
the other expression is (4-h)r(r-95/142), again with a unit
linear factor. The D2(d)-D2(2r) error has valuation at least17.
These congruences imply the scaled residue R=r/19 is10 or9.

For complete verification of the small proof certificate, reducing
(20) gives the following pairs (C,19A) modulo19:

    mu=0: lambda0 (11,17), lambda1 (4,7), lambda2 (11,16);
    mu=2: lambda0 (8,16), lambda1 (15,7), lambda2 (8,17).

All six second entries are nonzero. Equation(19) modulo19 is
C+R*(19A)=0. The required R values are respectively

    mu=0: 15,13,10;     mu=2: 9,6,4.

Comparing with(21) leaves only two cases.

For mu=0,lambda=2, one has

    C=-8, A=62068/4845,
    C+rA=A*(r-9690/15517).

But r is95/48 modulo19^3, whereas

    95/48-9690/15517
      =1008995/(48*15517), v=2.

For mu=2,lambda=0, one has

    C=8, A=-15452/4845,
    C+rA=A*(r-9690/3863),

and r is95/142 modulo19^3, whereas

    95/142-9690/3863
      =-1008995/(142*3863), v=2.

Both denominators are19-adic units, and
1008995=19^2*2795 with2795=2 mod19.
In each case v(A)=-1, so v(C+rA)=1.
This contradicts the required divisibility by19^2 in(19).

Thus finite k>=17 and exact delta=0 are both impossible.
Together with nu=1 and k>=15, this proves proposed RC2:
k is15 or16. The proof does not decide either remaining value.

## 6. Two indispensable higher rational witnesses

There are exactly four rational roots0,1,r,d. T1 implies that each
is indispensable in any rational cover: if none of the derivatives
had one of these values as its sole rational common-root value,
the other three would cover all derivatives.

Accepted D3 and its explicit low reductions give the rational
supports H2:{r}, H3:{1}, H4:{r}. H1 has{0,d}, since these roots
are double while1 and r are simple. H19 has{1}.
For H5, the ordinary coefficient c5 has valuation1 and uniquely
dominates H5 at every small rational root: terms of degree6..18
gain a positive root power, and the degree19,20 differentiated
terms have an extra binomial factor19. Thus H5 has only{1}.

Under(L), r belongs to the rational support of each of
H6,H8,H10,H12,H14. None of these can make0 or d indispensable.
Therefore both0 and d must be sole rational common-root values
at different orders in{7,9,11,13,15,16,17,18}.

At the order for0, H_k(f)(0)=binom(20,20-k)a_(20-k)=0 exactly.
Characteristic zero makes this equivalent to a_(20-k)=0.
This proves RC3 and the stated list of eight possible zero
coefficients. It is not a claim that one of these equations alone
forces the rest of the witness system.

## Source and unresolved-boundary check

The accepted project proofs supply D1/D3 and T1, with their
published attribution. CLO Proposition19 assumes all roots
rational, or its stated unramified extension; that hypothesis
does not hold here. The original August2011 erratum adds5 to
the bad base-degree4 primes, so no two-prime exclusion is inferred.

A bounded new source check read Marashdeh's arXiv2608.14726
Theorems A--E and the precise scenario boundary in the introduction,
rather than importing a classification. The one-nonzero-recycled-root
descent determinant and the two-element coefficient-support theorem
do not establish the present four-rational-witness statement.
The paper separately flags all-real-root interpolation results;
our unused roots are not assumed real. No external theorem from
that preprint is a proof input, and no exhaustive novelty claim
follows from the search.

RC1 treats general finite repeated-root displacement. RC2 also
requires the five explicit extra even-derivative equations(L).
It leaves asymmetric repeated roots at depths15,16, all cases
without(L), distinct2R roots, other low-center patterns,
multiple centers, lower J and all full masks unresolved.
The old low-order family is excluded only if one tries to impose
ALL rational witness equations on it; its stated partial
properties remain valid. No Q19-only value is chosen as a
rational witness, and no local factor is made rational without
actual rational division.


