# Routes rejected and exact remaining count gap

2026-10-17 UTC. **Candidate proof - unverified.** This is a record of
actual inference checks during GR1--GR4 construction. It is not a list
of new independent impossibility theorems.

## 1. Smoothing the whole vector profile is invalid

The accepted D=4 average of two full tiling profiles has the correct
range, full boundary and Vh=x, but its Delta_14 is -1/4 on the specified
overlap of a 12 tile and a 34 tile. Consequently neither averaging nor
ordinary vector convolution may be asserted to preserve the complete
ordered-minor constraint. A proof using that operation would fail at
the exact known counterexample.

Repair used here: take determinants against the two fixed VJ rows first.
For each individual i this gives the convex scalar cone q_u>=|q_s|.
Mollification is applied only to that scalar linear-cone inequality to
establish comparison along ALL segments. The remaining pair-minor
positivity is used directly through the Lipschitz area formula and
positive winding, not through convolution.

## 2. Generic affine multigrids are insufficient for nonlinear input

A rational constant J can yield a periodic multigrid tiling, but no
single such grid follows for a non-affine h. An arbitrary pseudoline
arrangement need not be stretchable. Inferring the construction from a
straight multigrid converse would leave the required variable-profile
and boundary interface unproved.

Repair used here: construct the actual entire scalar level arcs, choose
one phase, and build their finite dual disk. Positive physical face
orientations and exact boundary winding prove its degree-one embedding.
Straightening and periodicity are not needed.

## 3. A.e. differential inequalities do not automatically control an
exceptional prescribed line

It would be incorrect simply to integrate an a.e. derivative bound on
each chosen segment without accounting for exceptional lines. The
scalar cone is convex, so local scalar mollification plus interior
approximation gives the comparison on every segment, including the
boundary. This is why section 2 includes that argument explicitly.

## 4. A level set is not automatically a proper simple arc

Local implicit-curve language misses flat regions, extra components,
and boundary contacts. Smooth Sard hypotheses are unavailable for a
general Lipschitz profile. The full fiber construction instead makes
both level endpoints 1-Lipschitz in the transverse coordinate. A split
interval anywhere then creates positive level area. Only countably many
scalar levels can do this, and every other ENTIRE level is one graph
joining the exact color sides. No extra level component is dropped.

## 5. Invertible derivative at one point is not a neighborhood inverse

Differentiability with a nonsingular derivative does not justify an
inverse-function theorem for a merely Lipschitz map without additional
hypotheses. The argument uses only isolation of that one fiber, local
winding obtained by a derivative homotopy, and compactness. Winding
additivity then counts all preimages of a generic pair value. A separate
graph derivative check supplies the tame local crossing. No general
openness or local injectivity of the pair map is assumed.

## 6. Independent pairwise choices do not give a global phase

Selecting separately convenient levels for every pair could be
incompatible with a common ranked arrangement. The proof chooses a
single eta vector outside the finite/countable null union for ALL
levels and pairs, and outside the triple images as well. Opposite-side
rank pairing is automatic because each arc is the same scalar level
at both endpoints.

For general Lipschitz data this null-set argument does not promise a
rational eta. The separate rational PL algorithm avoids finitely many
proper affine hyperplanes by the moment curve; that finiteness is not
asserted for an arbitrary Lipschitz input.

## 7. Positive individual faces are not by themselves an embedding

A positive map of individual quadrilaterals could have several sheets,
extra exterior pieces or a pinched boundary. The full boundary-rank
calculation first proves that each boundary region has exactly one
interval. Its outside dual star is therefore an actual cone over a
simple cycle, whose complement is a disk. Summed face-boundary windings
then give multiplicity ONE. Integer unit-horizontal edges rule out
T-junctions; positive vertex-star angles rule out additional identified
vertices. Neither positivity alone nor connectivity alone replaces
these checks.

## 8. The existing finite-Q obstruction is not contradicted

OB1 has a forbidden extra coarse interior with prescribed local fine
boundaries 1243,4312. That data is not a full fine profile h on the
canonical balanced Omega. More precisely, an actual fine tiling in the
example can extend to a full admissible h, and that h can qualify here.
GR3 would approximate that h; it would not force its coarse image to
be the different forbidden filling. Thus the correct distinction is
the requested conclusion and prescribed data, not a blanket assertion
that every fine profile from the example violates our hypotheses.

The accepted 2-versus-3 coarse fiber comparison likewise concerns the
number of fine realizations, rather than whether one admissible full
profile can be approximated. GR3 is not a local exact-decoration
replacement theorem and does not remove the old multiplicity defect.

## 9. Exact admissible-profile realization still does not give R

GR3 supplies at least ONE tiling close to each admissible full h. Its
error is geometric O(1/p). That is not an estimate for the logarithm of
the number of tilings close to h. The error bound may be useful in a
future variational proof, but no count-sensitive upper approximation
or exponential fiber comparison has been proved in this packet.

In particular we do not reverse EC's one-sided lower certificate, use
an aggregate local LP as a sufficient finite counting model, assume
strong irreducibility of a free-boundary SFT, or infer computability
from entropy existence. No numerical bound or larger count table was
produced. The precise next useful missing interface is an effective
upper control of local/profile entropy compatible with these full
boundary realizations and with exponentially many choices. The present
candidate discharges only the full nonlinear-profile feasibility step.
