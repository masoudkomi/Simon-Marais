# Signed power gaps: sources and an attributed consequence

2026-10-17 UTC. **Candidate proof - unverified** pending two whole
audits with the companion PG1--PG3 candidate. No novelty is claimed.

The [official 2025 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2025_paper_b.pdf)
is already transcribed and source-checked in statement.md and the
initial reviews. Its geometric degree n is m-1 in our notation.
No preliminary part (a) proof is included.

The exact elementary inputs C2/C4 are the accepted frozen proof.md,
SHA-256 c422139567ee3e2f4eafd852c9a3f5fac73cb6c8e0bfdf9e2c9c5311a9348b0d,
as covered by proofs/reviewed-partial-v1.1.md and reviews/acceptance.md.
This return does not change those files or silently promote any
other conjectural conclusion in the original proof register.

## Positive-base overlap

Y. Bugeaud and P. Mihailescu, *On the Nagell--Ljunggren equation*,
Math. Scand. 101 (2007), 177--183,
[journal](https://journals.msp.org/mscand/article/view/659),
[PDF](https://journals.msp.org/mscand/article/download/659/658),
[DOI](https://doi.org/10.7146/math.scand.a-15038).
The root read the cached primary text through Theorem 1, including
its Equation (1) domain x,y>1, m>2, q>=2 and its known-exception
clause. For odd prime q, its m divisible by q conclusion is stronger
than PG2/PG3 for positive x. That positive domain does not itself
justify negative x. A fresh web retrieval of the PDF failed; the
already cached primary PDF/text supplies this reading. No new claim
of having reconstructed its entire proof is made.

## Signed published restriction

M. A. Bennett and A. Levin, *The Nagell--Ljunggren equation via Runge's
method*, Monatsh. Math. 177 (2015), 15--31,
[author-posted published PDF](https://personal.math.ubc.ca/~bennett/BeLe-Mona-2015.pdf),
[DOI](https://doi.org/10.1007/s00605-015-0748-1).
The root opened the author-posted PDF and read its Equation (1),
Proposition 1, Theorem 1 and their surrounding qualifications on
printed pages 15--17. It explicitly uses integers |x|,|y|>1,
m>2 and q>=2. Proposition 1 says that a solution outside their
four known examples has least prime divisor of m at least 5.
Theorem 1 states Omega(m)<=3, counting prime factors with multiplicity.
Their symbol n denotes our m. These are attributed published inputs;
this return does not reconstruct their entire Runge proof or its
exceptional-case import. No positive-base assumption is added.

### PG4. Attributed signed prime-power diagonal corollary

Assuming the two published Bennett--Levin restrictions just stated,
together with the elementary PG3, there are no integer solutions

    G_(q^a)(x)=y^q, |x|>=2, q an odd prime, a>=2.

Proof. By the accepted C1 magnitude bound |y|>1. None of the four
known examples has term count m=q^a with q odd and a>=2: their
(m,q) are (5,2), (4,2), (3,3), (3,3). If q=3, the least prime
divisor restriction in published Proposition 1 is violated. If q>=5,
published Theorem 1 gives a=Omega(q^a)<=3. Thus 2<=a<=3<q,
contradicting the necessary condition q divides a from PG3.
This proves the displayed corollary conditional on those attributed
published theorems, not a new proof of the imported theorems.

PG4 treats composite prime-power term counts with the same prime
as the power exponent. It leaves m=q (the prime diagonal case)
and general term counts unresolved. It makes no claim about the
known even-exponent term count m=4. It is not a full solution of B4(b).

## Separate class-group lead, not a premise or accepted inference

Mihailescu's 2008 diagonal chapter, the Bartolome--Mihailescu v2
appendix clarification, and Hart--Harvey--Ong's finite calculations
suggest a finite prime-range corollary. The root has not completed
the full hypothesis and proof-interface audit for that inference.
Nothing from it is used in PG1--PG4. No unrestricted Vandiver
conjecture or unreviewed recent preprint is assumed.

All full papers remain in ignored local cache. This note records
citations and theorem scope only, and redistributes no full paper.
