# Frobenius differential route beyond the special F8 orbits

2026-10-18 UTC, root. **Research lead - unverified**, not an accepted
extension or complete constructor packet. No mathematical executable,
CAS, field scan, numerical certificate or source-author program was used.
The following identities were derived by hand after FS acceptance.

Let ell=2^s-1, q=2^a, n=ell*q+1, W=X+Y+Z and
f=X^n+Y^n+Z^n+W^n, with R the three prescribed pair-sum lines.
Consider the characteristic-two derivation

    delta_q=X^q partial_X+Y^q partial_Y+Z^q partial_Z.

Since f_X=(X^ell+W^ell)^q and similarly, its derivative is

 delta_q f=[X^(ell+1)+Y^(ell+1)+Z^(ell+1)+W^(ell+1)]^q=0,

because ell+1 is a power of2. For each F2 pair-sum line L,
delta_q L=L^q. Thus

    delta_q R=R*S, S=sum_(three L) L^(q-1),
    delta_q(phi)=S*phi.

For any absolute irreducible factor h appearing ONCE in phi,
the product rule modulo h gives h|delta_q h. This uses squarefreeness
of the relevant actual polynomial; it cannot be applied blindly to a
repeated factor. On a smooth component point outside other factors,
the gradient ratios also agree with

    (X^ell+W^ell)^q:(Y^ell+W^ell)^q:(Z^ell+W^ell)^q.

Consequently the tangent contains the q-power Frobenius image of the
point. These are explicit polynomial identities, not a theorem that
all components descend to F_q or that every such curve is irreducible.
Generic nonconstant gradient maps and their inseparable degrees must
be checked before applying any Gauss-map theorem. In particular
the boundary case in which the displayed qth-power map is the FULL
q of the coefficient field is delicate.

The general cofactor note supplies, under its explicit ordinary-singularity
and line-contact assumptions, an integerD with qD>=e. Rewriting its
exact Bezout identity and contact sum gives

    e(e-1)-sum_A m_A(H)(m_A(H)-1)=qD.

This is consistent with a polar/class interpretation for a REDUCED
ordinary curve, but applying a Gauss-map degree formula, singular
normalization formula or rational-point estimate requires a complete
checked source/interface. No such theorem is imported as a new premise
here. Absolute components need not be individually F_q-defined.

Rejected shortcut: a low degree bound on a foliation does NOT itself
bound every invariant curve degree. Characteristic-zero foliation
results from broad searches have the wrong characteristic and often
extra singularity hypotheses. Likewise an inseparable Gauss map or
Frobenius-nonclassicality does not by itself imply irreducibility.

Fresh discovery lead: [Arakelian–Speziali, Curves on Frobenius nonclassical
loci of hypersurfaces](https://arxiv.org/abs/2512.08874), with primary
[published page](https://link.springer.com/article/10.1007/s00209-026-04128-y).
The returned Theorem5.3 explicitly requires its condition(A) and
p^r<q. A displayed qth-power gradient does not satisfy that strict
inequality merely by renaming its symbols. The abstract/search-returned
proof fragment is NOT an ENTIRE operative-proof read; this is a reading
lead only, with no theorem application or priority claim. Older
Hefez–Voloch/Gauss-map references likewise need original proof checks.

The new route might help replace special orbit calculations by a
geometric cofactor bound. It presently supplies NO new actual exponent
exclusion, new large-component bound, rational-point theorem, useful
annual reduction or solution. Preserve FS's accepted exact scope.
