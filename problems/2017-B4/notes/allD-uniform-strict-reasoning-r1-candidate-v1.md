# Strict local recovery in every fixed number of directions

2026-10-17 UTC. **Candidate proof - unverified.** Constructor
`review_2021_reasoning_j15_r2`; requested `gpt-6.1-sol` / `max`,
verified effective settings unavailable. Two OTHER fresh initially blind
nonconstructor whole auditors are required. Root suggested the uniform
strict strategy; its inspection cannot replace a fresh independent audit.
No novelty, global UR_D, H, PR or official limit is claimed.

This extends the accepted D4 strict construction to each FIXED D>=3.
The all-color poset, annulus, phase, available-box, winding and local
entropy arguments are proved below for that D. The accepted cutting
theorem already has arbitrary fixed D; its proof and its constants are
reconstructed in the unscaled physical frames. The D4 theorem alone
is not a theorem for larger D, and replacing the number six by a
binomial coefficient is not the proof offered here.

No mathematical program, enumeration or CAS was used. Exact accepted
dependencies and source scope are in the companion source packet.

## 1. Background, quantifiers and the proposed conclusion

Fix D>=3 and v_i=(1,i-1), 1<=i<=D; V has these columns.
Use genuine full marked zonogon tilings, their canonical continuous
affine-on-tiles lifts a with Va(x)=x, and the accepted full de Bruijn
dictionary. An oriented positive color-i edge increments a_i by one.
Same-color rank tracks do not cross; distinct-color tracks cross once
in a full zonogon. Integer-height-translated copies retain their full
marked boundary. There are B_D=binom(D,2) fixed integer prototiles,
each of physical area at least one and with a finite maximum diameter.

The accepted DG1 theorem supplies a positive edge path whenever the
endpoint lift difference is coordinatewise nonnegative. Its exact
DG2 bound is recalled in Section8. These are full-tiling statements,
not assertions about arbitrary incomplete wiring windows. They use
Arroyo–McQuillan–Richter–Salazar's original plane-arc Lemma2.2,
which permits parallel nonintersecting arcs, through the separately
reviewed disk/cell adaptation. No new entropy theorem is imported.

Let K be a nonempty compact set of D-by-2 matrices such that

    VJ=I_2,  max_i ||J_i||_2<=G,
    det(J_i,J_j)>=rho>0 for every i<j.                 (1)

Finite integer physical frames (u_h,v_h), of positive determinant,
will be fixed from K, before any rational approximation. For an
assigned frame put

    P_L=x0+{s u_h+t v_h:0<=s,t<=L},                    (2)

where L is a REAL physical span. Its area and squared diameter are
uniformly comparable to L² over the finite frame collection.

**US_D1, rational receiving families.** For allowed rational J' near
K choose q>=1 with a=qJ'u_h and b=qJ'v_h in positive Z^D, and one
common generic phase. Their event words U,W define complete weak-lens
counts C_m between U^mW^m and W^mU^m. Constants E_can,C_can,R_end,
B_end,H depend only on K,D and the finite physical frames, not on
q,J' or the generic phase. Boundary affine/digital errors are bounded
by E_can,C_can. For qm above a uniform threshold the Jordan main
lens contains the constant erosion of its straight span-qm frame and
is contained in its constant enlargement; its count Y_m obeys

    C_m/B_end<=Y_m<=C_m.

Furthermore

    e=lim_(m->infinity) (qm)^(-2) log2 C_m exists,
    0<=e<=H,  log2 C_m<=e(qm)^2 for EVERY m>=1.        (3)

The density e belongs to this ONE fixed rational frame/phase family.
No continuity, formula or denominator-uniform convergence rate for e
is asserted.

**US_D2, denominator-safe physical transfer.** There are uniform
constants C_buf,A0,K0,C and epsilon_*>0. For any allowed rational
J', its q and phase, let 0<epsilon<=epsilon_*, t=sqrt(epsilon), and

    L>=C(q+1)/t.                                     (4)

Suppose a nonempty family F of distinct restrictions to P_L has
actual full-tiling representatives, and T is ONE actual full reference,
all satisfying on the WHOLE C_buf tL neighborhood of P_L

    ||a(x)-J'x-c||_infinity<=epsilon L,  Vc=0,         (5)

with the SAME J',c. That whole neighborhood is inside each full tiled
disk. There is a comparable Jordan CUT lens Omega_T in the reference,
with its complete original boundary fixed, such that

    P_L eroded by C_cut tL subset Omega_T
       subset P_L+closed_ball(0,C_cut tL).             (6)

For the canonical counts of US_D1 set

    m_+=ceil((L+2A0 tL)/q),
    k_M=floor((ML-2A0 tML)/q).

Then

    log2 |F|<=log2 C_(m_+)+K0(tL²+L+1).              (7)

Let R_M(T) be the number of complete-boundary fillings of the EXACT
integer-dilated disk M Omega_T, keeping the full dilated reference
MT outside. For all sufficiently large integers M,

    R_M(T)>=C_(k_M)/B_end.                           (8)

The region M Omega_T is fixed by the original reference extraction,
not newly extracted at scale M. Its arbitrary inserted interiors need
not remain near the affine lift. The admissible epsilon_* and all
constants precede q; q changes the scale threshold (4).

**US_D3, real compact-strict local recovery.** For every eta>0 there
are epsilon>0, a finite rational net with fixed periods/phases, and
L0<infinity, chosen in that order, such that every J in K can use
one of the physical frames and the following holds. Whenever L>=L0
and an actual family F/reference T satisfy the common-offset version
of (5) relative to J on the required WHOLE buffered region, then

    log2 |F|<=liminf_(M->infinity) M^(-2)log2 R_M(T)
                         +eta L².                   (9)

No existence of references at all original scales is asserted. This
is a local comparison at each actual original L. All global window
selection, boundary strata, orientation-chart assembly, UR_D and H
remain separate obligations.

## 2. Ranked weak order and physical shellings in arbitrary D

A word of content N has internally ranked labels (i,1),...,(i,N_i),
and only shuffles preserving each same-color order are allowed. Initial
label order is color then rank. Write p<=q when their cross-color
inversion sets satisfy inclusion. Physical words use positive v_i
edges, so every edge advances horizontal coordinate by exactly one.

If p<=q, an inversion-creating adjacent-swap chain exists. At the
first position where the current word differs from q, move q's
desired next label left across the intervening labels. Each such
label must be smaller: crossing a larger one would remove an
inversion present in the current word but absent from q. Same-color
labels retain their rank order and are never crossed. Repeat.
Each swap ij->ji with i<j raises the physical path and adds precisely
the positive ij parallelogram between the old/new two-edge paths.
Its interior lies above the current path; previously added regions
lie below that path. Thus all added interiors are disjoint and fill
the weak lens between p and q. Contacts match entire edges or
vertices. An integer vertex cannot lie strictly inside a unit-x
integer edge, so no partial-edge subdivision is hidden. This is an
actual planar degree-one shelling for every D.

We will also need exact ranks at physical contacts. Two comparable
words have the SAME lift at any common physical vertex. Its horizontal
coordinate specifies the same prefix length. In the swap chain, only
a swap across that prefix changes its height vector, and such a swap
strictly increases its physical y coordinate by j-i>0. Other swaps
leave that prefix vector unchanged. Equality of the initial/final y
coordinates therefore forces no swap across that prefix. This proves
the height equality even though V is not injective on all Z^D.
Shared edges have the same color and ranks as well. Consequently the
lobes of a weak lens separated by common vertices or paths have
consistent complete lifted boundaries. Their tilings factor: an
interior of a positive-area tile cannot cross an abscissa where the
two boundary graphs coincide. Every component is itself tiled by
the restricted swap construction.

## 3. AD1: all-color prefix ideals, with the exact rank box

Fix outer words p0<=q0 of content N. Let P0 be the intersection of
their total ranked orders. It is a poset. A shuffle w belongs to
[p0,q0] exactly when it is a linear extension of P0: inversions
already in p0 and noninversions still in q0 are forced, and the
remaining pair comparisons are free subject to transitivity.

For an INTEGER h satisfying EVERY coordinate bound

    0<=h_i<=N_i,                                    (10)

put I(h)={(i,k):1<=k<=h_i}. Such h occurs as an extension's prefix
count if and only if I(h) is an ideal. Necessity is immediate.
For sufficiency concatenate p0 restricted to I(h) and p0 restricted
to its complement; ideality makes this a linear extension. The
coordinate bounds (10) are part of the domain, not an inference
from a set formula that could silently truncate a negative coordinate.

For each i<j let b_p(k) count the j's before the k-th i in the
two-color subword of p, with b_p(0)=0 and b_p(N_i+1)=N_j.
At h_i=s the closed two-color weak lens has exactly the integer
vertical range

    b_p0(s)<=h_j<=b_q0(s+1).                          (11)

Failure of the lower inequality means an unselected j is forced
before a selected i in BOTH outer words. Failure of the upper means
an unselected i is forced before a selected j in both. Conversely
any violated cross-color ideal comparison is one of these two types.
Same-color ideality already follows from taking initial rank sets.
Thus, ON the all-color rank box, ideality is equivalent to membership
in every one of the B_D projected closed lenses. Endpoint sentinels
handle s=0 and s=N_i; N_i=0 also uses them. No color pair or absent
inner color is omitted, and no label permutation is chosen.

## 4. AD2: an actual closed annulus and recoverable fibers

Suppose p0<=q0 bound a Jordan outer lens Omega0, based at integer
height zero. An actual tiled inner Jordan lens Omega has comparable
words p<=q, start a and end b=a+m in integer heights, and lies
strictly inside Omega0. Require

    0<=a_i<=b_i<=N_i for ALL i,                       (12)

and require I(h) to be an ideal for every inner boundary vertex.
Its color-i labels are the consecutive global ranks a_i+1,...,b_i.
An absent inner color m_i=0 still has the bound (12).

Let A be p0 restricted to I(a), and B be p0 restricted to the
complement of I(b). The words A p B and A q B are extensions
of P0. Prefixes within A are ideals because I(a) is; prefixes
inside the middle are exactly the given I(h); prefixes within B
are ideals because I(b) is and p0 orders its complement. The
fixed rank shifts give

    p0<=A p B<=A q B<=q0.                             (13)

Fixed adjacent-swap chains for the first and last comparisons tile
the lower/upper bands. Between the middle paths retain any chosen
actual tiling of Omega. The bands have disjoint interiors by their
pointwise path order and fill all of Omega0. The entry seam A has
horizontal positions before the inner left endpoint; the exit seam
B is after its right endpoint. Neither enters the inner interior.
They close both corners and give an actual annulus, with identical
global rank on both sides of every seam edge. No quotient of an
abstract surface is used.

Choose the two padding chains once from the boundary before the
inner filling varies. Restriction to the fixed Omega recovers the
chosen filling, proving injectivity. If inner boundaries vary with
O(L) letters and O(L) relative height coordinates, the boundary data
have at most (CL+1)^D D^(CL) times a polynomial number of possibilities,
hence cost O_D,C(L+log(L+2)) bits. The boundary code specifies Omega,
so distinct choices with the same output and code are recoverable.
No rank factorial or unseen strand matching is paid away.

For an outer start z0, rebase heights by z0 and physical positions
by Vz0. Conditions are z0_i<=a_i<=b_i<=z0_i+N_i and ideals
I(h-z0); all labels are retained. This is one fixed translation,
not independently chosen offsets on the four sides.

## 5. AD3: all pair windings force available ranks and ideals

Let VJ=I and all ordered minors Delta_ij>0. Put

    sigma(J)=min_(i<j) sigma_min((J_i;J_j))>0.

Retain the actual Jordan/comparable outer and inner lenses with
assigned complete lifts. Assume containment of the inner lens in
the outer and physical distance at least d>0 from every INNER
boundary vertex to the outer boundary. Suppose one common c in ker V
gives error <=E0 in infinity norm on the entire outer boundary
and <=E1 at inner boundary vertices, relative to Jx+c. If

    sigma(J)d>sqrt(2)(E0+E1),                         (14)

then (12) and every boundary ideal condition in AD2 follow.

First, the vertex separation and containment imply strict nesting.
On each interval [k,k+1] an inner edge and each outer positive path
are affine graphs: all their vertices have integer horizontal
coordinates and every edge has unit horizontal displacement. At
the inner edge endpoints the two outer graph gaps are positive.
Both affine gaps remain positive throughout that interval. There
is no interior edge contact. The compact closed inner lens is
therefore strictly inside, not merely vertex-separated in a drawing.

Fix an inner boundary vertex x and i<j, and let M=(J_i;J_j).
The affine image of the positively oriented outer boundary winds
once about Mx+c_ij, because det M>0 and x is inside. Its distance
to that boundary is at least sigma(J)d. The assigned h_ij(x) is
within sqrt(2)E1, so it remains inside the affine image. Homotope
the affine boundary to the actual projected outer lift; its error
is at most sqrt(2)E0. Inequality (14) keeps this homotopy away from
h_ij(x), so the projected loop also has winding one there.

That projected loop consists of the two ordered two-color paths.
Shared pieces cancel; its winding is one exactly in the open
components of their weak lens and zero outside. Thus h_ij(x) lies
in that closed lens. It is contained in [0,N_i]×[0,N_j]. Applying
this to every pair FIRST forces every coordinate of h into its
available rank interval, including a color absent from the inner
lens. At the two endpoints this gives (12). Only AFTER this range
check does AD1 turn all B_D projected-lens tests into ideality.
AD2 now constructs the actual annulus.

For start z0 use x'=x−Vz0, h'=h−z0 and
c'=c−(I−JV)z0 in ker V. The same two error bounds and physical
distances are unchanged. This proves the translated statement with
one globally fixed phase/offset, including all corners. Convex
interpolation of profiles and a bounded-gap height-to-displacement
lemma are not needed. The strict singular-value hypothesis is retained.

## 6. Finite physical cone frames and uniform margins

At a strict J the row angles are strictly increasing in an interval
of length less than pi. To see this, give the first row angle zero;
every later row lies in (0,pi), and a decrease of successive angles
would give a negative ordered minor. Hence the open common positive
cone {u:J_i u>0 for all i} is nonempty. Choose two independent
rational vectors in it with positive determinant, and multiply by
positive integers to obtain a physical integer pair u_h,v_h.

These inequalities persist on a neighborhood of J. Compactness and
a shrunken finite subcover give finitely many pairs and compact
assigned sets inside their open chart domains. There are constants
kappa>0,K_dir<infinity such that every assigned J and all allowed
nearby J' satisfy

    kappa<=J'_i u_h,J'_i v_h<=K_dir for every i.       (15)

Choose a small fixed neighborhood inside VJ=I in which row norms
are <=G+1 and minors >=rho/2. All approximants lie there and in
an assigned cone chart. For every two-row matrix,

    sigma_min((J'_i;J'_j))
       >=sigma0=rho/(2 sqrt(2)(G+1))>0.              (16)

This follows from det divided by the maximum singular value,
which is at most sqrt(2)(G+1). There are B_D matrices but the same
lower bound works for each; there is no missing least-pair condition.

The first coordinate of each physical pair member is positive,
since u_x=sum_i J'_i u and VJ'=I, and likewise for v. The slope
of u is strictly smaller than that of v. Let

    gamma=min_h det(u_h,v_h)/max(||u_h||,||v_h||)>0.

Concentric expansion of the span L to L+2h moves EACH of the four
supporting lines outward by at least gamma h; shrinkage reverses
the same gaps. Finite frame lengths, graph slopes, slope differences
and coordinate-change norms have uniform bounds. Every constant in
this section is fixed before epsilon, a denominator or an event phase.

## 7. AD4/AD5 and US_D1: exact rational digital receiving frames

### Common phases, comparability and a q-free error

Fix allowed rational J' and q with a=qJ'u and b=qJ'v in
positive Z^D. Choose 0<theta_i<1 avoiding equal event times on
both segments from zero to a and zero to b. Each equality has the
form a_j theta_i−a_i theta_j=constant, or its b analogue.
There are finitely many proper affine hyperplanes, so a rational
point of the open phase cube outside their union exists. No lower
bound on separation of event times is assumed or needed.

U records in order all events t(J'u)_i=k+theta_i, 0<=t<=q;
W uses J'v in the same way. Their contents are exactly a,b.
Away from an event, the count is

    h_i(t)=floor(t(J'u)_i−theta_i)+1,
    |h_i(t)−t(J'u)_i|<=1.                            (17)

It starts at zero and ends at a_i. The two one-sided counts at an
event satisfy the same bound; every point of the interpolated edge
does too at that event's straight parameter. Segment endpoints use
their exact integer content. Translating a segment by integer sums
of a,b preserves the SAME fractional thresholds. Thus (17) has no
accumulated period error along U^mW^n and W^nU^m.

For i<j, the two straight projected boundary chains have side
vectors m(a_i,a_j), n(b_i,b_j), whose determinant is positive.
At each i threshold k+theta_i the lower chain has no larger j
coordinate than the upper chain. The number of j thresholds already
crossed is its monotone floor function, with the SAME theta_j.
So b_lower(k)<=b_upper(k) for every i rank. These are precisely
the inversion comparisons for this pair. Checking EVERY pair proves

    U^mW^n<=W^nU^m for all integers m,n>=1.           (18)

This argument uses the all-color common phase and the positive
determinants det(J'_i,J'_j)det(u,v)q², not a four-color assertion.
Integer endpoint translations make the displayed words actual powers.

Let H be the corresponding straight height on any side. It belongs
to im J', and ||h−H||_infinity<=1. Therefore

    ||Vh−VH||_2<=M_V=sum_i||v_i||_2,
    h−J'Vh=(I−J'V)(h−H).                             (19)

Row norms of J' are uniformly bounded. Formula (19) bounds physical
digital displacement and affine boundary error uniformly in q,m,n,
J' and phase. The word lengths may be proportional to q; they do
NOT occur in these error bounds. A color-gap conversion with a
period-dependent gap is never used.

### Actual main lenses and bounded lobe factors

Set ell=qm. The two straight physical chains have total horizontal
span X=ell(u_x+v_x), and their vertical separation at abscissa x is

    (slope(v)−slope(u))
       *min(x,X−x,ell u_x,ell v_x),                  (20)

after translating the initial x to zero. Since the frame collection
is finite, (20) is at least c0 min(x,X−x,ell) for a uniform c0>0.
Both digital paths are x-monotone. Their pointwise physical band (19)
and the finite straight slopes give a uniform vertical graph error
at a common abscissa. Contacts are therefore confined to two fixed
end boxes once ell is above a uniform threshold.

Contacts are common integer vertices or shared edges: gap functions
are affine on every unit-x interval. The exact equal-lift result of
Section2 applies. Choose the last common vertex in the initial box
and first in the final box. The middle positive paths have no other
contact and form a comparable Jordan main lens with their inherited
global ranks. Every discarded lobe is confined to the two end boxes.
Their total tile count and number of possible fillings are uniformly
bounded by the finite integer alphabet; call the count bound B_end.
The weak-lens count factors over its pinched components, so
C_m/B_end<=Y_m<=C_m. This includes all discarded information, with
no matching factor. If ell is below the uniform threshold the whole
weak lens is in a uniformly bounded box; no large main-lens assertion
is needed for it.

There is also a uniform C_can such that the main lens is contained
in the C_can enlargement of its straight parallelogram and contains
its C_can erosion. Away from the end boxes this follows directly
from the vertical graph bound: a sufficiently deep point is above
the lower digital graph and below the upper one. Enlarge C_can so
the straight erosion avoids both bounded end boxes, using the finite
frame coordinate-change bounds. This proves inclusion of the whole
eroded core, not just Hausdorff closeness of arbitrary Jordan curves.

### Exact block injection and the all-scale density

For every m, the weak lens is tileable by Section2 and lies in a
box of diameter O(qm), uniformly in this finite collection. At each
integer tile origin record which of B_D fixed types are present.
There are O((qm+1)²) origins. Since qm>=1, for a uniform H

    1<=C_m<=2^(H(qm)²).                              (21)

Fix l and write m=kl+r, 0<=r<l. Group the U and W powers into
k blocks of size l and one remainder. Bubble the U blocks past
the W blocks. Each block exchange U^a W^b->W^b U^a is a comparable
weak lens by (18); choose a fixed filling at mixed remainder crossings.
Exactly k² crossings have a=b=l and allow arbitrary C_l fillings.
The successive physical paths only rise by Section2, so these
translated block regions have disjoint interiors and exactly matching
seams. Their global boundary heights are integer sums of a,b block
contents. Restriction to the fixed regions recovers all choices.
Consequently

    C_m>=C_l^(floor(m/l)²).                           (22)

No claim that arbitrary polygons pack at density one is being made.
These are the exact regions of this positive block-swap shelling.
Divide log(22) by m² and let m tend to infinity. Its liminf is at
least l^{-2}log2 C_l for every fixed l. The reverse limsup bound
by that same supremum is tautological. The finite upper bound (21)
therefore proves

    lim_m m^{-2}log2 C_m=sup_l l^{-2}log2 C_l=s.       (23)

With e=s/q², (21)/(23) prove (3), including its EVERY-m upper
bound. The bounded lobe factor leaves the main-lens density the same.
This is an all-integer-size limit for the receiving boundary family,
not the entropy of the full balanced zonogon or of a free window.

### One translated phase and rank alignment

For a desired physical starting corner y and c in ker V, choose an
integer z nearest J'y+c coordinatewise. Then

    ||Vz−y||<=C_round,
    ||(I−J'V)z−c||_infinity<=C_round,                 (24)

with one uniform constant. Indeed z−J'y−c is bounded coordinatewise,
and VJ'=I,Vc=0. Translate the ENTIRE frame physically by Vz and
its heights by z. Equations (19)/(24) bound its boundary error from
the SAME J'x+c and move its straight shape only a uniform amount.
Main trimming changes its initial height by uniformly many edges.
Thus (24) fixes every rank and corner phase together; it does not
introduce separate offset choices on each side.

## 8. ACUT: full all-D extraction, with q-independent constants

The accepted CUT1/CUT2 is already stated for arbitrary fixed D.
For use here we give the uniform argument from the exact DG bounds,
with u_h,v_h themselves, never q u_h,q v_h. Let t=sqrt(epsilon),
N=ceil(1/t), ell=L/N; for 0<t<=1,

    tL/2<=ell<=tL.

Choose a vertex of a tile containing each straight sample point,
using one deterministic tie rule. At each of the four corners use
the SAME vertex for both incident sides. Its lift error from the
straight sample is at most E=epsilon L+C_tile, with C_tile uniform
from (1), the finite tile diameters and the whole-buffer hypothesis.
If t<=kappa/8 and L>=8C_tile/(kappa t), then

    kappa ell>=2E.                                   (25)

For successive vertices, their lift coordinates are nondecreasing
and each increment is at most K_dir ell+2E. DG1 gives positive
paths. Each point of one such path has physical distance at most

    M_V(K_dir ell+3E)                                (26)

from its straight sample segment, as follows directly by bounding
all its coordinates between endpoint lifts and applying V. Under
(25)/(4), (26) is <=C_band tL with a uniform C_band. Choose C_buf
large enough to include every sample tile and this ENTIRE band.
No endpoint-only buffer and no path in an incomplete local graph
is presumed. The accepted full DG1 path cannot use an uncontrolled
shortcut: the coordinate estimate (26) confines it regardless of
which positive path is chosen.

Concatenate the u-side/v-side paths and the v-side/u-side paths.
They have common start/end vertices and are positive, hence simple
and x-monotone after removing empty pieces. Their lengths telescope
as sums of positive lift increments, so are O(L) uniformly in D's
fixed data. Formula (20), now at span L, and (26) confine every
contact to O(tL) boxes at the two extreme corners. The middle has
strict lower/upper separation for small fixed t. Retain the last
common initial-box vertex and first common final-box vertex. There
is no remaining contact, so these paths bound a Jordan lens Omega.
The graph bounds and corner boxes prove (6) and an area discrepancy
O(tL²+L). This is a whole-core inclusion proof, not a boundary-only
shape assertion.

Both paths use the same canonical height at their common vertices,
so their retained words have exactly the same rank content. For
each active rank track, positive a_i increments cross that level
once on each path. All inactive tracks cross neither path. Boundary
crossings occur only transversely at color-i edge midpoints, never
vertices. A full proper track restricted to the Jordan disk has
one arc joining these two ports; an extra component would require
more boundary crossings or a closed proper track. Two such arcs
cross at most once. At the sole possible ij crossing its positive
tile changes order only from ij on the lower path to ji on the
upper. Equivalently the alternating disk endpoints have precisely
this orientation. No already inverted pair can become uninverted.
Thus the retained words are comparable with ALL ranks fixed. This
uses the accepted full arrangement, not injectivity of V on Z^D.

For coding, record the finite local alphabet in a deterministic
strip about the FOUR straight sides of P_L of width C_cut tL plus
the maximum tile diameter. Unit lattice cells in those four strips
and corner squares number O(tL²+L+1): the t²L² corner terms are
absorbed because t<=1. A tile relevant to P_L but not in Omega
must meet this strip by (6). Record also the two O(L)-letter
boundary words, one endpoint lift/position and length/tie conventions.
Subtract ONE common integer vector nearest J'x0+c from every input
height, and translate physical coordinates by its V image. On the
buffered region all relative coordinates are O(L), uniformly in q;
the endpoint cost is O_D(log(L+2)). This is a common normalization,
not a per-filling hidden offset.

The output Omega filling, boundary code and strip record recover
the restriction to P_L. One full representative per distinct source
restriction is chosen before extraction. This yields an upper fiber
bound 2^(K_cut(tL²+L+1)) with uniform K_cut. The B_D possible tile
types, rather than six, enter this finite alphabet. No arbitrary
perimeter-only estimate for multiply connected windows is used.

## 9. AST and US_D2: actual upper padding and lower insertion

Let h=A0 tL. The outer canonical span
S_+=qm_+ lies in [L+2h,L+2h+q). Center its STRAIGHT frame at
the center of P_L and use the single rounded translation (24).
This outer canonical main lens is fixed before source representatives
vary. By Section7 its whole shape differs from the straight frame
only by a uniform constant and its boundary error from J'x+c is
bounded by a uniform E_b.

Choose A0 so large that gamma A0>=C_cut+4. The supporting-line
gaps imply that the extracted Omega, lying in P_L+B_(C_cut tL),
is at distance at least 4tL from the complement of the straight
outer frame. Its canonical main lens contains that straight frame's
constant erosion; rounding and trimming cost at most C_can. For
L>=C_can/t, the whole Omega is therefore inside that main lens
with vertex-to-boundary separation at least tL. The ceiling overshoot
q only enlarges the outer frame and cannot spoil this buffer.

Choose t small and then the uniform scale constant in (4) large
so that

    sigma0 tL>sqrt(2)(E_b+epsilon L).                 (27)

For example it suffices to require t<=sigma0/(4sqrt(2)) and
L>=4sqrt(2)E_b/(sigma0 t), with harmless enlargement of constants.
AD3 gives ALL coordinate rank ranges and all B_D ideal tests,
including absent inner colors. AD2 pads Omega into the canonical
outer main lens by an actual fixed-boundary annulus. Append fixed
bounded end-lobe fillings to obtain an output counted by C_(m_+).
The same source strip/boundary code recovers the source restriction.
Its extra annular boundary data cost O(L+log(L+2)) bits, absorbed
in K0(tL²+L+1). This proves (7). Common phases, all assigned ranks
and all corners are supplied by (24)/(27); none is chosen afresh
for different fillings of the same boundary fiber.

For the lower construction extract Omega_T ONCE from the actual
reference T. Replace each enlarged tile of MT by its M-by-M
uniform grid. The grids agree on all shared edges and have canonical
lift a_MT(Mx)=M a_T(x), including affine interpolation. The exterior
of M Omega_T is fixed, and its boundary has error <=epsilon ML
from J'X+Mc. Its positive boundary words remain comparable: replace
each original letter by M copies, and each ij->ji swap by the
M² positive swaps exchanging those two blocks. This also fixes every
consecutive boundary rank and its exact endpoint height.

Center an INNER canonical main lens of span q k_M in M P_L,
using one rounded integer offset (24) relative to Mc. It is no
larger than ML−2A0 tML. The same supporting-line argument now puts
its entire shape in the actual outer M Omega_T: that outer lens
contains P_(ML) eroded by C_cut tML, while the canonical inner lens
is at least gamma A0 tML−C_can from its boundary. The resulting
vertex-to-actual-outer-boundary buffer is at least tML for all
sufficiently large M. Floor undershoot only increases the buffer.
The canonical span tends to infinity because t is also chosen with
1−2A0t>0.

Apply AD3 with the roles of the bounded and epsilon ML errors
interchanged. It supplies the full relative rank box and all ideals
inside the ACTUAL outer lens. AD2 provides an annulus fixed before
the canonical core filling varies. Keep MT outside M Omega_T.
Every canonical main filling then gives a distinct fine replacement,
recovered by restricting to the fixed inner main lens. By its bounded
end-lobe factor there are at least C_(k_M)/B_end choices. This proves
(8). The reference replacement region is exactly M Omega_T, not a
new nearby disk and not a presumed affine interior.

The same construction at M=1 works whenever its inner canonical
span is above the uniform main-lens threshold; for a fixed rational
frame this holds at every sufficiently large actual original L.
Together with (23), this gives the usual fixed-rational strict
upper/lower sandwich at every scale where actual references exist.
If references exist only on a subsequence, only that subsequence
lower conclusion is valid. No all-scale reference existence follows.

To bound the outer frame diameter and coordinate code by O(L),
impose q<=tL and L>=1/t as well as the uniform geometric thresholds.
All conditions are met by (4) after increasing one fixed C.
None changes epsilon_* after q is chosen. This completes every
all-D annulus/cutting/strict-transfer interface used in US_D2.

## 10. Same-density cancellation, not an entropy continuity claim

Keep one rational point, q and phase fixed. The EVERY-m bound (3)
and (7) imply

    log2|F|<=e[(1+2A0t)L+q]²+K0(tL²+L+1).           (28)

For each FIXED original L and reference, k_M tends to infinity.
The all-integer-size limit (23), along this sequence, and (8) imply

    liminf_M M^(-2)log2 R_M(T)
       >=e[(1−2A0t)L]².                              (29)

The q-floor error and constant log2 B_end vanish in this M limit.
Subtract the two squares. Their exact difference is

    8A0tL²+2qL(1+2A0t)+q²
       <=(12A0+3)tL²                                (30)

when q<=tL and t<=1. Since 0<=e<=H and L>=1/t,
K0(tL²+L+1)<=3K0 tL². With

    C_loss=H(12A0+3)+3K0,

we obtain

    log2|F|<=liminf_M M^(-2)log2 R_M(T)
                         +C_loss sqrt(epsilon)L².    (31)

The same receiving density e occurs on both sides. It need not be
known, continuous in J', or uniformly approached as q varies. The
supremum identity (23) supplies the upper bound at every finite m,
so no denominator-dependent convergence threshold in original L is
silently required.

## 11. Real tangents and the noncircular order of choices

Fix target eta>0. FIRST choose epsilon>0 so that all uniform geometry,
(25)/(27) and 1−2A0sqrt(2epsilon)>0 hold and
C_loss sqrt(2epsilon)<=eta. These constants were fixed from K,D
and the finite PHYSICAL frames before any rational denominator.

The required enlarged buffer has ||x−x0||<=C_box L, with C_box
uniform over finite frames for this bounded epsilon range. SECOND
choose a finite rational net J'_alpha in VJ'=I with errors
delta<=epsilon/C_box, small enough to remain in the same chart
domains, with row bounds G+1 and minors >=rho/2. Rational density
here is explicit: choose rows3,...,D rational near their old values,
then solve rows1,2 from VJ'=I using the first two columns
((1,0),(1,1)), whose 2-by-2 determinant is one. The resulting map
is rational and continuous, so approximations are dense.

To ensure shared cone charts, use compact assigned subsets strictly
inside the finite open chart domains from Section6. Each has a
positive distance to the complement of its chart. Choose a finite
delta/2-net in each assigned set and approximate those centers
rationally within delta/2 and that chart margin. Every J in K
therefore shares a physical frame with one of its approximants.
This is a finite net with a tolerance fixed BEFORE any q, not a
collection of arbitrarily shrinking denominator-dependent balls.

For that J and approximant put

    c_alpha=c+(J−J'_alpha)x0 in ker V.

On the whole buffered region the extra error is

    ||(J−J'_alpha)(x−x0)||<=epsilon L.

The actual epsilon L error relative to J becomes <=2epsilon L
relative to J'_alpha, with ONE common offset c_alpha for the full
family and reference. Enlarge the initial buffer constant by sqrt(2)
once so it contains the rational theorem's buffer at parameter
2epsilon. This enlargement was fixed before the net.

THIRD select one denominator q_alpha and common generic phase for
each net point, and FINALLY choose L0 to be the maximum of the
finitely many C(q_alpha+1)/sqrt(2epsilon) and geometric thresholds.
It is finite. The permitted epsilon never shrinks after these q's
are seen. Applying (31) proves (9), completing US_D3.

## 12. Scope, profile control and precise remaining obligations

Every inserted core is an arbitrary valid filling of its complete
boundary. For fixed D the finite tile derivatives give a uniform
Lipschitz constant for every coordinate of a full canonical lift.
Integration along segments in its convex full zonogon makes this
bound global. Old/new full lifts agree outside the changed patch,
whose diameter is O(L). Comparing at a shared boundary point gives
an O_D,K(L) height change throughout. At global scale p and local
span L<=lambda p this is O_D,K(lambda) in normalized profile. It
is not an O(epsilon lambda) bound and no flat inserted interior
is asserted.

All new assertions are for EACH FIXED D and a compact STRICT set
(1), with matching finite physical frames, actual full representatives,
one actual reference, whole buffers and one common affine offset.
They do not give uniformity as D grows or rho tends to zero. The
separate orientation, chart-window, single-pair and rank-mesh results
may later connect this to other strata, but are not premises here.
No general zero-row deletion theorem or all-D global assembly is
claimed or needed by this local strict statement.

The direct all-D proofs AD1–AD5 and the q-free transfer/cancellation
are the proposed extension. The accepted D4 annulus/ST/US bodies are
preserved, attributed method/provenance sources, not silently rewritten
as all-D theorems. DG and CUT already have fixed-D scope and are used
only with their exact full-tiling, coordinate, common-direction and
whole-buffer hypotheses. Root's unproved global induction draft is
not a premise. No source or finite evidence is substituted for any
of these unrestricted local proofs. Every proposed new conclusion
remains candidate-unverified until two fresh nonconstructor whole
audits and coordinator resolution.
