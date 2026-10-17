# R5 R2: complete per-inference and issue ledger

2026-10-17 UTC. Reviewer `review_2022_complexity_r2`; nonconstructor. Initially blind complete freeze. **Unresolved substantive issues: 0. Repairs requested: 0.** No promotion or full-degree conclusion is made. Oxx below refers to constructor obligation R5-xx.

| ID | Inference challenged | Reconstruction / counterexample boundary | Result | Obligations |
| --- | --- | --- | --- | --- |
| R5-R2-01 | Official domain | Q-coefficients and an actual rational shared root separately for each derivative. A rational gcd, splitting over Q, and all-real roots are different hypotheses. | Pass | O01/O29 |
| R5-R2-02 | Rational normalization | Nontrivial example has a rational repeated root and distinct rational simple center, so translating/scaling is rational; use exact accepted body and CLO scope. | Pass | O02/O29 |
| R5-R2-03 | Root valuations | All noncenter nonzero roots have positive valuation; only rational selected roots are assigned integer valuation≥1. Ramified unused roots remain allowed. | Pass | O02/O15 |
| R5-R2-04 | Exact derivative | D_j=H_(d−j)/binom(d,j) is the monic integral polynomial over Q before reduction; j1 fixes1 and H1 can use0. | Pass | O03 |
| R5-R2-05 | Binomial valuations | For2≤j≤p−1 exactly one numerator p and no denominator p. β_j is an integer, and 1−d=−p. | Pass | O08 |
| R5-R2-06 | Selector quantifier | Any actual rational selection is permitted; no need to choose center whenever available. I includes1 and has maximum≤d−2. | Pass | O04/O05 |
| R5-R2-07 | Selected-center versus support | Selected center can have nonunit coefficient; even indices and all selector sizes are kept. PN's odd unit-support class is not substituted. | Pass | O04 |
| R5-R2-08 | Integer recursion | b0=1, b1=−1; on-center recursion has no divisions and off-center b_j=0 exactly. | Pass | O05 |
| R5-R2-09 | Add-largest-index identity | Previous coefficients fixed, b_m=−F_old(m), hence F_new=F_old−F_old(m)binom(Z,m). | Pass | O06 |
| R5-R2-10 | Classical recurrence hypotheses | Smaller descent set has maximum<m, so d(I^-;m) is an actual count. Concatenation splits by the join comparison; extend polynomially. | Pass | O06/O29 |
| R5-R2-11 | Sign and index orientation | Starting from empty selector, the two recurrences give F_I=(−1)^|I|d(I;Z), using exactly I, with no complement or reversal. | Pass | O06 |
| R5-R2-12 | Positivity | d>max I. Ascending runs assigned decreasing value blocks realize every prescribed I, including consecutive descents. | Pass | O07 |
| R5-R2-13 | pq_I identity | Evaluate the binomial polynomial at d; terms0/1 give−p and all others pβ_jb_j. | Pass | O08 |
| R5-R2-14 | Nonzero integer, not unit | Signed positive count proves q_I∈Z\{0}. It does not prove its residue nonzero; actual selectors require further divisibility. | Pass | O07/O08/O30 |
| R5-R2-15 | Empty minimum | If all selected witnesses are0/1, triangular equations give a_j=b_j exactly, contradicting f(1)=0 and nonzero F_I(d). | Pass | O09 |
| R5-R2-16 | Finite ν_w | Nonempty finite set consists of actual rational nonzero noncenter witnesses; all valuations positive integers. Zero omitted, no finite v(0). | Pass | O09/O15 |
| R5-R2-17 | Center comparison | Subtract actual and collapsed equations at1; previous coefficient differences propagate modulo p^ν_w. | Pass | O10 |
| R5-R2-18 | Noncenter comparison | b_j=0 and each previous term has positive witness exponent. p-integrality gives valuation≥ν_w; w_j=0 yields exact zero. | Pass | O10 |
| R5-R2-19 | Actual divided center | f(1)=0 over Q gives−1+Σβ_ja_j=0 exactly before reduction. | Pass | O11 |
| R5-R2-20 | Integer divisibility | q_I=Σβ_j(b_j−a_j) lies in p^ν_wZ_(p); q_I integer makes ordinary divisibility valid. Thus count divisible by p^(ν_w+1). | Pass | O11 |
| R5-R2-21 | Old q0 application | Accepted D5 collapses exactly the selected noncenters to0 in the same recursion. New nonzero identity removes only that stated old qualification. | Pass | O16 |
| R5-R2-22 | Triple orders | ++,+−,−+,−− allow1,2,2,1 of six relative orders, respectively; all entries distinct. | Pass | O12 |
| R5-R2-23 | Disjoint independence | Allocate unordered values to fixed disjoint position blocks first. Relative permutations then vary independently. Overlapping comparisons never treated independent. | Pass | O12 |
| R5-R2-24 | Pair/singleton and seams | Last pair permits one of two orders; singleton one. Discarding interblock comparisons gives upper bound, never equality claim. | Pass | O13 |
| R5-R2-25 | U_n | n!/(6^s2^[t=2]) allocations times≤2^s arrangements gives n!/(3^s2^[t=2]); works for n2 and all t. | Pass | O13 |
| R5-R2-26 | Valuation bound | p^v(count)≤positive count≤U; v(q_I)=v(count)−1≤K_p−1 and ν_w≤v(q_I). | Pass | O14/O15 |
| R5-R2-27 | Degree20 arithmetic | 1458·1668657070080000=20!, and 47045881²=19^12=2213314919066161>U20. Hand arithmetic only. | Pass | O14 |
| R5-R2-28 | Exact off-by-one | ν_w+1 cannot reach12, so ν_w≤10, not11 or a bound on collision depth. | Pass | O14/O15 |
| R5-R2-29 | Minimum-only scope | Every selector has a shallow selected witness; no upper bound on all roots, deepest witness, unused slot, rational height or v(d0−2r). | Pass | O15/O30 |
| R5-R2-30 | Equal/unequal J15 | Equal nonzero small-root valuations identify ν_w=ν. Fractional cluster unavailable to rational witnesses. Unequal case retains only actual selected minimum. | Pass | O16 |
| R5-R2-31 | J exists | Otherwise all a_j nonunits and divided center equation reduces to−1=0. | Pass | O17 |
| R5-R2-32 | h,e bounds | J≥(p+1)/2, J≤p−1 imply e≥2, 2≤h<p, e≤p−2, including p5/extremal J. | Pass | O17/O22 |
| R5-R2-33 | Strict edge inequalities | For l<h, v(c_l)≥2>L(l)≤(p−2)/e<2; for h<l<p, valuation≥1>L(l). | Pass | O17 |
| R5-R2-34 | Missing/leading coefficients | Constant/linear zero, top l=p+1 lies above negative supporting line. Only h,p lie on edge. | Pass | O17 |
| R5-R2-35 | Newton count | Width e roots of valuation1/e counted with multiplicity over Q_pbar; no rationality or distinctness assumption for them. Actual primary multiplicity theorem checked. | Pass | O18/O29 |
| R5-R2-36 | Local coefficient field | Valuation multiset Galois-stable; its monic product g lies in Q_p, not automatically Q. | Pass | O18 |
| R5-R2-37 | Eisenstein and repetitions | Symmetric sums give positive valuations which become integers in Q_p; constant valuation exactly1. Irreducibility/char0 separability then exclude repetitions. | Pass | O18 |
| R5-R2-38 | π-rescaling integrality | π^e=p in an extension; weights vanish only at h,p. Low coefficient exponents2e+l−p≥1, top exponent1. Reduction−T^p+λT^h exact. | Pass | O19 |
| R5-R2-39 | Root residue | T0=α/π unit and P(T0)=0; reduced identity gives T0^e=λ≠0 in residue extension. | Pass | O19 |
| R5-R2-40 | Hasse reduction | Hasse scaling exact; binom(p,k)=0 and binom(h,k)≠0 for1≤k≤h<p. | Pass | O20 |
| R5-R2-41 | Exact low values | The reduced Hasse value is a unit, giving valuation(p−k)/e and nonzero H_k(f)(α), not just a lower bound. | Pass | O20 |
| R5-R2-42 | One global carrier | Q=min_Q(α) divides f and its local factor g divides Q; every cluster root lies in the same Q, M≥e. | Pass | O21 |
| R5-R2-43 | All global conjugates | A shared root anywhere in irreducible rational Q would force Q to divide the rational derivative; low-value/degree arguments therefore exclude the entire global factor. | Pass | O21 |
| R5-R2-44 | Upper orders | k≥h+1 gives derivative degree≤e. M>e impossible; M=e leaves exactly k=h+1. Larger k strictly smaller. | Pass | O21/O22 |
| R5-R2-45 | Equal-degree trace case | Q=g but D_e has coefficient−e at X^(e−1), a p-unit, contradicting Eisenstein's divisible trace coefficient. Scalar normalization occurs before reduction. | Pass | O22 |
| R5-R2-46 | Residual factor | gcd(f,H_k) divides f/Q, deg≤h+1. Derivatives of f are not replaced by derivatives of the quotient. | Pass | O23/O30 |
| R5-R2-47 | Triple-zero corollary | Accepted T3 gives rational residual four-root factor and degree14 Eisenstein quotient when J15,m3; R5C excludes quotient and yields rational common values only. No exclusion claimed. | Pass | O23 |
| R5-R2-48 | Repeated actual slots | Full D3 sole-H3 setting retained; two2R slots must actually coincide. T1 then forces double d0 rational, root set exactly{0,1,r,d0}. | Pass | O24 |
| R5-R2-49 | RC2 to actual H18 witness | Extra full ladder L plus full rational-witness hypothesis invokes exact RC2 conclusion H18(1)≠0 for all ν/displacements. Contest supplies a rational noncenter witness. | Pass | O25 |
| R5-R2-50 | PN4 conjunction | PN4's hypotheses are exactly same setup+L+actual rational noncenter H18 witness, with no further unit condition. All present, so contradiction. | Pass | O26 |
| R5-R2-51 | No circular or retroactive strengthening | PP2 derives parity independently of RC2; old RC2 depths15/16 remain historical necessary outputs, now excluded only with combined full hypotheses. Missing L/distinct slots outside. | Pass | O26/O30 |
| R5-R2-52 | Five TA1 steps | m3..7 use a13,a11,a9,a7,a5 in that order; each preceding ladder equation supplied by induction. TA1 needs actual noncenter existence, even if center also available. No a3/H16 step. | Pass | O27 |
| R5-R2-53 | Sole rational center | Assuming all five orders have noncenter witnesses forces forbidden L. One order lacks such witness; full contest condition then forces1 as sole rational value. Units remain assumptions. | Pass | O27/O28 |
| R5-R2-54 | Full gcd and final ceiling | Rational degree14 carrier excludes all nonrational values; remaining four values rational; simple1 gives monic gcd exactly X−1 after any scalar extension. No full mask/degree/annual answer, universal theorem or novelty inferred. | Pass | O28/O29/O30 |

Counterexample attacks were directed at the tempting extensions, rather than routine cases: a positive descent count need not be a p-unit; an unused or deeper rational slot need not satisfy the selected-minimum bound; Q_p roots are not automatically rational; the quotient f/Q need not be CA; coincident residues do not imply repeated roots; and the ladder does not follow without TA1's unit and actual-witness hypotheses. The candidate expressly avoids each inference. No new false step requiring a counterexample or author repair was found. This ledger is frozen jointly with the complete proof reconstruction and source/integrity records before peer comparison.
