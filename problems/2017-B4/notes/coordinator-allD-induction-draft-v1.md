# All-direction recovery induction: construction draft

2026-10-17 UTC. **Research draft, unverified.** Coordinator root.
This is not an accepted theorem or a replacement for the whole G4 audits.
No numerical official rate or novelty is claimed. No mathematical program
was used. The exact new strict premise below remains under its own two
fresh whole audits. This draft will require a complete frozen proof and
two fresh whole nonconstructor audits before promotion of any new claim.

## Precise possible induction statement

For EACH fixed D>=2 and C<infinity, define GE_D,C(r) using actual
Jordan disks with complete colored lifted boundary of perimeter<=Cr,
and ONE common exterior in a full standard D-direction zonogon with
at most Cr curves of each color. Every filling must glue to that
same exterior. Zero ambient contents can be allowed: missing colors
can alternatively be added in a deterministic boundary belt before
balancing, without changing the original filling or its position.

Put

    Delta_D(B)=max(0,log2 Z(B)-liminf_M M^-2 log2 Z(MB)).

The intended induction is

    UR_D: sup_(B in GE_D,C(r)) Delta_D(B)/r² ->0
          for every fixed C, with D fixed first.              (A)

The new strict local premise is the COMPLETE exact US_D1–US_D3 in
allD-uniform-strict-reasoning-r1-candidate-v1.md,
SHA256 fc280881b1df650d07ab48f0f4c19d0e77f076e6b39a13f3a0b8d9969074a433,
37267bytes. It is a candidate, not an accepted theorem. Its all-D
AD1–AD5, ACUT/AST and denominator-safe uniform constants need both
whole independent audits. Merely invoking the earlier D4 theorem
does not discharge this premise for D>4.

Other local interfaces are already accepted at EACH fixed D:
the full marked/lift dictionary and K_D minor closure; OC1–OC3;
FL1; LW1; CW0–CW4; SP1–SP3; and remainder padding.
The all-D induction would use SP rather than silently broadening
the D4-only parts of the original RM2 statement. Its lower-dimensional
input is precisely UR_(D-1) on the GE class in(A), not just balanced
zonogon counts and not a periodic family.

## Base and the exact boundary reduction

For D=2 every full marked tiling is the unique grid of its single
parallelogram type: Va=x determines its two height coordinates,
and the rank tracks are the coordinate grid lines. A filling of any
actual GE2 disk extends to that same full grid and is its restriction.
Thus Z(B)=Z(MB)=1 and UR2 has zero deficit. This proposed elementary
base avoids importing a dimer variational theorem, provided the
all-D strict premise really includes D=3.

At an a.e. tangent in K_D, OC chooses one finite cyclic cut, with
A and A inverse bounded independently of zero minors. If every row
minor is positive, use US_D. Otherwise, after reorientation there
is a zero row or an adjacent positive-parallel pair. With a zero
row choose it and ONE adjacent slot: the chosen minor is zero.
Without a zero row, a zero minor means a consecutive positive-parallel
group contains an adjacent pair. Merge JUST this one consecutive pair.
All D-2 other COLOR groups stay singleton, even when some of their
tangent rows are zero or parallel to others. No entropy vanishing,
all-zero-row deletion or simultaneous multiple-merge theorem is used.

FL1 gives S=O_D(epsilon L²+L+1) chosen-pair events in the whole
fixed target square and its star enlargement. LW1 at fixed rank
spacing r0 discards bad closed selected faces and boundary-cut faces,
with cost

    O_D(L²/r0+epsilon r0² L²+r0² L+r0 L+r0²+log p).

Each retained good disk lies in an actual closed selected face
with no chosen-pair event even incident at a vertex. The all-D
SP theorem then gives an EXACT fine/coarse count bijection, at
every integer dilation, for this one merged group and D-2 singletons.
The output has D-1 standard physical directions. Active-curve
deletion supplies ONE small full exterior for EVERY filling, with
at most D(r0-1) total curves. It therefore lies in GE_(D-1),C_D(r0).
If there are missing directions, deterministic outer padding gives
a positive-content ambient full zonogon with the same O_D(r0)
bound; original complete boundaries and exact dilation counts stay
unchanged. This padding must be proved in the final whole argument,
not assumed from a count monotonicity slogan.

UR_(D-1), with THIS C_D, bounds the coarse deficits. In each selected
face the fine residual disks have aggregate boundary O_D(r0),
each diameter O_D(r0), and total area O_D(r0²). For a threshold
beta r0², isoperimetry and the aggregate perimeter give total
small-block area O_D(sqrt(beta)r0²). There are O_D(1/beta)
other blocks, each losing at most eta_(D-1),C_D(r0)r0².
LW1 bounds the number of whole interior faces by
O_D((L/r0+1)²). Thus boundary-window loss per area is

    O_D(1/r0+epsilon r0²+sqrt(beta)
                    +eta_(D-1),C_D(r0)/beta)+o_L(1).       (B)

Order: beta small, then r0 large using UR_(D-1), then epsilon
small, then L large. Multiplying an arbitrary number of tiny disks
by an individual r0² deficit bound would be invalid; the small-area
split is essential. No constants here must be uniform as D grows.

## Global steps that still need a complete all-D exposition

The proposed proof of UR_D repeats the ACTUAL construction in the
full G4 candidate with explicit D-dependent constants, not its
conclusion as an already proved theorem. In particular it must:

1. Embed each unbalanced common full exterior in one balanced frame
   by extruding the visible boundary chain, keeping the old ranks
   and filling fixed. If p=max N_i=o(r), a finite alphabet makes
   the deficit o(r²); otherwise normalize by p with p comparable
   to r. Supply one actual M-dilated reference afterward.
2. Extract the limiting rectifiable boundary curve and winding-one
   open set for a positive-deficit sequence. All compact subsets of
   that open set are eventually inside the original disks. Handle
   zero limiting area by the finite alphabet and the actual single
   Jordan boundary tube. Do not assume the limiting curve is Jordan.
3. Cover ALL extended normalized vector profiles on the SAME balanced
   full polygon. A largest fiber costs o(p²). Uniform-limit minor
   closure puts Dh in K_D a.e.; K_D is not declared convex and no
   admissible smoothing or density theorem is needed.
4. Discard an area-delta portion of the strictly positive stratum to
   retain one compact strict class. The singular strata are handled
   by the one-pair reduction above. Choose delta, collar theta and
   desired per-area error before rho; choose strict frames, all local
   tolerances, beta/r0, rational nets and periods before radii. Choose
   finite disjoint outer Vitali windows with all buffers, then take
   the large original-scale threshold. The uniformly bounded aspect
   ratio follows only AFTER rho and the finite charts are fixed.
5. Use US_D on slightly enlarged inner strict windows with their
   WHOLE buffers inside the outer windows. Its inequality holds for
   ANY reference satisfying the common-offset estimate. It compares
   the source restriction count to a count on the exact dilation
   of ONE extracted reference core; inserted interiors may be nonflat.
6. For each boundary window use CW winding inclusion to fix the whole
   target square and buffer. CW2 must cover ENTIRE source tile images
   and retain ONE absolute height anchor. Apply FL1/LW1 and(B), not
   the global mesh code under the false assumption N_i=O(L).
7. Record the original alphabet outside all INNER source windows and
   condition on ALL local codes/anchors JOINTLY. Only THEN select
   ONE actual global representative. Its discarded area is
   O_D(delta+theta)p²+o(p²), and its actual boundary/window tubes
   cost O(p) for the fixed finite window family. Do not maximize
   different local code classes independently.
8. From that same reference, CW3/CW4 turn boundary counts into fine
   patches with exactly the inherited complete boundary and exterior,
   and commute with EVERY integer dilation. Strict and weak patches
   lie inside disjoint source outer windows. Insert their choices
   together into the one M-dilated original disk. Restriction and
   each local forward chart recover the tuple; global chart maps
   need not commute.
9. With the original index j FIXED, the number of patches is finite.
   The product injection for every M gives the finite-sum liminf
   bound. Only then use j->infinity. The target estimate is

       Delta_D(B_j)/p_j²
           <=C_D(delta+theta)+area(Z_D)*zeta+o_j(1).

   All local errors must first be selected per PHYSICAL area, with
   the finite shape-determinant bounds preceding their scales.

The proposed induction has no need for a common constant across
different D, nor for a uniform rate as D->infinity. These nine
global steps are substantive proof obligations; this draft's list
does not discharge them. G4 is itself still under two whole audits.

## Conditional passage back to the official count

If(A) were proved for every fixed D, its application to full balanced
zonogons and remainder padding would give

    ell_D=lim_p log2 B_D(p)/(Dp)².

For each fixed r, use the exact-multiple lower counts from(A), then
pad Mr<=p<(M+1)r with the reviewed remainder injection and let M
grow. Taking r along the limsup sequence proves the balanced limit.
This order uses all sufficiently large multiples at a FIXED r,
not only a favorable subsequence or exact quadratic supermultiplicity.

The already accepted DC1/DC2 conditional-transfer theorem would then
give, for the official marked regular-polygon count,

    ell_D<=L_minus<=L_plus<=ell_D+h2(1/D)+1/D.

Since the last error tends to zero, L_minus=L_plus would follow.
This implication would prove existence, not determine a numerical
value for the common limit or establish a full answer to2017B4.
The all-D local premise and the whole global induction must first
be proved and independently reviewed. No acceptance is recorded here.
