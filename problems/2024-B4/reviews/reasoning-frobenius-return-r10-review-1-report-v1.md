# FR10 OTHER whole audit 1 — root

18 October 2026 UTC. **Initial whole review, findings EMBARGOED until
BOTH ENTIRE reviews are frozen, fully read back and separately verified.**
This is an independent audit of the ENTIRE13-file FR10 submission and
ALL64 obligations. C constructed the NEW mathematics and is excluded.
Root received constructor progress summaries but supplied no NEW FR10
inference. Its unrelated degree-gap exploration was not used by C.
Root's older CG/R4/R5 construction and R6/R9 review roles are disclosed;
the accepted inputs retain their old authority, not a newly independent
self-recertification. Requested inherited gpt-6.1-sol/max; effective
setting readback unavailable. No NEW review2 path/content/hash/inventory
or findings has been accessed, and no author conclusion substitutes for
this reconstruction.

## Independent mathematical reconstruction

Use exactly n=ell*q+1, ell odd>=3, q=2^i with i>=2, d=gcd(ell,q-1),
N=ell*q-2 over K=F2bar. This makes q the maximal power in n-1 and
wt(n)>=3. General accepted R6B/C therefore supplies reducedness and
degree>=q for EVERY absolute component, not just a component at the
center. Root freshly read the complete accepted R6 and R9 bodies and
EACH current authority MD/JSON. R9 is comparison context, not a new J
hypothesis. The historical T1 no-line premise is retained through R6C;
this audit does not falsely claim a new complete T1--T4/source audit.

Here is the potentially dangerous local step. If F has leading x^q
and squarefree next form H of degree q+1, any actual split F=UV through
the point has initial forms scalar powers x^u,x^v, u+v=q. The next
product form is divisible by x^min(u,v). If x does not divide H the
split cannot meet; if x divides H, squarefreeness forces min(u,v)=1.
Choose V_1=x, so V is smooth and formal coefficient induction solves
V(h(y),y)=0 with ord h>=2, including h=0. Formal difference division
gives V=(x-h)*unit. The simple x factor of H gives a nonzero xy^q
coefficient gamma. On this branch F_x has leading gamma*y^q:
the derivative of x^q is zero; every other differentiated term has
strictly greater y order. F_x=UV_x on V=0 and V_x is a unit. Thus
U(h(y),y) has EXACT order q, not merely order at least q. The finite
local quotient agrees with its formal completion because a power of
its maximal ideal vanishes, and finite truncations/units agree. Hence
the local intersection is EXACTLY q. Global irreducibility of the
complement is unnecessary. This verifies an upper bound independently
of the usual lower intersection bound and does not infer unibranchness
from a single tangent.

At an affine R-unit component intersection set c=a+b+1. Vanishing
partials gives equal ell-th powers of a,b,c; none is zero. F=0 and
a+b+c=1 give the common ell-th power1. R-unit then makes a,b,c,1
distinct. The q and q+1 Taylor forms in the submission follow directly
from (a+x)(a^q+x^q)^ell. In the next form Cx^(q+1)+D(x^qy+xy^q)+Ey^(q+1),
the derivative matrix has determinant CE+D²=1/(abc)^q, nonzero. Thus
H is squarefree. If the q form is nonzero the preceding local lemma
applies to F=RUV by absorbing the local unit R. If it is zero, equal
(q-1)-st powers give a=lambda*c,b=mu*c with lambda,mu in F_q. The
normalization (lambda+mu+1)c=1 forces c, and hence a,b, into F_q.
The ordinary points are therefore EXACTLY the normalized quadruples
in mu_d. The apparently extra unnormalized ratio case in a source table
is not imported or declared a source defect.

For a fixed a!=1 in mu_s the ELIGIBLE subset of mu_s\{1,a} consists
of those b for which c=a+b+1 is also an eligible distinct root. This
subset, not the entire ambient mu_s, is preserved by b<->c. It has no
fixed point and even cardinality, at most s-3 since s-2 is odd.
Thus M_s<=(s-1)(s-3), with M_1=0 separately. Ordinary off-diagonal
points have coprime tangent subproducts in any actual split, giving
intersection at most floor((q+1)^2/4)=q(q+2)/4. All other off-diagonal
points contribute either zero or exactly q. No point/orbit is counted
after a projective/Frobenius quotient.

On each diagonal, away from the center, differentiating the exact
polynomial identity F=R*phi in a transverse direction gives
phi(b,1,1)=(b^ell+1)^q/(b+1)^2. Thus only b in mu_ell\{1} occurs.
The displayed translated denominator v[(b+1)^2+(b+1)v+u²+uv]
is correct. If b is outside F_q the quotient has initial v^(q-1)
and a nonzero pure u^q term next: the degree2 denominator correction
only alters a pure v^q coefficient. Consequently two factors cannot
meet there. For b in F_q the initial form is proportional to
u^q+u*v^(q-1)+(1+b)v^q. At v=1 its derivative in u is1, and the
u^q coefficient excludes a missing direction at v=0. It has q distinct
tangents. There are 3(d-1) such distinct points; their combined split
intersection is at most 3(d-1)q²/4. At the center the exact uv(u+v)
division gives (u^(q-1)+v^(q-1))/(u+v), degree q-2 with q-2 distinct
tangents, giving at most (q-2)²/4. A factor may miss any such point.

There is no infinity contribution. At Z=0,R!=0 the derivative F_Z
is (X+Y)^(n-1)!=0, and at a point of phi the identity gives
R*phi_Z=F_Z. A common zero of two factors would have all homogeneous
partials zero. At the three R-zero infinity vertices, the local
linear numerator and denominator coincide and give quotient value1.
The explicit (1:1:0) chart works as printed. Together these arguments
exhaust all possible component intersections, including those on R=0.

Choose a least actual absolute component U of degree e and the FULL
complement V. Reducedness makes them coprime, q<=e<=N/2, and
e(N-e)-q(N-q)=(e-q)(N-e-q)>=0. Projective Bezout applies in char2 to
this same pair, including a reducible V. The independently checked
upper total is

    B=(q-2)^2/4+3(d-1)q²/4+q*M_ell+q(q-2)*M_d/4.

Both coefficients used for the M replacements are nonnegative. Hence
4[q(N-q)-B_upper] is precisely

    (4ell-d²+d-5)q²-[4(ell-2)²-2(d-1)(d-3)]q-4=P.

Reducibility forces P<=0; P>0 gives WHOLE absolute irreducibility,
not merely the existence of an absolute component. Reducedness also
excludes a nontrivial power of a single component.

For d=1 and q>=ell-1 the coefficient bracket is at least7ell-11,
giving P>=q(7ell-11)-4>0. For d=3, ell is a positive odd multiple3.
For ell>=9 the bracket is at leastell-5>=4; for ell3, P=q²-4q-4,
positive for all powers q>=8, but not for q4. Thus the exact n13
exception is retained. The two small-gcd families have respectively
d=gcd(2^s,q-1)=1 and d=gcd(6,q-1)<=3, with the printed ell>=3 bounds.

For ell35, i=6t+3,t>=1, one has q>=512, d7 and
P=93q²-4308q-4>0 since already at real q47 the bound is2957.
The NF4/J failure witness is genuine: a coset b+V of a two-dimensional
F2 subspace of F8, with b outside V, has four distinct nonzero roots
of mu35 summing0. Because q=1 mod7, delta=q²-q+1=1 mod7, the same
four delta powers sum0. Also ord35(2)=12, gcd(i,12)=3;35 is not a
power-of-two-minus1 and wt(35q+1)=4. These are literal distinctions
from R6D/R7/R8/R9 hypotheses, not a published novelty claim. An F2
factorization, even with nonhomogeneous integer lifts, would contradict
whole absolute irreducibility. No conclusion is obtained for every odd
n, P<=0, q2,ell1,n1/n3, or the exact ordinary reducibility classification.

## ALL64 independent dispositions

Every row is PASS in the exact submitted scope. These are independent
hand dispositions, not a copied constructor verdict or a partial review.

|ID|Independent disposition|
|---|---|
|01|PASS: official page2 B4(b) asks coefficientwise factorization; whole absolute irreducibility supplies a restricted negative answer.|
|02|PASS: odd ell gives maximal q=2^v2(n-1); d exactly gcd(ell,q-1), i>=2.|
|03|PASS: wt(ell)>=2 and the new bit0 is disjoint, so wt(n)>=3.|
|04|PASS: nonzero homogeneous quotient degree N=ell*q-2>=10, not a finite-field function.|
|05|PASS: complete current R6 body/authority freshly read; its reducedness has every odd n>=3 scope.|
|06|PASS: R6C says every component/divisor has degree>=q under this weight, not only a central component.|
|07|PASS: C old authorship and root old roles disclosed; no independent self-recertification.|
|08|PASS: fresh complete operative Fulton proofs are algebraic in char2 and allow reducible complements.|
|09|PASS: nonzero leading L^q and squarefree degree(q+1) are established before using the local lemma.|
|10|PASS: binary-form unique factorization forces both actual initial cones to powers of L.|
|11|PASS: degree(q+1) product term is divisible by L whenever both local orders are positive.|
|12|PASS: squarefreeness allows exactly one L factor in H when it divides H.|
|13|PASS: positive local orders add to q, and min must be1, giving1,q-1.|
|14|PASS: V_1=x makes the formal implicit coefficient recurrence have coefficient1 and h order>=2.|
|15|PASS: difference division yields V=(x-h)*unit; the quotient is K[[y]].|
|16|PASS: finite local length makes completion harmless by identical finite truncations and units.|
|17|PASS: gamma*x*y^q has gamma!=0, while derivative x^q vanishes.|
|18|PASS: every other differentiated term has greater y order after x=h, including h=0.|
|19|PASS: V_x is a unit on its smooth branch; exact orderq of F_x gives exact local lengthq.|
|20|PASS: unit absorption, linear coordinates and a reducible actual complement preserve the argument.|
|21|PASS: any R-unit common factor point gives f=f_x=f_y=0.|
|22|PASS: a zero among a,b,c forces all zero by the partial equations, contradicting c=a+b+1.|
|23|PASS: common ell-th power u gives f=u^q+1, hence u1 by injective Frobenius.|
|24|PASS: R-unit exactly excludes the possible pair equalities; the converse equations follow directly.|
|25|PASS: expansion (a+x)(a^q+x^q)^ell gives the gap and q/q+1 coefficients1.|
|26|PASS: a^(ell*q+1-q)=a^(1-q), and the next coefficient a^-q; mixed coefficients match.|
|27|PASS: differentiating in char2 gives Cx^q+Dy^q and Dx^q+Ey^q.|
|28|PASS: CE+D²=(a+b+c)^q/(abc)^q=1/(abc)^q.|
|29|PASS: no nonzero vector kills both partials; a repeated linear factor would do so.|
|30|PASS: R local unit is absorbed; shared tangent is counted with exactq rather than discarded.|
|31|PASS: zero q form is exactly equal (q-1)-st powers of a,b,c.|
|32|PASS: normalized sum1 forces c into F_q after the two ratios, not merely ratio membership.|
|33|PASS: precisely the mu_d quadruples have zero q form and squarefree orderq+1 cone.|
|34|PASS: M_s counts each ordered affine (a,b) once with c determined; no orbit division.|
|35|PASS: eligible subset has fixed-point-free b/c involution, hence even size<=s-3.|
|36|PASS: M1=0 separately and M3=0; the uniform product formula is0 at d1.|
|37|PASS: squarefree H partitions into disjoint tangent subproducts for the actual pair.|
|38|PASS: max integer product with sumq+1 is q(q+2)/4 for even q.|
|39|PASS: transverse coefficient in exact f=Rphi gives diagonal value, excluding other b.|
|40|PASS: direct multiplication gives v[(b+1)²+(b+1)v+u²+uv].|
|41|PASS: exact specialized Taylor forms give both u^qv and uv^q coefficients b^-q.|
|42|PASS: b outside F_q makes the leading coefficient nonzero, quotient orderq-1.|
|43|PASS: denominator w2 correction cannot cancel the nonzero pure u^q next coefficient.|
|44|PASS: two initial v-powers would force the next product form divisible by v, impossible.|
|45|PASS: b in F_q makes orderq and the displayed initial cone with coefficient1+b.|
|46|PASS: v1 polynomial derivative1 gives distinct finite directions; u^q excludes direction v0.|
|47|PASS: exactly3(d-1) distinct noncentral ordinary diagonal points, each maxq²/4.|
|48|PASS: exact central uv(u+v) cancellation produces degreeq-2 tangent quotient.|
|49|PASS: q-1 odd gives distinct root ratios; remove ratio1 once and neither axis occurs.|
|50|PASS: complementary local orders sumq-2 and cones are disjoint, allowing one local order0.|
|51|PASS: nonzero homogeneous Z derivative on Z0,Runit excludes a component intersection.|
|52|PASS: each infinity vertex has quotient value1; explicit charts cover all three.|
|53|PASS: affine R-unit, diagonal/center, and infinity analyses exhaust the locus.|
|54|PASS: least absolute component and full complement are homogeneous actual coprime factors by reducedness.|
|55|PASS: q<=e<=N/2 and (e-q)(N-e-q)>=0 give the claimed SAME-pair lower bound.|
|56|PASS: projective Bezout applies to precisely this actual coprime pair over K.|
|57|PASS: counts and local bounds give center+3(d-1)diagonal+q(Mell-Md)+q(q+2)Md/4.|
|58|PASS: combine off-diagonal terms before replacing BOTH nonnegative-coefficient M counts.|
|59|PASS: exact coefficient expansion gives P; only necessary reducibility/contrapositive is claimed.|
|60|PASS: d1 bound uses7ell-11 and strict q(7ell-11)-4>0 in whole range.|
|61|PASS: d3 ell>=9 and ell3 separated; q4,ell3 deliberately gives no contradiction.|
|62|PASS: both parametric gcd identities and positive odd ell/maximal-q bounds verified by hand.|
|63|PASS: ell35,d7 polynomial positive; F8 coset and exact order/binary checks establish old-hypothesis failures.|
|64|PASS: official consequence and all unread-source/priority/annual/endpoint limits explicit; no new root construction input.|

## Issue ledger

Eight closed scope notes, zero unresolved substantive defects, zero
required repairs. A substantive flaw later found requires versioned
author repair and BOTH affected whole reaudits; this initial is not
coordinator acceptance.

1. **Closed: one tangent.** It allows a1/(q-1) split. Exact derivative
   contact q pays for it; no unibranch assumption is made.
2. **Closed: completion.** Coprimality gives finite local quotient, so
   formal and polynomial length agree through a finite truncation.
3. **Closed: normalized fixed field.** Ratios alone are not substituted
   for coordinates; a+b+c=1 supplies the required field membership.
4. **Closed: eligible involution.** The invariant set is the eligible
   subset, not all mu_s; its ambient set has odd size s-2.
5. **Closed: denominator jets and infinity.** The pure u^q coefficient
   survives correction, and homogeneous Z differentiation is sufficient
   even though a different affine-chart gradient could be chosen.
6. **Closed: least component and budget.** EVERY-component lower bound,
   same full complement, reducedness and positive count coefficients
   are all explicit. No product genus or equal-degree grouping occurs.
7. **Closed: scope.** P<=0 has no converse; n13 is retained; ell35
   distinguishes reviewed hypotheses only. Whole reducibility over F2
   is ruled out in the proved range, not classified in general.
8. **Closed: publication/access.** Classical ingredients are attributed,
   original inaccessible Jedlicka/Ferard bodies remain unread by root,
   and overlap/priority remain open. Accepted input review roles do not
   become a fresh independent foundation audit.

## Primary reads and literal limits

Fresh exact [official2024 PaperB](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf)
page2 setup/(b)/coefficient definitions, returned57--74; local statement
complete. Other returned contest text was not researched.

Fresh COMPLETE operative [Fulton](https://math.stanford.edu/~conrad/145Page/handouts/algcurves.pdf)
Section3.3 properties1--7, Theorem3 with whole uniqueness/existence and
lemma proof, returned2419--2624, and returned2657--2673 properties8/9;
Section5.3 Bezout and ALL three proof steps3829--3924; complete AppendixA
7557--7598. These proofs justify the char2 local length/tangent equality
and global degree product for coprime possibly reducible curves. They
do not import the book's char0 Hessian/generic-tangent results. No
complete129-page foundational audit is claimed.

Fresh [Hernando--McGuire v4](https://arxiv.org/pdf/0903.2016v4)
Section3 and4, returned247--530, including the supplied local forms,
Lemmas4--7, tables and intersection context/Lemma9. Classical next-form
squarefreeness and quadruple-count attribution are retained; root has
independently rederived both. No table's ratio subcase, reported original
Jedlicka theorem or exceptional-APN component theorem is an operative
whole-polynomial premise. The present read does not claim a complete
fresh introduction, later main theorems, entire19 pages, or original
Jedlicka/JMW/Ferard proofs. Author access failures remain literal limits,
not evidence of published nonoverlap. No new paper download was needed.

## Entire packet, worklog and command/code record

Root read ALL13 author files: main, ALL64 obligations, issues, source
MD/JSON, failures, worklog, code boundary, full integrity source, full
baseline, input-validation, metadata and freeze. A clipped main Section6
was recovered separately; nothing was inferred from an ellipsis. Root
also read complete accepted R6/R9 bodies and each current MD/JSON as
recorded above. Every new proof step was reconstructed by hand, including
the local formal branch, finite length, geometry, counts, sign and family
arithmetic. No author/old/source executable was run.

The NEW review admin helper ONLY records or checks path/bytes/SHA/JSON,
literal ledger count and preserved guards. It performs no mathematical
calculation, network, CAS, scan, routine test or certificate/freezer replay.
Its prepare/freeze/verify calls are separate. No native mathematical job,
partial output, pending approval or claimed effective-setting override.
All existing frozen bytes and shared/Git files remain unchanged by this
review. Root alone separately integrated released unrelated material.

After this report, admin and baseline are generated, root must actually
read ALL final payloads, then freeze, fully read the freeze, and perform
a SEPARATE read-only verification. Until root explicitly confirms BOTH
ENTIRE initials, no corresponding NEW review2 findings/content/actual
inventory/hash/metadata access or review1 release is permitted. This is
ONE initially blind whole64 audit, not both audits or annual acceptance.
