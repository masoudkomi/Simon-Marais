# 2022 B4(b): a rational-lift complexity obstruction

**candidate proof - unverified**, version 1, 2026-10-16 UTC.

This is a partial result about the exact finite controller already used in
the accepted proofs. It is not a proof of universal equality. It has not
received either of the two independent adversarial audits required by the
research protocol. The author requests both audits before any promotion.

Requested worker settings: `gpt-6.1-sol`, `max`, as specified by the
coordinator's assignment and repository protocol. An effective-setting
readback is unavailable to this worker.

## 1. Input, scope, and terminology

The official open target is 2022 B4(b), for positive integers with
\(a_0b_0\ge600\), under the simultaneous recurrence

\[
a'=a+2\lfloor b/20\rfloor,\qquad
b'=b+3\lfloor a/30\rfloor.
\tag{1}
\]

We use the accepted exact quotient identities in
`../proofs/reviewed-partials-v1.md`, P1. The established strip
\(I=[-13,23]\cap\mathbb Z\) may be used as attributed context for an
actual orbit after entry; its preliminary trapping assertion is not
proved or investigated here. The abstract claims below concern infinite
paths staying in this finite strip controller. Published inputs and the
official statement are attributed in `../references.md`. The arguments
below are proposed deductions of this pass, with no novelty claim.

Write

\[
b=60Q+r,\quad 0\le r<60,\quad d=a-b,
\]
\[
c(d,r)=3\left\lfloor\frac{r+d}{30}\right\rfloor,
\qquad
D(d,r)=d+2\left\lfloor\frac r{20}\right\rfloor-c(d,r).
\]

For each controller state \(S=(d,r)\in I\times\{0,\ldots,59\}\), and
each control \(e\in\{0,\ldots,9\}\), the successor and correction are

\[
d'=D(d,r),\quad r'=(6e+r+c(d,r))\bmod60,
\qquad h=\frac{r+c(d,r)-r'}6.
\tag{2}
\]

The residue convention in (2) is the least nonnegative residue. For a
valid path all its states stay in the displayed finite set. The integer
\(h\) is well defined: the numerator is divisible by 6. Also

\[
h\equiv-e\pmod {10}.
\tag{3}
\]

Indeed, if \(r'=6e+r+c-60k\), then \(h=10k-e\). In the strip,
\(-13\le r+d\le82\), so \(c\in\{-3,0,3,6\}\). Consequently
\(-62\le r+c-r'\le65\); since this quantity is divisible by 6,

\[
-10\le h\le10.
\tag{4}
\]

For actual integer states, the accepted quotient calculation gives

\[
b'=66Q+r+c,
\qquad 10Q'=11Q+h.
\tag{5}
\]

Here and below \(\mathbb Z_{10}\) means the inverse-limit ring of
integers modulo \(10^N\), not a field. A rational element of this ring
means the diagonal image of a rational number \(u/v\) in lowest terms
with \(\gcd(v,10)=1\).

For a one-sided infinite word \(x\), let \(P_x(L)\) denote the number
of distinct contiguous length-\(L\) factors occurring anywhere in it.
The word need not be recurrent. An ultimately periodic word has a
periodic tail, with an arbitrary finite prefix permitted.

## 2. The lift of an infinite controller path

Let \((S_n,e_n)\) be an infinite valid controller path, and let \(h_n\)
be its corrections from (2). Define in \(\mathbb Z_{10}\)

\[
Q_n=-\sum_{j\ge0}h_{n+j}\frac{10^j}{11^{j+1}}.
\tag{6}
\]

The series converges in the inverse-limit ring: terms with \(j\ge N\)
vanish modulo \(10^N\), and powers of 11 are invertible there. It
satisfies

\[
10Q_{n+1}=11Q_n+h_n,
\qquad Q_n\bmod10=e_n,
\tag{7}
\]

where the second equality follows from (3). Thus (6) gives the
\(10\)-adic quotient lift of the path. It agrees with the accepted
finite lifting bijection at every finite depth. Uniqueness also follows
directly: two lifts differ initially by an element divisible by
\(10^N\) for every \(N\), because (7) can be iterated and 11 is a
unit. Such an element is zero in the inverse limit.

This construction does not assert that \(Q_0\) is an ordinary integer,
positive or otherwise. In Section 5 it will produce explicit irrational
\(10\)-adic lifts of avoiding paths.

## 3. Rational-lift dichotomy

**Proposed theorem.** For an infinite valid path in the strip controller,
if the lift \(Q_0\) in (6) is rational, then either

1. the sequence of full states \((Q_n,d_n,r_n)\) is ultimately periodic;
   in particular, \(h\) is ultimately periodic; or
2. its correction word satisfies

\[
\liminf_{L\to\infty}\frac{P_h(L)}L
\ \ge\ \kappa:=\frac{\log10}{\log(11/10)}.
\tag{8}
\]

The alternatives need not be asserted exclusive. The useful implication
is that a non-ultimately-periodic valid path with lower factor-complexity
slope less than \(\kappa\) cannot have a rational lift.

### A fixed denominator

Assume \(Q_0=u/v\), where \(v>0\), \(\gcd(u,v)=1\), and
\(\gcd(v,10)=1\). By iterating (7), \(Q_n\) is rational with a
denominator dividing \(v10^n\). Because \(Q_n\in\mathbb Z_{10}\),
the powers of 2 and 5 in that denominator cancel. More explicitly its
numerator over \(v10^n\) is an integer divisible by \(2^n\) and by
\(5^n\), and hence by \(10^n\). Thus

\[
vQ_n\in\mathbb Z\quad\hbox{for every }n.
\tag{9}
\]

### The real growth alternative

The rational \(Q_n\) may now also be read as a real number. Put
\(\beta=11/10\) and define the real, convergent series

\[
C=Q_0+\sum_{j\ge0}h_j\frac{10^j}{11^{j+1}}.
\tag{10}
\]

The sign in (10) is positive. Formula (6) is a \(10\)-adic equality;
it does not identify the real sum in (10) with zero. Iteration of (7)
in the real numbers gives

\[
Q_n=C\beta^n-T_n,
\qquad
T_n=\sum_{j\ge0}h_{n+j}\frac{10^j}{11^{j+1}},
\qquad |T_n|\le10.
\tag{11}
\]

If \(C=0\), then the \(Q_n\) are bounded. By (9) they lie in a
fixed discrete lattice, so only finitely many values occur. There are
also only finitely many \((d_n,r_n)\). The full state has a deterministic
successor: its \(10\)-adic residue \(Q_n\bmod10\) determines
\(e_n\), equations (2) determine \((d_{n+1},r_{n+1},h_n)\), and
(7) determines \(Q_{n+1}\). A repeated full state therefore repeats
its entire future. A sequence in a finite set must repeat, proving the
first alternative in this case.

If \(C\ne0\), equation (11) implies that \(Q_n\) is eventually
strictly monotone. In detail,

\[
Q_{n+1}-Q_n=C(\beta-1)\beta^n-(T_{n+1}-T_n),
\]

and the last parenthesis has absolute value at most 20. The first term
eventually has absolute value greater than 20 and constant sign. Fix
\(n_0\) after which strict monotonicity holds. Also, directly from
(7) and (4),

\[
|Q_n|\le \beta^n(|Q_0|+10)-10
\le A\beta^n,\qquad A=|Q_0|+10.
\tag{12}
\]

### Equal factors force a large integer difference

Suppose length-\(L\) correction factors starting at
\(n_0\le n<m\) are equal. Iteration of (7) over those factors gives

\[
10^LQ_{n+L}=11^LQ_n+H,
\qquad
10^LQ_{m+L}=11^LQ_m+H,
\tag{13}
\]

with exactly the same integer
\(H=\sum_{j=0}^{L-1}11^{L-1-j}10^j h_{n+j}\).
Subtract, multiply by \(v\), and use (9). Since
\(\gcd(10^L,11^L)=1\),

\[
10^L\mid v(Q_m-Q_n).
\tag{14}
\]

The right side is a nonzero integer, by strict monotonicity, so its
absolute value is at least \(10^L\). But (12) gives

\[
v|Q_m-Q_n|\le 2vA\beta^m.
\tag{15}
\]

Therefore no two length-\(L\) correction factors can agree if their
starting indices lie between \(n_0\) and an integer \(M\) satisfying

\[
2vA\beta^M<10^L.
\tag{16}
\]

Take \(M_L=\lceil\kappa L-\log(2vA)/\log\beta\rceil-1\).
For all sufficiently large \(L\), this is at least \(n_0\) and
satisfies (16). Hence the starts \(n_0,\ldots,M_L\) supply
\(M_L-n_0+1=\kappa L-O(1)\) distinct factors. This proves (8).
The implicit constant depends on the given rational lift and path, not
on \(L\).

## 4. Application to ordinary admissible integer starts

For an actual orbit in the official domain, after the attributed entry
into the strip its quotient lift is an ordinary nonnegative integer.
The bounded case in Section 3 is impossible, including small quotients:
bounded \(Q_n\) and strip-bounded \(d_n,r_n\) would bound both
original coordinates. They are nondecreasing positive integer sequences,
so they would eventually be constant. Both increments in (1) would then
vanish, forcing \(a\le29\), \(b\le19\), and
\(ab\le551<600\). The product cannot have decreased from its initial
value at least 600. This is a contradiction.

Thus every admissible actual integer orbit has the complexity lower bound
(8) on its tail in the strip, whether or not equality has occurred.
Adding the finite prefix cannot reduce factor complexity. The full
residue-state word also satisfies

\[
\liminf_{L\to\infty}\frac{P_S(L)}L\ge\kappa,
\tag{17}
\]

because any length-\((L+1)\) state factor determines its length-\(L\)
correction factor by (2). This argument addresses the bounded-orbit and
equal-quotient exceptions before using nonzero divisibility.

This extends the accepted exclusion of an ultimately periodic full
residue-state word to an obstruction against sufficiently low factor
complexity. It does not bound from above the complexity of a general
avoiding path.

## 5. An explicit nonperiodic avoiding family with irrational lifts

At the state \((d,r)=(1,0)\), there are two valid two-step loops:

\[
\begin{array}{c|c|c|c}
\text{loop}&\text{controls}&\text{successive residues}&\text{corrections}\\
A&(0,0)&0,0,0&(0,0)\\
B&(1,9)&0,6,0&(-1,1).
\end{array}
\tag{18}
\]

All their differences are 1. For both residues 0 and 6,
\(c(1,r)=0\) and \(D(1,r)=1\); substituting the displayed controls
in (2) proves every entry of the table. Arbitrary concatenations of
these loops are valid abstract paths and avoid equality forever.

Fix any irrational \(\alpha\in(0,1)\), and define the lower mechanical
binary word

\[
w_j=\lfloor(j+1)\alpha\rfloor-\lfloor j\alpha\rfloor.
\tag{19}
\]

Use loop \(A\) when \(w_j=0\), and loop \(B\) when \(w_j=1\).
Its correction word is the length-two coding

\[
0\longmapsto(0,0),\qquad 1\longmapsto(-1,1).
\tag{20}
\]

The word \(w\) is not ultimately periodic: its prefix averages tend
to \(\alpha\), by telescoping (19), whereas an ultimately periodic
binary word has rational limiting average. The injectivity of the
two-letter code shows that \(h\) is not ultimately periodic either.
Indeed, an eventual period \(p\) for \(h\) gives the even period
\(2p\); reading aligned two-letter blocks gives an eventual period
\(p\) for \(w\).

For completeness, \(P_w(k)\le k+1\). A length-\(k\) block beginning
at position \(n\) is determined by \(x=\{n\alpha\}\) through
the differences
\(\lfloor x+(j+1)\alpha\rfloor-\lfloor x+j\alpha\rfloor\),
\(0\le j<k\). They are constant on each of the \(k+1\)
half-open arcs cut by the distinct circle points
\(-j\alpha\bmod1\), \(0\le j\le k\). Values at a breakpoint
are the right-hand values, consistent with the half-open convention.

A length-\(L\) factor of \(h\) starts at offset zero or one within
a coded pair. The corresponding underlying \(w\)-factors have lengths
at most \(\lceil L/2\rceil\) and
\(\lceil(L+1)/2\rceil\), respectively. Consequently

\[
P_h(L)\le
\left(\left\lceil\frac L2\right\rceil+1\right)+
\left(\left\lceil\frac{L+1}2\right\rceil+1\right)
=L+3.
\tag{21}
\]

If this path's unique \(10\)-adic lift were rational, the first
alternative of Section 3 would contradict its nonperiodicity, and the
second would contradict (21), since \(\kappa>1\). Thus its lift is
not rational in \(\mathbb Z_{10}\). In particular it cannot be an
ordinary positive integer start for the contest recurrence.

Combining consecutive terms of (6) gives an explicit expression for it:

\[
Q_0=\sum_{j\ge0}w_j\frac{100^j}{121^{j+1}}
\quad\hbox{in }\mathbb Z_{10}.
\tag{22}
\]

The same formal series also converges in the real numbers, to a number
between 0 and \(1/21\). These are different convergence settings;
this note does not identify their limits as one common real value or
claim a real transcendence result. Equation (22) supplies an explicit
family of nonperiodic avoiding controller paths whose finite positive
integer lifts exist at every depth, while their infinite lifts are
irrational \(10\)-adic integers.

## 6. Exact remaining gap and audit targets

General infinite avoiding paths can have much higher factor complexity
than (21). The two loops in (18) even permit arbitrary binary choices,
so an upper bound like (21) cannot be inferred from the existence of a
finite controller. No claim is made that every avoiding path is
mechanical, automatic, periodic, or has small complexity. The argument
does not exclude an ordinary integer lift of a nonperiodic avoiding
path with complexity satisfying (8).

Required independent audits should reconstruct: the fixed-denominator
argument in the ring \(\mathbb Z_{10}\); deterministic evolution of a
rational lifted state; the separation of real and \(10\)-adic sums;
strict monotonicity only in the unbounded real case; the nonzero integer
in (14); exact factor lengths and off-by-one choices in (16)-(17);
the small-quotient/product exception; and the mechanical-word partition,
coding, and loop arithmetic. No computational experiment is a premise
of this candidate.
