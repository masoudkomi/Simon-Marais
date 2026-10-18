# Exploratory smaller Runge quotient and coefficient control

18 October 2026 UTC. Root mathematical worklog, **UNVERIFIED**. These are new deductions developed after reading C's distinct frozen Runge cover. They are NOT premises or repairs of that submission, and are NOT accepted results. Root's entire OTHER whole initial for the unchanged C submission is separately frozen. Any theorem promoted from this note needs a complete constructor packet and TWO OTHER independent whole audits, with root excluded.

The direction below has not supplied an improved published bound, new prime exclusion or annual solution. No mathematical program, coefficient calculation, RR basis computation, scan or CAS was used. Preserve it as hand reasoning to investigate, rather than execute a huge formal construction without a useful arithmetic objective.

## 1. A degree-p quotient rather than the degree-p² cover

Retain the exact accepted fixed theta, p>=37 and actual beta^p=Ptheta(X), beta in K, Y>1 and Y^p=Phi_p(X). Its canonical coefficients n_a belong to0/1/2, augmentationp-1 and M1!=0. Let A(T) be the product of T-zeta^a over n_a=2, and B(T) the product over n_a=0. Both are monic and coprime. Their degrees are the same r: comparing augmentation with the number of coefficients gives #2=#0. Also r>=1, since otherwise theta=N, contradicting M1!=0; r<=(p-1)/2. Complement2N implies that A and B are complex conjugates, though the proposed construction need not use this extra identity.

Consider the smooth projective normalization of

    V^p=A(T)/B(T),   V=beta/Y at the actual point.

This is the diagonal-mu_p quotient of C's U,W cover. A simple zero at any root of A proves Kummer degreep and geometric integrality. The ACTUAL point (X,beta/Y) is still K-rational. V itself need not be integral, but the Runge rational function is T, whose actual value is the integer X. A nonintegral coordinate must not be turned into an uncounted S-prime assumption.

At infinity, t=1/T, the ratio has constant1. Its p distinct roots give p K-rational UNRAMIFIED infinity points Q_c, each with T having a SIMPLE pole, V having residue zeta^c. The complete local expansion is

    V=zeta^c [A*(t)/B*(t)]^(1/p),
    A*(t)=t^r A(1/t), B*(t)=t^r B(1/t).

The 2r finite simple zeros/poles of A/B have tame ramificationp and there is no infinity ramification. Riemann–Hurwitz therefore suggests exactly

    g'=(p-1)(r-1).

This is about a factor p smaller than the former cover's genus and changes local decay from |X|^(-1/p) to |X|^(-1). Neither fact compares the still-unknown auxiliary coefficients with a published height estimate.

## 2. Explicit integral basis with a simpler monic equation

Proposed K[T] normalization basis:

    b_0=1,   b_i=B(T)V^i, 1<=i<p.

Character projections split the extension into K(T)V^i. At an A-root, ord(V)=1; at a B-root ord(V)=-1 while ord(T-root)=p. For0<i<p the coefficient of V^i must therefore be regular at A-roots, vanish once at B-roots, and have no other finite poles. It is B times a polynomial. This gives the proposed basis, with the usual proviso that all local normalization/eigenprojection hypotheses must be fully audited.

There is a particularly simple integral equation already over O_K[T]:

    b_i^p=A(T)^i B(T)^(p-i).

Thus each b_i is integral over O_K[T]. A coefficient rescaling that puts a polynomial combination of these b_i in O_K[T]-coefficients suffices to make its actual value integral; no numerical evaluation of beta/Y's denominators is required.

At every Q_c, b_i for i>0 has pole orderr and leading character zeta^(ci), while b_0 has order0. The full Fourier matrix across the p infinity points prevents simultaneous cancellation of a maximum pole order. Hence the span with poles bounded by d at all infinity points is proposed to be exactly

    T^h (0<=h<=d),
    T^h b_i (0<i<p, 0<=h<=d-r).

For d>=r it has N=pd+1-g' monomials, matching Riemann–Roch. In particular choose d=2g'+p-1=(p-1)(2r-1). Imposing all Laurent coefficients -d,...,0 at every Q_b except Q_c gives L(dQ_c-sum_(b!=c)Q_b), degree2g' and dimensiong'+1. The complete family has no common finite K-point zero by the same dimension-difference argument. At r=1, genus0 and degree0 still give dimension1 and evaluation-kernel0; do not discard this boundary.

## 3. Optional entirely explicit but very large cofactor bound

This is a proposed certificate scheme, not a program to run. Let R=(p-1)(d+1) be the number of Laurent constraints. The preceding dimension formulas give rankR=N-(g'+1), so the constraint matrix should have full row rank. Its cofactor kernel vectors on ALL(R+1)-column subsets span the kernel: fix any invertible R-column set, and adding each remaining column gives the usual kernel basis. Including zero vectors from other subsets causes no problem. This permits a full nonvanishing family without selecting a pivot set from an actual solution.

For i>0 the normalized local function t^r b_i has the product form

    A*(t)^(i/p) B*(t)^(1-i/p).

All exponents are nonnegative and their sum isr. Its coefficient of t^k has denominator cleared by p^k k!: expand the finitely many binomial factors and multiply by the integer multinomial coefficient. Thus D=p^d d! clears EVERY matrix entry involved. At |t|=1/2 its conjugate modulus is at most(3/2)^r, so Cauchy bounds each coefficient of order<=d by2^d(3/2)^r. The integer H=D*2^d*3^r is a deliberately loose common conjugate bound for the rescaled matrix entries, including b_0 entries.

Each R-by-R cofactor is then an algebraic integer with every conjugate bounded by C=(R H)^R, using Hadamard and R>=1. The associated function is an O_K[T]-linear combination of at mostR+1 monomials, hence integral over O_K[T]. On |t|=1/2, |T|=2, and

    |b_i|=|A|^(i/p)|B|^(1-i/p)<=3^r,

so every monomial is bounded by J=2^d 3^r. The circle bound L=(R+1) C J is uniform for all labels/functions/embeddings. At an unused infinity branch F/t is analytic, giving |sigma(F(P))|<=2L/|X|. At mostp-1 labels are forbidden by thep-1 embeddings, leaving a common unused label amongp; the family has some nonzero integral evaluation. Its norm would imply the proposed explicit bound

    |X|<=2(R+1)(R H)^R 2^d 3^r.

This bound is enormous and may be much WORSE than the already accepted R6 or stronger published bounds. Its purpose is an explicit zero-safe family and a simpler quotient/denominator interface. No claim of a numerical advance is justified. The full-row-rank/count, every Laurent normalization sign, integrality projection, all embeddings, negative X and cofactor spanning need two independent whole audits before use. Better coefficient control or an actual remaining arithmetic subcase would be needed to turn this into useful progress toward the annual problem.

Primary methodological context actually read: Levin2008, Theorems1.2–1.3 and the COMPLETE operative Section2 proof/effectivity discussion, plus opening covering context. No later explicit superelliptic theorem or unread full-paper claim is imported. Root will return first to the new actual2021 m6 exclusion audit, rather than execute this huge auxiliary construction.
