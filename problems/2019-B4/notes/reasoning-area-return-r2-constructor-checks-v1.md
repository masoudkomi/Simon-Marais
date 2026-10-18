# AR2 constructor reconstruction and adversarial checks

2026-10-18 UTC. Candidate proof - unverified. These are manual checks,
not two independent audits. No mathematical executable was run.

The main proof was reconstructed at the level of an arbitrary full
legal history. Its key observation is exact: for u=(01)^a the source
and next-left parity agree iff j is even. This proves the atomic RR
constraint rather than presuming it from a chosen schedule. The final
odd R exception is checked separately and forces all left letters to
have been read. This also prevents a spurious free L move after that
last right letter.

For every cut (i,2k), I checked the two minimum-cost paths with their
actual start/end clock parities. Prefix cost A_k(p) and suffix cost
B_k(p) each have parity p; surplus left moves can therefore be placed
in pairs independently on both sides. This is the important sufficiency
step for GLOBAL viability. For an odd-right cut, the preceding and
succeeding R are forced; the suffix witness can be chosen to start
that pair because its clock-change cost is zero. No globally unviable
height match is included.

At the neighboring augmented types00, the two parity costs are0 and2;
at11 they are2 and0; at01 and10 both extra costs are0. Thus the even-j
row counts are2d+1 for equal neighbors and2d+2 for unequal ones.
The total number of unequal neighboring types is2r. Odd-j rows always
have d+1 vertices. Adding gives(3b+2)d+2b+1+2r, exactly N+1+3bd.

Hand endpoints: b=0 gives the sole L-only path; a=0 forces every right
pair to be01; d=0 gives the minimum schedule and area N+1. For a=b=1,
epsilon0 gives the pair(01,01) with8 viable vertices (the3x3 grid except
(1,1)), while epsilon1 gives(01,10), its sole LRRL history and5
vertices. These are two explanatory hand checks, not a finite search
or a certificate extrapolated to unrestricted parameters.

The exact tail uses a set bijection, not a weight surrogate: deleting t
left pairs keeps epsilon fixed and changes exactly d. Both extension
maps in(17) add two right macro letters and one left pair, so their total
parameter changes by3. Appending10 creates at most one1-run even when
epsilon is empty. Their images are distinguished by the two last macro
letters, and the fixed left-length decrement recovers the original.
No input histories are counted as different outputs.

The high-area tail bound remains true when its integer threshold exceeds
m (the event is empty). At m=0, both parities have one output and d=0;
the mean estimate is valid, while the large-N probability assertion
does not invoke that degenerate case. The rational GF is derived from
an unambiguous run decomposition and is not used to guess an asymptotic
or a numerical value.

For the counterfamily, I checked the general word identity
beta((10)^k1)=1(0011)^k0, all interior run lengths, and the exact
degree8k+4. A preliminary attempted repetition(100110)^k introduces
101 across joins; it is NOT the irreducible right word used in the
theorem. The corrected displayed family uses1(0011)^k0 directly, so
the proof never denies those joins. Its first useful k is1, since k0
would give the actual reduced pair(01,10). The viable-area density is
6/64=3/32 and not the earlier exploratory9/100 from a different family.

AR4 is deliberately weaker than an output-count theorem. The selected
visits are moments immediately AFTER left moves of one fixed incoming
bit, so both heights and the source phase match exactly. The discarded
initial vertex costs at most1. The q-1 intervals have disjoint history
edges, and those longer than integer L consume at least L+1 moves each.
The right-empty qualification is retained and illustrated by an actual
canonical flat path.

All48 obligations have constructor PASS dispositions in the separate
ledger. The full-R_N mass statement remains OPEN, and no convenient
subclass is substituted for it. No author repair is pre-authorized from
future review findings; a substantive objection requires a new full
version, preserved old bytes, and both affected audits.
