# Four-direction recovery: detailed assembly construction

2026-10-17 UTC. **Research construction draft with explicit conditional
interfaces**, coordinator root. This file is NOT YET frozen as a complete
candidate for review. No UR4, H4, PR, official limit or novelty is claimed.
No mathematical program or CAS was used. The purpose is to confront the
global reference, chart-image, local-code and order-of-limits issues.

## Exact proposed target and dependency boundary

For fixed C, let GE4_C(r) be actual Jordan tile disks with complete
colored lifted boundary, perimeter<=Cr, and ONE fixed exterior in a
full standard four-direction zonogon with at most Cr curves per color.
Every filling glues to that same exterior. Define

    deficit(B)=max(0,log2 Z(B)-liminf_M M^-2 log2 Z(MB)).

The proposed target is sup_(B in GE4_C(r)) deficit(B)/r² ->0.
This is an asymptotic uniform deficit, not Z(MB)>=Z(B)^(M²).

Accepted inputs: full marked/vector-lift dictionary, extrinsic Lipschitz
bounds, necessary K4 and its uniform-limit minor closure; finite OC charts;
FULL repaired RM1–RM3 and UR3-GE, including the actual Jordan-window
cost and correct block aggregation; FL1; fixed rational annulus/CUT/ST;
and remainder padding. Pending NEW interfaces: US1–US3 compact-strict
uniform local comparison, LW1 LOCAL rank-mesh code when global contents
are much larger than the window, and CW0–CW4 fixed target windows,
anchored recovery and exact fixed-boundary/dilation pullback. Those are
not silently accepted because they have similar names to older results.

The assembly should prove a conditional theorem from their EXACT
statements, then needs two fresh whole audits of the assembly itself.
Root suggested the US denominator strategy, so root's reading is not
counted as an independent US audit. No all-D strict extension is assumed.

## 1. Put fixed exteriors in one bounded balanced frame

An elementary padding argument appears sufficient for unbalanced full
contents N_i. Add one segment [0,v_i] to the convex full zonogon.
For each line parallel to v_i, the Minkowski sum extends the right
endpoint of its interval by v_i. The visible boundary chain has all
steps +v_j for j>i and -v_j for j<i, in their boundary order, and
its i-height is constantly N_i. Extruding each of its unit edges by
v_i tiles precisely the new belt by ij parallelograms. Their transverse
projections form consecutive disjoint intervals, so interiors do not
overlap. End support segments parallel to v_i add no area.

This belt depends only on the old full boundary, never its filling.
Its new i-step has rank N_i+1; old canonical coordinates and physical
positions are unchanged. Iterating to p=max_i N_i gives a full
balanced exterior of content p<=Cr containing B. An eventual whole
audit must check this belt proof and its degeneracies explicitly.
For integer dilation one may simply dilate this one padded reference;
no commutation of two independently chosen padding algorithms is needed.

If a positive-deficit sequence r_j->infinity had p_j/r_j->0, the
finite local alphabet in the O(p_j)-diameter balanced frame would give
log Z(B_j)=O(p_j²)=o(r_j²), a contradiction. Otherwise pass to a
subsequence with p_j>=c r_j. Work in physical scale p_j. Then the
complete boundaries have uniformly bounded normalized perimeter,
and a presumed deficit>=a r_j² is at least a p_j²/C².
Also p_j->infinity. The full normalized ambient zonogon is now
the SAME standard unit-content polygon Z in every j.

## 2. Domains and vector profiles in a hypothetical deficit sequence

Parametrize each positively oriented boundary partial(B_j/p_j) by
constant-speed arclength on[0,1]. Uniform length and ambient bounds
give a uniformly convergent subsequence gamma_j->gamma. The limit
is a rectifiable closed curve, possibly with self contacts, and
has area zero. For x outside its image, uniform convergence fixes
the winding number eventually. Each old curve is Jordan with winding
zero or one, so the limit also has winding zero or one there.
Let Omega be the open set with winding one, away from gamma.
Every compact subset of Omega is eventually inside B_j/p_j.
Indicators converge almost everywhere, and areas converge by bounded
convergence. If Omega has zero area, the finite alphabet plus the
O(p_j) one-curve boundary tube makes log Z(B_j)=o(p_j²), again
contradicting a positive deficit.

All extended normalized vector heights a/p_j on Z have one uniform
Lipschitz bound and coordinates in[0,1]. Their sup-norm cover at
accuracy delta has finite size depending only on delta and D.
Choose delta_j->0 slowly enough that log N(delta_j)=o(p_j²).
Partition all B_j fillings by that cover and take one largest fiber.
Choose a representative full tiling in it. After a subsequence its
normalized lift converges uniformly to h; every member of the fiber
then converges to this SAME h. The profile-cover information is o(p_j²).

The accepted distributional Jacobian closure gives Vh=x and Dh in K4
almost everywhere in int Z. No convexity of K4, sufficiency for arbitrary
profiles, or smoothing through inadmissible gradients is needed. Work
only at differentiability points of h in Omega.

## 3. Choose genuinely fine disjoint windows before counting

Fix a small area-loss delta and desired entropy loss eta. The strict
set consists of points where all six minors of Dh are positive. Choose
rho>0 so that the portion of this strict set with some minor below rho
has area<delta. This follows by continuity from above of measure;
the discarded set decreases to empty within the strict set.
All retained strict tangents lie in ONE compact strict K_rho.
US supplies finitely many physical positive frames and uniform constants
there. Their aspect ratios are bounded.

At every remaining boundary tangent choose one of the finitely many
OC cuts. Its A and inverse have uniform bounds on K4, including zero
minors. In the target chart use a square; its affine inverse gives a
source parallelogram with uniformly bounded aspect ratio. The transformed
tangent has either a zero row or a positive consecutive parallel pair.
With a zero row one can choose the consecutive pair consisting of that
row and an adjacent slot; its minor is zero. With no zero row, some
positive parallel group has an adjacent pair. In D4 merging JUST that
pair leaves two singleton COLOR groups, even if their tangent rows are
also parallel. Only the chosen pair is forbidden. Thus RM2's exact
one-pair theorem suffices; no simultaneous multiple-merge assertion is
required, and no claim of zero entropy for all boundary strata is made.

Choose a small relative collar theta>0. At each retained good point,
fix its local theorem's tolerances FIRST. Differentiability gives
arbitrarily small windows of that fixed shape with the required affine
error on the ENTIRE outer window and its planned buffers. Choose closures
inside Omega. Shrink homothetically for the inner source count window;
the outer window is reserved for the buffer and later insertions.

These outer parallelograms form a fine Vitali family with uniformly
bounded aspect ratio (rho has already been fixed). Standard regular
Vitali selection gives disjoint outer windows covering the good set
up to measure zero. A finite subcollection covers all but O(delta)
of Omega. Its inner homothetic windows lose only O(theta) times their
total area. All windows, shapes, slopes and tolerances are now fixed
in normalized coordinates, BEFORE j tends to infinity.

For sufficiently large j the windows lie in B_j/p_j. Uniform convergence
to h makes every source in the profile fiber satisfy the SAME local
affine estimate on every whole buffered window. Its offset at a point x
is p_j(h(x)-Dh(x)x), in ker V. A fixed finite list permits all thresholds
to hold simultaneously. Rational approximation/period choices for US
are made after its tolerance and before this large-j threshold.

## 4. Strict windows compare to the SAME actual reference dilation

In a strict frame put the US count parallelogram strictly between the
inner and outer source windows. Choose its relative margins so it covers
the inner window and its whole US buffer stays in the outer window.
US's extracted Omega_T also stays inside that outer window when epsilon
is small enough relative to theta² and its constants. Every input
inner-window restriction is recovered from the slightly larger US
restriction, so its count is bounded by that source-family count.

For ANY actual reference in the globally conditioned family, US3 gives

    log(number of local restrictions)
       <=liminf_M M^-2 log R_M(T)+eta_local L²,

where R_M fills the EXACT M Omega_T with the one fixed dilated
exterior. Choose eta_local so the final loss per physical window area
is at most eta. This uses no entropy formula or continuity in slope.
The same canonical density cancels in US; its rational denominator
only changes the large-j threshold. No near-affine claim is made for
the new interiors. They remain inside their fixed outer source window.

## 5. Boundary windows: fixed target square, local code and UR3

For each boundary window use CW1 to place a fixed target square P
strictly between the affine images of the inner and outer source
windows. Choose its margin so P covers every transformed tile meeting
the inner source window and has the needed whole buffer in the actual
image of the outer window for every source. CW2 plus one O(log p_j)
lift anchor recovers the original inner-window restriction from its
target patch. CW0' gives the target's common affine estimate at the
weak tangent J*. Winding, rather than bare Hausdorff closeness, supplies
the fixed target containment.

FL1 for the chosen zero-minor consecutive pair gives at most

    S<=C(epsilon L²+L+1)

rare tiles meeting P and its fixed tile-star enlargement. Apply LW1
with rank spacing r0 fixed before L grows. It codes the local skeleton,
bad flags/fillings and Jordan boundary fringe with cost

    C[L²/r0 + epsilon r0² L² + r0² L + r0 L+r0²+log p_j].

Do NOT invoke the global-content M2 bound with N_i=O(L); here N_i=p_j
and L may be a small fixed fraction of p_j. LW's local rank/traversal
proof is the explicit pending interface that avoids this error.

Every remaining good target disk has the complete fine boundary fixed,
with no chosen forbidden event meeting its selected-face closure.
RM2 gives the exact count bijection to an actual GE3 disk both before
and after every integer dilation. RM3 gives one small full exterior
and the aggregate-perimeter bounds. UR3-GE therefore supplies its
uniform deficit, with no balanced-hexagon substitution.

Use the precise RM3 block aggregation: in one face of scale r0,
blocks of area<beta r0² have total area O(sqrt(beta)r0²), by
aggregate perimeter and isoperimetry; their whole count is at most
exponential in that area. At most O(1/beta) other blocks occur,
each with UR3 deficit eta3(r0)r0². Across the LW bound
O((L/r0+1)²) interior faces, the total normalized block loss is

    C[sqrt(beta)+eta3(r0)/beta]+o_L(1).

First choose beta small; then r0 sufficiently large to make eta3(r0)/beta
and1/r0 small; then epsilon small to make epsilon r0² small. L grows
only after these choices. The actual boundary/fringe L terms then vanish
relative to L². The finite list of windows allows pointwise choices of
constants, or uniform choices over its bounded chart data.

## 6. Joint conditioning BEFORE choosing one reference

Record the original finite alphabet outside the INNER source windows.
Its possible origins have size bounded by their leftover area plus a
fixed-width tube of partial B_j and the finitely many window sides.
The area is O(delta+theta)p_j²+o(p_j²); the tubes have O(p_j) sites
at the fixed finite window family. The one Jordan boundary of B_j has
perimeter O(p_j), even if the limiting gamma has self contacts.
No arbitrary component count is suppressed.

Also condition on ALL boundary-window LW codes and the finite lift
anchors, jointly. The number of joint code choices is at most the
product of their individual bounds. Choose ONE largest global class
and ONE actual reference T_j in it. This loses only the sum of the
stated code lengths. It does not assume that independently maximizing
each window's code gives compatible global choices.

In that class every boundary-window good disk has fixed complete
target geometry and heights. Inverse direction replacement therefore
fixes its fine source boundary as well; its original-reference
pullback is inside its outer source window. Every global original
tiling is recovered from: the conditioned outside/code records,
the strict-window restrictions, and the good target-disk fillings.
Hence its class count is at most the product of those local counts.

Apply each strict comparison to T_j. In each boundary window use the
same T_j's chart and good disks, and the repaired RM2/UR3 lower counts.
CW3 pulls replacements back to their EXACT original fine boundaries.
CW4 identifies the dilated reference pullbacks with exact M-fold
dilations. All changed patches lie in the disjoint outer source windows.
Therefore they insert independently into M B_j with the SINGLE fixed
exterior supplied by M T_j. Restriction recovers each choice.

Different windows may use different charts. They are used only to
construct boundary-compatible fine patches. No simultaneous global
chart map, composition of charts or preserved interior flatness of
the final tiling is needed.

For each fixed j there are finitely many blocks/cores. Thus

    liminf_M M^-2 log Z(MB_j)
       >=sum_(all cores) liminf_M M^-2 log(local count at M).

The lower count is a product injection for every M; the finite-sum
liminf inequality then gives the displayed estimate. M tends to
infinity with j FIXED, after the actual domains and reference have
been selected. No uniform M threshold across infinitely many j is used.

## 7. Intended contradiction and remaining audit obligations

Combining the profile-cover loss, outside information, joint local codes,
strict comparisons and aggregated boundary-block estimates should give

    deficit(B_j)/p_j²
      <=C(delta+theta)+eta * total_normalized_window_area+o_j(1).

Choose delta,theta and eta sufficiently small relative to a/C²,
then let j tend to infinity. This contradicts the positive-deficit
sequence and would prove the proposed UR4 statement.

The constant multiplying area loss is the fixed local alphabet's
constant. Local eta is chosen per physical area before window size,
so a small or large frame determinant is not hidden in the final sum.
Strict-near-boundary points discarded in step3 have area<delta;
exact boundary strata are handled by step5. No assumption of a
strict gradient almost everywhere or convexity of K4 is made.

This detailed draft still needs a final careful pass turning every
“choose margin” and measure/coding step into a complete frozen candidate,
with exact version hashes for US/LW/CW and accepted dependencies.
The padding belt, boundary/domain compactness, regular Vitali use,
strict-window upper recovery, finite joint conditioning, inverse patch
gluing, normalized losses and limit order all require fresh whole audits.
No theorem is promoted by this draft. If UR4 were eventually accepted,
balanced B4(r) plus accepted all-integer remainder padding would imply
H4's existence, not its numerical value. An all-D induction still needs
a complete separately reviewed all-D strict interface; the new all-D
single-pair theorem alone does not supply it. Neither official2017
rate is computed here.
