# DG whole review R2: per-inference issue ledger

2026-10-17 UTC. Complete initially blind whole audit. Target main
SHA256 `a62416fe466f21265b6f6572ce5333f7bbe75744cb17c293ef963288b73bf8f2`.
Every row was checked by hand against the complete argument. PASS means
no substantive defect or required author repair found, not promotion.
There are 43 inference checks covering all twelve author obligations.
No new DG peer finding/report was read before this complete freeze.

| Check | Obligations | Inference / adversarial check | Result |
|---|---|---|---|
|DG2-R01|1|Actual chronological relation is ordered alternating shuffle, with each distinct pair counted once by c_n.|PASS; accepted relation matched.|
|DG2-R02|1|Seed 1, addition phase 0, physical-left reversal and original mark-forgetting are distinct conventions.|PASS; old common root growth used, no equality of counts asserted.|
|DG2-R03|1,2|Empty histories and both singleton walks are in the stated domain.|PASS; empty cost is 1/2 and D_0=1.|
|DG2-R04|2|P-Q=H_u+H_v-1/2 converts the integer height strip exactly.|PASS; free grid heights are 0 or 1.|
|DG2-R05|2|An axis path in the strip consumes the alternating source and preserves both tape orders.|PASS; +/-1 steps must alternate starting positive.|
|DG2-R06|2|Endpoint parity follows without an independent balance premise.|PASS; height parity agrees with consumed length.|
|DG2-R07|3|Free diagonal endpoints force the two actual H increments to sum zero.|PASS; sums +/-2 cannot stay in the two-level strip.|
|DG2-R08|3|Both starting height cases admit the stated ordered refinement.|PASS; at 0 positive first, at 1 negative first, whichever tape supplies it.|
|DG2-R09|4|Discrete interpolation gives a continuous monotone matching at no larger cost.|PASS; scalar difference affine along each chosen segment.|
|DG2-R10|4|The closed-threshold continuous event uses an attained minimum, not an unattained infimum.|PASS; classical convention, with explicit x+y compactness justification in report.|
|DG2-R11|5|Every grid-edge free set is whole, a grid endpoint, or empty.|PASS; half-integer initial value and exactly unit slope give integral cuts.|
|DG2-R12|5|Cell free space is convex for both slope orientations.|PASS; affine difference and two halfplane inequalities.|
|DG2-R13|6|Outer-axis reachable sets are initialized without jumping gaps.|PASS; monotonicity forces traversal of all intervening axis points.|
|DG2-R14|6|Left/bottom predecessor order captures global reachability, including routes along shared grid lines.|PASS; an arriving monotone path cannot return from strictly above/right.|
|DG2-R15|6|When B is nonempty every free right-edge point is reachable.|PASS; straight segment from attained bottom minimum is monotone and free.|
|DG2-R16|6|When only L is nonempty the exact right-edge cutoff is min L.|PASS; necessity by monotonicity and sufficiency by convexity.|
|DG2-R17|6|Empty incoming sets do not lose a reachable shared corner.|PASS; every such corner belongs to an incoming closed edge.|
|DG2-R18|6|Top formulas exchange the two incoming sets correctly.|PASS; if L nonempty use all free top, otherwise cut at min B.|
|DG2-R19|6|Output reachable intervals retain closedness and minima 0 or 1.|PASS; whole/point/empty free edge intersected with an integral upper interval.|
|DG2-R20|7|Chosen incoming minima in the stronger induction are grid vertices already bearing axis histories.|PASS; predecessor or outer-axis induction covers them.|
|DG2-R21|7|The selected grid-to-grid segment is an edge, constant, or lower-left to upper-right diagonal.|PASS; anti-diagonal violates coordinate monotonicity; refine allowed diagonal by DG1.|
|DG2-R22|7|Continuous reachability of the terminal corner therefore gives an actual axis history.|PASS; no arbitrary upper-right rounding is used.|
|DG2-R23|4,5,6,7|Point pinches, equality at 1/2, one empty tape and both empty tapes are preserved.|PASS; zero-dimensional rectangles treated directly, closed incoming sets retain points.|
|DG2-R24|8|Tape swap is a bijection for every bidegree, including zero coordinates.|PASS; source letters are unchanged by which tape receives them.|
|DG2-R25|8|Concatenation recovery uses fixed cuts after a and b letters.|PASS; both inputs recover uniquely; no all-bidegree injection alleged.|
|DG2-R26|8|The concatenated blocks start at the same source phase.|PASS; both chosen total lengths are even.|
|DG2-R27|8,10,11|(LR)^m supplies D_m>=1 for every m, including the empty case.|PASS; tapes are 0^m and 1^m.|
|DG2-R28|8,10|Balanced concatenation yields D_(m+n)>=D_m D_n.|PASS; fixed cuts and even source blocks suffice for all nonnegative m,n.|
|DG2-R29|9|A maximum bidegree contains at least c_(2k)/(2k+1) distinct contexts.|PASS; exact partition into 2k+1 classes.|
|DG2-R30|9|Independent choices in the maximum class and its swapped class yield the SQUARE lower bound.|PASS; N^2 pairs, fixed cuts recover both independently chosen contexts.|
|DG2-R31|9|The balanced upper bound is D_(2k)<=c_(4k).|PASS; correct total degree, mere subset inclusion.|
|DG2-R32|9|The 1/(4k) roots of both outer expressions tend to lambda.|PASS; polynomial denominator disappears and square doubles the numerator exponent.|
|DG2-R33|10|Odd tape lengths follow by appending one LR source block.|PASS; phase 0 after 4k letters and last bits recover the old pair.|
|DG2-R34|10|The odd lower root has exponent 4k/(4k+2), proving the limit for ALL m.|PASS; upper root c_(4k+2) has accepted same limit.|
|DG2-R35|10|The supremum formula follows from repetition of each fixed balanced degree and the all-m limit.|PASS; lambda dominates each endpoint and is their limit.|
|DG2-R36|11|Reflection and translation preserve uniformity and independence of the second walk.|PASS; increment-pair encoding is a bijection on 4^m equiprobable pairs.|
|DG2-R37|11|The finite event has probability D_m/4^m with no coupling multiplicity.|PASS; existence selects each admitted word pair once.|
|DG2-R38|11|Probability roots and logarithms have the displayed factors of 2 and 4.|PASS; D_m>0 and log D_m/m tends to 2 log lambda.|
|DG2-R39|11,12|The strict old numerical enclosure gives rate bounds in decreasing lambda order only.|PASS; no new precision, infinite-pair probability, defect or annual evaluation.|
|DG2-R40|4,12|Actual Eiter–Mannila indexed/continuous definitions and comparison hypotheses match the attributed role.|PASS; additive longest-edge estimate does not supply the converse; incidental metric assertion unused.|
|DG2-R41|5,6,12|JoCG's described long-edge condition requires strictly greater than 2 delta.|PASS; 1=2(1/2) fails it; no approximation algorithm imported.|
|DG2-R42|12|Postfreeze ECCC source has a different axis-only convention, initial offset and growing-scale hypotheses.|PASS; context only, no fixed-threshold theorem or unrestricted strict-index assertion imported.|
|DG2-R43|1,12|Role boundaries, exact accepted authority, all old bytes and blind independent-whole protocol remain explicit.|PASS; root constructor excluded, own older R7 not self-recertified, coordinator promotion reserved.|

Substantive issues requiring repair: **none found**. The classical
minimum/infimum convention and excluded source shortcuts are explained
in the full report and source checks. This ledger neither certifies the
entire external papers nor changes any accepted input's scope.
