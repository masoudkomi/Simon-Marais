# PN1–PN4 R1: per-claim and per-inference ledger

2026-10-17 UTC. Initially blind whole review. No substantive defect found;
no required author repair. Status is a review recommendation, not promotion.

The reviewer authored accepted PP1/PP2 and PB1. The reviewer did not
construct the new PN lemma, formula, exhaustive table or applications.
This audit does not supply independent review of the accepted dependencies
the reviewer authored. No peer PN findings were read before this freeze.

| ID | Target | Check and disposition |
|---|---|---|
| PNR1-01 | Finite domain | Pass. Six independent optional indices and two mandatory endpoints give exactly 64 cases. No larger support or mask domain is claimed. |
| PNR1-02 | Exact recursion and integrality | Pass. Integer b_j, degree at most 15, binomial denominators divide 15!, a 19-unit. |
| PNR1-03 | T_j operator | Pass. New coefficient is minus old evaluation at the newly largest index; earlier integer roots are unchanged. |
| PNR1-04 | Prefix coefficient dependence | Pass. b_5=-16 when 3 is present; b_7 residues 6,17,12,6 for the four earlier choices independently derived. |
| PNR1-05 | All prefix entries | Pass. Three independently checked binomial columns and eight coefficient triples reconstruct all 40 displayed prefix entries. |
| PNR1-06 | Operator Pascal residues | Pass. Ten ordinary binomial integers and their mod19 reductions supplied in whole report. |
| PNR1-07 | g_11 and g_13 | Pass. Sequential T_9/T_11 corrections independently expanded with signs. |
| PNR1-08 | g_15 mixed terms | Pass. Direct subtraction of 8a f_9,16b g_11,10c g_13 reproduces every coefficient. |
| PNR1-09 | Final formula (1) | Pass. Final T_15 step gives the candidate formula, including coefficient 14abc f_9. |
| PNR1-10 | All 64 table entries | Pass. Independent eight-column simplification (**) and complete auxiliary table reconstruct all 64 entries by hand. No constructor-code read/rerun. |
| PNR1-11 | Table zeros and support labels | Pass. Only row111 columns000 and010 vanish, giving precisely the two stated subsets. |
| PNR1-12 | PN1 coefficient vector | Pass. Both have prefix (2,3,6), b_15=-8=11 and the same complete reduced vector. |
| PNR1-13 | Actual-support distinction | Pass. Optional b_11 is zero modulo19 in the second subset; this fails PP1 nonvanishing, without claiming it is the integer zero. |
| PNR1-14 | Derivative of binomial basis | Pass. Product derivative gives (-1)^(j-2)/(j(j-1)), negative at every odd j>=3. |
| PNR1-15 | PN2 derivative residue | Pass. Contributions 13+3+11+11=38=0; b_1=-1 leaves F'_I(1)=-1 in both cases. |
| PNR1-16 | Zero-residue lifts | Pass. Multiples of19 at index11 or other inactive coefficients cannot change derivative modulo19 because denominators are units. |
| PNR1-17 | Exact root F_I(1) | Pass. b_0=1,b_1=-1 and higher binom(1,j)=0 give an exact zero for every I. |
| PNR1-18 | Taylor mod361 | Pass. 19-integral polynomial yields F(20)=19F'(1) mod361; integer evaluation is -19, hence nonzero. |
| PNR1-19 | PN2 quantifier | Pass. Both PN1 cases treated without assuming actual-support nonvanishing, so joint endpoints are impossible throughout all 64 subsets. |
| PNR1-20 | Accepted PP1/PP2 provenance | Pass as dependency interface. Full frozen text, accepted register and acceptance read. Reviewer authorship disclosed; not counted as fresh review of those bodies. |
| PNR1-21 | PN3 PP1 hypothesis match | Pass. Exact normalized J15/multiplicity-two/rational-witness setting, H3 center and every even nonunit are retained. |
| PNR1-22 | PN3 common-sign factor | Pass. F=(-1)^|I|d changes neither endpoint divisibility; PN2 covers every output of PP1. |
| PNR1-23 | PN3 unit conclusion | Pass. All coefficients are 19-integral, so the logical negation of all even residues being zero supplies an even unit. |
| PNR1-24 | PN4 PP2 hypothesis match | Pass. Sole-H3 repeated2R-root setting, five exact ladder equations and actual rational noncenter H18 witness retained by explicit scope. |
| PNR1-25 | PN4 implication only | Pass. PP2 supplies PN3's contradictory conjunction. No automatic ladder, local-only witness, other mask or general repeated-branch exclusion asserted. |
| PNR1-26 | Published connection and limits | Pass. Primary descent recurrence and one-root source boundary checked; no borrowed multi-root, full-degree, lifting or novelty result. |

No open substantive issue. The finite certificate is complete on its
explicit domain, while the wider annual problem remains unresolved.
