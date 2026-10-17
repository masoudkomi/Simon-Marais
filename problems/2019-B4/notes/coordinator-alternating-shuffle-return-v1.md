# Alternating shuffles: a height formulation and a failed greedy rule

2026-10-17 UTC. **Research continuation — unverified.** This does not evaluate lambda or alter the accepted NR1–NR4 theorem. The earlier `coordinator-two-tape-directions.md` already records the four-generator context monoid; this note adds a geometric representation and a concrete obstruction to one proposed simplification.

For a word u, let H_u(i) be the number of0s minus the number of1s in its prefix of length i. Let u,v be chronological output tapes. A shuffle of u,v equals the alternating source0101... if and only if there is a north/east path from(0,0) to(|u|,|v|) in the integer grid such that every visited vertex(i,j) satisfies

    H_u(i)+H_v(j) = 0 when i+j is even,
                    1 when i+j is odd.                (AS1)

Proof: at each source time t the consumed tape prefixes together contain exactly the source prefix. Their bit imbalance is0 or1 as displayed. Conversely, along a path satisfying these equations, the height sum increases by1 at every even-to-odd step and decreases by1 at every odd-to-even step. The consumed letter is therefore0,1,0,1,..., proving the desired shuffle. A final even length requires total imbalance0; this endpoint condition by itself is insufficient. For the complemented source, reverse the signs in AS1. Chronological left reversal remains essential when translating back to physical contexts.

AS1 is an exact membership reformulation, not a count of distinct pairs. Dynamic reachability of a GIVEN pair in a finite rectangle is easy; summing all admissible pairs without counting multiple paths remains the growth problem.

A tempting rule is to consume a whole01 from the left tape whenever available at an even source time. This fails on the concrete pair

    u=011,  v=100.

The two-step blocks B,C,C, with B=(0,1) and C=(1,0), yield exactly that pair: the history LR RL RL routes source010101 to it. But consuming the available left prefix01 first leaves u=1,v=100 while the next source bit is0. Both heads are1, so this greedy branch is dead. The alternative uses the right tape's leading1 earlier. This is a hand-checked counterexample to that greedy choice, not a counterexample to an accepted theorem.

The visited grid is a two-level strip for the separable function H_u(i)+H_v(j). Local forks, inaccessible components and reconnections encode the ambiguity. A useful next target would be a proven contour/frontier description permitting exact counting, or an unambiguous recursive specification. Neither a finite frontier nor a context-free grammar is established here. Accepted nonregularity of the least-history language alone does not rule out an algebraic series or a different normal form.

Literature check: directly read Amarilli–Paperman, [Topological Sorting with Regular Constraints, ICALP2018](https://paperman.name/data/publi/10.4230.LIPIcs.ICALP.2018.115.pdf), §2's constrained-shuffle definitions and §3 Theorem3.6 with its displayed reduction. Their input permits a variable number of strings. Its NP-hardness for target(ab)* does not transfer to this fixed-TWO-tape counting problem. It supplies terminology and a warning about the number-of-inputs hypothesis, not an entropy theorem. No full external paper proof, mathematical program, enlarged history enumeration, novelty, or full solution is claimed.
