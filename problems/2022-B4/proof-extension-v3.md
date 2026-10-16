# 2022 B4(b): fixed-offset density theorem, version 3

**candidate proof - unverified**, 2026-10-16. This standalone partial proof
repairs the prefix-uniformity defect in version 2. It requires affected-
argument re-audits by both independent reviewers before any promotion.
Novelty is not established. The official universal equality question is
not resolved here.

## 1. Claim, official domain, and version boundary

Fix any integer \(\delta\). For each positive integer \(b\) for which
\(a=b+\delta>0\) and \(ab\ge600\), iterate the simultaneous map
\[
F(a,b)=\left(a+2\left\lfloor\frac b{20}\right\rfloor,
             b+3\left\lfloor\frac a{30}\right\rfloor\right).
\tag{1}
\]
The claim is that the set of these \(b\) whose orbit reaches equality
\(a_n=b_n\) for some \(n\ge0\) has natural density 1 as \(b\to\infty\).
Equivalently, the never-hit set on this fixed line has natural density 0.
Time 0 counts; when \(\delta=0\), the claim is immediate.

Only part (b) is investigated. This proof uses no preliminary trapping
theorem. Its auxiliary radius below depends on the initial difference;
it makes no assertion of eventual entry into the official fixed strip.
Published input is the recurrence and its hypotheses from the official
2022 Paper B, page 2, cited in references.md. The proof is a candidate
contribution of this research pass, without a novelty claim.

The frozen files `proof.md` v1 and `proof-extension-v2.md` remain unchanged.
Both initial independent audits found no substantive defect in v1 P1-P4.
Both found a blocking defect in v2's repeated-block count; their initial
reports are immutable. V3 reconstructs the needed lifting and counting
steps, rather than importing v2's faulty uniformity assertion.

## 2. Exact state and its ten abstract controls

At any time write \(d=a-b\) and \(b=60q+r\), where \(0\le r<60\), and
define
\[
c(d,r)=3\left\lfloor\frac{r+d}{30}\right\rfloor,\qquad
D(d,r)=d+2\left\lfloor\frac r{20}\right\rfloor-c(d,r).
\]
The integer-translation identity for floors, applied to (1), gives
\[
d'=D(d,r),\qquad b'=66q+r+c(d,r).
\tag{2}
\]
If \(e=q\bmod10\) and \(r'=b'\bmod60\), then
\[
r'=(6e+r+c(d,r))\bmod60.
\tag{3}
\]
For fixed \((d,r)\), the next difference is independent of \(e\). As
\(e\) takes the ten values 0,...,9, the next residues take each value
congruent to \(r+c(d,r)\pmod6\), once each. In particular every interval
of six consecutive integers within 0,...,59 contains exactly one
available next residue.

These are choices in an abstract state graph. A fixed integer pair has
one actual control and one successor. Sections 5-6 justify using finite
control choices when counting initial integers.

## 3. The missing uniformity: a radius valid after every prefix

For arbitrary integer \(d\) and \(0\le r<60\), put
\[
u=r+d-30\left\lfloor\frac{r+d}{30}\right\rfloor,\qquad
v=r-20\left\lfloor\frac r{20}\right\rfloor.
\]
Even when \(r+d<0\), integer floor remainders satisfy
\(0\le u\le29\) and \(0\le v\le19\). Substitution into (2) gives
\[
10D(d,r)=9d+u-v,\qquad
|D(d,r)|\le\frac{9|d|+29}{10}.
\tag{4}
\]
For the fixed initial difference \(\delta\), define the integer
\[
M=\max\{|\delta|,29\},\qquad K=M+1.
\tag{5}
\]
If \(|d|\le M\), equation (4) yields
\[
|D(d,r)|\le\frac{9M+29}{10}\le M.
\tag{6}
\]
Starting with \(|d_0|\le M\), induction therefore bounds every subsequent
difference by \(M\), **for every finite sequence of controls**. This
includes all actual surviving prefixes, and all abstract continuations
used below. The same \(M\) and \(K\), chosen from the original
\(\delta\), remain fixed throughout the counting argument.

This is a coarse auxiliary bound for the equality-density argument.
It does not prove or reproduce preliminary part (a), whose fixed narrow
eventual interval is not asserted or used here.

## 4. A hitting path of at most K steps from every reachable state

Consider any current state \((d,r)\) with \(|d|\le M\), at any prefix
length. Its next difference \(h=D(d,r)\) satisfies \(|h|\le M\) by (6).
If \(h=0\), equality occurs on that first update. Otherwise choose the
control in (3) so that the ensuing residue \(s\) is in

- \(30\le s\le35\) when \(h>0\);
- \(20\le s\le25\) when \(h<0\).

The availability follows from the six consecutive residues in either
interval. At every later update apply the same rule according to the
ensuing nonzero difference.

For a positive \(h\), the chosen residue gives
\[
D(h,s)=h+2-3\left\lfloor\frac{s+h}{30}\right\rfloor\le h-1.
\]
When \(h=1\), the value is exactly 0. For \(h\ge2\),
\[
D(h,s)\ge h+2-\frac{s+h}{10}
\ge\frac9{10}h-\frac32>0.
\tag{7}
\]
Thus positive differences strictly decrease to 0 without becoming
negative. From positive \(h\), at most \(h\le M\) further updates are
needed.

For a negative \(h=-k\), where \(k\ge1\), the chosen residue satisfies
\(s-k<30\), hence
\[
D(-k,s)=-k+2-3\left\lfloor\frac{s-k}{30}\right\rfloor\ge-k+2.
\tag{8}
\]
For \(k=1,2,3\), the respective values are 1,0,-1 because
\(17\le s-k\le24\). For \(k\ge4\), the strict inequality
\(\lfloor x\rfloor>x-1\) gives
\[
D(-k,s)<-k+5-\frac{s-k}{10}
\le-\frac9{10}k+3<0.
\tag{9}
\]
Consequently negative differences increase by at least 2 while remaining
negative until they reach -2 or -1, which map to 0 or 1; the positive
rule then maps 1 to 0. At most \(\lceil k/2\rceil+1\) further updates
are needed. Since \(k\le M\) and \(M\ge29\),
\[
\left\lceil\frac{k}{2}\right\rceil+1
\le\left\lceil\frac M2\right\rceil+1\le M.
\tag{10}
\]
Including the initial update that produced \(h\), every current state
in the radius has a hitting control word of length at most \(K=M+1\).
Equations (6) and (10) make this bound uniform over **every** surviving
prefix from the original fixed difference, not just over its 60 initial
residues. This is the repaired assertion.

## 5. Finite words correspond bijectively to initial residue classes

The map has the common-shift identity
\[
F(a+60t,b+60t)=F(a,b)+(66t,66t)\qquad(t\in\mathbb Z).
\tag{11}
\]
This is an algebraic floor identity; for this identity alone the same
formula (1) can be evaluated on arbitrary integers. All actual starts
counted for the theorem will satisfy the official positive domain.

If the initial pair is shifted by \(60\cdot10^m z\) in each coordinate,
then for \(0\le i\le m\) its shift at time \(i\) is
\[
60\cdot11^i10^{m-i}z.
\tag{12}
\]
Induction follows from (11), since the shift is divisible by 60 before
each of these updates. The states \((d_i,r_i)\) through time \(m\)
therefore agree, and the quotient \(q_m\) shifts by \(11^m z\).
The controls before time \(m\) agree as well.

Fix an initial residue \(r_0\). A length-zero control word corresponds
to the one class modulo 1 for \(q_0\). Suppose a word of length \(m\)
corresponds to one class modulo \(10^m\). Its ten refinements modulo
\(10^{m+1}\) are represented by shifting \(q_0\) by \(10^m z\),
\(0\le z<10\). By (12), they keep the existing word and time-\(m\)
state while changing \(q_m\bmod10\) by \(11^m z\). Since
\(\gcd(11,10)=1\), the ten next controls occur once each. Induction
proves that every length-\(N\) control word corresponds to exactly one
class of \(q_0\pmod{10^N}\), or exactly one class of
\(b_0\pmod{60\cdot10^N}\) with that fixed \(r_0\).

Every such finite class has arbitrarily large positive representatives
with \(b_0+\delta>0\) and \(b_0(b_0+\delta)\ge600\). No infinite
control word is claimed to have an ordinary positive integer lift.

## 6. Repeated-block finite counting and the density limit

Keep \(\delta\), \(M\), and \(K\) fixed as in (5). Let \(A_N\) be the
number of classes of \(b_0\pmod{60\cdot10^N}\) whose differences avoid
0 at all times 0,...,N. The state sequence up to time \(N\), and hence
this condition, depends only on that class, by (12). Let
\[
p_N=\frac{A_N}{60\cdot10^N}.
\]
After any surviving prefix of length \(N\), its current state remains
in the radius by (6). Section 4 supplies a hitting extension of length
\(\ell\le K\). Extend that word arbitrarily to length \(K\); a history
that has hit remains classified as hit even if later equality is lost.
Among the prefix's \(10^K\) refinements, Section 5 makes all extension
words distinct residue classes, and at least one is therefore removed
from survival. Thus the **same** fixed block length gives
\[
A_{N+K}\le(10^K-1)A_N,\qquad
p_{N+K}\le(1-10^{-K})p_N.
\tag{13}
\]
In particular, for every integer \(t\ge0\),
\[
p_{tK}\le(1-10^{-K})^t.
\tag{14}
\]
This is finite counting using a congruence-class bijection. It assumes
no independence or distribution theorem for one actual integer orbit.

For each fixed \(N\), the finite-time survivor set is periodic in the
initial \(b\), with modulus \(60\cdot10^N\), apart from the finitely
many values excluded by the official positivity and product hypotheses.
Its natural density is therefore \(p_N\). The never-hit set is a subset
of it for every \(N\), so its upper natural density is at most
\((1-10^{-K})^t\) for every \(t\), by taking \(N=tK\). These upper
bounds tend to 0. Its lower density is nonnegative, so its natural
density is 0, and the hitting set has density 1. This uses containment
in each fixed finite-time set, not an exchange of an infinite
intersection with a density limit.

## 7. Review objections, repair boundary, and remaining gap

V2 supplied a local bound for a state whose current difference was the
specified initial value, then incorrectly reused it after all surviving
prefixes. R1's admissible start (599,600) has \(K_{v2}(-1)=3\) but reaches
state (3,12) after three avoiding steps, needing four more abstract
steps to hit. R2's start (25,24), at the inclusive product boundary,
has \(K_{v2}(1)=4\) but reaches state (6,27) after four avoiding steps,
needing five more. Neither witness contradicts the density theorem; both
invalidate v2's conditional counting premise.

V3 retains the valid local control idea, bounds all reachable differences
by the initial-data-dependent radius, proves the fixed uniform bound
\(K=M+1\), and rebuilds (13)-(14). For both witnesses it uses \(M=29\),
\(K=30\), which applies at their later states as at their initial states.
The old bounds 3 and 4 are not used anywhere in this proof.

Both independent reviewers must re-audit Sections 3-6 and their
interaction, including the remainder bound for negative floor arguments,
the radius endpoints, the initial update in the path count, the finite
lifting modulus, and the quantifier that the same K applies at every
prefix. Review evidence is not a premise of this analytic argument.

A density-zero exceptional set may contain positive integers. Nothing
here proves it empty or gives a counterexample to the official question.
The theorem is on each fixed offset; it does not assert a two-dimensional
density statement when the offset varies with the size of the start.
