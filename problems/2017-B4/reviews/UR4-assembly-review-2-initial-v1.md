# G4 whole independent assembly audit R2

2026-10-17 UTC. Initial adversarial NONCONSTRUCTOR whole reconstruction,
completed and frozen before reading any peer G4 report, issues or
conclusions. Reviewer /root/review_2022_complexity_r2; requested settings
gpt-6.1-sol/max. Verified effective-setting readback is unavailable.

Exact target: notes/coordinator-UR4-assembly-candidate-v1.md,
22839 bytes, SHA-256
fa0bd05d345dee884335e3a5cd0e601ce08e8212da3d812227750f04c5113d0f.
Exact freeze: coordinator-UR4-assembly-freeze-v1.json, 3465 bytes,
SHA-256 20c10f07ba8cc7977628e218e4339976428e552f65d0efa1ec5764db33a03a0f.
The complete candidate, preserved earlier draft, every listed
mathematical premise and the relevant acceptance scopes were read.
The accepted OC, dictionary, LW and CW bodies had also received my
earlier whole reconstructions; those do not substitute for this new
global reconstruction.

Disposition: no substantive objection found to the exact conditional
G4 implication and its fixed-balanced-D4 limit consequence. Forty
separate inference records accompany this report. The topological,
geometric, coding and limit steps below are reconstructed rather than
inferred from the existence of separate local lemmas. This is not
promotion. The coordinator must compare two whole audits and resolve
any subsequent objection.

The frozen target explicitly retains LW1 and CW0–CW4 as pending exact
premises. During this audit the coordinator separately accepted those
exact bodies without mathematical change. I checked their new accepted
copies as byte-identical suffixes and read the status/scope additions.
That local update is not a peer G4 finding and does not itself accept
the global assembly.

## 1. Scope, full exteriors and balanced padding

The official 2017 B4 asks for two normalized rates with the number of
directions growing. G4 instead concerns a fixed four-direction marked
integer model and actual Jordan tile disks with a common small full
exterior. A fixed-origin translation normalization of that ambient
zonogon is harmless. All counts retain colors, canonical heights and
ranks. A standalone paired boundary without this full exterior is not
an input. No official rate, numerical value, all-D induction or novelty
claim is present.

Reconstruct the new extrusion, not merely a word about padding. Fix i
and use transverse coordinate t=det(v_i,x). Each nonextreme line of
constant t intersects the old convex zonogon in one interval along v_i.
Adding [0,v_i] keeps its left endpoint and increases its right endpoint
by v_i. The positive-v_i visible boundary therefore determines the
entire new belt, section by section.

On this visible chain the i coordinate is N_i. A convenient start is
N_i v_i+sum_(j<i) N_j v_j and the end is
N_i v_i+sum_(j>i) N_j v_j. Its steps are +v_j for j>i and -v_j
for j<i, in the appropriate cyclic boundary order. Every such step
strictly increases t. Extrude each unit step by v_i. Its transverse
interval is consecutive and disjoint from the interiors of those of
the other steps. For a t in that interval the resulting parallelogram
is exactly the section between the old visible endpoint and that
endpoint plus v_i. Hence these tiles have disjoint interiors and fill
the new belt exactly. At the two extreme support segments, directions
parallel to v_i add no area; the endpoint edges of adjacent belt tiles
still give the correct new boundary. No separate filling is missing
at either end.

Assign the old canonical heights unchanged on the old domain. In the
belt a_i runs from N_i to N_i+1. Every new color-i edge therefore
has rank N_i+1; the other coordinate increments are exactly those
of the old visible unit step. Reversed -v_j steps use the same old
rank in reverse orientation. These formulas agree across neighboring
belt tiles and the old seam. The new initial corner, old positions
and old full lift remain unchanged. The construction depends only
on the old complete outer boundary, not its filling.

Zero N_i or absent steps in a visible chain cause no problem. The
input B is a positive-area tile disk, so the original ambient
zonogon has at least two active physical directions. Each addition
retains that property. A hypothetical one-direction zero-area
ambient frame cannot contain such a B and is outside the domain.
If a color already has p=max N_i, it needs no addition.

Iterate the belts until every content equals p. This produces one
fixed balanced exterior for every filling of the original B. In
particular all these fillings extend to the same full Z_p, and old
rank coordinates are preserved. For dilation we use the one padded
reference's exact grids. It is unnecessary to equate padding done
after dilation with dilation of a separately rerun padding algorithm.

The finite alphabet in a diameter-O(p) balanced frame bounds log Z(B)
by K p², with fixed K. Dilation supplies at least one filling, so the
nonnegative deficit is at most log Z(B). Thus a deficit >=a r²
forces p/r>=sqrt(a/K), while p/r<=C by hypothesis. This also verifies
the candidate's subsequence argument excluding p/r ->0. Work in scale
p; p tends to infinity, boundary perimeter/p is bounded, and

    deficit(B_j)/p_j² >=a/C².

The normalized ambient polygon is now exactly the same unit-content Z
for every j. All source positions and heights are O_D(p_j).

## 2. Varying Jordan boundaries and one common limiting profile

Choose positive orientation and constant-speed arclength
parametrizations gamma_j on [0,1]. Their Lipschitz constants are the
normalized perimeters, uniformly bounded by the preceding p/r estimate.
The curves lie in compact Z. Arzela–Ascoli gives a uniformly convergent
subsequence gamma_j ->gamma. The limit is Lipschitz/rectifiable,
possibly self-touching or multiply retraced, and its image has planar
measure zero. No assertion that the limit is Jordan is required.

For x outside gamma's image, its distance from that compact image is
positive. Uniform closeness makes the straight homotopy between gamma_j
and gamma avoid x, so the winding numbers agree for all large j.
The Jordan gamma_j has winding zero or one, and therefore so does
gamma at every such x. Its winding-one set Omega is open. If K is
compact in Omega, its distance from gamma is positive, so the same
homotopy works uniformly over K; K is eventually inside B_j/p_j.
Outside gamma the indicators converge pointwise to that of Omega.
Bounded convergence on the fixed ambient polygon gives area convergence.
This permits several limiting components, narrow necks and contacts.

If area(Omega)=0, area(B_j)=o(p_j²). The possible integer tile origins
in B_j, or within fixed tile distance of its boundary, number
O(area(B_j)+perimeter(B_j)+1). One way to see this is to separate
unit lattice cells wholly inside from those meeting the boundary.
The latter lie in a bounded-width tube of ONE curve of length O(p_j);
an arclength cover pays O(p_j+1) for them. The finite tile alphabet
therefore gives log Z(B_j)=o(p_j²), contradicting the positive deficit.
There is no unpaid component term for a many-holed window here:
each finite B_j has its actual one Jordan boundary.

Every B_j filling extends through the same original exterior and
the fixed belts to a full content-p_j tiling. Its normalized vector
lift on Z has one uniform extrinsic Lipschitz bound, bounded coordinate
range [0,1] and the fixed full boundary normalization. A delta-net of
the physical domain has O(delta^-2) sites; quantizing D height values
there gives

    log N(delta)=O_D(delta^-2 log(2/delta)).

The common Lipschitz bound controls the rest of the domain. Thus
delta_j=1/log(p_j+2) gives log N(delta_j)=o(p_j²), without needing
an unknown rate from abstract compactness.

Take one largest profile fiber A_j and one actual extended lift h_j
in it. Its size loses at most log N(delta_j). Compactness gives a
subsequence h_j ->h uniformly. Each other member differs from h_j
by O(delta_j), hence every member of A_j converges to the SAME h.
This is a full-domain compact cover with actual representative,
not independent profile choices for different windows.

The identities Vh_j=x pass to the limit. Uniform derivative bounds
and the distributional identity for 2x2 minors pass nonnegative
minors to the limit, as in the accepted dictionary. Consequently
Dh belongs to K4 almost everywhere. This does not require K4 to be
convex or every necessary profile to be realizable. Rademacher gives
differentiability almost everywhere in Omega. At a good point x0,
J=Dh(x0) and c0=h(x0)-Jx0 satisfy Vc0=0.

## 3. Strict truncation, exact boundary strata and actual fine windows

On the strict set the minimum of the six nonnegative minors is
positive. Its portion with minimum below rho decreases to the empty
set as rho decreases to zero. Choose rho so this lost area is <delta.
The retained strict matrices form one compact K_rho. The accepted US
theorem supplies finitely many physical frames with bounded shape
constants on that set. These may depend on rho, but not on j.

At any retained non-strict tangent use one OC cut. The finite cuts,
compact K4 and the weighted determinant identity bound A and A^-1
uniformly, including zero minors. The inverse image of a centered
target square therefore has uniformly bounded eccentricity, diameter,
perimeter and positive unit-scale area.

There is an eligible adjacent zero-minor pair in the target chart.
If a row is zero, pair it with an adjacent slot, including the case
that the neighbor is also zero. Otherwise a zero minor gives two
parallel rows; OC has made their parallelism positive and their
group consecutive, so some adjacent pair is available. Merge ONLY
this pair. There remain two singleton COLOR groups, regardless of
whether some of their tangent rows are zero or parallel. RM2 concerns
these actual color groups, not an assertion that all tangent groups
are distinct. Its exact D4 one-pair hypothesis is satisfied. No
simultaneous two-pair lifting theorem or wholesale zero-row deletion
is needed. Three-direction recovery also includes its degenerate
active-content cases. A positive-area disk always retains enough
actual directions for its full exterior.

All local tolerances are fixed before window radii. Strict tolerances
come from the compact US class, the desired loss per area and the
collar theta. Boundary tolerances absorb the uniform CW error map,
the chosen r0 and the rare-flux/code budget. Differentiability at
x0 then gives arbitrarily small centered windows of its chosen shape
with affine error on the ENTIRE outer window; its bounded aspect
ratio converts the usual differentiability ball to this scale.
Take the closure inside Omega. Inner homothetic windows use side
factor 1-theta. Their total collar area is at most 2theta times the
outer area. Planned US or target buffers are kept inside the outer
window, not supplied from just its corners.

For completeness, the regular Vitali use can be reconstructed directly.
All these closed parallelograms are centered at their good points,
are arbitrarily small there and have area >=c times diameter²,
with common c>0 after rho is fixed. Choose disjoint members greedily,
each with diameter at least half the supremum still available.
Their area sum is finite in bounded Omega. A candidate disjoint from
the first n must eventually be hit by a later chosen set of at least
half its diameter; otherwise infinitely many disjoint sets would
have area bounded below. For a point not in the selected union,
fineness gives arbitrarily small candidates disjoint from those
first n closed sets. Thus that leftover point lies in a fixed-radius
enlargement of some later chosen set. The area of the enlarged tail
is bounded by a fixed constant times the original tail area, which
tends to zero. The uncovered good set has outer measure zero.
This justifies the regular Vitali assertion for the actual variable
shapes, not a claim about arbitrary rectangles of unbounded aspect.

The discarded strict-near-boundary set has area <delta, and
nondifferentiability has measure zero. A finite subcollection of the
disjoint outer windows therefore covers all but O(delta) of Omega.
Inner windows lose a further O(theta) area. The entire finite list,
its frames, offsets and tolerances are now fixed before j grows.

At a selected point x_alpha, the common physical plane is
J_alpha x+p_j c_alpha, c_alpha=h(x_alpha)-J_alpha x_alpha.
Normalized uniform convergence of EVERY A_j member and the
differentiability estimate put every one within the prescribed
tolerance on the whole physical outer window for all large j.
Each physical side parameter is ell_alpha p_j with fixed ell_alpha>0,
so every required scale threshold eventually holds simultaneously.
Offsets can depend on alpha,j but are common across the family
for that window. No uniform differentiability modulus for all
profiles, or simultaneous chart for all tangents, is presumed.

## 4. Strict windows: upper restrictions versus one reference core

Use the US frame selected for the retained strict tangent. The count
parallelogram has side factor 1-theta/2, between the inner and outer
source windows. Its transverse separation from the outer boundary
is a fixed positive multiple of theta times its scale. Choose the
US tolerance sufficiently small that both its WHOLE buffer and
its extracted Omega_T's enlargement have less than a quarter of
that margin. All constants are known before the tolerance and
rational periods. The source tolerance on the outer window is
smaller still, absorbing scale and norm conversions and US's
real-tangent doubling.

There is no period circularity. One may first impose all upper
caps on the uniform US error supplied by its proof, then choose
the actual small error to meet both those caps and the boundary
budgets, and only then form US's finite rational net and periods.
The exact proof allows any sufficiently smaller tolerance while
its loss bound improves. The periods affect the eventual L0 only.
No tolerance must be shrunk after its periods have been fixed.

Let N_s count distinct restrictions of the global class to the
slightly larger US window. Its full representatives and the later
chosen actual reference have the same affine bound and common
offset on the whole buffer. Its restriction recovers the desired
inner source restriction. Accepted US3 applies to ANY such actual
reference T_j and gives

    log N_s <= liminf_M M^-2 log R_(s,M)(T_j)
                  +eta_s L_s².

Here R fills exactly M Omega_(T_j), not a new extraction at M.
All new interiors may be nonflat. The unchanged exterior is that
of the exact integer dilation of T_j, and Omega_(T_j) lies within
this window's outer source frame. With eta_s chosen per outer
physical area, summing the errors will not introduce a frame
determinant or a factor equal to the number of windows.

The accepted US input's comparison uses the SAME rational canonical
density in upper and lower counts, its EVERY-m supremum upper bound
and its all-integer-size limit. The assembly does not replace this
with a formula for entropy at the real tangent or an assumed
continuity in slope.

## 5. Boundary windows: original restrictions and locally coded good disks

Use the fixed OC chart chosen at this tangent. The affine image of
the outer source window is a square, and its inner homothetic image
is a smaller concentric square. A target square P at intermediate
side factor 1-theta/2 has a uniform transverse margin to both.
CW0 gives O(epsilon L) physical error, CW0' gives a uniformly
bounded multiple of that lift error, and CW1 gives actual winding
inclusion of P AND its entire required tile-star buffer for every
source. Choose epsilon sufficiently small relative to theta and
then j sufficiently large to absorb fixed tile diameters.
The same explicit margin puts the ENTIRE image tile of every
source tile meeting the inner source window inside P.

CW2 consequently recovers the WHOLE inner source restriction from
the target restriction plus one absolute lift anchor. In the
balanced frame all relevant positions and heights are O_D(p_j);
one can take R=C_D p_j. Thus the retained cost is O(log p_j),
without requiring p_j=O(the local L) with uniform constant.
Extra target tiles in the record are harmless; their exact inverse
uses the full tiling correspondence. A single full representative
per distinct original restriction suffices for CW2's injection.

The selected adjacent pair has target minor zero. Apply FL1 to
the target square with its constant-width star enlargement.
The whole required boundary has the common affine error, and its
diameter/perimeter are O(L). Green's identity and the nonnegative
event integral give

    S <= C(epsilon L²+L+1).

The L+1 term counts actual tiles cut by or merely touching the
boundary. No conclusion locates the rare tiles in a thin band.

LW1, with integer r0 fixed before L grows, gives the skeleton,
bad flags/fillings and ONE-Jordan fringe code

    C[L²/r0+epsilon r0² L²+r0² L+r0 L+r0²+log p_j].

This is its local theorem, not global-content M2. The ambient
content can be much larger than this window's side. The code
counts only retained actual GLOBAL selected faces, pays cut
faces in the explicit fringe, and fixes their complete fine
boundaries and lifts. One boundary trace and anchor determine
all relevant ranks; no outside exit matching or per-tile log p
factor is suppressed.

A retained good face has its WHOLE closure and incident tile stars
free of the forbidden pair. Thus RM2's closed-face condition holds,
including forbidden tiles outside an individual biconnected block
that touch its boundary. Each actual good block has its two fine
ports for every active coarse curve, with exactly one merged pair
and two singleton color groups. RM2 gives a count bijection with
its complete coarse Jordan disk, both at scale one and EVERY
integer dilation. Green's zero boundary flux also rules out
forbidden tiles in arbitrary alternative fine fillings.

RM3 removes curves inactive on that disk; their coordinate is
constant there. This changes the disk only by a fixed translation
and rank shift and supplies one small full three-direction exterior
with O(r0) curves per color. Deformation to standard lozenges
preserves complete boundaries, counts and dilation. Hence it is
actually a GE3_C0(r0) disk, not an arbitrary ragged boundary
substituted for a balanced hexagon. The fixed C0 is uniform over
the finite color-pair choices. Accepted UR3-GE applies.

Do not pay one UR3 error per FACE while ignoring multiple blocks.
The actual aggregate perimeters in a selected face sum to O(r0),
and the total fine/coarse area is O(r0²) with fixed comparability
constants. For blocks of area A<beta r0²,

    A <=sqrt(beta) r0 sqrt(A)
       <=sqrt(beta) r0 perimeter/(2 sqrt(pi)).

Their total area is O(sqrt(beta)r0²). Their log counts are at most
a fixed constant times that area: a reference filling bounds
perimeter and number of possible origins by its tile number,
and each physical tile has area bounded above and below.
Using the trivial lower count one is therefore sufficient for
these blocks. There are at most O(1/beta) larger blocks, each
costing <=eta3(r0)r0² in UR3 deficit. Across the LW face bound
O((L/r0+1)²), their normalized loss is

    C[sqrt(beta)+eta3(r0)/beta]+o_L(1).

Choose beta small, then integer r0 large for eta3(r0)/beta and
1/r0, then epsilon small for epsilon r0² and all chart/collar
requirements. The remaining r0² L, r0 L, r0² and log p_j
terms vanish relative to the window's L² as j grows at the
already fixed window list. Both the per-window fringe charges
and every anchor are summed, rather than one charge reused
for an unbounded family.

## 6. Outside conditioning, recovery and a single common reference

The uncovered part of B_j outside the INNER source windows has
area at most C(delta+theta)p_j²+o(p_j²), by area convergence and
the finite Vitali selection. Record the actual original finite
tile alphabet there, including tiles crossing its boundaries.
Its possible origin set is bounded by that area plus fixed-width
tubes about the actual partial B_j and the finitely many window
sides. The former is ONE curve of length O(p_j), the latter
have total length a finite constant times p_j. Thus the tube
cost is o(p_j²). The coefficient on the area term is the fixed
local alphabet constant, independent of rho and the eventual
number of windows. A large finite boundary-length constant
depending on those windows is harmless after j grows.

Within the largest profile fiber, condition JOINTLY on this
outside record, all boundary-window LW codes and all required
anchors. The number of joint records is at most the product
of their individual uniform bounds. Take a largest joint class
X_j and then ONE actual full representative T_j from it. This
loses at most the summed code length. Independently maximizing
each window and then hoping for a compatible reference would
not work; that invalid move is absent.

In X_j the target good-disk geometry and complete canonical
boundaries are fixed by each code. Through the exact chart inverse
their original fine boundaries are also fixed. A good target
disk lies strictly inside the target core, so its reference
fine pullback is within its outer source window. The source
inner restriction is recovered from target good-disk fillings,
the LW code and anchor by LW plus CW2. Strict inner restrictions
are recovered from their slightly larger US restrictions.
Together with the original outside record these determine the
whole original tiling of B_j. This is a recovery of ALL source
tiles, not just a family of chart-coordinate fragments.

It follows that

    log |X_j| <=sum_s log N_(j,s)+sum_b log Z(C_(j,b)),

where C_(j,b) may be read as the recorded good TARGET fine disk.
Its count and dilated counts equal the coarse GE3 counts by RM2.
Its insertions into the ORIGINAL domain are provided by CW3/4;
one must not identify its physical shape with its fine pullback.
The inequality only needs upper recovery and those lower
insertions, so this notation entails no unproved shape equality.

The local choices in this upper product need not be compatible
with one another: it is an upper bound. For the LOWER product,
use precisely the one selected actual T_j. Apply the strict
comparison to that T_j; in each boundary chart use its actual
good disks and coarse exterior. CW3 inverts a full target tiling
with fixed exterior, so each new fine patch has EXACTLY the
old fine boundary and occupies the same Jordan disk. The new
interior inverse need not equal the old inverse pointwise.

Every changed patch lies in its own outer source window.
Different outer windows are disjoint, and inside each boundary
window the original good blocks have disjoint interiors and
only fixed possible shared boundary vertices. Their reference
fine pullbacks preserve those incidences. Thus all these new
fine patches glue independently to the one full T_j exterior.
They lie inside B_j and preserve its complete boundary.

## 7. Exact integer scales and the finite-sum limit

For every integer M>=1 the reference M-grid lift satisfies
a_(MT_j)(Mx)=M a_(T_j)(x). CW4 commutes with that grid exactly
using content Mp_j and translation M b0. Every boundary good
target disk therefore pulls back to the exact M-dilation of
its original fine reference disk, with consecutive fine ranks
fixed on each subdivided boundary edge. RM2's every-M port
lifting gives the corresponding coarse count, not a choice
of new matching data.

For a strict window US has already fixed Omega_(T_j) in the
original reference. R_(j,s,M) counts fillings of precisely its
M-dilation. For small M the same region is tileable by the
reference grid; the stronger US canonical lower estimate is
needed only for all sufficiently large M at fixed j. All these
patches can consequently be inserted into EXACT M B_j, leaving
the SAME fine exterior of M T_j. Restriction, followed where
necessary by the fixed local chart, recovers each choice.
Different charts never have to commute as global maps.

At each fixed j the number of cores/blocks is finite. For
every M the product injection gives the appropriate count
lower bound, and nonnegative finite sums satisfy

    liminf_M M^-2 log Z(M B_j)
      >=sum_s liminf_M M^-2 log R_(j,s,M)
        +sum_b liminf_M M^-2 log Z(M C_(j,b)).

No inequality in the opposite direction is used. The list may
grow as j grows, but j is FIXED for this M limit. Thus each
local finite M threshold may depend on j and the actual
reference. No uniform threshold across an infinite family
or interchange of j and M is assumed.

## 8. Quantitative budget and contradiction

Here is a consistent order realizing the prose of sections3–8.
Start from a presumed positive normalized deficit a/C².
Choose delta and theta to make the universal OUTSIDE area
cost smaller than a/(4C²); choose the desired local per-area
budget zeta to make area(Z) times that budget smaller than
a/(4C²). Then choose rho for strict truncation. This fixes
the strict finite shape collection, the uniform boundary
shape bounds and positive m0 for unit-scale source areas.

Choose the strict eta parameters at most an appropriate fixed
fraction of zeta*m0; choose beta, then r0, then the tolerances
as in section5, imposing the strict collars too. All unit-scale
loss constants are bounded before this choice. After the
US tolerance is fixed choose its finite rational net, periods
and phases. Only then use differentiability and Vitali to
select the finite normalized windows, and finally choose
the simultaneous large-j threshold. Each physical L tends
to infinity, including ones from very small fixed windows.
For each such j, take M to infinity last.

The shape bounds justify the per-area normalization. A window
of side ell has area >=m0 ell²; the intermediate count side
is no larger, and target/source areas have uniformly bounded
ratios from the A determinant bounds. Dividing an error chosen
as a small multiple of zeta*m0 times ell² by that physical
area gives the desired per-area zeta bound. Their total outer
area is <=area(Z), because the windows are disjoint. No
small determinant, numerous windows or huge rational
denominator is hidden in the final area sum.

For every j,

    log Z(B_j)<=log |A_j|+log Ncov_j,
    log |A_j|<=log |X_j|+c_j.

The profile term is o(p_j²), and

    c_j <=C_D(delta+theta)p_j²
          +zeta sum_alpha area(outer window_alpha)
          +o_j(p_j²),

with constants in local budgets adjusted as stated. Strict
upper-minus-lower losses and all boundary-block losses have
the same summed per-area bound, already allocated in zeta.
Subtract the finite-product liminf lower bound from the
upper recovery inequality. The candidate's absorption of
fixed numerical fractions yields

    deficit(B_j)/p_j²
       <=C_D(delta+theta)+C_Z zeta+o_j(1),
    C_Z<=area(Z)

after renaming the total local budget if needed. The
right side is eventually <a/C² by the preceding choices,
contradicting the positive-deficit sequence. Taking max(0,...)
in the deficit causes no problem since all allocated losses
are nonnegative. This proves the claimed uniform implication;
no explicit rate in r is obtained.

## 9. From G4 to the balanced fixed-four-direction limit

The full balanced content-r zonogon is a GE4_C(r) disk for
one fixed C: it has its actual Jordan boundary, O(r)
perimeter and r curves per color. Its exterior may be
empty, which is a valid fixed exterior. G4 therefore gives

    liminf_M (Mr)^-2 log B4(Mr)
       >=r^-2 log B4(r)-eta_C(r), eta_C(r)->0.

For a FIXED positive integer r, this is a liminf over all
large M, not a sparse sequence of scales. RP1 injects
B4(Mr) into B4(p) whenever Mr<=p<(M+1)r. The ratio
Mr/p tends to one uniformly over that bounded remainder.
RP3 therefore transfers the displayed lower bound to
the FULL integer-p liminf. No entropy is created from
one finite tiling; the supplied input is the all-large-M
count lower bound just proved.

The finite alphabet bounds the full limsup by a finite
constant. Take r through an integer limsup sequence.
For each fixed r the full liminf is at least
r^-2 log B4(r)-eta_C(r); then let those r grow.
The full liminf is at least the full limsup. This proves
existence of this fixed-D4 balanced limit, conditional on
the exact premises and successful global audit, with no
finite exact quadratic supermultiplicativity assumption.
The normalization differs by the harmless fixed factor16
if one uses (4p)² instead of p². It does not address
growing D in the official question.

## 10. Adversarial attempts, source boundary and disposition

I tried degenerating old contents, misplaced extrusion ranks,
independently rerun padding at M, p/r vanishing, non-Jordan
boundary limits, zero limiting area with a long thin interior,
profiles chosen separately in different windows, antiparallel
and zero tangent rows, multiple parallel groups, highly eccentric
Vitali sets, denominators chosen before errors, target windows
controlled only at corners, global-content M2 used locally,
many tiny blocks in one rank face, independently maximal
window codes, unknown original tiles left by a chart record,
a changed interior inverse, overlapping local chart images,
a growing block count inside a liminf, and sparse-multiple
padding. The exact restrictions and estimates reconstructed
above resolve these attempts. I found no false step needing
an author repair in the stated scope.

The proof uses actual references throughout. It does not assume
arbitrary necessary profiles are realized, K4 is convex, slopes
have a continuous entropy formula, limiting Omega is Jordan,
local source/target counts are identical, a chart preserves
canonical shapes, new interiors stay flat, different charts
globally commute, or separately chosen code classes share an
exterior. All-scale statements concern exact integer dilations
of fixed finite references before the separate bounded-remainder
step. There is no all-D or official-rate promotion.

Sources and exact read scopes are recorded separately. In
particular CKP's external theorem enters only through accepted
UR3-GE and its precise GE3 hypotheses; no new varying-domain
application of a smooth-boundary source theorem is made.
The new global domain limit is handled directly above.

Only this assigned review prefix was written. No candidate,
shared file or Git edits; no mathematical enumeration/CAS.
The 14 author-freeze rows are verified, supplemental local
acceptance bodies are exact suffix copies, and all earlier
own frozen records are preserved by the integrity packet.
Latest direct authoritative telemetry during the audit was
29% total weekly used at 07:19:25 UTC, reset1792745187,
with the 90%-total ceiling and integration reserve retained.
