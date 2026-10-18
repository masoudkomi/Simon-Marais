# PM9 entire initially blind whole audit 2

2026-10-18 UTC. Independent reviewer `/root/review_2022_complexity_r2` (B).
Requested inherited gpt-6.1-sol/max; independent effective-setting readback
unavailable. **Candidate proof - unverified; this report does not promote it.**

I reconstructed the entire operative PM9A–PM9C argument and all 48
obligations. I found no substantive defect, counterexample, or required
author repair in the stated scope. The proof gives an absolute positive
moment, a uniform actual-cutpath bound, and a strict improvement over the
current PM8 base. It does not determine the exact official value or an
effective error for the different all-scale entropy interface. Eight
closed scope notes are recorded separately. A second OTHER whole audit
and full coordinator reconciliation are still required.

This disposition was written before access to any corresponding NEW C
PM9 finding, report, ledger, source record, code, hash, or metadata. Its
release is embargoed until the coordinator explicitly confirms BOTH
entire initial freezes. The author is root alone and is excluded from
both required independent audits. I did not construct or contribute to
NEW PM9. I previously reviewed accepted WC, WO, and PM8 inputs, as well
as other 2017 packets; those older roles are disclosed and do not count
as fresh independent recertification of my own work. Root's older WC/WO
construction role is also retained. No NEW pending BT or R19 peer
material is an input to this audit.

## Exact target, input status, and official scope

The target is the unchanged 12,255-byte main
`notes/coordinator-path-moment-r3-candidate-v1.md`, SHA256
`0af3e42df62385e086a53eec1d95461ba01ba26148a6f92bd34b1fb778924076`,
under operative `coordinator-path-moment-r3-freeze-v2.json`, 4,093 bytes,
SHA256 `7210932f81b90afa8197fb40fe6c7cc3603fbfc85c39b58c67df4f36728b185d`.
All 16 author files were read, including working text, both checklists,
checks/failures, source MD/JSON, both admin programs as text, baseline,
validation, metadata, both freezes, and the notation note. Neither author
admin program was executed. The initial snapshot's compressed checklist
tokens are historical, not operative formulas. The explicit v2
checklist and unchanged main govern this review; the v2 manifest binds
all 12 original files without alteration. See N1.

The official target is the fixed unit-sided regular 2N-gon count for
integer N≥2, with base-2 logarithm divided by N². An upper bound is
within scope. I used the local statement and original official B4
passage, plus only the B4 part of the official comments. Source-tool
over-return of other contest problems was ignored; no such problem was
investigated or reproduced here.

The complete current accepted PM8, WC, and WO bodies and their MD/JSON
authorities were read. Their accepted mathematical bodies preserve the
exact original candidate as a byte-identical suffix. The new proof uses
the following operative interface on EVERY actual simple marked
arrangement of EVERY n≥2:

* a finite common set of north-to-south complete paths, each with n edges,
  with the same set indexed in the reverse orientation;
* strictly positive normalized forward/reverse path measures P,Q and
  `sqrt(PQ) ≥ K^(−n) rho^(−b/2)` on each common path;
* the separately paid complementary sum `sum chi^(−c/2) ≤ K0^n`;
* adapted greedy two-edge trials at forward degree four, otherwise one
  ordinary edge, full continuation mass one, success probability at
  least kappa at every arriving prefix, `c_F≤2t`, and `S≤b`;
* the reverse counterpart with the SAME both-direction b;
* the exact canonical marked insertion and fixed-polygon dictionary.

Here `c=c_F+c_R`. The terminal of each orientation contributes no
degree-zero penalty. The positive nonunique degree-two/at-least-five
penalties in b are the accepted both-direction statistic, not simply
the number of unsuccessful trials or a new forward-only statistic.
The current PM8 authority explicitly accepts its actual local geometry,
the disjoint targets, and the paid raw-row tilt. Its older WO4
conditional wording is historical; this exact premise was discharged
by accepted PM8. I do not silently import a wider abstract-DAG theorem
or an optimality result for arbitrary weights.

## Reconstruction of PM9A

Put `r=sqrt(rho)`, `a*=1−kappa(1−r)`, `q=−ln a*`, and `z=a*^(−1/2)`.
The accepted constants imply `0<r<1`, `0<kappa<1/16`, `0<a*<1`, and
`z>1`. At a trial, the actual indicator Y is zero or one. Conditional
on ANY already arriving prefix,

    E[r^Y] = 1−(1−r)Pr(Y=1) ≤ 1−kappa(1−r) = a*.

This uses no independence between trials. It keeps all conditional
two-edge continuations, including a small-probability exit or a second
step from a high-degree cell. Multiply each trial's conditional weight
by `r^Y/a*`; ordinary-block weights are unchanged. Every block row then
has total at most one. Unfold the finite directed graph into distinct
prefixes, even after reconvergence. From leaves of mass one, backward
induction bounds each subtree continuation by one. Multiplication along
one leaf gives exactly `P(p) r^S a*^(−t)`. The decomposition is unique
because the rule uses only the current degree and past. Consequently

    sum_p P(p) r^S(p) a*^(−t(p)) ≤ 1.

Variable trial counts do not require optional stopping. Trials near
the end are legal because accepted actual degree-four geometry leaves
two steps; nonterminal rows have continuation mass one. Shared block
endpoints do not reuse target sets: the next trial starting at the
previous endpoint has two new targets. Hence accepted `c_F≤2t` and
`S≤b` apply to every leaf, including b=0. Since z>1 and r<1,

    z^c_F ≤ z^(2t)=a*^(−t),       r^b ≤ r^S.

Both factors are positive. Multiplying and summing gives
`sum P z^c_F r^b≤1`. The occurrence of final b here is a pointwise
comparison AFTER the adapted finite-flow calculation. It never defines
a transition conditioned on future b. The reverse proof is independently
the same calculation for Q and `c_R`; it need not choose the same trial
blocks. Both sums use the same complete-path index set and the same b.

Cauchy on the square roots of these two arrays yields

    sum sqrt(PQ) z^((c_F+c_R)/2) r^b ≤ 1.

The r factor is `r^b`, not `r^(b/2)`. Each summand is at least
`K^(−n) rho^(−b/2) z^(c/2) r^b = K^(−n) z^(c/2)`.
The equality uses `r=sqrt(rho)` and the identical accepted b on both
sides. Thus

    sum_p z^(c(p)/2) ≤ K^n.

This proves the asserted positive absolute moment. It neither divides
by an unknown path count nor asserts that a uniform random path sees
any specified density of trials. This distinction closes the tempting
but invalid future-conditioning and uniform-path shortcuts.

## Reconstruction of PM9B

Let B=ln chi>0 and `theta=2B/(2B+q)`. Then `ln z=q/2`,
`0<theta<1`, and `theta ln z=(1−theta)B`. On EACH path, the two
positive numbers `X=z^(c/2)` and `Y=chi^(−c/2)` satisfy
`X^theta Y^(1−theta)=1`. The finite Hölder inequality therefore gives

    #paths ≤ (sum X)^theta (sum Y)^(1−theta)
           ≤ K^(n theta) K0^(n(1−theta)) = H^n.

The main also proves this inequality directly. The scalar function
`theta u+(1−theta)−u^theta` has derivative
`theta(1−u^(theta−1))`, negative below one and positive above it,
and value zero at one. Apply the resulting Young inequality to ratios
of the two normalized positive finite arrays and sum. This establishes
the exact finite Hölder instance without an unread measure-theoretic
theorem. The actual set of complete paths is nonempty; even an empty
set would make the counting inequality trivial without normalization.

The negative-c moment is the accepted PAID moment, not a fictitious
feasible raw degree-two row. It is a second absolute sum on the same
path set. With fixed `1<K0<K`, strict geometric-mean inequalities give
`1<K0<H<K`. Constants are fixed before n and the arrangement. No
per-path prefactor, factor four, or uniform-path sampling enters.

## Reconstruction of PM9C and all strict comparisons

Improving K alone would not improve current PM8 J. I therefore checked
the complete Section 4 comparison to the actual accepted J2≤J.
Use positive `A=ln(K/K0)`, `B=ln chi`, `t=−ln(1−kappa/2)`,
`h=−ln r`, and `delta=min(1,A/B)`. The accepted eta and J2 give

    ln(K/J2)=delta*t*h/(8 ln 2),
    ln(K/H)=A*q/(2B+q).

For the first equality, `ln rho=−2h` and
`eta=delta*t/(8 ln 2)`; this checks the factor two explicitly.
The second uses `1−theta=q/(2B+q)`; the denominator is a SUM.

From accepted `ell<19/9` and `rho≥2/ell`, one has `rho>18/19`.
The exact numerator `18*1296−19*1225=53>0` proves
`r>sqrt(18/19)>35/36`. Also V>1 gives `kappa<1/16`.
Thus `x=kappa(1−r)<1/576`. Integrating `1/(1−u)` gives
`−ln(1−x)≤x/(1−x)`, so `q<1/575`. In the other direction,
integrating `1/(1+u)` gives `ln(1+y)>y/(1+y)` for y>0.
With `y=149/61731`,

    B>149/61880>1/575,

and the exact last cross-product numerator is
`149*575−61880=23795>0`. Therefore `0<q<B`. These are hand
rational comparisons, not rounded logarithms or a parameter search.

Similarly, `h≤(1−r)/r` and r>1/2 imply `1−r>h/2`.
Hence `q≥kappa(1−r)>kappa*h/2`. The same upper integral inequality
gives `t≤kappa/(2−kappa)<16*kappa/31`, so

    q>31*t*h/32.

Both branches of delta satisfy `A≥delta B`. Since `2B+q<3B`,

    ln(K/H)>delta*q/3>31*delta*t*h/96.

The integral of `1/x>1/2` over `1≤x<2` proves `ln 2>1/2`.
Consequently

    ln(K/J2)<delta*t*h/4=24*delta*t*h/96.

All common factors are strictly positive; 31>24 gives
`ln(K/H)>ln(K/J2)`, and exponentiating in the correct direction
gives `H<J2≤J<K`. The argument covers delta=1, delta=A/B, and
their equality boundary. No endpoint q=0, h=0, t=0, rho=1, or
kappa=0 is admitted by the accepted constants. Arbitrarily small
positive gaps cause no loss of the strict inequalities.

Finally, accepted canonical insertion is
`B_(n+1)≤gamma_n B_n`, `B2=1`, `C(n)=B_n` in the fixed-polygon
marking convention. Substitution of `gamma_n≤H^n` and summation from
2 to N−1 gives

    log2 C(N) ≤ [N(N−1)/2−1] log2 H,       N≥2.

At N=2 this is the empty product and exponent zero. The finite bound
uses ≤, not a spurious strict inequality there. Division by N² gives
the limsup upper bound `(1/2)log2 H`, strictly below the current
`(1/2)log2 J`. There is no factorial, relabeling quotient, history
count, or accumulating factor four. This does not identify the exact
limit, a matching lower bound, or an effective all-scale upper R.

## Adversarial/source/integrity disposition

I tested the inferences symbolically at b=0, c=0, zero trials, one last
ordinary block, trial endpoints shared by later starts, reverse double
flags, variable trial counts, reconvergent prefixes, arbitrarily small
positive gaps, both delta branches, and N=2. None supplies a
counterexample within the accepted actual-arrangement hypotheses.
Removing those hypotheses, replacing b by a forward-only number,
merging tree prefixes, using a raw unpaid row, or normalizing by an
unknown uniform-path count would change the argument; none is done.
No enumeration, CAS, numerical optimizer, test run, or mathematical
executable supplied these checks.

The separate sources MD/JSON record complete accepted input reads,
fresh original-source passages, and unread external foundations. In
particular, the MIT zone manuscript is context only and supplies no
PM9 theorem; an unsuccessful literal term search cannot establish
nonoverlap or priority. Finite flow, Cauchy, Young, and logarithmic
inequalities are reconstructed here rather than delegated to an unread
probability theorem. I do not claim to have re-proved the older sharp
zone theorem or every representation foundation.

The only new executable is reviewer metadata code checking bytes,
declared records, scope labels, and counts. It does not evaluate any
mathematical assertion, execute author code, traverse pending peer
packets, or replay an old freezer. All necessary declared old
fingerprints and accepted suffixes are checked, with immutable parent
metadata bound compactly instead of copying historical inventories.
The immediately preceding own R14 checkpoint binds 793 own historical
paths; this ten-file review will bind 803 transitively. Full final model
readback of all new payloads/code/generated metadata, manifest readback,
and a separate read-only verification are required before identity-only
handoff. All author, prior, shared, Git, and cache bytes remain unchanged.
