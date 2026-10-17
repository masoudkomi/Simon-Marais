# Linear-output return: complete research and failed-route log

2026-10-17 UTC. Candidate proof - unverified. Parent assigned this work
only AFTER the complete blind CCL initial was frozen. The CCL report and
every older packet remain unchanged; its non-context-freeness statement
is not a premise of this new work. No peer CCL findings were consulted.

## Reasoning record

1. Reconstructed the supplied two-state grammar by deleting the final
   mandated symbol. Linear/reduced/strongly connected is immediate, but
   the grammar is ambiguous already at101. I did not assume a new
   unambiguous presentation exists.
2. Strengthened that warning symbolically: the alternating odd output
   (10)^k1 has EXACTLY2^k parses. Its outer two-step forms can only be
   prefix10 or suffix01, leaving the same smaller word. All derivation
   totals are2^(n-1), so the formal two-state matrix yields derivations.
   Accepted lambda<2 makes even their MEAN ambiguity exponentially large.
3. Derived exact original-language0*1* slices from the mandated symbol
   balance and explicit wrap0w1. They show that ORIGINAL unmarked B,
   O and E are nonregular, while the grammar proves linear context-freeness.
   This does not establish inherent ambiguity or a nonrational series.
4. Checked the extra occurrence clause in the primary linear-ergodicity
   definition, rather than treating strong connectivity alone as enough.
   Any binary pattern is a subsequence of alternating emissions; send
   precisely its chosen letters left. This gives a whole contiguous
   terminal block in a nonterminal sentential form, from either state.
5. Eliminated E into four legal odd operators P,Q,R,S. Their three
   nonempty pair intersections are exactlyI,I,J; all other pairs are
   disjoint by a first/last letter, so there are no triple intersections.
   This gives the DISTINCT-word recurrence, separate from weighted equations.
6. Identified a dangerous short-boundary mistake before freezing: J0 is1,
   since10*1=1*01, whereas rewriting through a length-1 middle word would
   lose that fixed-prefix/suffix overlap. The middle-word rewrite is used
   only fork>=1. I0 is0. No constructor code was run to find these.
7. Tried J_k=a_(k-1), because every old odd word gives a J overlap by
   prefix/suffix extension. Exact counterexamplet01110 defeats it:
   t is notodd (both ends0), yet10t=Q(R²(1)) andt01=R(Q²(1)). This
   is one hand-derived counterexample needed for a proposed finite closure,
   not an enumeration. No claim that ALL finite closures are impossible.
8. Constructed fixed-length recoverable injections O_k->J_(k+1) and
   O_k->I_(k+2). Together with projections back to O_k, both overlap
   counts have the SAME exponential rate as original outputs. Treating
   them as subcritical correction languages would be an unjustified step.
9. Wrote the formal generating identities. Their apparent pole at1/2
   cancels because acceptedlambda<2; exact2I(1/2)+J(1/2)=4 is a
   normalization, not a solution forlambda. Same-radius overlap series
   are the unclosed part of the count problem.
10. Used the pattern occurrence construction to give an explicit
    weighted avoidance bound: in each even blockL=2|f| of productions,
    one orientation pattern forces f into the terminal word. This loses
    at least one of2^L choices perblock. It proves a rate below2 for
    derivation-weighted avoidance, but not a rate belowlambda for
    DISTINCT-word avoidance.
11. Preserved the conditional finite rational route: a proper finite
    UNAMBIGUOUS linear grammar would give a genuine disjoint linear
    series system and a rational distinct-word series. Neither linearity,
    nonregularity nor one ambiguous presentation establishes that premise.

## Primary literature and access work

Read the complete official part(b) normalization and accepted proof.md;
older reference/method notes were checked before claiming a new route.
Primary source searches included exact titles, author/year and
"context-free entropy computable growth rate ambiguous". Secondary
discovery hits were not used as proof authorities. No primary theorem
about unrestricted ambiguous distinct-word entropy was located and
applied; absence of such a retrieved theorem is not an absence claim.

The full2007 published article was read through web.run's public PDF
viewer, with bounded open ranges around lines0,330,510,425,645. Those
overlap and cover its entire text, including the proof/weighted section
and references. Its SOLO author/electronic-versus-print dates were checked.
The2005 primary abstract was read, full text unavailable; no theorem
from the unread body is imported.

Public command template, always with certificate verification:

```
curl -L --fail --silent --show-error --max-time 30 URL -o CACHE_PATH
```

Actual attempts (all on2026-10-17 UTC):

* AMS URL
  `https://www.ams.org/journals/tran/2007-359-02/S0002-9947-06-03958-4/S0002-9947-06-03958-4.pdf`
  ->curl56,HTTP403, completed in about0.18seconds. No access bypass.
* Citeseer URL supplied by parent
  `https://citeseerx.ist.psu.edu/document?doi=73e6ff5c84a6f9944fd5ac785cce02d215ef7967&repid=rep1&type=pdf`
  ->session82838, --max-time30; completed curl56,HTTP404 and was
  reaped by bounded write_stdin poll. It was read-only HTTP retrieval,
  not a native mathematical child. No job remains running.
* Public PDF-copy URL
  `https://scispace.com/pdf/growth-and-ergodicity-of-context-free-languages-ii-the-4xfrjcv85s.pdf`
  ->curl56,HTTP403. The SAME published article's text was accessible
  through web viewer. No binary success or hash is claimed.

The cache directory `.cache/2019-B4-linear-output-return-r1/` was created
for these authorized public attempts. Failed requests supplied no
mathematical evidence. No downloaded full paper is added to tracked files.
No paid material, restricted institutional file, person contact or
subscription was used. No separately billed API was used.

## Operations and remaining gap

Only this assigned notes prefix was written. No mathematical program,
word generation, table, CAS, scan or old certificate/constructor rerun
was performed. Administrative Python hashes/JSON are explicitly separate.
No Git or shared-file edit, spawning, global process cleanup, contact,
charge or access bypass occurred. Current direct authoritative weekly
telemetry at11:47:01UTC was35% TOTAL, reset1792745187; stop ceiling90%
TOTAL with integration/review reserve, no automatic new-window spending.
At the checkpoint transition11:59:03UTC the direct authoritative meter
was rechecked:36% TOTAL, same10080minute window and reset1792745187.

This is a COMPLETE meaningful partial checkpoint, not a completed count.
The exact overlap hierarchy is unclosed, ordinary growth-sensitivity is
not established, another unambiguous presentation is not constructed
or excluded, and lambda is unevaluated. Two OTHER fresh whole initially
blind audits are required for these proposed scoped results. The newly
queued Kasami whole-criterion review begins only after this checkpoint
and its preservation/hash freeze are completed.
