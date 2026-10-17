# A hole in the viable-seed set of an actual original output

2026-10-17 UTC. **Failed shortcut / hand-checked observation, not a reviewed theorem or growth result.** Root. This concerns the actual original strings and seed marks, not a range statistic of unrelated tape pairs. No interval property is used by the accepted counting results.

A tempting simplification is that viable seed positions form an interval in the order of the word's one positions. The concrete word

    w=100111001

has viable zero-based positions3 and5 but not4. Thus even this simple interval assumption fails.

For seed3, take chronological left tape u=001 and right tape v=11001. Interleave source01010101 with history

    L R L R R L R R.

The left contributions at times1,3,6 are0,0,1; the right contributions at2,4,5,7,8 are1,1,0,0,1. Thus the actual output is reverse(u) 1 v=100111001 with seed3. These are legal alternating additions starting at1, not just balanced bit counts. The word is its own reversal. Reversing every output and swapping the side choices therefore gives the viable symmetric seed5.

For seed4, both immediately adjacent bits are1. The first required addition to a seed is0, and it would have to occupy one of those adjacent positions. Neither side is possible. Equivalently both chronological tape heads are1 while the first required source bit is0. Thus this seed has no history. In fact the only other one positions are0 and8: at either endpoint all additions must be to one side, whose chronological tape begins00, again impossible. So the viable set is EXACTLY{3,5}.

This also gives the elementary necessary local check: an interior viable mark other than the length-one seed must have a zero immediately next to it on at least one side. This check is necessary only, not sufficient. It does not decide the aggregate number of marks or its typical order. One rejected interval idea supplies no actual renewal-defect conclusion.

## Narrow diagnostic and limits

The accompanying diagnostic was run solely to seek a counterexample to this conjecture. It propagated exact sets of seed positions under the four legal two-step maps10w,1w0,0w1,w01, with the corresponding position shifts2,1,1,0, from seed1. It was capped at odd length15 and stopped on its FIRST discrepancy at length9/k4. Dedicated child24520 completed/reaped with exit0 in0.0175seconds, external timeout20seconds unused; exact code/output/job/stderr are preserved. It did not run through the unused length15 cap or enumerate further data after finding the word. The unrestricted negative interval observation rests on the direct hand argument above, not an extrapolation from bounded checks. No minimality beyond this diagnostic convention is claimed.

## Further literature check, with actual access scopes

The original-output grammar is already known here to be linear and its displayed presentation ambiguous. That does not establish inherent ambiguity or an unambiguous alternative. A new bounded search located primary Ceccherini-Silberstein2005 *On the growth of linear languages*, DOI10.1016/j.aam.2005.01.002, https://www.sciencedirect.com/science/article/pii/S0196885805000321 . Only the actual publisher abstract was inspected: its algorithm concerns the UNAMBIGUOUS subclass and the polynomial/exponential alternative, not an exact value for our language. Its full proof was not read/imported.

The2007 follow-up *Growth and ergodicity of context-free languages II: the linear case*, DOI10.1090/S0002-9947-06-03958-4, was found through indexed original text: the stated theorem also requires unambiguity. A Citeseer public PDF open returned an internal error; search text is discovery only, and the full proof is unread. No access bypass, fee or native retry occurred. Flajolet1987 *Analytic models and ambiguity of context-free languages*, https://www.sciencedirect.com/science/article/pii/0304397587900119 , primary publisher abstract only, explains why algebraic enumeration needs the appropriate unambiguous hypotheses; no full-paper theorem was applied. Other broad search hits and snippets were not used as proof.

No claim of general CFL entropy computability/noncomputability, algebraicity, growth sensitivity, full grammar, exact lambda or novelty follows. All earlier candidate/review/accepted bytes are intact; no new proof is promoted from this failed-route note. Primary-source discovery does not discharge the missing grammar hypotheses.
