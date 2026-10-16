# R2 affected-argument re-audit: 2022 B4(b), extension v3

Verification date: 2026-10-16. I completed this re-audit without reading
the other reviewer's v3 re-audit or conclusions. The old witnesses quoted
in v3 were reproduced directly from their integer starts; no other review
file was read. The initial R2 report and frozen proofs were not edited.

Requested launch settings remain `gpt-6.1-sol` with reasoning `max`.
No effective-setting readback is available; these are requested settings,
not independently verified effective settings.

## Audited object and recommendation

Audited `proof-extension-v3.md`, SHA-256
`0238f99a93b0ba1076484db1c16b173efcc02be4410e859f2c5bafc55f0f2a3f`.

**No substantive mathematical objection found in this re-audit.** The
new radius and fixed block length repair R2-2022-01 for v3. Sections 3-6
now establish the density-one statement for each fixed integer offset.
The proof includes its needed quotient and finite lifting arguments and
does not depend on the faulty v2 counting premise or on the preliminary
trapping theorem.

This is a reviewer recommendation to resolve the earlier objection in
the separately versioned repair. It does not erase the defect in frozen
v2 and does not promote any status; promotion belongs to the coordinator
after both required audits. The result remains partial: it does not
establish that every admissible integer start hits equality.

## Independent reconstruction of the repair

### Exact state and remainder bound

I rechecked Section 2 against the simultaneous recurrence and the official
positive-integer/product hypotheses verified in the initial audit.
Writing \(b=60q+r\) gives

\[
d'=d+2\lfloor r/20\rfloor-3\lfloor(r+d)/30\rfloor=D(d,r),
\qquad b'=66q+r+c(d,r).
\]

The residue equation has exactly ten different successors, one for each
control \(q\bmod10\), comprising precisely one residue class modulo 6.
Every six-consecutive-residue interval used by the control rule therefore
contains an available residue. The distinction between abstract choices
and the single successor of an actual integer start is maintained.

For the remainders in Section 3, the identity
\(x-m\lfloor x/m\rfloor\in\{0,\ldots,m-1\}\) holds for negative integers
\(x\) as well as nonnegative ones. Thus \(u\in[0,29]\),
\(v\in[0,19]\), and

\[
10D=10d+(r-v)-(r+d-u)=9d+u-v.
\]

Here \(u-v\in[-19,29]\), so \(|u-v|\le29\). The triangle inequality
gives exactly the claimed absolute bound, with no sign assumption on
\(d\) or \(r+d\).

Set \(M=\max(|\delta|,29)\). For any current \(|d|\le M\),
\(9M+29\le10M\), so every one of the ten successors again has difference
in \([-M,M]\). Induction applies after every finite prefix and during
every abstract continuation. The choice of \(M\) depends only on the
original fixed \(\delta\), not on the prefix length, its controls, or
\(b\).

The endpoint \(M=29\) is included: \(D(29,0)=29\) saturates the positive
bound. Strict contraction is neither asserted nor needed. Negative
remainder arguments cause no exceptional case. This auxiliary interval
depends on the initial offset and makes no claim of eventual entry into
the preliminary part's narrow fixed interval.

### Uniform hitting length and the initial update

From any current state in that same radius, one update produces
\(h=D(d,r)\), also with \(|h|\le M\). If \(h\ne0\), the current control
can select its ensuing residue in the stated sign-dependent interval.
Thus the control acts on the residue for the following difference
update; the argument does not incorrectly make it choose the first
difference \(h\).

For positive \(h\), the selected residue 30 through 35 makes the next
difference at most \(h-1\). At \(h=1\) it is zero, and at \(h\ge2\)
the lower bound \(0.9h-1.5>0\) prevents a negative overshoot. Hence
there are at most \(h\le M\) further updates.

For negative \(h=-k\), residues 20 through 25 give increase at least 2.
The small cases \(k=1,2,3\) are exactly 1, 0, -1. For \(k\ge4\), the
strict upper bound \(-0.9k+3<0\) excludes a zero or positive overshoot.
There are at most \(\lceil k/2\rceil+1\) further updates, including the
possible -1 to 1 to 0 passage. This is at most \(M\) because \(M\ge29\).

The initial update producing \(h\) is added separately, giving the single
fixed bound \(K=M+1\) from every current state. If a current difference
is already zero, equality has already occurred; survivor prefixes never
have that case. A shorter successful word can be padded arbitrarily
because the counted property is having hit at least once. All states
on the chosen continuation remain in the radius by the independent
invariance argument.

This proves the quantifier needed in counting: for the original fixed
\(\delta\), every length of surviving prefix has a hitting continuation
of length at most the same \(K\). It replaces, rather than merely
renames, v2's initial-state-only bound.

### Finite lifting and its exact modulus

The common shift of both coordinates by \(60t\) shifts both updated
coordinates by \(66t\). For initial shift \(60\cdot10^m z\), induction
gives common shift \(60\cdot11^i10^{m-i}z\) at \(i\le m\). Therefore
the states through time \(m\) agree, the controls before time \(m\)
agree, and \(q_m\) changes by \(11^m z\).

For a fixed initial residue and a length-\(m\) word, its ten refinements
of \(q_0\bmod10^m\) to classes modulo \(10^{m+1}\) add \(10^m z\),
\(0\le z<10\). They supply each next control once, since \(11^m\) is
invertible modulo 10. This reconstructs the induction from the
length-zero class: length-\(N\) words correspond bijectively to
\(q_0\bmod10^N\), or to one class of \(b_0\bmod60\cdot10^N\) with
the prescribed residue modulo 60.

The state through time \(N\), including its final residue, is determined
by that modulus. Avoidance of equality through time \(N\) may need less
information, but using this larger modulus is safe and causes no
off-by-one error in the refinement count. Each finite class contains
arbitrarily large admissible ordinary positive integers with the fixed
offset. The algebraic extension of the floor map to arbitrary integers
is used only to justify congruence identities; the actual counted starts
are the official positive domain.

There is no appeal to an ordinary integer lift for an infinite control
word. The finite lifting result is sufficient for the repeated finite
counts.

### Repeated blocks and the density limit

Every class counted by \(A_N\) has exactly \(10^K\) refinements at
modulus \(60\cdot10^{N+K}\). They correspond to all length-\(K\)
extension words. Its current state lies in the same fixed radius; the
uniform path supplies at least one extension which has hit. Classes
already excluded from \(A_N\) cannot become survivors later, even if
their difference ceases to be zero. Consequently

\[
A_{N+K}\le(10^K-1)A_N.
\]

Dividing by \(60\cdot10^{N+K}\) gives the stated recurrence for \(p_N\).
The base value \(p_0\le1\) yields the geometric bound at every
\(N=tK\). All quantities \(\delta,M,K\) stay fixed in this induction.
The argument uses a finite congruence-class bijection, not probabilistic
independence or equidistribution along an orbit.

For each fixed \(N\), its survivor set has natural density \(p_N\),
since it is periodic except for finitely many inadmissible positive
integers. The exclusions are finite for every fixed integer \(\delta\),
including negative or arbitrarily large offsets. The never-hit set is
contained in each finite-time survivor set; hence its upper density is
bounded by \((1-10^{-K})^t\) for every \(t\). Since \(K\) is finite,
these bounds tend to zero. No exchange of limits or infinite-intersection
density principle is used. The complement of the admissible starting
domain is finite, so the hitting set has natural density one among all
positive \(b\) as well as relative to that domain. At \(\delta=0\),
time-zero equality handles every admissible start directly.

The constants are not uniform as \(\delta\) varies. The proof correctly
claims a separate theorem on each fixed line and does not infer a
two-dimensional density or an empty exceptional set.

## Checks of both old witnesses

Both witnesses have original offset of absolute value 1, so v3 uses
\(M=29\), \(K=30\) throughout their histories.

- \((599,600)\) evolves in three updates to \((795,792)\), whose state is
  \((3,12)\). The abstract continuation
  \((3,12)\to(3,30)\to(2,33)\to(1,30)\to(0,33)\) hits in four
  updates, within the new bound.
- \((25,24)\), with product exactly 600, evolves in four updates to
  \((33,27)\), whose state is \((6,27)\). Applying v3's sign rule gives
  \((6,27)\to(5,30)\to(4,33)\to(3,30)\to(2,33)\to(1,30)\to(0,33)\),
  a six-update continuation, also within the new bound. The shorter
  five-update path in the initial report remains valid but is unnecessary.

These are finite abstract paths for the counting argument; they are not
asserted to be the next actual paths of those fixed integer starts. The
earlier counterexamples invalidate bounds 3 and 4 in v2, while v3 uses
neither bound. The old one-step R2 state \((3,24)\) is covered as well.

## Evidence and clean checkpoint

`review-2-v3-evidence.py` and `review-2-v3-evidence.txt` contain the new
finite audit evidence. Command, from the repository root:

```sh
.venv/bin/python -u problems/2022-B4/reviews/review-2-v3-evidence.py > problems/2022-B4/reviews/review-2-v3-evidence.txt
```

Environment: repository `.venv/bin/python`, Python 3.12.14, macOS arm64,
standard library only. The bounded run completed in under one second
and emitted incremental checkpoints. No native CAS, external dependency,
network access, installation, or long-running child process was used.

The finite checks included 240,060 remainder cases with differences from
-2000 through 2000; full finite radius checks for \(M=29,30,31,60,123\);
local inequalities at magnitudes through 10,000; a 3,540-state graph for
\(M=29\); both actual witness prefixes; and 31,000 finite lifting classes,
including negative offsets and a fixed offset 1000. The remainder
extrema 0, 29 and 0, 19 all occurred. The endpoint
\(D(29,0)=29\) was checked. The script did not attempt to enumerate
\(10^{30}\) control blocks: the unrestricted counting and density
conclusions are the analytic arguments above, not consequences of finite
computational evidence.

Checkpoint fingerprints verified unchanged:

- v1: `8b35be18bb70f81b623f78e7dd1a148478c698c1f5ad32e4097def92ff75aed3`.
- v2: `b41aff3fcfadd33f80fdec80570d5b2f61807a5b9e16a28becacefaa237743ed`.
- initial R2 report:
  `1fe554ad4e5c77a1cad18a739a05b7ad1ceba4a8bce0beee91d6d34eedefbc04`.

No new substantive issue was identified. The only mathematical issue from
initial R2, R2-2022-01, is addressed by the separately preserved v3 repair.
No shared proof, initial report, issue log, or status was changed, and
no commit or push was made. No job remains running.
