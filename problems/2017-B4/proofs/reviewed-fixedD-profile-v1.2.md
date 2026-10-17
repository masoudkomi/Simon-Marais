# Fixed-D profile entropy: an exact upper reduction and the missing recovery

2026-10-17 UTC. **Proved, independently reviewed P1 and qualified side-padding
partial results; the recovery program remains explicitly unproved.**
Accepted exposition v1.2 of author-repaired v1.1. Both full initial audits,
FD2-01 author repair and both independent targeted re-audits were read by
the coordinator. Original v1 and its false consequence/counterexample
remain preserved. See reviews/fixedD-structural-acceptance.md/json and
[accepted structural companion](reviewed-fixedD-structural-v1.2.md).
Status and companion links change here; the repaired proofs do not.
EAI, PR, H and the exact official rates are not accepted conclusions.

## 1. What compactness and upper semicontinuity really prove

Normalize by p^2 here; division by the fixed constant D^2 converts to (H).
For a subset U of compact profile space X_D let

    Z_p(U) = #{tilings of Z_p with normalized lift in U},
    L_plus = limsup p^(-2) log_2 B_D(p),
    L_minus = liminf p^(-2) log_2 B_D(p).

Use log 0=-infinity. The already reviewed quadratic arrangement bound
gives a finite uniform upper bound. Define

    s_plus(h) = inf_(epsilon>0)
                 limsup_p p^(-2) log_2 Z_p(B_epsilon(h)).

**Compact-profile lemma:** s_plus is upper semicontinuous and

    L_plus = max_(h in X_D) s_plus(h).                    (P1)

This statement does not require convexity of X_D. To prove upper
semicontinuity, fix epsilon>0. For h' sufficiently close to h,
`B_(epsilon/2)(h')` lies in `B_epsilon(h)`. Thus s_plus(h') is bounded
above by the limsup count of the latter ball. Take the upper limit as
h' tends to h and then the infimum over epsilon.

For (P1), one inequality is immediate. Suppose every s_plus(h) were
less than L_plus. For each h choose a neighborhood ball on which the
limsup count is less than a number c_h<L_plus. Compactness gives a
finite such cover of X_D. The global count is at most the sum of these
finitely many neighborhood counts, whose normalized logarithmic limsup
is at most the maximum of their c_h, still below L_plus. This is a
contradiction. Upper semicontinuity supplies a maximizer as well.

There is no inferred lower bound at all sufficiently large p. The
additional **profile recovery property**

    for a maximizer h*, for every epsilon>0,
    liminf_p p^(-2) log_2 Z_p(B_epsilon(h*))
       >= s_plus(h*)                                    (PR)

would prove L_minus>=L_plus and hence (H). Requiring recovery for every
h is stronger than necessary. Conversely (H) alone need not supply one
profile present with optimal entropy at every scale, so (PR) should be
viewed as a useful sufficient target, not a claimed equivalence.

Upper semicontinuity alone cannot close the gap. Abstractly one may put
all configurations at one profile and give scale p
`2^floor(p^2(1+(1/4)sin(log p)))` configurations. Then the profile entropy
is upper semicontinuous, the count is nondecreasing for all sufficiently
large p, its logarithm has increments O(p), and its normalized entropy
oscillates. Positivity of the derivative follows from
`2+(1/4)(2 sin t+cos t)>0`. This is not a rhombus-tiling counterexample;
it shows exactly why compactness, monotonicity and an upper entropy
supremum do not by themselves imply an all-scale recovery theorem.

## 2. The finite lattice model does not remove the boundary condition

Finite-range locality gives van Hove/free-window upper entropy limits.
It does not show that patterns can be sewn into the specified lifted
frame of Z_p. The boundary height is non-affine and constrains tile
frequencies through macroscopic conservation identities. In D=3 this
distinction already separates the boxed-hexagon entropy from the
flat/free entropy. A general SFT theorem with free boundaries therefore
does not prove (H).

This distinction was checked in a primary theorem rather than assumed:
Balister--Bollobas--Quas, Theorem A, counts `N(Lambda)`, the restrictions
of ALL points of the infinite subshift to Lambda. Its convergence over
large convex sets does not prescribe one polygonal boundary word or one
lifted frame. Their separate Theorem B assumes strong irreducibility,
which includes a uniform filling distance; that hypothesis is not established for
the present boundary-constrained model.
[Author manuscript, definitions and Theorems A--B, pp. 2--4](https://web.uvic.ca/~aquas/papers/paper15.pdf).

Fixed-window coarse graining does supply upper estimates. For a physical
mesh of size delta p, the tile data on its one-tile-wide skeleton have
O_D(p/delta) cells, so recording them costs o(p^2) at fixed delta.
Once the skeleton is fixed, interiors are independent exact boundary
fibers. Local patches in boxes of side L have at most exp(O_D(L^2))
patterns, simply from the finite local alphabet. Thus boxes in a small
area fraction contribute a small quadratic entropy bound.

These observations locate high entropy in finitely many local fibers.
They do NOT assert that their boundary words can be replaced by another
fiber with the same number of ports, or that all those fibers can be
replicated into the large zonogon. The full paired boundary word and
the vector height traces must survive the lower construction.

## 3. A local extension target strong enough to give recovery

Here is a substantive local target rather than an assumption that
zonogons pack themselves. It is deliberately stated as UNPROVED.
In particular its proposed uniform modulus is not furnished by the
side-padding lemma: that lemma requires ranked displacement or a fixed
reference gap G and has G-dependent constants. A proof must keep track
of the chosen backgrounds and separately confront degenerating strata.

**Entropy annulus interpolation target EAI_D.** There should be a modulus
rho_D(epsilon)->0 and a local scale threshold with these properties.
Consider a large simply connected parallelogram-type window of diameter
L, cut from an actual D-direction tiling. Its normalized vector lift is
epsilon-close to one affine admissible lift `Jx+c`, J in K_D. At rational
slopes use the canonical periodic flat tilings of the structural note;
near irrational slopes allow a rational admissible slope within epsilon.

1. **Extraction.** Every finite family F of such window patches can be
   mapped to patches with one prescribed periodic flat outer boundary
   in a window enlarged by at most rho_D(epsilon)L+O(1). The map may
   discard a boundary band and repair rare-tile or phase data, but its
   fibers have size at most `2^(rho_D(epsilon)L^2+o(L^2))`. The periodic
   phase and integer lift offset may be selected from the boundary data.

2. **Insertion.** In any actual outer reference patch with that same
   affine approximation, one can surround a periodic flat inner window
   of relative side loss at most rho_D(epsilon) by a tiling annulus
   matching the actual outer boundary. The annulus is fixed before
   varying the inner periodic-boundary tiling. If boundary-stratum
   repairs are necessary, their multiplicity/loss obeys the same
   subquadratic-density bound. Different inserted interiors remain
   recoverable from the designated core.

The target must apply in the relevant admissible boundary strata, or be
accompanied by a proof that their entropy can be approximated with
strictly positive slopes. The latter is not supplied by convex mixing:
the structural note gives an exact D=4 counterexample to that shortcut.
The microscopic offset in a zero-density color cannot be assigned
arbitrarily; phase/offset choices and rerouting of the few entering
strands are part of the target's hypotheses and conclusion.

Why this type of target would suffice is specific. At a maximizer h*
from (P1), Lipschitz differentiability gives arbitrarily fine disjoint
windows on which h* is close to its affine tangent, outside a set of
arbitrarily small area. In a high-entropy subsequence of tilings close
to h*, record a fine mesh skeleton. The finite alphabet makes its cost
subquadratic. Extraction bounds each important local fiber by a fixed
periodic-boundary family, up to the specified small entropy loss.
For each fixed periodic family, one would additionally need exact
commensurate window definitions and opposite collars matched by period
translations before invoking two-dimensional boundary-preserving
replication. Those compatibility conditions are part of the unproved
extraction/insertion program. Merely calling a boundary periodic does
not supply its entropy limit.

For an all-scale reference, choose one large finite tiling close to h*,
dilate it by an integer factor, and subdivide every enlarged ij
parallelogram into the forced fine ij grid. This preserves its normalized
lift. At scales not divisible by the fixed starting size, an explicit
boundary-preserving remainder padding is still required; invoking the
side-envelope theorem for that step would require its labelled/gap
hypotheses, and height closeness alone does not provide them. The
remaining intended construction would insert independent fixed-boundary
cores in selected tangent windows and recover choices by restriction.
To prove(PR), one must show that band and exceptional-area losses,
extraction multiplicity and all padding errors tend to zero in one
quantified argument. This paragraph is a program, not an established
all-scale lower bound. It does not rely on convexity or uniqueness of
a maximizing profile.

The foregoing is a reduction/program, not a completed proof: a precise
choice of cut windows, rational phases, corners and boundary-stratum
repair is part of EAI_D and must be proved. Merely calling those costs
surface terms would repeat the missing inference in the older source.
Neither EAI_D nor its all-scale application is promoted here.

## 4. What can already be proved about its boundary words

The bounded-envelope lemma in the accepted structural companion controls a qualified
one-dimensional part. Let the boundary words have equal color counts,
length O(L), and a common reference word, adjoined to the family as in
the structural theorem. If every ranked occurrence
has positional displacement at most r from that reference, then universal
weak-order meets and joins stay within O_D(r) physical distance and
cost O_D(r*L) padding area. This is the actual labelled theorem.

One may start instead with a prefix color-count bound epsilon L only
when a separate reference gap bound G is established. Include the gaps
before the first and after the last occurrence of every active color.
The companion v1.1 proof gives ranked displacement at most
G*ceil(epsilon L). The resulting bounds are

    band O_(D,G)(epsilon L+1),
    area O_(D,G)(epsilon L^2+L).

G is fixed for that reference, for example a fixed all-active-color
periodic word; it is not uniform over arbitrary near-flat words or
slopes approaching a missing color. Every resulting padding is still
an explicit adjacent-swap tiling. Rank labels are forced by each color
word, so no unrestricted matching factorial is introduced.

FD2-01 shows why the extra hypothesis is substantive. Reviewer2 supplied,
for M>=2 and length L=3M, the equal-content reference and two words

    w0=1^M 2_1 3^M 2_2...2_M,
    wA=2_1 1^M 3^M 2_2...2_M,
    wB=1^M 3^M 2_1...2_M.

Both have prefix color-count error at most1 from w0, but their join
with w0 is 3^M 2_1 1^M 2_2...2_M. The inversions(1_a,2_1) and
(2_1,3_c) force all(1_a,3_c). Its prefix-M height error is M and
its added physical area is2M^2+2M. Label2_1 moves M positions, and
the reference has unbounded gaps. Thus there is no D-only height-to-band
or height-to-area consequence. This is a correction of v1's omitted
hypothesis, not a counterexample to the labelled lemma,(H), or the
expressly unproved EAI target.

The missing two-dimensional work is to make these side envelopes close
around all corners with the right color-rank identifications, then match
them to one periodic boundary pattern, and finally handle frozen or
parallel-row strata without changing macroscopic flux. No proof of
those operations is hidden in the envelope lemma.

An overstrong annulus statement is false even before D=4. On a pure ij
flat slope, a zero-density color has no strands crossing a canonical
outer frame. An inner lift shifted by a positive constant in that color
cannot be connected to that frame while preserving its assigned color
labels: a same-color de Bruijn curve cannot close inside the annulus.
Uniform closeness of heights alone permits such an O(epsilon L) shift.
Thus exact interpolation for arbitrary near-flat lifted collars must
include flux/phase compatibility or allow a controlled repair. This is
why EAI_D is stated with those qualifications.

## 5. First nontrivial D=4 case: outcome of this pass

The D=4 analysis yields an exact obstruction to convex interpolation and
a candidate bounded-band weak-order extension lemma. It does not yield
the entropy of all octagonal tilings or an all-scale recovery theorem.
The source route through generalized partitions gives useful finite
codings but does not, without an additional uniform asymptotic argument,
repair the annular matching step.

The immediate useful next target is an explicit D=4 annulus construction
for strictly positive rational slopes, using correctly qualified
labelled side control or a separate global rank argument. Such a proof
must establish exact closed boundary, corner and phase compatibility;
one cannot infer it from bare prefix closeness. It must then be followed
by stratified entropy control or a legitimate global regularization
with the original zonogon frame. No routine enumeration would settle
either unrestricted inference. Any separate later annulus candidate
requires its own audits and is not a premise of this repair.

## Preserved failed shortcuts

- Fixed integer prototiles plus a free-boundary entropy theorem: loses
  the prescribed vector lift along the full zonogon boundary.
- Convexly average height profiles: false already for two unit-octagon
  tilings with the same boundary, by the companion example.
- Infer recovery from compactness and an upper semicontinuous profile
  entropy maximum: supplies (P1) only; all-scale lower recovery is absent.
- Assume arbitrary near-flat collars interpolate: misses phase/flux
  obstructions at zero-density strata.
- Assume `B_D(2p)>=B_D(p)^4`, or pack homothetic zonogons at density one:
  no such construction is given or used.
- Replace the full count by one periodic-grid patch family: each such
  family is a local building block only, and EAI_D is precisely the
  unproved transfer back to the full fixed frame.

No mathematical computation, enumeration, CAS process, charge, API call,
source-PDF redistribution, Git commit, or push was used. The stated partial lemmas are accepted after independent audits;
EAI, PR, H and the recovery program remain explicitly unproved.
