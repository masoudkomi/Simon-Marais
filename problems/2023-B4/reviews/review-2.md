# Independent adversarial review R2: 2023 B4(b)

**Initial blind report completed:** 2026-10-16, 10:07 UTC.

**Verdict:** I found no substantive mathematical objection to the full-classification argument in the assigned version. The proof reconstructs for arbitrary coprime reduced indices, rather than only for checked exponents. This report supports accepting the argument after the coordinator has also considered the other independent audit and resolved any objections. It does not itself promote the candidate's status.

## Identity, independence and scope

- Reviewed artifact: [candidate-resultant-v0.1.md](../notes/candidate-resultant-v0.1.md).
- SHA256 checked before review:
  77d209d6a35ebf96a72d5d3a29f9f23d8f7456adae01d1572c180cf842c05365.
- Reviewer R2 did not construct the candidate. I did not read another review report, ask another reviewer for conclusions, or receive another reviewer's mathematical findings before completing this report. The coordinator supplied only the existing research Python interpreter location when the initially tried interpreters lacked SymPy.
- Requested launch settings: gpt-6.1-sol with max reasoning. No independent effective-setting readback was available.
- Work was confined to auditing B4(b), the cited established inputs needed for it, this report, and its disjoint computational evidence. I did not solve or reproduce the preliminary part (a).
- The candidate remains a candidate proof until the coordinator makes the protocol's status decision. No claim of novelty or absolute certainty is made here.

## Official statement and published inputs

I opened the primary [2023 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2023_paper_b.pdf) and [official solution notes](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2023solutions.pdf) online on 2026-10-16. I also extracted the relevant cached text and visually inspected Paper B p. 2 and solution-note pp. 15-16 after rendering them with bundled Poppler. The statement is: for each fixed positive integer \(n\) that is not a perfect square, classify positive integer pairs \((a,b)\) admitting a real \(r\) with both indicated shifted powers rational. There is no positivity condition on \(r\), and no squarefreeness assumption on \(n\). The paper designates only part (b) as open.

The candidate matches those quantifiers and domains. Its attributed uses of the official notes on pp. 14-16 are appropriate: the diagonal family and the absence of positive off-diagonal witnesses; absence of further same-parity pairs; and the complete exponent-1 case with off-diagonal pair \(\{1,2\}\). Those are inputs, not claimed new contributions. The official negative witness for \((1,2)\) is stated on p. 15. The primary notes currently served at the cited URL still describe partial results, rather than the candidate's full classification; that observation is not a broader publication or priority audit.

Cached source hashes checked during the audit:

- Paper B: 7d8ec51774224eeb1d66c1bae5ba6df98c0f7b41b0635811105a669be7a6eee2.
- Solutions: 446d9d19f962e9bbc727422be6a5c1de62fcf0fc3d0cf424494861d7eb7d832c.

Only references and review evidence are added to Git. The primary PDFs remain in the existing local cache.

## Independent reconstruction of the full argument

### 1. Reduction and real signs

For an off-diagonal solution, the published inputs give \(r<0\) and opposite parity of \(a,b\); \(r=0\) cannot work because \(\sqrt N\) is irrational. Thus \(d=\gcd(a,b)\) is odd. With \(x=r^d<0\), the reduced exponents \(e,o\) are coprime, with \(e\) even and \(o\) odd. Their shifted powers have the same rationality property.

Both \(x^e,x^o\) lie in \(K=\mathbb Q(\sqrt N)\) and are nonzero. If \(ue+vo=1\), including possible negative \(u,v\), then \(x=(x^e)^u(x^o)^v\in K\). Negative powers cause no problem in this field. Conjugating each rationality relation gives the candidate's two positive differences \(2\sqrt N\). In particular the odd relation gives \(x'>x\); the even one gives \(|x'|>|x|\). A negative \(x'\) with that greater magnitude would satisfy \(x'<x\), so \(x'>0\). Hence \(U=x'>V=-x>0\).

Consequently \(D=U-V=x+x'>0\) and \(P=UV=-xx'>0\) are rational. These signs, including strict \(U>V\), are justified. The two power equations become
\[
U^e-V^e=U^o+V^o=2\sqrt N.
\]
The first implies \(U>1\), since \(N\ge2\). Therefore \(e<o\) would give the strict chain in the candidate; equality is excluded by parity. Thus \(e>o\). The official exponent-1 result handles \(o=1\), so the new exclusion only needs \(e>o\ge3\).

### 2. Recurrence and the rational denominator

The recurrence polynomials have characteristic roots \(U,-V\), whose difference \(U+V\) is nonzero. Thus the displayed closed form for \(F_j\) is legitimate. It gives \(F_e=F_o\) and
\[
(D^2+4P)F_o^2=4N.
\]
This squared relation is used only as a necessary condition, so its possible loss of a sign is harmless.

For \(D,P>0\), all \(F_j\), \(j\ge1\), are positive. If \(D\ge1\), then \(F_{j+1}=DF_j+PF_{j-1}>F_j\) for \(j\ge2\), so \(F_e=F_o\), with \(e>o\ge3\), is impossible. Therefore \(D=p/q\) in lowest terms with \(0<p<q\) and \(q\ge2\). Neither \(p=0\) nor \(q=1\) is silently omitted.

The binomial recurrence formula gives weight \(j-1\) with weights \(1,2\) for \(D,P\). Put \(m=(e-2)/2\), \(h=(o-1)/2\). Then \(F_e\) has degree \(m\), leading coefficient \((e/2)D\), while \(F_o\) is monic of degree \(h\).

### 3. General unit-resultant lemma

At \(D=1\), put \(\alpha=\zeta/(1+\zeta)\), \(\beta=1/(1+\zeta)\) for a nontrivial \(o\)-th root of unity \(\zeta\). Because \(o\) is odd, \(1+\zeta\ne0\); because \(\zeta\ne1\), \(\alpha\ne\beta\). Their sum is 1 and product is \(-P_\zeta\). The recurrence formula therefore gives \(F_o(1,P_\zeta)=0\) and the displayed value for \(F_e(1,P_\zeta)\).

The equation defining \(P_\zeta\) is quadratic in \(\zeta\), with reciprocal roots. Thus each \(P_\zeta\) has exactly the two preimages \(\zeta,\zeta^{-1}\); odd \(o\) prevents self-inverse nontrivial roots. This yields exactly \(h\) distinct roots, so it exhausts the roots of the monic degree-\(h\) polynomial \(F_o(1,P)\). This works for composite \(o\), not just prime \(o\).

Coprimality makes \(\zeta\mapsto\zeta^e\) a permutation of all nontrivial \(o\)-th roots. Therefore the numerator/denominator product \(\prod(\zeta^e-1)/(\zeta-1)\) is exactly 1. Also \(\prod(1+\zeta)=1\) by evaluating the quotient of \(T^o-1\) by \(T-1\) at \(-1\). Hence the product of the displayed \(F_e\) values over all \(\zeta\ne1\) is 1. It is the square of the product over distinct \(P_\zeta\), so the latter is \(+1\) or \(-1\). The root-product formula for a monic polynomial then makes the resultant a unit up to sign.

For clarity, the general exponent after \(P=D^2Z\) is
\[
(e-1)h+(o-1)m-2mh=(e-1)h
=\frac{(e-1)(o-1)}2.
\]
The substitution and scalar-resultant rules apply over \(\mathbb Q(D)\); equality there implies the integer-polynomial identity in \(D\). Thus the candidate's unrestricted unit-resultant lemma is established, without extrapolating from finite tests.

### 4. Weighted bound for the elimination polynomial

Over \(\mathbb Q(D,N)\), \(A=F_e-F_o\) has degree \(m\) in \(P\). When \(e=o+1\), its leading coefficient is \((e/2)D-1\), a nonzero polynomial; it is not legitimate to assume this coefficient never vanishes after numerical specialization, but the argument does not do so. The polynomial \(B\) has degree \(o\) and leading coefficient 4.

Under \(D\mapsto tD\), \(P=t^2Z\), \(N\mapsto t^{2o}N\),
\[
A\mapsto t^{e-1}(F_e-t^{-\delta}F_o),\qquad
B\mapsto t^{2o}B,\qquad \delta=e-o.
\]
Scalar factors in the resultant contribute \(t^{(e-1)o+2om}\); the variable substitution contributes \(t^{2mo}\). Their quotient is \(t^{o(e-1)}=t^L\). This verifies (16), including its exponent.

The resultant of \(F_e-sF_o\) and \(B\) is a polynomial in \(s\): in the Sylvester matrix, all entries are polynomial in \(s\). Taking \(s=t^{-\delta}\) introduces only nonpositive powers of \(t\). Since monomials \(D^iN^j\) on the left carry distinct formal variables and powers \(t^{i+2oj}\), no monomial of weight exceeding \(L\) survives. This proves the required bound for arbitrary \(e,o\).

### 5. The \(N=0\) identity and specialization audit

All eliminations and multiplicative identities are first performed at generic degrees over the rational-function field, then recognized as polynomial identities. At \(N=0\),
\[
\operatorname{Res}(A,(D^2+4P)F_o^2)
=\operatorname{Res}(A,D^2+4P)\operatorname{Res}(A,F_o)^2.
\]
Replacing \(A\) by \(F_e\) in the second resultant is allowed by the root-product formula at the monic \(F_o\); the generic first degrees agree. Its square is \(D^{(e-1)(o-1)}\).

For the linear factor, up to the irrelevant resultant-order sign,
\[
\operatorname{Res}(A,D^2+4P)=4^m A(D,-D^2/4).
\]
The repeated characteristic root at \(P=-D^2/4\) causes no division problem: the recurrence itself yields \(F_j=j(D/2)^{j-1}\). Substitution gives
\[
4^m A(D,-D^2/4)
=D^{o-1}\left[(e/2)D^\delta-2^{\delta-1}o\right].
\]
Multiplication proves (15), including both exponents and coefficients. The bracket is a nonzero polynomial because \(\delta>0\), so \(R\) is not identically zero.

I specifically checked degree loss as a potential gap. At \(e=o+1,D=2/e\), the actual degree of \(A\) drops. A universal resultant specialized there can differ from the resultant recomputed at reduced degrees by a nonzero power of the unchanged leading coefficient 4. This does not invalidate either polynomial identity or the necessary vanishing: a common finite root makes the fixed-degree Sylvester determinant vanish as well. One can also see this directly from its singularity or its standard Bezout identity. No assertion that a nonzero resultant is sufficient for existence is used. The excluded value \(D=0\) likewise cannot create a lost physical solution.

### 6. Denominator divisibility and both branches

Multiply \(R(p/q,N)=0\) by \(q^L\). A term involving \(N^j\), \(j\ge1\), has denominator-clearing factor \(q^{L-i}\) with
\[
L-i\ge2oj\ge2o.
\]
All its other factors are integers. The constant part is, up to sign,
\[
p^{e(o-1)}\left[(e/2)p^\delta-2^{\delta-1}o q^\delta\right].
\]
The exponent identity \(e(o-1)+\delta=L\) is exact. Because \(\gcd(p,q)=1\), cancellation of the displayed power of \(p\) modulo \(q^{2o}\) is valid. This proves \(q^{2o}\mid H\).

If \(\delta<2o\), reduction modulo \(q^\delta\) and coprimality imply \(q^\delta\mid e/2\). Therefore
\[
e\ge2q^\delta\ge2^{\delta+1},\qquad
o=e-\delta\ge2^{\delta+1}-\delta\ge2\delta.
\]
The elementary inequality used here holds for every positive integer \(\delta\): \(2^{\delta+1}\ge3\delta\), with the induction step following from \(6\delta\ge3(\delta+1)\). In particular \(e/2=(o+\delta)/2<o\). Together with \(0<p<q\), this proves \(H<0\), while \(0<-H<2^{\delta-1}o q^\delta\). The nonzero integer multiple of \(q^{2o}\) then forces
\[
2^{2o-2\delta+1}<o.
\]
But \(o\ge2\delta\) makes the left side at least \(2^{o+1}>o\). This contradiction includes the smallest case \(\delta=1\); there is no unhandled zero value of \(H\).

Thus \(\delta\ge2o\). The second term of \(H\) is divisible by \(q^{2o}\), so coprimality gives \(q^{2o}\mid e/2\), and therefore \(e\ge2q^{2o}\ge2^{2o+1}\). The equality boundary \(\delta=2o\) is harmless (indeed parity makes it unattainable), and the branch's divisibility argument covers it without an extra assumption.

### 7. Large-exponent contradiction

The sum relation and \(U>V\) give \(U^o>\sqrt N\ge\sqrt2\), hence \(U>2^{1/(2o)}\). Factoring the even-power difference and retaining its first positive term gives
\[
D U^{e-1}<U^e-V^e=U^o+V^o<2U^o.
\]
All inequalities are strict: \(V>0\), \(e\ge4\), and \(U>V\). Since \(\delta-1>0\),
\[
1/q\le D<2U^{-(\delta-1)}
<2^{1-(\delta-1)/(2o)}.
\]
Thus \(q^{2o}>2^{\delta-1-2o}\). Combining this with \(e/2\ge q^{2o}\) gives exactly \(e>2^{e-3o}\); there is no missing factor of 2.

For \(o\ge3\), the earlier lower bound gives \(e\ge2^{2o+1}\ge6o\), with \(e\) even and at least 4. Then \(e-3o\ge e/2\) and \(2^{e/2}\ge e\), the latter by induction over even \(e\). Hence \(2^{e-3o}\ge e\), a contradiction. This completes the unrestricted exclusion.

### 8. Returning to all pairs and sufficiency

The only off-diagonal reduced pair left by the new exclusion and the published exponent-1 result is \(\{2,1\}\). Restoring the odd gcd gives exactly \(\{2d,d\}\) for positive odd \(d\). The official witness \(x=1/2-\sqrt N<0\) has a real negative \(d\)-th root for each such \(d\); that root has the two required powers. Even \(d\) is not inferred by this construction. Symmetry restores both orders. The attributed diagonal family handles every equal positive pair.

Accordingly the candidate's full proposed classification follows with the official domain and all boundary cases covered.

## Supplemental exact evidence and reproducibility

The unrestricted conclusion above rests on the reconstructed symbolic argument, not these finite checks.

- Script: [review-2-evidence.py](review-2-evidence.py).
- Preserved output, including failed first attempts: [review-2-evidence.txt](review-2-evidence.txt).
- Successful command, from the repository root:

      /Users/uqmkamga/Documents/ChatGPT/Website/.venv/bin/python problems/2023-B4/reviews/review-2-evidence.py

- Successful runtime: Python 3.12.14, SymPy 1.14.0, python-flint 0.9.0.
- Parameters: \((e,o)=(4,3),(6,5),(8,3),(8,5),(8,7),(10,3),(10,7),(12,5),(14,9)\). All nine independently launched children completed successfully, with 20-second timeouts each, no timeout and empty stderr.
- Each child checked the unit-resultant identity, the constant-in-\(N\) identity up to sign, integer coefficients, the weighted-degree bound and denominator-clearing powers. It also checked fixed-degree versus recomputed resultants at \(D=0\), and at \(D=2/e\) in the three \(\delta=1\) cases.
- A separate exhaustive integer loop checked (17) on 4,278 tuples with odd \(3\le o\le15\), even \(o<e\le60\), \(\gcd(e,o)=1\), \(2\le q\le10\), \(0<p<q\), \(\gcd(p,q)=1\). There were no divisibility exceptions. This is only bounded evidence.
- The initially selected bundled Python and /usr/local/bin/python3 lacked SymPy. The first script run logged all nine import failures and its successful pure-integer check; those outputs were retained before the successful rerun. No package was installed. Each native CAS child had its PID and parameters checkpointed before waiting; the script targets only that child on timeout.

## Findings and disposition

No counterexample or substantive proof gap was identified. The root-of-unity calculation is general; the weighted bound is a formal polynomial argument; the \(N=0\) factorization survives degree-specialization concerns; and the integer and real estimates are compatible and contradictory in the required ranges.

There is one optional exposition improvement: include the explicit exponent calculations in the resultant scaling, as expanded above, so a reader can verify (11) and (16) without supplying them. This is a readability suggestion, not a mathematical repair or an unresolved objection.

No shared issue-log entry was edited. There are no open R2 substantive objections to return to the author. The coordinator must make any promotion decision after both independent audits.
