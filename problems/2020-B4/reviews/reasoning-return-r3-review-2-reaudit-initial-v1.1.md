# 2020 return R2: complete affected reaudit of v1.1

2026-10-17 UTC. Reviewer `review_2021_reasoning_j15_r2`; requested
`gpt-6.1-sol` / `max`, verified effective settings unavailable.

**Recommendation:** close issue **2020R2-01 for v1.1 only**. The full
replacement repairs both F4 clauses, explicitly resets recursive
restricted-action hypotheses, and preserves the actual counterexample
to frozen v1. No new substantive defect was found in the affected
arguments or their downstream uses. This recommendation is not
coordinator acceptance. Both affected reaudits remain required.

I did not construct the repaired candidate. I supplied the original
common-T versus individual-t objection in my initially blind whole R2
audit; the author wrote the full repair. I read no new peer targeted
review or findings before this complete reaudit freeze. My original
whole report, issue ledger, source checks and manifest remain unchanged,
including the objection and counterexample. The first original audit's
historical disposition is also preserved without retroactive revision.

## Exact records and complete-reading scope

Full new main: `notes/reasoning-return-r3-candidate-v1.1.md`, 19010 bytes,
SHA-256 `f6f9947b8140f9d4bafc01ec24bf68dcd7634df5ccba655f4e6cdab334bef467`.
Eight-artifact author freeze: SHA-256
`807827ddb14ace9a98f0c9f8bf7f63244129414d0a85cfcde4889ff84d7aa806`.
Complete repair ledger: SHA-256
`12fabe3054a308bbb578bf59cdf9696f835eb5092558d8f2a90f2dc6cd678877`.

I read the full replacement, repair ledger, complete exact diff,
worklog and source record, and the saved administrative builder and
freeze script. I reread my complete original report and source checks,
then traced every common-fixed-subgroup and individual-action use in
the complete new main. The accompanying administrative freeze independently
recomputes the exact original-to-replacement unified diff without
executing the author's builder. It validates the eight new artifacts,
the old main and original records, both original audit manifests and
the author-declared preserved dependencies. New peer targeted findings
are not among the read inputs.

Only B4(b), with q=n−1>=2, is in scope. The accepted difference-set
equivalence, common sum-zero translate and prime-divisor multiplier
input are unchanged. The preliminary construction and q=1 boundary
are not revisited. All multipliers used below fix the same D setwise,
not each member pointwise.

## Reconstruction of both corrected F4 clauses

The arbitrary common subgroup assertion F1 remains valid: if
H=G^T and nonzero z in H has unique representation d−e, then every
t in T takes (d,e) to another representation of z. Uniqueness forces
each representing point to be fixed by every t. Thus E=D intersect H
is an actual difference set in H and f(f−1)=h−1. This is not a
quotient projection statement, and it requires no group-order
coprimality between T and G.

For F4 the replacement now explicitly introduces an individual known
multiplier t of prime order ell and defines

    H_t=G^<t>, E_t=D intersect H_t, h_t=|H_t|, f_t=|E_t|.

All t-orbits on D have size one or ell. The singleton orbits are
exactly E_t. Hence q+1=|D| is congruent to f_t modulo ell.
Applying F1 to exactly T=<t> gives, when h_t>1,
f_t=m_t+1 and h_t=m_t²+m_t+1. Subtracting one from both sides of
the orbit congruence gives q−m_t divisible by ell. The m_t=1,
h_t=3 boundary is allowed; no nondegenerate subplane is needed there.

When h_t=1 the subgroup is {0}; f_t is exactly the indicator of the
actual membership 0 in D. The second clause q+1 congruent to f_t
modulo ell is therefore also valid. That indicator is shared by
every element with this trivial fixed subgroup in the same normalized
D. It is not an independent binary choice at each test. No m_t is
assigned in the h_t=1 case, avoiding an empty-set descent.

The replacement explicitly forbids substituting the smaller common
H=G^T from a larger group containing t. It asserts no analogous
prime-order congruence for |D^T| merely from t in T. This removes
the exact false quantifier in original v1, in both clauses rather
than only in the displayed h>1 equation.

## Exact retained counterexample and corrected values

The repair preserves the actual normalized example

    q=4, v=21, D={7,9,14,15,18}, T=<2>.

I checked the displayed ten separations by hand. In lexicographic
pair order they are 2,7,8,10,5,6,9,1,4,3, exactly 1 through 10.
Since v is odd, the twenty ordered differences are exactly all
nonzero residues. Thus this is an actual difference set, not a
quotient occupancy vector. Its sum is 63=0 modulo 21.
Multiplication by 2 cycles (7,14) and (9,18,15), and its powers
are 2,4,8,16,11,1. It fixes this same D setwise and has order six.
The common fixed subgroup has size gcd(21,2−1)=1 and f=0.
The original v1 congruence would give 5=0 modulo 2 for t=8,
and 5=0 modulo 3 for t=4. Both are false.

The individual groups in the repair are precisely

    H_8={0,3,6,9,12,15,18}, E_8={9,15,18}, f_8=3, m_8=2;
    H_4={0,7,14}, E_4={7,14}, f_4=2, m_4=1.

Indeed their sizes are gcd(21,7)=7 and gcd(21,3)=3.
The unit 8 has order two; 4 has order three. The corrected
congruences give 5=3 modulo 2 and 5=2 modulo 3, equivalently
q−m_8=2 and q−m_4=3. These use the same D and the same absence
of zero. The example both refutes the frozen general-T version and
satisfies the repaired individual-t version. No search, preliminary
existence construction or routine enumeration was used.

## Recursive use and all affected downstream arguments

The new recursive-use sentence requires every hypothesis to be reset
inside the actual subgroup H, especially the order of the restricted
action and that action's own fixed subgroup. Restricting an original
prime-order automorphism can produce the identity, so one cannot retain
its original order by notation. A genuine E with unique differences
permits reapplication only after these hypotheses are met. A quotient
image need not have that property. Empty/trivial intersections do not
acquire a fictitious smaller plane. The replacement asserts no stronger
automatic recursive action statement.

F1's common-fixed closure, gcd formula, proper subplane embedding and
q>=m² bound do not use F4. Their original proof remains: representing
points are fixed by every t, and the external-point incidence count
bounds the proper embedded plane. The h=1 and m=1 exceptions remain
explicit. No repair is needed in those assertions.

F1a now expressly uses T=<p> for a prime integer divisor p of q.
Its automorphism order need not be prime. The equation
h=gcd(p−1,u²+u+1) follows from F1 and the cyclic annihilator, not
from a prime-order orbit count. Thus the obstruction at h=19 for
p=20 modulo 57, the stated order-7p family and the single hand prime
certificate p=761 remain valid. This repaired invocation does not
reintroduce the error through the word "prime" applied to p.

F2 now expressly applies F1 to T=<t> for its one exact involution.
B is ker(t−1), and the projections alpha=(1−t)/2 and beta=(1+t)/2
give the actual direct sum with A=ker(t+1). The symmetric-fiber
argument gives 2R=|A|−1; the fixed intersection has size s+1 and
|B|=s²+s+1. Counting yields |A|=q−s+1 and
(q−s)(q−s²)=0. The identity case is excluded, so q=s². The
coprime factors q−s+1 and q+s+1 give the same exact involution
t=s³ modulo v. None of these equations counts orbits of a larger
common group. The nonsquare odd-order consequence therefore survives.

F2a uses the unique involution just proved. In its abelian multiplier
group the 2-primary subgroup is cyclic. For each even-order element
its halfway power has local value −1 exactly where the local order
has full 2-part. Comparing with the same involution gives F10 on the
two coprime factors. It does not insert a common fixed cardinality
from another group or confuse one local order with the full order.

F3 continues to use E=D intersect B for this same specified involution,
and P=beta_*(D) retains multiplicities. Unordered-sum uniqueness and
the augmentation count prove P+((1/2)E)*((1/2)E)=2U_B coefficientwise.
Neither its trace identity nor its phase conclusion uses F4.

F3a now expressly invokes F1 with T=<t> when a nonzero difference
lies in this involution's B. Its unique representing points would
then be fixed by that involution, excluding repetition of a nonzero
A coordinate in two fibers. The sign-pair bijection follows by the
existing count, but an arbitrary bijection is still not sufficient.
The delta=0 coefficient follows from that bijection and the doubling
automorphism of A; every nonzero-delta equation F15 retains every
A coefficient. Thus the full coefficientwise iff, rather than only
its quotient augmentation, is preserved by the correction.

B1 uses no fixed subgroup: its real norm example still has augmentation
q+1 and exact product q*1+U_G while failing the 0/1 condition. Its
separate integer recovery still follows from
sum c_g(c_g−1)=0 with nonnegative integer summands. Nothing in the
repair weakens those exact full-group-ring premises. The final
prime-v/odd-order barrier remains a statement of unresolved scope,
not a universal exclusion through F4.

## Source and preservation disposition

There is no new theorem or source import. The original BBB Section2
involution/trace hypotheses and attribution are unchanged. In my
frozen original whole audit I independently read the complete applicable
primary setup and proofs on printed pp1–2, while reconstructing the
candidate's elementary alternative proofs. Those passages concern an
individual involution, not an arbitrary common multiplier group.
The unrelated later Desarguesian theorem, original Mann proof and
Huang–Schmidt uniqueness results remain unused. The raw BBB PDF byte
hash remains unresolved; this review does not fabricate one or repeat
the stalled native download. Its full source-audit record is preserved.

No mathematical code, CAS, broad scan, author mathematical program,
charge, contact or access bypass was used. Only this new versioned
reaudit prefix was written. The freeze verifies the exact diff and
the byte preservation of all declared earlier inputs and 29 older own
packets. Latest authoritative total weekly use is 28%, reset
1792745187, below the 90%-total ceiling with integration reserve.

All 18 targeted ledger checks pass. I recommend resolving 2020R2-01
for v1.1, retaining the failed v1 and both original audits as historical
records. This provides scoped structural restrictions and barriers;
the full cyclic prime-power classification and official B4(b) remain
unresolved. Only root may decide promotion after both targeted audits.
