# Actual residual sets and coinvariant fibers for 2020 B4(b)

2026-10-17 UTC. **Candidate proof - unverified.** Constructor:
`/root/review_2017_coarsening_r1`; requested `gpt-6.1-sol` with `max`
reasoning, verified effective-setting readback unavailable. Two OTHER
initially blind whole audits and coordinator reconciliation are required.
Only the open part (b) is investigated. No preliminary construction,
mathematical search, CAS, certificate replay, new verification cutoff,
novelty or unrestricted classification is claimed.

This packet gives necessary restrictions on ACTUAL cyclic planar
difference sets in the nonsaturated branch. Its main consequence is:
outside order four, a known multiplier subgroup of order greater than
12 acts faithfully on the complement of a unit orbit whenever that
complement has at least two points. An elementary abelian-action bound
then forces a logarithmic number of residual points. The proof first
identifies a nonfaithful residual as an actual smaller difference set;
it never treats an arbitrary residual or abstract matrix as one.

## 0. Exact domain, old roles and inputs

The official question asks which integers n>=2 are taut. Use the
accepted part-(b) dictionary, without reproducing it: for

    q=n-1>=2, k=q+1, v=q^2+q+1, G=Z/vZ,

tautness is equivalent to an ACTUAL subset D of k distinct residues
whose ordered differences represent every nonzero element of G once.
The accepted q=1,n=2 boundary remains outside all new statements.
The official discussion attributes prime-power existence to Singer;
that established existence result is used only for two boundary
examples, without reconstructing the preliminary argument.

Use the common sum-zero translate of D. Its full numerical multiplier
group M fixes this chosen D setwise. A known subgroup T<=M need not
be all of M, and setwise stability is not pointwise fixedness. All
groups of numerical multipliers here are abelian, as subgroups of
(Z/vZ)^*. The following are separately accepted inputs.

1. `proofs/reviewed-partial-v1.1.md` and its COMPLETE linked body
   `proofs/partial-v1.md`: the dictionary, common normalization,
   quotient/character equations, and the ATTRIBUTED planar First
   Multiplier Theorem. Each prime divisor of q, hence q itself,
   belongs to M. No sufficiency of quotient norms is imported.
2. `proofs/reviewed-return-r3-v1.2.md`, repaired F1/F2: for a
   nonidentity subgroup U<=M put

       H_U=G^U, E_U=D intersect H_U, h_U=|H_U|, f_U=|E_U|.

   H_U is proper. If h_U=1, f_U is 0 or 1. If h_U>1, E_U is an
   ACTUAL cyclic planar difference set in H_U, and

       f_U=m_U+1, h_U=m_U^2+m_U+1, 1<=m_U<=sqrt(q).       (I1)

   Every numerical involution forces q=m^2 and is the particular
   element m^3 modulo v. In particular, when q is nonsquare M has
   odd order. Individual prime-order congruences use that element's
   OWN fixed subgroup; no common/individual substitution is allowed.
3. `proofs/reviewed-reasoning-return-r4-v1.2.md`, R4B/R4C: outside
   q=4, Cohen1989 Theorem1 supplies a unit d in the ACTUAL normalized
   D; its orbit dT has size |T|. The classical multiplier bound is
   |M|<=q+1. Cohen's literal two generator-free exceptions are

       E1={3,6,7,12,14}, E2={7,9,14,15,18}=-E1 in Z/21Z. (I2)

   The theorem is an attributed published import. Its full character
   sieve and finite exceptional-parameter analysis are not newly
   reconstructed here. Its hypothesis 1<k<v-1 holds for q>=2.
4. `proofs/reviewed-reasoning-return-r5-v1.1.md`: only its exact
   accepted classical-normalizer and saturated-branch scope is used
   to locate the remaining problem. Neither cyclicity nor prime-power
   order alone makes a plane classical; saturation is EXTRA.

The constructor authored the older repaired R3/F1/F2 packet and
reviewed R4/R5. This is new construction, not an independent re-audit
of those accepted inputs. The earlier q=4 quantifier error, the R4
final-moment error, both old reports, repairs and accepted copies
remain unchanged. Metadata preservation is recorded separately.

## R6A. Exact coinvariant fiber energy, including noncoprime overlap

Let U<=M be ANY nonidentity subgroup. Set H=H_U, E=E_U,
h=|H|, f=|E|, and define the additive coinvariant subgroup

    A=sum_{u in U}(u-1)G.

For generators u of U, the usual cyclic-group calculation gives

    h=gcd(v,u-1 for u in U), H=(v/h)G, A=hG,
    b=|A|=v/h, c=|H intersect A|=gcd(h,v/h).             (A1)

There is no assumption gcd(h,v/h)=1 and no assumption gcd(|U|,v)=1.
The same gcd describes all elements of U because if u,w are units,
uw-1=(u-1)w+(w-1), and inverses give the reverse containment for a
chosen generating set. In a cyclic group the common annihilator has
size h; the ideal of all images (u-1)G is exactly hG. The displayed
formula for c follows from the unique subgroup of each divisor order.

Write pi:G->G/A. Every U-orbit stays in one pi-fiber, since
ux-x is in A. For each y in G/A put

    g_y=|E intersect pi^{-1}(y)|,
    w_y=|(D minus E) intersect pi^{-1}(y)|.

The exact identity is

    b-c = sum_y [w_y(w_y-1)+2g_y w_y].                  (A2)

Indeed pairs of distinct D-points in the same pi-fiber are precisely
the ordered pairs with difference in A minus{0}. Uniqueness gives

    sum_y (g_y+w_y)(g_y+w_y-1)=b-1.

For E the corresponding differences are exactly H intersect A minus{0}:
if h>1 this follows from the actual smaller difference set I1; when
h=1 both sides below are zero because f is 0 or 1. Thus

    sum_y g_y(g_y-1)=c-1.

Subtracting proves A2, including its cross term and overlap correction.

Let rho be the smallest prime divisor of |U|. A point of D minus E
is not fixed by all of U, so its U-orbit has size a divisor of |U|
greater than one, hence at least rho. Each nonempty w_y is a union
of whole such orbits and is at least rho. Consequently

    b-c >= (rho-1)(k-f).                               (A3)

More generally rho in this conclusion may be replaced by any proven
common lower bound for the lengths of these nonfixed U-orbits. It
must not be replaced by |U| without freeness, nor by the order of
an unrelated multiplier.

If h>1, write f=m+1, h=m^2+m+1. Since U is nonidentity m<q;
A3 becomes

    v/h-c >= (rho-1)(q-m),                             (A4)
    (q-m)[q+m+1-(rho-1)(m^2+m+1)]
        >= (c-1)(m^2+m+1).                             (A5)

In particular q+m+1>=(rho-1)(m^2+m+1), strictly when c>1.
The displayed factorization follows by subtracting h from v before
collecting terms. It does not set c=1 silently.

For U=<t> of PRIME order ell, all nonfixed orbits have exactly
ell members. Put w_y=ell a_y. The exact nonnegative defect is

    b-c-(ell-1)(k-f)
       = ell^2 sum_y a_y(a_y-1)+2ell sum_y g_y a_y.     (A6)

Thus equality in A3 holds exactly when every a_y is 0 or 1 and
g_y a_y=0 for every fiber: at most one nonfixed orbit in a fiber,
and no such orbit in a fiber containing a fixed D-point. If h>1
one may replace k-f by q-m in A6. All fixed data in this clause
belong to <t> itself. This avoids the previously repaired error of
using G^T for a prime-order element contained in a larger T.

This is an elementary within-fiber difference count. Arasu's method,
as presented in Gordon2020, Theorem3, already counts differences
inside multiplier orbits. That published theorem assumes a direct
factor Z_p x H with coprime orders and a specified multiplier power.
It is not invoked outside those hypotheses here. A2 is proved directly
for cyclic coinvariants with arbitrary c; no new-method or priority
claim is made.

## R6B. A numerical pointwise stabilizer of a fixed Baer subgroup

Suppose a nonidentity U<=M has

    q=m^2, H=G^U, |H|=m^2+m+1, m>=2.                  (B1)

Then

    |U|=2, and its nonidentity member is m^3 modulo v.  (B2)

For any nonidentity u in U, H is contained in G^{<u>}. The latter
has an actual fixed difference set of order m_u by I1. Its order
is at most sqrt(q)=m, while containing H forces m_u>=m.
Therefore G^{<u>}=H for every such u. It follows that U acts
FREELY on G minus H: a nonidentity point stabilizer outside H would
contradict that equality. This is a conclusion, not an assumption.

Here

    v=(m^2-m+1)(m^2+m+1), b=m^2-m+1, c=1,
    b-1=q-m>0.

The two factors are coprime: a common divisor divides 2m, is
coprime to m, and is odd. Apply A2 with the now justified minimum
nonfixed orbit length |U|. It yields

    q-m >= (|U|-1)(q-m),

so |U|<=2. Nonidentity gives |U|=2; accepted F2 identifies its
involution. This statement concerns numerical multipliers of an
ACTUAL cyclic planar difference set. It is not a bound on arbitrary
collineations fixing a Baer subplane, and it makes no unrestricted
converse assertion that a square order must be supplied with an
involution before the multiplier hypotheses are checked.

## R6C. A residual-kernel restriction in the nonsaturated branch

Assume q!=4, choose a unit d in the actual D, and let T<=M have
order s. Define

    O=dT, R=D minus O, r=|R|=q+1-s.

The set O is an ACTUAL full unit orbit of size s. Let

    K={t in T: tx=x for every x in R}, a=|T/K|.

The kernel is for the action on this chosen residual R. It is not
the kernel of the action on all of D and is not a stabilizer of one
arbitrarily selected fixed subgroup. Both O and R are T-invariant.

### C1. A nontrivial kernel forces an actual residual plane

Suppose r>=2 and K is nonidentity. Put H=G^K. Every member of R
lies in H. No point of O does: if a nonidentity u in K fixed a
unit x, cancelling x would give u=1 modulo v. Therefore

    R=D intersect H,
    h=|H|=r^2-r+1, m=r-1, q>=(r-1)^2.                 (C1)

This is the step making R an ACTUAL cyclic planar difference set
of order r-1. No such assertion is made for a general residual.

Since T is abelian, it preserves H and restricts to a group of
automorphisms of H preserving R. The kernel of restriction is exactly
K. One inclusion is immediate from R subset H. For the other, an
element fixing R pointwise fixes every difference of R. These are
all nonzero elements of H by C1, so it fixes H pointwise. The image
therefore has order a and consists of actual numerical multipliers
of R, viewed in its OWN cyclic group H. Changing a generator of H
does not change this order. If needed, translating R to its own
sum-zero frame leaves its numerical multiplier group unchanged;
one does not assume that ambient normalization already normalizes R.

Define

    A_r = r if r!=5, and A_5=6.

Then

    a<=A_r.                                          (C2)

For r=2 the group H has order three and Aut(H) has size two,
which proves a<=2 directly; Cohen's nontriviality convention is not
used at this degenerate order-one boundary. For r>=3 and r!=5,
reset the accepted classical multiplier bound to the actual smaller
order m=r-1>=2, m!=4. It gives a<=m+1=r.

For r=5 the smaller group has order 21. If R contains a unit
relative to H, that unit's orbit under the image has a members,
all in R, and a<=5. Otherwise Cohen's theorem says that, in any
chosen cyclic coordinates, R is one of the TWO LITERAL exceptions
I2. Their setwise stabilizers have order six, as follows without
a table. In E1 the two points {7,14} have additive order three;
all two units modulo three preserve that pair. The other three
points are 3{1,2,4}, of additive order seven; the multipliers
preserving them modulo seven are precisely {1,2,4}, the subgroup
of order three. CRT gives 2*3=6 stabilizing units modulo 21.
The negative set E2 has the same stabilizer. Thus a<=6. This
does not assert that every order-four difference set has no unit,
nor replace a bound by a classification of all cyclic planes.

### C2. Exact inequality for a nontrivial residual kernel

Let b=v/h, c=|H intersect hG| as in R6A with U=K. Every K-orbit
on O is free, with length |K|=s/a, because its points are units.
There are no other points of D outside H. Hence A2 gives

    v/h-c >= (s/a-1)s.                               (C3)

Since c>=1 and a<=A_r,

    (v-h)/h >= s^2/A_r-s.

Use q=s+r-1 and h=r^2-r+1 to obtain EXACTLY

    v-h=s(s+2r-1).

Cancelling the positive s and rearranging is legitimate because
h>A_r for every r>=2. It yields

    s <= A_r(h+2r-1)/(h-A_r)
      = { r^2(r+1)/(r-1)^2, r!=5;
          12,                 r=5. }                 (C4)

For r>=6 the first bound is at most 2r, since
r(r+1)<=2(r-1)^2 is equivalent to r^2-5r+2>=0.
But C1 would give s=q+1-r>=(r-1)(r-2)>2r, with the last
inequality following from the same positive quadratic. This is a
contradiction. For r=2,3,4, the bounds in C4 are respectively
12,9,80/9; r=5 gives 12. Consequently

    K!=1 and r>=2 imply 2<=r<=5 and s<=12.             (C5)

These are necessary conditional restrictions. They do not construct
a difference set at every small parameter satisfying the inequalities.

### C3. Faithfulness and a logarithmic nonsaturation gap

If q!=4, s>12 and r=q+1-s>=2, C5 forces K=1. Thus T is an
abelian group acting faithfully on the residual r points. Let its
orbits there have sizes r_1,...,r_j, with sum r_i=r. Because T is
abelian, the point stabilizer T_i on each orbit is the same at every
point of that orbit and is normal. The quotient T/T_i has order
r_i. Faithfulness says intersection_i T_i={1}, so the diagonal map

    T -> product_i T/T_i

is injective. In particular s divides product_i r_i, and

    s <= product_i r_i <= 3^(r/3).

For completeness, u<=3^(u/3) holds for each positive integer u:
u=1,2,3 are direct (at u=2 cube both sides); from u>=3 to u+1
use (u+1)/u<=4/3<3^(1/3). Multiplying proves the second inequality.
Therefore the new restricted necessary condition is

    q+1-|T| >= 3 log_3 |T|
    whenever |T|>12 and q+1-|T|>=2.                   (C6)

Equivalently, for an ACTUAL difference set with a known multiplier
subgroup of order s>12, either its residual size is 0 or 1 (the
already accepted extra saturated branch), or it is at least
3 log_3 s. This applies to T=M as well as a proper known subgroup.
It is not a theorem that saturation holds, and it does not exclude
all positive residual sizes. The stronger but false step s<=r is
not used; faithful abelian actions can have several residual orbits.

### C4. The faithfulness cutoff cannot be changed to s>=12

Use only the established existence of a classical Singer difference
set at q=16, v=273, in its accepted common sum-zero frame. Its
existence is attributed, not constructed here. Hall gives the known
subgroup T=<2>. Since 2^12-1=4095=15*273 and every proper divisor
of 12 is at most six, while 0<2^6-1=63<273, T has order exactly
12. Cohen supplies a unit d, so O=dT has size 12 and R has size
17-12=5.

The nonidentity multiplier u=2^6=64 has fixed subgroup of size
gcd(63,273)=21. By accepted F1 its fixed intersection with D has
five members. None belongs to the unit orbit O, hence that fixed
intersection is exactly R. Thus u belongs to K and K is nontrivial.
This is an ACTUAL known example, not just an abstract action or an
arithmetic parameter vector. It shows the strict s>12 threshold in
C3 is necessary for this faithfulness assertion. No claim that the
full multiplier group is T is needed. It does not contradict the
logarithmic inequality by itself; it refutes extending the intermediate
faithfulness conclusion to s=12.

## R6D. A character bound in a nonsquare modulo-three stratum

Assume q is nonsquare and q=1 mod3. Necessarily q>=7. Then the
full actual numerical multiplier group M has order s satisfying

    3s <= q-2+2sqrt(q).                               (D1)

The same bound holds for the order of any known T<=M. This is a
multiplier-size consequence of an actual fixed intersection and the
accepted character equation, not a new norm-exclusion computation.

By accepted F2 the abelian group M has odd order. Reduction modulo
three maps M to a group of order two, so every member is 1 mod3.
Its common fixed subgroup therefore contains the subgroup of G of
size three. The known multiplier q has order exactly three modulo v:
q^3-1=(q-1)v, while q and q^2 are not 1 mod v. Its OWN fixed
subgroup has size gcd(q-1,v)=3. Consequently G^M=G^{<q>} is
exactly that size-three subgroup.

Let b=v/3, H={0,b,2b}, E=D intersect H. Accepted F1 gives |E|=2.
The nonfixed q-orbits in D have length three and their element sum
is x(1+q+q^2)=0 in G. Since D is sum zero, the two points of E
sum to zero. Hence E={b,2b}. If q=3t+1, then

    b=3t^2+3t+1=1 mod3.

Thus E contributes one point to EACH nonzero residue class modulo
three. These points are nonunits, since b>1.

Cohen supplies a unit d in D. Its full orbit dM has s points,
all in the SAME nonzero residue class modulo three because M=1
mod3. That orbit is disjoint from E. Therefore one of the two
nonzero quotient occupancies n_i satisfies n_i>=s+1. With omega a
primitive complex cube root of unity, accepted P4 gives

    Z=sum_{i=0}^2 n_i omega^i, |Z|=sqrt(q),
    3n_i=k+2 Re(Z omega^(-i)) <= q+1+2sqrt(q).

Combining these two ACTUAL facts proves D1. Replacing M by a
known T only shortens its unit orbit and preserves the conclusion.
The fixed-set calculation used the OWN subgroup <q> explicitly;
the common fixed subgroup happened to be the same here by the two
opposite containments. This is not a new misuse of a common fixed
subgroup in an individual orbit congruence.

## 5. What this does and does not bridge

These restrictions need no extra S0 saturation hypothesis. They act
on actual nonsaturated configurations. R6A gives a coinvariant energy
test with all overlap retained; R6B settles the numerical common
pointwise stabilizer at a fixed Baer size; R6C rules out a logarithmic
band immediately below saturation when |T|>12; R6D adds an explicit
character bound in its nonsquare congruence stratum.

S0 cannot be proved for every actual taut order: at the known
classical order q=5, v=31 is prime and accepted R5B gives the full
multiplier group <5> of order three, less than q. This is an
attributed known existence example plus the accepted CLASSICAL
normalizer theorem. No claim cyclic=>classical is involved.

The accepted saturated even branch q>8 is equivalent, with Xia2023
Proposition1.2's exact reverse import, to an ACTUAL non-Desarguesian
flag-transitive plane of order q. This is the separate flag-transitivity
obstruction identified in the accepted source record, not an arithmetic
contradiction. The odd affine two-flag-orbit branch
does not satisfy that flag-transitivity hypothesis. Neither branch
is eliminated here, and none of those facts is applied to a general
nonsaturated plane.

In particular, when v is prime every nonidentity common fixed
subgroup is {0}; R6A then has no nontrivial subplane information.
R6C can still force a faithful residual action, but large residual
sets easily accommodate it. The remaining actual orbit unions must
still satisfy all difference incidences and character PHASES. The
present proof does not control those phases or force a small enough
residual. An abstract positive-definite matrix, a quotient norm, an
orbit cardinality solution or an arbitrary residual is not an actual
configuration. No full B4(b) answer or stronger universal prime-power
classification follows.

The complete obligations, constructor checks, failed routes, actual
source read limits, administrative commands and hash freeze accompany
this submission. Only the coordinator may promote its exact scoped
claims after two other whole audits; all earlier bytes are preserved.
