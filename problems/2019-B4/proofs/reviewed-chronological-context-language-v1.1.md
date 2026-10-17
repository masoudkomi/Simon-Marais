# Accepted chronological-context-language: coordinator status and scope

2026-10-17 UTC. **Proved, independently reviewed scoped partial result.**

CCL is accepted exactly for the stated separator serialization of finite chronological routing pairs. Its regular positive-even four-run intersection is EXACTLY {0^(2a)1^(2b)#1^(2a)0^(2b):a,b>=1}. The complete slice proof treats the final initial-run pair ambiguity, both choices when A<C, one extra zero before A>C fails, the A=C forced crossing, opposite suffix runs and excluded odd endpoints. Sufficiency is explicit for every pair of exponents. Pumping defeats EVERY eligible context-free decomposition at exponent2, including a separator in the unpumped middle and both central1 blocks touched. Standard regular-intersection closure gives the claimed non-context-freeness.

Both fresh initially blind nonconstructor WHOLE audits reconstructed all15 obligations, with15 and27 checks. Root read the entire candidate, obligations and sources plus BOTH COMPLETE reports, full inference ledgers and actual-source records before reconciliation. No substantive objection or required repair remains. Root is the constructor, not an independent auditor. Reviewer2's older NR authorship and moment-review role is disclosed; those older nonregularity/counting results are NOT mathematical premises of this new proof. The chronological dictionary is also directly reconstructed from insertion order.

The proof concerns ordinary finite words and allows the empty source outside the positive-run slice. The physical left component is reversed and the seed marked; no partial-reversal context-free closure is assumed. Variable-input constrained-shuffle hardness is contextual only and is not imported for fixed two tapes or the annual count. No mathematical program, routing scan, CAS, finite table, constructor rerun or certificate replay supplies the proof.

This result does NOT determine context-freeness of canonical histories or original unmarked outputs, rule out every encoding, prove a nonrational or nonalgebraic generating series, improve the numerical enclosure or determine exact lambda. The original output language's separate linear-grammar research remains unverified and outside this acceptance. The full annual target and novelty remain unresolved.

The complete frozen submission follows as a byte-identical suffix. Its historical unverified labels and conditional statuses record the submission date; this header and the acceptance record state the current scope.

---

# The serialized chronological context language is not context-free

2026-10-17 UTC. **Candidate proof — unverified.** Root constructor. Two independent nonconstructor WHOLE audits are required. This concerns one precise encoding of the accepted chronological contexts, not the least-history language, original binary outputs, or algebraicity of their counting series.

Let C be the set of all chronological output-tape pairs(u,v) formed by routing each successive letter of the alternating source0101... to exactly one of two tapes, preserving order on each tape. Include all finite source lengths, including0. The earlier accepted dictionary identifies these pairs with marked contexts, after reversing the physical left tape. Let

    L_C={u#v : (u,v) in C},

where # is a new separator. The proposed statement(CCL) is that L_C is not context-free. No regularity or context-freeness assertion about a different encoding follows automatically.

## 1. An exact regular slice

Let R=(00)+(11)+#(11)+(00)+, where each plus means one or more copies of the displayed two-letter block. Thus words of R have the unique form

    0^A 1^B # 1^C 0^D

with A,B,C,D positive EVEN integers. I claim

    L_C intersect R
      ={0^(2a)1^(2b)#1^(2a)0^(2b) : a,b>=1}.       (1)

To prove necessity, consider the unread tapes u=0^A1^B and v=1^C0^D at an even source time, initially0. Until one of the initial runs0^A and1^C is exhausted, a source pair01 MUST take0 from u and1 from v. Indeed two successive0s in u prevent taking the1 there unless its0-run has just ended; two successive1s in v prevent supplying the0 there before its1-run ends. During the first min(A,C) pairs, a potential last0 of u could be followed by its own first1, but only at the last pair when A<=C. This exceptional choice must be handled, rather than silently declaring every pair forced.

For the first min(A,C)−1 pairs neither initial run can end, so these pairs are forced. At the final such pair there are three cases:

- If A<C, u has its last0 while v still has at least TWO initial1s, because A,C are even. The1 may be taken from either u or v. If from v, both unread heads are1 at the next required0. If from u, both unread heads are again1, since B is even and B>=2, so at least one left1 remains. Both choices fail.
- If A>C, u has at least TWO initial0s while v has its last initial1. The0 is forced from u and the1 from v. Both new heads are0; at least one left0 remains and v contains only0s. After any next0, a1 is inaccessible. This case fails.
- If A=C, the final0 is forced from u. Taking its next1 also from u would leave a left1, because B>=2, and the right head is still1; the next required0 is impossible. Thus the1 must come from v. Exactly A cross-tape01 pairs have been consumed, leaving u=1^B and v=0^D at the next even source time.

In the last case every following complete01 pair is forced to take0 from v and1 from u. If B=D, all letters are consumed legally. If B<D, after B such pairs the only unread letters are D−B zeros; this difference is a positive EVEN integer, so consuming its first0 leaves no source1 accessible. If B>D, after D pairs only left1s remain while the next source letter is0. Thus success requires B=D. This also excludes completion at an odd source length: the even run constraints prevent the one-extra-zero endpoint.

Sufficiency is explicit. For A=C and B=D, route the first A source pairs with blocks LR and the next B pairs with blocks RL. This yields precisely u=0^A1^B and v=1^A0^B. Equation(1) follows. Every run and time is finite and ordinary; no table or empirical pattern is used.

## 2. The slice is not context-free

Suppose the right side of(1) were context-free and let P>=1 be its context-free pumping length. Take

    w=0^(2P)1^(2P)#1^(2P)0^(2P).

For any pumping decomposition w=uvxyz with |vxy|<=P and |vy|>0, the window vxy cannot meet BOTH of the matching block pair(first0 block, third1 block), nor BOTH of the other matching pair(second1 block, fourth0 block). The intervening full block alone has length2P. A window may meet the two central1 blocks across#, but those are not a matching pair in(1).

If v or y contains#, pumping twice creates more than one separator, leaving the language. Otherwise at least one binary block gains a symbol when v and y are repeated. If the resulting word breaks the required block order or even run parities, it is already outside the language. If it retains that form, choose any block whose exponent increases. Its MATCHING counterpart cannot meet the pumping window and therefore cannot increase. One of the equalities A=C or B=D is broken. In every case uv²xy²z lies outside(1), contradicting the pumping lemma. Hence the slice is not context-free.

Context-free languages are closed under intersection with a regular language. If L_C were context-free, its intersection with R would be context-free, contrary to(1). This proves the proposed CCL statement.

## Scope, source context and remaining count problem

The only project premise is the accepted chronological routing dictionary; the slice proof itself is supplied in full. Ordinary context-free pumping and regular-intersection closure are used in their standard finite-word forms. [Amarilli–Paperman, ICALP2018](https://paperman.name/data/publi/10.4230.LIPIcs.ICALP.2018.115.pdf), §2's constrained-shuffle definitions and §3 Theorem3.6, were directly inspected as terminology/context. Their variable-number-of-inputs hardness is not a premise or a hardness conclusion for this fixed-two-tape problem.

The conclusion rules out a context-free grammar for THIS separator serialization of chronological pairs. It does not prove that the canonical HISTORY language is non-context-free, that the original unmarked output-string language is non-context-free, or that no other useful encoding/grammar exists. In particular the physical left word is reversed in the official string; partial reversal of a component must not be treated as a context-free closure operation. Non-context-freeness alone also does not establish a nonalgebraic counting series or determine lambda. The current numerical enclosure remains unchanged. No computation, scan, full annual solution or novelty is claimed.
