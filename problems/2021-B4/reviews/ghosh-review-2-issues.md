# Ghosh source audit R2 - frozen blind issue log

2026-10-17 Australia/Brisbane. Independent initial report. No other reviewer
conclusions/shared issues were consulted. The proof/note author owns repairs.

| ID | Severity | Location | Finding and necessary disposition |
|---|---|---|---|
| R2-GH-01 | Substantive source-proof blocker | Universal PDF p. 19, Lemma 4.5, after (4.23); current HTML same passage | The coefficient descent discards a term known only to lie in p, rather than I. A polynomial unit over the Artinian local quotient can have a nonzero nilpotent X-coefficient. Both candidate examples check exactly as abstract local examples. Supply a specialized argument proving the needed f_i vanishing or another local-contraction proof. No counterexample to the actual characteristic-zero lemma or Theorem A is asserted. |
| R2-GH-02 | Substantive source-proof blocker | Universal PDF p. 9, Proposition 3.3, after (3.8); current HTML same passage | Inverting a zero divisor need not kill the whole ring. The presented nonzero localization does not prove t is regular in the m-times-J quotient. Supply torsion-freeness/saturation for the actual H_i. Both candidate generic models are valid. An additional actual-family characteristic-11 test failed to contradict the claimed equality and is preserved as such. |
| R2-GH-03 | Substantive source-proof blocker | Universal PDF pp. 12-13, Lemma 3.7; current HTML same passage | Fiber of total projective closure need not equal projective closure of affine fiber. The incidence model verifies finite special affine fiber with an escaping point at infinity. Properness of total projection does not exclude that parameter from the infinity image. Supply a no-escape/properness argument for the actual Abel-Gontcharoff map. Remark 3.8 covers some but not all witness tuples. |
| R2-GH-04 | Required metadata correction | Candidate full-context note, Sources/version paragraph | The exact specified 22-page cached PDF and fresh versioned PDF both print internal Date: March 24, 2026. Current HTML prints August 24, 2026; arXiv abstract history and PDF margin say v2 March 21, 2026. Fresh primary TeX contains date-today, so these internal strings are rendering dates. Correct the note's assignment of the August date to the cached PDF; distinguish the artifacts without inferring a new arXiv revision. |
| R2-GH-05 | Scope guard, retained | Any resulting integration or source-status update | Generic models do not match all specialized derivative/global induction hypotheses. No actual characteristic-zero CA counterexample, theorem refutation, or full contest solution follows. Keep arXiv2402.18717v3 finiteness separate from arXiv2501.09272v2 universal claim. |

No issue is marked resolved in the source proof. R2-GH-04 is a concrete repair
to the candidate note; the remaining findings define the limit of what this
review supports. The coefficient-query note's deliberately provisional
wording is appropriate. No source/candidate proof was edited and no result
was promoted.
