# 2020 return R2: initially blind whole reconstruction

2026-10-17 UTC. Reviewer `review_2021_reasoning_j15_r2`.
Requested gpt-6.1-sol/max; effective readback unavailable. I did not construct
or contribute to this packet. This complete report, ledger, source checks
and integrity freeze were completed before reading any peer 2020 return
review or findings. Only root may promote a repaired scoped result.

There is one substantive quantifier/notation defect: F4 uses the previously
defined COMMON fixed subgroup H=G^T when a single prime-order t is introduced.
Its orbit congruence is valid for H_t=G^<t>, not for arbitrary H=G^T. An
actual sum-zero normalized order-4 example below refutes the literal h=1
version. The author should give a full versioned repair making that change
explicit, and both reviewers should re-audit the affected claim and scope.

The remaining F1/F1a/F2/F2a/F3/F3a/B1 arguments reconstruct on their explicit
domains. The F4 repair is local: F1a uses T=<p>, and F2 uses the fixed
subgroup of its one involution; neither argument needs the false general-T
congruence. No full classification or improved published search range is
proved here. No mathematical program, scan or CAS was used in this review.
The one finite counterexample was constructed and verified by hand.

## Exact inputs and accepted normalization

Candidate: `notes/reasoning-return-r3-candidate-v1.md`, SHA-256
`2cb5803b20cdcc96961956773f02a3fe2e00f0ae9a4bee8df56af0ec2cd86796`.
Constructor freeze-v1 SHA-256
`413351e9d6d6b9e8c463ba6b3ad230f2d4440c5042711df882f879a7b82a02ed`.
I read the entire candidate, obligations, worklog, source Markdown/JSON,
official statement normalization, accepted partial register, acceptance,
and complete frozen P1–P6 argument. The new author is a different actor.

Use q=n-1>=2, k=q+1, v=q^2+q+1 and G=Z/vZ. A planar difference set D
has k distinct elements, with every nonzero ordered difference represented
once. The accepted P3 chooses a SINGLE translate with sum D=0. Since
gcd(k,v)=1, any multiplier translation then vanishes; every chosen known
multiplier fixes this same D SETWISE. It is not assumed to fix its members
pointwise. Each prime divisor of q is a unit modulo v and a known numerical
multiplier by the accepted attributed multiplier input.

The q=1 boundary and preliminary part (a) are not researched here. The
accepted equivalence and plane dictionary are used in their q>=2 scope,
with the ambient regular action a collineation action. Quotient occupancy
vectors are not treated as subsets with unique differences.

## F1: fixed-subgroup closure, size, embedding and the subplane bound

Let T fix D setwise, H=G^T and E=D intersect H. For nonzero z in H,
write its unique representation z=d-e. For EACH t in T, the ordered pair
(td,te) is another representation of the same nonzero z. Uniqueness of
ordered representations forces td=d and te=e individually. This holds
for every t, so both belong to E. Conversely E's nonzero differences
are differences in H, and cannot repeat. Therefore E is an actual
(h,f,1) difference set on H and f(f-1)=h-1.

No group-order coprimality with T is needed. If h=1, the equation gives
f=0 or 1, with E respectively empty or {0}; it does not give a plane.
If h>1, f>=2, m=f-1>=1 and h=m^2+m+1. For h=3 this is m=1, the
degenerate order-one boundary, not a nondegenerate subplane.

If t_1,...,t_s generate T, the simultaneous annihilator has size
h=gcd(v,t_1-1,...,t_s-1). To check the converse as well as the obvious
inclusion, Bezout implies any common killed x also satisfies hx=0
modulo v. Thus x is a multiple of v/h. Every such multiple is killed
by all t_i-1. There are exactly h of them.

For nonidentity T the fixed subgroup is proper: an element acting
identically on all G would be the identity unit. Consequently m<q when
h>1. For m>=2, the E+x incidence plane is embedded in the ambient one.
Indeed a full line D+g meeting two points x,y of H has a unique difference
pair in E, so g=x-d lies in H. Conversely (D+g) intersect H=E+g when
g is in H. Thus the ambient lines meeting two subplane points are
precisely the extended E+g lines.

There is an external point P because H is proper. It lies on at most
one extended subplane line; two such lines already meet at a subplane
point. If P lies on one, that line contains m+1 subplane points. Each
of the other m^2 subplane points needs a different other ambient line
through P, giving q>=m^2. If P lies on none, all m^2+m+1 subplane
points need different lines, giving the stronger q>=m^2+m. For m=1
the claimed q>=m^2 is automatic and no nondegenerate subplane is used.
It follows that h<=q+sqrt(q)+1 for every nontrivial proper H. All these
arguments pass as written.

### Issue 2020R2-01: F4 must use the fixed subgroup of t, not arbitrary T

The valid prime-order orbit count is

    |D|=|D^<t>| mod ell,
    |D^<t>|=|D intersect G^<t>|,

where t has order ell. It does not generally use |D^T| for a larger T.
F4, however, retains the notation h,f,m from the arbitrary common T
fixed subgroup just defined, without resetting T=<t> or introducing
h_t,f_t,m_t. Its h=1 clause is false under that literal notation.

Here is an exact counterexample inside the accepted domain. Take q=4,
v=21 and

    D={7,9,14,15,18} in Z/21Z, T=<2>.

The ten unordered pairs have the following positive undirected cyclic
separations, in the indicated order:

    (7,9):2, (7,14):7, (7,15):8, (7,18):10,
    (9,14):5, (9,15):6, (9,18):9,
    (14,15):1, (14,18):4, (15,18):3.

They are exactly 1,...,10. Since v is odd, the twenty ordered differences
are therefore exactly the twenty nonzero residues. D is an actual planar
difference set, not a quotient solution. Its sum is 63=0 modulo21.
Multiplication by 2 permutes it in the cycles (7,14) and (9,18,15).
The unit 2 has order 6 modulo21, so all T fixes this chosen D setwise.

But H=G^T=ker(2-1)={0} and f=0, because 0 is not in D. The element
t=8 in T has prime order 2. F4's literal h=1 congruence would require
q+1=5 congruent to f=0 modulo2, which is false. The element t=4
of order3 similarly gives 5 not congruent to 0 modulo3.

The intended correction works exactly: for t=8 the fixed subgroup has
size7 and intersection {9,15,18}, so 5=3 mod2. For t=4 it has size3
and intersection {7,14}, so 5=2 mod3. The same global membership of 0
is retained throughout; no independent singleton choice was made.

Required repair: explicitly set T=<t> for the F4 paragraph, or replace
h,f,m there by h_t,f_t,m_t defined from G^<t>. Then for h_t>1,
q-m_t=0 mod ell; for h_t=1, q+1=|D intersect {0}| mod ell. The proof
is immediate from t-orbits after that exact hypothesis repair. Check
that no later application accidentally uses the larger common fixed
subgroup with this congruence. This is a substantive statement-domain
repair, rather than an objection to common-fixed-subgroup closure itself.

## F1a: cofactor restriction and the 761 instance

For q=pu, p a prime divisor of q, the accepted multiplier theorem gives
p fixing the chosen D. Its own fixed subgroup has size gcd(v,p-1).
Reducing p to 1 modulo p-1 gives v=q^2+q+1=u^2+u+1 modulo p-1,
so the displayed gcd identity is exact. If h>1, the fixed-size equation
requires (2f-1)^2=4h-3; a nonsquare right side excludes D. It does not
assert that the descended order must already be a prime power.

For a prime p=20 mod57 and u=7, u^2+u+1=57=3*19. Now 19 divides
p-1 and 3 does not, so h=19 exactly, regardless of higher prime
valuations in p-1. Then f(f-1)=18 has no integer solution. This
excludes q=7p, equivalently n=7p+1, for every such prime p. It uses
the fixed subgroup of p itself, so does not use the invalid general-T F4.

Independently checked the one written prime certificate: sqrt(761)<28
and the primes below 28 are 2,3,5,7,11,13,17,19,23. Dividing 761 gives
remainders 1,2,1,5,2,7,13,1,2. Hence 761 is prime and equals 57*13+20.
The resulting q=5327,n=5328 are correct. q is 3 modulo4 and 2 modulo3,
so the stated comparison with those particular congruence tests is
consistent; the candidate does not claim that every earlier test passes
or that this is a new published bound. No prime-progression infinitude
or finite-range search is used.

## F2: complete involution fiber reconstruction

An involution t has exact order2 in the FULL unit group modulo v. Since
v is odd, division by 2 is an automorphism. The maps
alpha=(1-t)/2 and beta=(1+t)/2 satisfy alpha+beta=1, alpha beta=0,
alpha^2=alpha, beta^2=beta. Their images are A=ker(t+1) and
B=ker(t-1), giving G=A direct_sum B and t(a,b)=(-a,b).

Nonidentity t means a=|A|>1. Each fiber D_y over y in B is symmetric.
If two different x,z are not opposites, the distinct ordered pairs
(x,z) and (-z,-x) in that fiber have the same nonzero difference.
That is impossible. A fiber therefore has at most two points; a
singleton is {0}, because 2 is invertible. A double fiber is {x,-x}
with x nonzero. It gives precisely the two nonzero differences
+2x,-2x in A. Uniqueness of every (z,0), z nonzero, gives 2R=a-1.

If b=|B|=1, D is a single fiber and has at most2 elements, contrary
to q+1>=3. Thus b>1 and F1 for T=<t> gives |E|=s+1 and b=s^2+s+1,
s>=1. Counting singleton and double fibers gives q+1=s+a and hence
a=q-s+1. Since ab=v,

    0=(q-s+1)(s^2+s+1)-(q^2+q+1)
      =-(q-s)(q-s^2).

The q=s root makes a=1 and t the identity, contrary to hypothesis.
Thus q=s^2 and s=m>=2. We obtain a=m^2-m+1, b=m^2+m+1.
The factors are odd and coprime: a common divisor divides 2m and is
coprime to m. On A multiplication by m^3 is -1 because
m^3+1=(m+1)(m^2-m+1); on B it is 1 because
m^3-1=(m-1)(m^2+m+1). These agree with t on both summands, proving
t=m^3 modulo v. No prime-power hypothesis or plane-involution
classification entered this reconstruction.

For nonsquare q an even-order multiplier would give an exact involution
by its halfway power, impossible. A local even order at any divisor
divides the full multiplier order and forces it even. One must not
identify a partially negative CRT involution with global -1; the proof
does not do so.

## F2a: abelian 2-parts and the exact CRT coherence

All numerical multipliers form an abelian subgroup of the unit group.
F2 permits only one nontrivial involution m^3 when q=m^2. A finite
abelian 2-group with at most one involution is cyclic: if nontrivial,
its doubling map has a kernel of order2. Induction makes its image
cyclic of half the order, and a lift of a generator has full order.
The order2 base case is immediate. This argument uses commutativity;
it is not a claim about arbitrary nonabelian 2-groups.

Let ord_v(x)=2^a s with s odd and a>=1. The local order at an exact
odd prime-power factor r^e is 2^(a_r)s_r, with a_r<=a and s_r|s.
If a_r<a, the halfway exponent 2^(a-1)s is divisible by the whole
local order, so the local power is 1. If a_r=a, it is an odd multiple
of half the local order, so the local power has exact order2. At an
odd prime power the only nontrivial solution of z^2=1 is -1: the
factors z-1,z+1 have gcd dividing2. Hence the local halfway power
is -1 exactly at full 2-part factors.

The coprime A0=m^2-m+1 and B0=m^2+m+1 partition the exact prime
powers dividing v. Compare the halfway power with F2's m^3, which
is -1 on A0 and +1 on B0. This proves F10 exactly. Inconsistent
halfway powers among known multipliers are impossible, but passing
F10 does not make an arbitrary unit a multiplier or construct D.

## F3: the full relative trace, with all coefficients

For a difference set in this odd group, equality d1+d2=d3+d4 makes
the unordered pairs equal, including repetitions. If d1=d3 this is
immediate. Otherwise d1-d3=d4-d2 is a nonzero ordered difference;
uniqueness gives d1=d4,d3=d2. Division by2 is injective as well.

Let E=D intersect B, F=(1/2)E, and P=beta_*(D) with multiplicities.
Each nonfixed orbit {d,td} contributes coefficient2 to P at its
average, and each fixed e contributes coefficient1 at e. Distinct
orbits/fixed entries have distinct averages by unordered-sum uniqueness.
The convolution F*F has coefficient1 at e for each repeated E pair,
and coefficient2 at the average of each distinct E pair. These averages
are all distinct and cannot overlap a nonfixed orbit average or a
different repeated pair. Thus every coefficient of P+F*F is 0 or2.
Its augmentation is (m^2+1)+(m+1)^2=2|B|, so every one of the |B|
positions must have coefficient2. This proves F11. The convolution
is a SQUARE, not a product with inversion.

It follows that P has values 1 on E, 0 on the binom(m+1,2) distinct
averages of distinct E entries, and 2 on the remaining m(m-1)/2
positions. For a nonprincipal character chi of B, chi(U_B)=0, hence
chi(P)=-chi(F)^2. F is itself an order-m difference set, as the
half-map is an automorphism of B, so |chi(F)|^2=m and |chi(P)|^2=q.
The phase equation is stronger than its magnitude. P is not E.

## F3a: necessary sign assignment and the exact remaining iff

If a nonzero x in A occurred in two different nonfixed fibers, the
two points (x,b),(x,b') would have a nonzero difference in B.
F1 for B forces its unique representing points themselves into B,
contradicting x nonzero. Thus every nonzero x occurs in at most
one fiber. There are 2R=a-1 such point slots, so all nonzero x
occur, giving precisely the sign-pair bijection F13. This necessity
does not make an arbitrary assignment sufficient.

Given E and that bijection, the displayed F14 subset has size q+1,
is 0/1, and is symmetric on each A fiber. Writing its fiber polynomial
as L_b gives the coefficient of delta in DD^(-1) as

    sum_b L_b (L_(b-delta))^(-1)=sum_b L_b L_(b-delta),

because every L_b is inversion-invariant. At delta=0 the singleton
fibers give m+1 identity terms, and double fibers give 2R identity
terms and X^(2f(b))+X^(-2f(b)). The sign bijection and the automorphism
x->2x enumerate every nonzero A element once. Thus that coefficient
is (q+1)*1+(U_A-1)=q*1+U_A automatically.

For each nonzero delta it must be U_A. These are exactly F15, and
together with the already established delta=0 coefficient they are
equivalent to the full original difference-set identity. This proves
both directions of the stated iff, without silently checking only
the augmentations.

For completeness those augmentations really do follow from the trace
data and the smaller difference-set norm. Put b0=|B|, a0=|A|.
Using F F^(-1)=m*1+U_B and P=2U_B-F^2 gives

    P P^(-1)
      =m^2*1+[5b0-4(m+1)^2+2m]U_B
      =q*1+a0 U_B.

Hence the nonzero-delta augmented equations are a0 as claimed.
They leave the individual A coefficients genuinely unconstrained;
F15 retains them. No function-model uniqueness theorem with extra
prime-power hypotheses is used.

## B1: real relaxation and the integrality boundary

For every integer q>=2, set r=sqrt(q), k=q+1 and b=(k-r)/v>0.
The real element A=r*1+b U_G has augmentation r+bv=k and is fixed
by every unit automorphism. Since inversion fixes 1,U_G and U_G^2=vU_G,

    AA^(-1)=r^2*1+(2rb+vb^2)U_G=q*1+U_G,

where 2rb+vb^2=(k^2-r^2)/v=(k^2-q)/v=1. Nonprincipal characters
have magnitude r. Its identity coefficient r+b is greater than1;
it is not a subset indicator. This is a valid real relaxation even
at the excluded 7p orders, and does not refute an integral argument.

Conversely for an integer coefficient vector C with FULL identity
CC^(-1)=q*1+U_G and positive augmentation k=q+1, the identity
coefficient gives sum c_g^2=k while the augmentation gives sum c_g=k.
Thus sum c_g(c_g-1)=0. Every summand is a nonnegative integer,
even for negative c_g, so every coefficient is 0 or1. A quotient,
smaller conductor, altered augmentation or character-magnitude-only
statement does not supply those exact premises. This proves the
claimed integrality boundary.

## Primary-source scope and final disposition

I independently opened the complete original BBB author PDF and read
its applicable Section2 setup, involution argument and Lemmas1–2 with
their proofs on printed pages1–2. They apply to an abelian planar
difference set in a common multiplier-fixed translate, with an actual
involutory multiplier. Those passages do not assume a prime-power
order. The later Desarguesian unital theorem does, and is not imported.
The original Lemma2 is precisely F11 after additive translation.
[Primary full text](https://aeb.win.tue.nl/preprints/hermitian1.pdf).

The candidate's elementary F2 proof and F3 coefficient proof stand on
their own; an original Mann proof or a survey is not substituted for
them. Neither the external complete unital theorem nor a function-model
classification is part of this audit's proof reconstruction. The fresh
web source provides no binary hash, and I do not fabricate one or repeat
the author's stalled native retrieval. Its access limitation is disclosed.

F4 requires the explicit fixed-group correction 2020R2-01. I recommend
a complete versioned author repair retaining the counterexample and
both initial audits, followed by both affected reaudits. The remaining
claims pass the stated mathematical reconstruction, but this report
does not promote them or the full packet. The nonsquare odd-order
multiplier branch, possible permitted fixed subgroup sizes, rational
coefficient/trace lifting obstruction and unrestricted cyclic
prime-power conjecture remain unresolved. No novelty or exhaustive
published-range verification is claimed.

The one-time freeze validates the complete constructor packet, its
declared source/dependency rows, and all 25 older own frozen packets.
Only this review prefix was written. Latest authoritative total weekly
use is 27%, reset1792745187, with90%-total ceiling and integration reserve.
