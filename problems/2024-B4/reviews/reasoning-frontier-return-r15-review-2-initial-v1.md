# F15: sealed independent whole review 2

19 October 2026 UTC. Reviewer C, `/root/review_2017_coarsening_r1`.
**Initial disposition: PASS all 24 obligations in the stated necessary-condition
and failed-route scope; zero substantive defects, zero required repairs.**
Eight scope notes below are closed by the printed hypotheses. This is an
initial audit, not coordinator promotion, a classification, or an external
validation. Findings remain SEALED until explicit BOTH-entire release.

A is the sole NEW constructor. C supplied no F15 inference and has not read,
inventoried, opened or hashed corresponding NEW F15 peer material. C constructed
OLD FR10/FR11/CL14 and was an excluded conceptual trigger for OLD TR12/R13.
Those separately accepted inputs are not independently re-certified here.
This review independently reconstructs the NEW DS1--DS3 argument conditional
on their exact accepted interfaces. Requested inherited gpt-6.1-sol/max is
distinct from unavailable independent effective-backend readback.

## 1. Entire packet, target, and exact input boundary

The author freeze was read FIRST. Its five-file identity is
`notes/reasoning-frontier-return-r15-freeze-v1.json`, 2505 bytes,
SHA256 d5d9804d237c368818cfaa7dcc9dda188cb474f7c4f5b7e97d50e1d561b283d2.
The full main is 19639 bytes, SHA256
b12c04780620c440ee88fb734ef97e25c85ed5b21402198a672c153938082ffa.
Every author payload was fully read, including sources, documentary helper,
baseline and all 24 constructor obligations. Author code was NEVER executed.
The complete accepted CL14, FR10, FR11, TR12 and R13 bodies and EACH current
acceptance MD/JSON were freshly read. The first aggregate body output clipped;
standalone complete FR10 and CL14 reads recovered it. No hash substitutes for
a mathematical read. FR11/R13 are comparison context, not extra premises.

The official target is ONLY 2024 B4(b): a coefficientwise integer-polynomial
product with both prescribed reductions nonconstant. After the established
quotient, ordinary F2 reducibility is the relevant condition; a factor solely
over an extension or polynomial-function equality is insufficient. The new
argument assumes q=2^i, i>=2, odd ell>=3 dividing q-1, n=ell*q+1. Thus q is
exactly the two-part of n-1, n>=13, and binary weight is at least three.
It does not investigate preliminary(a) or extend to n1/n3, ell1 or q2.

Write phi=phi_n, C=(1:1:1), N=ell*q-2. U is a NONZERO homogeneous ACTUAL
divisor in F_q[X,Y,Z], with homogeneous complement V there. Set e=deg U and
m=ord_C U, taking order zero for a local unit. No irreducibility, absolute
coefficient descent, common stabilizer or coordinate invariance of U is
assumed. Constant and whole divisors are legitimate endpoints.

The operative accepted FR10 interface supplies the exact local forms and
restriction data, reducedness, and the actual least-component/FULL-complement
intersection budget. CL14/TR12 supply the exact normalized M21 count. Older
Fulton/T1/R6 source chains retain their accepted scope; this is not a fresh
entire audit of them. No unaccepted packet or peer finding is a premise.

## 2. Independent reconstruction of DS1

Every b in mu_ell minus {1} lies in F_q*. At P_b=(b:1:1), put
X=b+u,Y=1+v,Z=1. In the accepted FR10 expansion the numerator degree-q
term vanishes, since b^(1-q)=1. Dividing its degree-(q+1) term by the
degree-one denominator (b+1)^2 v gives the quotient initial form

    c_b [u^q+u v^(q-1)+(1+b)v^q],
    c_b=b^(-1)/(b+1)^2 in F_q*.

This also directly checks the scalar and tangent orientation in the cited
formula. At v=0 the form is u^q, so no tangent has v=0. In the chart v=1
the roots satisfy lambda^q+lambda=a, a=1+b in F_q*. The derivative is 1,
so the q roots are distinct. For each root,

    lambda^q=lambda+a,
    lambda^(q^2)=lambda+a+a=lambda.

They lie in F_(q^2). Frobenius_q is the fixed-point-free involution
lambda -> lambda+a: its square is the identity and its fixed-point equation
would force a=0. In particular no tangent line is F_q-defined. This is a
field argument for every admissible q,b, not an enumeration of roots.

If m_b=ord_(P_b) U, initial forms multiply to the displayed squarefree
degree-q form. Consequently initial(U) is a product of a SUBSET of its
distinct tangent lines. Translation at an F_q point preserves coefficients
in F_q; Frobenius_q therefore preserves that subset. Its cardinality m_b
is even, including m_b=0 or q. This does not require an individual absolute
component or branch to descend to F_q.

Finally, the initial part of U evaluated at v=0 is nonzero: it divides a
binary form whose value at the direction (1:0) is nonzero. Thus
U(b+u,1,1) has exact order m_b in u, with no higher-order cancellation.
This verifies the restriction multiplicity rather than identifying it with
local multiplicity without a non-tangency proof.

## 3. Independent reconstruction of DS2

The accepted polynomial restriction is

    phi(X,Y,Y)=(X^ell+Y^ell)^q/(X+Y)^2
      =(X+Y)^(q-2) product_(b!=1)(X+bY)^q.              (R)

For an independent check that this is polynomial restriction, take the
coefficient of v in the identity f_n(X,Y,Y+v)=R(X,Y,Y+v)*phi(X,Y,Y+v).
The numerator coefficient is X^(ell*q)+Y^(ell*q), and the denominator
coefficient is (X+Y)^2. Cancelling in the polynomial domain gives (R),
whose displayed right side is polynomial since q>=4 and ell is odd.
This uses the established quotient, not a new preliminary proof.

At infinity on this line, (1:0:0), (R) has value 1. The identity UV=phi
there forces U(1,0,0) and V(1,0,0) nonzero. Hence U(X,Y,Y) is a nonzero
homogeneous binary form of degree e, with NO infinity root. All its finite
roots must occur in (R).

At C the accepted first numerator form is u^q v+u v^q and the denominator
is u v(u+v). Their quotient is

    C_q(u,v)=(u^(q-1)+v^(q-1))/(u+v)
            =product_(lambda in F_q minus {0,1})(u+lambda v).

The last equality follows from the distinct nonzero roots of
T^(q-1)+1; division removes lambda=1. This cone is squarefree, degree q-2,
and nonzero at all three diagonal directions u=0, v=0 and u=v.
Initial(U) divides it. Therefore each diagonal restriction has exact order
m at C, including m=0, by the same non-tangency argument as above.

On the first diagonal factorization over K, combined with (R) and the
noncentral multiplicities just proved, yields

    U(X,Y,Y)=c (X+Y)^m product_(b!=1)(X+bY)^(m_b),
    e=m+sum_(b!=1) m_b, c in F_q*.

The degree identity loses no root at infinity. The leading coefficient c
belongs to F_q because the original restriction does, and every b is in
that field. Every m_b is even. Squaring is an automorphism of the finite
field F_q, so c has a square root in F_q. With epsilon=m mod2=e mod2,
halving the even exponents and replacing m by floor(m/2) gives

    U(X,Y,Y)=(X+Y)^epsilon B_1(X,Y)^2,
    B_1 in F_q[X,Y], deg B_1=(e-epsilon)/2.

Apply this proof to the coordinate-permuted ACTUAL divisor of the symmetric
whole polynomial. A coordinate permutation fixes C and is an automorphism
of its local ring, so it preserves m. It follows, without assuming U itself
invariant, that U(Y,X,Y) and U(Y,Y,X) have the same epsilon and the stated
square forms over F_q. If U is center-free, m=0, hence e is even and all
three restrictions are squares. The converse and global gluing are not proved.

## 4. Independent reconstruction of DS3 and endpoints

For U over F2, its initial form at C has F2 coefficients and is a divisor
of C_q. Thus its distinct slope set in F_q minus {0,1} is a union of
Frobenius_2 orbits. Every orbit length divides i and exceeds 1: the only
fixed slopes under squaring are 0 and 1, both absent. Thus m is a sum of
lengths of DISTINCT available orbits, with each orbit selected at most once.

If i is a power of two (with the standing i>=2), every permitted orbit
length is even. Hence m and e are even and all three restrictions are
squares. If i has an odd prime divisor and e is odd, then m is odd. A sum
of even lengths cannot be odd, so a selected odd-length orbit must occur.
Its length is an odd divisor >1 of i, and is at least the smallest odd
prime divisor of i. This proves the printed lower bound on m, without
asserting realizability of any orbit selection.

For constants, e=m=m_b=0 and constant nonzero scalars in F_q are squares.
For the whole phi, e=N is even, m=q-2 is even, and (R) is a square.
The smallest allowed q4 has q-2=2; its center cone is u^2+uv+v^2 and
has the two nontrivial F4 slopes, one orbit of size 2 over F2. All three
directions remain non-tangent. This is a symbolic endpoint check, not a
new factorization or preliminary-family investigation. Odd-degree F_q
divisors are NOT generally excluded: they may have odd positive m. Arbitrary
absolute components with larger coefficient fields are outside DS1--DS3.

## 5. Failed-sector arithmetic and attempted counterexamples

For ell21,q=2^(6t),t>=1, ell divides q-1. Independently insert
B2,r3,s7,A8,L21 into the accepted CL14 count:

    M21=8*(8-2)+(21-1-8)*(2*3-2)=48+48=96.

The ordered normalization and full root group match FR10. Since d=ell,
the accepted same-pair upper expression becomes

    (q-2)^2/4+60q^2/4+96q+96q(q-2)/4
      =157q^2/4+47q+1.

Its lower product is q(N-q)=20q^2-2q. Four times their difference is
-77q^2-196q-4, strictly negative. This demonstrates only failure of
that sufficient contradiction.

For a split DEFINED OVER F_q, both noncentral orders are even and sum
to q. Since q/2 is even, the midpoint is not excluded: locally one may
select q/4 tangent PAIRS, a subset of q/2 lines. This is not a global
factor construction or a claim that every least absolute component is
F_q-defined. If e is even, both central orders are even and sum to q-2;
the real/integer midpoint q/2-1 is odd. The nearest even allocation gives
product at most (q-2)^2/4-1. The fourfold gap increases by 4 only, to
-77q^2-196q, still negative. If e is odd, the midpoint parity is allowed.
No universal additional quadratic discount follows from the displayed
pairing proof alone. The author does not claim this exhausts DS1--DS3's
possible consequences, or that a nonpositive test proves reducibility.

Adversarial attempts were directed at the following interfaces:

* A root fixed by Frobenius_q would force a=0; b=1 is excluded, so the
  alleged fixed-point counterexample lies outside the domain.
* A tangent at v=0 would remove an affine slope or inflate a restriction
  multiplicity; the u^q coefficient rules it out. At C all three diagonal
  directions are checked, not merely one.
* An infinity zero of U would invalidate the degree identity; UV=1 at the
  line infinity point excludes it for constants and nonconstant U alike.
* An odd degree over F_q is not a contradiction unless m=0 (or an added
  F2 orbit condition applies). This blocks an overstrong extension.
* A noninvariant divisor need not share literal tangent sets on the three
  lines. The proof only needs the corresponding permuted divisor and the
  common local order at C, so this attack does not invalidate the claim.
* Local branch unions do not construct an actual plane factor. The packet
  explicitly retains simultaneous compatibility as the missing inference.

No counterexample to the printed DS statements was found. No scan, CAS,
mathematical executable, finite factor table or author program was used.

## 6. ALL24 individual dispositions

| Author obligation | Disposition and independent reason |
|---|---|
| F15-O01 | PASS: official only(b), coefficientwise positive odd n and both nonconstant reductions preserved; no function-value substitution. |
| F15-O02 | PASS: all five accepted bodies and each current MD/JSON fully read; exact operative versus context roles distinguished. Old C construction/trigger roles disclosed, not self-certified. |
| F15-O03 | PASS: ell odd>=3 divides q-1, q2^i i>=2 implies exact two-part, n>=13 and all FR10 hypotheses; ell=q-1 allowed only in local scope. |
| F15-O04 | PASS: U and V are homogeneous actual F_q polynomials; no arbitrary absolute-component descent or U symmetry is assumed. |
| F15-O05 | PASS: every b belongs to F_q*, and direct substitution gives scalar b^-1/(b+1)^2 times the stated noncentral cone. |
| F15-O06 | PASS: a=1+b nonzero, derivative1, q distinct slopes; leading u^q excludes slope infinity. |
| F15-O07 | PASS: lambda^q=lambda+a, lambda^(q²)=lambda and a!=0 give a free involution on all tangent slopes. |
| F15-O08 | PASS: initial factors multiply; squarefree cone makes the actual F_q tangent subset distinct and Frobenius-stable, hence m_b even. |
| F15-O09 | PASS: initial U evaluated at v0 is nonzero, so the first surviving u term has exact order m_b, also when m_b0. |
| F15-O10 | PASS: coefficient-of-v argument proves polynomial restriction; UV=1 at (1:0:0) rules out a lost infinity zero. |
| F15-O11 | PASS: center cone is exactly the product over F_q minus {0,1}; squarefree degreeq-2 and all three diagonal directions absent. |
| F15-O12 | PASS: restriction zeros are a subset of the whole line zeros; all finite multiplicities and no infinity root give e=m+sum m_b. |
| F15-O13 | PASS: finite-field squaring is surjective, c has an F_q square root, and all halved exponents are integers. These are coefficient identities. |
| F15-O14 | PASS: coordinate permutation transports an actual divisor of the symmetric whole polynomial, fixes C and preserves m; no invariance of U is required. |
| F15-O15 | PASS: center-free means m0, then e even and three squares. The statement does not eliminate all remaining even factors or all centered odd factors. |
| F15-O16 | PASS: initial F2 coefficients force a union of DISTINCT squaring orbits on the center slopes; squarefreeness forbids repeated selections. |
| F15-O17 | PASS: orbit lengths divide i, exceed1, and imply exactly the printed power-of-two/minimal odd-prime consequences; no allocation existence asserted. |
| F15-O18 | PASS: constants, whole divisor, zero local orders, q4 and the even N/q-2 endpoints checked; no n1/n3/ell1/q2 extrapolation. |
| F15-O19 | PASS: M21=96 independently reconstructed from the accepted formula; upper157q²/4+47q+1 and lower20q²-2q give exact negative gap. |
| F15-O20 | PASS: q/2 even leaves the noncentral maximum; an even-center allocation saves one unit only and leaves G+4<0. This insertion is conditional on an F_q-defined split. |
| F15-O21 | PASS: no local-to-global factor realization is inferred; simultaneous restrictions and off-diagonal incidences remain the genuine missing inference. |
| F15-O22 | PASS: no Gauss-map, exceptional-APN whole theorem, unread Ferard criterion or publication-priority inference enters the proof. |
| F15-O23 | PASS: literal source limits/roles/failures/quota and no-math-code boundaries are explicit; fresh selected primary reads recorded below and in JSON. |
| F15-O24 | PASS for the present initial workflow: entire payloads/metadata will be finally read back before manifest, then full manifest before separate read-only verification. Two OTHER initials and coordinator reconciliation remain mandatory. |

## 7. Issue ledger: zero required repairs; eight closed scope notes

F15R2-N1 CLOSED: F_q definition is essential. An absolute component is not
silently descended merely because its incident point is rational.
F15R2-N2 CLOSED: squarefree initial form, not global branch transitivity,
justifies a subset and distinct orbit counting.
F15R2-N3 CLOSED: no infinity zero and all three non-tangent diagonal
directions justify exact degree/multiplicity identities.
F15R2-N4 CLOSED: coefficient squares use the PERFECT finite coefficient
field; they are stronger than equalities of values but not sufficient for
plane divisibility.
F15R2-N5 CLOSED: center-orbit restrictions concern actual F2 divisors;
the power-of-two corollary does not rule out odd F_q factors with m odd.
F15R2-N6 CLOSED: the ell21 numerical saving concerns an F_q-defined
split and does not assert every least absolute component has that field.
F15R2-N7 CLOSED: HM's conditional whole theorem also requires the proper
odd-part condition ell!=q-1. That source is not applied to the maximal
ell=q-1 endpoint allowed by the NEW local lemma.
F15R2-N8 CLOSED: unknown global compatibility, publication overlap and the
annual target remain open; failure of the gap test supplies no converse.

There is no substantive issue requiring author repair in the stated scope.
Acceptance remains solely the coordinator's decision after BOTH full audits.

## 8. Literal sources, failure limits, and operations

Fresh original official Paper B p2 setup57--63, only(b)68--74 and coefficient
definitions were returned/read. Adjacent preliminary/other-problem text was
not investigated. Local statement and AGENTS were fully read.
https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf

Fresh primary HM arXiv0903.2016v4: returned local Taylor/type context,
Lemmas4/5 statements, COMPLETE Lemmas6/7 proofs and multiplicity tables;
COMPLETE Theorem15 statement/proof; Theorem16 statement/returned proof
context; Section6 counterexample context/references. Theorem15 is conditional
on ordinary irreducibility and proper ell|q-1; Theorem16 gives a component.
Neither supplies a NEW whole-irreducibility premise here. No whole-paper or
new foundational source audit is claimed. https://arxiv.org/pdf/0903.2016v4

Fresh Férard2017 publisher metadata/ENTIRE abstract only; the subscription
operative body remains UNREAD, so its actual criterion/overlap is unresolved.
No theorem is inferred from that preview and no access retry, charge,
contact, bypass or priority inference occurred.
https://link.springer.com/article/10.1007/s12095-017-0213-1

No new external theorem is required for the elementary Frobenius/square
argument. Accepted FR10/CL14/TR12 supply the separately reviewed interfaces;
old Fulton/T1/R6 proof reads are not relabeled fresh. FR11/R13 were fully
read for comparison, without introducing their conclusions as extra premises.

Worklog: freeze-first and narrow unused-prefix check; full author5 read;
five complete accepted bodies and each MD/JSON; recovery of first clipped
aggregate via standalone body reads; bounded primary web reads; independent
hand proof and endpoint/counterexample attempts above; compact exclusive
review writes and necessary once-listed documentary guards. The NEW helper
only binds bytes/JSON/literal obligation labels. It NEVER executes source,
author, old helper or mathematical code. No native job/PID or pending tool
approval exists. No Git/shared/old/cache/configuration changes or spawning.

ONE exact OWN JT13 WHOLE1 manifest is outer-bound as immediate parent;
its payloads/history are not recursively opened or re-hashed. Corresponding
NEW F15 peer access remains embargoed until BOTH release. JT13 findings
remained separately sealed until root's explicit BOTH release received
during this review; its unchanged disposition was then sent without peer
access. Root also administratively released PH13 peers, but no such peer
material was accessed or used.

Start direct quota:85%TOTAL at03:52:36UTC; latest direct observation86%TOTAL
at04:00:37UTC, reset1792874445,10080-minute window, ordinary usage allowed,
both views agree.90%TOTAL includes review/integration reserve; no later
window authorized. Final freeze/readback/separate identities will be reported
only after the actual operations, not invented here.
