# Next-digit coupling lead and bounded branch count

2026-10-16 UTC. **Unverified research lead; no second-digit job yet.**
The full first-digit projection is the separate frozen coupled-leading
candidate. Its constructor found 18 excluded J=16 masks, not yet reviewed.
No numerical change below is accepted as a theorem.

The new branch-index script is a transparently recorded copy of that
constructor which also saves every passing (mask, active labels,nu,U,V).
It finds 768 such leading branches: 756 at nu=1 and 12 at nu=2.
Each omitted noncenter position may still have label 0,u or v. Restoring
these inactive labels gives **840396 full label/residue/minimum-valuation
branches**, substantially smaller than blindly eliminating all bivariate
families. They are a finite projected cover, not rational solutions.

Child PID44469 completed in2.568seconds under30seconds, exit0, reaped.
Exact copying replacements, old/new source hashes, parameters, stdout,
all768 branches and the expansion counts are saved in same-prefix
`computations/coordinator-J16-leading-branch-index-v1*` files. This is
constructor reuse, not independent review.

Here is a proposed further necessary digit test, to derive and audit
before using it. Write beta_j=binom(20,j)/19 and use the exact factor
identities of the coupled-leading candidate. Put s=u+v,t=u*v. They give

    c3+c4*s = b1*(t-s^2)+b2*t*s,
    c5 = b1-b2*s+b3*t.

For nu=1, write u=19*(U+19*U2),v=19*(V+19*V2). Reduction one digit
further than the earlier root-sum identity suggests

    beta17*a17/19 + beta16*a16*(Uactual+Vactual)
       =19*beta15*a15*(U*V-(U+V)^2) mod19^2.

Here Uactual=U+19*U2 and similarly for V. The c5/19 residue equals
b1/19, while b2*t*s has valuation at least4 and vanishes after dividing
c3 by19^2 and reducing modulo19^2. The a_j on the left must be evaluated
at the actual u,v, with enough digits; their derivatives modulo19 are
the same A_j,B_j as before.

Evaluate a_j at base u0=19U,v0=19V modulo19^3 for each full label
assignment. The leading conditions ensure a17 is divisible by19,
a18 by19^2 and Ptilde=f(1)/19 by19^2. Three proposed next equations in
the unknown digits U2,V2 have coefficient rows

    (sum beta_j*A_j, sum beta_j*B_j),
    (A18,B18),
    (beta17*A17+C4, beta17*B17+C4),
    C4=beta16*a16^0 mod19.

Their constants are respectively Ptilde(u0,v0)/19^2;
a18(u0,v0)/19^2-(C4/beta18)*U*V; and the base root-sum residual
minus the displayed correction, divided by19. The second row is the
exact leading root-product equation c2=b0*u*v, since
c2/19^3=(c4/19)*U*V modulo19. The third row's divided residual uses
the beta17*a17/19 expression, not a17/19^2. Check every division and
modulus carefully before implementation. Consistency of a 3-by-2 affine
system over F19 can be decided exactly without trying361digit pairs.

For nu=2, evaluate at u0=19^2 U,v0=19^2 V modulo19^4. The next unknown
digits enter at19^3. A weaker but necessary next test has the same three
rows: the center-root equation modulo19^4; a18=0 modulo19^4 (the actual
condition is stronger at its leading product digit); and the root-sum
identity modulo19^2 after division by19^(1+nu). The correction involving
b1 has an extra factor19^nu and vanishes at that last modulus. Do not
apply the nu=1 product constant to nu=2.

Scalar truncated recursion is enough for these evaluations. At a
noncenter position with w=19^nu U or19^nu V, modulo19^(nu+2) only
-j*a_(j-1)*w and, for nu=1, -binom(j,2)*a_(j-2)*w^2 can survive.
All center positions retain their full linear sum of previous a_k.
This avoids constructing full bivariate polynomials and uses exact
integers. New digits enter linearly because second-order changes in
19^(nu+1) exceed the modulus.

Next: derive all formulas independently, benchmark a bounded initial
8192 branches with explicit incomplete status, then run the fixed
840396 cover only if the measured runtime is appropriate. Use an
external subprocess timeout, incremental counts and targeted child
cleanup. Save every eliminated/surviving-mask tally. Even a complete
finite result is a candidate until two independent audits reconstruct
both the previous leading reduction and this additional digit test.
