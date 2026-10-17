# Strict-slope transfer: independent whole initial audit R1

2026-10-17 UTC. Reviewer `review_2021_reasoning_j15_r2`.
Requested gpt-6.1-sol / max; no independently verified effective-setting
readback. This is a review recommendation, not coordinator promotion.

## Identity, independence and recommendation

Audited candidate: `notes/coordinator-strict-transfer-candidate-v1.md`,
SHA-256 `a19f8e66cb0fb810098eb209a47e73ecbb26e1d43316c13fa64bb5f743c8c3f1`.
Its freeze manifest has SHA-256
`a1b47d24cd01e032e97d11cfc917d787518f53d1902b71ddbeece24be428410e`.

I did not construct this packet or contribute its strict-transfer
composition. I completed the whole mathematical reconstruction below
without reading another new strict-transfer review or receiving its
findings. Accepted earlier dependencies and their acceptance scopes were
read. The separately queued rank-mesh construction has not been read as
a premise or as advance information for this review.

**Recommendation:** ST1, ST2 and ST3 withstand this whole audit with the
candidate's fixed rational strict slope, fixed matching shape, common
affine offset, genuine full-tiling source, buffered neighborhood and
reference-existence qualifications. No substantive defect or required
author repair was found. The lower count is a boundary-compatible
replacement count; it is not a count of fillings uniformly nearly affine
throughout their interiors. No global H, PR, zero-minor transfer or exact
official entropy rate is recommended for acceptance.

The frozen text still calls its annulus/CUT premises conditional. That
historical label has not been changed. The coordinator has now accepted
their exact mathematical bodies: I verified that the accepted expositions
end byte-for-byte with the frozen bodies named by the candidate, rather
than assuming a later theorem has matching scope by its title.

## 1. Official setting and dependency interface

The official 2017 B4 asks for the liminf and limsup of log2 C(n)/n^2
for fixed regular 2n-gon tilings. This packet is a partial fixed-D=4
integer-frame construction, not a determination of those values. It
does not replace the full fixed-boundary zonogon count by C_m.

I read the full accepted annulus and CUT expositions and their scope
registers; the complete accepted DG exposition; and the exact integer
dictionary, finite alphabet, lift and gradient portions of the accepted
fixed-D structural exposition. The precise interfaces needed are:

* CUT1 applies to a genuine full marked zonogon tiling, with the standard
  de Bruijn dictionary, not merely to an arbitrary locally tileable
  neighborhood. Its whole buffered neighborhood has a common near-affine
  approximation, and the two fixed independent directions have all lift
  increments positive. It extracts a comparable actual Jordan lens with
  O(L) boundary length, contained in a C_cut sqrt(epsilon)L enlargement
  and containing the corresponding inner parallel set.
* CUT2 recovers a source restriction by the extracted filling, its exact
  boundary/offset code and a fixed boundary-strip record. The strip has
  O(sqrt(epsilon)L^2+L) cells. Its O(L)-bit total version needs O(L)
  relative coordinate ranges; this is checked below rather than omitted.
* Range-corrected A2 pads a strictly nested actual comparable Jordan lens
  into an outer comparable Jordan frame when its all-color rank box and
  outer-poset boundary ideals hold. Empty inner colors are included in
  that range test. The annulus depends on the inner boundary alone and
  is fixed before varying an inner filling.
* A3 obtains those rank and ideal conditions from one common affine
  approximation and a positive-minor physical vertex buffer. The buffer
  test is sigma(J)t>sqrt(2)(E0+E1). It does not permit independent
  corner offsets or forget the inner lift.
* A4 supplies the fixed-phase canonical U,W frames, uniform physical and
  affine errors, bounded corner trims, and rounded integer translations
  for arbitrary desired corners and common offsets. A5 supplies the
  all-integer-scale limit of their complete weak-lens counts C_m.

These accepted hypotheses are retained. In particular the candidate's
“as stated, including every ... qualification” clause and its use of
full-tiling representatives must be read literally. The new statements
do not assert CUT1 for a disk lacking a compatible full-tiling source.

## 2. Fixed rational frame and receiving counts

Fix D=4, v_i=(1,i-1), VJ=I, and rational J with every ordered row minor
strictly positive. The two fixed common-positive directions u,v satisfy
det(u,v)>0 and a=Ju,b=Jv positive integral. Because VJ=I, u=Va and
v=Vb, so their physical increments are exact integer vectors. The same
fixed phase is used in all powers of U and W. No phase is chosen after
seeing a source filling.

The six two-row matrices of J are invertible, hence their least singular
values have a positive minimum sigma(J). This constant is fixed and is
not uniform as a minor tends to zero. The positive components J_i u,
J_i v also have fixed positive lower and finite upper bounds, supplying
the CUT/DG direction margins.

A5 counts the complete weak lens between U^m W^m and W^m U^m. Its
bounded end lobes lie in fixed-size boxes. For a fixed m, tilings of the
open lobes recover independently by restriction; their total count is
the main-lens count times the counts of the remaining bounded lobes.
Their product is uniformly bounded by some B_J. Thus the Jordan main
count is at least C_m/B_J. Conversely, appending one fixed filling of
each discarded lobe injects the main fillings into the complete count.
There is no unidentified label or seam matching factor.

The accepted block-swap construction gives

    s=lim_(m->infinity) log2 C_m/m^2,
    0<=s<infinity,

at every integer m, not only multiples of one selected block. Its
main-lens counts have the same limit. Only this one shape and phase
are used below.

## 3. Matching-shape margins and the order of constant choices

Let delta=sqrt(epsilon)L. A centered parallelogram with side parameter
L has four fixed unit supporting normals. Increasing its side parameter
to L+2t displaces each supporting line outward by d_j t for a fixed
d_j>0. Put c_shape=min_j d_j>0. Shrinkage has the same normal gaps.
This is the required matching-shape fact; mere flatness of an unrelated
lens would not supply it.

The canonical digital boundary and its bounded corner trims have a
fixed physical error B, including the rounding displacement. The
main Jordan domain contains the B-eroded canonical parallelogram and
lies in its B-neighborhood: this follows from the pointwise digital
side approximations and their consistently oriented two-path boundary,
with modifications only in the bounded corner boxes. The analogous
statement holds for every sufficiently large canonical size.

Choose A first, sufficiently large compared with C_cut/c_shape and
the other fixed geometric constants. For

    m=ceil(L+2A delta),       k=floor(L-2A delta),

the half-parameter gaps are at least A delta. In both uses below the
physical buffer is bounded below by

    (c_shape A-C_cut)delta-B.

For example A>=4C_cut/c_shape and sufficiently large delta make this
at least (c_shape A/2)delta. Thus c4 can be fixed as a positive shape
constant independent of L and epsilon after A is selected. Ceilings
and floors strengthen rather than erode the concentric margins; only
bounded digital errors need absorption.

Choose epsilon0 next so that 1-2A sqrt(epsilon)>0, bounded away from
zero, and so that the epsilon L error is less than half the collar
allowance in A3. With b=sigma(J)c4 A>0 it is enough that

    sqrt(epsilon)<=b/(2sqrt(2)C1)

when C1>0. Then require L large enough, depending on epsilon, that

    b sqrt(epsilon)L>=2sqrt(2)C'_J,

and that CUT1's scale threshold and all bounded-rounding thresholds
hold. Taking a strict inequality at the threshold if necessary gives
sigma(J)t>sqrt(2)(C1 epsilon L+C'_J). These choices show that there
is no circular assumption or epsilon=0 use hidden in the qualitative
phrase “sqrt(epsilon) dominates epsilon.” All frame and phase data
are fixed before taking L to infinity.

## 4. The common integer translation and rank offsets

For a desired corner y, choose z in Z^4 nearest Jy+c coordinatewise,
using a fixed rounding tie rule. If e=z-Jy-c is bounded, then

    Vz-y=Ve,
    (I-JV)z-c=(I-JV)e,

because VJ=I and Vc=0. Both physical and affine-offset errors are
therefore bounded independently of y, c, L and the filling. Translating
physical space by Vz and heights by z gives the same fixed phase words
with boundary error O_J(1) relative to Jx+c.

For ST1, y=x0+(L-m)(u+v)/2, so this one z and the one receiving frame
are fixed across the entire source family. For ST2 the corresponding
inset corner and z are fixed before varying any canonical filling.
Trimming the bounded end lobes only changes the frame's starting height
by its fixed actual prefix; it does not introduce a new adjustable offset.

When A3 is applied in an outer main frame with starting height z0,
one rebases x to x-Vz0 and h to h-z0. The common affine offset becomes
c-(I-JV)z0 on both boundaries, exactly the accepted translated-frame
convention. Neither the source's assigned rank shift nor a missing color
is discarded. A3 consequently supplies the entire available rank box
before the ideal test, including endpoints and absent colors, as required
by the repaired A2.

## 5. ST1: extraction, fixed-frame padding and recovery fibers

Choose one genuine full-tiling representative for each distinct source
restriction to P_L. The whole-neighborhood hypothesis permits CUT1 for
each representative with the same fixed data and constants. The resulting
actual Jordan lens Omega_T is comparable, has its original assigned
lifted boundary, lies in P_L's C_cut delta neighborhood, and contains
its C_cut delta-eroded core.

Center the canonical size-m frame as specified above. The margin calculation
places Omega_T strictly inside its main Jordan lens, with vertex buffer
at least c4 A delta. The outer canonical boundary has affine error at
most C'_J relative to the same Jx+c; the actual inner boundary has error
at most C1 epsilon L because it is inside the tiled hypothesis neighborhood.
The quantitative A3 inequality holds by Section 3. Its hypotheses are
exactly nested comparable actual Jordan lenses with their fixed lifts;
no arbitrary patch-extension theorem is substituted here.

A3 gives all relative ranks and ideals, so A2 pads Omega_T into the
fixed canonical outer main frame. Choose the padding deterministically
from the inner boundary. Append fixed fillings in the bounded outer
end lobes. The result is one of the C_m complete-frame tilings.

For a fixed inner boundary/offset code, restriction of that output to
the identified inner region recovers its filling. CUT2's original
alphabet strip record then recovers every source tile relevant to P_L,
including cases where Omega_T extends outside P_L. There is no need to
recover or count the chosen full representative outside the source
restriction. Different representatives with the same source restriction
were already reduced to one before the map was made.

The relative-coordinate qualification is fulfilled uniformly. Let z_base
be one integer vector nearest Jx0+c, fixed across the family. Rebase
heights by z_base and physical coordinates by Vz_base. Since
Vz_base-x0=O(1), the whole O(L) neighborhood has O(L) physical coordinate
range. The assumed affine error and fixed J give O(L) height range too.
The receiving corner shift is O(delta)<=O(L). Boundary words have O(L)
letters; a starting height and location cost only O(log L) bits; the
finite length/tie data are absorbed in O(L). Absolute global ranks
thus add no factorial or unbounded range cost.

The deterministic strip has O(delta L+L)=O(sqrt(epsilon)L^2+L)
cells, with a fixed finite local alphabet. Boundary/offset coding costs
O(L) further bits. Hence every output has at most
2^[K(sqrt(epsilon)L^2+L)] possible input source restrictions, giving

    log2 |F|<=log2 C_m+K(sqrt(epsilon)L^2+L).

This proves the stated ST1 upper bound, including variable cut boundaries,
without treating annulus insertion alone as a bounded-fiber statement.

## 6. ST2: one actual exterior and arbitrary canonical main fillings

Fix one actual reference tiling satisfying the same whole-neighborhood
hypotheses and cut its Omega_T once. The canonical size-k frame is
concentric and inset; the geometry in Section 3 puts its whole main
lens inside the eroded P_L core and hence inside Omega_T, with the same
positive lower buffer. The outer boundary is now the actual Omega_T
with error C1 epsilon L, and the inner canonical boundary has error
C'_J. A3 is symmetric in the sum of the two errors and therefore
applies after this exchange of roles.

The inner canonical lens has at least one actual filling by its accepted
shelling construction. A2 may first be applied with that filling to
construct one annulus, which depends only on the boundary. Keep this
annulus and the reference outside Omega_T fixed. Vary all canonical
main-lens fillings. Each is a face-to-face filling with the same assigned
boundary lift, so it glues exactly to that annulus. Restriction recovers
each filling, giving at least C_k/B_J distinct replacements of the
chosen actual reference exterior. No count of a free-window family or
unproved full-zonogon extension is needed.

The interiors being varied need not be epsilon L-near-affine. A3 uses
only their boundary approximation, so that absence of an interior bound
does not invalidate the insertion. It does limit the interpretation of
the lower count: these are boundary-compatible replacements, not a lower
bound for the same uniformly flat class appearing in ST1.

The claimed O(L) profile change is nevertheless valid. Old and new lifts
agree on the boundary of the changed Jordan patch and have uniformly
bounded coordinate gradients on every tile. For any point in the patch,
take a closest boundary point. The segment up to that boundary remains
inside the patch and has length at most its O(L) diameter. Integrating
the bounded difference gradients along it gives sup|a_new-a_old|=O_J(L).
This argument does not require convexity of the patch or an admissible
convex interpolation of profiles. On a physical patch of diameter O(eta p),
division by global scale p gives O_J(eta), not O(epsilon eta).

## 7. ST3: the two scale limits have the stated quantifiers

Fix 0<epsilon<epsilon0 first. Then
m/L tends to 1+2A sqrt(epsilon), and the all-integer A5 limit gives

    limsup_(L->infinity) L^-2 log2|F_L|
      <=(1+2A sqrt(epsilon))^2 s+K sqrt(epsilon)

along every source sequence satisfying the hypotheses. The O(L) coding
term disappears. The source family need not be an entire set of all
frame fillings, so this is legitimately an upper statement.

Similarly k/L tends to 1-2A sqrt(epsilon)>0, and
log2 B_J/L^2 tends to zero. If compatible actual reference tilings exist
at every sufficiently large L, the universal ST2 construction for each
one gives

    liminf_(L->infinity) L^-2 log2(number of replacements)
      >=(1-2A sqrt(epsilon))^2 s.

If they exist only on a subsequence, only the corresponding subsequence
liminf is justified, precisely as the candidate states. No reference
existence or all-scale global fixed boundary is manufactured by the
local argument. There is also no inference of entropy from only one
particular reference size or one canonical block C_l.

Letting epsilon decrease to zero after these scale limits compares the
two displayed quantities to the same fixed-frame s. It does not assert
that both quantities count one identical nearly affine interior class.
It does not compare different frame shapes or assume continuity of s
as J varies.

The rational-approximation remark has its stated limited validity. In
the affine solution space VJ=I, rational solutions are dense and strict
minor inequalities are open. If J' approximates a strict irrational J,
recenter the offset at a fixed window center x_c by
c'=c+(J-J')x_c. Then Vc'=0 and

    (Jx+c)-(J'x+c')=(J-J')(x-x_c)=O(||J-J'||L).

Fix J' and all its frame denominators before L tends to infinity.
This does not provide a uniform irrational-slope entropy theorem or any
continuity assertion for the resulting fixed-frame s.

## 8. Adversarial checks and exclusions

The following were specifically checked rather than suppressed:

* Centering a different shape or keeping only an endpoint buffer would
  not suffice. Matching u,v and the whole-neighborhood CUT hypothesis
  are both used quantitatively.
* The incoming and outgoing corners are assigned by one global integer
  translation. All-color rank ranges come before ideality; the old absent-
  color counterexample to unrepaired A2 is not admitted.
* The variable cut boundary is included in the upper code. A2's fixed-
  boundary injection alone would not bound the whole source family.
* The canonical C_k interiors are allowed to fluctuate at order L.
  The profile edit is controlled only at the later window mesh scale.
* Epsilon is positive, chosen after fixed frame constants, with
  L>=L0(epsilon). Zero-minor limits and epsilon=0 are not included.
* C_m counts complete weak lenses, and bounded lobe factors are explicitly
  accounted for before main-lens insertion. It is not the full balanced-
  zonogon count B_D(p).
* The lower all-scale statement is conditional on actual all-scale
  references. Global skeleton counts, strata and remainder losses remain
  separate, unproved obligations for H or PR.

No counterexample or missing mathematical inference was found for ST1-ST3
with those hypotheses. The historical conditional dependency labels can
be updated by an acceptance header only after this packet's own second
whole audit; they should not be read as a defect in its fixed implication.

## 9. Process and immutable records

Only `reviews/strict-transfer-review-1-*` was written. There was no
mathematical enumeration, CAS, code experiment, dependency installation,
candidate edit, shared-file edit, Git operation, spawning, charge, contact
or source redistribution. Python was used only for byte/hash validation
and review metadata. Full annulus and CUT bodies were read; a truncated
batched display was followed by separate reads covering all missing A4-A5
text. No theorem was accepted from a truncated passage alone.

Authoritative telemetry at this transition: 24% total weekly used,
10080-minute window, reset 1792745187. Stop threshold remains below
90% total with integration reserve. The complete report, claim ledger,
source checks and manifest are frozen before a peer comparison or any
author-repair request. Earlier reviews and construction packets are
preserved byte-for-byte.
