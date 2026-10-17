# 2019 return research log: alternating blocks and nonregularity

2026-10-17 UTC. **Candidate proof - unverified.** Constructor
`review_2021_reasoning_j15_r2`, requested gpt-6.1-sol/max; effective
readback unavailable. The exact official B4(b) rate remains unknown.
This log accompanies complete proposed NR1–NR4, requiring two fresh
OTHER nonconstructor whole audits. No reviewer acceptance is claimed.

## Scope and inputs actually read

The coordinator assigned a conceptual2019 checkpoint after the whole
2024 CP review froze, while a different actor completed an unrelated
global2017 construction. No2017 active global file or future2024
generalization was read during this task. Ownership was restricted to
`problems/2019-B4/notes/reasoning-return-r3-*`; no shared file was edited.

Read AGENTS, the full2019 official(b) statement and local statement,
the existing proof of growth existence and marked-context comparison,
the second-pass acceptance register and all three complete mathematical
notes (canonical renewal, rigid collisions, staircases), the full
bounded-separation/cap3 proof and acceptance, and the full reviewed
moment/tail body and acceptance. Initial combined tool output truncated
part of the moment/staircase material; it was reread in bounded pieces
before treating it as complete. Also read the full deep primary-source
report, its source cache metadata, references/research, and the two-tape
generator-direction note. No old certificate was executed or extended.

Fresh primary browsing checked the actual official B4(b), Mohri §4.3
bounded-delay definition and finite-residual hypotheses, and the
queue-action paper's definition/theorem4.1 and the product embedding
context. Those papers concern different hypotheses/equivalences and
are methods/context, not theorem imports into NR1–NR4.

## Reasoning sequence and rejected inferences

1. The accepted renewal root and first-moment bounds already give a
   converging enclosure. Merely summing more known factors or increasing
   the separation cap would not address exact closure, so no such job
   was started. No new numerical trial for lambda was selected.
2. I first asked whether a long alternating history block is a universal
   barrier for bounded-separation witnesses. Halfway through
   `(RL)^(2D)`, an upper path of separation at most D would have extra
   left bits all beta and missing right bits all alpha. Equal source
   symbol counts make this impossible. The RR/LL endpoints of true
   minimal factors then give a cap-dependent bridge and DFA reset.
3. The accepted staircase has a unique other history. Its height
   difference has maximum n+1. This provides a missed factor at EVERY
   finite cap, rather than relying on finitely observed widths. Combined
   with an irreducible finite graph, this proves a strict gap above
   lambda for each cap. It does not prove strict decrease at every
   consecutive cap.
4. To strengthen the barrier without imposing any separation cap, I
   counted beta symbols supplied by the fixed history prefix a before
   `(RL)^m`. If K0 are on the right tape, at time `|a|+2K0` a strictly
   upper witness cannot have passed the entire constant-beta left block
   when m>2K0; it would already exceed the available source budget.
   Remaining inside it forces surplus d<=K0, after which its right
   consumption is past V_a and the combined beta count exceeds the
   source by d. This gives the unrestricted prefix bound NR1.
5. A regular subset of actual F with arbitrarily long RL powers would
   pump such a block while keeping a,b and their source phase fixed,
   contradicting NR1. The accepted staircase has unbounded RL powers;
   hence F is nonregular. The exact minimal-forbidden operation gives
   nonregular K, and elementary projection/right-quotient arguments give
   the two stated representation consequences.
6. Any regular G subset F therefore avoids a fixed RL power. That power
   is a universal bridge, which resets the MINIMAL avoiding DFA to its
   initial right language. An actual missing f in F minus G deletes an
   edge from an irreducible higher-edge graph; the finite Perron
   comparison gives a strict rate gap. This extends the older finite-list
   obstruction to all regular actual-obstruction subsets.

No step assumes that every minimal bad factor has exactly two histories.
That is used only for the accepted staircase in the explicit width
calculation. The unrestricted budget lemma uses the accepted existence
of one strictly upper witness and applies also when a context has more
histories. This distinction preserves the known three-history examples.

## Failed stronger conclusions, deliberately not adopted

- A nonregular language can have a rational counting series or algebraic
  growth. NR2 does not settle rationality/algebraicity of F(z), C(z) or
  lambda. No algebraic numerical guess was made.
- No-finite-presentation or sparse staircase evidence alone was not used
  to assert nonregularity. The NEW fixed-prefix budget and pumping
  contradiction are the additional argument.
- The cap bridge does not imply a uniform bridge for the full K. Indeed
  h_n contains `(RL)^(n-1)` and is minimal bad; cutting immediately around
  that proper block supplies canonical outside factors while the full
  word is bad. No fixed power of RL bridges every pair of words in K.
- The reset assertion concerns minimal follower-state DFAs. I did not
  infer that the unminimized residual-subset monitor literally reaches
  its empty state after the same block; unmatched future guesses can
  distinguish raw subset states with the same right language.
- A queue transformation equality tests all initial FIFO contents. It
  has not been identified with equality of this pair of chronological
  tape outputs. The published queue normal form cannot be transferred
  solely because both settings involve two projections.
- The ordinary binary-string language B need not share the regularity
  status of K. Accepted polynomial-size marked fibers equate growth,
  not formal-language classes.

## Commands and operational record

Read-only commands used `rg --files`, `cat`, and `sed -n` on the named
files, with exact web opens/searches listed in the source record.
`apply_patch` created only the assigned new prefix. Python was used only
for administrative input fingerprinting and the freeze command:

    python3 problems/2019-B4/notes/reasoning-return-r3-freeze-v1.py

It hashes and serializes immutable inputs, source bytes and older own
packets; it is not a mathematical computation. No histories, queues,
cap automata, sign fractions or root approximations were enumerated.
There was no native mathematical child, CAS, installation, network
download, contact, charge or access workaround. No PID cleanup was
needed and no other worker process was touched. All existing files
and candidate versions remain unchanged; no Git/spawning operation
was performed.

Direct authoritative telemetry at task start was31% total weekly use,
10080-minute window, reset1792745187. The90%-TOTAL ceiling and reserve
remain applicable; no automatic new-window spending is authorized.
The candidate/obligations/source/log/input/manifest packet must freeze
before reassignment to a fresh independent review in another year.
