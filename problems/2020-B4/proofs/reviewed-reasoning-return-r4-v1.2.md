# Accepted repaired R4A--R4E: scope and review history

2026-10-17 UTC. **Proved, independently reviewed scoped partial results, with explicit published theorem imports.**

R4A--R4B give a reconstructed classical planar multiplier collision/Sidon restriction with the exact q=4 exception preserved. R4C explicitly imports Cohen1989 Theorem1 to obtain a mandatory UNIT orbit for the actual normalized difference set outsideq4, and couples it to actual fixed-subplane intersections. Its involution corollary requires an ACTUAL numerical involution; square order alone does not suffice. Cohen's complete sieve proof is an attributed published import, not reconstructed here.

R4D proves that the EXTRA saturated hypothesis |T|>=q forces primev, M=T and a single multiplicative coset or that coset pluszero according to the stated parity. Hall's separately accepted multiplier import gives the exact order-three congruence. No theorem that every relevant order satisfies saturation is supplied. Xia's extra non-Desarguesian flag-transitive hypotheses are not dropped or applied to all cyclicplanes.

R4E proves an elementary exact moment iff for the prescribed saturated subgroup shapes. In the repaired version the final moment B_L=-1 is AUTOMATIC, and the INTERIOR equations alone already suffice: the knownactualzero count allows a square nonzero-residue Vandermonde, then0<=mu(z)<=k<ell lifts the fieldcongruence to integercounts. The L2 empty-list boundary and E5's L>2 condition are retained. This does not solve the unbounded interior system or the nonsaturated branch.

R4R2-01 was a REAL author error: v1 falsely called the last moment essential and earlier tests insufficient. Coordinator root's original wholeR1 missed it; reviewer2 found it independently. The COMPLETE fullv1.1 authorreplacement corrects everyaffected explanation and adds both automatic-row proofs plus the reduced-matrix sufficiency proof. BOTH required affected reaudits independently reconstruct the correction and resolveR4R2-01. Originalv1, both differing wholeinitials, their ledgers/sources, the exact counterargument, the five-file diff and the olderq4 errortrail remain unchanged. This record does not retrospectively amend either initial.

The two original fresh nonconstructor WHOLE initials froze before peer comparison. The two affected reaudits also completed before reading each other's new targeted reports. Root read the FULL original and replacementmain, both COMPLETE originalreports/ledgers/sources and both COMPLETE affectedreports/ledgers/sources, all44replacementobligations, repairledger/worklog/sourceJSON and ENTIREexactdiff. Root oldR3reviewmiss and reviewer2 oldrepairedR3F1/F2authorship are disclosed; this is not a new independent self-review of those older acceptedinputs. No substantive objection remains in the repaired scope.

All mathematical arguments and symbolic moment proofs were hand reconstructed. No mathematical scan,CAS,binomial table,certificate orauthorcomputation was rerun. Text equality andmetadatahashes establishpreservation only. Fulltautclassification/CyclicPrimePowerConjecture, improvedpublishedcutoff, arbitrarycyclicplaneclassification andnovelty remainunresolved. Internal review is not externalvalidation.

The COMPLETE repaired submission follows as a byte-identical suffix. Historical candidate labels record submission status; this header and acceptance record state the current narrow scope. The original erroneousv1 and both original initials remain preserved separately.

---

# Unit orbits, multiplier collisions and a restricted cyclotomic criterion

2026-10-17 UTC. **Candidate proof - unverified, full replacement v1.1.**
Constructor `review_2022_complexity_r2`; requested `gpt-6.1-sol` with `max`
reasoning, independent effective-setting readback unavailable. Both
initially blind nonconstructor WHOLE v1 audits are frozen and preserved.
Reviewer2 correctly found substantive auxiliary error R4R2-01: the author
falsely called the last moment congruence essential. Reviewer1's initial
report missed that assertion. This replacement corrects it, proves the
last row automatic and the earlier rows sufficient, and keeps the entire
valid full E2 iff. Both reviewers must re-audit the affected arguments
before coordinator acceptance. Neither old report is retroactively edited.

Only 2020 B4(b) is investigated. This is a structural partial packet,
not a classification of taut integers. It reconstructs elementary
consequences and explicitly imports Cohen's published generator theorem.
The multiplier bound is classical; cyclotomic difference-set criteria
also have an extensive literature. No novelty or improved published
verification range is claimed. No mathematical program, enumeration,
certificate rerun or CAS was used.

## Exact domain and inputs

Use the accepted B4(b) dictionary and normalization from
`proofs/reviewed-partial-v1.1.md`, whose full original body
`proofs/partial-v1.md` was read. Set

\[
q=n-1\ge2,\quad k=q+1,\quad v=q^2+q+1,\quad G=\mathbb Z/v\mathbb Z.
\]

Assume that an actual subset \(D\subset G\) of size \(k\) represents
each nonzero element of \(G\) exactly once as an **ordered** difference
of two members. This is equivalent to tautness in the accepted dictionary.
The already accepted \(q=1\) boundary is left outside the new lemmas.
The preliminary prime-order existence construction is not reproduced.

A numerical multiplier is a unit \(t\pmod v\) such that
\(tD=D+c\) for some \(c\). All numerical multipliers fix the same
sum-zero translate of \(D\). Indeed \(\gcd(k,v)=1\), so translating
by \(-k^{-1}\sum D\) makes the sum zero. Thereafter summing
\(tD=D+c\) gives \(kc=0\), hence \(c=0\). Use this translate
throughout. Write \(M\) for its full numerical multiplier group and
\(T\le M\) for any known subgroup. Setwise invariance does not mean
pointwise fixedness.

The second accepted input is **F1 only** from the fully repaired
`proofs/reviewed-return-r3-v1.2.md` and its acceptance record. For any
nonidentity subgroup \(U\le M\), let

\[
H_U=G^U,\quad E_U=D\cap H_U,\quad h_U=|H_U|,\quad f_U=|E_U|.
\]

Then \(H_U\) is proper. If \(h_U=1\), \(f_U\in\{0,1\}\).
If \(h_U>1\),

\[
f_U=m_U+1,\quad h_U=m_U^2+m_U+1,\quad
1\le m_U\le\sqrt q.                                  \tag{I1}
\]

These are actual intersections, not quotient occupancies. To recall
the reason: every nonzero \(z\in H_U\) has a unique representation
\(d-e\); applying every \(u\in U\) fixes both representing points.
Thus \(E_U\) is itself a planar difference set. For \(m_U\ge2\)
it embeds as a proper subplane. An external point lies on at most one
extended subplane line; counting the remaining subplane points on
distinct lines through that point gives \(q\ge m_U^2\). For
\(m_U=1\) that bound is automatic. No prime-order orbit congruence
from a larger common fixed subgroup is used here.

When needed, the accepted attributed planar First Multiplier Theorem
says that every prime divisor of \(q\) belongs to \(M\). Its proof
is an external import, not reconstructed in this packet. The new
published import used in R4C--R4D is stated separately below.

## R4A. Two proper individual fixed subgroups cannot cover D, except at q=4

Let \(u,w\in M\setminus\{1\}\). Unless \(q=4\),

\[
D\not\subset G^{\langle u\rangle}\cup
                G^{\langle w\rangle}.                \tag{A1}
\]

For \(q\ge6\), I1, including its \(h=1\) clause, bounds each
intersection with \(D\) by \(\sqrt q+1\). A cover would imply
\(q+1\le2\sqrt q+2\). But \(q-1>2\sqrt q\): both sides are
nonnegative and
\((q-1)^2-4q=q(q-6)+1>0\). This is a contradiction.

For \(q=2,3,5\), the respective moduli \(7,13,31\) are prime.
Every nonidentity unit fixes only \(0\), so two such fixed groups
cannot cover a set of size \(q+1\ge3\). This checks the remaining
integer values without a search.

At \(q=4\), proper subgroup sizes are \(1,3,7\). A cover by two
fixed groups is possible only when they are the distinct groups of
sizes \(3\) and \(7\), the respective intersections have sizes
\(2\) and \(3\), and \(0\notin D\). Indeed either a singleton
group together with a size-seven group covers at most four members;
equal groups cannot supply five; and the two distinct groups
intersect only at zero. The following retained example realizes
this exception, so it cannot be deleted from A1.

Take the already preserved counterexample

\[
q=4,\quad v=21,\quad D=\{7,9,14,15,18\}.
\]

Its ten undirected separations, in pair order
\((7,9),(7,14),(7,15),(7,18),(9,14),(9,15),(9,18),
(14,15),(14,18),(15,18)\), are
\(2,7,8,10,5,6,9,1,4,3\). Thus its actual ordered differences
are all twenty nonzero residues, exactly once. Its sum is zero.
Multiplication by two has cycles \((7,14)\) and \((9,18,15)\),
so \(T=\langle2\rangle=\{1,2,4,8,16,11\}\) preserves it.
Here

\[
\begin{aligned}
G^{\langle4\rangle}&=\{0,7,14\},&D\cap G^{\langle4\rangle}&=\{7,14\},\\
G^{\langle8\rangle}&=\{0,3,6,9,12,15,18\},&
D\cap G^{\langle8\rangle}&=\{9,15,18\}.
\end{aligned}
\]

Their union contains \(D\), although the common fixed group of
all of \(T\) is only \(\{0\}\). This is the accepted R3
counterexample, reused analytically rather than rediscovered by a
scan. It also makes the distinction between individual and common
fixed groups visible in the new proof.

## R4B. The multiplier group is an additive Sidon set for q != 4

Assume \(q\ne4\). If \(t_1,t_2,t_3,t_4\in M\) satisfy

\[
t_1-t_2=t_3-t_4\ne0\quad\text{in }G,                  \tag{B1}
\]

then \((t_1,t_2)=(t_3,t_4)\). Repeated entries in the four-tuple
are allowed; the claim is about ordered pairs with nonzero difference.

Suppose the pairs differ. Then \(t_1\ne t_3\). Put
\(a=t_1-t_2\ne0\) and \(b=t_1-t_3\ne0\). For each
\(d\in D\), either \(ad=0\), or B1 gives the same nonzero
ordered difference

\[
(t_1d)-(t_2d)=(t_3d)-(t_4d)
\]

between members of \(D\). Uniqueness in the latter case forces
\(t_1d=t_3d\), hence \(bd=0\). Consequently

\[
D\subset\ker(a:G\to G)\cup\ker(b:G\to G).
\]

Multiplying by a unit identifies these kernels as the individual
fixed groups of \(t_1t_2^{-1}\ne1\) and
\(t_1t_3^{-1}\ne1\), respectively. R4A is a contradiction.
Thus all \(|M|(|M|-1)\) nonzero ordered multiplier differences
are distinct, giving

\[
|M|(|M|-1)\le v-1=q(q+1),\qquad |M|\le q+1.          \tag{B2}
\]

The exact exceptional group above has the nontrivial collision
\(1-4=8-11=-3\pmod{21}\). The two kernels in this proof have
sizes three and seven; their cover is exactly the displayed one.

B2 is a classical planar multiplier bound, not a new theorem. Gordon
(1994), Theorem 4, records the same order-four exception; the broader
Xiang--Chen bound and Cohen-based argument appear in Gordon (2020).
The proof here uses the already accepted subplane bound, and does not
import a collision criterion as a substitute for its proof. Once
Cohen's theorem below is allowed, a unit member \(d\in D\) also
gives the short classical proof: \(dM\subset D\), and cancelling
the unit \(d\) in a unique ordered difference gives B1 immediately.

## R4C. A compulsory unit orbit and its fixed-subplane complement

**Attributed import.** Cohen, *Generators in Cyclic Difference Sets*,
JCTA 51 (1989), Theorem 1, proves that a cyclic \((v,k,\lambda)\)
difference set with \(1<k<v-1\) contains a residue coprime to \(v\),
apart from the two stated \((21,5,1)\) exceptions. The original
definition and theorem were directly read in the author-uploaded text:
<https://www.researchgate.net/publication/220077727_Generators_in_cyclic_difference_sets>.
This is a published theorem import; its complete character-sum/sieve
proof is not claimed as reconstructed. Both exceptions have \(q=4\).

Hence, throughout the rest of this packet, assume \(q\ne4\), and
choose a **unit** \(d\in D\). The theorem applies to the actual
sum-zero translate: \(q+1<v-1\) for \(q\ge2\), and the parameter
\(q\ne4\) excludes both exceptions. No claim that unit membership
is preserved by arbitrary translations is needed or made.

For any known \(T\le M\) of order \(s\), its orbit
\(O=dT\subset D\) has exactly \(s\) elements, all units. If
\(td=t'd\), cancelling the unit gives \(t=t'\). In particular
the unit stratum in the accepted orbit decomposition cannot be
omitted when choosing an actual \(D\): at least one full such
orbit is present. This is a necessary orbit condition, not a
sufficient way to select difference-set orbits.

More generally let \(U\le M\) be any nonidentity subgroup, not
necessarily contained in \(T\). No unit point belongs to \(H_U\):
a nonidentity element \(u\in U\) could not satisfy \(ux=x\)
with \(x\) a unit. Therefore \(O\cap E_U=\varnothing\), and

\[
s+f_U\le q+1.
\]

If \(h_U>1\), I1 gives the sharper coupled bound

\[
s+m_U\le q,\qquad
m_U\le\min\{\sqrt q,q-s\}.                           \tag{C1}
\]

If equality \(s+m_U=q\) holds in this branch, it forces the
exact disjoint decomposition \(D=dT\sqcup E_U\). It does not
say that an arbitrary such union is a difference set. For \(h_U=1\)
the correct statement stays \(s+f_U\le q+1\), with the actual
membership \(f_U\in\{0,1\}\); no fictitious \(m_U\) is assigned.

For example, conditional on the accepted involution theorem F2 and
the **presence** of a numerical involution, \(q=a^2\), \(a\ge2\),
and its own \(m_U=a\). If \(q\ne4\), every known \(T\)
then obeys \(s\le q-\sqrt q\). A square order alone does not
assert the presence of an involution. Nor may C1 be recursively used
without resetting the group, actual action, unit condition and all
other hypotheses in the smaller difference set.

## R4D. Saturation |T| >= q forces a prime modulus and one coset

Assume \(q\ge2\), \(q\ne4\), and a known \(T\le M\) has
order \(s\ge q\). Then the following are necessary:

\[
\begin{array}{c|c|c|c}
q&v=q^2+q+1& s=|M|&\text{D after multiplication by a unit}\\ \hline
\text{even}&\text{prime}&q+1&T\\
\text{odd}&\text{prime}&q&\{0\}\cup T .
\end{array}                                             \tag{D1}
\]

Here \(T\) in the final column is the corresponding multiplicative
subgroup of \(\mathbb F_v^\times\). This does not assert that every
taut order has a known multiplier group of this size.

Proof. B2 implies \(s\in\{q,q+1\}\), and R4C supplies a unit
orbit \(O=dT\) of size \(s\). Thus there is at most one point of
\(D\setminus O\). For any nonidentity \(t\in T\), no member of
\(O\) can be fixed by \(t\). Hence \(|D\cap H_{\langle t\rangle}|\le1\).
I1 would give at least two such points if that fixed group were
nontrivial. It follows that

\[
\gcd(t-1,v)=1\quad\text{for every }t\in T\setminus\{1\}. \tag{D2}
\]

For each prime \(\ell\mid v\), reduction of \(T\) into
\(\mathbb F_\ell^\times\) is injective. Otherwise two distinct
members \(t,t'\) with the same reduction give
\(tt'^{-1}\ne1\), congruent to one modulo \(\ell\), contrary
to D2. Lagrange's theorem gives \(s\mid\ell-1\), so
\(\ell\ge s+1\ge q+1\). If \(v\) were composite, its prime
factorization, counting multiplicity, would have at least two factors
each at least \(q+1\). This would give
\(v\ge(q+1)^2>q^2+q+1\), a contradiction. Thus \(v\) is prime.

No planar \(D\) of size at least three in an odd group is invariant
under global negation. Choose distinct \(a,b\in D\) which are not
opposites; such a pair exists in a set of at least three. If \(-D=D\),
the equal nonzero differences
\(a-b=(-b)-(-a)\) have distinct ordered representing pairs.
Consequently \(-1\notin M\). A subgroup of the prime-field unit
group with even order contains its unique element of order two,
namely \(-1\), so \(s\) is odd. Of \(q,q+1\), exactly the
value displayed in D1 is odd.

If \(s=q+1\), the orbit is all of \(D\), and multiplying by
\(d^{-1}\) gives \(D=T\). If \(s=q\), write
\(D=O\sqcup\{z\}\). The complement of the invariant orbit
is invariant, so \(z\) is fixed by every member of \(T\).
There is a nonidentity member because \(s\ge2\), and D2 then
forces \(z=0\). Scaling again gives \(\{0\}\cup T\).
Finally \(T\le M\), \(|M|\le q+1\), and \(s\mid|M|\)
force \(M=T\) in either case.

There is a useful additional consequence of the **accepted Hall
multiplier import**. The residue \(q\) belongs to \(M\) because
it is the product of prime-divisor multipliers. It has order exactly
three: \(q^3-1=(q-1)v\) and \(q\not\equiv1\pmod v\).
Thus \(3\mid|M|=s\). The two rows of D1 consequently require

\[
q\equiv2\pmod6\quad(q\text{ even}),\qquad
q\equiv3\pmod6\quad(q\text{ odd}).                    \tag{D3}
\]

In the even row, the accepted plane dictionary also gives a
flag-transitive action: translations are transitive on lines, and
\(T\), which fixes line \(D\), acts transitively on its points
\(dT\). These transformations are collineations since
\(t(D+x)=D+tx\). This puts that row inside the classical
cyclotomic/flag-transitive setting. Xia's discussion is useful
context, but its theorems about **non-Desarguesian flag-transitive**
planes are not imported to eliminate arbitrary cyclic planes or the
odd row here.

## R4E. An exact finite congruence criterion for the saturated shapes

The following is a standalone symbolic iff, with no parameter scan.
Let \(m\ge3\) be odd, let \(\epsilon\in\{0,1\}\), and suppose

\[
\ell=m^2+(2\epsilon-1)m+1\quad\text{is prime}.
\]

Put

\[
k=m+\epsilon,\quad q=k-1,\quad
L=m+2\epsilon-1,\quad \ell-1=mL.
\]

Then \(L\) is positive and even. Let \(H\) be the multiplicative
subgroup of order \(m\) in \(\mathbb F_\ell^\times\), and set
\(D_0=H\), \(D_1=H\cup\{0\}\). The unit group is cyclic,
so this subgroup exists and is unique. For even \(t\) with
\(2\le t\le L\), define the integer

\[
B_t=2m(m+\epsilon)+m^2\sum_{i=1}^{t-1}
             (-1)^i\binom{tm}{im}.                    \tag{E1}
\]

The subset \(D_\epsilon\) is a cyclic planar difference set
of parameters \((\ell,k,1)\) **if and only if**

\[
\begin{cases}
B_t\equiv0\pmod\ell & (2\le t<L,\ t\text{ even}),\\
B_L\equiv-1\pmod\ell.&
\end{cases}                                           \tag{E2}
\]

The final congruence is AUTOMATIC for every actual size-\(k\) subset
of \(\mathbb F_\ell\), before imposing any earlier congruence. It is
included in E2 to display the full target moment sequence. For these
prescribed \(D_\epsilon\), the earlier even-index congruences alone
are already sufficient; the proof below also establishes this shorter
criterion. Redundancy does not change the final target value from
\(-1\) to zero. The index \(m\) here is the **order** of the
multiplicative subgroup. Its usual cyclotomic index is \(L\), so
source notation using the index must not be substituted blindly.

Proof. Work first in \(\mathbb F_\ell\). Define the zeroth
power sum by \(S_0=k\), without assigning a value to \(0^0\),
and for \(j>0\) let \(S_j=\sum_{a\in D_\epsilon}a^j\).
Summing powers over the cyclic group \(H\) gives

\[
S_j=\begin{cases}m&m\mid j,\\0&m\nmid j,\end{cases}
\quad j>0.                                             \tag{E3}
\]

Indeed a generator of \(H\) turns the sum into a geometric
series; \(m\ne0\) in the field because \(m<\ell\).
The possible zero member contributes zero to positive powers.

Let \(\mu(z)\) be the **integer** number of ordered pairs
\((a,b)\in D_\epsilon^2\) with \(a-b=z\). For positive
\(j\), the difference moment in the field is

\[
M_j=\sum_{a,b\in D_\epsilon}(a-b)^j
   =\sum_{h=0}^j(-1)^h\binom jh S_{j-h}S_h.             \tag{E4}
\]

If \(m\nmid j\), every term vanishes: an endpoint contains
\(S_j=0\), while two positive nonzero power sums would require
both \(h\) and \(j-h\) divisible by \(m\). If \(j\) is odd,
\(M_j=0\) by pairing \((a,b)\) and \((b,a)\), in odd
characteristic. These cover all positive indices except
\(j=tm\) with \(t\) even. At such an index the two endpoints
of E4 give \(2mk\); its interior nonzero terms have \(h=im\).
As \(m\) is odd, their signs are \((-1)^i\), and E4 is exactly
\(M_{tm}=B_t\). This proves all moment formulas for every
\(1\le j\le\ell-1\), including the last index.

The target perfect-difference counts are \(\nu(0)=k\) and
\(\nu(z)=1\) for nonzero \(z\). Their positive moments are
zero for \(1\le j<\ell-1\), and minus one at \(j=\ell-1\),
by the geometric power sums over \(\mathbb F_\ell^\times\).
Their constant moment is \(k+\ell-1=k^2\), because
\(k(k-1)=mL=\ell-1\). This is also the constant moment of
\(\mu\). Equations E2 are therefore equivalent to equality
of **all** moments of \(\mu\) and \(\nu\) at indices
\(0,1,\ldots,\ell-1\).

The \(\ell\)-by-\(\ell\) evaluation matrix
\((z^j)_{0\le j\le\ell-1,\ z\in\mathbb F_\ell}\), with
the zeroth row defined to be all ones, is invertible. For example,
a polynomial of degree at most \(\ell-1\) vanishing at all
\(\ell\) field elements is zero, which proves independence of
its rows. Consequently E2 gives
\(\mu(z)\equiv\nu(z)\pmod\ell\) separately at every residue.

This field statement lifts to the required integer counts in this
particular setting. Distinct members give \(\mu(0)=k\) exactly.
For \(z\ne0\), each second member \(b\) permits at most one
first member \(a=b+z\), so \(0\le\mu(z)\le k<\ell\).
The only integer in that interval congruent to one is one. Thus
every nonzero difference occurs exactly once. Conversely such an
actual difference set has all the target moments, hence E2. This
completes the iff, rather than just a necessary field relaxation.

**Automatic final row and sufficient interior list (R4R2-01 repair).**
For ANY actual subset \(A\subset\mathbb F_\ell\) of size \(k\)
with \(k(k-1)=\ell-1\), Fermat's theorem gives

\[
\sum_{a,b\in A}(a-b)^{\ell-1}
  =\#\{(a,b)\in A^2:a\ne b\}
  =k(k-1)=-1\quad\text{in }\mathbb F_\ell.             \tag{E2a}
\]

The diagonal contributes zero and every off-diagonal field summand is
one. In particular \(B_L\equiv-1\pmod\ell\) holds for the actual
\(D_\epsilon\), independently of every preceding test. There is also
a direct check of its formula: for \(1\le i\le L-1\),

\[
\binom{\ell-1}{im}\equiv(-1)^{im}\pmod\ell,
\qquad (-1)^i(-1)^{im}=1
\]

because \(m\) is odd. Thus

\[
B_L\equiv2mk+m^2(L-1)
      =(m+1)\ell-1\equiv-1\pmod\ell.                 \tag{E2b}
\]

The intermediate integer identity uses the exact definitions of
\(k,L,\ell\); no earlier moment equation is used.

For completeness, sufficiency can be recovered WITHOUT using the last
moment at all. Suppose the interior equations \(B_t=0\) for even
\(2\le t<L\) hold. E3/E4 and odd-pair cancellation give all positive
moment equalities at \(1\le j\le\ell-2\), and the constant moments
are already equal. Also \(\mu(0)=\nu(0)=k\) EXACTLY for the actual
subset. Delete this known zero coordinate. The remaining square matrix

\[
(z^j)_{0\le j\le\ell-2,\ z\in\mathbb F_\ell^\times}
\]

is invertible: a polynomial of degree at most \(\ell-2\) with all
\(\ell-1\) distinct nonzero roots is zero. Consequently the count
vectors agree modulo \(\ell\) at each nonzero residue, and the same
bound \(0\le\mu(z)\le k<\ell\) lifts the count to the integer one.
Necessity of the interior equations follows from an actual difference
set as before. Therefore E2 is equivalent to its interior list alone,
including an empty interior list when \(L=2\). This is a correction
of the false v1 necessity/insufficiency assertion, not an unproved
new external import. The full-matrix proof and full E2 list above remain
valid with the redundant last row retained.

When \(L>2\), the first interior congruence \(t=2\) yields

\[
\binom{2m}{m}\equiv2+\frac{2\epsilon}{m}\pmod\ell.      \tag{E5}
\]

Division by \(m\) is legitimate in the prime field. When
\((m,\epsilon)=(3,0)\), \(L=2\) and this index is instead
the **final** congruence \(B_2=-1\); E5 must not be used there.
No small prime-order example or existence construction is verified
in this packet. For the actual saturated branch D1, set
\((m,\epsilon)=(q+1,0)\) in the even case, and \((q,1)\)
in the odd case. D3 additionally forces \(3\mid m\).

As a corollary using the accepted Hall theorem, if \(3\nmid m\)
then the full E2 system cannot hold: its sufficiency would give an
actual difference set with multiplier subgroup \(H\) of order
\(m\ge q\), outside \(q=4\), and D3 would force \(3\mid m\).
This corollary does not simplify or solve E2 for \(3\mid m\).

## What the packet does and does not settle

R4A--R4B give a direct fixed-subplane proof of a classical collision
restriction, with its exact counterexample. R4C couples one compulsory
unit orbit to **actual** fixed intersections. R4D identifies the
saturated known-multiplier branch, and R4E gives its full finite-field
moment test with an explicit integer lifting step. These remain
candidate partial claims pending BOTH affected v1.1 re-audits and
coordinator reconciliation; both original whole initials stay preserved.

Cohen's theorem is stronger than R4A as a noncoverage statement:
a unit cannot lie in any proper subgroup of a cyclic group. The
initial hope that a two-subgroup argument supplied an unrecorded
general obstruction therefore did not survive the literature check.
Its elementary reconstruction and the coupled criteria are retained
for their precise hypotheses and proof architecture, with no claim
of mathematical originality. Gordon, Cohen, Baumert--Gordon and Xia
provide the relevant classical context; the companion source audit
separates direct theorem reads, proof passages and unused material.

There is no proof that an arbitrary non-prime-power order has
\(|M|\ge q\). The accepted odd-order \(q=2435\) record is an
explicit reminder that a known multiplier group may be much smaller;
that recorded computation is not rerun. Proper-subplane descent can
also be unavailable when the modulus is prime. The system E2 may be
nontrivial even in the narrow saturated branch, and the broader
cyclotomic nonexistence questions are not treated as established
theorems. For the prescribed shapes here the interior E2 list IS
sufficient, because the omitted final row is automatic and the actual
zero count is known, as proved above. A different shortened moment
list, an orbit-size subset sum, or a real norm identity is not promoted
to existence without a valid reconstruction argument of its own. No
full taut classification, cyclic prime-power conjecture, numerical
answer or new published cutoff follows from this packet.
