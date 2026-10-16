# Unequal three-bundle entropy: candidate v1.1

**candidate proof - unverified**

Full revised version **v1.1**, 2026-10-17 (Australia/Brisbane). The revision author is `/root/owner_2017`, the original constructor of these second-pass packets. Both frozen independent initial reports were read for this author repair. All frozen v1 notes, manifests and review reports are preserved. The revised inferences require both targeted re-audits and coordinator acceptance before any promotion.

Original draft written 2026-10-16. No independent reviewer has audited this version. No claim of novelty, a better global B4 bound, or a solution of the open rates is made. The purpose is a precise obstruction to a tempting improvement of an existing construction.

Requested worker settings: `gpt-6.1-sol`, `max`; effective-setting readback unavailable.

## Attribution and relation to the open problem

Felsner–Valtr, *Coding and Counting Arrangements of Pseudolines*, Section 4, equations (11)–(14), [author PDF](https://page.math.tu-berlin.de/~felsner/Paper/new-pla.pdf), reproduces MacMahon's plane-partition product and gives a balanced three-bundle gluing lower bound. Its coefficient is
\[
c_0=\frac34\log_2 3-1=0.188721875540\ldots.
\]
This is weaker than the current located published lower bound 0.2721. The product formula and geometric counting dictionary are attributed context. The calculation below investigates the additional assertion that merely changing the three bundle sizes, even adaptively in a hierarchy, cannot improve that coefficient.

Local cached source used: `.cache/literature/2017/cited-7f7251133b0c4ebc.pdf`. Its retrieval URL and hash are recorded in the coordinator's `sources/literature-retrieval.json`; this pass does not alter that manifest. No full paper is copied into tracked files.

## Candidate M1: a sharp finite inequality for MacMahon's product

For positive integers a,b,c, define
\[
M(a,b,c)=\prod_{i=1}^{a}\prod_{j=1}^{b}
\frac{i+j+c-1}{i+j-1}.
\]
This is the telescoped MacMahon product. Put S=ab+bc+ca. The proposed inequality is
\[
\boxed{M(a,b,c)^2\,16^S\le27^S.}\tag{M1}
\]
Equivalently, \(\log_2 M(a,b,c)\le2c_0 S\). The numerical constant is asymptotically sharp along a=b=c tending to infinity, by the balanced MacMahon asymptotic reproduced in the attributed source. That sharpness statement does not assert anything about the full C(n).

### Step 1: replace the exact product by an integral, in the correct direction

Use natural logarithms in this proof. For c>0 let
\[
f_c(t)=\log\frac{t+c}{t},\qquad t>0.
\]
Then \(f_c''(t)=1/t^2-1/(t+c)^2>0\). On the unit square
\([i-1,i]\times[j-1,j]\), the average of x+y is i+j-1. Jensen's inequality therefore gives
\[
f_c(i+j-1)\le
\int_{i-1}^{i}\!\int_{j-1}^{j}f_c(x+y)\,dy\,dx.
\]
The integrable logarithmic singularity at (0,0) causes no difficulty: the random variable is positive almost everywhere and has a finite expectation. Sum these inequalities to obtain
\[
\log M(a,b,c)\le I(a,b,c):=
\int_0^a\!\int_0^b\log\frac{x+y+c}{x+y}\,dy\,dx.\tag{1}
\]

### Step 2: evaluate and normalize that integral

Set N=a+b+c, p=a/N, q=b/N, r=c/N. Thus p,q,r>0 and p+q+r=1. Define 0 log 0=0. Twice integrating log t, using
\(F(t)=\tfrac12t^2\log t-\tfrac34t^2\), yields
\[
I(a,b,c)=N^2 A(p,q,r),
\]
where
\[
A(p,q,r)=\frac12\sum_{x\in\{p,q,r\}}
\left[x^2\log x-(1-x)^2\log(1-x)\right].\tag{2}
\]
In deriving (2), the terms involving log N and the quadratic terms cancel because
\(N^2+a^2+b^2+c^2=(a+b)^2+(b+c)^2+(c+a)^2\).

### Step 3: the symmetric calculus inequality

Write
\[
\kappa=\frac34\log3-\log2=c_0\log2>0,
\quad g(x)=x^2\log x-(1-x)^2\log(1-x),
\quad h(x)=g(x)+2\kappa x^2.
\]
The desired inequality for (2) is
\[
A(p,q,r)\le\kappa(1-p^2-q^2-r^2),\tag{3}
\]
or, equivalently, \(h(p)+h(q)+h(r)\le2\kappa\).

The derivatives on (0,1) are
\[
g'(x)=1+2[x\log x+(1-x)\log(1-x)],
\quad h''(x)=2\log\frac{x}{1-x}+4\kappa.
\]
Consequently h'' is strictly increasing and vanishes exactly at
\(u=(1+e^{2\kappa})^{-1}\). Since \(0<\kappa<\tfrac12\log2\), we have \(1/3<u<1/2\). Thus h is strictly concave on (0,u) and strictly convex on (u,1).

The continuous function H(p,q,r)=h(p)+h(q)+h(r) has a maximum on the closed simplex.

- On its boundary, say r=0, the identity g(x)+g(1-x)=0 gives
  \(H=2\kappa[p^2+(1-p)^2]\le2\kappa\).
- At an interior maximum, at most one coordinate exceeds u. If two did, varying those two while fixing their sum would have strictly positive second derivative, contradicting local maximality.
- If all coordinates are at most u, concavity on [0,u] gives
  \(H\le3h(1/3)=2\kappa\).
- If one coordinate a exceeds u, the other two are in [0,u]; averaging them cannot decrease H. It is enough to bound
  \(J(a)=h(a)+2h((1-a)/2)\) for \(a\in[1/3,1]\).

For this last function,
\[
J''(a)=\log\frac{a^2}{1-a^2}+6\kappa.
\]
It is strictly increasing. We have J'(1/3)=0,
\(J''(1/3)=-\log8+6\kappa<0\), and the one-sided endpoint value J'(1)=4κ>0. Hence J' first decreases below zero and then increases, crossing zero once more. Therefore J first decreases and then increases on [1/3,1], and its maximum is at an endpoint. Direct substitution gives
\[
J(1/3)=J(1)=2\kappa.
\]
This completes (3). Moreover, the only interior equality point of (3) is p=q=r=1/3.

### Step 4: return to the product

Equations (1)–(3) give
\[
\log M(a,b,c)\le
\kappa\,[N^2-a^2-b^2-c^2]=2\kappa S.
\]
Multiplying by 2 and exponentiating gives
\(M^2\le e^{4\kappa S}=(27/16)^S\), which is (M1).

## Candidate M2: consequence for adaptive ternary gluing

Define a **specific construction model**, rather than claiming it covers all arrangements. An ordered rooted **full** ternary tree (every internal node has exactly three children) has n singleton strand leaves. Such a tree exists only when n is odd; for even n this singleton-leaf family is empty. This is an upper-counting construction model, not an all-n lower construction. The fixed bounded-size base-block extension is considered separately below. A node whose three child subtrees have a,b,c leaves may choose independently one of M(a,b,c) three-bundle partial arrangements. The choices within each child are then inserted using the boundary-preserving gluing construction. For one fixed tree T, the number of represented outputs is at most the product of those M-values (and equals that product if the gluing map is injective).

Applying (M1) at every internal node and telescoping gives
\[
\log_2\prod_{v\in T}M(a_v,b_v,c_v)
\le c_0\sum_{v\in T}
\left[n_v^2-a_v^2-b_v^2-c_v^2\right]
=c_0(n^2-n).\tag{4}
\]
Thus no choice of unequal sizes at the nodes of a fixed hierarchy improves its leading coefficient above c0. Allowing all ordered ternary tree shapes and labelled singleton leaves adds at most \(2^{O(n\log n)}\) choices, since the number of such trees is exponential in n and there are at most n! leaf labellings. Their union still has rate at most c0. An arbitrary fixed finite collection of bounded-size base blocks likewise contributes only \(2^{O(n)}\) further possibilities.

This is an upper bound on the number of outputs of this narrowly defined family. It is **not** an upper bound on C(n). Four or more interacting bundles, overlapping larger patches, or construction mechanisms outside this tree model are not covered.

## Candidate M3: floor-robust unequal recursion, for future constructions

This algebraic lemma explains what would be needed to use an unequal-bundle construction with a genuinely better local toll. Set b(1)=0 as the formal empty-network convention, with b(n)=log2 C(n)≥0 for n≥2. Suppose A>0 and for all sufficiently large n a valid geometric injection has already established
\[
b(n)\ge (A-o(1))n^2+\sum_{i=1}^k b(m_i(n)),
\]
where k≥2 is fixed, 0<p_i<1, sum p_i=1, m_i(n)/n→p_i, and \(\sum_i m_i(n)\le n\). Then
\[
\liminf_{n\to\infty}\frac{b(n)}{n^2}
\ge\frac{A}{1-\sum_i p_i^2}.\tag{5}
\]

For a proof, choose any \(0<\gamma<A/(1-\sum p_i^2)\). For all sufficiently large n,
\((A-o(1))n^2+\gamma\sum m_i(n)^2\ge\gamma n^2\), and all m_i<n. Choose K≥0 so that b(n)≥γn²−Kn for every smaller n. Strong induction, using \(\sum m_i\le n\), gives
\[
b(n)\ge\gamma n^2-K\sum_i m_i(n)\ge\gamma n^2-Kn.
\]
Divide by n², take liminf, and then let γ approach the right side of (5). Floors and unused bounded numbers of strands are allowed **only after** the underlying geometric injection has been established for all sufficiently large n. This lemma supplies no such injection by itself and does not prove existence of the limit.

For the three-bundle toll, the bit-valued local coefficient is \(A_{\rm bits}=A(p,q,r)/\log 2\) from (2), and (3) says that the right side of (5) is at most c0. The exact finite bound (4) is the stronger obstruction for that particular family.

## Independent-review obligations

Both independent initial v1 reports are frozen. This v1.1 adds the explicit full-ternary/odd-leaf convention in M2; the M1 and M3 mathematical arguments are unchanged. Both reviewers must perform the requested targeted re-audit of the revised scope before coordinator acceptance. Finite exact tests in `secondpass-macmahon-bound-output.txt` remain evidence only, not the proof of M1. This author revision does not promote any result.
