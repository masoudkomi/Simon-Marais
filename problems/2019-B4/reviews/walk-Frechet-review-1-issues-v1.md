# DG1–DG4 whole R1: complete inference and issue ledger

2026-10-17 UTC. Reviewer `/root/review_2022_complexity_r2`.
Requested gpt-6.1-sol/max; effective readback unavailable. NEW DG
nonconstructor, initially blind to peer findings through the complete
freeze. **No substantive scoped issue or author repair request.**
All12 author obligations map to40 checks. PASS is not promotion.

|Check|Author obligation|Independent reconstruction and challenge disposition|
|---|---|---|
|DGR1-01|DG-O01|PASS. R is the actual phase-zero alternating chronological tape relation. c_n counts distinct contexts once, not histories or unmarked strings; physical left reversal is deferred to conversion.|
|DGR1-02|DG-O01|PASS. Accepted canonical/marked model and common root growth checked against exact bodies/scopes. Earlier own R7/MR review roles are disclosed and no unaccepted MR or short-joining result is imported.|
|DGR1-03|DG-O02|PASS. P_i-Q_j=H_u(i)+H_v(j)-1/2, so the closed distance condition is exactly the integer height strip{0,1}. Reflection and half offset have the necessary signs.|
|DGR1-04|DG-O02|PASS. Any legal history gives a free axis path. Conversely unit height changes staying in{0,1} from0 force alternating +1,-1, hence source0,1,... with endpoint parity automatic.|
|DGR1-05|DG-O03|PASS. A diagonal's two unit increments must sum0 because both endpoint heights are in{0,1}. At start0 take positive first; at start1 take negative first. One allowed intermediate vertex refines every diagonal preserving tape order.|
|DGR1-06|DG-O01, DG-O03|PASS. Axis paths are valid discrete couplings, so both DG1 directions hold without equal tape lengths or an added endpoint-balance condition. Multiple paths do not multiply context counts.|
|DGR1-07|DG-O04|PASS. Couplings are indexed, with axis/diagonal increments; repeated geometric values are not collapsed. Continuous matching uses nondecreasing continuous surjections, waiting, no jumps or backtracking.|
|DGR1-08|DG-O04|PASS. Polygonal closed-threshold attainment agrees with infimum definitions: finitely many monotone gate itineraries, compact gate subsequences and closed convex cells give a limiting matching. No strict-to-closed shortcut is presumed.|
|DGR1-09|DG-O04|PASS. Interpolating each discrete coupled move makes P-Q affine along a cell segment, bounded in absolute value by its endpoints. Thus continuous<=discrete is valid directly.|
|DGR1-10|DG-O05|PASS. Along each grid edge the slope is +/-1 and endpoints are half-integers. Solving for threshold endpoints gives integer parameters; only whole/point/empty free edges occur at the CLOSED half threshold.|
|DGR1-11|DG-O05|PASS. In each cell difference is d+s*epsilon-t*eta. Free space is the intersection of the square with two affine closed halfplanes, hence convex. Ordered free endpoints have a free monotone straight segment.|
|DGR1-12|DG-O06|PASS. On either outer axis, a monotone path cannot leave and return; allowed whole edges or isolated endpoints initialize closed reachable sets with grid minima0/1. Gaps cannot be jumped.|
|DGR1-13|DG-O06|PASS. If incoming bottom set B is nonempty, every free right-edge point is reachable from an included B point by an ordered straight segment, regardless of that point's horizontal location.|
|DGR1-14|DG-O06|PASS. If B empty and L nonempty, right-edge reachability is exactly its free set intersected with[minL,1]. Included minimum gives sufficiency; every entry path through L and monotonicity give necessity.|
|DGR1-15|DG-O06|PASS. If both incoming sets are empty no route exists; reachable shared corners are included in their incident incoming sets. Boundary-running paths still enter through one of these edges/corners.|
|DGR1-16|DG-O06|PASS. Top-edge formulas exchange L/B. Intersections of whole/point/empty free edges with integral-minimum thresholds preserve closedness, interval form and min0/1. Mere nonempty flags are not substituted.|
|DGR1-17|DG-O07|PASS. Strengthened induction uses incoming MINIMUM grid vertices already reached by earlier cells or axes. A monotone segment to an output grid vertex is identity, one grid edge or the lower-left/upper-right diagonal.|
|DGR1-18|DG-O07|PASS. Edges use convexity and diagonals use DG1's free axis refinement. Appending gives an axis history for EVERY reachable grid vertex, in particular the endpoint(a,b), proving DG2's reverse implication.|
|DGR1-19|DG-O05, DG-O07|PASS. Naive upper-right rounding is false, e.g. u=v=0 gives difference-1/2+s+t and a forbidden upper-right corner despite free interior points. This attacks only a rejected shortcut; the candidate's induction avoids it.|
|DGR1-20|DG-O01, DG-O04|PASS. One empty tape gives a degenerate rectangle/constant curve and an axis-only matching; affine edge maxima equal vertex maxima. Both empty tapes have cost exactly1/2 and the admitted empty context.|
|DGR1-21|DG-O08|PASS. Tape swap is a bijection M_(a,b)=M_(b,a). Chronological concatenation of EVEN source blocks has correct phase0 in the second block; physical-left concatenation reversal is not mistakenly used.|
|DGR1-22|DG-O08|PASS. Fixed first bidegree cuts recover both input contexts, including zero-length tape pieces. This proves injection only at FIXED bidegrees; no injectivity over all unlabelled splits is assumed.|
|DGR1-23|DG-O08|PASS. Balanced fixed-bidegree concatenation yields D_(m+n)>=D_m D_n. History(LR)^m supplies0^m,1^m, so every D_m>=1; D0=1 is compatible with empty conventions.|
|DGR1-24|DG-O09|PASS. c_(2k) splits into exactly2k+1 bidegrees, so one has at least c_(2k)/(2k+1) contexts. Selection of that fixed maximizing degree for each k is legitimate.|
|DGR1-25|DG-O09|PASS. Independently choose a context of that degree and one of its SWAPPED degree. Equal cardinalities and fixed recovery cuts give the SQUARE lower bound for D_(2k), not merely one context paired with its own swap.|
|DGR1-26|DG-O09|PASS. D_(2k)<=c_(4k). Raising the two bounds to1/(4k) gives lower c_(2k)^(1/(2k))/(2k+1)^(1/(2k)) and upper c_(4k)^(1/(4k)), both tending to lambda.|
|DGR1-27|DG-O10|PASS. Appending tape bits0,1 at total source length4k preserves phase; last-letter deletion is an inverse, so D_(2k+1)>=D_(2k). The exponent ratio4k/(4k+2) tends1.|
|DGR1-28|DG-O10|PASS. Odd upper bound D_(2k+1)<=c_(4k+2) and even subsequence give the ALL-m limit. No positive-proportion or particular polynomial-fraction claim is inferred.|
|DGR1-29|DG-O10|PASS. For each fixed m>=1, D_(jm)>=D_m^j and the already established all-m limit imply D_m^(1/(2m))<=lambda. The endpoints themselves tend to lambda, so their SUPREMUM equals lambda, with no reversed Fekete inequality.|
|DGR1-30|DG-O11|PASS. There are exactly4^m independent uniform tape-word pairs. Reflection of the second simple walk and translation by1/2 preserve its uniform independent law; word-to-walk correspondence is bijective.|
|DGR1-31|DG-O11|PASS. DG1 selects exactly D_m pairs, once each regardless of coupling multiplicity; DG2 identifies the same event continuously at this threshold only. Thus pi_m=D_m/4^m exactly.|
|DGR1-32|DG-O11|PASS. Positive D_m makes every pi_m positive. Balanced all-m rate gives pi_m^(1/m)->lambda²/4 and continuity of log gives rate2log(2/lambda). No infinite-pair probability or sampler is imported.|
|DGR1-33|DG-O11|PASS. Rate decreases in lambda, so accepted strict lower/upper lambda bounds translate in reversed endpoint order exactly as displayed. These are unchanged bounds, not a numerical improvement.|
|DGR1-34|DG-O12|PASS. Complete Eiter–Mannila Sections1–5/ref list read. Only indexed coupling/monotone matching and the continuous<=discrete comparison are relevant; general additive longest-edge error cannot prove DG2. Incidental metric/stuttering statements are not imported.|
|DGR1-35|DG-O12|PASS. Actual primary JoCG definition/free-space setup and Section4 long-edge condition were read. Required edge length is STRICTLY>2delta. Here1=2*(1/2), so that algorithmic hypothesis fails.|
|DGR1-36|DG-O12|PASS. Postfreeze ECCC addendum remains context, not a changed mathematical target or new premise. Actual axis-only Definition4.1 and growing-threshold/Delta statements were checked; offset/diagonal conventions differ.|
|DGR1-37|DG-O12|PASS. Lemma4.3 uses d=n^(1/4-epsilon)>=(2/3)lnn; Lemma4.7 requires Delta>=2logn. Direct constant-threshold substitution is invalid, and bounds on larger events do not evaluate the fixed-threshold exponential rate. No full ECCC external proof is claimed.|
|DGR1-38|DG-O12|PASS. Original discrete/continuous methods and interval-chain connection are attributed, without priority or absence-of-literature claims. No new2026 annual problem or unrelated critical-code note is investigated.|
|DGR1-39|DG-O12|PASS. Root is constructor and excluded; this reviewer did not construct DG and kept peer findings unread through the complete freeze. Prior R7/MR roles are disclosed, without converting unaccepted candidates into premises.|
|DGR1-40|DG-O12|PASS. Exact candidate/context inputs and older own bytes are preserved by metadata only. No mathematical scan/code/CAS/certificate rerun, exactlambda/defect/grammar/annual/novelty conclusion or promotion is made.|

## Issue disposition

No substantive issue requiring author repair was identified. The main
report supplies the complete reconstruction, including closed-threshold
attainment, actual interval necessity/sufficiency, all shared-corner
cases, strengthened grid-vertex induction, independent square and
correct all-scale exponents. The analytic rounding counterexample
preserves a failed shortcut without alleging a false DG theorem.

The whole initial report, ledger and source/integrity packet freeze
before any NEW peer DG findings. Later substantive objections require
versioned author repair and affected reaudits; this initial stays intact.
