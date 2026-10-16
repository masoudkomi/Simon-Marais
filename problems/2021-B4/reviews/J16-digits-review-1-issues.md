# R1 adversarial issue log for the complete J16 L1--L4 packet

2026-10-16 UTC. Initial blind audit. No reviewer-2 conclusions read.
All items below are closed by reconstruction or exhaustive verification;
no candidate-author repair is requested. This is a review recommendation,
not the coordinator's promotion decision.

| ID | Challenge | Resolution and evidence |
|---|---|---|
| R1-01 | Does T2 assume all roots are rational, or infer a rational Newton factor without justification? | T2 is an explicitly accepted rational-witness result. Its exact rational quotient after the four rational roots is monic degree 15, with the fifteen fractional-valuation roots, and Eisenstein. Only that quotient is used. |
| R1-02 | Could unequal small-root valuations allow cancellation in c3 or invalidate the width-one derivative lemma? | For r<s, c3 has unique minimum -b0*u and valuation 1+r. The edges are exactly (2,1+r+s)--(3,1+r)--(4,1); each has only two minimum terms. The accepted lemma applies at i=2,3<19. |
| R1-03 | Are root ratios wrong when H3 may use zero, or when residues agree? | Direct quartic Hasse differentiation gives every displayed value. H3(0)=-(U+V) is retained. H2(0)=UV is a unit in equal-valuation cases. Equal residues are not discarded by a closeness test. |
| R1-04 | Does an absent flag really imply a failed center equation? | It does for the actual canonical mask, which chooses the center whenever available. Extra formal families whose center also vanishes merely enlarge the necessary cover. |
| R1-05 | Could q0 vanish and leave an unbounded valuation case? | All 88 exact q0 values are nonzero; 84 have valuation 1 and four valuation 2. The complete independent binary enumeration agrees with the accepted 88-mask list. |
| R1-06 | Can omitted inactive labels alter later digits? | They can, so every inactive label is restored independently. Unique full keys expand 768 projected branches into 840396 cases. Only the constant Jacobian is compressed, using the proved zero linear coefficients. All later constants use full assignments. |
| R1-07 | Are the three E equations integral uniformly, including nu=2? | Checked constant prerequisites make the low quotients integral. Every higher middle term has the explicit factor 19 and enough q powers. The denominator beta18=10 is a unit. The exact general derivation precedes constructor data. |
| R1-08 | Could the exceptional c19=-20 or c20=1 terms lose a digit? | Both are included in every independent full monic-division evaluation. Their parameter degrees also establish the theoretical valuation bounds after normalization. |
| R1-09 | Were a quadratic term at nu=1 or a carry at nu=2 missed? | Direct division, without the candidate's scalar shortcuts, reproduces all 840396 L3 constant vectors and the entire scalar stream hash. General precision uses coefficient modulus 19^(nu+k+1) and remainder modulus 19^(nu+k+2). |
| R1-10 | Does a rank-deficient system need branches that the implementation silently drops? | Cramer's rule/free-coordinate enumeration and separate RREF agree at every input. Every consistent rank-1 system generates all 19 digits. All 249356 rank-1 precision-2 nodes are independently checked inconsistent. |
| R1-11 | Is T1 pruning justified when a formal variable is still required to be a root? | An unused label means the other three rational roots already witness every derivative, including H1 at 0 and H19 at 1. T1 forbids that covering set regardless of the unused variable's root condition. Exactly 14248 initial assignments are pruned. |
| R1-12 | Could a missing, repeated, or reordered certificate hide a branch? | Expected-layer key sets are generated independently. Every input is removed exactly once; every child is generated independently; every saved node stream equals the complete next set. No missing or duplicate key occurs at any level. |
| R1-13 | Could exact precision-four states, fractions, or rank-two bounds be wrong? | All 90 are rebuilt with full integer recurrence and exact monic division. Every coefficient, F coefficient, remainder, Fraction, matrix and minor matches. All matrices have rank 2, proving at most 90 future states per layer. |
| R1-14 | Are final inconsistency certificates merely sampled or based on a sign error? | All 104 systems are reconstructed exactly. All 361 digit pairs are checked for each. Every signed-minor vector annihilates both columns; 76 precision-four and 14 precision-five failures have nonzero obstruction, while the 14 passing rows have zero obstruction. |
| R1-15 | Do benchmarks, target changes, or timeouts masquerade as complete results? | Benchmarks remain explicitly incomplete and contribute no exclusions. Full independent runs finish under fixed external caps. The independently covered tree is 840396 -> 361194 -> 2026 -> 90 -> 14 -> 0, empty at precision six before fixed target eight. |
| R1-16 | Do artifact hashes establish anything beyond frozen-byte integrity? | All 46+53+14 artifact records match, but acceptance is based additionally on the independent mathematics, complete key coverage, full coefficient and residue reconstruction, all fibers, and exact final obstructions. |
| R1-17 | Does this establish degree 20, another field, or the annual classification? | No. The supported consequence is only the rational J16 exclusion under accepted normalization/T1--T2. The other 684 necessary masks remain outside this candidate. |

There are no unresolved substantive objections or requested mathematical
repairs. Neither finite agreement alone nor this single audit supplies
the required two-review promotion gate.
