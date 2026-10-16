# Coupled leading-root restrictions in the rational J=16 case

2026-10-16 UTC. **Candidate proof - unverified.** Constructor: coordinator.
Two independent adversarial audits are required for every new assertion
and the finite mask consequence. This is a partial restriction only;
no full degree or annual problem is solved and no novelty is claimed.

## Scope and accepted dependencies

Use the separately reviewed rational-witness normalization and T2 of
the [three-witness packet](coordinator-three-rational-witnesses-reviewed-v1.1.md).
In a hypothetical nontrivial degree-20 rational-witness counterexample
with J=16, 0 has multiplicity two, the complete rational root set is
{0,1,u,v}, both small roots are simple with positive integral valuations,
and

    f(X)=X^2*(X-1)*(X-u)*(X-v)*g(X)

where g is monic, rational, degree 15 and Eisenstein at 19. Let H_k be
the ordinary Hasse derivative of order k, and a_j the normalized
coefficients c_(20-j)=binom(20,j)*a_j. The previously reviewed
width-one Newton-edge lemma and the 88 necessary J=16 center masks
are explicit inputs. No complex-witness extension is an input here.

Proposed L1: if v19(u)!=v19(v), both H_2(1) and H_3(1) vanish.
If exactly one of these center equations is available, the valuations
are equal, say nu, and for the nonzero residues U=u/19^nu,V=v/19^nu:

- H_2(1)=0 but H_3(1)!=0 requires one of U+V,3U-V,3V-U to vanish.
- H_3(1)=0 but H_2(1)!=0 requires 3U-2V=0 or 3V-2U=0.

Proposed L2: combine these conditions with the root-sum identity below
and a necessary first-order lift. The complete finite projection rules
out 18 of the 88 J=16 masks, leaving 70. Combined with earlier unrelated
J classes, this would reduce 772 to 754 necessary masks. Those numbers
remain unverified until both new audits; survivors are not rational lifts.

## 1. Exact factor consequences and L1

Write B=(X-1)g=sum b_i X^i. Eisenstein gives v19(b_0)=1 and
v19(b_1),v19(b_2)>=1 (infinity is allowed). For the low coefficients,

    c_2=b_0*u*v,
    c_3=-b_0*(u+v)+b_1*u*v,
    c_4=b_0-b_1*(u+v)+b_2*u*v.

Thus v19(c_4)=1, v19(c_2)=1+v19(u)+v19(v), and
v19(c_3)>=1+min(v19(u),v19(v)). If nu=min(v19(u),v19(v)), then
v19(a_17)>=nu and v19(a_18)>=2nu. Put U=u/19^nu,V=v/19^nu,
now allowing one of U_bar,V_bar to be zero if the valuations differ.
Reduction of the exact identities gives

    c_3/19^(1+nu) = -(c_4/19)*(U+V) mod19.          (R)

Indeed b_0/19=c_4/19 modulo19, while the b_1*u*v term after division
has valuation at least nu>=1. This is a root identity, independent of
which selected higher derivatives use u or v.

If the two valuations differ, suppose v19(u)<v19(v). The small-root
Newton edges have width one and endpoints at exponents (3,4) for u and
(2,3) for v; the other 16 roots have valuations 0 or 1/15. The accepted
width-one lemma makes H_k(u) nonzero for 1<=k<=4, and H_k(v) nonzero
for 1<=k<=3, since the relevant endpoint exponents are below 19.
Also H_2(0)=c_2!=0 and H_3(0)=c_3!=0: in the latter identity the term
-b_0*u has strictly smallest valuation. These are all rational roots
apart from the center. Therefore both H_2 and H_3 must use 1, proving
the first assertion of L1. The same argument applies after swapping u,v.

If exactly one center equation is available, their valuations must
therefore be equal to nu. Both U_bar and V_bar are nonzero. The integral
rescaling f(19^nu*T)/(c_4*19^(4nu)) reduces to

    F(T)=T^2*(T-U_bar)*(T-V_bar)
        =T^4-(U_bar+V_bar)*T^3+U_bar*V_bar*T^2.

For example B(19^nu*T)/c_4 reduces to 1; every nonconstant term has
positive valuation, including its monic degree-16 term. Hasse
differentiation commutes with this affine rescaling and reduction.
If H_3 has a noncenter witness, its reduction at 0,U_bar,V_bar is one
of -(U_bar+V_bar),3U_bar-V_bar,3V_bar-U_bar. If H_2 has a noncenter
witness, it cannot be 0 since c_2!=0, and its reduced values at the
other two roots are U_bar*(3U_bar-2V_bar) and
V_bar*(3V_bar-2U_bar). This proves the remaining necessary ratios in L1.
No distinctness of their residues was presumed; the equations themselves
impose it in these sole-center cases at prime 19.

## 2. A complete small finite projection

Choose the center whenever available, as in the accepted canonical-mask
enumeration. For each of 88 masks, assign every noncenter normalized
derivative equation to 0,u or v. The exact recursion gives a_j(U,V) in
Z[U,V]. Let a_j^0 denote its value at (0,0), which depends only on the
center mask. Let A_j,B_j be its two linear coefficients modulo19.
All labels are allowed, repeated witnesses included.

At a center position these coefficients obey

    A_j=-sum_(k<j) binom(j,k)*A_k mod19,

and likewise for B_j. At a noncenter position only the k=j-1 term is
linear, giving -j*a_(j-1)^0 in the selected u or v slot, or zero for
the zero label. If a_(j-1)^0 is divisible by19, all three choices have
the same zero linear coefficient. Thus one need only label the active
positions where a_(j-1)^0 is a unit. Every full assignment maps to one
of these projected label assignments; omission of its higher terms is
legitimate only to the stated modulus.

Define beta_j=binom(20,j)/19 and

    q0=-1+sum_(j=2)^18 beta_j*a_j^0.

The exact divided center-root equation has integral coefficients and
constant q0. Every nonconstant monomial at (u,v) has valuation at least
nu. Therefore nu<=v19(q0), provided q0!=0. Exact calculation finds q0
nonzero for every mask, with bound 1 for 84 and bound 2 for four. This
gives a finite complete list of possible minimum valuations, not a
rational-height bound.

For each projected label assignment and each 1<=nu<=v19(q0), require
a_17^0 and a_18^0 divisible by19^nu; if not, no actual variables of
that minimum valuation can cancel their lower constant digits. Set
u=19^nu*U,v=19^nu*V. Since 2nu>=nu+1, exact recursion gives

    a_j=a_j^0+19^nu*(A_j*U+B_j*V) mod19^(nu+1).

Three necessary affine equations over F_19 are now

    q0/19^nu + sum beta_j*(A_j*U+B_j*V)=0,
    a_18^0/19^nu + A_18*U+B_18*V=0,
    beta_17*(a_17^0/19^nu + A_17*U+B_17*V)
        + beta_16*a_16^0*(U+V)=0.                 (E)

The first is the next divided center-root digit. The second uses
v19(a_18)>=2nu: its displayed consequence modulo19^(nu+1) is weaker
than the full condition when nu=2, which is harmless. The third is
exactly (R). At least one of U,V is nonzero. In a sole-center mask,
L1 forces both to be nonzero and imposes the corresponding displayed
ratio. When both center flags are true, no such ratio or nonzero-both
condition is imposed, so unequal valuations remain allowed.

This is a necessary superset test. It does not assert that a passing
label/nu/residue triple lifts to an exact rational CA polynomial.
Inactive derivative choices and higher-order equations can only remove
additional candidates, not restore one excluded by these necessary equations.

## 3. Exact evidence and unresolved review gate

`computations/coordinator-J16-coupled-leading-v1.py` independently of any
review constructs the complete projection, explicitly reusing the earlier
constructor's first-order method. It checks 11,559 projected label/nu
tests over all 88 masks, then all 361 residue pairs at each retained
constant-divisibility branch. It finds no allowed point for exactly

    49653,53811,56921,57023,57049,62315,63471,64375,
    82365,82877,83059,90180,92151,92153,93023,93059,95103,122803.

The result retains the full 70-mask list and a leading-point example for
each surviving minimum valuation. Of the excluded masks, eight have
only the H_3 center flag, nine only the H_2 flag, and one both. These
are canonical flags, not assertions that a formal family must fail at
the center whenever its bit is absent.

The dedicated child PID 44069 completed in 2.406 seconds, exit 0,
under a 30-second external timeout, with a checkpoint per mask, reaped.
No native CAS, installation, paid API, global kill or cap increase was
used. Exact source/result hashes, command and stdout are in the job.
This is constructor evidence only. Both reviewers must independently
reconstruct L1, (R), every condition in (E), valuation-case coverage,
active-label compression and the complete finite result before L2 or
the proposed 754-mask count is promoted.
