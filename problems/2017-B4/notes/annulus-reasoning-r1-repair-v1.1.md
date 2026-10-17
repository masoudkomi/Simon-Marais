# Author repair ledger for annulus A1--A5, version 1.1

2026-10-17 UTC. **Candidate proof - unverified.** This ledger and the
complete v1.1 candidate preserve the frozen v1 and both complete initial
audits. They propose repairs for independent targeted re-audit; the author
does not close the reviewers' ledgers or promote any result.

The first complete initial report and issues were read after the 2024
divisor review1 packet had been frozen. The second complete initial report,
issues and source checks were read only after the coordinator confirmed
their initial freeze. No report was read while its author was still doing
the blind initial audit.

## AR1-01: explicit available rank box, including absent colors

I accept this as a substantive omission in the literal standalone v1 A2
statement. A1 explicitly had the domain 0<=h_i<=N_i. A2 only asked that
the displayed sets I(h) be ideals, while allowing an inner color not to
occur. The literal set formula forgets a negative h_i. Its ideality cannot
recover the missing coordinate. Describing an empty active-rank interval
does not itself repair this defect.

The first reviewer supplied an exact diagnostic, retained in the complete
v1.1 candidate. For the full Z_10 outer frame, let the inner words be13
and31, with start a=(7,-2,7,4) and end b=(8,-2,8,4). The physical
tile has vertices (16,24),(17,24),(17,26),(18,26), strictly inside the
outer zonogon. All literal sets I(h) are ideals of the four separate
rank chains, but a color-2 height -2 cannot extend to the outer rank
range0,...,10. The entry seam constructed from the truncated ideal
would have height (7,0,7,4), not a. Thus the proof would insert a
different placed and lifted core.

The complete v1.1 statement adds the explicit hypothesis

    0<=a_i<=b_i<=N_i, every color i.                      (R)

Empty inner colors m_i=0 remain allowed; their a_i=b_i still must
belong to the available interval. Along each positive boundary path,
a<=h<=b coordinatewise, so all tested heights are in A1's domain.
The proof now explicitly observes that I(a),I(b) have the actual
coordinate counts a,b. Therefore the restriction of p0 to I(a)
reaches Va, and the complement after I(b) starts after Vb. All
remaining entry/exit, shelling, matching and restriction arguments are
the original ones.

For an outer starting lift z0 the complete statement also specifies

    z0_i<=a_i<=b_i<=z0_i+N_i,
    relative ideal test I(h-z0).

Rebase physical points by Vz0 and heights by z0. This is one fixed
normalization, not a freedom to change the prescribed inner offset.

A3 is adjusted to avoid circularly assuming the new condition. Its
statement retains the geometry, words and assigned lifts of A2 but
does not yet assume rank range or ideality. Winding one in each pair
first puts h_ij into [0,N_i] times [0,N_j]. All six projections
therefore put every boundary height, including a and b, in the rank
box. Only then is A1 applied to obtain ideality. Thus A3 derives the
new A2 hypotheses, including absent colors, rather than adding an
unchecked requirement to its conclusion.

For the translated version, x_prime=x-Vz0 and h_prime=h-z0 give

    c_prime=c-(I-JV)z0 in ker V,
    h_prime-J*x_prime-c_prime = h-J*x-c.

The error bounds and physical distance do not change, so the relative
range follows from the identical winding proof. These exact equations
are now in the full candidate.

Author disposition: **repair proposed; both targeted re-audits and
coordinator resolution pending**. This is not treated as a cosmetic
change or ignored because the second reviewer reconstructed the inherited
range. No counterexample to A3 or to the range-corrected A2 is claimed.

## ANN2-N1: vertex buffer supplies strict nesting in this exact model

The second audit found no counterexample but requested the missing short
geometric explanation. The complete v1.1 A3 now includes it.

Every boundary edge has integral endpoints and horizontal displacement
one. On each [k,k+1] that contains an inner edge, both outer paths and
that inner edge are affine graphs. Containment and positive vertex
distance put both endpoint vertices strictly between the outer paths.
Both affine vertical differences are positive on the whole interval.
Hence there is no nonvertex contact, and the closed inner lens is
strictly inside the Jordan outer lens. Compactness then gives positive
separation.

This does not replace the actual numerical vertex bound t by an equal
bound for every interior edge point. The winding proof only tests inner
boundary vertices and uses exactly their stated bound. Thus no extra
quantitative inference was introduced. This clarification depends on the
integer unit-horizontal geometry already fixed in Section0; it is not
asserted for arbitrary edge geometries.

Author disposition: **explicit clarification included; targeted checks
pending**.

## ANN2-N2: retain the full conditional transfer hypotheses

The summary following A5 is rewritten as a conditional statement. It now
lists the fixed strict rational slope J, one common affine offset, one
fixed phase and a compatible receiving integer frame; actual comparable
two-path Jordan inner lenses with their assigned lifts; physical
containment; and A3's common-affine estimates and quantitative buffer.
When A2 is used directly, its rank-box and ideal tests are stated as
explicit alternatives to the A3 sufficient test.

The varying-boundary fiber estimate retains both O(L) word lengths and
O(L) relative integer offsets. A thin surrounding canonical frame,
small relative area overhead, independently adjustable corner offsets
and uniform constants at zero minors are expressly outside the summary.
The same cut-window, stratum and global original-boundary recovery gaps
remain after the repair. A5 is still the exact receiving-frame C_L
limit, not hypothesis(H).

Author disposition: **scope clarification included; targeted checks
pending**.

## Change and dependency boundary

A1's mathematical criterion, the range-corrected A2 construction, the
six-pair winding estimate, A4's fixed rational digital words and bounded
corner trimming, and A5's actual block-gluing inequality are retained.
The new copy adds no arbitrary-window, stratum or full-zonogon theorem.
The finite counterexample is attributed to reviewer1. All new reasoning
in this repair is exact analytic word/geometry reasoning; no enumeration,
CAS, numerical test or newly executed mathematical certificate was used.

The original external Levi paper remains a lead only. Neither the
coordinator's separately developed directed-geodesic results nor its
cutting packet is used as a repair premise. The earlier false unqualified
prefix-height conversion is not used, and constants are never claimed
uniform as a row minor tends to zero. Published sources keep their
original attribution and no priority claim is made.

Both complete initial audit reports, their issue ledgers and associated
source/freeze records are hash-preserved. The v1.1 candidate is a full
replacement reading copy, not a patch that requires a reader to silently
repair v1. A separate textual diff is retained for targeted review.
