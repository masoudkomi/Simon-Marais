# Sole-H4 review1 issue ledger

2026-10-16 UTC. Initial blind review of candidate SHA-256
`042b15f45a39f6773ec8e5eea6c4294eab5e794e98a961534b899ef2568b508e`.
No peer single-center review or conclusions read. All entries below were
resolved analytically within the initial audit; none requires author repair.

| ID | Potential issue audited | Resolution | Status |
| --- | --- | --- | --- |
| H4-R1-01 | Official hypothesis might permit algebraic rather than rational witnesses | Official B4 page2 requires a common root in Q for every derivative. Candidate preserves this. | Closed, no defect |
| H4-R1-02 | D1 might incorrectly force the third small root into Q | Galois argument gives Q19 only; candidate never treats this as Q. At least2 distinct globally rational small roots are an accepted T1 consequence. | Closed, no defect |
| H4-R1-03 | D2 or its width-one applications might miss valuation ties | Reconstructed unique-minimum, two-minimum and all-distinct cases; ratio sets disjoint, lower exponents2,3,4<19. Ties and repeated residues covered. | Closed, no defect |
| H4-R1-04 | Degree-five scaling might divide by a nonunit improperly | Direct B(qT)/b0 coefficient valuations are positive in every nonconstant degree; resulting G is integral and Hasse scaling is exact. | Closed, no defect |
| H4-R1-05 | H3 split might assume actual-root uniqueness from residues | The split first covers zero, any slot of residue1, and any other slot; distinctness follows only after solving. | Closed, no defect |
| H4-R1-06 | Denominator2x-3 or quadratic degeneracy could discard a branch | Vanishing denominator leaves -1/2!=0. Leading quadratic coefficient12!=0, discriminant2 nonsquare. | Closed, no defect |
| H4-R1-07 | Cubic factorization might be asserted over integers | Candidate explicitly factors over F19; integer differences are19x+38. | Closed, no defect |
| H4-R1-08 | Nonzero-root H2 formula could erroneously admit zero in caseI | H2(F)(0)=-z!=0 handled separately; q2's zero root is irrelevant. | Closed, no defect |
| H4-R1-09 | Necessary reduction might be promoted to actual common-root existence | Existence comes from full contest hypothesis; residue tests exclude all but a unique actual slot. No sufficiency inference used. | Closed, no defect |
| H4-R1-10 | CaseIII global rationality might be inferred from local splitting | Unique3R slot is rational because the actual rational H3 witness must occupy it. No assertion about unselected slot. | Closed, no defect |
| H4-R1-11 | H4 center conclusion might overlook zero or fractional roots | Nonzero s excludes zero; linear H4 roots miss all small slots; fractional roots cannot be rational. Center is the only remaining eligible witness. | Closed, no defect |
| H4-R1-12 | Result might be represented as mask/full degree exclusion | Candidate and report state necessary classification only; no lifts or branch emptiness asserted. | Closed, no defect |

Unresolved substantive objections:0. Requested repairs:0. Recommendation:
accept the stated partial classification and forced H4 center condition,
after coordinator reconciliation with a second independent whole audit.
