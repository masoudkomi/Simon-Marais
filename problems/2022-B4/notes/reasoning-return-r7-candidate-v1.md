# An exact real-phase criterion and a maximal rational-base fiber

2026-10-17 UTC. **Candidate proof - unverified.** Constructor
`/root/review_2017_coarsening_r1`. Requested gpt-6.1-sol/max;
verified effective-setting readback unavailable. TWO OTHER fresh,
initially blind WHOLE audits and coordinator reconciliation are required.
Only2022 B4(b) is investigated. No infinite positive ordinary start,
termination/equality theorem, full-controller classification, novelty or
annual solution is claimed. No mathematical program, CAS, scan, larger
table, certificate replay or author rerun was used.

The new mechanism addresses the missing ordinary infinite lift directly.
It supplies an EXACT all-time real criterion, whose converse constructs
ONE ordinary integer trajectory, and an exact scalar rescaling to a
particularly restricted ceiling path. A hypothetical positive A/B lift
then forces TEN full rational-base expansions of the distinct value10C,
and a NINE-point ceiling-growth fiber there. Neither the all-time real
criterion nor this maximal fiber is proved impossible. Finite shadows,
normality and an at-most-two conjecture are not used as proofs of that.

## 0. Official scope, exact accepted input and notation

The actual official simultaneous recurrence is

    a_(n+1)=a_n+2 floor(b_n/20),
    b_(n+1)=b_n+3 floor(a_n/30),

with positive ORDINARY integers and a0*b0>=600. The open question is
whether equality must occur. The established preliminary trapping result
is attributed context, not researched or reproduced here.

Use COMPLETE accepted F5 and R6 in
`proofs/reviewed-reasoning-return-r5-v1.1.md` and
`proofs/reviewed-reasoning-return-r6-v1.1.md`. The new theorem uses the
restricted A/B realization, not an equivalence with every avoiding
controller. Put

    beta=11/10, gamma=121/100,
    10Q_(n+1)=11Q_n+h_n,
    (h_(2j),h_(2j+1))=(-w_j,w_j), w_j in{0,1},
    X_j=Q_(2j), 100X_(j+1)=121X_j-w_j.             (I1)

The exact ordinary block rules are

    w_j=0 iff X_j=0mod100,
    w_j=1 iff X_j=81mod100.                        (I2)

Thus F(x)=121x/100 on the positive0mod100 class,
F(x)=(121x-1)/100 on the positive81mod100 class, and STOP otherwise.
Every allowed positive block state is at least81. The accepted two
intermediate controller steps realize an actual finite/infinite A/B
path by the official start(a,b)=(60X0+1,60X0), avoiding equality.
The product condition is retained; no sequential-update substitution
is made. An infinite ordinary A/B path would refute universal equality,
whereas terminating all such paths would handle only this family.

Accepted F5 supplies the following exact facts, whose source and failure
boundaries remain in force.

* Every positive real has at most TEN full admissible base11/10
  expansions, with full alphabet0,...,10, prefix integrality and one
  common global radix convention (F5A). This is not the smaller ceiling
  alphabet0,...,9. Zero has one expansion.
* Ordinary ceiling digits are d_n=10Z_(n+1)-11Z_n in0,...,9.
  Finite integer canonical representations are unique at any fixed
  padded length. Appending a digit which makes the next prefix an
  ordinary nonnegative integer preserves admissibility.
* A positive ordinary A/B path has BOTH letters infinitely often and

      C=lim_n beta^(-n)Q_n=X0-R0>0,
      R_j=sum_(k>=0)w_(j+k)100^k/121^(k+1),
      0<R_j<1/21, gamma^j C=X_j-R_j.              (I3)

  These R_j are REAL series. They are not identified with the two-prime
  series under which X0's ordinary membership is still unresolved.
* At C itself, F5C gives exactly NINE full expansions and an EIGHT-seed
  ordinary ceiling-growth plateau. R6's finite-prime rational cycles
  and finite ordinary shadows do not create any ordinary infinite path.

The constructor authored OLD accepted R4 and reviewed older complexity,
R3/F5/R6 packets. This is NEW construction, not an independent audit
of that older work. No new R7 proof contribution from another worker
has been used. All frozen old bytes remain unchanged.

## Proposed claims and the unresolved bridge

Let H=(20/21,1), L=(1/21,1/11), J=H union L, as subsets of[0,1).

**R7A.** A positive ordinary infinite A/B path exists if and only if
some C>0 satisfies, for EVERY j>=0,

    {beta^(2j)C} in H,
    {beta^(2j+1)C} in J.                           (P)

The construction below recovers ONE ordinary start X0=ceil(C) and
ALL its actual steps. This is not an inference from changing finite
representatives, and it retains the odd/intermediate powers missing
from the older one-interval condition.

**R7B.** There is an explicit bijection between positive ordinary
infinite A/B starts X0 and positive ordinary ceiling starts Z0 such that

    Z_(n+1)=ceil(11Z_n/10),
    d_n=10Z_(n+1)-11Z_n in{0,1} for ALL n,
    d_(2j)=1 for ALL j.                            (S)

It is Z0=10X0-1, with exact full-time formula in Section2. The digit
word is a concatenation of blocks11 (A) or10 (B). In particular
every Z_n is0 or9mod10, and every even Z_(2j) is9mod10. Dropping
the even-time condition is only a necessary relaxation, not an
equivalence with every such two-residue ceiling orbit.

**R7C.** Any hypothetical positive ordinary A/B path of real growth C
forces exactly TEN full admissible expansions of10C, with nine
eventually minimal tails, nine eventually maximal tails and eight
common unary tails. For G(z)=lim_n beta^(-n)ceil(beta*.)^n(z) on
positive ordinary integers, its ENTIRE fiber is

    {z>0:G(z)=10C}={10X0-9,...,10X0-1}.            (M)

Consequently a theorem excluding TENfold fibers would suffice to
exclude A/B lifts. No such theorem is proved or assumed here. The
new value10C is different from C; its tenfold fiber does NOT
contradict F5C's ninefold fiber of C.

**R7D.** The feasible C in(P) is unique for each ordinary X0. The
set of all such C is uniformly discrete: any two distinct members
are more than20/21 apart. This gives no emptiness proof. Section4
also makes one exact, still UNPROVED future-to-past termination
bridge explicit by examining actual ordinary predecessors.

## 1. R7A: the two real intervals give an exact ordinary criterion

### 1.1 Necessity, including every odd time and strict endpoint

Suppose an ordinary positive A/B path exists. Use its REAL C and
R_j in(I3). At even times Q_(2j)-beta^(2j)C=R_j belongs to(0,1/21),
so its fractional part lies in H. Since

    R_j=(w_j+100R_(j+1))/121,

the intermediate integer Q_(2j+1) has error

    E_(2j+1)=Q_(2j+1)-beta^(2j+1)C
             =(10/11)R_(j+1)-w_j/11.              (1)

For an A block this is strictly between0 and10/231, hence less
than1/21; its fractional part is again in H. For a B block it is
strictly between-1/11 and-1/21, so the fractional part is in L.
All inequalities are strict because both letters recur in every
tail. Thus(P) is necessary, with the odd interval recording the
ACTUAL block letter. No rationality of C is asserted.

### 1.2 Sufficiency constructs ordinary states at all times

Now suppose ONE C>0 satisfies ALL of(P). Put V_n=beta^n C and
choose integers Q_n by

    Q_n=ceil(V_n) if {V_n} in H,
    Q_n=floor(V_n) if {V_n} in L.                  (2)

This is unambiguous since H,L are disjoint and every even fraction
lies in H. Write E_n=Q_n-V_n. Exactly,

    H-state: 0<E_n<1/21,
    L-state: -1/11<E_n<-1/21.

The quantity h_n=10Q_(n+1)-11Q_n is an ORDINARY integer and equals
10E_(n+1)-11E_n. The three transition types actually required by(P)
have the following strict ranges:

|transition|range containing h_n|only possible integer|
|---|---|---:|
|H to H|(-11/21,10/21)|0|
|H to L|(-10/11-11/21,-10/21)|-1|
|L to H|(11/21,1+10/21)|1|

The second lower endpoint exceeds-2 because10/11<1 and11/21<1;
the third upper endpoint is less than2. Hence each row really has
only its listed integer. At even time the state is H; if its odd
successor is H the two corrections are(0,0), and if it is L the
two corrections are(-1,1). Set w_j accordingly. We have obtained
EXACTLY(I1) at ALL times, not just the first one or two.

Positivity must also be checked. Each even Q_n is ceil(V_n)>=1.
For an H-to-H first step,10Q_(n+1)=11Q_n>0. For an H-to-L first
step,10Q_(n+1)=11Q_n-1>=10, so that odd integer is positive too.
Thus every Q_n is an ordinary positive integer. Grouping each pair,

    100X_(j+1)=121X_j-w_j, X_j=Q_(2j)>0.

Reducing this ORDINARY identity modulo100, and using
121^(-1)=81mod100, gives exactly X_j0mod100 for w0 and X_j81mod100
for w1. Therefore EVERY step belongs to the accepted actual stopped
map and both intermediate controller steps are legitimate. The
accepted official realization provides the required positive product
and nonequality. Since all E_n are uniformly bounded, the growth
coefficient of this constructed path is exactly the ORIGINAL C.
This proves the converse without any profinite compactness step.

The older F5E two-time obstruction is correctly outside this new
criterion. Its C*=62-342/14641 satisfies the two block-time interval
tests but beta*C*=68+232/1331. This fraction is greater than1/11
and less than20/21, hence outside J. Thus the new odd-time condition
removes that explicit discrepancy2 example; no infinite counterexample
or termination is inferred from this local check.

## 2. R7B: clearing the bounded correction potential

For an actual A/B path define a bounded INTEGER potential

    t_(2j)=0, t_(2j+1)=w_j.

Then h_n=t_n-t_(n+1), an exact identity. Set

    N_n=10Q_n+t_n, Z_n=N_n-1.

Multiplying(I1) by10 gives

    10N_(n+1)=11N_n-t_n,
    10Z_(n+1)=11Z_n+(1-t_n).                      (3)

All values are ordinary integers. Since1-t_n is0 or1, it is a
valid canonical CEILING digit, so Z_(n+1)=ceil(11Z_n/10).
Here Z_n>0 because Q_n>=81. Also d_n=1-t_n=1 at every even
index. Its pair is11 at A and10 at B. This proves necessity of(S).
It is a scaling by TEN with a bounded state-dependent correction,
not a unit-coefficient bounded carry for the full controller.

Conversely take a positive ordinary ceiling path satisfying(S).
Its digit relation implies Z_n=-d_nmod10; hence

    t_n=1-d_n in{0,1},
    Q_n=(Z_n+d_n)/10

is an ORDINARY integer. A positive Z with digit0 or1 is respectively
0 or9mod10, so Q_n>=1. Substituting Z_n=10Q_n+t_n-1 into(3) gives

    10Q_(n+1)=11Q_n+t_n-t_(n+1).

The even digit1 says t_(2j)=0. With w_j=t_(2j+1), the correction
pairs are exactly(-w_j,w_j); integer grouping gives(I2) as in Section1.
Thus this is an actual positive A/B path. Its initial value is
X0=(Z0+1)/10, since d0=1. The constructions are mutually inverse.

Finally bounded t_n shows

    lim_n beta^(-n)Z_n=10 lim_n beta^(-n)Q_n=10C.   (4)

There is no claim that every positive ceiling path confined to0/9mod10
has this even-time digit alignment. There is also no claim that an
arbitrary full avoiding controller has a binary bounded potential
with h=t-t_next. The earlier full-controller carry obstruction does
not cover this restricted scaling, and is not contradicted.

## 3. R7C: the complete maximal fiber and its exact ordinary plateau

Assume a hypothetical positive ordinary A/B path. Its Z path from
Section2 has digits d_n=1-t_n in{0,1}, with1 at EVERY even index.
Since infinitely many B blocks occur, d=0 also occurs infinitely often.
Define its REAL tail error

    T_n=10C*beta^n-Z_n
       =(1/11)sum_(j>=0)d_(n+j)beta^(-j).

The geometric sum bound and both recurring digits give

    0<T_n<1 for EVERY n.                           (5)

### 3.1 Constructing ten full expansions

For each c=0,...,9 let Y_n^(c)=Z_n-c. These are positive ordinary
integers: Z0=10X0-1>=809, and Z_n grows. Exactly,

    10Y_(n+1)^(c)=11Y_n^(c)+(d_n+c),
    0<=d_n+c<=10.

Start with the canonical finite representation of Z0-c and append
these digits. Every prefix is admissible by ordinary integrality.
Their entire real values with the radix after the seed are

    Z0-c+sum_(n>=0)(d_n+c)/(11 beta^n)=10C,         (6)

because the constant-c geometric sum is c. Align all ten seeds
to ONE padded length. Their tails differ by distinct constant
offsets, so they are ten distinct expansions, without counting
leading-zero copies or changing radix separately for each word.
Accepted F5A already bounds the fiber by ten. The next argument
also reconstructs exhaustiveness directly.

### 3.2 Matching every full expansion to an exact shift

Choose one seed length m large enough for all ten words and with
V=beta^(-m)10C<1/10. An arbitrary global admissible expansion of V
has zero digits at indices>=0, since each such nonzero digit has
weight at least1/10 and all weights are nonnegative. It is therefore
one root word. Let U_n be its ordinary integer prefix value at
length m+n, with next digits a_n in0,...,10. The standard full-tail
bound gives

    U_n=10C*beta^n-B_n, 0<=B_n<=10.

Thus c_n=Z_n-U_n=B_n-T_n is an ordinary integer in{0,...,9}, by(5).
Subtract the two integer recurrences:

    10(c_(n+1)-c_n)=c_n+d_n-a_n.                   (7)

The right side lies in[-10,10]. Its value-10 would require
c_n=0,d_n=0,a_n=10 and force c_(n+1)=-1, impossible. Its value10
would require c_n=9,d_n=1,a_n=0 and force c_(n+1)=10, impossible.
The only remaining multiple of10 is zero. Therefore c_n is one
constant c in0,...,9 and a_n=d_n+c at ALL indices. Its first
length-m prefix has value Z0-c; fixed-length finite uniqueness
identifies that prefix with the constructed padded seed. Hence the
entire expansion is exactly one of(6). Common index translation
returns from V to10C. This proves EXACTLY TEN full expansions,
with no causal carry assumption or finite-state inference.

After their seeds, c0,...,8 have digits in0,...,9 and are minimal;
c9 takes digit10 at every even index and is not eventually minimal.
The shifts c1,...,9 have digits in1,...,10 and are maximal; c0
takes digit0 infinitely often and is not eventually maximal. The
eight shifts c1,...,8 have digits in1,...,9, so their nodes have
unique next digits and their tails are unary. The other two have
infinitely many branching positions. These counts refer to eventual
tails, not to arbitrary finite seed choices.

### 3.3 Exhausting the positive ordinary ceiling-growth fiber

For ANY positive ordinary z, its ceiling orbit U_n has bounded digits
a_n in0,...,9, so G(z)=lim_n beta^(-n)U_n exists and

    G(z)*beta^n-U_n in[0,9].

Suppose G(z)=10C. Then c_n=Z_n-U_n is an integer in{0,...,8},
because0<T_n<1. Equation(7) now has right side in[-9,9], so it
vanishes; c_n=c, a_n=d_n+c and z=Z0-c. Conversely each shift
c0,...,8 is a positive ceiling path with that growth. This proves(M),
including all positive seeds, not just a displayed subfamily.

The scalar identity G=10C is essential. F5C's full fiber at C has
size nine and its ordinary ceiling plateau size eight. The NEW full
fiber at10C has size ten and its plateau size nine. Multiplication
by10 is not a radix translation; the proof does not assume that
fiber cardinality is invariant under integer multiplication.

Accordingly, excluding TENfold fibers would now suffice to exclude
A/B. The old F5 paragraph warning that its ninefold argument was
not ruled out by excluding tenfold fibers must be understood as a
limit of THAT argument. If read as a universal logical insufficiency
claim, it needs this qualification after review of R7. No old frozen
byte is edited here. No mathematical F5A--F5E lemma is refuted: the
extra tenfold implication at a DIFFERENT value was not provided there.
Only the coordinator may reconcile that explanatory scope after both
new whole audits.

## 4. R7D: uniqueness, discreteness and a precise future-to-past gap

For feasible C in(P), Section1 constructs X0=ceil(C) and the
deterministic stopped map(I2). That ordinary start fixes every later
state and bit. Its positive real growth limit is therefore unique,
so at most ONE feasible C belongs to each interval

    (X0-1/21,X0).

If C<C' are distinct feasible values, their different integer starts
have X0'<X0 impossible: the displayed intervals are disjoint and
ordered. Thus X0'>=X0+1, and C'-C>1-1/21=20/21. This proves
uniform discreteness and countability, not emptiness. A metrical
almost-everywhere theorem cannot decide the remaining countable set.

There is also an exact ordinary predecessor description. An allowed
positive x has an integer predecessor under F if and only if

    x=0mod121 or x=98mod121.                       (8)

For the first case the unique predecessor is100x/121 in the A
class. For the second it is(100x+1)/121 in the B class, because
100^(-1)=23mod121 and-23=98mod121. Both predecessors are positive
and STRICTLY smaller than x; their congruences modulo100 follow
directly from121y=100x or100x+1. Conversely those are the only two
affine equations for a predecessor, and the residue classes are
disjoint. This is about ACTUAL integer predecessors, not p-adic ones.

If any positive ordinary infinite survivor exists, take the smallest
such start. Its residue modulo121 CANNOT be0 or98: the predecessor
in(8) would be a smaller positive survivor. Equivalently, every
survivor's backward descent eventually reaches an ordinary start
outside those two incoming classes, and its forward trajectory still
survives forever. Thus the following would be a sufficient termination
bridge:

    UNPROVED: every positive ordinary infinite A/B survivor
              has an ordinary predecessor under F.                (B)

Under(B), well-ordering immediately rules out all survivors. Neither
the real criterion(P), maximal fiber, finite-prime cycles nor finite
ordinary lifting proves(B). It is a clean future-to-past inference
still missing; it is not accepted as a theorem or silently used in
Sections1--3.

## 5. Why current rational-power and representation theorems do not close it

The union J has total length

    |H|+|L|=1/21+(1/11-1/21)=1/11.

However its shortest containing circular arc has length
1/21+1/11=32/231, strictly greater than1/11=21/231. Dubickas2009,
*Powers of a rational number modulo1 cannot lie in a small interval*,
Theorem1, excludes a SINGLE CLOSED circular interval of length1/p
when1<q<p<q². These integer hypotheses hold for11/10, but its
geometric hypothesis does NOT hold for J. The even-time base gamma
has numerator121, whose critical length1/121 is smaller than1/21.
Neither application gives a contradiction. The two component lengths
must not be added and substituted as the length of one interval.

Geometry matters even more generally: Kari--Kopra2017, Corollary4.11,
gives, for each coprime p>q>1 and each epsilon>0, SOME finite union
of intervals of total length at most epsilon containing all powers
modulo1 of SOME positive real. Their set depends on epsilon and
is not our J; this is not an existence theorem for(P). It prevents
a blanket measure-only extension of the single-interval exclusion.
Theorem5.9's existence of other large forbidden unions likewise does
not identify this fixed J as forbidden. These source contexts are
not new proof premises for R7A--R7D.

The AFS full alphabet,1/10 weights and prefix language are retained.
Its at-most-two Corollary38 assumes p>=2q-1, false at11/10. AEVv2
states general at-most-two/normality and the proper-residue termination
route as conjectural/conditional. Original Dubickas--Mossinghoff
Proposition3.2 proves only a SINGLE allowed ceiling residue; our
relaxation has TWO,0 and9, plus an even-time restriction. No source
read here supplies the needed no-tenfold theorem or proves(B).

## 6. Remaining problem and review boundary

This packet replaces the insufficient block-time fractional interval
by an exact PHASED all-time criterion and reveals a maximal fiber
forced by a hypothetical ACTUAL ordinary lift. It neither realizes
that all-time criterion nor excludes it. Ordinary versus rational
cycles, two-prime shadows and real evaluations remain distinct.
Even a termination proof for this A/B family would not settle all
ordinary avoiding controller paths. The full-controller signed alphabet
need not be a binary coboundary, so Section2 cannot be extended to it
by assertion or by the mere finiteness of the controller.

The full source/failure/worklog/constructor-check/obligation packet
accompanies this proof. Two OTHER fresh initially blind whole audits
must verify both converses, every integer range, all canonical seeds
and complete fiber recovery, phase indexing, positivity and official
realization. Only the coordinator may promote exact scoped results;
no full annual answer, novelty or arithmetic resolution is inferred.
