# Reviewed first-moment approximation and regular-tail bound

**Proved, independently reviewed partial results**, 2026-10-17 UTC.
The coordinator accepts all M1--M3 in the exact frozen body appended
below, following two fresh initially blind nonconstructor whole audits,
including independent reconstruction of every inference and both exact
rational signs. Both complete reports, issue ledgers and source checks
were read. No substantive objection or author repair was required.

Accepted conclusions are the uniform approximation inequalities
(1-1/N)rho_G<=lambda<=rho_G for actual obstruction subsets agreeing
below N, the cap error rho_D-lambda<=1/(D+1), the exact regular-tail
sign criterion, and **1.76522347<lambda<1.834856083**. The upper bound
is the unchanged previously reviewed result. The exact growth constant,
full grammar and unrestricted regularity/algebraicity remain unresolved.

The original candidate, reports and certificates remain unchanged.
Their historical unverified labels below are superseded solely for the
accepted M1--M3 scope by this register and the acceptance record.
No novelty is claimed. No preliminary part (a) proof is included.

---

# 2019 B4(b): first-moment approximation and a known regular tail

**Candidate proof - unverified**, v1, 2026-10-17 UTC. Coordinator construction.
Two fresh nonconstructor whole audits are required. This is a partial
result for the open part (b), not an exact determination of the growth
constant and not a claim of novelty. No preliminary part (a) is reproved.

## Accepted inputs and notation

Use the accepted canonical history language K on {L,R}, minimal forbidden
set F, c_n=|K intersect {L,R}^n|, and lambda=lim c_n^(1/n). Put R=1/lambda.
The second-pass acceptance register covers the frozen canonical-renewal
text and the complete length24 factor certificate. In particular F is
factor-free and has no nonempty proper suffix-prefix overlaps, and

    C(z)=1/(1-2z+F(z)), F(R)=2R-1, F'(R)<=2.          (I)

The prime at R denotes the convergent nonnegative first-moment series.
The accepted third-pass result defines F_D subset F, K_D=Avoid(F_D), and
rho_D=lim |K_D intersect {L,R}^n|^(1/n). It proves agreement F_D=F through
length2D+1 and the exact regular series

    F_3(z)=z^4+z^12/(1-2z^5-z^8).                   (II)

These are independently reviewed inputs, with immutable file hashes in
the companion freeze. The historical candidate labels inside frozen old
notes are superseded by their acceptance registers. The original
canonical count and the official distinct-string count have the same
lambda, as already accepted. No theorem about a larger regular language
or algebraicity of F is assumed here.

## M1. Uniform first-moment convergence of obstruction subsets

Let G be ANY subset of F, possibly infinite, containing every member of
F of length less than N, where N is an integer greater than1. Let
G(z)=sum g_n z^n, H(z)=F(z)-G(z), and let rho_G be the growth of
Avoid(G). Then

    (1-1/N) rho_G <= lambda <= rho_G,               (1)
    0 <= rho_G-lambda <= rho_G/N <= 2/N.

Proof. Avoid(G) is factorial and contains K and the all-L word of every
length. Its counts a_n satisfy 1<=a_n<=2^n and a_(m+n)<=a_m a_n.
Thus rho_G=inf a_n^(1/n) exists and a_n>=rho_G^n. The generating series
A_G has radius R_G=1/rho_G<=R and diverges at R_G.

Every subset G inherits both nonoverlap properties of F. The same
append-and-remove-final-forbidden-suffix bijection used in (I) gives the
FORMAL identity A_G(z)=1/D_G(z), D_G(z)=1-2z+G(z), even when G is
infinite: each coefficient has only finitely many words. For real
0<=x<R_G all needed series converge, since G<=F coefficientwise and
x<R. Taking x up to R_G, nonnegative monotone convergence and finiteness
of G(R)<=F(R) imply D_G(R_G)=0. This also handles R_G=R, without analytic
continuation or a simple-root assumption.

All derivative series are finite at R by (I). On [0,R], G' is
nondecreasing and <=F'(R)<=2. Finite first moment gives uniform
convergence of G' there, so D_G is continuously differentiable and the
fundamental theorem of calculus applies. Set A=2-G'(R)>=0. Because H
is supported in degrees at least N,

    H(R)<= (R/N) H'(R) <= (R/N) A.                 (2)

Also D_G(R)=D_F(R)-H(R)=-H(R), whence

    H(R)= integral_[R_G,R] (2-G'(t))dt
         >= (R-R_G) A.                            (3)

If A>0, cancel A in (2)-(3), obtaining R_G>=R(1-1/N).
If A=0, then H'(R)<=A=0. Its nonnegative coefficients and R>0 imply
H=0, so G=F and R_G=R. Both cases give
R_G/R=lambda/rho_G>=1-1/N, which is (1). This proof neither assumes
strict convexity nor divides by a possibly zero derivative gap.

In particular, take G=F_D and N=2D+2. Then for every D>=1,

    ((2D+1)/(2D+2)) rho_D <= lambda <= rho_D,
    rho_D-lambda <= 1/(D+1).                       (4)

This strengthens the earlier general O(log D/D) bound to O(1/D). It is
a universal error bound, not a claim that the actual error has that size.
It is weak for the small numerical caps already computed. No larger-cap
state enumeration has been performed or requested for this argument.

## M2. An exact sign criterion incorporating infinite known tails

For any G as in M1 define, at points where the displayed derivatives
exist,

    E_G(x)=D_G(x)-(x/N)D_G'(x)
          =1-2(1-1/N)x+G(x)-(x/N)G'(x).          (5)

At R, (2) and D_G(R)=-H(R) imply E_G(R)>=0. Moreover E_G is
nonincreasing on [0,R]. Indeed for 0<x<R,

    E_G'(x)=(1-1/N)D_G'(x)-(x/N)G''(x)<=0,

because D_G'<=0 and G''>=0. Every derivative is analytic on the OPEN
interval (0,R): G is coefficientwise bounded by F, which converges at R.
No finiteness of G''(R) is needed. Continuity of E_G at R follows from
the already finite first moment. Consequently E_G(t)>=E_G(R)>=0 for
0<=t<=R. If a rational trial r>0 lies in the convergence interval of
G and satisfies the EXACT inequality E_G(r)<0, it follows by contradiction
that r>R. Thus

    E_G(r)<0  ==> lambda>1/r.                      (6)

For the contradiction one only assumes r<=R; the derivative argument is
used on [0,R], never beyond the unknown convergence boundary of F.
A convergence check on the explicitly known G at the chosen r is enough.

## M3. The accepted separation-three tail improves the length24 bound

The complete accepted length24 polynomial is

    P24(z)=z^4+z^12+2z^14+3z^16+2z^17+4z^18+8z^19
           +6z^20+20z^21+14z^22+40z^23+42z^24.

Take as a SET union G=(F intersect words of length<=24) union F_3.
It contains all factors of length<25. The long branch of (II) has
prefix through24 equal to z^12+2z^17+z^20+4z^22: loop lengths are5,5,8,
and the terminal/base length is12. Terms at25 or greater are retained,
not subtracted. The z^4 short branch is already in P24. Thus exactly

    G(z)=P24(z)+z^12/(1-2z^5-z^8)
                    -z^12-2z^17-z^20-4z^22.      (7)

This is a union of actual word sets, so the formal subtraction cannot
create negative coefficients. No complete minimal factors at length25
or later are being claimed known. Put N=25 in (5).

The saved exact rational certificate uses

    alpha=176522347/100000000 = 1.76522347,
    r=1/alpha=100000000/176522347.

It verifies 1-2r^5-r^8>0, r<3/5, and E_G(r)<0 by integer numerator and
denominator arithmetic. Positivity of the loop denominator gives
2r^5+r^8<1, so the nonnegative rational geometric series in (7), and its
first derivative, converge at r. Formula (6) therefore gives the
candidate strict improvement

    lambda > 1.76522347.                           (8)

The certificate also has E_P24(r)>0, so at this precise trial the known
infinite regular tail supplies a strict extra sign contribution beyond
the old length24 first-moment test. No assertion that the old polynomial
could prove no other improved bound is intended. The previously accepted
upper bound remains lambda<1.834856083. The exact lambda, a complete
weighted grammar, and regularity/algebraicity of F remain unresolved.

## Finite arithmetic, failed direction and source scope

`coordinator-regular-tail-certificate-v1.py` uses only Fraction. Its
bisection selects a rational trial from an already known explicit
rational function. The proof uses only the final exact negative sign,
not monotonicity of signs at unproved trial points or a floating-point
root. Full fractions, coefficients and the next trial sign are in its
JSON. It enumerates no histories, factors, queues or automata. Child
PID79111 had an external10second timeout, exited0 and was reaped in
0.0456321239seconds; the start/completion/stdout/stderr files are saved.
No computation was rerun during this freeze. No dependency was installed.

The initial idea of splitting long minimal factors into canonical halves
would have supplied a roughly square-root cap error. It was discarded
because it is weaker than the already accepted O(log D/D) estimate.
The first-moment cancellation above avoids that loss. The proposed
regular-tail lower improvement is deliberately modest: using accepted
infinite factors adds information without inventing their complement.

All mathematical premises here are the repository's accepted renewal,
length24 and separation-three results, not a newly cited external paper.
The official four-move relation remains attributed to official solutions;
preliminary part (a) is not reproduced. Literature sources and limits for
the wider project remain in thirdpass-literature.md. No novelty claim,
full solution, full finite-state model or independent reviewer acceptance
is made. This packet must receive TWO fresh initially blind whole audits
before changing the accepted numerical enclosure or convergence theorem.
