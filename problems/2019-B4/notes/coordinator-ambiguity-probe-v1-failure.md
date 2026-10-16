# Coordinator extension probe: incomplete, no new theorem

2026-10-16 UTC. The intended length-28 extension used the author's frozen
targeted generator, seeded with the complete length-24 data, with a
2,000,000-node cap per layer and a 35-second external timeout. It was
exploratory work and receives no independent-review credit.

Child PID27345 was killed by the dedicated supervisor at the external
timeout and reaped (return code -9). Incremental output reports completed
layers25 (74 new minimal words) and26 (122), but the generator saves its
word list only at normal termination. Thus no extension JSON, complete
new word list, or proposed multiplicity report was saved. Do not use those
transient counts as a replacement for a reproducible complete dataset.
The output, stderr, source, PID, hashes and elapsed time are preserved.

There is also no reason to keep pursuing an all-two-history conjecture:
the already completed R1 independent length-24 audit reports four
length-19 minimal bad factors having three histories. The accepted rigid
families are special families, not a universal description. Larger caps
or a repeated long run do not address that mathematical obstruction.

This attempt changes no frozen input, accepted bound or review verdict.
