# Independent adversarial review 2: rational-lift complexity candidate

Initial report, 2026-10-16 UTC. The reviewed work remains **candidate proof - unverified** until the coordinator applies the repository's two-review acceptance procedure. This report itself makes no promotion.

## Freeze, independence, settings, and scope

Reviewed candidate: `../notes/arithmetic-reasoning-complexity-candidate-v1.md`, SHA-256 `e9c24e96982d1d2a74aa97cb5fd045a3319f37c69316fbada884eeec0a0412d3` (12810 bytes).

I did not construct the candidate. Before completing this report, its separate issue ledger, and its source-check record, I did not read another new arithmetic-complexity review or receive another reviewer's conclusions. I read the existing acceptance record only to establish the already accepted dependencies. The initial artifacts are frozen by the separately recorded SHA-256 hashes. Any later comparison must be a new supplement rather than an alteration of these initial findings.

Requested settings: `gpt-6.1-sol`, reasoning `max`, as specified in the coordinator assignment and AGENTS.md. No independent effective-setting readback is available to this reviewer; requested settings are not reported as verified execution settings.

Only 2022 B4(b) is audited. I checked the official positive-integer domain, inclusive initial product threshold 600, simultaneous updates, and equality at a nonnegative time against [Official Paper B, page 2](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2022-paper-b.pdf). The published strip-entry result is accepted attributed context; its preliminary proof is neither reconstructed nor investigated here. No other contest problem is investigated.

## Initial disposition

**No blocking or substantive mathematical defect found.** The rational-lift dichotomy, its application to every admissible actual orbit after strip entry, and the explicitly coded irrational-lift family all survive my independent reconstruction. I recommend acceptance of these statements as partial results after the coordinator also has the second independent audit. No author repair is required by this initial review.

This is not a proof that every admissible orbit reaches equality. The argument leaves open ordinary integer lifts of sufficiently complicated nonperiodic avoiding paths. Neither density-one earlier results nor the present complexity obstruction closes that gap. Originality is not established. The attribution supplement correctly presents the main comparison mechanism as an adaptation of published work.

## 1. Exact controller arithmetic and signed recurrence

For an actual integer state write \(b=60Q+r\), \(a=b+d\), \(0\le r<60\). Integer translation of floors gives

\[
\lfloor b/20\rfloor=3Q+\lfloor r/20\rfloor,
\qquad
3\lfloor a/30\rfloor=6Q+c(d,r).
\]

Therefore \(b'=66Q+r+c(d,r)\) and \(d'=D(d,r)\), with the candidate's definitions. Reduction modulo 60 gives \(r'=(6e+r+c)\bmod60\), where \(e=Q\bmod10\). If \(r'=6e+r+c-60k\), then

\[
h=(r+c-r')/6=10k-e,\qquad 10Q'=11Q+h.
\]

Both the sign and the normalization of \(h\) are correct. There is no replacement of the simultaneous recurrence by sequential updates. The numerator defining \(h\) is divisible by 6 even for abstract controls. On the specified strip, \(-13\le r+d\le82\), so \(c\in\{-3,0,3,6\}\). The loose interval \(-62\le r+c-r'\le65\), combined with divisibility by 6, justifies the uniform bound \(|h|\le10\). Tightening the bound is unnecessary.

The scalar ceiling recurrence cannot be substituted for this controller. For the admissible state \((a,b)=(599,600)\), \(Q=10,r=0,d=-1,c=-3\); the actual next \(b\) is 657 and the next quotient is 10. In contrast, \(\lceil11Q/10\rceil=11\). Here \(h=-10\). This single exact check confirms that signed corrections and the controller state are substantive features of the extension, not cosmetic notation.

## 2. Inverse-limit lift and uniqueness

In \(\mathbb Z_{10}\), each term of the candidate's series (6) is defined because 11 is a unit, and terms with index at least \(N\) vanish modulo \(10^N\). Thus the series converges without treating this ring as a field. Directly shifting the summation gives

\[
11Q_n+h_n=10Q_{n+1}.
\]

Modulo 10, \(Q_n\equiv-h_n/11\equiv-h_n\equiv e_n\). Consequently the prescribed abstract controls really are the residues of the constructed quotient sequence.

If two lifts obey these relations for the same path, then

\[
11^N(Q_0-\widetilde Q_0)=10^N(Q_N-\widetilde Q_N).
\]

Since 11 is invertible, their initial difference belongs to every ideal \(10^N\mathbb Z_{10}\), whose intersection is zero. Apply the same argument to every tail for uniqueness of the whole lift. This reasoning is valid despite the zero divisors in the ring.

For a length-\(N\) prefix, reduction of the infinite series gives the initial class modulo \(10^N\) associated with that prefix by accepted P1. Accepted finite lifting supplies arbitrarily large positive representatives in this class. It supplies no ordinary integer representative common to all infinitely many prefixes; the candidate explicitly preserves that distinction.

## 3. Fixed rational denominator

Here is a reconstruction that avoids any implicit division by a nonunit inside the inverse-limit ring. Suppose \(Q_0=u/v\), with \(v>0\), \(\gcd(u,v)=1\), and \(\gcd(v,10)=1\). Iterating the recurrence gives

\[
10^n vQ_n=K_n,
\qquad
K_n=11^n u+v\sum_{j=0}^{n-1}11^{n-1-j}10^j h_j\in\mathbb Z.
\]

The left side is zero modulo \(10^n\). The embedding of the ordinary integers respects that quotient, so the ordinary integer \(K_n\) is divisible by \(10^n\). Write \(K_n=10^n z_n\), \(z_n\in\mathbb Z\). Multiplication by \(10^n\) is injective in \(\mathbb Z_{10}\): if \(10^n x=0\), reduction modulo \(10^{m+n}\) forces \(x\equiv0\pmod{10^m}\) for every \(m\). Hence \(vQ_n=z_n\).

This proves (9), including cancellation of both the 2-primary and 5-primary denominator factors. It also proves that every quotient is the same ordinary rational \(z_n/v\) when later interpreted over the reals. Neither a varying denominator nor an unjustified identification of real and 10-adic limits enters the argument.

## 4. Real boundedness, growth, and deterministic full states

With \(\beta=11/10\), iteration in the reals and the convergent tail sum give exactly

\[
Q_n=C\beta^n-T_n,
\quad
C=Q_0+\sum_{j\ge0}h_j10^j/11^{j+1},
\quad
|T_n|\le10.
\]

The plus sign in \(C\) is necessary and correct. Equation (6) is a different, 10-adic convergence statement and does not force this real \(C\) to vanish.

If \(C=0\), bounded quotients in the fixed lattice \(v^{-1}\mathbb Z\), together with finitely many strip states, yield finitely many triples \((Q,d,r)\). The evolution of a triple is deterministic: its rational 10-adic residue determines \(e\), which determines the next residue and correction, and the rational recurrence determines the next quotient. Repetition of a full triple therefore repeats the future. Repetition of \(Q\) alone would not suffice; the candidate uses the full state correctly. Negative rational quotients cause no difficulty in this argument.

If \(C\ne0\), then

\[
Q_{n+1}-Q_n=C(\beta-1)\beta^n-(T_{n+1}-T_n).
\]

The error has absolute value at most 20, while the first term eventually dominates it with constant sign. Thus strict monotonicity holds from some \(n_0\), including the case \(C<0\), when the real sequence decreases. The recurrence also gives

\[
|Q_n|\le\beta^n(|Q_0|+10)-10\le A\beta^n,
\qquad A=|Q_0|+10>0.
\]

These are valid for every \(n\ge0\); strict monotonicity is used only on the selected tail. The bounded branch has not been silently excluded from the abstract theorem.

As an adversarial check on its necessity, repeating loop \(B\) gives the rational two-cycle \(Q_0=1/21,Q_1=-1/21,Q_2=1/21\), with corrections \(-1,1\). It is a valid bounded abstract lifted path and belongs to the theorem's first branch. Repeating \(A\) gives \(Q_n=0\). These examples would invalidate a blanket abstract claim excluding periodic rational lifts, but do not contradict the stated dichotomy or the actual-orbit application.

## 5. Equal factors, nonzero divisibility, and the exact slope

For equal correction blocks of length \(L\) starting at \(n_0\le n<m\), the iterated numerator is the same integer

\[
H=\sum_{j=0}^{L-1}11^{L-1-j}10^j h_{n+j}.
\]

Subtracting the two recurrences gives

\[
10^L v(Q_{m+L}-Q_{n+L})=11^L v(Q_m-Q_n).
\]

All quotient differences multiplied by \(v\) are integers. Coprimality gives \(10^L\mid v(Q_m-Q_n)\). Strict monotonicity on the tail makes this a nonzero integer, so its absolute value is at least \(10^L\). The proof does not assume that equality of correction blocks implies equality of controller states, and it permits overlapping blocks.

The real bound gives \(v|Q_m-Q_n|\le2vA\beta^m\). Hence equal length-\(L\) factors are impossible among starts \(n_0,\ldots,M\) whenever \(2vA\beta^M<10^L\). Put

\[
x_L=\frac{L\log10-\log(2vA)}{\log\beta},
\qquad M_L=\lceil x_L\rceil-1.
\]

The inequality \(M_L<x_L\) holds even if \(x_L\) is an integer, resolving the strict-inequality endpoint. For sufficiently large \(L\), all the \(M_L-n_0+1\) starts exist and give distinct factors. Their number is \(\kappa L-O(1)\), so the claimed lower bound holds for the liminf over all sufficiently large lengths, not merely a subsequence. No recurrence, distribution, or independence property of the word is assumed.

## 6. Application to the exact official domain

An actual positive integer orbit has a nonnegative integer quotient after the accepted strip-entry time, and uniqueness of the inverse-limit lift identifies it with the series lift. If this tail had \(C=0\), bounded \(Q,d,r\) would bound \(a,b\). Both coordinates are nondecreasing positive integer sequences, hence eventually constant. Vanishing of the two increments then implies \(a\le29\), \(b\le19\), so \(ab\le551\). The product has never decreased and started at least 600, a contradiction. This explicitly covers small and equal quotients; it does not infer nonzero differences merely from positivity.

The complexity conclusion therefore applies to every actual admissible orbit, including an orbit that reaches equality at time zero or later. The proof never assumes equality remains invariant after a hit.

For the residue-state conclusion, each length-\((L+1)\) state block determines its length-\(L\) correction block through the adjacent-state formula for \(h\), so \(P_h(L)\le P_S(L+1)\). Replacing \(L+1\) by \(t\) and dividing by \(t\) preserves the liminf slope. A finite prefix cannot remove any tail factors. Thus (17) has no off-by-one or prefix defect.

## 7. Avoiding loops, mechanical word, coding, and irrationality

For \(d=1,r=0\) or 6, \(c=0,D=1\). The controls \(0,0\) return residue 0 through 0,0 and have corrections 0,0. The controls \(1,9\) send residues \(0\to6\to0\) and have corrections \(-1,1\). These exact two-step calculations verify both loops and arbitrary concatenation. All differences stay 1, so these abstract paths avoid equality.

For irrational \(0<\alpha<1\), the lower mechanical word is binary and satisfies

\[
\sum_{j=0}^{N-1}w_j=\lfloor N\alpha\rfloor.
\]

Its limiting frequency of 1 is the irrational number \(\alpha\), excluding ultimate periodicity. An eventual period \(p\) of the coded correction word would also give its even period \(2p\). For sufficiently late aligned two-letter blocks, injectivity of the two codewords would make \(w\) eventually \(p\)-periodic, a contradiction.

For a length-\(k\) mechanical block, \(x=\{n\alpha\}\) determines the floor differences. The \(k+1\) distinct breakpoints \(-j\alpha\bmod1\), \(0\le j\le k\), partition the circle into \(k+1\) half-open arcs on which the block is constant. The included point \(x=0\) is assigned the right-hand value, so the prefix does not add an exceptional factor. This establishes the upper bound \(P_w(k)\le k+1\) directly; no unverified Sturmian theorem is needed.

For factors in the length-two code, aligned starts use at most \(\lceil L/2\rceil\) underlying letters; starts one letter into a codeword use at most \(\lceil(L+1)/2\rceil\). Summing their bounds gives \(L+3\) for both odd and even \(L\), as asserted. Ultimate periodicity of full lifted states would force periodic corrections, and the alternative lower slope \(\kappa>1\) contradicts this upper slope at most 1. Thus the lift is irrational in the candidate's explicitly defined diagonal-rational sense in \(\mathbb Z_{10}\).

Combining the two signed terms from a \(B\) loop gives

\[
\frac{100^j}{11^{2j+1}}-\frac{10\,100^j}{11^{2j+2}}
=\frac{100^j}{121^{j+1}},
\]

which verifies formula (22). The associated real series is bounded by \(\sum100^j/121^{j+1}=1/21\). The mechanical word has both symbols, so its real value is strictly between 0 and \(1/21\). This is not an identification of that real value with the 10-adic value. Every finite avoiding prefix still has positive integer realizations by accepted P1; irrationality excludes an ordinary integer realization of the whole infinite path.

## 8. Attribution, checks, and residual limitation

I read the original [Dubickas 2009 publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C40C0C07FEC20797475BB2899C436C9A/S0017089508004655a.pdf/on_integer_sequences_generated_by_linear_maps.pdf), Theorem 3 (journal p.245) and its complete Section 4 proof (p.249). Its positive integer scalar ceiling hypotheses do not directly cover this controller. The supplied attribution supplement correctly credits the matching-block divisibility versus real-growth comparison; Sections 2–6 above independently check the extra signed, rational, finite-state steps. No new theorem about the scalar map is invoked.

The separate source-check record verifies the discovery citation and version date. The separate issue ledger records all substantive attack points and their disposition. The candidate and all accepted-input fingerprints match the supplied manifest. This review uses analytic reconstruction and exact hand calculations, not enumeration, a native CAS, or a numerical experiment.

No universal upper bound on avoiding-path complexity has been obtained. Arbitrary binary concatenation of the two loops prevents inferring such a bound from finiteness of the controller alone. No resolution of the universal equality question, real transcendence result, or novelty claim follows from this audit.
