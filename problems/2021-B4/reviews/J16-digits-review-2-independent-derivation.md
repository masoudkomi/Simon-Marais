# R2 independent reconstruction, frozen before constructor code/data

2026-10-16 UTC. Review scope: the rational J=16 exclusion L1--L4 only.
Requested gpt-6.1-sol / max; no independently verified effective-setting
readback is available. No J16 peer report, peer code or peer result has
been read. Designated candidate mathematical notes and the accepted
normalization/Newton/T1--T3 registers have been read. No constructor code,
manifest or finite data has yet been opened. The accompanying independent
checker is to be hashed with this derivation before that happens.

## Reconstruction from ordinary Hasse coefficients

Use the accepted normalization and T2. The rational root set is exactly
{0,1,u,v}; 0 is double, 1,u,v are simple, u,v are nonzero distinct
rational numbers of positive integral 19-valuations. Other roots are not
assumed rational. Write c_(20-j)=binom(20,j)a_j. In the ordinary Hasse
equation H_(20-j)(f)(w)=0 the coefficient of a_h is
binom(20-h,20-j)binom(20,h)=binom(20,j)binom(j,h).
Cancellation over Q gives the division-free exact recurrence
a_j=-sum_(h<j)binom(j,h)a_h w^(j-h), a0=1,a1=-1, 2<=j<=18.
Thus every full assignment of derivative witnesses from 0,1,u,v forces
an integer polynomial family in u,v. Conversely these families are only
necessary covers. a19=a20=0 accounts for f(0)=f'(0)=0; the derivative
order19 has witness1. All masks select1 whenever it actually works.
This canonical choice is why a missing bit can be treated as a failed
center equation when proving L1; formal families may retain excess cases.

Put B=(Z-1)g. Its low coefficients b0,b1,b2 have valuation>=1, with
v(b0)=1. Direct multiplication by Z²(Z-u)(Z-v) gives
c2=b0uv, c3=-b0(u+v)+b1uv,
c4=b0-b1(u+v)+b2uv. In particular v(c4)=1 and for
nu=min(v(u),v(v))>=1, v(a17)>=nu, v(a18)>=2nu. If the valuations differ,
the lower Newton edges have widths1 and lower exponents2 and3; the
accepted width-one lemma applies below prime19 and excludes H2,H3 at
both small roots. Neither can vanish at0 (c2,c3 nonzero), so both must
vanish at1. The long-edge roots of valuation1/15 supply no rational
witness. This handles the possible ramified algebraic cluster without
assigning integer valuations to its roots.

If just one of H2,H3 has center1, the valuations are equal. Writing
u=qU,v=qV, q=19^nu, the integral polynomial
f(qT)/(c4 q^4) reduces to T²(T-Ubar)(T-Vbar).
For H3 at 0,Ubar,Vbar its values are -(Ubar+Vbar),
3Ubar-Vbar,3Vbar-Ubar. H2 cannot use0; at Ubar,Vbar its values are
Ubar(3Ubar-2Vbar),Vbar(3Vbar-2Ubar). These give exactly the two
sole-center ratio filters. Equal reduced roots are allowed before these
filters; their exclusion in a sole-center case follows from these actual
nonzero-unit identities. When both centers work, a zero residue on one
variable and equal nonzero residues are both retained.

For the root-sum condition reduce c3/19^(1+nu): its value is
-(c4/19)(Ubar+Vbar). The b1uv term has extra valuation>=nu;
c4/19=b0/19 mod19. This supplies the third affine leading equation.

## Finite leading cover

Compute the exact constant coefficients a_j^0 at u=v=0. They depend only
on the center mask. Mod19, at a center bit a_j is minus the binomial
sum of previous a_h; elsewhere it is0. The divided center-root equation
is P=-1+sum beta_j a_j=0, beta_j=binom(20,j)/19, 2<=j<=18.
All 2^17 masks can therefore be independently generated. The accepted
J18/J17 exclusion and J16/J15 disjunctions leave the accepted 772 masks;
only the J16 subset is used below.

Write A_j,B_j for the linear coefficients of the family modulo19.
At center bits they obey the same binomial sum. At a label u, A_j is
-j*a_(j-1)^0 and B_j=0; at v the roles reverse; at0 both vanish.
Only noncenter positions with a_(j-1)^0 nonzero mod19 are active.
Projection onto these positions preserves all A,B. Later all inactive
positions must be independently restored with labels0,u,v, once each.

P(0,0)=q0 is an exact integer. Since every nonconstant monomial after
substituting u=qU,v=qV is divisible by q, an actual solution requires
q|q0. q0 must be checked nonzero for every mask; its integer valuation
then bounds nu without any rational-height assumption. The low
coefficients also require q|a17^0,a18^0. Mod19^(nu+1), only the constant
and linear terms survive. The three necessary leading rows are

q0/q + sum beta_j(A_j U+B_j V)=0,
a18^0/q + A18 U+B18 V=0,
beta17*a17^0/q +(beta17 A17+C4)U+(beta17 B17+C4)V=0,
C4=beta16*a16^0 mod19.

The second row is a consequence of v(a18)>=2nu, since 2nu>=nu+1.
Test every (U,V) in F19² except(0,0), with the sole-center filters above.
All labels and every positive integer nu allowed by v(q0) are covered.
There is no division by u-v and no all-roots-rational assumption.

## Uniform exact equations and independent evaluator

For every restored full family put F=f/Z² and divide by the MONIC
quadratic Q=Z²-(u+v)Z+uv. Let remainder=R0+R1 Z.
The remainder of Z^e has homogeneous degrees e in its constant part
and e-1 in its Z part. At e=0 it is1, at e=1 it isZ.
For e>=2 both homogeneous polynomials have integer coefficients.
Consequently R0 has initial c2 and R1 has initial c3+c4(u+v).
All middle c's carry19. After u=qU,v=qV their subsequent terms in R0
carry at least q² and in R1 at least q. The exceptional coefficients
c19=-20,c20=1 occur at e=17,18, so their terms contain q^17 and q^16
or more. Hence

E=(P/q, R0/(19q*10), R1/(19q))

is in Z_(19)[U,V] provided q|q0,a17^0,a18^0. 10 is a 19-unit.
Modulo19 this is exactly the three displayed affine rows. Its matrix M
is constant modulo19; terms of parameter degree>=2 in E have an extra19.
Thus every next-digit fiber at precision k>=1 is
M(dU,dV)^t=-E(U,V)/19^k mod19. Taylor's remainder is divisible by
19^(k+1) since 2k>=k+1; denominators prime to19 do not affect this.

The checker evaluates coefficients modulo q*19^r for desired E precision
19^r, using the full center recurrence and omitting noncenter powers
w^e only when nu*e>=nu+r. It constructs the actual coefficients c_e,
including -20,1, modulo D=19q19^r. Its direct quadratic Horner step is
(R0,R1) <- (c_e-u*v*R1, R0+(u+v)*R1) mod D, traversing F from
degree18 to0. Dividing the resulting residues by19q, and multiplying
the constant part by10^-1 mod19^r, returns E exactly modulo19^r.
P is separately formed from the a_j modulo q19^r. No scaled h_e
recursion and no constructor helper is needed.

The finite-field solver chooses a nonzero two-row minor when available,
solves its two equations and verifies the third. For rank1 it chooses a
nonzero row and gives its whole affine line after testing consistency;
for rank0 it gives all361 or none. For every encountered matrix it will
also enumerate all361 digit pairs and compare complete nonempty fibers,
so singular systems cannot silently lose children. Full exact integer
Horner recurrence and direct monic remainders will additionally be
reconstructed for every remaining state at input precisions4 and5.

## Logical conclusion and adversarial boundaries

T1 requires all four roots. Since0 and1 already witness derivative
orders1 and19, either small-root label omitted from all j=2..18 makes
that family impossible; this pruning is allowed only after the full
unpruned second-digit stream has been checked. A true rational pair
gives 19-adic integers U,V and therefore a path through every finite
precision. Distinct rational roots may agree at all tested finite digits;
no such finite equality is pruned. Once a layer is empty there is no
actual rational solution. Constant rank2 at precision4 gives at most one
child per node at every later level and a structural bound of90 if that
count is independently reproduced. The unrestricted statement follows
only from this coverage plus complete finite incompatible congruences,
not from a finite height search or a conjectured lift failure.

This initial reconstruction identifies no substantive gap, conditional on
independent exact exhaustion. It is not an acceptance report. Candidate
code/data are still unopened. Later reports will record all discrepancies
and limits and will remain blind to peer conclusions until frozen.
