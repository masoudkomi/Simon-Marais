# Kasami factor fields and Frobenius orbit products

2026-10-16 UTC. **Candidate proof - unverified, conditional on an
attributed decomposition theorem.** It is not a full solution of B4(b),
and its deductions require two fresh independent reviews before any
project promotion. Only part (b) is discussed. No novelty is claimed.

## Precisely stated source premise

Let k>=2, q=2^k and t=q²-q+1. Write

    phi_t(X,Y,Z)=(X^t+Y^t+Z^t+(X+Y+Z)^t)
                  /((X+Y)(X+Z)(Y+Z)) over F2.

The Janwa--Wilson decomposition is reproduced in full in Section 3,
equation (5), of Delgado--Janwa,
[arXiv:1612.05997v1](https://arxiv.org/pdf/1612.05997v1), 2016-12-18:

    phi_t(X,Y,1) = product_(alpha in F_q minus F2) P_alpha(X,Y),

where the factors are absolutely irreducible of degree q+1, lie in
F_q[X,Y], and have specialization

    P_alpha(X,0)=(X+alpha)^(q+1).                           (K1)

The displayed equality is an equality of normalized polynomials, not
only of zero sets up to unspecified scalars. Their equation (6) groups
conjugates into F2 polynomials. The original Janwa--Wilson chapter,
LNCS 673 (1993), pp. 180--194, DOI 10.1007/3-540-56686-4_43, remains
unread in full. Consequently (K1) is a stated source premise, not
independently reconstructed in this packet.

## Proposed conditional deduction

The P_alpha are pairwise nonassociate: their specializations in (K1) are
monic powers of different linear factors. Let sigma square every
coefficient. Since phi_t is over F2, sigma permutes its normalized
absolute factors. Specializing sigma(P_alpha) at Y=0 gives
`(X+alpha²)^(q+1)`, so unique factorization and (K1) give

    sigma(P_alpha)=P_(alpha²).                             (K2)

Normalization is needed here to remove a scalar; the monic
specialization forces that scalar to one. The coefficient of X^q in
(K1) is alpha, so a field of definition of P_alpha must contain alpha.
Conversely (K2) shows that the sigma-orbit has exactly the orbit length
d of alpha under squaring. Its minimal coefficient field is F_(2^d).

For one orbit O define `Q_O=product_(alpha in O) P_alpha`.
Equation (K2) makes Q_O fixed by sigma, hence a polynomial over F2 of
degree d(q+1). If Q_O had a proper nonconstant F2 divisor, its set of
absolute factors would be a nonempty proper sigma-invariant subset of
O, impossible for one orbit. Thus Q_O is irreducible over F2. The
different Q_O are precisely the irreducible F2 factors of the affine
phi_t. This argument uses distinctness, normalization, unique
factorization and Frobenius descent; all are review targets.

For completeness of the affine/homogeneous transfer, odd t>1 has a
nonzero X^(t-1)Y coefficient in f_t(X,Y,0). Since R(X,Y,0)=XY(X+Y)
is also nonzero, phi_t(X,Y,0) is nonzero. Thus Z is not a factor,
dehomogenization retains the full degree t-3, and rehomogenizing its
factorization gives phi_t. Conversely homogeneous factorization
dehomogenizes without losing any factor to a power of Z. The same
reasoning works over the algebraic closure. This elementary transfer
lemma is itself an unreviewed deduction here.

## Consequences of the conditional deduction

For k=2 the two elements of F4 minus F2 form one orbit. Hence phi13
has two absolute quintics over F4 but a single irreducible factor over
F2. It supplies no two-positive-degree F2 factorization by itself.

For k>=3, there are q-2>k labels while every orbit has length at most k.
There are therefore at least two F2 factors. Grouping the orbit products
into two nonempty groups gives the positive-degree g,h required by
part (b), conditional on the source premise and the descent proof.
This is a family statement, not an exhaustive classification.

Small degree patterns follow from ordinary finite-field element degrees:

| k | t | Orbit lengths in F_(2^k) minus F2 | Irreducible F2 factor degrees |
|---|---|---|---|
| 2 | 13 | 2 | 10 |
| 3 | 57 | 3,3 | 27,27 |
| 4 | 241 | 2,4,4,4 | 34,68,68,68 |
| 5 | 993 | 5,5,5,5,5,5 | 165,165,165,165,165,165 |

These patterns are deductions, not a newly run multivariate factorization
experiment. They agree with the absolute component counts reproduced
in the 2019 paper, but those absolute degrees alone would not determine
the contest's factor fields without (K2). No unrestricted computational
classification is asserted, and no preliminary Gold result is reproduced.
