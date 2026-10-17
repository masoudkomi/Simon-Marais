# Whole initially blind audit of uniform strict D4 recovery

2026-10-17 UTC. Reviewer `review_2017_coarsening_r1`; requested
`gpt-6.1-sol` / `max`, effective-setting readback unavailable. This is a
fresh whole nonconstructor audit of US1--US3. The complete candidate,
construction log, source record and six-artifact manifest were read.
No other uniform-strict reviewer report, issue, source check or conclusion
was read before this report and its issue/source/integrity freeze.

**Disposition: no substantive defect found in the explicitly stated D4
compact-strict local scope.** This is a reviewer assessment, not promotion.
Only the coordinator may accept after the second independent whole audit.
Neither H, PR, a boundary-stratum theorem nor the official 2017 limit follows
from this packet alone.

The reviewer previously constructed the accepted annulus A1--A5 and some
fixed-D/rank-mesh background. Those are disclosed dependencies, not this new
uniform-denominator construction. I did not construct US1--US3, supply its
mechanical-word/denominator strategy or see a peer's new US conclusions.
I reconstruct below why the old fixed-data theorems suffice only after the
new constants and quantifiers have been checked.

## Target, official domain and dependencies

The target is the full 22943-byte
`notes/uniform-strict-reasoning-r1-candidate-v1.md`, SHA256
`643d0906e3eebee91dd91f53e5e1b241de35c3b7912d5010d2e651e830258c9d`.
Its manifest SHA256 is
`902b8ad01e994b03204673f55f647c2e03db80e8ac2b917faf514bc0ca249bbc`.
AGENTS.md and the local official statement were read, and official Paper B
p.2 B4 was checked directly. The official question concerns marked tilings
of a fixed regular 2n-gon for every n>=2 and the liminf/limsup of
n^-2 log2 C(n). A four-direction local entropy transfer is partial progress;
it is not that conclusion or a replacement of the full zonogon count by a
receiving patch count.

I read the complete accepted annulus v1.2, directed-geodesics v1.1,
lens-cutting v1.1, strict-transfer v1.1 and fixed-D structural v1.2 bodies.
Their scope/acceptance records were checked separately. In particular:
A2 needs ALL coordinate rank ranges, even for absent inner colors;
A3 needs containment, a common affine offset and its quantitative buffer;
CUT requires a WHOLE tiled neighborhood; and A5 counts the exact event-word
receiving family. None already asserts denominator-uniform transfer.
The rank-mesh repair and dimension-induction program are not premises.

## 1. Finite physical frames and numerical margins

Fix V with columns (1,0),(1,1),(1,2),(1,3). For J in the stated compact K,
all six ordered row determinants are at least rho>0. In particular the rows
are nonzero. Rotate the first row to angle zero: all later row directions
are in (0,pi); their pair determinants put them in increasing angular order.
They therefore lie in an open half-plane and admit a common strictly
positive physical direction. Two nearby independent rational directions
with positive determinant are possible, and scaling them gives one fixed
integer pair (u_h,v_h). Positivity persists on a neighborhood of J.

A finite subcover, with smaller balls subordinate to the open cone cover,
gives finitely many PHYSICAL pairs and uniform positive lower bounds for
all J_i u_h,J_i v_h in assigned neighborhoods. Upper bounds follow from
the row norm bound and the finite vector lengths. A small neighborhood in
the affine space VJ=I retains row norms <=G+1 and minors >=rho/2. Each pair
matrix has largest singular value <=sqrt(2)(G+1), so its least singular
value is at least sigma0=rho/[2 sqrt(2)(G+1)]. These constants precede
epsilon and any rational denominator.

Both physical vectors have positive first coordinate: u_x=sum_i J_i u.
Their positive determinant therefore gives a strictly ordered pair of
physical slopes. The separation constant for a concentric expansion is
at least det(u_h,v_h)/max(|u_h|,|v_h|). The finite minimum is positive.
Thus all graph slopes, transverse margins and corner constants can be
chosen from this finite list rather than from q u_h,q v_h.

## 2. Event-prefix error, phases and US1

For a rational J' in one assigned neighborhood choose ANY positive integer
q clearing J'u_h and J'v_h. Their q-scaled contents A,B are positive
integer vectors. A common phase theta_i in (0,1) avoids the finitely many
simultaneous-event hyperplanes for both segments. No lower bound on gaps
between distinct event times is needed.

For one U segment parameterized over [0,q], the prefix counts are
floor(t J'_i u_h-theta_i)+1. At 0 they are zero; at q they are A_i.
Their coordinate errors against t J'u_h are bounded by one, with the
proper one-sided values at an event. A path edge can be interpolated
between the two endpoint assignments; both height and straight parameter
interpolate, so this same bound holds along the edge. Since A and B are
integer vectors, complete-segment translations preserve every phase
threshold. Errors do not accumulate through U^m, W^n or their junction.

Writing h-H for this bounded error gives Vh-VH bounded only by V, and
h-J'Vh=(I-J'V)(h-H) bounded uniformly by the row norm bound. Thus physical
and affine boundary errors are independent of q and of an almost-tied
generic phase. The O(q) word length is never used as an error bound.

A4 comparability is valid with the scaled integral frame. In every i,j
projection the two straight boundary chains have positive determinant
q^2 det(J'_i,J'_j)det(u_h,v_h). At each i threshold the lower chain has
passed no more j thresholds than the upper one; the single shared phase
and integer junction shifts give the actual powers, not arbitrary words
with those contents. All six inversion inclusions follow.

At equal exponents the straight physical paths are the boundary of the
span-qm parallelogram. Their graph separation is a fixed positive multiple
of min(distance from left end, distance from right end,qm). Each digital
path has uniformly bounded physical/vertical error; its slopes lie among
0,1,2,3. Thus all contacts lie in two uniformly bounded end boxes. A
physical common vertex has the same prefix length on both words. Along
an inversion-creating swap chain a swap across that prefix strictly raises
its y value, and all other swaps preserve its whole prefix height. Equal
y therefore forces the identical lift at that common vertex.

For large qm the last contact in the first box and first in the last box
bound a genuine Jordan main lens, with the assigned common ranks. Remaining
lobes lie in the two bounded boxes. Their tile counts and number of
possible fillings are uniformly bounded by the integer origin/six-type
alphabet. Choices factor across the fixed common paths/vertices. Thus one
uniform B_end gives C_m/B_end<=Y_m<=C_m. The main lens contains a uniform
erosion of its straight parallelogram and is contained in a uniform
enlargement: graph error proves the side statement, and a fixed corner
erosion removes the contact boxes. This is stronger than merely asserting
Hausdorff closeness of arbitrary Jordan curves.

All weak lenses have diameter O(qm) in the finite frames. Recording at
each integer origin its subset of six possible tile types bounds
log2 C_m<=H(qm)^2 with one H, including small qm by increasing the constant.
A5 for this ONE fixed q,J',phase gives

    s=lim_m m^-2 log2 C_m=sup_m m^-2 log2 C_m.

Hence e=s/q^2 is in [0,H] and log2 C_m<=e(qm)^2 for EVERY m. This does
not need convergence uniform in q, continuity of e, or equality of e
between two different phases/periods. The exact block-swap proof of A5
was inspected: its k^2 patches have matching translated word boundaries
and disjoint shell interiors, so it is not a density-one packing claim
for arbitrary zonogons.

For arbitrary desired physical corner y and common c in ker V, round
J'y+c once to z in Z^4. Then Vz-y is uniformly bounded and
(I-J'V)z-c=(I-J'V)[z-(J'y+c)] is uniformly bounded. Translating the
physical frame by Vz and heights by z keeps one common offset. Trimming
a bounded end box changes the height by only boundedly many edges. There
is no independent corner or color rank reset.

## 3. Uniform CUT reconstruction and its code

Run CUT in u_h,v_h, not in q times these vectors. Set t=sqrt(epsilon),
N=ceil(1/t), ell=L/N, so tL/2<=ell<=tL for t<=1. A sample vertex differs
from the affine lift at the sample point by E<=t^2 L+C_tile. If
t<=kappa/8 and L>=8 C_tile/(kappa t), then

    2E<=kappa tL/2<=kappa ell.

DG1 therefore gives positive paths, and DG2's exact localization
M_V(K_dir ell+3E) is O(tL) with a uniform constant. All samples and these
bands lie in the WHOLE C_buf tL hypothesis region. The same deterministic
corner vertex is used by both incident sides. This supplies actual common
endpoints; independent phase choices for four sides are not assumed.

The two candidate positive paths contact only in O(tL) end boxes. For
small fixed t these boxes are disjoint; the prescribed last/first contacts
give comparable Jordan Omega_T. Its height is the original full-tiling
lift. The lens contains an erosion of P_L and is contained in an O(tL)
enlargement. Its lengths are O(L) because positive coordinate increments
telescope between endpoint heights whose errors are O(epsilon L+1).

The upper code uses a deterministic strip around the FOUR straight sides
of P_L of width O(tL+1). Rectangle and corner-box bounds give
O(tL^2+L+1) integer cells; a finite alphabet records all missing tiles.
No perimeter-only assertion for a multiply punctured arbitrary set is
used. Boundary words have O(L) letters. Subtracting ONE common integer
height nearest J'x0+c also shifts physical coordinates by its V image;
the desired corner then has bounded relative displacement. Relative
positions/heights of the recorded endpoint are O(L), so their cost is
O(log(L+2)). This explicitly resolves the absolute-offset range issue.
The output inner tiling plus boundary code and strip record recover the
original restriction. K_cut is uniform in q.

## 4. Both annuli, rank ranges, injection and US2

Let h=A0 tL. The canonical outer span q m_+ lies in
[L+2h,L+2h+q). Center its straight parallelogram at P_L's center and use
the single rounded integer translation just checked. Choose A0 from the
finite shape margin so it dominates the uniform CUT displacement. For
large L the bounded canonical/rounding errors are also absorbed. Ceiling
overshoot only enlarges this outer frame. The entire actual inner lens
is contained in the canonical main lens with vertex buffer b0 tL.

The two boundary errors relative to the SAME J'x+c are <=epsilon L and
one uniform E_can+C_round. Thus A3 applies provided

    sigma0 b0 tL>sqrt(2)(E_can+C_round+t^2 L).

Choose t small from the uniform constants, then L>=C/t. The six projected
winding tests first give every relative coordinate rank box, including
absent colors, and then ideality. Corrected A2 constructs a genuine tiled
annulus fixed from the boundary before its filling varies. Fixed end-lobe
fillings produce an output in C_(m_+). Its restriction plus the upper code
recovers each input restriction; the bound (U) follows. One never infers
rank compatibility from physical nesting alone.

For insertion, Omega_T is extracted ONCE in the original reference.
Dilate every reference tile by the integer M and subdivide it into its
M-by-M same-type grid. Adjacent subdivisions agree on shared edges; lifted
coordinates equal M times the old interpolated lift. The complete boundary
of M Omega_T and the full reference exterior are therefore fixed exactly.
The boundary has error epsilon ML from J'x+Mc and contains the eroded
parallelogram with the scaled CUT band.

The inner canonical span q k_M<=ML-2A0 tML, concentrically placed and
rounded by one integer vector, has the same lower buffer inside this
actual outer lens for all sufficiently large M. A3 now has error roles
exchanged. The actual outer boundary is comparable and Jordan because
the same typewise subdivision preserves its boundary words and positive
edge geometry. A3 gives the full relative rank box and ideals; A2 gives
one annulus independent of the chosen core filling. The original exterior
of M Omega_T is unchanged. Every canonical main filling is recovered by
restriction to that fixed core, proving (I), with B_end only a bounded
factor. The receiving region is exactly M Omega_T, not a new cut per M.

The further conditions q<=tL and L>=1/t ensure the upper frame has
diameter O(L) and absorb rounding. All thresholds can be bounded by
C_*(epsilon)(q+1), with C_*(epsilon)=C/t for a large uniform C. The
admissible epsilon, buffer, code, lobe and density constants are independent
of q; only the required original scale grows with it.

## 5. Same-density cancellation and US3

Keep J',q,phase fixed. US1 and (U) yield

    log2|F|<=e[(1+2A0 t)L+q]^2+K0(tL^2+L+1).

For each fixed ORIGINAL L and T, as M tends to infinity the floor-defined
k_M tends to infinity and q k_M/M tends to (1-2A0 t)L>0. A5 and (I) give

    liminf_M M^-2 log2 R_M(T)>=e[(1-2A0 t)L]^2.

The q rounding and bounded lobe factor vanish in this M limit. No lower
convergence rate in the original L is used. The SAME canonical e occurs
in both inequalities; its value need never be identified or continuous.
Their squared-span difference is exactly
8A0 tL^2+2qL(1+2A0 t)+q^2, at most (12A0+3)tL^2 for q<=tL,t<=1.
Also K0(tL^2+L+1)<=3K0 tL^2 for L>=1/t. Since e<=H, (R') follows with
the displayed uniform C_loss.

Given eta, choose epsilon first so C_loss sqrt(2epsilon)<=eta and all
uniform smallness bounds hold. Approximate K by a finite rational net in
VJ'=I to accuracy epsilon/C_box in the assigned physical charts.
Rational density here is explicit: the first two columns of V form a
unimodular 2-by-2 matrix, so the last two rows of J' may be chosen rational
and its first two solved rationally. Compactness then supplies a finite
subordinate net, retaining strict margins. It is not an assumption about
entropy continuity at real slopes.

For J matched to J', put c'=c+(J-J')x0; Vc'=0. On the WHOLE buffered
region the change of affine function is bounded by epsilon L. A source
error epsilon L relative to J becomes <=2epsilon L relative to J', with
the SAME c' for the source family and reference. Increase the original
buffer constant by sqrt(2) beforehand to contain the 2epsilon input
buffer. Choose one period/phase for each net point, then choose L0 as the
maximum of the finitely many thresholds. Thus epsilon is never shrunk
after seeing the q's. Applying (R') proves US3 for every actual L>=L0
and its existing actual reference, without asserting references exist at
all original scales or that arbitrary replaced interiors remain flat.

## 6. Degeneracies, attribution and residual scope

I checked: arbitrary large/nonminimal q; phases approaching forbidden
ties; small qm before main-lens trimming; very large absolute offsets;
real original L; k_M nonpositive at early M (the insertion is expressly
eventual); e=0; K containing many physical cone charts; and one fixed
original reference used through every integer dilation. None requires a
uniform convergence rate. Ties themselves are excluded, epsilon=0 is not
claimed, and zero minors/zero rows/antiparallel strata are outside K.
Empty source families satisfy an upper count trivially, with log0=-infinity;
the operative comparison assumes the stated actual reference exists.

Fixed prototiles bound all coordinate gradients. Old and new full lifts
agree outside the modified patch and are Lipschitz on their common convex
zonogon. A point in a patch of diameter O(L) is O(L) from its boundary,
so the height change is O(L); normalized at global p it is O(L/p).
No epsilon factor is manufactured for arbitrary inserted interiors.

The only external geometric method entering through DG is the published
Arroyo--McQuillan--Richter--Salazar arc-dual path lemma. Its actual arc
definition and full Lemma2.2 proof were checked directly; it allows
noncrossing parallel arcs. The disk-relative cell identification is the
separately accepted DG adaptation, not an asserted projective theorem.
A5 is the project's explicit block-shell argument, not a free-boundary
or thermodynamic-limit import. No new external entropy theorem, routine
enumeration, mathematical program, CAS, author rerun or empirical test was
used in this audit.

The full local US argument passes this reconstruction under its exact
buffer/common-offset/reference/compact-strict D4 hypotheses. The unresolved
boundary strata, multiple-window/global assembly and full H/PR conclusion
remain separate. Source/integrity records accompany this report, and all
earlier frozen author/review bytes are preserved.
