# Independent whole review 2: sole-H4 and sole-H2 candidates

2026-10-16 UTC. This joint initial report audits two separate coordinator-constructed candidates. Both remain **candidate proof - unverified** pending coordinator reconciliation and the required two-review acceptance. I make no promotion.

## Independence and frozen inputs

I did not construct either candidate. I completed this report, its issue ledger, and its source/provenance record before reading any peer sole-H4, sole-H2, or single-center review report or conclusion. The pre-existing J15 acceptance record was read solely to identify accepted dependencies. The earlier frozen 2022 review remains unchanged and its peer findings remain unread.

Requested settings remain gpt-6.1-sol / max, as specified in the assignment and AGENTS.md. Independent effective-setting readback is unavailable; no effective setting is claimed.

The exact reviewed candidates are:

- Sole-H4: notes/coordinator-J15-soleH4-candidate-v1.md, SHA-256 042b15f45a39f6773ec8e5eea6c4294eab5e794e98a961534b899ef2568b508e.
- Sole-H2: notes/coordinator-J15-soleH2-candidate-v1.md, SHA-256 a21d53ab434ea715b85cca9bcf98c715a1522f4faa33d1977c1ad9411b7f9d39.

Both match their freeze records. Source and dependency fingerprints, command details, and the joint freeze manifest are separate artifacts.

## Initial disposition

**No blocking or substantive mathematical defect found in either candidate. No author repair requested.** I independently reconstructed every finite-field elimination, split-witness branch, final exclusion table, and passage from a residue slot to an actual rational witness. Both necessary-pattern classifications survive this audit, including repeated-root and coincident-residue possibilities at the outset.

These are conditional restrictions on a normalized degree-20, J=15, double-zero hypothetical counterexample to 2021 B4(b). Neither note excludes a complete center mask, establishes that a listed residue pattern has a full lift, resolves degree 20, or determines the annual set of degrees. I recommend accepting only the stated partial classifications once the coordinator has reconciled both independent reports.

## 1. Official scope and accepted dependencies

The [official 2021 Paper B, page 2](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf) requires a rational polynomial and a rational common root separately for every nonconstant derivative; witnesses may depend on the derivative. Part (b) asks which degrees have the stated pure-power conclusion. I checked these quantifiers and fields. No proof of preliminary part (a), or another contest problem, is investigated here.

The accepted normalization is rational and keeps the contest witness field \(\mathbb Q\). In the present degree-20 branch, 0 has multiplicity exactly two, 1 is simple, and J=15. Accepted Newton and rational-cover inputs give fourteen root slots of valuation \(1/14\), the center 1, two copies of zero, and three nonzero small slots. At least two distinct small root values are rational over \(\mathbb Q\). The fourteen fractional-valuation slots cannot be rational witnesses, because valuations of elements of \(\mathbb Q_{19}^{\times}\), hence of rational numbers, are integral.

Accepted D1 gives the local factorization

\[
f=X^2(X-u)(X-v)(X-w)B,\qquad B=(X-1)g
\]

over \(\mathbb Q_{19}\), with all three small slots in \(\mathbb Q_{19}\) and \(g\) degree fourteen and Eisenstein. I checked the field argument: remove one copy of each of two distinct rational small roots; the local Galois action fixes those copies and preserves valuations, so it fixes the single remaining small slot. This proves local rationality only. It does not prove that the third value is in \(\mathbb Q\), or that it may be chosen as a contest witness.

For the coefficient facts used below, writing \(B=\sum b_iX^i\) gives \(v(b_0)=1\), \(v(b_i)\ge1\) for \(1\le i\le13\), \(b_{14}\equiv-1\pmod{19}\), and \(b_{15}=1\). These follow from the Eisenstein factor and the simple center factor. No quotient over \(\mathbb Q\) is presumed.

Accepted D2 is applied by contrapositive. If the small valuations are unequal, at least two of \(H_2,H_3,H_4\) vanish at 1. Each new note explicitly assumes two specified center values are nonzero, so its valuations must all equal an integer \(\nu\ge1\). This uses actual nonvanishing at the center, not merely a selected noncenter witness where the center might also work.

I checked the relevant D2 algebra and hypotheses on use. For a unique outer minimum and two tied inner roots, the ratio sets for simultaneous noncenter \(H_2,H_3\) witnesses are \(\{11,7\}\) and \(\{18,3,13\}\), disjoint. For two tied outer roots and one deeper root the sets are \(\{14,15\}\), \(\{2,10\}\), and \(\{18,4,5\}\), pairwise disjoint. In the all-distinct case the width-one edges have lower exponents 4, 3, and 2, all strictly below 19 as the accepted width-one lemma requires. Coincident residues in a tied group do not evade those necessary ratio sets. Thus the stated accepted theorem applies with precisely the hypotheses present.

## 2. Common scaled initial form and witness domain

Put \(q=19^\nu\). An explicit integral rescaling is

\[
G(T)=\frac{f(qT)}{q^5b_0}
=T^2(T-u/q)(T-v/q)(T-w/q)\frac{B(qT)}{b_0}.
\]

For \(1\le i\le13\), the coefficient \(b_iq^i/b_0\) has valuation at least \(i\nu\ge1\). For \(i=14,15\), its valuation is respectively \(14\nu-1\) and \(15\nu-1\), also positive. Therefore \(B(qT)/b_0\equiv1\pmod{19}\), and

\[
\overline G=F=T^2(T-U)(T-V)(T-W)
=T^5-sT^4+tT^3-zT^2,
\quad U,V,W\in\mathbb F_{19}^{\times},\ z=UVW\ne0.
\]

This argument supplies an explicit meaning for division by the leading valuation and confirms that high-degree terms disappear without an invalid nonunit division after reduction.

For \(k=2,3,4\), Hasse scaling gives

\[
H_k(G)(T)=\frac{q^{k-5}}{b_0}H_k(f)(qT).
\]

Any actual zero or small-root common witness therefore gives the corresponding necessary common-root equation for \(F,H_k(F)\) after reduction. The center 1 is handled separately. The fourteen fractional-valuation roots are not possible rational witnesses, so the actual rational noncenter witness list is exhausted by zero and the globally rational members of the three small slots. Allowing all three local slots during the algebra only enlarges this necessary list.

For a nonzero cubic root \(A\), use \(z=A^3-sA^2+tA\) in

\[
H_2(F)=10T^3-6sT^2+3tT-z.
\]

This gives the exact formulas used by both candidates:

\[
H_2(F)(A)=A(9A^2-5sA+2t),\quad
H_3(F)(A)=10A^2-4sA+t,\quad H_4(F)(A)=5A-s.
\]

At zero the three values are \(-z,t,-s\). The nonzero-root formula for \(H_2\) is not used at zero. Scaling by a nonzero witness residue \(R\) scales \(s,t,z\) by \(R,R^2,R^3\), so normalizing that residue to 1 is legitimate.

The nonzero squares modulo 19 are \(1,4,9,16,6,17,11,7,5\), from the representatives 1 through 9. All constant denominators below are nonzero modulo 19. A single variable denominator is separately checked before use.

## 3. Whole reconstruction of the sole-H4 classification

Here \(H_2(f)(1)\ne0\) and \(H_3(f)(1)\ne0\). A rational noncenter \(H_2\) witness exists. Zero is impossible since its scaled \(H_2\) value is \(-z\ne0\). Normalize this witness's residue to 1; denote the other two slots \(x,y\), allowing repetitions and equality with 1 at this stage. Then

\[
s=1+x+y,\qquad t=x+y+xy,\qquad 2t=5s-9.
\tag{H4.1}
\]

There are exactly three branches for an actual \(H_3\) witness: zero; a small root with residue 1; or a small root with another residue, called \(x\). This is a split by residue, not an initial assumption that the actual roots are distinct.

### 3.1 \(H_3\) at zero

Necessarily \(t=0\). Equation (H4.1) gives \(s=9/5=17\), hence \(x+y=16,xy=3\). The discriminant is \(16^2-12=16\), with square roots \(\pm4\), giving \(\{x,y\}=\{6,10\}\). This is row I.

### 3.2 \(H_3\) at residue 1

The equation is \(10-4s+t=0\). Together with (H4.1), this yields \(3s=11\), hence \(s=10,t=11\), and \(x+y=9,xy=2\). The discriminant is \(9^2-8=16\), giving \(\{x,y\}=\{12,16\}\). This is row II. If another actual slot had reduced to 1, it would have been covered by this same equation; the resulting distinct residues exclude that possibility rather than assuming it away.

### 3.3 \(H_3\) at another residue \(x\ne1\)

Equation (H4.1) becomes

\[
2xy-3x-3y+4=0.
\]

If \(2x-3=0\), then \(x=3/2\) and its remaining term is \(-1/2\ne0\), a contradiction. Thus division is valid and \(y=(3x-4)/(2x-3)\). The \(H_3\) equation becomes \(6x^2-3x+y(1-3x)=0\); multiplying by the verified nonzero denominator yields

\[
12x^3-33x^2+24x-4=0.
\]

Modulo 19 this is

\[
(x-3)(12x^2+3x+14)=0.
\]

Expanding the displayed factorization differs from the unreduced integer polynomial by multiples of 19, as required. The quadratic discriminant is \(9-4\cdot12\cdot14=2\pmod{19}\), a nonsquare. Therefore \(x=3\), \(y=8\), \(s=12,t=16\). This is row III. A repeated \(x=y\) was not divided out or omitted; it simply does not solve this branch.

### 3.4 Complete derivative checks and actual root slots

Write \(Q_2(T)=9T^2-5sT+2t\). The following factorizations over \(\mathbb F_{19}\) independently verify all final table entries:

| Row | Small residues | \(Q_2(T)\) | \(H_3(F)(T)\) | \(H_4(F)(T)\) |
|---|---|---|---|---|
| I | \(1,6,10\) | \(9T(T-1)\) | \(10T(T-3)\) | \(5(T-11)\) |
| II | \(1,12,16\) | \(9(T-1)(T-13)\) | \(10(T-1)(T-3)\) | \(5(T-2)\) |
| III | \(1,3,8\) | \(9(T-1)(T-12)\) | \(10(T-3)(T-17)\) | \(5(T-10)\) |

At zero \(H_2(F)=-z\ne0\). The \(H_3\) zero-root possibility occurs only in I, since its \(t\) is 0, whereas II and III have \(t=11,16\). In all rows \(s\ne0\), and the listed \(H_4\) root is outside the small residue multiset, so neither zero nor a small root can be an actual rational \(H_4\) witness. The contest hypothesis consequently forces \(H_4(f)(1)=0\).

Only the residue 1 among the three small slots can witness \(H_2\). Every surviving row has three pairwise distinct nonzero residues, so exactly one actual root slot has that residue. The full hypothesis guarantees the witness exists; that unique slot is therefore an actual \(\mathbb Q\)-rational root \(r\). In II the only allowed \(H_3\) residue is also 1, so its actual witness equals \(r\), not merely its residue. In III the sole possible \(H_3\) slot has residue \(3R\) and is rational over \(\mathbb Q\) because it is the required witness. In I only zero can serve. This verifies the complete claimed witness identification.

## 4. Whole reconstruction of the sole-H2 classification

Here \(H_3(f)(1)\ne0\) and \(H_4(f)(1)\ne0\). Both required rational witnesses are noncenter, and the same equal-valuation reduction applies. Split first by whether the actual \(H_4\) witness is zero or a nonzero small root.

### 4.1 \(H_4\) at zero

Then \(s=0\). If \(H_3\) also uses zero, \(t=0\), so the nonzero roots form \(T^3-z\). Choose any root residue \(R\ne0\) and scale it to 1. The remaining roots satisfy \(X^2+X+1=0\), whose roots are 7 and 11: their sum is 18 and product 1. They are distinct because the cubic has derivative \(3T^2\), nonzero at every nonzero root. This gives row A.

If instead \(H_3\) uses a nonzero small root, scale its residue to 1. Its equation gives \(t=-10=9\). The other two slots have sum 18 and product \(t+1=10\), with discriminant \(18^2-40=18\), a nonsquare. This excludes that branch even if repeated slots had initially been allowed.

In row A, \(H_3(F)(A)=10A^2\), \(H_4(F)(A)=5A\), and \(H_2(F)(A)=9A^3\) are nonzero at all nonzero small roots. Zero fails \(H_2\) because \(z\ne0\). Thus the actual \(H_3,H_4\) witnesses are both zero and \(H_2\) must use the center. Choosing a different member of \(R\{1,7,11\}\) for \(R\) merely permutes the same normalized set, since \(\{1,7,11\}\) is the cube-root-of-unity subgroup.

### 4.2 \(H_4\) at a nonzero small residue

Normalize this residue to 1. Then \(s=5\), \(x+y=4\), and \(xy=t-4\). If \(H_3\) uses zero, \(t=0\), so the remaining discriminant is \(16-60=13\), a nonsquare. Thus \(H_3\) must use a nonzero small slot.

If it uses residue 1, \(10-20+t=0\) gives \(t=10\). The remaining roots have sum 4, product 6, and discriminant \(11=7^2\). Their residues are 8 and 15, yielding B. Possible repeated slots of residue 1 have been included and then excluded by these derived distinct values.

Otherwise name its residue \(x\ne1\). With \(y=4-x\), one has \(t=4+4x-x^2\), and the \(H_3\) equation is

\[
9x^2-16x+4=0.
\]

Its discriminant is \(17=6^2\), and \(2\cdot9=18=-1\) is a unit. The roots are \(x=16\) and \(x=9\), respectively giving \((y,t)=(7,2)\) and \((14,16)\). These are C and D. This exhausts zero, the \(H_4\) residue, and every other small slot without division by a root difference.

### 4.3 Complete derivative checks and actual root slots

The independently reconstructed factorizations are:

| Row | \((s,t)\) | Small residues | \(Q_2(T)\) | \(H_3(F)(T)\) | \(H_4(F)(T)\) |
|---|---|---|---|---|---|
| A | \((0,0)\) | \(1,7,11\) | \(9T^2\) | \(10T^2\) | \(5T\) |
| B | \((5,10)\) | \(1,8,15\) | \(9(T-13)^2\) | \(10(T-1)^2\) | \(5(T-1)\) |
| C | \((5,2)\) | \(1,7,16\) | \(9(T-8)(T-18)\) | \(10(T-16)(T-5)\) | \(5(T-1)\) |
| D | \((5,16)\) | \(1,9,14\) | \(9(T-3)(T-4)\) | \(10(T-9)(T-12)\) | \(5(T-1)\) |

For B,C,D, the unique eligible \(H_4\) residue is 1; zero fails since \(s=5\ne0\). The only eligible \(H_3\) residues are respectively 1,16,9; its second roots 5 and 12 in C,D are outside the small residue sets, and zero fails since \(t\ne0\). The double \(H_3\) root in B gives no second small slot: only one small slot has residue 1. Thus B's actual witnesses coincide at the unique root \(r\), and C,D's two witnesses occupy distinct unique actual slots. Existence and \(\mathbb Q\)-rationality follow from the original witness hypothesis, not from reduction alone.

For \(H_2\), in B,C,D the quadratic \(Q_2=9T^2-25T+2t\) has discriminants respectively 0,6,5. The square roots \(0,\pm5,\pm9\), with denominator 18, give exactly the displayed roots. They lie outside each respective small-root set. At zero \(H_2=-z\ne0\); A has already been checked. Hence there is no noncenter rational \(H_2\) witness in any row, and the contest hypothesis forces \(H_2(f)(1)=0\).

## 5. Adversarial boundary and quantifier audit

Repeated actual roots imply repeated slots and repeated leading residues, and are therefore excluded here only after the derived pattern lists have distinct residues. Initial tied residues, a third slot with residue equal to a distinguished witness, and \(x=y\) were all retained during the splits. No factor \(x-y\) or \(x-1\) was canceled. The sole variable denominator \(2x-3\) was proved nonzero before cancellation. A discriminant zero does not cause a missed field extension: in B the derivative quadratic has a double root, explicitly retained and checked.

The nonsquare contradictions require all three small residues to be in \(\mathbb F_{19}\). Accepted D1 provides exactly that. They would not be valid for arbitrary small roots in a residue extension without D1; no such extension is silently allowed. Conversely, a small root in \(\mathbb Q_{19}\) need not be in \(\mathbb Q\). The algebra temporarily allows every local slot as a possible witness, then uses the guaranteed actual rational witness and uniqueness of its slot. Case A's free choice of scale \(R\) requires no claim that its selected local root is globally rational.

Neither candidate infers a sufficient exact derivative equation from a residue equation. All lifting statements are phrased as necessary patterns. The existence of full derivative witnesses is used only to force the indicated unique candidates and the remaining center equation. The other small slots are not collectively asserted rational. The accepted D1 guarantee of at least two distinct global rational small roots remains separate from the newly determined low-order roles.

Both new notes are independent of each other and of any unreviewed single-center peer analysis. Their comments about accepted D4 do not import its parity obstruction into distinct-residue patterns. No complete mask, J15 branch, multiplicity-three branch, lower-J case, or degree-20 classification follows. All of these scope boundaries are correctly stated.

## 6. Verification boundary

The audit uses exact hand algebra and finite-field factorizations explained above. No enumeration, CAS operation, finite-height search, or numerical experiment was used. Reading accepted source registers and their frozen theoretical bodies does not amount to a fresh re-review of unrelated historical computational certificates; those remain accepted inputs within their established scopes. No substantive author repair is needed on either audited candidate. Only the coordinator may decide acceptance after the second independent whole report.
