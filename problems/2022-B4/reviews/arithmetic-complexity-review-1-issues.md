# Arithmetic complexity review 1: initial blind issue ledger

2026-10-16 UTC. Candidate SHA-256
`e9c24e96982d1d2a74aa97cb5fd045a3319f37c69316fbada884eeec0a0412d3`.
Read together with attribution supplement SHA-256
`b2ddb5337b0e669bab594916ed0e590a358feb812b0d8c338948372422786aed`.
No peer arithmetic-complexity report was read before this ledger froze.

| ID | Audit target | Finding / disposition |
|---|---|---|
| R1-AC-01 | Rational denominators in Z_10 | Resolved. Iterate `10^n vQ_n=A_n`, reduce modulo 10^n, then cancel the injective multiplication by 10^n. This gives vQ_n in Z without field division or an assumption that 2 and 5 are units. |
| R1-AC-02 | Bounded exception and nonzero divisor difference | Resolved. The full rational/controller state is deterministic and finite when C=0. When C!=0, strict monotonicity follows after a fixed n_0 and makes the divisible integer nonzero. A repeated-B loop supplies a real bounded rational example, confirming the exception is necessary. |
| R1-AC-03 | Official product condition and small quotients | Resolved. Bounded actual coordinates eventually become constant, which forces ab<=551. Positivity makes the product nondecreasing from >=600, including threshold equality and Q_0=0. |
| R1-AC-04 | Factor starts and off-by-one choices | Resolved. `ceil(t)-1<t` gives the strict comparison for M_L. Starts n_0 through M_L yield kappa L-O(1) factors. `P_S(L+1)>=P_h(L)` reindexes to the same slope. |
| R1-AC-05 | Mechanical partition and two-letter code | Resolved. There are k+1 half-open arcs, including the right-side convention at 0. Even and odd factor lengths both give P_h(L)<=L+3. An eventual odd period of h is handled by doubling it before decoding. |
| R1-AC-06 | Explicit avoiding lifts and signs | Resolved. Loop corrections are (0,0) and (-1,1), all d=1. Pairing the lift terms gives the positive series with denominator 121^(j+1). Finite ordinary positive lifts and the infinite nonrational lift are different assertions. |
| R1-AC-07 | Dubickas theorem hypotheses and method credit | Resolved by the frozen supplement. The scalar ceiling theorem is not imported directly; the official start (599,600) demonstrates its simplest identification fails. The divisibility-versus-growth method is credited as an adaptation, with no novelty claim. |
| R1-AC-SCOPE | Universal equality and general avoiding paths | Remaining research gap, not a defect of the stated partial theorem. High-complexity avoiding paths are not excluded. No full 2022 B4(b) solution is recommended. |

No substantive objection to the packaged partial claims remains open in
this review. The reviewer has not promoted the result. Retaining or
integrating the attribution supplement is necessary for an accurate final
presentation of the method; the frozen package already supplies it.
