# Constructor adversarial checks and issue ledger

2026-10-17 UTC. **Candidate proof - unverified.**
Constructor checks do not count as either required fresh whole audit.

## Proof-critical checks

**C1: Which tracks are being compared?** OP1 uses projected rank identities,
not the original labels routed through smoothed contacts. At the instant
of an erased original swap, omitting earlier same-color swaps leaves
exactly the same color list at each position. The two projected tracks
there are the two neighboring current ranks of that color. An external
projected identity has a well-defined current position and crosses each
compared projected track at most once. This prevents a hidden identity
switch in the crossed-set proof.

**C2: Does equality of counts hide an order choice?** The proof gives
equality of SETS, hence counts, not equality of per-track crossing orders.
The latter orders can differ; the exact A,A,B,C example in main3 shows
this. The partner gap index is unique even when those orders differ.
No assertion that the physical gap segments share a point is made.

**C3: Are signs/interleavings still missing?** Keeping only x_r would be
insufficient. The code records the WHOLE internal commutation class A.
Its full port-ID list on each rank determines the -/+ interleaving.
After every + is located and its - partner receives the same gap index,
each full list either has nondecreasing indices (as every actual code
does) or is invalid. There is no further choice inside a gap.

**C4: Is kth matching global or local?** For adjacent ranks r,r+1,
the lth + on r and lth - on r+1 identify the same internal event.
These IDs are invariant because a commutation never exchanges two
events on one rank. Multiple contacts of one rank pair are permitted.
No arbitrary matching or S! pairing factor is introduced.

**C5: Does a representative sweep leak into the class code?** The sweep
only proves equality of canonical prefix sets at actual contacts.
Q, its per-track crossing orders, A_i and every plus-gap count are
invariants under the accepted DC decoration map. Reconstruction returns
the complete decoration, then the original-label event poset. It does
not store or count a selected linear extension.

**C6: Does the common-prefix bound assert sufficiency?** No. Matching
prefix sets, full per-track port-list compatibility, global acyclicity
and a simultaneous lifting can impose additional restrictions. Equation6
counts many invalid records. Only actual inputs need injective recovery.
It is expressly not an arbitrary disk recoloring/extension theorem.

**C7: Finite endpoints.** a=0 gives one allowable gap; F_0=1. m=1 has no
host tracks and no ports. S=0 forces every m_i=1 and E_+=0; H is defined
as1 separately. If S>0, E_+>=1 and binom(E_++S-1,S) is valid. D=1 uses
the sharp weighted bound for equality; the looser global composition
bound is not asserted to be equality.

**C8: Normalization.** All limits in main5 are taken with D fixed.
The internal sum is L/D rather than 2L/D or a discarded lower-order
term. There are S plus ends, yielding the ratio1/(2D-1) and total
binomial scale1-1/(2D). No D=D(n) substitution or effective threshold
is inferred. The U substitution is a separate accepted input.

**C9: Small hand example.** The successive projected lists are
1234,1324,1342,1432,4132,4312. Thus A_2 sees B,C and A_1 sees C,B.
The only matching prefix indices are0,2. Prefix s_1 or suffix s_3
provides two full reversals. DC's invariant port indices distinguish
them, so the fiber exactly meets the refined two-record bound.

**C10: Auxiliary even-word check.** The OE layer sends original positions
around (1,3,...,m-1,m,m-2,...,2); t=m/2 steps give reversal. The total
length is inversion length. Thus the old almost-balanced degree vector
is genuinely realizable, not an arbitrary integer relaxation. Its
near-maximal old weight is a per-class obstruction only.

## Open/failed-inference ledger

| ID | Status | Exact disposition |
|---|---|---|
| GV2-OPEN-01 | Open; not a theorem claim | No effective finite p modulus for any fixed-D balanced count is supplied |
| GV2-OPEN-02 | Open; not a theorem claim | Earlier E and R remain unproved; direction-error computability does not prove L computable |
| GV2-OPEN-03 | Open; not a theorem claim | No quadratic-scale evaluation/distribution theorem for Q-dependent common-prefix weights |
| GV2-FAIL-01 | Rejected by proof | Improve old Jensen product uniformly by delta m^2 using only actual degree feasibility: the explicit even brickwall classes prevent that |
| GV2-FAIL-02 | Rejected as unsupported | Treat common-prefix equality as sufficient for inserting arbitrary internal classes |
| GV2-FAIL-03 | Rejected as unsupported | Infer an effective rate from existence, qualitative UR_D, or the sharper D error |
| GV2-FAIL-04 | Not used | Coordinator's integer-grid/SFT possibility lacks exact encoding, normalization and entropy/boundary interface |
| GV2-OPS-01 | Operational interruption; no mathematical import | Felsner–Valtr escalated curl stalled awaiting tool/approval result and was interrupted; no file/hash/PID success claimed |

There is no unresolved AUTHOR-observed defect in OP1–OP3 at this freeze;
that is not an independent pass. All48 inferences remain subject to the
two required whole audits. Value/novelty/full2017 claims are absent.

