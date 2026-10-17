# Denominator-safe strict local recovery in four fixed directions

2026-10-17 UTC. **Candidate proof - unverified.** Constructor:
`review_2021_reasoning_j15_r2`. Requested gpt-6.1-sol/max; independent
effective-setting readback unavailable. This is new construction, requiring
two other fresh initially blind nonconstructor audits. It is not a review
conclusion or an accepted theorem. No novelty, H, PR, full fixed-D recovery
or official limit is asserted. No mathematical program or CAS was used.

The result below is D=4 only. It strengthens the accepted fixed-rational
strict transfer by making its tolerance independent of a rational frame's
denominator, in physical units. It compares a near-affine source FAMILY
upper count with insertions in the integer dilations of ONE actual reference.
The inserted interiors need not be near affine.

## 1. Fixed background, quantifiers and the proposed conclusion

Let v_i=(1,i-1), i=1,2,3,4, and V=[v_1 ... v_4]. All tilings below are
genuine full marked zonogon tilings with the accepted de Bruijn dictionary,
integer canonical lift a, Va=x, positive color-i edges incrementing e_i,
and fixed complete exterior when a patch is replaced. There are exactly six
fixed integer parallelogram prototiles. Interpolate lifts affinely on tiles.

Let K be a nonempty compact set of real 4-by-2 matrices satisfying

    VJ=I,  ||J||<=G,  det(J_i,J_j)>=rho>0 for every i<j.

For the displayed G use the maximum Euclidean norm of a row; in finite
dimensions all other norm conversions below are fixed constants. A finite
collection of independent integer physical frame pairs (u_h,v_h), with
det(u_h,v_h)>0, will be chosen from K in section 2. For a suitable chosen
chart h put

    P_L=x0+{s u_h+t v_h:0<=s,t<=L}.

Here L is a REAL physical span parameter. Frame periods will not be called
the scale. Because the collection of physical pairs is finite, this L is
uniformly comparable to diameter and the area is det(u_h,v_h)L^2.

**US1 (uniform digital frames).** For rational J' sufficiently close to
K and in a chosen frame's chart, choose an integer q>=1 with

    A=J'(q u_h), B=J'(q v_h) in positive Z^4.

Use one generic common phase to make the accepted event words U,W of these
contents. There are constants E_can,R_end,B_end,H, independent of q,J'
and the chosen phase, such that their canonical weak lenses at physical
span ell=qm have bounded affine boundary error E_can, bounded digital
physical error, and all nonmain end lobes in two R_end boxes. Their total
end-lobe count factor is at most B_end. Their complete counts C_m satisfy

    0<=e(J',h,q,phase):=lim_m (qm)^(-2) log2 C_m <=H,
    log2 C_m <= e(qm)^2 for EVERY m>=1.                (US1)

The main-lens assertions require qm sufficiently large, with a threshold
independent of q. The entropy limit and last inequality use accepted A5
for this fixed rational frame. No uniform convergence rate or continuity
of e between different rational points is asserted.

**US2 (uniform physical transfer).** There are constants C_buf,A0,K0 and
epsilon_*>0 depending only on K, the finite physical frames and V. For
each chosen rational J', its period q, and 0<epsilon<=epsilon_*, the
following holds whenever

    L>=L_*(epsilon,q),
    L_*(epsilon,q)<=C_*(epsilon)*(q+1)

for a sufficiently large function C_* independent of J' and q. Suppose a
family F of distinct restrictions to P_L, and one actual reference T, have
genuine full-tiling representatives on the WHOLE C_buf sqrt(epsilon)L
neighborhood of P_L, with one common offset c in ker V and

    ||a(x)-J'x-c||_infinity <= epsilon L.             (F)

Then the reference has an actual comparable Jordan CUT lens Omega_T,
with the fixed complete boundary inherited from T and

    P_L eroded by O(sqrt(epsilon)L) subset Omega_T
       subset P_L+O(sqrt(epsilon)L),

such that, putting

    m_+=ceil((L+2A0 sqrt(epsilon)L)/q),

one has

    log2 |F| <= log2 C_(m_+)
                    +K0(sqrt(epsilon)L^2+L+1).       (U)

For every integer M, let R_M(T) count fillings of M Omega_T with its
COMPLETE dilated lifted boundary. Each filling glues to the one fixed
exterior of the integer-dilated reference M T. For all sufficiently large M,

    R_M(T) >= C_(k_M)/B_end,
    k_M=floor((ML-2A0 sqrt(epsilon)ML)/q).            (I)

In particular the region kept outside is exactly M Omega_T, not a newly
chosen nearby lens at each scale. The canonical frame for (U) is fixed
for F, and the annulus for (I) is fixed before its canonical filling varies.

**US3 (uniform strict local recovery, including real tangents).** For
every eta>0 there are epsilon>0 and L0<infinity, chosen in that order,
such that every J in K can use one of the finite physical frames and the
following holds at every L>=L0 for which the actual source family F and
reference T exist with common affine offset and WHOLE buffered error
at most epsilon L relative to J:

    log2 |F| <= liminf_(M->infinity) M^(-2) log2 R_M(T)
                          +eta L^2.                 (R)

The finite rational net and its periods are chosen AFTER epsilon and
BEFORE L0. They affect L0, not the allowable epsilon. There is no assertion
that references exist at all original L, that arbitrary interiors in R_M
remain flat, or that varying tangents have a known entropy formula.

## 2. Finite physical cone charts and uniform numerical margins

At each J in K its nonzero rows lie in one open half-plane, with increasing
angles: the positive ordered minors put all angles after the first in
(0,pi) and order them there. Hence {u:J_i u>0 for all i} is nonempty
and open. Choose two independent rational directions in this cone with
positive determinant and multiply them by fixed positive integers to obtain
integer u_h,v_h. Positivity persists in a neighborhood of J.

Compactness gives finitely many such neighborhoods. Shrink their local
center balls before taking a finite subcover. Consequently there are
uniform kappa>0 and K_dir<infinity so that every assigned chart, and a
sufficiently small neighborhood of its center, satisfies

    kappa<=J_i u_h,J_i v_h<=K_dir.

Take a fixed delta0-neighborhood of K inside VJ=I, small enough that
norms are at most G+1 and all minors at least rho/2. Restrict to those
chart neighborhoods just chosen. All rational approximants will be chosen
there. A uniform lower singular-value bound for the two-row matrices is

    sigma0=rho/(2 sqrt(2)(G+1))>0,

using sigma_min(M)=det(M)/sigma_max(M) and the row norm bound. A change
of the initial norm convention only changes this displayed constant.

For each physical frame, concentric expansion of the span from L to
L+2t moves its four supporting lines outward by at least gamma_h t,
where one may take

    gamma_h=det(u_h,v_h)/max(||u_h||,||v_h||)>0.

The minimum gamma over the finite frames is positive. Their lengths,
slopes and straight lower/upper graph-separation constants are uniformly
bounded. All these choices precede epsilon and rational denominators.

## 3. Event paths: the digital error is independent of the period

Fix one of the allowed rational J'. The affine space VJ'=I is defined
over Q. Choose any q clearing J'u_h and J'v_h. Both integer contents
are strictly positive. On a U segment, use physical time 0<=t<=q and
the straight height H(t)=t J'u_h. Choose 0<theta_i<1 avoiding simultaneous
events along both finite segments. Such phases exist by the finite set
of forbidden hyperplanes. No uniform separation between event times is
needed below.

The count of color-i events by time t is

    h_i(t)=floor(t (J'u_h)_i-theta_i)+1,

at times other than the one-sided convention at an event. It starts at
0, ends at A_i, and |h_i(t)-H_i(t)|<=1. At the vertices before and after
an event use the two corresponding one-sided limits. Endpoints can be
assigned times 0 and q. For an interpolated edge, linearly interpolate
both its height and the associated straight parameter, preserving the
coordinatewise discrepancy bound.

Since A and B are integral, translating any segment by a sum of complete
segments preserves the same phase thresholds. Thus the bound <=1 holds
on the entire U^m,W^n powers and their single junctions, with no error
accumulation across q-periods. On each segment H lies in im J', and

    ||Vh-VH|| <=C_V,
    h-J'Vh=(I-J'V)(h-H).

The first constant depends only on the four fixed vectors; the second
has a uniform bound because ||J'||<=G+1. This proves a q-independent
physical band and affine boundary error E_can. The same bound holds
uniformly in the generic phase, even when two event times nearly coincide.

This is the step that cannot be replaced by a bound using the length of
U or W. Their lengths are q(u_h)_x and q(v_h)_x, but these word lengths
are not digital error bounds.

## 4. Comparability, common ranks and bounded end lobes

Accepted A4 applies to this rational frame u=q u_h,v=q v_h:
the two full words U^m W^n and W^n U^m are comparable. Its pairwise
proof has no numerical constant depending on q: each projected side
pair has determinant det(J'_i,J'_j)det(u_h,v_h)q^2>0, and the same
phases are preserved at integral segment junctions.

For equal m, the straight physical chains enclose the span-qm
parallelogram. In each finite physical chart their vertical gap is at
least a fixed positive multiple of

    min(x-x_left,x_right-x,qm).

Both digital chains are x-monotone, with slopes among 0,1,2,3. The uniform
physical band from section 3 therefore gives a uniform vertical graph
error at common abscissas. A common vertex or shared edge of the two
chains can occur only in two fixed boxes at their extreme corners,
independent of q,m,J' and phase.

Comparable words have the SAME lift at a common physical vertex.
Indeed they have the same prefix length there, because every positive
edge has horizontal displacement one. In an inversion-creating swap
chain a swap across that prefix strictly increases its y coordinate;
other swaps leave the whole prefix vector unchanged. Equal y implies
no swap across the prefix, hence equal prefix height. Thus the lobe
decomposition retains the assigned ranks, not just physical endpoints.

Once qm is above a uniform constant, choose the last common vertex in
the initial box and the first common vertex in the final box. The
intervening comparable paths form the Jordan main lens. All other lobes
are inside those two boxes. The fixed integer local alphabet bounds the
total number of tiles and the total tiling count there uniformly, by
B_end. Tiling choices in the lobes factor at their fixed shared vertices
and paths. Consequently, with Y_m the main-lens count,

    C_m/B_end <=Y_m<=C_m.

The main lens is contained in a bounded enlargement of its straight
parallelogram and contains its erosion by a uniform constant. To verify
the latter, use the uniform graph error away from the corner boxes;
in the corner boxes a uniformly enlarged erosion removes the possible
contact portions. Hence there is no unproved shape assertion inferred
from Hausdorff closeness of arbitrary Jordan curves.

Every weak lens has diameter O(qm), uniformly in this finite frame
collection. Record, at each integer tile origin in that box, the subset
of six possible tile types. This determines the geometry and, from the
fixed start height, its lift. It gives log2 C_m<=H(qm)^2 for a uniform
H after increasing H to cover qm>=1. Accepted A5 gives

    s=lim_m m^(-2)log2 C_m=sup_m m^(-2)log2 C_m.

Divide by q^2 to prove US1, including the upper inequality for every
m, with e=s/q^2. We never need a denominator-uniform convergence
rate or continuity of e as J' or its phase varies.

For any desired corner y and common offset c, choose z in Z^4 nearest
J'y+c. Then

    ||Vz-y||<=C_V,
    ||(I-J'V)z-c||<=C_round,

where C_round is uniform for ||J'||<=G+1. Translate the frame physically
by Vz and its heights by z. Main-lens trimming changes the starting
height only by uniformly many edges. Both the physical and affine
rounding errors remain bounded by one uniform constant, independent of
q, c, y and phase. This supplies complete translated-frame alignment.

## 5. Uniform CUT constants in the unscaled physical frames

Here we reconstruct the constants rather than invoke the fixed-frame
ST statement with rescaled epsilon. Apply CUT with physical u_h,v_h,
not q u_h,q v_h. The sampling lift error at a vertex of a tile containing
a straight sample point is

    E<=epsilon L+C_tile,

where C_tile is uniform from the fixed tile diameter and ||J'||<=G+1.
Let t=sqrt(epsilon), choose N=ceil(1/t), and use the exact equal
mesh ell=L/N. For 0<t<=1, tL/2<=ell<=tL.

For t<=kappa/8 and L>=8 C_tile/(kappa t), one has

    kappa ell >=2E.

For example, allocate kappa tL/4 to 2epsilon L and the other
kappa tL/4 to 2 C_tile. DG2's exact band bound is

    M_V(K_dir ell+3E), M_V=sum_i ||v_i||,

which is at most C_cut tL with C_cut uniform in J' and q after
increasing the same large-L threshold. DG1/DG2 give the required
positive side paths inside that band. The WHOLE C_buf tL neighborhood
is required; take C_buf sufficiently large for all sample tiles and
these bands. Its choice is independent of q.

Use one deterministic corner vertex for both incident sides. The
remaining CUT proof uses only the finite physical frame separation,
the fixed edge slopes, and these uniform bands. Its extreme-corner
contact boxes are O(tL); retaining the last/first contacts gives an
actual comparable Jordan Omega_T, containing the erosion of P_L by
C_cut' tL and contained in its C_cut' tL enlargement. The complete
lift is the original canonical lift. No endpoint or corner phase can
be chosen independently.

For the upper code, every missing tile of a restriction to P_L lies
in a deterministic strip about the FOUR fixed straight sides of width
O(tL+1). Its number of integer cells is O(tL^2+L+1), with uniform
constant, by the four rectangle and corner-box bounds. No arbitrary
perimeter-only multiply-connected-window estimate is used.
The fixed local alphabet records these cells. The two boundary words
have O(L) letters, with a uniform constant because their length is
the sum of their positive lift increments and their endpoints lie in
an O(L) box with ||J'|| bounded. One endpoint's physical coordinate
and integer lift cost O(log(L+2)) bits after a COMMON integer-height
normalization for F. Therefore CUT2's total information cost is

    K_cut(tL^2+L+1),

uniform in q,J' and phase. This reproduces the actual code and its
coordinate-range hypothesis, rather than suppressing an arbitrary
global offset. It fixes the whole inner boundary before padding.

## 6. Uniform annuli and proof of US2

Let h=A0 tL. The canonical outer span S_+=qm_+ lies in
[L+2h,L+2h+q). Center its STRAIGHT parallelogram at the center of
P_L, then apply the common rounded translation of section 4. Its
main lens differs from that straight parallelogram by at most a
uniform constant, say C_can.

Choose A0 so large that the finite shape margin gamma A0 tL
dominates the C_cut' tL extraction band. For large L the bounded
rounding/trimming error is also dominated. The canonical OUTER
main lens contains every extracted Omega with a vertex-to-boundary
buffer at least b0 tL for a fixed b0>0. The same b0 works in all
charts, and neither q nor an event gap has entered it. The possible
ceiling overshoot makes an outer frame larger and does not spoil
this lower bound on the buffer.

Its affine boundary error is uniformly at most E_can+C_round.
The inner actual boundary error is at most epsilon L. Thus the
accepted A3 winding/range test applies whenever

    sigma0 b0 tL >sqrt(2)(E_can+C_round+epsilon L).

Choose epsilon_* small and then L sufficiently large, using only
the uniform constants. This proves the explicit ALL-color rank box
and every ideal test, including absent colors and both corners.
It uses the translated-frame convention with one fixed integer z,
not a free per-corner rank shift. Corrected A2 then gives an actual
closed annulus, fixed by the inner boundary before its filling varies.
Append any fixed end-lobe fillings. The output is counted by C_(m_+).
The CUT strip record, its fixed boundary word/offset and the output
recover the original restriction. This proves (U), with uniform K0.

For insertion choose Omega_T ONCE in the actual original reference.
Integer dilation of every original tile is tiled by its M-by-M grid
of that same type. These grids agree along shared subdivided edges,
so give a genuine full reference M T. Its restriction outside
M Omega_T is fixed. Its boundary lift is the exact M-fold scaled
old lift with consecutive color ranks on each subdivided edge.
The boundary has error at most epsilon ML from J'x+Mc and the
same physical containment with band C_cut' tML.

Center an INNER canonical main lens at the center of M P_L with
span q k_M<=ML-2A0 tML. Integer rounding and trimming have the same
uniform bounded error as before. The actual outer M Omega_T contains
the eroded straight parallelogram, so the canonical inner lens has
the same b0 tML buffer, once M is large. Interchange the two error
roles in the A3 test. It gives the full relative rank box and ideals;
A2 supplies a fixed closed annulus around the chosen canonical core.
The actual exterior of M Omega_T is not changed. Every canonical main
filling gives a genuine distinct full replacement, recoverable by
restriction to that core. Its number is at least C_(k_M)/B_end.
This proves (I), including the fixed original core region rather
than a fresh extraction at each M.

To make (U)'s physical frame diameter O(L) and absorb every bounded
term and the period ceiling, it is sufficient also to impose

    q<=tL, L>=1/t,

besides the preceding uniform thresholds proportional to 1/t.
All these conditions have the form L>=C_*(epsilon)(q+1); after fixing
epsilon_* one can take C_*(epsilon)=C/sqrt(epsilon) for one sufficiently
large fixed C. The
admissible epsilon_* and every code, shape, lobe and buffer constant
are independent of q. We did not apply the accepted fixed-rational
ST theorem by changing epsilon to q epsilon; that would give no
denominator-safe conclusion.

## 7. Cancellation of the unknown canonical density

Keep one rational point, period and phase fixed. US1 and (U) give

    log2|F| <= e[(1+2A0 t)L+q]^2+K0(tL^2+L+1).

For each fixed ORIGINAL L and actual reference, k_M tends to infinity.
A5's all-integer-size limit, applied along this sequence, and (I) give

    liminf_M M^(-2)log2 R_M(T)
         >= e[(1-2A0 t)L]^2.

Take t small enough that 1-2A0 t>0. No convergence in the original
L has been assumed. The q-rounding and bounded end-lobe factors
disappear in this M limit with L fixed. Subtract the lower from
the upper. For q<=tL and t<=1, the difference of the two squares
is at most

    (12A0+3)tL^2.

Indeed its exact expression is 8A0 tL^2+2qL(1+2A0 t)+q^2.
Using 0<=e<=H and L>=1/t gives the uniform choice
C_loss=H(12A0+3)+3K0, after increasing fixed constants if needed, with

    log2|F| <=liminf_M M^(-2)log2 R_M(T)
                          +C_loss sqrt(epsilon)L^2.  (R')

There is no assumption of entropy continuity in J', nor an explicit
formula for e. The SAME fixed receiving family is used on both sides.
The upper bound for all m is essential: it follows from A5's supremum
identity and avoids a denominator-dependent convergence estimate in L.

## 8. Real tangents and the noncircular finite-net order

Here are the full parameter quantifiers needed for US3. First choose
the target eta>0. Choose a small positive epsilon so the uniform
bound in (R'), with an input error 2epsilon L, is at most eta L^2.
Also shrink epsilon to meet the uniform extraction, A3 and chart
thresholds. All constants determining this choice were fixed from
K and the finite PHYSICAL frames before any rational point or q.

There is a constant C_box so the whole required buffered region has
||x-x0||<=C_box L in every chart when epsilon<=epsilon_*.
Choose a finite rational net J'_alpha in VJ'=I approximating K to
delta<=epsilon/C_box, small enough to retain the chart margins.
Existence is elementary: V's first two columns form an integer
unimodular basis, so the last two rows can be chosen rational and
the first two solved rationally. This proves rational density in
the affine space; compactness gives a finite net. A sufficiently
fine net of center balls subordinate to the finite open cone cover
ensures each J and its selected J'_alpha share one physical chart.

For a given J, put

    c'=c+(J-J'_alpha)x0 in ker V.

On the whole buffered region,

    ||Jx+c-J'_alpha x-c'||
         <=||J-J'_alpha|| ||x-x0||<=epsilon L.

Thus an actual error <=epsilon L relative to J becomes an error
<=2epsilon L relative to J'_alpha, with one common offset c' for
the whole source family and reference. Select one denominator
q_alpha and one generic common phase for each net point. Only NOW
set L0 to the maximum of their finitely many L_*(2epsilon,q_alpha)
and the uniform geometry bounds. This maximum is finite. The
allowed epsilon did not shrink after seeing any q_alpha.

If necessary enlarge the original buffered-neighborhood constant
by sqrt(2), so it contains the US2 neighborhood for error parameter
2epsilon. This is one uniform change made before the net. Applying
(R') proves (R) for every J in K, the selected physical chart and
every actual L>=L0. This establishes US3 with no irrational-slope
entropy theorem hidden in rational density.

## 9. Scope, profile effect and unresolved assembly

Every new inserted core is an arbitrary valid filling with its fixed
lifted boundary. Fixed prototiles give a uniform bound on all coordinate
gradients. The glued old and new FULL lifts are globally Lipschitz on
the same convex zonogon, by integration along its straight segments.
They agree outside the modified patch, whose diameter is O(L), so their
height difference is O(L), independent of epsilon and q. In a global scale-p
configuration with L<=lambda p this is O(lambda) in normalized
profile. It is not an O(epsilon lambda) assertion.

The conclusions apply only to compact STRICT tangents, the finitely
many matching physical parallelogram shapes, an actual full reference
and a WHOLE tiled buffer, with one fixed affine offset per family.
They do not prove a fixed-D boundary-stratum or arbitrary orientation
theorem. They do not assemble multiple windows, code variable chart
images, supply rare-count extraction, settle a general rank-mesh
recovery theorem, or establish H/PR/the official limits.

The new construction does not depend on the rank-mesh candidate or its
pending Jordan-window repair. It uses the separately accepted DG,
annulus, CUT and fixed-rational ST bodies in their stated scope, with
the denominator-free constants explicitly reconstructed above. No
all-D extension is asserted by replacing six projections with a
binomial coefficient. Every claim in this packet remains unverified
until two fresh nonconstructor audits and coordinator disposition.
