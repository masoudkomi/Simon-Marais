# Actual plane patches, finite upper certificates, and a boundary-entropy gap

2026-10-18 UTC, FULL version1.1. **Candidate proof - unverified.** Constructor C,
`/root/review_2017_coarsening_r1`; inherited requested gpt-6.1-sol/max,
independent effective-setting readback unavailable. TWO OTHER initially
blind WHOLE nonconstructor audits and coordinator reconciliation are
required. No mathematical executable, scan, CAS, certificate replay or
proposed-algorithm execution was used.

This full version repairs PMR2-01 after BOTH original whole initials
froze. The countably distinct ambient perturbation in version1 did not
retain de Tiliere's standing finite-angle hypothesis. Here ONLY the
finite track set meeting the marked patch is perturbed; the ambient
angle set stays finite. The precise finite same-track completion input,
its operative boundary/corner data, the DC limit and PM3 dependence are
made explicit. EVERY original v1 byte and both initial audits are
preserved. BOTH affected reaudits are required; this is not promotion.

The numerical2017 scalar remains unknown. This packet supplies an actual
finite local model and an actual bounded-content patch-extension bridge,
then proves that the resulting free-window upper certificates do NOT
converge to the balanced entropy already in three directions. The last
claim is an exact model comparison, including asymptotically matched tile
composition, rather than another abstract noncomputability example.
No effective upper hypothesis R or full annual answer is established.

## 0. Scope, accepted inputs and four proposed claims

Fix D>=2 and v_i=(1,i-1), V=[v_1 ... v_D]. Put

    P_ij=[0,v_i]+[0,v_j], i<j,
    b_D=binom(D,2), A_D=area Z_1=sum_(i<j)(j-i)
                                      =D(D^2-1)/6.

The accepted marked dictionary identifies full tilings of
Z_p=sum_i[0,p v_i] with B_D(p) commutation classes. The accepted all-D
global result gives k_D=lim_p p^-2 log2 B_D(p), ell_D=k_D/D^2 and the
official common scalar L. EC1--EC4 give effective LOWER certificates
only. GR1--GR4 concern the exact full-boundary profile class and one
tiling per approximation; they supply no exponential mass theorem.

An **integer plane tiling** is an edge-to-edge tiling of R^2 by translates
z+P_ij, z in Z^2, with these fixed colored vectors. There is no matching
rule, rotation quotient, permutation of colors, fractional origin or
unrecorded lift parameter. Some colors may be absent. Write X_D for
these plane tilings encoded below.

**PM1, exact local model and actual finite upper certificates.** X_D
has an explicit finite-alphabet finite-range encoding on Z^2, with exact
decoding. Its train tracks are proper embedded lines, same-color tracks
are disjoint and two tracks of different colors meet at most once.
Let N_D(m) be the finite count of locally admissible m-by-m origin-bit
blocks for the specified rules. It is computable in principle, and

    k_D<=A_D m^-2 log2 N_D(m)                 for EVERY m>=1.       (1)

The right-hand finite-block sequence has a limit A_D h_D^loc, where

    h_D^loc=inf_(m>=1) m^-2 log2 N_D(m).

Thus running minima of rational logarithm upper approximants are genuine
computable upper certificates. No equality h_D^loc=k_D/A_D is asserted.

**PM2, bounded-content completion of an ACTUAL plane patch.** Let P
be a positive-area finite Jordan tile disk in an integer plane tiling,
with e boundary edges and its complete colored/lifted boundary fixed.
Then P, up to one integer physical translation, is a subpatch of an
actual full standard zonogon tiling with contents

    0<=N_i<=e/2 for every i,  sum_i N_i<=e/2.                    (2)

ONE such exterior works for EVERY filling with P's same complete
boundary. In particular perimeters O(L) give an actual GE exterior
with all contents O(L); this does not assert that P or the zonogon
packs at density one. Zero ambient colors are allowed.

**PM3, a strict-slope plane-to-full finite counting interface.** In the
fixed compact-strict US_D2 domain, replace its family of restrictions
having full-zonogon representatives by restrictions having actual
integer-plane representatives, with the SAME whole-buffer affine
estimate and common offset. Then its upper bound still holds:

    log2 |F|<=log2 C_(m_+)+K'(tL^2+L+1),                       (3)

with the same canonical receiving family and m_+, and a fixed enlarged
constant K'. Constants retain the accepted order of quantifiers:
tolerance before the finite rational net/periods, and periods enter the
original scale threshold. This is a new interface to that accepted
theorem, not a reproof of its annular construction or a lower estimate
for unconditioned free-window entropy. It does not retain a preassigned
plane reference or assert any new lower dilation-count theorem.

**PM4, an actual strict failure of the free-window upper limit.** At D=3,

    k_3 ln2=(9/2)ln3-6ln2,
    4 h_3^loc ln2 >=3 M >=(1/2)ln6 > k_3 ln2,                 (4)

where M is the logarithmic Mahler measure of 1+z+w. The plane tilings
used for the lower bound have limiting densities 1/4 of EACH tile type
per unit physical area, exactly the balanced zonogon's densities.
The finite torus sectors in the proof approach these densities; exact
equality of their three counts at every finite torus size is NOT claimed.
Consequently adding only these limiting global composition constraints
does not repair the free-window entropy substitution.

The original integer-grid coding LEAD was suggested earlier by root.
It is a contribution if this packet is used, so root is conservatively
excluded from its two independent whole-audit count. C authored older
annulus/rank/OP/GR material and reviewed other accepted inputs. Those
roles are disclosed, not independent self-recertification here. Published
rhombic-extension, dimer-pressure and boxed-partition theorems below are
attributed; none is claimed new. Only the new interfaces and deductions
are submitted for review.

## 1. Exact finite local rules, including physical degeneracies

At each z in Z^2 use a b_D-bit symbol. Its ij bit says whether the tile
z+P_ij is present. Several bits at one origin may be one: different
positive-angle sectors can meet only at that origin. A single categorical
tile label would therefore be an incorrect alphabet.

Impose the following two families of finite-range constraints.

1. No two distinct active candidate tiles have intersecting interiors.
2. For every unit cell Q_z=z+[0,1]^2, the sum of the areas of its
   intersections with all active candidate tiles equals one.

These are genuinely finite rational rules. Every tile has horizontal
width2 and vertical span at most2D. Only origins within a fixed
radius, for example 4D+10 in the infinity norm, can occur in either
test. Each intersection polygon has rational vertices, so its area
and the decision whether two interiors overlap are rational finite
computations. This describes a terminating rule compiler, not a run
of an enumeration or geometry program.

For a global bit field obeying the rules, the active tiles are locally
finite. Rule2 and rule1 give coverage almost everywhere. Their union is
closed locally, so an omitted point would have an omitted open
neighborhood of positive area, impossible. They thus cover the plane.

There is no hidden T-junction. Every tile edge is an integer translate
of a unit segment v_i=(1,i-1), whose open horizontal interval contains
no integer abscissa. An integer tile vertex cannot lie strictly inside
another edge. Partially overlapping collinear edges also cannot occur:
their endpoints have integer abscissae and their x-lengths are one.
A transverse crossing of edge interiors would force overlapping tile
interiors in one of its adjacent sectors. Hence intersections are whole
edges or vertices, giving exactly an edge-to-edge tiling. Conversely
every integer plane tiling supplies the two rules. Its unique origin
for an ij tile is the vertex of minimum x-coordinate, so encoding and
decoding are inverse, with no tile-permutation multiplicity.

The colored edge cochain assigns +e_i to a positive v_i edge. It sums
to zero round every tile. The cell complex is the whole simply connected
plane, so integration gives an integer lift a on vertices, unique after
one anchor. Its affine interpolation on each tile has Va(x)=x after
calibrating that anchor. Active row covectors are the inverse of the
two edge vectors; their norms are bounded by a constant depending only
on D. Thus every coordinate is globally Lipschitz. No global rank box
or full-boundary condition is asserted for this plane lift.

## 2. Reduced train tracks are a consequence, not an extra local rule

Join midpoints of the two color-i edges in each tile containing i.
At an i edge there are exactly two neighboring tiles, on opposite sides
of its supporting line. The pieces therefore continue uniquely.

Let q_i(x)=det(v_i,x). Across an ij tile the two midpoints differ by
v_j, and the difference of q_i is j-i. Orient each resulting track by
increasing q_i. This orientation agrees through shared edges, and its
q_i increment per complete tile is |j-i|>=1. Thus a track cannot close
or self-intersect, and in both directions q_i tends to the corresponding
infinity. It is a proper embedded line. Different i tracks are disjoint.

For i<j, at every ij crossing the two q-oriented tangent directions are
v_j and -v_i. Their determinant is j-i>0. All crossings of the same
two tracks therefore have the same oriented sign. A proper Jordan line
separates R^2 into two sides. Crossings of another proper oriented line
with it, when read in order, alternate side-change direction and hence
alternate sign. Two or more crossings with only the same sign are
impossible. This proves the required at-most-once property, including
parallel noncrossing tracks. There are no triple crossings because a
tile has only two colors and midpoint tracks avoid tile vertices.

This is the same elementary necessity principle used in the original
Kenyon--Schlenker theorem, here checked for the actual nonunit integer
parallelograms. It avoids assuming an unrelated arbitrary-pseudogrid
straightening or a finite-type condition on reduced words.

## 3. Finite local counts and their rigorous upper direction

Define N_D(m) to count all b_D-bit fields on the sites
{0,...,m-1}^2 satisfying every translated rule whose ENTIRE site scope
is contained in that square. Rules reaching outside are not tested.
These counts are positive: the plane grid using just v_1,v_2 gives
an admissible restriction. They are finite and computable by checking
a finite list of bit fields against the rational rules. No such count
has been evaluated in this packet.

A locally admissible n-square restricts to a locally admissible
m-square. Partitioning into floor(n/m)^2 disjoint m-squares leaves
at most2mn sites, with at most b_D bits per site. Consequently

    log2 N_D(n)<=floor(n/m)^2 log2 N_D(m)+2 b_D mn.            (5)

Taking n to infinity at fixed m proves limsup q_n<=q_m, where
q_m=m^-2 log2 N_D(m). Since every q_n is at least inf_m q_m,
q_n converges to that infimum. This proof does not presuppose mixing,
extendability of every locally admissible block, or strong irreducibility.
We use the notation h_D^loc for this exact local-rule limit; no separate
general entropy variational theorem is needed below.

Now encode a tiling of the actual Z_p by its origin bits. Fix m FIRST.
Use an m-square lattice partition of the plane. Boxes at a fixed tile
distance from boundary Z_p have restrictions counted by N_D(m).
The remaining sites meeting Z_p lie in a boundary tube of width O_D(m),
and their number is O_D(pm+m^2). This follows by arclength sampling of
the fixed convex polygon boundary and the finite tile diameter, not a
perimeter-only assertion for arbitrary multiply connected windows.
The number of bulk boxes is at most A_D p^2/m^2+O_D(p/m+1).
Their bit fields, together with the boundary-site bits, determine the
tiling. Thus

    log2 B_D(p)
      <=[A_D p^2/m^2+O_D(p/m+1)]log2 N_D(m)
                                      +O_D(pm+m^2).          (6)

Divide by p^2 and let p tend to infinity at this ONE fixed m. This
proves(1). Taking running minima of exact finite logarithm upper
approximants gives computable rational upper certificates tending to
A_D h_D^loc. Their limit is NOT identified with k_D.

For context the accepted HC direction inequality gives, at each fixed
D>1 and each m, the further genuine finite certificate

    L <= D/(D-1) [ A_D q_m/D^2 + (1/2)h_2(1/D) ].            (7)

Logarithms and binary entropy of the displayed rational arguments have
arbitrarily accurate effective rational upper approximants. Formula(7)
is a correct upper bound family; no claim that its infimum evaluates L
or improves the already accepted numerical bound is made.

## 4. Primary extension input and its precise geometry

The published inputs used ONLY here are:

* Kenyon--Schlenker, arXiv math-ph/0305057v1, Theorem3.1 and
  Theorem4.1/Lemma4.5: the train-track criterion for rhombic embedding,
  and prescribed positive wedge/track-angle embeddings of the infinite
  quad graph. Its image may be a plane, half-plane or strip.
* de Tilière, arXiv math/0403324v3, Lemmas4.2--4.3: an actual finite
  simply connected patch in a plane rhombus tiling can first be made
  train-track-convex and then completed to a convex opposite-edge
  polygon. The operative construction keeps the same track set.

The second source has a STANDING finite-rhombus-angle hypothesis in
its front matter. It is retained literally below, including after the
perturbation. Version1 failed to state/check that condition; positive
minimum areas do not imply a finite angle set. The first review checked
the finite operative proof, while the second required an explicit author
interface repair. This version supplies one instead of silently importing
the reviewer's explanation or an infinite-angle extension.

These statements and operative proofs were actually read. Parallel
ambient tracks are allowed. Only the finitely many tracks meeting the
patch need distinct unoriented directions in the second finite
construction. That exact finite corollary is exposed in section4.2.
No dimer measure, periodic density or entropy conclusion is imported
from these geometric results.

### 4.1 Passage to an actual rhombus tiling of the WHOLE plane

Let G be the graph of an integer plane tiling. Section2 verifies the
train-track criterion. Give each edge color i the unit vector
u_i=v_i/||v_i||, preserving its direction. The tile angles and their
cyclic order round each vertex are unchanged; adjacent tile wedges sum
to pi and the vertex sum is2pi. The cited embedding theorems therefore
give an actual rhombic embedding in the same planar isotopy class with
these prescribed angles/transversals.

Its image is the WHOLE plane. Indeed its tile areas have one fixed
positive lower bound because there are only finitely many nonparallel
u_i. Infinitely many unit rhombi approaching a finite boundary point
would all lie in a bounded larger ball, contradicting disjoint interiors
and this area bound. A finite collection cannot create a boundary point
because every vertex/edge has a full planar neighborhood. This excludes
the half-plane and strip alternatives in the cited theorem.

This deformation preserves the abstract patch P and its boundary,
not its intermediate physical coordinates. Those coordinates will be
restored exactly after completion.

### 4.2 Track preservation, finite perturbation and finite completion

In the rhombic plane let T be the finite set of global tracks meeting
P. Every one crosses P's boundary at least twice, and each boundary
edge belongs to just one track. Hence |T|<=e/2. Lemma4.2 gives a
train-track-convex disk P' containing P and meeting exactly T.

For clarity, the first published construction follows a boundary track
through each finite excursion outside the current patch and fills the
bounded region between that excursion and the old boundary. It keeps a
disk. Any track through a newly filled region must also meet the old
bounding arc, since crossing the excursion track twice is forbidden.
Thus no track outside T is introduced. The same once-only fact prevents
undoing convexity already achieved for an earlier track. There are
finitely many original boundary tracks and finite excursions, so the
result P' is finite, meets exactly T and has precisely two ports for
each member of T. This is Lemma4.2 in its actual original finite-angle
plane domain; no added arbitrary decorated disk is substituted.

Now assign distinct fixed numbers c_t in(0,1) to ONLY the tracks t in T.
For a track of original color i in T set its positive transversal angle
to theta_i+epsilon c_t; leave EVERY track outside T at theta_i. Opposite
orientations receive angle+pi. Choose epsilon smaller than a fixed
fraction of the positive gaps between the original color directions
and of their common open-half-plane margin. Then:

* every existing crossing of different original colors remains strictly
  order-preserving in the Kenyon--Schlenker convention;
* same-color tracks do not cross, so neither their perturbed comparisons
  nor their comparisons with unperturbed same-color tracks impose an
  existing-crossing inequality;
* the directions on T are distinct, nonparallel, and stay in one open
  half-plane; their within-color order is fixed by c_t;
* the ENTIRE perturbed plane uses at most D+|T| transversal directions,
  and therefore finitely many rhombus angles.

Kenyon--Schlenker Lemma4.5 gives the perturbed embedding in the same
planar isotopy class. All its existing tiles still use different
original colors, so their angles have the same uniform positive margin
after the small perturbation. Section4.1's area argument again gives the
WHOLE plane. P' is the same embedded marked finite disk and its track
convexity/ports are unchanged. Thus the second source's standing domain
now holds LITERALLY; an assertion for arbitrary infinite-angle planes
is unnecessary.

**FC, the exact finite same-track corollary used.** In an actual rhombus
plane with finitely many angle types, let H be a finite Jordan tile disk,
train-track-convex, meeting n tracks whose n unoriented transversal
directions are distinct. Then H can be enlarged to a convex centrally
symmetric 2n-gon tiled by rhombi on those SAME n distinguished directions,
retaining H as a marked subpatch. Every pair of distinguished tracks
crosses exactly once in the output. No new track or port pair is added;
at most binom(n,2)-f new faces are needed, where f is the old face count.

This is the finite conclusion of de Tiliere Lemma4.3 in the literal
standing domain just restored. The geometric legality of its embedded
corner additions is an ATTRIBUTED published input in that domain,
rather than a claim that any locally positive abstract disk embeds.
Here is the operative finite argument, including the data that are
needed for the marked/content claim.

Orient the 2n boundary ports counterclockwise and pair each with the
other port of the same track. Their vectors are opposites. Let W(e,f)
be the UNWRAPPED turn along the counterclockwise boundary interval.
The finite construction uses these facts:

    total boundary turn=2pi; W(e,e*)=pi;
    W(e,f)>-pi for any two boundary ports;                 (FC1)
    convexity iff every pair of the n tracks crosses.       (FC2)

The port identity W(e,e*)=pi is computed on one boundary side of that
track's finite strip, with path comparison on the bounded subdisk. It
does not identify an unwrapped turn with a principal angle modulo2pi.
For FC2, a noncrossing pair has nonalternating ports. The two intervals
between their corresponding ports have opposite turns, by the paired
pi identities and the total2pi identity. Distinct directions make one
negative. If the pair crosses, its crossing rhombus and the two strip
boundary paths cut off a bounded subdisk; the same turn identities make
the corresponding port-to-port turn positive. Hence all pairs crossing
is equivalent to all corner turns being positive.

The lower bound in FC1 is the finite corner induction in the operative
proof. Order the strips adjacent to the boundary. Their oriented
transversal directions turn through2pi, so some consecutive pair has
a positive turn and their crossing is an outer boundary rhombus.
Removing that rhombus leaves a smaller train-track-convex disk (a strip
which disappears is simply omitted in this induction). Starting with
one rhombus and reinserting these boundary rhombi proves the lower
bound using the simple strip/subdisk path comparisons. This induction
uses only the finite ports, strips and their crossing rhombi, not a
bound on directions of unrelated outside faces. We retain the source's
embedded-corner conclusion, with all its ambient hypotheses met, rather
than claiming these angle inequalities alone prove global injectivity.

If a pair is missing, FC2 gives a negative adjacent boundary turn.
The source's corner operation attaches the rhombus of those two
directions across that concave corner. The adjacent turn inequalities
in FC1 keep the neighboring boundary fans admissible; its finite
induction proves that this is an embedded addition and preserves FC1.
The two old tracks are extended through this face. Their remaining
ports are unchanged, their two corner ports exchange boundary order,
and all other tracks/ports remain fixed. They did not previously cross
(a crossed pair has positive turn), so exactly ONE new pair crossing
is created. The old ambient pieces OUTSIDE the finite patch are not
retained: a pair which met out there is still an uncrossed pair of the
finite arcs until this operation. No double crossing is added inside
the completed finite diagram. The disk and its marked old rhombi survive. Repeating
increases the crossing count by1 and can occur at most binom(n,2)-f
times. It ends with all pairs crossed and a convex polygon. The paired
pi identities give its opposite boundary edges as equal and parallel;
one unit port of each sign occurs for every distinguished track.
Sorting their directions therefore identifies precisely the full
zonogon with those n unit generators, up to translation. This is a
finite completion statement; no periodic plane, measure, or entropy
claim is imported.

Apply FC to the perturbed P'. All existing and added directions are
the n=|T| directions already assigned to T. At this fixed n there are
only finitely many full classes and marked occurrences of P'. Along
epsilon down to zero choose a subsequence with those data fixed.
Within each original color the c_t order is fixed, so its distinguished
directions form one consecutive block. No choice of epsilon or
subsequence changes n or the content bound.

Apply the accepted DC smoothing to this fixed full class, erasing all
within-color crossings. It gives an ACTUAL block-reversal tiling with
contents N_i=#{tracks of T of color i}. To use the accepted DC statement,
first OMIT the groups with N_i=0; its partition has nonempty blocks.
After projection reinsert the absent color coordinates as constants.
Positive area of P guarantees at least two active original directions.
This yields the desired possibly-zero-content D-direction zonogon.
Its physical realization at
the vectors u_i is the limit of the noncollapsed tiles. Every old P'
tile uses two different colors, so none is erased. Its coordinates,
integrated from its fixed marked anchor, tend to exactly its original
rhombic coordinates. Hence P' and P survive as actual subpatches.
This uses the accepted actual DC projection, not an unsupported rule
that an arbitrary collection of zero-area faces can be removed.
Explicitly, the group map sends each distinguished e_t to its color
e_i. At retained tiles this is their canonical cochain after smoothing;
an erased tile becomes a collinear two-edge lens. Thus the positive
tile coordinates agree with the group-summed limiting coordinates.

Finally apply the accepted full-zonogon deformation dictionary from
u_i back to v_i. It gives a genuine full standard zonogon tiling.
On the connected marked P all edge increments are the original +/−v_i,
so all its physical coordinates are restored up to ONE translation.
An anchored vertex is integer in the ORIGINAL v_i realization and in
the FINAL v_i realization, making this translation integer; the
intermediate unit rhombic coordinates need not be integer. The original
plane lift and the final canonical full lift may differ by ONE integer
rank vector. They are aligned at that single marked vertex, not by
independent choices on different sides. The contents satisfy(2),
including absent colors.
This proves PM2's existence assertion without a density-one packing.
In particular finite perturbation avoids the old infinite-angle grid
certificate rather than denying it. The proof imports no extension of
de Tiliere's global standing model to countably many angle types.

### 4.3 One exterior and actual complete-boundary fibers

Fix one of these completed tilings. Delete the interior tiles of P
and keep its entire exterior. Any other filling with P's SAME physical,
colored, lifted boundary glues along those exact full edges and vertices.
Its support is the same Jordan disk; the exterior has disjoint interior.
Thus the union is another genuine full zonogon tiling. Restriction to P
recovers the filling, giving injectivity. The exterior is selected ONCE
before the filling varies. The lift agrees by the boundary cochain and
one anchor; no independently chosen rank offsets or matching are used.

This proves the actual GE property with contents bounded by perimeter.
It is specific to an ACTUAL plane patch. Necessary prefix tests for a
formal decoration do not supply its plane representative, so the older
OP/OB1 arbitrary-decoration counterexamples are not contradicted.

## 5. Full-boundary conditioning for a strict plane family

We now prove PM3, retaining all US_D2 hypotheses other than its old
full-representative requirement. Thus D>=3 is fixed, J' is in the
accepted compact strict rational family, L>=C(q+1)/t and all plane
representatives obey the SAME affine estimate on the WHOLE required
buffer of P_L. Here t=sqrt(epsilon). Choose one representative per
distinct restriction; no choice changes the count of restrictions.

Take a larger fixed parallelogram W containing that buffered region
and an additional fixed tile-width margin. Its perimeter is O(L).
Choose its placement generically to avoid lattice vertices and edge
coincidences, simultaneously for every integer-origin candidate tile.
Record every tile meeting a fixed-width tube of boundary W. There
are O_D(L+1) possible origin/type bits in that tube. Their number
depends on the fixed frame, not on a global ambient strand number.

For any representative let Q be the union of tiles whose interiors
meet W's interior, and fill all bounded complementary components.
The resulting P is a finite Jordan tile disk with boundary in a
fixed-width tube of boundary W and with O_D(L+1) boundary edges.
Here are the needed topology details. The interior of Q is connected:
generic paths in the convex W connect its intersecting tiles through
whole shared edges. All holes are outside W but inside its fixed-width
enlargement, so filling them uses only that tube. The filled set has
connected interior and connected unbounded open complement. A vertex
pinch with separated interior sectors would, by a path joining those
sectors in the interior and the Jordan curve theorem, trap a bounded
open complementary component. Thus no pinch remains; its boundary
is one Jordan polygon. Each boundary tile lies in the bounded-width
tube, and tile areas are >=1, proving the edge bound.

The recorded trace determines this P and its complete colored boundary;
all its nontrivial choices are in that same tube. Condition also on
one boundary vertex's integer lift. Even if the common offset is large,
the affine estimate at an interior point and the global finite-type
Lipschitz bound place that anchor in a fixed known box of side O(L).
Its number of possible values is polynomial in L. Thus a largest
joint class loses at most O_D(L+1+log(L+2)) bits and has ONE complete
P boundary. The count uses relative anchor indices in that known box,
not an unbounded independent absolute-coordinate code per tile.

Apply PM2 to one class member. Its ONE full exterior works for every
member, so all original restrictions now have actual full-zonogon
representatives agreeing outside P. Their given affine estimates are
unchanged on the required buffer, which is contained in P. If the
completed zonogon starts at x_out, its canonical lift differs from the
given source lift by one common integer vector b with Vb=x_out.
Translate physical coordinates by x_out and heights by b. The new
offset is J'x_out+c-b, whose V-image is zero. It is the SAME for the
whole conditioned family.

Here PM2 means the repaired finite-angle/FC construction in section4.2.
It chooses the finite perturbation and one completed exterior ONLY for
that single class member. The complete-boundary fiber argument then
extends every other filling. Its content bound, not any small-angle
constant from an intermediate embedding, is what is used by this
conditioning step. Thus no epsilon depending on that member or on
|T| introduces a new q-dependent estimate or a per-filling phase choice.

US_D2 therefore applies with every rank, phase, available-box and
whole-buffer hypothesis intact. Add the boundary-class loss to its
upper code. Since L+log(L+2) is absorbed by a fixed multiple of L+1,
this proves(3). In particular a genuine strict plane family has the
accepted receiving-boundary upper comparison. Arbitrary locally valid
finite bit blocks are not thereby asserted to extend to the plane.

## 6. A three-direction failure with matching limiting composition

This section uses NATURAL logarithms until the final conversion. It
does not extrapolate a three-direction theorem to D>=4.

### 6.1 The fixed balanced value

MacMahon's boxed-plane-partition formula, via its standard marked
three-direction tiling bijection, gives

    B_3(p)=product_(1<=i,j<=p) (i+j+p-1)/(i+j-1).

The formula and exact box/tiling domain were verified in the
author-posted Björner--Stanley exposition cited in the source record;
the theorem is attributed to MacMahon, not a new enumeration here.
No finite table is computed.

Dividing its logarithm by p^2 gives the Riemann integral

    K=integral_[0,1]^2 ln[(x+y+1)/(x+y)] dx dy
     =(9/2)ln3-6ln2.                                      (8)

The logarithmic corner is integrable. For i+j<=delta p, grouping the
sum by i+j bounds its contribution by a constant times
delta^2(1+|ln delta|), uniformly as p grows; elsewhere ordinary Riemann
convergence applies. One can evaluate(8) with the twice-antiderivative
F(s)=(s^2/2)ln s-3s^2/4, F(0)=0. Thus K=k_3 ln2.

### 6.2 Actual torus matchings and a source-hypothesis check

Use the honeycomb dimer graph with one black and one white vertex per
fundamental cell, positive orientation weights a,b,c, and its N-by-N
torus quotient. It has N^2 dimers per matching. Its characteristic
polynomial is a+bz+cw, up to harmless unit monomials/sign changes.
The actual primary import is Kenyon--Okounkov--Sheffield,
math-ph/0311005v1, Theorem3.5: the logarithmic partition function per
cell is the torus logarithmic Mahler integral when the polynomial has
only finitely many zeros on the unit torus. Near a=b=c=1 the strict
triangle inequalities give exactly two simple zeros, so this hypothesis
holds. No theorem about D>=4, fixed zonogon boundaries, or exact finite
balanced homology sectors is imported.

Write f(log a,log b,log c) for this pressure. Jensen's one-variable
integral gives

    f(log a,log b,log c)
        =(1/(2pi)) integral_0^(2pi)
                   ln max(c,|a+b exp(it)|) dt.              (9)

Near unit weights the two threshold angles solve a smooth equation
with nonzero angular derivative. The two integrands agree at the
moving threshold, so differentiation under the two smooth pieces
shows f is C1 there. It is symmetric in a,b,c by a unimodular torus
change of variables and homogeneous of degree one before logarithms:
f(x+t,y+t,z+t)=t+f(x,y,z). Hence each log-weight derivative at zero
is1/3.

This gives a direct elementary concentration argument. For any
delta>0 choose s>0 small enough that
f(s,0,0)-f(0,0,0)<s(1/3+delta/2). Exponential weighting bounds the
number of unweighted torus matchings having first orientation count
>=(1/3+delta)N^2 by
exp(N^2[f(0)-s delta/2+o(1)]). A negative tilt treats the lower tail;
do this for all three orientations. Their complement still has
exp(N^2[f(0)+o(1)]) matchings. There are only polynomially many
orientation-count triples. Choosing one largest triple, then taking
delta down to zero along a subsequence, gives ACTUAL sectors with

    r_12+r_13+r_23=N^2,
    r_ij/N^2 ->1/3,
    N^-2 ln(number in that sector)->M=f(0,0,0).             (10)

This proves approximate balanced sectors from the full pressure theorem;
it does not silently assume every N has an exact one-third sector.

### 6.3 Exact integer-period deformation and physical area

Realize the ordinary lozenge tilings at the three vectors
w_1=(1,0), w_2=(1,1), w_3=(0,1). All pair areas are one. Their
period torus is [0,N]^2 and its lift a has periods

    A=(N-alpha,alpha,-alpha),
    B=(-beta,beta,N-beta),                               (11)

because W A=(N,0), W B=(0,N). On tiles12,13,23, the gradient
of a_2 is respectively(0,1),(0,0),(1,0). Integrating the two
derivatives on the torus gives EXACTLY

    N alpha=r_23, N beta=r_12.

In particular alpha,beta are integers, nonnegative, with
alpha+beta<=N. A fixed orientation-count sector has the same lift
periods for every one of its tilings.

Replace the w_i by our v_1=(1,0),v_2=(1,1),v_3=(1,2). The new
integer physical periods are

    P=(N-alpha,-alpha), Q=(N-beta,2N-beta),
    det(P,Q)=2N^2-N(alpha+beta)=N^2+r_13.                  (12)

This replacement is a genuine torus embedding. The edge cochain
integrates on the universal cover; the two periods make its map descend
to the new torus. Tile determinants remain positive, and the cyclic
order of the positive and negative edge directions is preserved, so
the map is a local homeomorphism on tiles, edges AND full vertex fans.
It induces the basis P,Q on the target period lattice, hence has
topological degree one. A local homeomorphism of compact tori of
degree one is a homeomorphism. Lifting gives an actual plane tiling
in X_3, with all vertices integer. Replacing v_i back by w_i recovers
the original colored tiling with its anchored origin, so no exponential
identification of distinct matchings occurs. A possible choice of
torus anchor has only polynomial multiplicity and would not affect(10).

Both periods have length O(N). Their area divided by N^2 tends to4/3,
and each physical tile density r_ij/det(P,Q) tends to1/4. A balanced
Z_p also has exactly p^2 of each type and area4p^2, giving the same
limiting density vector. No finite exact-equality assertion is needed.

For a fixed local block size m, partition a half-open period
parallelogram into lattice m-squares. Boundary sites cost O(Nm+m^2)
bits and bulk squares are bounded by their N_3(m) choices, exactly
as in(6). Thus(10)--(12) imply

    m^-2 ln N_3(m) >=(3/4)M for EVERY fixed m,
    4 h_3^loc ln2 >=3M.                                (13)

The limit N first, then the infimum over m, is explicit. This is a
count of ACTUAL periodic plane tilings, not a formal phase assignment
or an assertion about arbitrary finite bit blocks.

### 6.4 A strict exact sign, with no decimal estimate

At unit weights(9) reduces to

    M=(2/pi) integral_0^(pi/3) ln(2cos u) du.

The integrand is concave. Its chords on[0,pi/6] and[pi/6,pi/3]
give the lower trapezoid area (pi/12)ln6. Hence M>=ln6/6.
Combining with(8),(13),

    4 h_3^loc ln2 >=(1/2)ln6,
    (1/2)ln6-K=(13/2)ln2-4ln3>0,

the final sign following from 2^13=8192>6561=3^8. This proves(4)
without evaluating a transcendental constant or running a sign child.

## 7. What this proves and the precise remaining mass bridge

PM1 is an exact finite local encoding, with decoded physical tilings and
reduced tracks, not a guessed SFT identification. PM2 is a true
bounded-content full-boundary realization for existing plane patches.
PM3 supplies the previously missing strict local plane/full interface
after ONE boundary class and ONE exterior are fixed. These are useful
geometric/counting inputs, even though they do not give the desired
upper approximation R.

PM4 rules out identifying the free-window entropy with the fixed
balanced entropy, even after the natural limiting tile-composition
constraints. The obstruction is already in an exactly solvable actual
three-direction model and does not depend on possible higher-codimension
noncomputability or an abstract invented counting sequence.

An actual upper-R proof still needs a finite MASS upper functional
that retains the WHOLE prescribed macroscopic boundary/profile and
whose upper values can be matched by actual fine fillings. GR provides
the reference shapes; it does not multiply their counts. PM2 provides
an exterior, but its size may be a constant multiple of the patch span,
so it does not supply a vanishing relative collar cost. PM3 applies
only to genuinely near-flat strict families on whole buffers; it does
not say that all free patterns have that shape at every fixed scale.
Passing a band bound K to infinity before a box size, or replacing
pointwise profile data by one averaged tile-density vector, would lose
these conditions. No such interchange is made here.

The source record, exact failed routes, full proof obligations, commands,
read limits and compact immutable preservation metadata accompany this
candidate. No earlier byte, source cache or shared file is edited.
No practical algorithm, numerical improvement, entropy upper R,
two-sided computability, annual solution or novelty is claimed. TWO
OTHER whole audits must precede any coordinator promotion.
