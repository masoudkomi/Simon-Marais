# Joint leading-root and next-digit candidate in rational J=16

2026-10-16 UTC. **Candidate proof - unverified.** Constructor: coordinator.
Two fresh complete independent audits must reconstruct this entire packet,
including the earlier unverified leading argument. It is not accepted
merely because its finite program completed. No full degree or annual
classification, lift of a survivor, or novelty is claimed.

The proposed joint result is L1-L3. L1-L2 and their complete argument
are the unchanged [frozen leading packet](coordinator-J16-coupled-leading-candidate-v1.md),
SHA-256 `d8ad259a3084635d5f3b66e1aaf6fe611c6a118b47dfd16578d0e2958bde3fce`.
They are incorporated as arguments to audit, not as an accepted dependency.
Only the earlier separately reviewed T2, normalization, Newton lemmas
and 88-mask list are accepted inputs.

Proposed L3: the next necessary digit excludes twelve additional masks
after L2's eighteen. Thus 58 of the 88 J=16 masks remain in this
projection. If verified, the combined earlier 772-mask condition becomes
742. The additional twelve are

    82109,82349,82861,87537,88621,89423,
    89551,89791,90035,90499,92511,122559.

The full retained list and complete congruence streams are saved. No
passing branch is asserted to lift. All older proof/data versions remain
unchanged, including the first projection that excluded no masks.

## 1. Restore every omitted derivative label

The leading branch-index construction enumerates every one of L2's
passing projected label/residue/nu combinations, not just its saved first
example. It gives 768: 756 with nu=1 and twelve with nu=2. Each omitted
noncenter position is restored with all labels 0,u,v. Since a full
assignment has one unique active projection, its minimum valuation
and leading residues, this finite cover omits no actual counterexample.
Its exact expansion count is 840396. A complete key is
(center_mask,U_label_mask,V_label_mask,nu,U,V); the label bit sets are
disjoint and supported on noncenter positions. Repeated witness use
and equal leading residues are not discarded.

The branch-index constructor transparently reuses the earlier leading
constructor, with exact changes and provenance recorded. The audits
must independently regenerate its cover and uniqueness, not adopt a
constructor's count or status. This packet does not prune assignments
that omit u or v; retaining them is harmless necessary excess.

## 2. An integral polynomial system for all next digits

For a fixed full derivative assignment, the triangular recursion gives
f over Z[u,v]. Let q=19^nu, u=q*X, v=q*Y, nu=1 or 2 as in L2.
Let s=u+v,t=u*v. Divide f/Z^2, as a polynomial in Z, by the monic
quadratic Z^2-sZ+t. Its remainder is R1*Z+R0. Monic division uses
no u-v denominator, so coincident residues or coincident formal parameters
cause no exception. An actual polynomial with the distinct roots u,v
must have R0=R1=0. Let Ptilde=f(1)/19, as before.

The normalized vector, with beta18=binom(20,18)/19=10, is

    E1=Ptilde/q,
    E2=R0/(19*q*beta18),
    E3=R1/(19*q).                                  (N)

These are polynomials over Z_19 in X,Y for every branch satisfying
L2's constant divisibility prerequisites. Indeed each a_j-a_j^0
belongs to (u,v), Ptilde's constant q0 is divisible by q, and a17^0,
a18^0 are divisible by q. The low constants of R1 and R0 are
c3=19*beta17*a17 and c2=19*beta18*a18. All subsequent middle-coefficient
terms in those remainders have an extra power of u or v and an explicit
19. The exceptional coefficients c19=-20,c20=1 are multiplied by
homogeneous parameter terms of degrees at least16 in R1 and17 in R0;
they also have sufficient valuation. Division by beta18 is legal in
Z_19 because 19 does not divide 10. This is not division by a possibly
zero parameter or by its residue.

The reduction of (N) is exactly L2's three affine equations, after
the harmless unit factor in E2. Its Jacobian modulo19 is constant,
with rows

    (sum beta_j*A_j, sum beta_j*B_j),
    (A18,B18),
    (beta17*A17+C4, beta17*B17+C4),
    C4=beta16*a16^0 mod19.                          (J)

Every higher parameter degree in (N) has an additional factor19, so
this derivative does not depend on the leading point. The A_j,B_j
are the same exact linear coefficients modulo19 derived in L2;
inactive labels affect later constants but not these rows.

For a leading solution (U,V), write X=U+19*U2,Y=V+19*V2. Taylor
expansion of these integral polynomials gives

    E(X,Y)=E(U,V)+19*J*(U2,V2)^T mod19^2.

Hence the next digits exist only if a three-by-two affine system over
F19 is consistent. Its constant vector is E(U,V)/19 modulo19. This
argument proves necessity without requiring a unique lift, nonsingular
Jacobian, or distinct leading roots. Rank-one systems may have nineteen
next points and rank-two systems zero or one; the code tests consistency,
not merely a nonzero determinant.

## 3. Exact computation of the next constant vector

For each restored full assignment evaluate its coefficients at
u0=q*U,v0=q*V, modulo19^(nu+2). At a noncenter position w=u0 or v0,
only -j*a_(j-1)*w and, when nu=1,
-binom(j,2)*a_(j-2)*w^2 can survive this modulus. Every power >=3
vanishes. For nu=2 even the quadratic term vanishes. Center positions
keep the complete sum of previous coefficients. This is a truncated
exact scalar recursion, not a floating-point approximation.

The leading conditions ensure Ptilde(u0,v0) divisible by19^(nu+1),
a18(u0,v0) by19^(nu+1), and a17(u0,v0) by19^nu. The program asserts
these divisibilities for every case rather than performing silent
integer-floor divisions when a prerequisite fails.

The first constant is Ptilde(u0,v0)/19^(nu+1) modulo19. For nu=1 the
second constant is

    a18(u0,v0)/19^2 - (C4/beta18)*U*V mod19,

while for nu=2 it is a18(u0,v0)/19^3 modulo19. These are E2/19 at
the required precision: t*c4 first contributes to that digit at nu=1;
at nu=2 it is still divisible by another19. The same distinction must
be preserved in an independent reconstruction.

For the third constant, if B=(Z-1)g=sum b_i Z^i, the exact identities are

    c3+c4*s=b1*(t-s^2)+b2*t*s,
    c5=b1-b2*s+b3*t.

The b_i needed here have valuation at least1. For nu=1, E3(U,V)
modulo19^2 is

    beta17*a17(u0,v0)/19 + beta16*a16(u0,v0)*(U+V)
      -19*beta15*a15(u0,v0)*(U*V-(U+V)^2).

For nu=2 it is simply

    beta17*a17(u0,v0)/19^2 + beta16*a16(u0,v0)*(U+V)
      mod19^2.

The first omitted correction has a factor19^nu. Divide the appropriate
displayed residual by19 and reduce modulo19 to obtain the third
constant. The residual is asserted divisible by19. Thus all three
constants used by the program agree with the necessary Taylor system
of (N), with no inversion of 19 in the residue field.

## 4. Complete finite evidence and limitations

`computations/coordinator-J16-second-digit-v1.py` tests every 840396
full-label/leading-residue/nu key. For each it computes the exact scalar
coefficients and constants above, then uses row reduction over F19
to decide the affine system. There are125346 consistent branches:
112222 with rank2 and13124 with rank1. They supply no rational solutions.
The other branches fail this necessary next digit. The 58 retained
mask list is obtained by taking the union over every branch, retaining
a mask whenever any branch is consistent. Including L2's eighteen,
30 masks have no surviving branch in this joint projection.

The constructor stores every row as

    [mask,U_label_mask,V_label_mask,nu,U,V,c1,c2,c3,rank,consistent],

in15 deterministic gzip chunks (14of60000rows, one396rows), 3223838
compressed bytes. Uncompressed row-stream SHA-256:
`b0ab2fd44f64015b0ae1caa954c3dad76be44c02833cec62d79c2df6c1f3dacb`.
The stream binding each key to its exact scalar coefficient vector has
SHA-256
`dfe2ca43528f5e55c68a642f61838343b0a09bc6690afe153643c04ff574e49f`.
Rows and full coefficients are independently regenerable from the frozen
assignments; reviewers must compare the complete streams and coverage.

The8192-case benchmark is preserved with explicit incomplete status and
supplies no mask exclusion. ChildPID46042 finished0.405seconds under30s.
The full childPID46081 finished29.439seconds under180s, exit0, reaped,
with8192-case checkpoints, no timeout or native CAS. Exact source,
parameters, commands and output hashes are in the job records.

The earlier leading computation and next-digit computation are both
construction, with no independent-review credit. Joint acceptance
requires two fresh full reconstructions of L1-L3, the root identities,
uniform normalization, exact modulus accounting, all label/valuation
coverage and every finite record. Higher Hensel digits are a separate
research direction, not a conclusion of this packet.
