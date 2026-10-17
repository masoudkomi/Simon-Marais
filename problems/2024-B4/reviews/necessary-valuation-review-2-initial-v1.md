# Necessary-valuation candidate: whole initial review 2

2026-10-17 UTC. Reviewer `/root/review_2017_coarsening_r1`. This is an
initially blind whole audit of the coordinator's NEW NV argument. I have
not read the other new NV review, its findings, or later coordinator
reconciliation. Requested settings: gpt-6.1-sol/max; verified effective
readback unavailable. This report does not promote the result.

**Finding:** no substantive mathematical objection found. All eleven
submitted obligations pass in the stated domain. The conclusion is the
necessary implication

\[
 q=2^k,\quad k\ge2,\quad d=q^2-q+1,\quad n\ge3\text{ odd},\qquad
 \phi_d\mid\phi_n\text{ over }\mathbf F_2
 \Longrightarrow v_2(n-1)=k.
\]

This is a statement about the WHOLE fixed divisor. It supplies neither a
converse nor a classification of reducible \(\phi_n\), individual Kasami
components, or the annual problem.

## Independence boundary and inputs

I constructed the older CP1--CP3 packet. Its accepted CP1 is therefore an
explicit accepted dependency, not an input for which this report is a
fresh nonconstructor review. I read the COMPLETE accepted CP1--CP3 body
and its acceptance scope, including the homogeneous/dehomogeneous
equivalence, free rank-four descent, repeated diagonal cancellation,
composition criterion and unit endpoints. The NEW local valuation
argument was constructed by root; I did not supply or construct it and
reconstructed it below without peer findings. The fact that the same
reviewer authored an old dependency does not make this an independent
re-audit of that old dependency.

Exact submission: `coordinator-Kasami-necessary-valuation-v1.md`, 3446
bytes, SHA256
`5b772b77f821c3e3b2f7b04a22c0f9d3609f85942e9cd3d3a0d13104cbc118a4`.
Exact author manifest: 1363 bytes, SHA256
`005a5ea65ac2b7da94ec085c3b6d93ac7938f2102cd5b1af79f569012b6e2ac8`.
I read the entire main note, all eleven obligations and its complete
source record. The manifest's administrative script is fingerprinted,
not executed. No mathematical program, scan, CAS, finite-field sampling
or old certificate rerun is used in this review.

## Official domain and accepted bridge

The official 2024 B4(b) asks for all odd positive \(n\) admitting the
specified coefficientwise modulo-two factorization into two factors
nonconstant modulo two. The present implication concerns a restricted
whole divisor of its quotient \(\phi_n\); it does not answer that entire
question. The official coefficient convention does not permit replacing
polynomials by functions on a finite field. The accepted \(n=1\) zero and
\(n=3\) unit boundaries remain separate. Nothing here reproduces part(a).

Accepted CP1 applies to ALL odd \(d,n\ge3\) and says

\[
 \phi_d\mid\phi_n \iff g_n=H\circ g_d,
 \qquad H\in\mathbf F_2[T],
 \quad x^j+(x+1)^j=g_j(x^2+x).
\]

It also gives \(\deg g_j=(j-1)/2\). For this candidate \(q\ge4\), so
\(d\ge13\) is odd and the dependency's hypotheses hold. Both \(g_d\)
and \(g_n\) have positive degree, and hence \(H\) has positive integer
degree. Comparison of these degrees gives

\[
 n-1=(\deg H)(d-1)=(\deg H)q(q-1).
\]

Thus \(n\ge d\) and \(s=v_2(n-1)\ge k\). This is a WHOLE-divisor
consequence, with no information about one isolated absolute component.
It is valid also for \(n=d\), when \(H=T\).

## Reconstruction of the exact local-order argument

Set \(G_j(x)=x^j+(x+1)^j\). CP1 gives the polynomial identity
\(G_n=H(G_d)\) by substitution, over \(\mathbf F_2\). For EVERY odd
\(j\ge3\), direct evaluation and formal differentiation give

\[
 G_j(0)=1,\qquad G'_j(0)=0^{j-1}+1^{j-1}=1.
\]

The exponent \(j-1\ge2\) rules out a problematic \(0^0\) endpoint.
Evaluation and the chain rule consequently give
\(H(1)=1\) and \(H'(1)=1\). Polynomial division yields

\[
 H(T)+1=(T+1)Q(T),\qquad Q(1)=H'(1)=1.
\]

For any finite point \(\alpha\) with \(G_d(\alpha)=1\), the factor
\(Q(G_d(x))\) has value one at \(\alpha\) and is a local unit. Therefore

\[
 \operatorname{ord}_{\alpha}(G_n+1)
 =\operatorname{ord}_{\alpha}(G_d+1).                 \tag{A}
\]

This uses only the simple root of \(H(T)+1\) at \(T=1\). No global
separability or nonvanishing derivative at other values of \(H\) is
needed. In particular a possible inseparable contribution away from this
fiber cannot invalidate (A).

There exists \(\alpha\in\mathbf F_q\setminus\mathbf F_2\) because
\(k\ge2\). Put \(a=\alpha\) and \(b=\alpha+1\). Both are nonzero,
\(a+b=1\), \(a^q=a\), \(b^q=b\), and
\(a^{q-1}=b^{q-1}=1\). Work in the polynomial ring
\(\mathbf F_q[z]\), with \(x=\alpha+z\). Frobenius gives

\[
 (a+z)^d=(a+z)(a+z^q)^{q-1}.
\]

Terms through degree \(q+1\) come only from the powers zero and one
of \(z^q\); powers two and above have degree at least \(2q>q+1\).
Their expansion, including the coefficient \(q-1=1\) in characteristic
two, is

\[
 (a+z)^d
 =a+z+z^q+a^{-1}z^{q+1}\pmod {z^{q+2}}.
\]

The same formula with \(b\) follows from the same identities. Summing
gives

\[
 G_d(\alpha+z)+1
 =(a^{-1}+b^{-1})z^{q+1}\pmod {z^{q+2}}
 =\frac{z^{q+1}}{ab}\pmod {z^{q+2}}.
\]

The displayed coefficient is nonzero since \(a+b=1\) and \(ab\ne0\).
This independently checks the submission's constant, linear, degree
\(q\), degree \(q+1\), and all missing intermediate coefficients.
In particular \(G_d(\alpha)=1\) and

\[
 \operatorname{ord}_{\alpha}(G_d+1)=q+1.               \tag{B}
\]

Suppose \(s>k\), and write \(n=1+2^s h\) with \(h\) positive odd.
Already \(q-1\mid n-1\), so
\(a^{n-1}=b^{n-1}=1\). The exact identity

\[
 (a+z)^n=(a+z)(a^{2^s}+z^{2^s})^h
\]

shows, modulo \(z^{2^s}\), that \((a+z)^n=a^n+a^{n-1}z=a+z\).
The analogous expression for \(b\) sums to one. Therefore

\[
 G_n(\alpha+z)+1\equiv0\pmod {z^{2^s}},
 \qquad \operatorname{ord}_{\alpha}(G_n+1)
 \ge2^s\ge2q>q+1.                                   \tag{C}
\]

There are no unaccounted powers between one and \(2^s\); the argument
is a Frobenius polynomial identity, not a Lucas sampling assertion.
\(G_n\) has degree \(n-1\) with leading coefficient one for odd
\(n\ge3\), so \(G_n+1\) is a nonzero polynomial and this order is
finite. Equations (A)--(C) contradict each other. Thus \(s>k\) is
impossible, and the already established \(s\ge k\) proves NV.

## Degenerate cases and attempted attacks

* At \(q=2\), \(\phi_3=1\) divides every \(\phi_n\), and \(n=5\)
  would have \(v_2(n-1)=2\ne1\). Thus neither the field-point step nor
  the implication extends to \(k=1\). The candidate explicitly excludes
  it; this is a successful check of necessity of its hypothesis.
* At \(q=4\), there are two valid choices outside \(\mathbf F_2\).
  The expansion still has \(2q=8>q+1=5\). It gives the same necessary
  valuation as the older exact whole-\(\phi_{13}\) criterion, without
  importing that criterion's proof or strengthening this conclusion.
* At \(n=d\), \(v_2(d-1)=k\), and \(H=T\) has precisely the required
  simple fiber. A unit cofactor does not invalidate a statement about
  divisibility, although it alone is not the official factorization.
* If \(3\le n<d\), the assumed whole divisibility fails by CP1's degree
  relation. There is no hidden small-\(n\) exception.
* Repeated factors of \(\phi_d\), an absolute component defined over an
  extension field, or a finite-field functional identity cannot replace
  the whole F2-polynomial hypothesis. Accepted CP1 retains multiplicities
  and gives an actual F2 composition. The new proof then legitimately
  evaluates that polynomial identity in \(\mathbf F_q\).
* Higher critical fibers of \(H\) cannot affect the selected fiber at
  one, where the formal derivative is exactly one. No characteristic
  two cancellation can remove the explicitly nonzero \(1/(ab)\) term.

These checks produced no counterexample inside the stated domain. They
do not give a converse, the full general-\(q\) progression, or an
all-factor obstruction. The submission's attribution and non-novelty
limits are appropriate. Source scope, commands and administrative
integrity are recorded separately. No repair requested; coordinator
reconciliation with a second blind whole audit remains necessary.
