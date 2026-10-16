# A restricted exponent-pair exclusion

**candidate proof - unverified**, coordinator draft v0.1, 2026-10-16.

This concerns only B4(b). It is not a full classification, has not received either required independent audit, and makes no novelty claim. The year owner should check both mathematics and prior literature before extending it.

## Proposed partial result

For every nonsquare positive integer N and positive integer d, neither exponent pair (4d,3d) nor (3d,4d) admits a real witness r in B4(b).

## Reduction to (4,3)

If r were a witness for (4d,3d), the real number z=r^d would be a witness for (4,3). The two conditions are symmetric in the exponents. It therefore suffices to exclude (4,3).

Write s=sqrt(N), so s>=sqrt(2), and suppose

    r^4 = u-s,  r^3 = v-s,  with u,v rational.

The value r is nonzero, since s is irrational. Thus r=r^4/r^3 belongs to Q(s). Let r' be its quadratic conjugate. Conjugation gives

    r'^4-r^4 = 2s,  r'^3-r^3 = 2s.                 (1)

In particular r'>r and |r'|>|r|.

## Exclude nonnegative r

If r>0 and r'<1, the cubic difference in (1) is less than 1, contradicting 2s>1. If r'>=1, set h(t)=t^4-t^3. Equation (1) implies h(r')=h(r)>=0. Since h is negative on (0,1), this forces r>=1; but h is strictly increasing on [1,infinity), contradicting r'>r. The value r=0 was already excluded.

Hence r<0. If r' were nonpositive, r'>r would imply |r'|<|r|, another contradiction. Therefore

    U=r'>V=-r>0.

Equation (1) becomes

    U^4-V^4 = U^3+V^3 = 2s.                      (2)

## Rational trace and norm

Put D=U-V=r+r' and P=UV=-rr'. The quadratic trace and norm show D,P are rational; both are positive. Divide the equality U^4-V^4=U^3+V^3 by U+V>0 to obtain

    D(D^2+2P) = D^2+P,
    P(2D-1) = D^2(1-D).                          (3)

Because P,D>0, neither D=1/2 nor D=1 is possible. If D<1/2, the two sides of the second identity in (3) have opposite signs; if D>1, they again have opposite signs. Consequently

    1/2 < D < 1,
    P = D^2(1-D)/(2D-1).                         (4)

Set S=U+V. Then S^2=D^2+4P and U^3+V^3=S(D^2+P). Squaring the cubic identity in (2), using (4), yields

    4N = (D^2+4P)(D^2+P)^2,
    N = D^8(3-2D) / (4(2D-1)^3).                (5)

All denominators used so far are nonzero by (4).

## Denominator obstruction

Write D=p/q in lowest positive terms. Since 1/2<D<1, q>=3. Equation (5) becomes

    N = p^8(3q-2p) / (4q^6(2p-q)^3).             (6)

If an odd prime ell divides q, it divides neither p nor 3q-2p (the latter is -2p modulo ell). Thus the numerator of (6) is an ell-adic unit whereas its denominator is divisible by ell, contradicting N being an integer. Therefore q is a power of 2. As q>=3, q is divisible by 4 and p is odd. Now 3q-2p has 2-adic valuation exactly 1, whereas the denominator in (6) has valuation at least 2+6*v_2(q)>1. This again contradicts integrality. No witness exists.

## Review obligations

Check the use of the quadratic conjugation, the positive-witness case, trace/norm signs, the algebra from (3) to (5), and the denominator valuations. Independently attempt exact counterexamples. Determine whether this restricted exclusion already follows from published work. Even if accepted, all other opposite-parity exponent ratios remain outside this result; it is not a solution of B4(b).
