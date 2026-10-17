# Uniform recovery in every fixed direction count and the scalar official limit

2026-10-17 UTC. **Candidate proof - unverified.**
Constructor: /root/review_2022_complexity_r2. The coordinator supplied
the induction/assembly strategy and is a co-constructor for review
purposes. TWO OTHER initially blind whole nonconstructor audits are
required; neither the constructor's earlier local audits nor the
coordinator's inspection can replace them. No novelty is claimed.
No mathematical enumeration, CAS or computational certificate is used.

The precise strict premise S_D is the COMPLETE all-D local packet
notes/allD-uniform-strict-reasoning-r1-candidate-v1.md,37267B,
SHA-256 fc280881b1df650d07ab48f0f4c19d0e77f076e6b39a13f3a0b8d9969074a433.
It had two frozen independent whole initial audits and pending
coordinator reconciliation at the start of this construction, so
the construction initially treated it as an EXPLICIT conditional
premise. During construction the coordinator completed reconciliation
and separately accepted its exact unchanged body in
proofs/reviewed-allD-uniform-strict-v1.1.md,39136B,
SHA-256 a5ebfd81d59b26f301b1e105889451f4c86262da80e6e77e6913c045d71147d2.
The suffix was independently byte-compared here. All named local
premises are therefore accepted at this freeze, on their exact
scopes. The NEW GLOBAL argument remains candidate-unverified and
requires its own two whole audits; local acceptance does not promote it.

The coordinator's all-D induction draft is an unverified outline,
NOT a theorem premise. The G4 special case received separate D4
acceptance during construction, but is likewise NOT a premise here.
Every global argument needed below is supplied for symbolic fixed D.
In particular no CKP/dimer/variational theorem or UR3 is imported.
The base is elementary UR2. The final official consequence is
existence/equality of its two scalar rates, not a numerical value
and not a complete answer determining that value.

## 0. Definitions, exact premises and proposed conclusions

Fix an integer D>=2, v_i=(1,i-1), and V=[v_1 ... v_D].
Write Z_N=sum_i[0,N_i v_i], where N_i are nonnegative integers.
At least two directions are active whenever a positive-area disk
is considered. Full actual marked tilings use the fixed integer
parallelogram types ij. Their canonical continuous affine-on-tiles
lift a satisfies Va(x)=x, with a(0)=0 at the marked initial corner.
Translations are normalized by that corner; a height translation z
is accompanied by the physical translation Vz. No rotation,
reflection or rank permutation quotient is taken.

A complete disk boundary specifies its physical Jordan polygon,
oriented color word on every edge, and inherited canonical integer
heights/ranks. A filling always means an actual edge-to-edge tiling
of that fixed disk with that complete boundary. Let Z_D(B) be its
count. For integer M>=1, MB has the M-fold physical boundary,
heights multiplied by M and each old color edge replaced by M
unit edges at consecutive ranks. A reference filling enlarged
tilewise and subdivided into M-by-M grids makes Z_D(MB)>=1.

For C>0,r>=1 define GE_(D,C)(r) to be positive-area Jordan tile
disks B with perimeter<=Cr for which there is ONE actual full
Z_N tiling with every N_i<=Cr, and ONE fixed tiled exterior of B,
such that EVERY filling of B glues to that same exterior.
Zero ambient contents are allowed. Diameter bounds alone or one
extendable subfamily of fillings do not define this class.
The counts and deficits are invariant under consistent marked
translations. Put

    Lambda_D(B)=liminf_(M->infinity) M^-2 log2 Z_D(MB),
    Delta_D(B)=max(0,log2 Z_D(B)-Lambda_D(B)).

The finite alphabet bounds the logarithms by squared diameter of
the fixed full exterior, so these quantities are finite.

**UR_D (proposed).** For each fixed D>=2 and each fixed C>0,

    eta_(D,C)(r):=sup_(B in GE_(D,C)(r)) Delta_D(B)/r² ->0.   (G1)

Use supremum zero for an empty class. No rate uniform in D or C
is asserted, and no finite exact quadratic supermultiplicativity
is asserted.

**Balanced consequence (proposed).** For each fixed D>=2, if
B_D(p) counts ALL full marked tilings of Z_(p,...,p), then

    k_D=lim_(p->infinity) p^-2 log2 B_D(p) exists,
    ell_D=k_D/D².                                        (G2)

**Official scalar consequence (proposed).** For the official marked
regular-polygon count C(n), n>=2,

    liminf_n n^-2 log2 C(n)=limsup_n n^-2 log2 C(n)=L,
    ell_D<=L<=ell_D+h2(1/D)+1/D for every D>=3,
    ell_D->L as D->infinity.                             (G3)

No numerical value for L or ell_D is supplied.

Inputs and their firewall:

1. FD: full marked integer/de Bruijn dictionary, finite local
   alphabet, bounded tile gradients, compact necessary K_D and
   uniform-limit distributional minor closure.
2. RM1: general fixed-D selected-face Jordan blocks, exact
   residual ports, diameter and AGGREGATE perimeter/area bounds,
   in the fully repaired accepted rank-mesh packet.
3. OC: finite cyclic reorientation, including zeros/antiparallels;
   exact full BALANCED marked transformations, positive physical
   direction replacement, bounded A,A^-1 and common affine offset.
4. FL1: boundary Green estimate for rare zero-minor tile counts,
   retaining O(epsilon L²+L+1).
5. LW1: LOCAL rank-mesh code at arbitrary global contents, one
   absolute height anchor, actual global interior faces, actual
   one-Jordan fringe and fixed complete residual boundaries.
6. CW0–CW4: exact common translations; winding-based fixed target
   cores/WHOLE buffers; all-source-tile anchored recovery; exact
   full inverse of replacements and EVERY integer dilation.
7. SP1–SP3: ONE consecutive pair with all D-2 other COLOR groups
   singleton; closed-face incident cleanliness; actual coarse
   Jordan disks/two ports; whole-count bijection at EVERY M;
   inactive-curve deletion and ONE small full exterior.
8. S_D: the exact compact-STRICT all-D AD1–AD5/US_D1–US_D3
   packet above, with q-free constants, its every-m upper
   supremum identity and exact one-reference dilation comparison.
9. RP1–RP3: balanced monotonic padding and passage from ALL
   sufficiently large multiples of one fixed base to all integers.
10. DC1/DC2: the already reviewed finite direction-coarsening
    count comparison, balanced entropy error and conditional
    implication from full balanced fixed-D limits.

Items1–10 are now accepted in their exact local/finite scopes,
including item8's separate unchanged-body acceptance during
construction. D4-only clean/strict conclusions are not used as
general-D theorems. The lower-dimensional premise in the induction
is (G1) for the EXACT GE class, not H_(D-1) alone.

## 1. Elementary bounds, actual boundary tubes and balanced exteriors

Let d_D be a maximal tile diameter. At fixed D there is a finite
integer-origin alphabet: for every lattice cell record all nearby
tile origins/types. It reconstructs a tiling and has a fixed
finite number of symbols. A simpler presence-bit record at all
possible integer origins also suffices when a known region is given.
In a diameter-O(p) box this costs O_D(p²+1) bits.

If Gamma is ONE rectifiable closed curve of length P, its fixed-width
neighborhood has O_D(P+1) possible lattice origins. Sample its
arclength at spacing one; O(P+1) bounded-radius disks cover that
neighborhood, and each disk contains boundedly many lattice points.
At width rho>=1 the same argument at spacing rho gives
O_D(rho P+rho²) lattice origins. This statement charges an actual
one-curve neighborhood, not an arbitrary multiply connected set.

For a bounded region E whose actual boundary is a finite list
Gamma_0,...,Gamma_m, the possible tile origins for tiles meeting E
are bounded by

    O_D(area(E)+sum_t length(Gamma_t)+m+1)              (1)

at fixed tile width. Indeed unit cells wholly inside E cost its
area; all remaining relevant cells meet the corresponding fixed-width
boundary tubes. Actual component terms and perimeters are summed.
We use (1) only with one finite B boundary and a fixed finite list
of window sides. No unbounded number of holes is given one charge.

A tileable Jordan disk A consisting of t reference tiles has
area(A)>=t and perimeter(A)<=4d_D t. Equation(1) therefore gives

    log2 Z_D(A)<=c_D area(A).                          (2)

The additive constant is absorbed since t>=1. Locations are known
from the fixed boundary; there is no coordinate code for every
alternative tile or every disk. This is also valid for the standard
lower-direction disks, with their own fixed-dimensional constant.

Here is a complete count-injective padding for unbalanced contents,
including zero contents. Add [0,v_i] to the convex full Z_N. On a
line of transverse coordinate t=det(v_i,x), its old section is one
interval parallel to v_i. Minkowski addition keeps the left endpoint
and moves the right endpoint by v_i. The positive-v_i visible chain
starts at N_i v_i+sum_(j<i)N_j v_j, follows +v_j for j>i and
then -v_j for j<i in cyclic boundary order, and ends at
N_i v_i+sum_(j>i)N_j v_j. Zero-length color blocks are skipped.
Every such unit step strictly increases t. Extruding each step by
v_i gives the actual ij parallelogram between its old/new visible
sections. Their transverse intervals have disjoint interiors and
are consecutive, so these tiles fill exactly the new belt without
overlap. Extreme support segments parallel to v_i add no area;
the endpoint v_i edges are precisely the new support extensions.

The visible chain has canonical a_i=N_i throughout. In the belt
let a_i run from N_i to N_i+1; all other increments agree with
the old visible unit steps. Thus the new i-rank is N_i+1,
negative -v_j orientations carry their original j-rank in reverse,
and every seam has identical full heights on both sides. Old
physical positions, old ranks and a(0)=0 remain fixed. The belt
depends only on the old full boundary, not its filling.

Iterate to p=max_i N_i. The result is one fixed balanced Z_p
exterior for every filling of B, with p<=Cr. At least two old
directions are active because B has positive area; additions
preserve nondegeneracy. Adding a previously absent color causes
no exception. Already maximal colors need no belt. Restriction
to the old region recovers each filling. This also proves
coordinatewise monotonicity of full B(N_1,...,N_D).

For M we will dilate this ONE chosen padded reference and use
its grids. Padding after dilation need not coincide with
dilation of a separately rerun algorithm, and no such assertion
is used. The physical disk MB and its complete multiplied
boundary are the same ones in its count definition.

## 2. Base UR2 and the exact induction hypothesis

For D=2, V is invertible. Every canonical height is V^-1 x,
so integer vertices and unit tile edges form the unique coordinate
grid in the full two-direction parallelogram. Any alternative
filling of a GE2 disk glues to its fixed full exterior, hence
would be a different full grid tiling, impossible. Its count
is one. The reference M-grid supplies a filling of MB and
the same argument gives Z_2(MB)=1 for every M. Therefore
Delta_2(B)=0 and UR2 holds with eta_(2,C)=0, for every C.
No dimer entropy theorem is needed.

Now fix D>=3. Assume UR_(D-1) for EVERY fixed C'>0,
on the exact GE_(D-1,C') class just defined. The induction
step below proves UR_D for each chosen C. All constants
may depend on this fixed D,C and on a hypothetical positive
deficit, but not on the eventual index j or dilation M.
There is no simultaneous-limit assertion in D.

Suppose UR_D fails. Choose a>0, r_j->infinity and
B_j in GE_(D,C)(r_j) with

    Delta_D(B_j)>=a r_j².                             (3)

Use section1's one fixed balanced extension, with p_j=max N_i.
The alphabet gives log Z_D(B_j)<=K_D p_j². Since each
Lambda_D(B_j)>=0, (3) forces

    sqrt(a/K_D) r_j<=p_j<=C r_j.                       (4)

In particular p_j->infinity, the boundary lengths divided by
p_j are uniformly bounded, and

    Delta_D(B_j)/p_j²>=a/C².                          (5)

After dividing positions/heights by p_j, the full domain is
the SAME convex Z_D=sum_i[0,v_i]. Let A_D=area(Z_D)<infinity.
Every filling is extended through the SAME chosen exterior
for that j; this extension is injective.

## 3. Actual varying Jordan disks and the common profile fiber

Parametrize partial(B_j/p_j) positively by constant-speed
arclength on [0,1]. Uniform length and ambient bounds give
a uniformly convergent subsequence gamma_j->gamma. Its
limit is Lipschitz and rectifiable, possibly with self
contacts/retracing, and its image has planar area zero.

For any x outside gamma's compact image, uniform closeness
makes the straight homotopy from gamma_j to gamma avoid x
eventually. The winding equals the old Jordan winding,
zero or one. Let Omega be the winding-one open set away
from gamma. Each compact K inside Omega is eventually in
B_j/p_j: its distance from gamma is positive, and the same
homotopy argument is uniform on K. Indicators converge
pointwise off gamma, so bounded convergence gives

    area(B_j)/p_j² ->area(Omega).                     (6)

The limit need not be Jordan or connected. Every FINITE
B_j still is a Jordan disk. If area(Omega)=0, section1's
alphabet in B_j and the actual one-boundary O(p_j) tube
give log Z_D(B_j)=o(p_j²), contradicting (5).
Hence the relevant case has positive area.

Every extended normalized vector lift h_T(x)=a_T(p_jx)/p_j
on Z_D has a common extrinsic Lipschitz bound G_D and
coordinates in [0,1]. These facts use the convex FULL
zonogon, not intrinsic paths in a ragged B_j. A delta mesh
of the fixed domain has O_D(delta^-2) sites. Quantize D
values at those sites; the Lipschitz bound controls the
rest. Consequently these profiles have a sup-norm cover
with

    log2 N(delta)=O_D(delta^-2 log(2/delta)).

Put delta_j=1/log(p_j+2). Its logarithmic cover size is
o(p_j²). Partition the Z_D(B_j) extended fillings by
this cover and choose a largest fiber A_j. Then

    log Z_D(B_j)<=log |A_j|+o(p_j²).                   (7)

Choose one actual profile h_j in A_j. By compactness a
subsequence converges uniformly to h on Z_D. All profiles
in A_j differ from h_j by O(delta_j), so EVERY member
of this one fiber converges to the SAME h. No separate
profile selection will be made in different windows.

We have Vh=x. The accepted distributional identity

    det(grad f,grad g)
      =partial_1(f partial_2 g)-partial_2(f partial_1 g)

and bounded derivatives pass nonnegative row minors to
the uniform limit. Hence Dh(x) belongs almost everywhere
to the compact necessary slope set

    K_D={J:VJ=I, det(J_i,J_j)>=0 for i<j}.

It is only a necessary condition. We do not use convexity
of K_D, realizability of arbitrary necessary profiles,
smoothing or a variational entropy formula. At a
differentiability point x0 set J=Dh(x0),
c0=h(x0)-Jx0. Then Vc0=0.

## 4. Local strict and boundary mechanisms, with exact area budgets

We establish the local comparisons needed later, keeping their
constants and parameter order separate from the global selection.
The outer unit shapes below have area in [mu,M0] and bounded
diameter/perimeter/eccentricity. Boundary shapes enjoy such bounds
depending only on D; strict shapes get them after a compact strict
class has been fixed. A physical outer window has span ell and
area at least mu ell². Its inner homothetic copy has factor
1-theta, with 0<theta<1/4, and an intermediate copy has factor
1-theta/2. All centers and shapes are fixed across a source family.

### 4.1 Strict windows from the exact S_D premise

On K_(D,rho)={J in K_D:min_(i<j)det(J_i,J_j)>=rho},
S_D supplies finitely many physical integer frames, uniform
q-free C_buf,C_cut,C_loss, and the denominator-safe rational
construction. The full body gives the quantitative bound

    log |F|<=liminf_M M^-2 log R_M(T)
                    +C_loss sqrt(2epsilon) L²          (8)

after the real-tangent net step. R_M(T) fills the EXACT M-dilation
of one extracted original reference lens. Choose epsilon first
so this loss is at most zeta mu L²/8, and also so both
C_buf sqrt(2epsilon)L and C_cut sqrt(2epsilon)L are smaller
than a quarter of the intermediate-to-outer support margin.
This is possible using the proof's free small epsilon and its
q-free constants, before any rational period.

Choose the finite rational net, periods and phases only AFTER
that tolerance, as in S_D's explicit real approximation proof.
These affect L0, not epsilon. On the outer source window assume
a common affine error small enough (for example epsilon ell/4,
with fixed norm conversions) to imply (8)'s error on its
WHOLE intermediate-window buffer. This buffer is inside the
outer source window. The intermediate span L<=ell and its
restriction recovers every source tile meeting the inner
window once its fixed tile margin is absorbed at large scale.

For any actual common-family reference T, its extracted
closed core C_s(T) lies strictly inside the outer window.
With N_s counting distinct restrictions to the intermediate
window, S_D gives

    log N_s<=Lambda_s+tau_s,
    Lambda_s=liminf_M M^-2 log Z_D(M C_s(T)),
    tau_s<=zeta area(outer window)/8.                  (9)

It is valid for ANY such actual T, so that T may be chosen
only after global conditioning. New interiors need not
remain affine. No entropy continuity or all-scale original
reference existence has been inferred.

### 4.2 Every non-strict tangent uses exactly ONE adjacent pair

At J in K_D with a zero ordered minor, apply one OC cut.
Its signed permutation S and full direction replacement
give A=W S J, invertible, and J*=S J A^-1. Compact K_D
and the finite cuts bound A,A^-1,J* and the error map
uniformly, even at zero minors. No nonzero-row lower bound
or strict-pair margin is used here.

If J* has a zero row, pair it with one adjacent slot,
including another zero row if that is the neighbor.
If it has no zero rows, a zero minor is positive parallelism
after OC; positive parallel groups are consecutive, so one
adjacent pair exists. Merge JUST that pair k,k+1.
ALL other D-2 COLOR groups are singleton, even when their
tangent rows are zero or parallel to others. Rank two
follows from WJ*=I. We use neither simultaneous several
merged groups nor a claim that every boundary stratum
has zero entropy.

Choose a centered target square and its affine inverse
as the source outer shape. Uniform A,A^-1 bounds make
these shapes regular with positive area bounds. Take
a target square P intermediate between affine images
of the inner and outer source windows.

For a common source affine error <=epsilon_source ell,
CW0 gives image displacement <=C_D epsilon_source ell
and target lift error <=C_D epsilon_source ell with
one COMMON target offset. Choose this tolerance small
relative to theta. For large ell the fixed source/target
tile diameters and target star width are also dominated
by the collar. CW1's winding argument then puts P and
its ENTIRE fixed-width enlargement in EVERY actual
outer-window image. In addition

    A(inner source window+B_(d_D))+b
                       +B_(C_D epsilon_source ell) subset P. (10)

This is the explicit whole-tile margin of CW2. Hence all
original tiles meeting the source inner window are
recoverable from the target P restriction and one
canonical target anchor. Four-corner inclusion or
Hausdorff closeness alone is not being substituted.

### 4.3 Rare count, LOCAL mesh and small full lower-dimensional class

In target coordinates the selected pair minor is zero.
FL1 on P and its fixed tile-star enlargement gives

    S_rare<=K_D(epsilon_target L²+L+1),               (11)

where L is P's side, uniformly comparable to ell.
The error bound is available on the whole needed
boundary by (10)/CW1/CW0'. The L+1 term counts cut
or touching tiles; rare events need not lie in a band.

Choose an integer rank spacing r0>=2 fixed BEFORE L
grows. Apply the accepted LOCAL LW1 theorem, not
the global-content skeleton code M2. The ambient
content may be arbitrarily larger than L. It gives
a code of at most

    kappa_L<=K_D[L²/r0+epsilon_target r0² L²
                 +r0² L+r0 L+r0²+log(R+2)]            (12)

bits, after absorbing (11). It fixes the whole local
skeleton, discarded bad data and one-Jordan fringe,
and the complete lifted boundaries of all remaining
RM1 biconnected Jordan disks. Retained faces are
ACTUAL global selected faces, not cut-window pieces;
their number is O_D((L/r0+1)²).

The one absolute trace anchor is retained in log R.
Together with a completed good-disk filling and its
fixed boundary it determines absolute heights throughout
the reconstructed target restriction. Thus CW2's
deterministic target anchor is computable from that
same reconstructed lifted record; no independently
unbounded anchor is needed per disk. Allowing an
extra O(log R) per window instead would give the
same bound. Later R can be chosen C_D p.

RM1 is used as a GLOBAL arrangement statement
(ambient scale p, with contents p), not by pretending
the local contents are O(L). Its spacing conclusions
give n_F<=D(r0-1), total area O_D(r0²) and aggregate
block perimeter O_D(r0) in one selected face.
LW1 supplies the genuinely local face/code count.

In a retained good F, its WHOLE closure and incident
tiles avoid the chosen pair, including forbidden
tiles outside an individual disk touching a vertex.
Its closed stars are in the actual full tiled domain.
SP1–SP3 therefore apply: coarsening exactly this pair
embeds every closed residual disk as an actual
Jordan disk Qbar with two complete fine ports
for every active coarse rank, at most D(r0-1)
active curves, and an EXACT bijection

    Z_D(B_tar)=Z_(D-1)(Qbar),
    Z_D(M B_tar)=Z_(D-1)(M Qbar) for EVERY integer M.  (13)

The other groups are singleton, as required even
when their tangent rows coincide. The singleton
barrier return argument is the accepted reason
one coarse curve has one visit/two ports. Boundary
recoloring fixes all fine ranks, and zero boundary
pair flux rules out forbidden tiles in EVERY fine
alternative filling. This is not arbitrary insertion
after deleting even one forbidden event.

Deleting inactive full coarse curves changes this
connected disk only by a fixed translation and rank
shift. It supplies ONE full standard (D-1)-direction
exterior with O_D(r0) curves per color, valid for EVERY
filling. Its actual perimeter is O_D(r0). This is
precisely GE_(D-1,C_D)(r0) for one fixed C_D.
Zero ambient contents are allowed in its definition;
alternatively section1's fixed belts balance it at
content <=C_D r0 without changing its disk or count.
After any once-chosen translation/rank normalization,
its dilations multiply that same data; no new
outside matching is chosen at M.

Our induction hypothesis, with THIS C_D, now gives

    Delta_D(B_tar)=Delta_(D-1)(Qbar)
                  <=eta_(D-1,C_D)(r0) r0².           (14)

Only an actual GE recovery theorem justifies this.
A balanced lower-direction limit alone would not.

### 4.4 Correct aggregate loss and the order beta,r0,epsilon,L

There can be many blocks in ONE face. Write
eta_-(r0)=eta_(D-1,C_D)(r0), which tends to zero.
For a threshold beta r0² in TARGET fine physical
area, sum small-block areas using isoperimetry:

    area(B)<beta r0² implies
    area(B)<=sqrt(beta) r0 sqrt(area(B))
            <=sqrt(beta) r0 perimeter(B)/(2 sqrt(pi)).

Aggregate perimeter O_D(r0) therefore gives total
small area O_D(sqrt(beta)r0²). By (2) their entire
log count is bounded by this area times a fixed
constant, so their deficits can be charged by that
quantity, using the trivial lower count one.

At most O_D(1/beta) other blocks occur, because
total area is O_D(r0²). Each uses (14). Fine and
coarse unit tile areas are comparable by fixed
D constants; all perimeter/GE constants are
uniform over the finitely many adjacent pair choices.
Thus the total deficit in one face is

    K_D[sqrt(beta)+eta_-(r0)/beta] r0².

Across the local LW face bound this yields

    sum_b Delta_D(B_(tar,b))
      <=K_D[sqrt(beta)+eta_-(r0)/beta]
                          (L²+r0 L+r0²).             (15)

Combine (12) and (15). Given a desired loss zeta
per SOURCE outer area, first choose beta small;
then choose integer r0 large so eta_-(r0)/beta
and 1/r0 are small; then choose epsilon_target
small so epsilon_target r0² is small. Respect
the fixed theta/CW margins by decreasing the
source tolerance BEFORE window radii/strict periods.
Since source area>=mu ell² and L/ell is bounded,
these choices give uniformly over code classes
and their actual references

    kappa_L+sum_b Delta_D(B_(tar,b))
       <=zeta area(source outer window)/4
           +O_(D,beta,r0,shapes)(ell+1)
           +O_D(log(R+2)).                            (16)

Numerical fractions are chosen with spare room;
strict errors in (9) can be included in the
same total per-area budget zeta. This pays tiny
blocks by area and large blocks by the actual
inductive deficit; multiplying an arbitrary
block number by r0² is not done.

At fixed r0,beta all fringe, perimeter, constant
and logarithmic terms are lower order as ell
grows. A finite collection pays its SEPARATE
r0 P+r0² charges and anchors. No unbounded
collection of holes/windows is paid once.

## 5. All parameters and a genuinely fine finite Vitali selection

Return to the limiting h and Omega from section3. All selections
in this section concern this ONE limit, before the physical
indices grow. Let c_D be a sufficiently large alphabet constant
for (1). Choose 0<delta,theta<1/4 with

    c_D(2delta+2theta A_D)<a/(8C²).                   (17)

Choose a target total local per-area allowance zeta>0 with

    zeta A_D<a/(8C²).                                (18)

These choices precede strict truncation and shape constants.
The outside area coefficient c_D does not depend on those
later constants; actual boundary lengths will be lower order.

At differentiability points write J(x)=Dh(x). On the strict
set E_s={x in Omega:min_(i<j)det(J_i,J_j)>0}, the sets where
this minimum lies in (0,rho) decrease to empty as rho->0.
Choose rho so their area is <delta. Retain strict points
with minimum >=rho and all differentiability points of the
exact boundary set where the minimum is zero. The omitted
area in Omega is <delta, apart from a null set.

If the retained strict set is nonempty, K_(D,rho) is a
nonempty compact strict class and we fix its S_D physical
frames. Otherwise no strict theorem is invoked. OC provides
uniform boundary-shape bounds as in4.2. The union of these
shape collections has unit areas >=mu>0, uniformly bounded
diameter/perimeter/eccentricity; mu may depend on D,rho.
Empty strata cause no difficulty.

For the strict part choose its small epsilon and uniform
constants to meet both (9)'s per-area budget and the theta
collars. For the boundary part use (16): beta first, then
integer r0 using the induction hypothesis, then target/source
epsilon small for epsilon r0² and all theta/CW margins.
One can order these without a period loop as follows:

    delta,theta,zeta;
    rho and all unit-shape bounds, including mu;
    beta, then r0;
    strict and boundary epsilon caps, then ONE small
        source tolerance tau meeting every cap;
    S_D finite rational nets, denominators and phases;
    normalized window radii/finite selection;
    original large-j threshold;
    finally M->infinity with j fixed.                (19)

In the strict construction take the free epsilon in S_D's
proof small enough from the outset for both its collar and
loss caps. Rational nets are constructed only after this
choice, and no denominator requires a later shrinkage.
The common source tolerance tau can be fixed before those
nets by the explicit q-free formulas of4.1. The boundary
tolerance depends on fixed r0,theta, not on a local radius.

At each retained good point x_alpha use its fixed shape:
strict finite physical frame, or the affine inverse by its
chosen A_alpha of a centered target square. Differentiability
gives arbitrarily small span ell>0 with closure in Omega and

    sup_(x in W(x_alpha,ell))
      ||h(x)-J_alpha x-c_alpha||_infinity
                      <=(tau/4) ell,
    c_alpha=h(x_alpha)-J_alpha x_alpha in ker V.       (20)

The whole OUTER window is controlled. Planned strict
buffers and target-core source preimages are kept inside
it by the earlier collar choices. Bounds on diameter/
eccentricity convert differentiability in balls to (20).
These centered closed parallelograms form a fine family.

Here is the required regular Vitali argument. Choose disjoint
closed members greedily, each with diameter at least half
the supremum still available. All lie in bounded Omega and
area>=c diameter² for a common c>0. Their total area is
finite. A candidate disjoint from the first n members must
eventually intersect a later chosen member of diameter at
least half its own: if it stayed available forever, infinitely
many disjoint chosen sets would have a positive area lower
bound. For an uncovered point, fineness gives an arbitrarily
small candidate away from the first n closed sets. It is
therefore in a fixed-radius ball about some later chosen
set's center, with radius a fixed multiple of that set's
diameter. The area of this enlarged tail is bounded by a
fixed constant times the original tail area, tending to zero.
Thus the uncovered good set has outer measure zero.
No unbounded-eccentricity rectangle theorem is assumed.

A finite subcollection W_1,...,W_m therefore satisfies

    closures disjoint, W_alpha compactly inside Omega,
    sum_alpha area(W_alpha)>=area(Omega)-2delta.       (21)

Indeed the countable union covers the good set except a
null set, and a finite partial sum loses less than delta
of its area. Denote its inner homothetic windows by
W_alpha^-=(1-theta)W_alpha about the same center. Then

    area(Omega)-sum_alpha area(W_alpha^-)
                        <=2delta+2theta A_D.          (22)

If the finite list is empty the same estimate holds when
area(Omega)<=2delta; all local products below are one.

Every physical W_(j,alpha)=p_j W_alpha is eventually
inside B_j, as is its closure. Its span ell_(j,alpha)
=p_j ell_alpha tends to infinity. All profiles in A_j
are uniformly within o(1) of h, so for all sufficiently
large j and EVERY full representative in A_j,

    sup_(x in W_(j,alpha))
       ||a(x)-J_alpha x-p_j c_alpha||_infinity
                            <=tau ell_(j,alpha).     (23)

There is one common offset per window, across the entire
source family; no tiling-dependent shifts are chosen.
The finite list permits (23), all strict rational period
thresholds, all fixed tile/star margins, and all large
window assumptions simultaneously. Radii, r0 and periods
are already fixed. No uniform differentiability modulus
for a family of unrelated h is being asserted.

## 6. Original outside information and joint conditioning

Record the original finite alphabet for every tile meeting
the complement in B_j of the INNER physical windows
W_(j,alpha)^-. Include the fixed-width boundary margins
needed for full tile records. Equation(6) and (22) give
discarded area at most

    [2delta+2theta A_D+o_j(1)] p_j².                  (24)

The actual boundary consists of partial B_j plus the finite
list of parallelogram sides. Their total length is O(p_j),
with a finite coefficient depending on the chosen windows
and the normalized B_j length bound. Equation(1) gives an
outside code of length at most

    c_D(2delta+2theta A_D)p_j²+o_j(p_j²).             (25)

The area coefficient c_D is the fixed local alphabet's
constant, independent of rho, mu or number of windows.
Large but FINITE window-perimeter/component constants
contribute only O(p_j+1). The finite B_j has one Jordan
boundary even if its limiting gamma has many contacts.

In each boundary window construct the chart family and
the target P_(j,alpha) of4.2. Its cut,J_alpha,c_alpha
are fixed for all members; the common CW translation
and target offset scale with p_j. The affine target
outer square and intermediate P therefore are fixed
physical sets for this j. All target full domains are
the SAME standard balanced Z_(p_j,...,p_j).

Condition on ALL these boundary-window LW codes,
including their absolute anchors, AND the original
outside record JOINTLY within A_j. At global balanced
scale one may take R=C_D p_j for all positions/heights.
Each separate log R term is O(log p_j); there are only
finitely many windows. Their actual per-window fringe/
perimeter terms from (16) likewise total o_j(p_j²).
The number of possible joint records is no greater
than the product of their individual bounds. Variable
code lengths can be padded to a fixed uniform bound
with an extra constant/length convention absorbed above.

Choose a largest JOINT class X_j and only THEN choose
ONE actual complete extended reference T_j in X_j.
This gives

    log |A_j|<=log |X_j|+outside_code_j
                          +sum_boundary kappa_(j,alpha). (26)

Independently maximizing the code class of each window
would not ensure such a common reference and is NOT used.
The common profile fiber was chosen first; no new limit
profile is selected after this conditioning.

## 7. Recover EVERY original tile and compare the exact local counts

For each strict window let N_(j,s) count distinct restrictions
of X_j to its intermediate strict count parallelogram.
Their restriction recovers the entire inner source window;
the actual full representatives and T_j satisfy (23)
on its whole buffer. Apply (9) to that SAME T_j and write

    C_(j,s)^src=C_s(T_j),
    L_(j,s)(M)=Z_D(M C_(j,s)^src),
    log N_(j,s)<=liminf_M M^-2 log L_(j,s)(M)+tau_(j,s). (27)

The core is fixed by this original reference. Its closed
region lies in int W_(j,s).

For a boundary window its fixed LW code specifies the
target good disks B_(j,b)^tar, their geometry and complete
lifted boundaries. They do not depend on which X_j member
is considered. Knowing their fillings and the code recovers
the target restriction including absolute heights. CW2,
with its whole-source-tile margin (10), then recovers
ALL original tiles meeting the source inner window.
This is recovery of physical source tilings, not just
independent target fragments or four corner heights.

Let Q_(j,b) be the associated standard (D-1)-direction
coarse disk with its fixed small exterior and complete
normalized boundary. SP gives

    Z_D(B_(j,b)^tar)=Z_(D-1)(Q_(j,b)),
    L_(j,b)(M):=Z_D(M B_(j,b)^tar)
                           =Z_(D-1)(M Q_(j,b))        (28)

for every integer M, with the one-reference port/rank
assignments. Any once-fixed translation/rank shift in
Q scales by M. No new inactive-curve deletion algorithm
is needed at M; its count is invariant under that
scaled translation. Put

    d_(j,b)=max(0,log Z_D(B_(j,b)^tar)
                       -liminf_M M^-2 log L_(j,b)(M)).

Equations(14)–(16) bound the SUM of these d_(j,b),
including the small-area split. No need to multiply
the single-block r0² error by an uncontrolled block
number remains.

Together with the fixed original outside record,
the strict intermediate restrictions and the target
good-disk fillings determine the whole B_j filling.
Boundary-crossing source tiles are present in the
outside margin and/or local records. If a tile meets
only an inner window, (10) guarantees that its entire
target image is represented. Consequently

    log |X_j|<=sum_s log N_(j,s)
                       +sum_b log Z_D(B_(j,b)^tar).   (29)

The upper product may include incompatible local
choices; that only enlarges this upper bound.
No compatibility assertion is needed for it.

## 8. ONE reference, disjoint fine pullbacks and EVERY integer dilation

We now justify the LOWER product, where compatibility matters.
Use exactly the same T_j fixed in section6. A boundary
target disk B_(j,b)^tar lies in the common target core,
strictly inside its target window. Its REFERENCE pullback

    C_(j,b)^src=(F_(T_j,alpha))^-1(B_(j,b)^tar)

is an actual fine Jordan tile disk inside int W_(j,alpha).
The code's complete target height determines its original
fine boundary through the exact inverse direction change
and signed rank/translation formulas.

For any new target filling of B_(j,b)^tar, complete it
by T_j's fixed FULL target exterior and apply the full
inverse OC map as in CW3. The target exterior has the
old normalization and heights, so its inverse is the
old fine exterior. The boundary pulls back to exactly
partial C_(j,b)^src. A full homeomorphism maps the
interior disk to the unique bounded Jordan region
with that boundary, hence to this SAME fine region.
The new interior inverse map need not agree pointwise
with the old one. Forward charting recovers the target
choice, so this is an injection with no boundary loss.

Within one window the reference target good blocks
have disjoint interiors and possibly shared fixed
vertices; their fine reference pullbacks have the
same incidence under a homeomorphism. Between different
windows all fine patches lie strictly inside disjoint
outer source windows. Strict cores C_(j,s)^src enjoy
the same containment. Thus all new fine fillings
glue to the SINGLE fine T_j exterior independently.
They remain inside B_j and leave its full boundary
and exterior fixed.

These LOWER insertions need not remain in X_j,
preserve its original outside-inner-window code,
or remain in the original profile ball. Some
reference cores extend into the conditioned collars.
The lower target is the unrestricted count Z_D(MB_j);
only their fixed patch boundaries and the actual
full exterior are required. Conditioning was used
for upper recovery and for selecting one compatible
reference, not imposed anew on the lower fillings.

At integer M subdivide every enlarged tile of T_j
into its M-by-M unit grid. Its canonical lift is
exactly a_(MT_j)(Mx)=M a_(T_j)(x), including affine
interpolation. The CW chart uses content Mp_j and
translation M b0, giving the EXACT identity

    F_(MT_j,alpha)(Mx)=M F_(T_j,alpha)(x).            (30)

Hence the reference inverse of M B_(j,b)^tar is
EXACTLY M C_(j,b)^src, with every subdivided rank
predetermined. SP's every-M equality in (28)
supplies the target fine fillings from the coarse
counts, and CW3 supplies their source insertions.
For strict windows, S_D already supplies fillings
of exactly M C_(j,s)^src with the same MT_j exterior.

All fine patches after scaling still have disjoint
interiors, and share only fixed compatible boundary
data where appropriate. We therefore obtain for
EVERY integer M>=1

    Z_D(MB_j)>= product_s L_(j,s)(M)
                            product_b L_(j,b)(M).     (31)

For strict small M use their reference grid if the
stronger canonical S_D estimate starts later; their
exact region counts are always defined. This does
not affect (27)'s liminf. Restriction to the fixed
fine patches, and the appropriate local forward
chart, recovers the tuple of choices.

Different windows may use different global chart
maps. Those maps never have to commute. Each is
used to construct a patch with exactly its reference
fine boundary, after which the actual fine patches
are what are glued in the original physical plane.
New interiors may be far from the old affine plane.
No independent reference is chosen for another
conditioned class or another window.

## 9. Fixed j, then M: finish the uniform induction

For each fixed j the entire list of strict cores
and boundary blocks is finite. It may grow with j,
but M tends to infinity with this j FIXED.
From (31) and the finite-sum liminf inequality,

    Lambda_D(B_j)>=sum_s liminf_M M^-2 log L_(j,s)(M)
                         +sum_b liminf_M M^-2 log L_(j,b)(M).
                                                               (32)

All counts are >=1 and have finite normalized upper
bounds. No opposite liminf inequality or uniform
M threshold across infinitely many j is invoked.
Each local induction/strict theorem may use a
large-M threshold depending on the actual fixed
reference and j.

Combine (7),(26),(27),(29),(32) and the definitions
of d_(j,b). The positive part causes no problem,
because all paid errors are nonnegative:

    Delta_D(B_j)
      <=o_j(p_j²)+outside_code_j
          +sum_boundary[kappa_(j,alpha)
                             +sum_(b in alpha)d_(j,b)]
          +sum_strict tau_(j,s).                     (33)

Choose the numerical fractions in4.1/4.4 so all
local sums in (33) are bounded by
zeta sum_alpha area(W_(j,alpha))+o_j(p_j²).
This is possible by their arbitrary per-area
budgets, with the positive unit-area lower bound
mu and bounded source/target area ratios fixed
BEFORE scales. There is no factor equal to the
window count: disjointness gives

    sum_alpha area(W_(j,alpha))<=A_D p_j².

All separate O(ell_(j,alpha)+1) fringes/perimeters
and O(log p_j) anchors are o_j(p_j²) for this
FIXED finite normalized list. Thus (25),(33)
give the explicit normalized inequality

    Delta_D(B_j)/p_j²
       <=c_D(2delta+2theta A_D)+zeta A_D+o_j(1).       (34)

By (17),(18) the fixed part is <a/(4C²).
Let j grow after every preceding choice; the
right side is eventually <a/C², contradicting
(5). This proves UR_D from UR_(D-1) and the
exact local strict premise S_D.

The induction starts at elementary UR2, so it
proves (G1) for EACH fixed finite D conditional
on the stated S_d for3<=d<=D. There is no use
of CKP, a lozenge entropy formula or UR3.
In particular all lower-dimensional inputs
are produced on the required GE class by the
induction itself, not guessed from a balanced
hexagon or a periodic family.

## 10. Full balanced limits at ALL integer sizes

For a fixed D the full balanced content-r zonogon
is a member of GE_(D,C_D')(r) for one fixed C_D':
its actual boundary is Jordan, its perimeter is
2r sum_i||v_i||, each color has r curves, and
the empty exterior is a legitimate fixed exterior.
Let eta(r)=eta_(D,C_D')(r). By UR_D,

    liminf_M log B_D(Mr)/(Mr)²
       >=log B_D(r)/r²-eta(r), eta(r)->0.             (35)

Here M ranges over ALL positive integers, with
r FIXED. RP1 pads the fixed-origin Z_(Mr,...,Mr)
injectively into Z_(p,...,p) for
Mr<=p<(M+1)r. The old core and its ranks are
recovered by restriction. Since Mr/p->1 uniformly
over that bounded remainder, (35) implies

    liminf_p p^-2 log B_D(p)
       >=log B_D(r)/r²-eta(r)                        (36)

for EVERY fixed positive integer r. This is the
precise RP3 quantifier: a liminf controls all
sufficiently large multiples, not merely a
favorable subsequence. One finite reference
alone would not provide (35).

The finite alphabet gives a finite limsup in
p. Take r along an integer limsup sequence in
(36) and then let those r grow. The full liminf
is at least the full limsup, establishing k_D
in (G2). Dividing by D² defines the finite ell_D.
No exact inequality B_D(Mr)>=B_D(r)^(M²)
or numerical entropy formula was required.

## 11. Conditional official scalar limit through the accepted DC bounds

The accepted marked dictionary identifies the
official fixed-polygon orientation-distinguished
C(n) with full n-strand reversal commutation
classes. It includes no rotation/reflection
quotient, insertion histories or extra n! factor.
For a fixed D>=3 and large n, partition its
initial labels into consecutive nonempty groups
of sizes m_i in{p,p+1}, p=floor(n/D).
The accepted finite comparison DC1 is

    B(m_1,...,m_D)<=C(n)
       <=B(m_1,...,m_D) binom(n²-1,2S) 2^(2S),
    S=sum_i binom(m_i,2).                            (37)

Its code recovers erased same-color crossings
from canonical gaps/ordered neighboring-rank
ports; no uncontrolled matching or sweep factor
is being added here. DC2 gives

    0<=[log C(n)-log B(m_1,...,m_D)]/n²
       <=h2(1/D)+1/D+o_n(1)                         (38)

at this FIXED D. The error then tends to zero
as D is subsequently increased.

Full B is coordinatewise nondecreasing, either
by the accepted DC strand-addition/deletion
injection or by section1's actual boundary
belts. Hence

    B_D(p)<=B(m_1,...,m_D)<=B_D(p+1).

The limits (G2) are for exactly these FULL
marked balanced counts, so both extreme
logarithms divided by n² tend to ell_D:
their normalization ratios (Dp/n)² and
(D(p+1)/n)² tend to one. Therefore (37),(38)
imply for the official L_minus,L_plus

    ell_D<=L_minus<=L_plus<=ell_D+e_D,
    e_D=h2(1/D)+1/D.                                (39)

Finiteness is already implied at a single
fixed D, say3: ell_3 is finite and DC's
comparison bounds the official limsup.
No separate numerical upper bound is needed.

For every D>=3, (39) gives
0<=L_plus-L_minus<=e_D. Now let D->infinity
AFTER the fixed-D/n limits. Since e_D->0,
L_minus=L_plus=L. Equation(39) also gives
0<=L-ell_D<=e_D, so ell_D->L.
No rate in UR_D uniform in D, exchange of
D with p, or global D-dependent entropy
formula is used. This proves the candidate
existence/equality statement (G3), conditional
on the exact local premises and the present
new global proof passing its own audits.

The common numerical value remains undetermined.
The official request to determine both rates
therefore is not claimed fully solved by
this scalar-existence partial result.

## 12. Preserved limits of the construction

All new assertions remain candidate-unverified.
The global proof is exposed for every symbolic
fixed D, not inherited from the G4 special-case
conclusion or from an induction outline.
The all-D strict local premise has only its
exact separate LOCAL acceptance status. The source
packet distinguishes every accepted interface
from new arguments and from research precedent.

No simultaneous nonsingleton-group coarsening,
unrestricted lifting through a forbidden event,
convexity of K_D, realizability of all necessary
profiles, slope entropy continuity, smooth
limiting boundary, free buffer, independent
local reference maximization, chart commutation,
affine replacement interior or all-scale
reference existence is assumed.

All actual component/perimeter costs and
absolute anchors are paid. Every lower product
uses one reference and every integer dilation.
The only induction lower input is the exact
GE_(D-1) theorem just established at that
dimension. The elementary base avoids any
published dimer theorem. Existing failed
versions, counterexamples, local candidates
and all prior review bytes remain unchanged.
Two OTHER initially blind whole adversarial
audits must inspect this complete new packet
before any coordinator promotion.
