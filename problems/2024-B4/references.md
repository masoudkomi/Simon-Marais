# 2024 B4 references and published status

## Official starting sources

- [Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf), B4 on page 2.
- [Official solutions](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc_2024_solutions.pdf).

Official solutions (pp. 15-17) prove (a), discuss further reducible families and irreducible cases, and mention n=205. They do not give a complete classification. Verify exact family conditions against the PDF; connect later literature only after checking its field, reducibility and exceptional-exponent conventions.

## Primary-source checks, 2026-10-16

1. Fernando Hernando and Gary McGuire, *Proof of a Conjecture on the Sequence of Exceptional Numbers, Classifying Cyclic Codes and APN Functions*, J. Algebra 343 (2011), 78-92, DOI [10.1016/j.jalgebra.2011.06.019](https://doi.org/10.1016/j.jalgebra.2011.06.019). Author preprint [arXiv:0903.2016v4](https://arxiv.org/pdf/0903.2016), displayed date 18 September 2009; checked 2026-10-16.
   - Their g_t is exactly phi_t here, including the homogeneous F2 definition. Sections 2.1 and 2.3 distinguish absolute irreducibility from existence of an F2-defined absolutely irreducible factor.
   - Theorem 16 concerns t=2^i*l+1, odd l>=3, l dividing 2^i-1 but l not equal to 2^i-1: an absolutely irreducible F2-defined factor exists. Combined with earlier results it classifies exceptional APN exponents. This does not classify reducibility of the whole phi_t.
   - Their Theorem 15 begins by assuming irreducibility over F2; it cannot be used to establish that assumption.
   - Section 6 prints a degree-10 factor of g_205(x,y,1). It is transcribed and verified in computations/invariant_probe.py. The displayed homogeneous factor is phi_13, as shown by exact arithmetic here. Published attribution is preserved.
   - The prior t=3 mod4 theorem is listed with t>3, avoiding the unit t=3 edge case.

2. Moises Delgado and Heeralal Janwa, *On the absolute irreducibility of hyperplane sections of generalized Fermat varieties in P^3 and the conjecture on exceptional APN functions: the Kasami-Welch degree case*, [arXiv:1612.05997v1](https://arxiv.org/pdf/1612.05997), 18 December 2016; checked 2026-10-16.
   - Section 3, equation (5), attributes to Janwa--Wilson the decomposition for t=2^(2k)-2^k+1 into absolutely irreducible factors P_alpha of degree 2^k+1, indexed by F_{2^k} minus F2, with P_alpha(x,0)=(x+alpha)^(2^k+1).
   - Equation (6) explicitly groups Frobenius conjugates into F2-defined factors Q_alpha. This is relevant to the field distinction in the B4(b) target.
   - This author source has been checked, but the original 1993 Janwa--Wilson article has not yet been read in full. The original theorem should be verified before relying on it in a promoted proof.

3. [On the Decomposition of Generalized Fermat Varieties, Congressus Numerantium 232, paper 4](https://combinatorialpress.com/article/cn/Volume%20232/vol-232-paper%204.pdf), primary article located 2026-10-16. Its indexed text quotes the same Gold/Kasami decompositions and reports the absolute degree patterns for 13,57,241,993. The PDF has not yet been text-extracted/visually audited, so it is a lead rather than a relied-upon theorem source.

## Current-literature audit and limits

Search date: 2026-10-16. Queries included:

- `Simon Marais 2024 B4 polynomial modulo 2 n 205 solution`
- `phi n polynomial reducible over F2 Gold Kasami exponent 205`
- `Hernando McGuire Proof conjecture sequence exceptional numbers 205 factorization g205 arxiv`
- `Janwa McGuire Wilson 1995 absolutely irreducible polynomials GF2 3 mod 4 g_t pdf`
- `"reducibility" "Janwa" "2025"`
- `"reducible" "g_t" "205" APN`
- `"205" "13" "polynomial" "Hernando"`
- `"3277" "APN" polynomial`

The searched primary sources do not provide a complete B4(b) classification. The official 2024 notes explicitly describe only partial results. No later complete classification was located in this bounded search; absence of a search result is not evidence that no such work exists. Much newer APN literature concerns arbitrary lower terms or existence of a component, so its theorem conclusions must not be substituted for this target.
