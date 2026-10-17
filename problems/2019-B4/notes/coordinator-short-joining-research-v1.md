# A precise short-joining route to the normalized-count regime

2026-10-17 UTC. **Research lead / unverified candidate deductions.**
Root construction, no new annual result or novelty claimed. Any proposed
proof requires TWO OTHER initially blind whole audits before promotion.
This does not change the frozen/accepted R7 result or either old audit.

R7 proves c_n/c_(n-1)->lambda and s_n=c_n/lambda^n increasing, with
delta=2-F'(1/lambda)>0 exactly when s_n is bounded. One substantive
remaining question is a uniform joining property for the ACTUAL canonical
history language K, not a finite-cap substitute:

    (J_C) There exists a FIXED finite C such that for every u,v in K,
          some history w of length<=C has uwv in K.

**Conditional deduction, not an established J_C theorem.** If J_C holds,
choose one such bridge for every pair of words of lengths n,m. For a
fixed bridge length k, the resulting word of length n+m+k determines
u,v by their known cuts; the selected assignment is injective into the
disjoint union over k. Thus

    c_n*c_m <= sum_(k=0)^C c_(n+m+k).

Divide by c_m and let m tend to infinity with n,C FIXED. The accepted
consecutive-ratio limit gives c_(m+n+k)/c_m->lambda^(n+k), by a finite
product. Hence

    s_n <= sum_(k=0)^C lambda^k for every n.

R7 would then imply delta>0, with the finite normalized limit and
delta>=1/[R*sum_(k=0)^C lambda^k]. This supplies no exact value of
lambda, local analytic continuation, original b-ratio theorem or
unconditional positive defect until J_C is actually proved.

## Why the shortest guess fails

The hand pair u=RRLRR,v=LLRLL is canonical under the exact accepted
small-obstruction description: neither contains RRLL, and no other
minimal bad word has length below12. Every bridge of length at most2
fails. Empty,L,R,LL,RL,RR introduce RRLL across a boundary. The one
remaining bridge LR gives exactly the known minimal bad word
RRLRRLRLLRLL. Thus J_2 fails. This is a particular two-word obstruction,
not an obstruction to all bounded joining.

For these same u,v the bridge RLR instead gives
RRLRRRLRLLRLL, length13, which avoids RRLL and the length12 minimal
word. The old COMPLETE list through24 confirms canonicality at this
length. This motivates C3 as a question, not a theorem. Minimal bad
words with long interior runs and staircase patterns prevent a casual
fixed-buffer or run-parity argument. A single constant bridge fails
for other pairs: a minimal bad word can often be split around it into
two canonical proper factors. The bridge must be allowed to depend
on both inputs.

## ONE bounded diagnostic, and its limits

Root ran one targeted counterexample search, not another growth or
obstruction enumeration. It used the already accepted COMPLETE143-factor
list through24 from secondpass-full-obstruction24-v2.json and examined
all ordered pairs of length8 canonical words, with bridges of length0..3.
Every tested concatenation has length<=19, within the old exact list.
It examined31329pairs and found NO pair defeating all those bridges.
This finite absence proves NO unrestricted joining theorem. It does
not distinguish the actual defect/mean regime or justify a larger scan.
The next step is a conceptual scheduling/splicing argument or an explicit
structural counterfamily; no automatic cap enlargement is planned.

Exact script/output/stderr/job are in computations/
coordinator-short-bridge-diagnostic-v1.{py,json,log} and
coordinator-short-bridge-diagnostic-v1-job.json. Command:
`.venv/bin/python problems/2019-B4/computations/coordinator-short-bridge-diagnostic-v1.py`.
Parent used subprocess.communicate(timeout=10), recorded childPID18934,
and reaped exit0 in0.076304seconds without a timeout. The child used
0.047052seconds. No package installation, CAS, native operation,
older-certificate regeneration or process-wide cleanup occurred.
The accepted source-list SHA is recorded in the JSON. The code is
diagnostic evidence, not an unrestricted proof.

This lead and the hand J2 witness are UNVERIFIED until the normal whole
review process; the accepted annual enclosure and unresolved exact
lambda remain unchanged. No preliminary part(a) is reproduced.
