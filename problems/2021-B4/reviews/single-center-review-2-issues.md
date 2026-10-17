# Joint initial issue ledger: single-center review 2

2026-10-16 UTC. Completed blind to peer sole-H4, sole-H2, and single-center reports and conclusions. Frozen with the full reconstruction and source record.

Candidate fingerprints:

- Sole-H4: 042b15f45a39f6773ec8e5eea6c4294eab5e794e98a961534b899ef2568b508e.
- Sole-H2: a21d53ab434ea715b85cca9bcf98c715a1522f4faa33d1977c1ad9411b7f9d39.

**No blocking or substantive defect found in either candidate; no repair requested.** The entries are adversarial questions closed by reconstruction, not a record of errors previously present in the candidates.

| ID | Candidate/location | Attack point | Initial disposition |
|---|---|---|---|
| SC2-01 | Both, accepted input sections | Using D2 when a noncenter choice need not mean center nonvanishing | Closed. Both explicitly assume the two relevant center values are nonzero. D2's at-least-two-center conclusion therefore forces equal valuations. |
| SC2-02 | Both, reduction to \(F\) | Nonunit scaling or high-degree terms might survive | Closed. \(f(qT)/(q^5b_0)\) is integral and \(B(qT)/b_0\equiv1\); the explicit coefficient valuations are given in the report. |
| SC2-03 | Both, available witness list | Local roots could be confused with rational contest witnesses | Closed. Fractional valuations exclude fourteen slots. D1 places all three other slots in \(\mathbb Q_{19}\) but does not place all in \(\mathbb Q\). The algebra allows a superset, then uses actual witness existence and unique slots. |
| SC2-04 | Both, Hasse formulas | Sign, Hasse normalization, or invalid \(H_2\) formula at zero | Closed. Elimination of \(z\) gives \(A(9A^2-5sA+2t)\) only at nonzero cubic roots. Zero is checked separately as \(-z\). |
| SC2-H4-01 | Sole-H4 lines 71–93 | \(H_2\) may use zero; repeated residue 1 could be omitted | Closed. \(z\ne0\) excludes zero. The residue-1 branch includes a priori repeated slots and derives distinct \(1,12,16\). |
| SC2-H4-02 | Sole-H4 lines 95–119 | Variable denominator or cubic factorization may discard roots | Closed. \(2x-3=0\) contradicts the original relation. The unreduced cubic and its modulo-19 factorization match; the quadratic discriminant is the nonsquare 2. |
| SC2-H4-03 | Sole-H4 lines 123–149 | Candidate tables might miss another actual \(H_2,H_3,H_4\) witness | Closed. Explicit factorizations verify every allowed residue. All three surviving small slots have distinct residues. \(H_4\)'s root is outside each set and zero fails, forcing the center. |
| SC2-H4-04 | Sole-H4 final roles | Equality of residues is weaker than equality of actual roots | Closed. There is exactly one slot of residue \(R\), so case II's witnesses are the same actual rational root. Case III's \(3R\) slot is likewise unique and is rational because it must be the actual \(H_3\) witness. |
| SC2-H2-01 | Sole-H2 lines 52–67 | \(H_4\)-zero branch may omit a nonzero \(H_3\) witness or repeated cubic | Closed. That branch has discriminant 18 if \(H_3\) is nonzero, impossible over \(\mathbb F_{19}\). The \(t=0\) cubic has three distinct nonzero roots because its derivative is \(3T^2\). |
| SC2-H2-02 | Sole-H2 lines 69–91 | Zero \(H_3\) branch, residue-1 ties, and quadratic solutions | Closed. The zero branch has nonsquare discriminant 13. Residue 1 derives row B. The other-root quadratic has discriminant 17 and roots 16,9, deriving C,D. No root differences are divided out. |
| SC2-H2-03 | Sole-H2 lines 93–102 | Double root of \(H_3\) in B could mean two actual witness slots | Closed. The derivative's double root is residue 1 but exactly one small root slot has residue 1. Both actual witnesses therefore coincide. C,D have distinct unique witness slots. |
| SC2-H2-04 | Sole-H2 lines 104–111 | Vanishing \(H_2\) discriminant or zero witness may evade center forcing | Closed. The double quadratic root 13 in B is explicitly outside its root set; C's roots 8,18 and D's 3,4 are also outside. At zero \(-z\ne0\). |
| SC2-H2-05 | Sole-H2 row A and scale convention | Choosing \(R\) from any small slot might assert global rationality | Closed. The choice is only a nonzero residue scale. Multiplication by 7 or 11 permutes the cube-root subgroup; no \(\mathbb Q\)-rationality is inferred from that choice. |
| SC2-05 | Both, all witness splits | Repeated actual roots, tied residues, or residue-extension roots | Closed. Repetitions are allowed before solving. Distinctness is a derived conclusion. D1 is essential to split residues over \(\mathbb F_{19}\), and its hypotheses hold. |
| SC2-06 | Both, conclusion and limits | Necessary patterns might be presented as full lifts or complete exclusions | Closed. Both explicitly deny sufficiency, mask exclusion, degree-20 resolution, and novelty. No D4 parity conclusion is imported for these distinct-residue patterns. |

Residual mathematical work is unchanged: none of the three sole-H4 or four sole-H2 patterns is eliminated, nor is a complete mask proved to lift. This is a limitation of scope, not a defect in the necessary classifications.
