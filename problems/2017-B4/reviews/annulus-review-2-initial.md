# Annulus A1--A5: whole initial blind audit 2

2026-10-17 UTC. Independent nonconstructor audit of the complete
annulus-reasoning-r1 packet. No peer annulus report, issue ledger or conclusion
was read before this report, its ledger and source checks were completed and
jointly frozen. The earlier fixedD and DG reviews, and the separate FD2-01
targeted reaudit, remain immutable records.

## Conclusion and scope

I found no substantive defect in A1--A5 under their explicit hypotheses. The
annulus construction has a global rank condition and two actual planar
shellings; it does not infer a collar from four unrelated one-dimensional
envelopes. The six-pair winding argument supplies the rank condition at a
strict positive slope. The rational repeated-word frames and their block
shellings give the stated local entropy limit for exactly those frames.

I independently reconstruct every part below, including the digital-word
comparison, the bounded end-lobe deletion and the geometric disjointness
required by the entropy inequality. The finite-word FD2-01 counterexample
does not contradict this proof: no height-to-labelled-displacement inference
is used. The bounded gaps of the specifically constructed reference words
are also valid, with constants depending on the chosen rational frame.

Two nonblocking clarifications are logged: explicitly justify the use of
vertex separation in A3, and retain all A2--A4 hypotheses when summarizing
the transfer after A5. These do not overturn the stated results. The
coordinator alone may accept or promote them after both independent audits.

The input candidate is
problems/2017-B4/notes/annulus-reasoning-r1-candidate-v1.md,
20465 bytes, SHA-256
020d3f6408f9423b83ac2d5633d3e508a7468a16ebe6db673879fca2af1ff610.
The worklog, sources and author freeze are included in this whole audit and
the companion manifest.

The official open 2017 B4 concerns both limiting exponents for all marked
regular-polygon unit-rhombus tilings, \(n\geq2\). A1--A5 concern a narrower
fixed \(D=4\) integer-parallelogram model and one receiving boundary family.
They do not establish the full balanced zonogon hypothesis (H), a universal
cut-window extension, a zero-minor-stratum theorem, a numerical exponent, or
novelty. The candidate states these distinctions correctly.

## Setup and elementary planar shelling

The four physical vectors are \(v_i=(1,i-1)\). Positive edges have integer
lift increments \(e_i\) and unit horizontal displacement. A color word is
internally ranked, so each label has a fixed order within its color. Weak
order compares cross-color inversion sets.

The asserted adjacent-swap chain can be reconstructed without invoking an
external lattice theorem. For \(p\leq q\), look at their first different
position and bring the label wanted by \(q\) leftwards in the current word.
Every crossed label is later in \(q\). If it were initially larger, the
move would remove an inversion present in the current word but absent in
\(q\), contradicting inversion inclusion. Same-color labels cannot be
crossed because \(q\) respects internal rank order. Thus every move is
\(ij\mapsto ji\), \(i<j\), and creates an allowed inversion.

Geometrically this move replaces the lower two-edge chain by the upper
chain of the positive \(ij\) parallelogram. Its vertical path difference
is nonnegative, and it adds exactly that tile. The current path rises at
each move. At a fixed abscissa the previously swept region is below the
current path, whereas the newly added tile is above it. Hence tile interiors
are disjoint and the final union is the entire region between \(p\) and
\(q\), rather than a folded abstract surface.

Every tile vertex is integral, and each edge spans a unit interval in
the first coordinate. A tile vertex cannot occur strictly inside another
tile edge. Partial overlap of collinear unit edges is likewise impossible
with integral endpoints. Thus the planar shelling has the required
face-to-face incidence. Shared path portions have zero area and are
handled as prescribed weak-lens seams.

## A1: interval, ideals and the exact two-color range

Let \(p_0\leq q_0\) have content \(N\), and let \(P_0\) be the common
comparisons of the two ranked total orders. Their intersection is
transitive. An inversion of \(p_0\) must occur in both words; a
noninversion of \(q_0\) must occur in both. All other cross-color pairs
are free in this common-comparison poset. Same-color comparisons are
always fixed. Consequently its linear extensions are exactly the
shuffles in \([p_0,q_0]\).

For an integer \(h\) in the coordinate range \(0\leq h_i\leq N_i\),
define \(I(h)\) as the first \(h_i\) labels of each color. It is the
prefix of a linear extension only if it is an ideal. Conversely, order
\(I(h)\) by its restriction of \(p_0\), then order its complement in
the same way. There can be no predecessor in the complement of an
element of \(I(h)\); all comparisons within each part are respected.
Their concatenation is therefore a linear extension with that prefix.

Fix \(i<j\), and let \(b_p(k)\) count the \(j\)'s before the \(k\)-th
\(i\), with
\[
b_p(0)=0,\qquad b_p(N_i+1)=N_j.
\]
Inversion inclusion says \(b_{p_0}(k)\leq b_{q_0}(k)\). At horizontal
coordinate \(s=h_i\), a two-color path can have a vertical segment:
its lower endpoint is \(b_p(s)\) and its upper endpoint is
\(b_p(s+1)\). The complete closed lens between the lower path \(p_0\)
and upper path \(q_0\) therefore has integer vertical section
\[
b_{p_0}(s)\leq h_j\leq b_{q_0}(s+1).                 \tag{A1-range}
\]

The lower failure selects an \(i\) while omitting a \(j\) that must
precede it in both total orders. The upper failure selects a \(j\)
while omitting an \(i\) that must precede it in both. These are exactly
the possible cross-color failures of the ideal property. Checking all
six color pairs is thus equivalent to the whole ideal condition;
there is no additional rank permutation or multi-color relation left
unchecked.

The sentinels handle \(s=0\) and \(s=N_i\), and even \(N_i=0\):
the projected path can then be a vertical segment, while the explicit
coordinate-range condition fixes \(h_i=0\). Grid vertices on a boundary
are admitted by the closed inequalities. A winding-one test later
gives the stronger interior condition, so no ambiguity at a projected
boundary is used there.

## A2: concatenate global extensions and tile the actual annulus

The outer frame is a Jordan lens with the fixed words \(p_0,q_0\).
The actual inner Jordan lens has start lift \(a\), end lift \(b=a+m\),
and lower/upper words \(p\leq q\). Its color ranks are identified with
the consecutive global ranks \(a_i+1,\ldots,b_i\). The hypothesis says
that every boundary prefix \(I(h)\), including \(I(a)\) and \(I(b)\),
is an ideal of the one outer poset.

Let \(A\) be \(p_0\) restricted to \(I(a)\), and \(B\) be \(p_0\)
restricted to the complement of \(I(b)\). All prefixes along \(A\)
are ideals, because \(I(a)\) is an ideal and \(p_0\) is an extension.
Prefixes in the middle part \(p\), or \(q\), are ideals by hypothesis.
After \(I(b)\), a prefix of \(B\) is again an ideal: predecessors
outside \(I(b)\) occur earlier in its restricted \(p_0\) order, and
those in \(I(b)\) have already been selected. Hence
\[
p_0\leq A p B\leq A q B\leq q_0.
\]
The middle comparison is the original \(p\leq q\), with the same
integer rank shifts, and no comparison of persistent same-color
labels is reversed.

Fix swap shellings of the first and last comparisons. They tile the
bands between \(p_0\) and \(ApB\), and between \(AqB\) and \(q_0\).
The middle region is precisely the original inner lens: the paths
coincide along \(A\), then follow the inner \(p,q\), then coincide
along \(B\). At each abscissa these three regions partition the
outer vertical section, with disjoint interiors.

Because every edge advances the first coordinate by one, the whole
entry path \(A\) has abscissa at most that of the inner start, and
the whole exit path \(B\) has abscissa at least that of the inner end.
They cannot enter the inner interior. They are two actual seams of
the annulus, with exact common lift increments and rank labels.
Nothing has been left to an unspecified corner cap. Retain any
actual inner filling and attach the two fixed outer bands; the result
is a geometric tiling of the full outer lens.

A useful additional check concerns accidental physical contacts of
comparable paths. At a fixed integral prefix position, each swap
there strictly increases the physical vertical coordinate by \(j-i\);
all other swaps leave that prefix unchanged. Equal vertical coordinates
at that prefix therefore imply that no swap changed it, so the full
prefix lift agrees. Thus a common physical boundary vertex cannot
silently identify different lifts along these shellings.

For one prescribed inner boundary, the seams and bands are fixed before
the inner tiling varies. Restriction to that designated physical core
recovers it, proving injection. With varying inner boundaries, a
boundary code consists of \(a,p,q\). Four integer coordinates bounded
by \(cL\), two words of length at most \(cL\), and polynomially many
length conventions give at most
\[
(2cL+1)^4\,4^{2cL}\operatorname{poly}(L)=2^{O_c(L)}
\]
codes. Given the code and the final outer tiling, restriction again
recovers the original. Thus any output has at most that many
preimages. No strand-matching factorial has been suppressed.

## A3: winding in all six projected planes

Fix \(VJ=I_2\), all \(\Delta_{ij}>0\), and a common affine offset
\(c\in\ker V\). Every \(M_{ij}=(J_i;J_j)\) is orientation-preserving
and invertible; its least singular value is positive. The finite
minimum \(\sigma(J)\) is consequently positive.

At an inner boundary vertex \(x\), put
\[
y=M_{ij}x+c_{ij},\qquad \widehat y=h_{ij}(x).
\]
Since \(x\) is inside the physical Jordan outer lens and at distance
at least \(t\) from its boundary,
\[
\operatorname{dist}\bigl(y,M_{ij}\partial\Omega_0+c_{ij}\bigr)
\geq \sigma(J)t.
\]
The affine image is a Jordan domain with positive orientation. Moving
from \(y\) to \(\widehat y\) costs at most \(\sqrt2E_1\). The strict
inequality
\[
\sigma(J)t>\sqrt2(E_0+E_1)
\]
keeps \(\widehat y\) in that affine domain and at distance greater
than \(\sqrt2E_0\) from its boundary.

The actual projected outer lift loop differs pointwise from the
affine loop by at most \(\sqrt2E_0\). Their straight homotopy avoids
\(\widehat y\), so the actual loop has winding number one there.
This homotopy need not be simple and need not be the boundary of an
admissible interpolated profile; avoidance of the test point is
exactly what winding invariance requires.

The actual loop is the two-color subword of \(p_0\) followed by the
reverse subword of \(q_0\), with steps of the other two colors
collapsed. Inversion inclusion orders these two paths. Their common
pieces cancel and their remaining lobes have positive orientation.
The winding number is one in a lobe and zero outside the closed
projected lens. The test point is off the loop by the same avoidance
estimate; hence it belongs to the lens and satisfies (A1-range).

Repeating this for all six pairs proves both the coordinate range and
every ideal constraint. It controls the integer offset \(a\) and all
corner ranks at once. A2 now constructs the actual tiled annulus.
This argument does not mix profiles convexly and does not invoke the
bounded-displacement envelope theorem.

There is a small geometric detail in A3 worth making explicit.
Its containment assumption plus positive distance of all inner
vertices ensures strict physical containment of the entire inner
boundary in this integer unit-horizontal model. On an open interval
\((n,n+1)\), every inner and outer boundary is linear. An interior
contact of nonparallel edges would be a transverse crossing, violating
containment; a collinear contact would make the whole unit edge
common, including its vertices, violating the positive vertex
distance. Contacts at an integral abscissa are vertex contacts.
Thus the strict-containment premise of A2 is supplied, not omitted.

For fixed \(J\), \(E_0=O_J(1)\), and \(E_1=\varepsilon L\), a
separation larger than a suitable \(J\)-dependent multiple of
\(\varepsilon L+1\) suffices. This is a sufficient buffer condition,
not a proof that any shape admits a thin surrounding canonical
frame or that every annulus obtained has small area. Its constant
depends on \(\sigma(J)^{-1}\); no uniform boundary-stratum conclusion
follows.

## A4, first part: choose cone directions and one phase

Every row of \(J\) is nonzero. Put the first row direction at angle
zero for this argument. Positivity of its minors puts the other
three directions in \((0,\pi)\). Positivity between any subsequent
pair orders those directions strictly within that interval.
The total angle spread is less than \(\pi\), so their common positive
dot-product cone
\[
C=\{u:J_i u>0\text{ for all }i\}
\]
has nonempty interior. Choose two rational independent directions in
it, ordered so \(\det(u,v)>0\), and scale them so
\[
a=Ju,\quad b=Jv
\]
are positive integral vectors. Then \(u=Va\), \(v=Vb\), and
\[
a_ib_j-a_jb_i=\Delta_{ij}\det(u,v)>0.
\]

Pick \(0<\theta_i<1\) outside the finite rational hyperplanes where
any two threshold events coincide on either segment \(ta\) or
\(tb\). Such rational choices exist. Recording those events gives
two unambiguous words \(U,W\), where \(W\) denotes the candidate's
Vword. Their contents are exactly \(a,b\).

Integer translation by \(a\) or \(b\) preserves all thresholds
modulo integers. The same phase therefore gives the literal words
\(U^mW^n\) and \(W^nU^m\) on the two height-parallelogram chains.
There is no phase reset or hidden permutation at a corner.

## A4, second part: exact digital comparison

Here is a detailed reconstruction of the main comparison, rather
than an assumption that digital paths inherit an arbitrary
continuous containment. Fix \(i<j\), put
\[
\alpha=a_j/a_i,\quad \beta=b_j/b_i,\quad
A=ma_i,\quad B=nb_i.
\]
Then \(\beta>\alpha\). The two continuous chains in coordinates
\((i,j)\) have heights \(Y_{\rm low}(X)\) and
\(Y_{\rm up}(X)\), and direct evaluation gives
\[
Y_{\rm up}(X)-Y_{\rm low}(X)
 =(\beta-\alpha)\min\{X,A,B,A+B-X\}\geq0
\]
for \(0\leq X\leq A+B\).

At the \(k\)-th \(i\)-event the continuous abscissa is
\(X=k-1+\theta_i\). The number of earlier \(j\)-events is the
number of thresholds \(r-1+\theta_j\) below \(Y(X)\).
It is a nondecreasing function of \(Y(X)\), the same function on
both chains. The phase avoids a tie. Thus
\[
b_{U^mW^n}(k)\leq b_{W^nU^m}(k)
\]
for every \(i\)-rank \(k\). The six pairwise inequalities are
precisely the full inversion inclusion
\[
U^mW^n\leq W^nU^m.
\]
No rounding-order reversal is possible because the phases agree.

Each fixed word contains every color. A power has a bounded gap for
each color, and the single \(U/W\) junction contributes at most the
sum of two fixed word lengths. The proposed bound
\(2(|U|+|W|)\), including the end gaps, is sufficient and is
independent of \(m,n\). It depends on the fixed frame and cannot be
held uniform over arbitrary rational approximations.

## A4, third part: flatness and bounded end-lobe deletion

At an event parameter \(t\), the count of each color differs from
its continuous height \(ta\), or \(tb\), by less than one. At an
edge interior one can interpolate the two adjacent event parameters;
the same coordinatewise bound holds by convexity. Initial and final
partial parameter intervals also have bounded discrepancy. This
shows bounded physical distance to the straight chains.

Writing \(H\) for a lifted boundary point and \(S\) for its
corresponding straight height point, \(S\) is a combination of
\(a,b\) and
\[
(I-JV)S=0,\qquad H-JVH=(I-JV)(H-S).
\]
The boundary lift thus stays within a fixed constant of \(Jx\).
The bound covers all interpolated edges and is independent of
\(m,n\).

For \(m=n=L\), put \(u_x=\sum a_i>0\) and \(v_x=\sum b_i>0\).
The straight physical side slopes are strictly ordered because
\(\det(u,v)>0\). Their vertical gap is
\[
\left(\frac{v_y}{v_x}-\frac{u_y}{u_x}\right)
\min\{x,Lu_x,Lv_x,L(u_x+v_x)-x\}.
\]
Bounded physical error, with the fixed straight slopes, gives a
bounded vertical discrepancy at a common real abscissa. The
digital paths therefore cannot meet except within a bounded
abscissa distance of their two extreme corners. Integral prefix
positions and unit horizontal edges also preclude a new isolated
nonvertex contact between ordered path segments.

As proved in the A2 reconstruction, any common physical vertex of
comparable words has the same full prefix lift. Select the last
common vertex in the initial bounded box and the first common
vertex in the final bounded box. For sufficiently large \(L\)
these boxes are disjoint. There are no common vertices or edges
between them, so the retained paths form one Jordan lens.

The common prefix and suffix label sets agree. Restricting to the
middle preserves inversion inclusion and internal ranks. Every
discarded lobe lies in one of two bounded physical boxes. Its
positive tiles have area at least one; alternatively its possible
integer origins form a bounded set. Thus the total number of
discarded tiles and the number of possible discarded fillings are
bounded by frame-dependent constants.

A weak lens is counted by independently tiling its open lobes.
No tile interior can cross a pinch point or a shared zero-area
path piece between lobes. Therefore its count factors over those
lobes. The end-lobe factor lies between one and a fixed constant,
so deleting them changes the logarithmic count by \(O_J(1)\).
For small \(L\) a Jordan main lobe need not be defined, but this
has no effect on the asserted large-\(L\) limit.

## A4, fourth part: affine offsets and exact integer ranks

For a prescribed physical corner \(x_0\) and \(c\in\ker V\), round
\(Jx_0+c\) to an integer vector \(z\), with error \(\delta\)
bounded coordinatewise by \(1/2\). Then
\[
Vz=x_0+V\delta,\qquad
(I-JV)z-c=(I-JV)\delta.
\]
Both errors are bounded in the fixed data. Translating physical
points by \(Vz\) and heights by \(z\) consequently makes the
same fixed phase words approximate \(Jx+c\).

The integer translation preserves color ranks and phases modulo
integers. If one applies A1 to a translated frame, subtract its
starting lift from all heights and its physical projection from
all positions; its relative rank poset is exactly the one already
used. This is a normalization, not a new relabeling freedom.
For each fixed inner boundary fiber the frame, rounding choice
and padding are fixed before the filling varies.

The bounded corner adjustment must still fit the A3 buffer. This
procedure does not give arbitrary independently chosen integer
offsets at different corners; one global \(z\) fixes all of them.

## A5: finite counts, actual block gluing, and all scales

Let \(C_L\) count tilings of the complete weak lens between
\(U^LW^L\) and \(W^LU^L\), including its end lobes and exact
lifted boundary. A swap chain gives at least one filling. All
possible tile origins lie in an integer box of diameter \(O_J(L)\).
At each origin a subset of the six tile types can be recorded,
so a finite alphabet gives
\[
1\leq C_L\leq 2^{K_JL^2}.
\]
This is an elementary fixed-frame bound, not a free-window
entropy theorem.

For fixed \(\ell\geq1\), write \(L=k\ell+r\), \(0\leq r<\ell\).
Split each power into \(k\) blocks of size \(\ell\) and, if
needed, one remainder block. Bubble the \(U\)-blocks through the
\(W\)-blocks. Every full-size crossing replaces exactly
\[
U^\ell W^\ell\quad\hbox{by}\quad W^\ell U^\ell,
\]
at a fixed global prefix height, so its swept region is a
translated copy of the size-\(\ell\) weak lens. Each mixed-size
remainder comparison is also covered by the already proved
\(U^mW^n\leq W^nU^m\), and receives a fixed filling. If \(r=0\)
there is no remainder to cross.

For clarity, the blocks do not carry immutable disjoint sets of
same-color ranks that are illegally swapped. Each local word is
ranked by the global prefix before it, and replacement has the
same total content. Hence its endpoint height, and every later
prefix, remain unchanged. Its internal color-\(i\) labels are
exactly the next consecutive global ranks. The canonical rank
assignment supplies the seam data on both sides.

Every block replacement raises the physical path. The same
one-dimensional path-order argument used for an individual tile
shows that successive block regions have disjoint interiors.
Their locations and complete boundary words are fixed by the
block schedule and do not depend on the selected fillings.
Primitive unit-horizontal edges exclude boundary subdivisions
or T-junctions when those fillings are assembled.

There are \(k^2\) full-size crossings. Choose any of the \(C_\ell\)
fillings independently in each. They form an actual tiling of
the large weak lens; restriction to the designated regions
recovers every choice. Therefore
\[
C_L\geq C_\ell^{\lfloor L/\ell\rfloor^2}.             \tag{A5-gluing}
\]
As an independent area check, the change in type-\(ij\)
inversions between \(UW\) and \(WU\) is
\(a_ib_j-a_jb_i>0\). Weighted by tile areas \(j-i\), the
area is exactly
\[
\sum_{i<j}(j-i)(a_ib_j-a_jb_i)=\det(Va,Vb)=\det(u,v).
\]
The size-\(L\) area is \(L^2\det(u,v)\), consistent with
the full blocks and remainder shellings. No density-one packing
of arbitrary zonogons is assumed.

Set \(S=\sup_{\ell\geq1}\ell^{-2}\log_2C_\ell\), finite
by the alphabet bound. For each fixed \(\ell\), (A5-gluing)
gives
\[
\liminf_{L\to\infty}L^{-2}\log_2C_L
\geq \ell^{-2}\log_2C_\ell.
\]
Taking the supremum yields a lower bound \(S\). Every individual
\(L^{-2}\log_2C_L\) is at most \(S\), giving the opposite
limsup bound. Thus the limit exists and equals \(S\).
This argument covers all integer \(L\), not only multiples of
one block size. The uniformly bounded end-lobe factor gives the
same limit for the Jordan main-lens counts.

## Retained obstruction and degenerate attacks

The candidate's offset obstruction is valid. For
\(k=(1,-2,1,0)\), \(Vk=0\). In a fixed canonical frame,
translate a size-\((L-2s)\) inner main lens by \(s(a+b)\),
where a sufficiently large fixed integer \(s\) dominates the
bounded digital corner errors. Its physical collar is bounded.
Replacing the assigned lift by \(h+Mk\), with \(M\to\infty\)
and \(M=o(L)\), preserves the same physical patch and keeps
its affine error \(O_J(M+1)\).

Its initial color-2 rank is
\(s(a_2+b_2)+O_J(1)-2M<0\) eventually. It cannot extend to
the prescribed outer rank range. In any positive parallelogram
tiling of this outer lens, a color level outside its boundary
range would require a closed color track; the strictly monotone
transverse coordinate along such a track forbids that. This
also follows from the usual marked lift/track dictionary.

The obstruction is about an assigned lift. It says nothing
against insertion after arbitrary kernel relabeling, and it
does not meet A3's necessary growing-buffer inequality.

Other attacks checked:

- A1 permits weak or degenerate projections, with exact sentinel
  ranges. A2 instead requires actual Jordan inner and outer
  lenses. The two hypotheses are not interchanged.
- The homotopy need only avoid each test point; no simplicity of
  the intermediate loops or admissible-gradient interpolation is
  required.
- Rationality is unnecessary in A1--A3 but is explicitly assumed
  when constructing the canonical repeated frame in A4--A5.
- The phase is fixed once for both direction words. Using
  unrelated phases would invalidate the displayed digital
  comparison argument and is not allowed.
- Fixed \(J\) and the chosen frame data are essential. Zero
  minors, zero rows and arbitrary disappearing-color limits
  are excluded from A3--A5's quantitative claim.
- Different boundary codes can produce the same outer filling;
  the code-count fiber bound, rather than global injection for
  an uncoded varying family, is the claimed result.
- The conditional transfer summary retains physical nesting,
  a common affine lift and the required buffer. It does not
  manufacture a thin canonical frame around an arbitrary
  shape merely from the phrase “near-flat lens.”

## Unproved interfaces and source boundary

No result of the separately constructed DG1/DG2 packet is an
accepted annulus dependency in this audit. A1--A5 begin with an
actual two-path inner lens and prove no thin-band extraction
from an arbitrary cut window. A finite-alphabet encoding would
bound the information in a controlled discarded band, but the
required cutting operation is still missing.

The non-strict slope strata and a legitimate original-frame
regularization remain unresolved. The local limit for \(C_L\)
does not replace the full balanced zonogon count, and global
profile recovery with the original boundary is not proved.
These are the candidate's express limits, not hidden accepted
lemmas.

The sole named primary theorem in the worklog, Arroyo et al.
Lemma 2.2, concerns a plane-arc dual path and is a lead for the
separate cutting interface. Its finite-arrangement and
at-most-one-crossing hypotheses were checked against the
original paper. It is not a theorem about a finite disk,
an annulus or the entropy family, and it is not used to
justify A1--A5. The source record preserves this attribution
boundary. No originality claim was inferred.

## Review provenance, integrity and budget

This is a whole analytic audit. No enumeration, CAS, random
tests or numerical certificate was used. Only the assigned
annulus-review-2 prefix is written. The four input hashes,
earlier frozen review records and FD2-01 reaudit records are
verified in the manifest. No candidate, shared source, peer
annulus review, frozen original ledger or Git state was edited.

Requested model/reasoning: gpt-6.1-sol / max. Independent
effective-setting readback is unavailable. Authoritative
account-wide weekly telemetry at 2026-10-17 00:38:56 UTC was
20% total used, 10080-minute window, reset 1792745187.
The 90% total-used cutoff and integration reserve continue to
apply; no separately billed API was used.

This full initial report, issue ledger and source checks are
frozen before peer comparison. Acceptance remains with the
coordinator after the second independent whole audit.
