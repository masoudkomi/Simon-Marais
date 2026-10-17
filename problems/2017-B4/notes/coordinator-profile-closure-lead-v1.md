# A finite-test route for the feasible profile space

2026-10-17 UTC. **Research lead / candidate argument - unverified.**
Root reasoning, not an accepted theorem. No entropy upper certificate,
upper-R hypothesis, numerical value, annual answer or novelty claim.
This does not supply or independently review C's concurrent R5
realization proof, which remains separate and unverified. No program
or finite mathematical experiment was run.

The point of this lead is to make a possible upper-profile argument
precise enough to expose its remaining MASS/ENTROPY gap. Ordinary
compactness is not declared effective without a finite test.

Fix D>=2, v_i=(1,i-1), V=(v_1,...,v_D), and the full balanced
unit zonogon Z=V[0,1]^D. Its boundary lift is the usual fixed
polygonal lift h_boundary. Consider continuous h:Z->[0,1]^D
with Lipschitz coordinates and

    Vh(x)=x, h|boundary=h_boundary,
    Delta_ij=det(grad h_i,grad h_j)>=0 a.e. for i<j.    (P)

This is a GLOBAL continuous lift constraint, not an arbitrary finite
decoration. It is not obtained by taking pointwise convex mixtures
of the nonconvex allowable gradient set.

## 1. A fixed coordinate Lipschitz bound follows from the constraints

At a differentiability point write grad h_i=(a_i,b_i). From VDh=I,

    sum a_i=1, sum b_i=0,
    sum(i-1)a_i=0, sum(i-1)b_i=1.

Put Delta_ik=a_i b_k-b_i a_k, with its antisymmetric extension.
Directly summing gives

    a_i=sum_k(k-1)Delta_ik, b_i=-sum_k Delta_ik.

The two-by-two determinant expansion of VDh gives

    1=sum_(i<j)(j-i)Delta_ij.

All terms are nonnegative. Thus sum_(i<j)Delta_ij<=1,
|a_i|<=D-1 and|b_i|<=1. In particular |grad h_i|<=D.
Convexity of Z turns the a.e. bound into a global D-Lipschitz
representative, by interior mollification and line integration.
So a fixed compact ambient class of coordinate-D-Lipschitz maps
contains every such profile. This bounds each coordinate; it does
not claim the whole vector map has Lipschitz constantD.

## 2. Minors have continuous boundary tests despite nonconvexity

For a closed rational rectangle Q strictly inside Z define

    J_ij,Q(h)=integral_boundaryQ h_i d h_j.

For coordinate-D-Lipschitz h,g with uniform coordinate error<=e,
integration by parts on the closed boundary gives

    |J(h)-J(g)|
      <=D perimeter(Q)(||h_i-g_i||inf+||h_j-g_j||inf)
      <=2D perimeter(Q)e.                            (1)

Indeed subtract the two integrals as
integral(h_i-g_i)dh_j - integral(h_j-g_j)dg_i.
The variation of each restricted coordinate is at mostD*perimeter.
This estimate concerns ACTUAL functions and their traces; it neither
averages gradients nor assumes the allowable gradient set convex.

For Lipschitz h, ordinary smooth Green's formula extends to

    J_ij,Q(h)=integral_Q Delta_ij.                    (2)

One direct proof mollifies h on a neighborhood of Q. Its gradients
converge in L1 there and remain uniformly bounded. The determinant
difference is bounded by a fixed multiple ofD times the gradient
difference, so its integrals converge. The boundary integrals
converge by(1). Smooth Green's formula itself follows by two
one-dimensional integrations by parts.

Consequently all the minor inequalities in(P) are EQUIVALENT to
J_ij,Q(h)>=0 for all rational interior rectangles and all i<j.
The forward direction is(2). For the reverse, a negative Lebesgue
point of a bounded minor would give a small negative-integral
rectangle, and a rational perturbation of its sides keeps the
integral negative. This would violate one of the listed tests.
The boundary of Z has area0 and creates no extra derivative condition.

Thus these constraints are CLOSED for uniform convergence within
the fixed Lipschitz class. This is a null-Lagrangian boundary
argument, not pointwise convexity of the gradient constraints.

## 3. What a finite-cover certification algorithm would do

The ambient coordinate-D-Lipschitz maps to[0,1]^D admit explicit
finite uniform e-nets. Choose a rational delta-net x_k of the
rational polygon Z and all tuples r_k on a finite rational mesh
of[0,1]. The clipped functions

    g(x)=clip_[0,1] min_k[r_k+D|x-x_k|]

are D-Lipschitz and computable at rational points. If the r_k
approximate h(x_k) within e0, the resulting g differs from h by
at most e0+2Ddelta. Taking all finite tuples, separately in each
coordinate, therefore gives an explicit finite ambient net. No
feasibility of a tuple is presumed. Square roots in the finite
formula are computable real numbers with elementary rational
error bounds, not an oracle for an unknown profile.

Each J functional is computable uniformly on this ambient class:
interpolate the two boundary traces linearly on a fine partition.
Their uniform error is at mostD times the mesh size, and(1) bounds
the resulting integral error explicitly. The polygonal integral
is the finite sum of (u_k+u_(k+1))/2 times(v_(k+1)-v_k).
Its sample values can then be approximated to any prescribed
rational tolerance. Evaluation constraints Vh=x and the fixed
boundary lift can likewise be tested at countable dense rational
points, using their uniform continuity moduli.

All FAILURES of(P) can therefore be enumerated as open uniform
balls: a strict negative J test, or a strict discrepancy from an
evaluation/boundary equality, has an explicit neighborhood of
failure. This enumerates the complement of the feasible class
inside the compact ambient class.

For a proposed FINITE rational open-ball cover U of the feasible
class, enumerate these failure balls and progressively refine
finite ambient nets. If U together with the accumulated failure
balls covers every ambient net ball with a strict margin, halt
and certify coverage. If U really covers the feasible class,
compactness gives a finite subcover of the ambient class by U
and failure balls, and some sufficiently fine net verifies it.
If U does not cover the feasible class, no sound margin check
can halt. This is a HALTING CERTIFIER FOR TRUE COVERS, not a
total decision procedure for noncoverage or a chosen feasible
point. No unlicensed real-closed-field decision theorem is used
on an infinite-dimensional function space.

## 4. The missing implication remains entropy

The foregoing argument, if fully audited, would supply a precise
effective closedness/cover interface. It does not estimate how
many marked tilings have any one profile. C's separate in-progress
realization theorem aims to approximate each feasible h by an
actual balanced tiling at every p. IF its claimed uniform bound
is proved, finite enumeration of actual B_D(p) tilings would also
give explicit Hausdorff nets of this profile class. This is a
conditional future use, not an accepted import from an unfinished
candidate. No enumeration is being run.

Even those two facts would only approximate the set of SHAPES.
The scalar k_D concerns the exponential MASS of fillings. A
convergent entropy upper approximation still needs a proved
finite local-count/profile inequality and the relevant converse
realization of that mass. Neither set convergence nor one tiling
near each shape supplies it. The earlier free-boundary SFT/LP
failure is therefore not repaired merely by this lead.

All steps above require whole audits before use as a proved
premise in a new candidate. The elementary boundary/compactness
methods are classical and not claimed novel. This note preserves
the concrete proposed test mechanism and its precise unresolved
endpoint, rather than claiming the 2017 value computable.
