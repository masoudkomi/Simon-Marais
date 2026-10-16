# 2022 B4 proof register

**Status: candidate proof - unverified (partial results only), version 1,
2026-10-16.** No full solution of B4(b) has been proposed. The arguments below
have not had the two independent adversarial reviews required by AGENTS.md.
They are research contributions of this pass; novelty has not been established.

## Scope and attributed input

Write
\[
F(a,b)=\left(a+2\lfloor b/20\rfloor,
             b+3\lfloor a/30\rfloor\right).
\]
All actual starts in this document are positive integers with product at least
600. Equality at time 0 counts. Only B4(b) is investigated.

We use, as established context, that the strip
\(I=[-13,23]\cap\mathbb Z\) for \(d=a-b\) is invariant and eventually
entered. This is attributed to the official 2022 solution notes and is also
stated in Henderson and Warnaar's 2023 organizer report; see references.md.
No proof of the preliminary result is reproduced here. The density theorem
below uses only invariance, for starts already in the strip.

## P1. Exact quotient dynamics and finite lifting

Let \(a=b+d\), \(b=60q+r\), \(0\le r<60\), and put
\[
c(d,r)=3\left\lfloor\frac{r+d}{30}\right\rfloor,
\quad D(d,r)=d+2\left\lfloor\frac r{20}\right\rfloor-c(d,r).
\]
Direct substitution in the simultaneous recurrence gives
\[
d'=D(d,r),\qquad b'=66q+r+c(d,r).
\tag{1}
\]
Consequently, writing \(e=q\bmod10\),
\[
r'=(6e+r+c(d,r))\bmod60.
\tag{2}
\]
As \(e\) ranges over 0,...,9, equation (2) takes every residue modulo 60
congruent to \(r+c(d,r)\pmod6\), exactly once. These are ten abstract
successors; an individual integer start has only its one actual successor.

The common-shift identity is
\[
F(a+60t,b+60t)=F(a,b)+(66t,66t)\quad(t\in\mathbb Z).
\tag{3}
\]
For a shift \(60\cdot10^m z\) of both initial coordinates, induction using
(3) shows that after \(i\le m\) steps the common shift is
\[
60\cdot11^i10^{m-i}z.
\tag{4}
\]
In particular the states \((d_i,r_i)\) through time \(m\) agree. The
quotient \(q_m\) changes by \(11^m z\). For \(z=0,...,9\), its residue
modulo 10 takes all ten values, because \(\gcd(11,10)=1\).

It follows by induction that, for fixed initial \((d,r)\), each word of
\(N\) successive controls \(e_0,...,e_{N-1}\) is realized by exactly one
class of \(q_0\pmod{10^N}\), equivalently one class of
\(b_0\pmod{60\cdot10^N}\) with the prescribed \(r\). Each such finite
class has arbitrarily large positive representatives satisfying the product
condition. This is a **finite** lifting statement. It does not say that an
infinite word has a lift that is an ordinary positive integer.

## P2. Candidate density-one partial theorem

**Claim.** Fix an integer \(d\in I\). Among positive integers \(b\) such
that \(b+d>0\) and \(b(b+d)\ge600\), the set for which the orbit starting
at \((b+d,b)\) ever reaches equality has natural density 1 in \(b\).
Equivalently, the exceptional set has natural density 0. This claim does
not say the exceptional set is empty.

### A short abstract path to equality

Take any current abstract state \((d,r)\) in the strip. Its ensuing
difference \(d'=D(d,r)\) is fixed before a control is chosen. By the
attributed invariance result, \(d'\in I\). If \(d'=0\), a hit has occurred.
Otherwise use the control in (2) to choose the ensuing residue as follows:

- If \(d'>0\), choose \(r'\in\{30,31,32,33,34,35\}\).
- If \(d'<0\), choose \(r'\in\{20,21,22,23,24,25\}\).

Each interval contains exactly one representative of the required class
modulo 6, so the choice is available. For \(1\le h\le23\) and
\(30\le s\le35\), formula (1) gives
\[
D(h,s)=h+2-3=h-1,
\]
because \(31\le s+h\le58\). For \(-13\le h\le-1\) and
\(20\le s\le25\), the same formula gives
\[
D(h,s)=h+2,
\]
because \(7\le s+h\le24\). Continue to choose the next residue according
to the sign of the next difference. A positive difference takes at most
23 further steps to reach 0. A negative difference either reaches 0 by
increments of 2, or reaches 1 and then 0, in at most 8 further steps.
Including the first step, every abstract state has a hitting path of
length at most \(K=24\).

### Counting finite control words

For fixed \(d\), survival through \(N\) steps is determined by the
initial residue class modulo \(60\cdot10^N\), by P1. After any surviving
prefix, at least one extension of length at most \(K\) hits 0. Extend it
arbitrarily to length \(K\). Thus at least one of the \(10^K\) equally
numerous length-\(K\) extensions hits. By finite counting, the fraction
of residue classes surviving through \(tK\) steps is at most
\[
\left(1-10^{-K}\right)^t.
\tag{5}
\]
No statistical independence of actual integer orbits is assumed here;
the equal counts are supplied by the finite lifting bijection.

For each fixed \(t\), the surviving set is periodic in \(b\), apart from
the finitely many starts excluded by positivity and the product condition.
Its natural density therefore exists and is bounded by (5). The never-hit
set is a subset of it for every \(t\); its upper natural density is at
most (5) for every \(t\), and hence is 0. This proves the stated candidate
partial theorem if all preceding inferences survive independent audit.

**Boundary checks.** \(d=0\) hits at time 0. The largest positive value
23 and smallest negative value -13 are included in the displayed floor
bounds. Removing finitely many small \(b\) does not affect natural density.
The result is along each fixed offset in the strip, not a two-dimensional
density result and not a solution for every start.

## P3. Arbitrarily long finite avoidance within the strip

For integers \(N\ge1\), \(t\ge1\), and \(0\le r\le19\), start with
\[
b_0=60\cdot10^N t+r,\qquad a_0=b_0+1.
\]
For every \(0\le n\le N\), direct induction gives
\[
b_n=60\cdot11^n10^{N-n}t+r,\qquad a_n=b_n+1.
\tag{6}
\]
Indeed, for \(n<N\), the common leading part is divisible by 60, and
the two small remainders \(r\) and \(r+1\) have floor quotients 0 under
division by 20 and 30, respectively. The added amounts are equal and
multiply the common leading part by \(11/10\). These starts are positive,
have product above 600, and have difference 1 through time \(N\).
Consequently a constant upper bound on the first equality time is
impossible, even for starts already at difference 1. Formula (6) says
nothing about what happens after time \(N\).

## P4. An ultimately periodic full residue state cannot be an admissible orbit

**Claim.** No orbit with the official positive/product hypotheses has an
ultimately periodic sequence \((d_n,b_n\bmod60)\). This excludes a simple
lift of a periodically repeated quotient-graph cycle. It does not exclude
periodicity of \(d_n\) alone.

Suppose the full state repeats with period \(p\) from some time onward,
and let \(r_n=b_n\bmod60\), \(q_n=(b_n-r_n)/60\). From (1)-(2),
\[
q_{n+1}=\frac{11q_n+h_n}{10},\qquad
h_n=\frac{r_n+c(d_n,r_n)-r_{n+1}}6\in\mathbb Z.
\]
The \(h_n\) are periodic with period \(p\). On one phase of the period,
the integer quotient therefore obeys
\[
x_{j+1}=\frac{Ax_j+H}{B},\qquad
A=11^p,\ B=10^p,\ H\in\mathbb Z.
\tag{7}
\]
Iterating (7) and multiplying by \(A-B\) shows
\[
(A-B)B^j x_j
=A^j\bigl((A-B)x_0+H\bigr)-H B^j.
\]
Since \(\gcd(A,B)=1\) and all \(x_j\) are integers, \(B^j\) divides
the fixed integer \((A-B)x_0+H\) for every \(j\). That integer must be
0. Equation (7) then implies \(x_j=x_0\) for all \(j\). Both original
coordinates at this phase repeat exactly after \(p\) steps. They are
nondecreasing, so every update in the period is zero. Positivity then
forces \(a<30\) and \(b<20\), giving \(ab\le29\cdot19=551<600\), a
contradiction.

## Review requirements and exact unresolved gap

Before any promotion, two independent reviewers must audit this whole
partial proof, initially without each other's conclusions. One must
reconstruct the argument. In particular check the simultaneous quotient
arithmetic, the finite control-word bijection, the finite counting-to-density
limit, all strip endpoints, and the periodic-orbit divisibility argument.

The full question is still open in this work. A density-zero exceptional
set can contain ordinary positive integers. The finite graph has many
infinite avoiding walks; finite liftability gives only successively nested
congruence classes, whose limiting 10-adic integer need not be an ordinary
positive integer. The present proof does not establish whether any
nonperiodic avoiding walk has such an integer lift.
