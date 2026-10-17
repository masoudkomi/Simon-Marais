# Finite orientation charts for weakly ordered slope rows

**Candidate proof - unverified.** Coordinator, 2026-10-17 UTC.
Two fresh initially blind whole nonconstructor audits are required.
No H, PR, entropy recovery or official limit is claimed. This packet
addresses an explicit orientation obligation in the rank-mesh program;
that program is not a premise of the elementary statements below.

Fix D>=2 and v_i=(1,i-1), and let V be the matrix of these columns.
Let J be a D-by-2 real matrix with

    VJ=I_2, det(J_i,J_j)>=0 for every i<j.

Zero rows are permitted. The rows span R^2 because VJ=I_2.
They are the relevant tangent matrices, but the algebra below does
not assume an entropy theorem, a strict maximizer, or profile convexity.

## OC1. A cyclic reorientation makes all nonzero rows positively ordered

There is an index k, 2<=k<=D, such that the list

    J_k,...,J_D,-J_1,...,-J_(k-1)

has all its nonzero rows in one open half-plane, in weak angular
order, with every ordered row minor nonnegative. Zero rows remain
zero. All parallel nonzero rows in this new list point in the same
direction and form consecutive groups, allowing interposed zero rows.

Proof. Give the first nonzero row angle0 by a physical rotation of
the coordinate axes. Every later nonzero row has angle in [0,pi]
because its determinant with that first row is nonnegative.
An inversion in this list of angles would have negative sine
unless the earlier angle were pi and the later angle0. Such an
endpoint inversion forces every row to have angle0 or pi:
any row with angle strictly between0 and pi, wherever placed,
would have negative determinant with one of that inverted pair.
That would make the row span one-dimensional, a contradiction.
Consequently the nonzero angles are weakly increasing in [0,pi].

Since the span is two-dimensional, two successive nonzero rows
in that list have a positive angular gap. Choose k to be the
original index of the later row. Rows between the two chosen
indices are zero. The cyclicly reoriented nonzero angles are

    theta_k,...,theta_D,theta_first+pi,...,theta_previous+pi.

They are weakly increasing: theta_D<=theta_first+pi. Their total
span is pi-(theta_k-theta_previous)<pi. Hence they lie strictly
inside some open angular half-plane and have the stated nonnegative
ordered minors. Equality of two of these nonzero directions means
positive parallelism; their weak angular order makes each such
group consecutive among the nonzero rows. No antiparallel pair
remains. This proves OC1.

The choice depends on J. Only D-1 possible cuts occur, so this
is a finite family of charts, not a new continuum of orientations.
There are two independent directions u,v with J_i u,J_i v>0
for every nonzero row in the chosen chart: the common strict
positive dual cone is open and nonempty. Its margin need not be
uniform as nonzero rows approach zero or angular gaps close.

## OC2. Exact reorientation of a full tiling and its lift

Fix a cut k and an actual full marked balanced zonogon tiling of
content p in each direction. For i<k set epsilon_i=-1; otherwise
epsilon_i=1. Reorder indices as k,...,D,1,...,k-1, simultaneously
for all vectors, heights, rows and labels. Before that permutation set

    v'_i=epsilon_i v_i,
    a'_i(x')=a_i(x) if i>=k, and p-a_i(x) if i<k,
    x'=x-p sum_(i<k) v_i.

Then V'a'(x')=x'. The physical polygon is exactly a translate of
the original zonogon because [-p v_i,0]=[0,p v_i]-p v_i for
each flipped direction. Its tiles are unchanged up to translation;
the sign changes specify the opposite edge orientation on those tiles.
The count is therefore unchanged bijectively, with every complete
boundary word, tile and fine rank recovered by reversing the formula.

The reordered physical vectors are strictly angularly increasing in
an open half-plane too. Their angles are

    phi_k,...,phi_D,phi_1+pi,...,phi_(k-1)+pi,
    phi_i=arctan(i-1).

Their span is pi-(phi_k-phi_(k-1))<pi. All their ordered minors
are strictly positive. The new tangent is exactly the signed and
permuted J', with V'J'=I. Complete ranks are carried by p-a_i on
flipped colors, not discarded or replaced by independent port data.
The transformed boundary of the full convex zonogon has its usual
ascending/reversed cyclic color order from its new initial vertex.

This is an exact marked tiling/lift bijection at every p. It does
not assert that one chart simultaneously orients every tangent
matrix in an arbitrary nonaffine profile.

## OC3. Return to the standard integer directions

Let W have columns w_i=(1,i-1) in the NEW index order. The standard
full-tiling deformation sends the reoriented lift to

    y=W a'(x').

Each old tile maps affinely to its corresponding standard integer
tile, with positive determinant because both ordered vector lists
have positive minors. The full boundary maps once around the convex
standard zonogon. At a point outside the image edges, winding degree
is1 in that zonogon and0 outside. Every face-interior preimage has
positive sign. Thus there is exactly one preimage in the interior
and none outside. The same cyclic fan argument at edges and vertices
gives local degree1; a repeated interior preimage would give degree
at least2 at a nearby regular point. Boundary injectivity follows
from its convex cyclic order. Hence this is a face-to-face tiling
homeomorphism. Reversing the direction replacement recovers the
original marked tiling, giving an exact count-preserving bijection.

This map and its inverse are uniformly Lipschitz for the fixed D
and cut. On a tile of type(i,j), their derivatives are respectively
W_(ij)(V'_(ij))^(-1) and V'_(ij)(W_(ij))^(-1). There are finitely
many such invertible pairs. Integrating their bounded derivatives
along segments in the two convex full zonogons proves the two
global Lipschitz bounds. Thus the full deformation is bilipschitz,
with constants independent of p and the particular tiling.

For a tangent J' from OC1 put A=WJ'. Cauchy--Binet gives

    det A=sum_(i<j) det(w_i,w_j) det(J'_i,J'_j)>0,

because the row minors are nonnegative and at least one is positive.
Thus the transformed tangent in standard physical coordinates is

    J*=J' A^(-1), WJ*=I_2,
    det(J*_i,J*_j)=det(J'_i,J'_j)/det A>=0.

Every zero row, zero minor and positive parallel group is preserved.
Right multiplication by the invertible A^(-1) preserves the common
open half-plane property and positive rather than negative parallelism.
The new physical coordinates are the standard integer directions,
not merely signed directions silently treated as (1,i-1).

The affine-approximation interface is exact. Suppose on an actual
source region

    a'(x')=J'x'+c'+e(x'), V'c'=0, |e|<=E.

Then y=Ax'+Wc'+We, and

    a'(x')-[J*(y-Wc')+c']=(I-J*W)e.

The target offset c*=c'-J*Wc' lies in ker W. Thus the new lift
is within ||I-J*W|| E of J*y+c* on the actual image region.
This formula carries one common affine offset and does not choose
new offsets independently at different corners or boundary ports.

Uniform nondegeneracy of A for fixed D and cut follows from

    1=det(V'J')=sum_(i<j) det(v'_i,v'_j)det(J'_i,J'_j).

All physical determinants here are positive fixed numbers. Therefore
det A is between the minimum and maximum, over i<j, of
det(w_i,w_j)/det(v'_i,v'_j). In particular its lower bound does
not vanish merely because some row minors vanish. If ||J||<=G,
the matrix norms of A, A^(-1), J* and the displayed error map
are bounded in terms of D,G, uniformly over the finite cuts.
No lower bound on every nonzero row or positive minor is asserted.

## D=4 stratum consequence and remaining obligations

For D=4, every transformed tangent has between2 and4 distinct
nonzero positive-parallel groups. Four groups means all rows are
nonzero and all row minors strictly positive. Three groups means
either one zero row and three singleton nonzero rows, or one
positive consecutive merged pair and two singleton groups. Two
groups may have multiple rows or zero rows; the geometry alone
does not determine its entropy. Interposed zero rows can first be
deleted, with their fixed original labels retained.

This matches the TYPES of strict and clean-stratum arguments under
investigation. It does not prove their recovery estimates, rare-tile
flux, compatible reference tilings, finite-window skeleton sums or
global assembly. Applying the affine error identity does not itself
show that the image of a chosen physical window is a particular
canonical frame. Shape/buffer hypotheses must still be established
when invoking CUT or ST. Different profile regions may require
different charts and actual matching seams; no global chart is
assumed. No H, PR or official limit follows from OC1--OC3 alone.

The full-tiling deformation is the accepted marked-dictionary method,
not a novelty claim. The angle, common-offset and Cauchy--Binet
calculations are supplied explicitly to expose their quantifiers.
No mathematical computation, enumeration or CAS was used.
