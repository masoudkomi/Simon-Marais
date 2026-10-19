# Exploratory global polar constraint after F15

19October2026UTC. **Exploratory / unverified throughout: no new assertion
below is accepted or independently reviewed.** One bounded HAND pass by A,
not a new proof packet or classification. Root supplied a generic target,
no mathematical inference. Requested inherited gpt-6.1-sol/max; independent
effective backend readback unavailable. Only official2024 B4(b). No new
sources, mathematical execution, old helper, Git or other file changes.

## Exact retained setting

Use F15's actual polynomial setting over the algebraic closure K of F2:

    q=2^i, i>=2; ell>=3 odd, ell | q-1; n=ell*q+1;
    W=X+Y+Z, R=(X+Y)(Y+Z)(Z+X),
    H=phi_n=(X^n+Y^n+Z^n+W^n)/R, N=ell*q-2.

The quotient/reducedness and exact diagonal local forms are the separately
accepted inputs, not newly proved here. Let U be an ACTUAL nonconstant
homogeneous divisor of H over F_q, with complement V. H is reduced, so
U,V are coprime. No coordinate symmetry of U is assumed. For an ordinary
F2 factor, keep that smaller coefficient field; an absolute factor alone
does not establish ordinary reducibility or the official product.

The motivating failed-budget sector is ell21,q=2^(6t),t>=1. F15 proves
three square restrictions, paired noncentral diagonal tangents and center
orbit allocations, while its numerical gap remains negative. None is a
sufficiency criterion for a divisor. This pass reread the complete own
F15 candidate; no further source claim or old program was imported.

## Proposed next constraint: cofactor-free global polar equations

Put

    A_X=X^ell+W^ell, A_Y=Y^ell+W^ell, A_Z=Z^ell+W^ell.

Differentiate the ORIGINAL identity RH=X^n+Y^n+Z^n+W^n in characteristic2.
Since n is odd and q is a power of2, its X derivative is A_X^q. Also
R_X=(Y+Z)^2. Thus the exact global identities are

    R H_X+(Y+Z)^2 H=A_X^q,

and the two coordinate permutations. Reduce them modulo ACTUAL U and
use H=UV:

    A_X^q = R V U_X modU,
    A_Y^q = R V U_Y modU,
    A_Z^q = R V U_Z modU.                          (P)

Eliminating the SAME cofactor RV gives three concrete necessary polynomial
divisibilities, for example

    U | A_Y^q U_X+A_X^q U_Y,                       (G)

with XZ and YZ counterparts. They involve U and known polynomials only,
not independently assigned branches at separate singularities. Each
nonzero quotient in(G) is homogeneous of degree ell*q-1. This is a
specific global differential constraint to impose on any proposed factor
before attempting actual division; it neither constructs U nor makes
the unknown-coefficient problem linear.

There is a sharper geometric reading, still proposed/unverified here.
For an absolute irreducible component G of H, write H=G B and work in
K(G). R is nonzero there: none of the three diagonal lines divides H.
B is nonzero because H is reduced. Not all G_X,G_Y,G_Z vanish: otherwise
over the perfect field K, G would be a square, contradicting irreducibility.
Hence(P) gives the exact generic Gauss coordinates

    (G_X:G_Y:G_Z)=(A_X^q:A_Y^q:A_Z^q) in K(G).

Where G_Y is nonzero, for example,

    G_X/G_Y=(A_X/A_Y)^q.                            (F)

If that denominator vanishes identically, use a nonzero coordinate instead;
(P) guarantees the matching A coordinate is nonzero. Thus the ACTUAL
generic normal ratios are q-th powers of explicit rational functions on
the SAME component. This is stronger data than Frobenius pairing at the
three diagonal fibers. A useful next target is to reconcile(F), its
possible constant-map degeneration, and the assigned local branch divisor
on that one curve. I have not proved an incompatible degree/genus bound.
No general characteristic2 Gauss-map theorem is silently invoked.

## A precise failed sufficiency inference

Even the COMPLETE three diagonal restrictions and their leading local
cones do not force global divisibility. In the ell21 sector let

    T=X^(N-3(q+1)), U_*=H+R^(q+1) T.

The exponent N-3(q+1)=18q-5 is nonnegative. U_* is a nonzero homogeneous
F2 polynomial of degree N. Its restrictions to ALL three diagonals are
exactly those of H, since R vanishes on them. They remain nonzero and
have the same infinity values and root orders. At a noncentral diagonal
point P_b, R has order1, so the perturbation has order at least q+1,
strictly beyond H's orderq. At C=(1:1:1), R has order3, so its order is
at least3(q+1), strictly beyond H's orderq-2. Consequently U_* has the
same leading local cones and maximal local tangent/orbit allocations as
H at every F15 point. No finite-value substitution is used in this claim.

Nevertheless U_* does NOT divide H. Their equal degree would force
U_*=cH for a nonzero scalar c. Restriction to any diagonal, where H is
nonzero as a binary polynomial, gives c=1. Then R^(q+1)T=0, impossible
in a polynomial integral domain. This example has full degree N; it
does not refute a yet-unproved compatibility theorem restricted to proper
smaller degrees. It does prove that those boundary/initial-form data alone
are insufficient, even when retained exactly rather than just in parity.

The bad inference would be: choose allowed branch orbits, interpolate
their diagonal data, and declare the resulting polynomial a factor.
The perturbation preserves all that data while losing divisibility.
(G)/(F) provide a concrete next global condition absent from that recipe;
I do not assert without proof that U_* fails every displayed polar equation,
or that satisfying those equations would suffice for a factor either.

## Remaining step and checkpoint limits

The unresolved implication is to turn the explicit q-power normal ratios
and actual local branch assignments into a quantitative obstruction for
a proper G, or recover an actual factor. Constancy/ramification of the
Gauss map, points at infinity and off-diagonal incidences must be handled;
local pairings alone cannot supply that argument. No stronger component
degree bound, ell21 classification, converse to G<=0, annual result or
novelty claim is made. F15's earlier unsuccessful Gauss-map idea remains
unsolved, but(P)--(F) specify the exact global equation it would need.

Fresh authoritative start04:13:31UTC:87%TOTAL,10080-minute window,
reset1792874445,ordinaryallowed,legacy/by-limit agree. Same authorized
window only;90%TOTAL includes integration reserve. Final readback and
fresh end telemetry are reported separately. This short exploratory note
is the sole new file; no frozen bytes were changed.
