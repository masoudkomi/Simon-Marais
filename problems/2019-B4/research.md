# 2019 B4(b) research log

## Research significance and connections

Opening overview updated 2026-10-18. This problem asks how quickly the number
of distinct words grows under a simple rule that appends alternating symbols
at either end. Different construction histories can produce the same word.
Understanding those collisions is the central enumerative difficulty: the
number of histories alone does not determine the exponential growth rate.
The [official discussion](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-solutions_1.pdf)
gives initial bounds while leaving the two requested rates undetermined.

Our research connects the problem to combinatorics on words, forbidden-pattern
descriptions, and finite-state generating functions. Finite-memory envelopes
give controlled approximations; renewal decompositions would describe how
long words assemble from recurring pieces. These are methodological
connections, not an assertion that the complete language already has a
finite automaton or a rational generating function. In entropy language,
the growth constant measures the information retained after construction
histories are identified.

The project has independently reviewed existence of a common growth constant
and the enclosure \(1.765224<\lambda<1.834843\), together with converging
approximation structures and quantitative gaps for specified truncations.
The newly accepted [bivariate growth and pressure theorem](reviews/reasoning-growth-return-r1-acceptance.md)
proves M(a,b)<=lambda^(a+b) at EVERY bidegree, an exact complete
imbalance-moment identity and conditional random-length limiting laws.
Its finite-critical alternative has a uniform angular limit and a
pressure cusp; it does not establish that this is the actual regime.
Both OTHER ENTIRE WHOLE60-obligation audits and reconciliation are
complete. Its exact value, the actual renewal-moment regime, and sharp
asymptotics remain unresolved. See the [current dashboard](../../progress/dashboard.md)
and [review register](reviews/README.md); older bounds and pending-review
language below record earlier stages.

## Coordinator third-pass acceptance

The bounded-separation hierarchy, legal-envelope identification with actual minimal obstructions, entropy convergence, exact cap3 grammar and strict upperlambda<1.834856083 are **proved, independently reviewed partial results**. Both fresh initially blind reviewers reconstructed the whole argument and independently checked every cap7 transition and all11662 integer-vector inequalities. See proofs/reviewed-thirdpass-v1.1.md and reviews/thirdpass-acceptance.md/json. Combined with the earlier accepted lower bound,1.76521<lambda<1.834856083. Exactlambda/fullgeneratingfunction/novelty remain unresolved. No larger enumeration is substituted for the remaining proof problem.

## Coordinator acceptance update, 2026-10-16

The partial growth-limit, converging-enclosure and upper-bound arguments are now **proved, independently reviewed (partial results)**. Both fresh blind audits reconstructed the whole argument and independently reproduced the finite counts/certificate. The requested attribution repair was made by the author and rechecked by R1; no mathematical repair was needed. See reviews/acceptance.md. The exact growth constant remains undetermined. Owner-stage pending-audit notices below are historical and superseded by this update; separate exploratory notes are not covered by acceptance. Novelty is unestablished.

## Historical owner checkpoint

Date: 2026-10-16. Owner: `owner_2019`. Requested launch settings:
`model=gpt-6.1-sol`, `reasoning_effort=max`. Independent effective-setting
readback was unavailable; these are requested settings, not a claim about
verified backend execution. The owner constructed the candidate and cannot
serve as either independent adversarial reviewer.

Status: serious first investigation completed; **candidate proof - unverified**
of growth existence and an improved upper bound. No full solution of the
requested exact determination is claimed.

## Scope and statement fidelity

The official 2019 Paper B, p. 2, and the official solution notes, pp. 10–12,
were inspected through the primary-source browser on 2026-10-16. The
normalization in `statement.md` matches the seed, parity-dependent additions,
distinct-word counting and limiting quantities. Only (b) is explicitly open.
Following the coordinator's user-scope clarification, the research below
concerns (b) only. The existing (a) bounds are cited as published context;
no work on solving or reproving (a) is included.

## Exact language characterizations

1. **Endpoint deletion.** A word of length \(n>1\) is admissible exactly when
   an endpoint equal to \(n\bmod2\) can be deleted leaving an admissible
   word. The terminal admissible length-one word is `1`. This gives an exact
   interval dynamic program with an existential choice when both endpoints
   match; greedy choice is unsafe. It was independently checked against the
   forward generator for every binary word through length 14.
2. **Two subsequences of an alternating word.** Mark a possible original
   seed and write the final word as \(l1r\). The chronological left additions
   are `reverse(l)` and the chronological right additions are `r`. Their
   ordered shuffle must be `0101...` of length \(n-1\). Conversely such a
   shuffle specifies a legal history. Distinct marked contexts \((l,r)\)
   are retained, then the mark is removed to count distinct output words.
3. **Overlap grammar.** If \(a\) is the mandated next bit,
   \(B_{n+1}=aB_n\cup B_na\), whence
   \(b_{n+1}=2b_n-o_n\). Here \(o_n\) counts words \(x\) of length
   \(n-1\) such that both \(ax\) and \(xa\) belong to \(B_n\).
   This is exact but introduces additional overlapping membership predicates;
   no finite closed scalar recurrence has been obtained.

These characterizations are elementary candidate lemmas, included for audit,
not established new published theorems.

## Main candidate results and their roles

`proof.md`, version 1, gives all details.

- Marked contexts after an even number of moves compose. Their counts are
  submultiplicative and lie between the unmarked word count and that count
  times the number of possible seed positions. This gives a short candidate
  proof that the two quantities in (b) are equal: \(b_n^{1/n}\) has a limit.
- Fixing the marked position gives an injective block-substitution family.
  If \(M_k\) is the largest fixed-position class of \(2k\)-move contexts
  and \(C_k\) is their total, then
  \(M_k^{1/(2k)}\le\lambda\le C_k^{1/(2k)}\), with endpoint ratio at most
  \((2k+1)^{1/(2k)}\). Thus exact finite context enumeration yields
  converging enclosures and a computable representation, but no evaluated
  exact constant has yet been extracted.
- A 12-move context collision gives a lex-decreasing replacement in
  addition to the published four-move replacement. Every lex-minimal
  history avoids `RRLL` and `RRLRRLRLLRLL`. A 12-state automaton and a
  positive integer vector give the exact candidate inequality
  \(\lambda<1.83761\). The matrix proof uses integer inequalities;
  its numerical spectral radius is recorded separately as evidence.

## Exact finite computations

All scripts use Python 3.12.14, standard library only. Full parameters,
commands, outputs and hashes are in `computations/README.md` and the JSON
files. These are finite computational evidence, not a replacement for the
unrestricted arguments in `proof.md`.

- Direct distinct-word generation through \(n=25\):
  \(b_{25}=1417222\). Histories are never counted in place of words.
- Independent endpoint-deletion acceptance of all binary words through
  \(n=14\) matches the direct generator at every length.
- Marked contexts through 24 moves: \(C_{12}=2985943\).
- The largest 24-move fixed-position class has 395397 contexts, at twelve
  left moves. An independent enumeration of all 2704156 subsets of twelve
  source positions gives the same number. If the count survives audit,
  Lemma 3 yields the candidate estimate
  \(\lambda\ge395397^{1/24}\approx1.710841292477\).
- Exact automaton certificate: the minimum strict integer slack is
  174288855158; all twelve slacks are positive. Numerical spectral radius
  evidence is approximately 1.837605905420144, not used in the certificate.

## Failed or incomplete approaches

- **Count only numbers of zeros and ones:** necessary but insufficient.
  `1001` has the required two zeros and two ones and is not admissible,
  because both endpoints disagree with the first deletion bit 0.
- **Always delete the left matching endpoint:** fails already at `11001`,
  which is admissible. Left deletion gives `1001` and fails, whereas the
  successful deletion sequence is `11001 → 1100 → 110 → 10 → 1`.
- **Ordinary concatenation/submultiplicativity of unmarked words:** plain
  concatenation is not closed: `10` and `01` are admissible, but `1001` is
  not. Marked contexts or fixed-position seed substitution repair the
  counting argument.
- **Use only `RRLL ↔ LLRR` to identify all histories:** incomplete. Two
  `RRLL`-avoiding 12-move histories, `LLRLLRLRRLRR` and `RRLRRLRLLRLL`,
  already give the same marked context. Thus the published regular-language
  upper count cannot simply be declared the exact context count.
- **Declare the two-pattern avoidance automaton exact:** unsupported.
  It supplies representatives and hence an upper bound. A complete
  collision presentation or a confluence proof has not been found.
- **Fit a recurrence or extrapolate ratios:** not attempted as a proof.
  The saved exact initial terms are suitable evidence for future guesses,
  but finite agreement cannot establish a recurrence or asymptotic value.

## Next investigations

First obtain the required two fresh adversarial reviews, one reconstructing
the full partial argument. The first reports must be independent of each
other. Repair any substantive objections and request re-review of affected
parts before promotion by the coordinator.

For further research, enumerate minimal additional context relations with
bounded history length, checking that every proposed replacement preserves
both contexts at both bit parities. Seek a full canonical-form theorem;
without one, every finite avoidance automaton remains only an upper bound.
A second route is a direct characterization of which pairs can shuffle to
an alternating word, potentially producing an exact generating function.
The converging finite enclosures can produce precision only at substantial
cost; no uncontrolled large run has been started.
