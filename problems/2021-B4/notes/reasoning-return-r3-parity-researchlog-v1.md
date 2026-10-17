# Odd-support projection research log

2026-10-17 UTC. **Candidate proof - unverified.**
Continuation after freezing the collision-depth packet; all older
packets remain unchanged.

The repeated-root even ladder forces the middle even normalized
coefficients to vanish modulo19. Once H18 has a noncenter witness,
the Euler reflection error also forces a2,a4 nonunit. Together with
D1, all even normalized coefficients vanish modulo19. This suggests
a parity projection rather than another small-root digit tree.

The main proposed PP1 deliberately takes all-even nonunits as an
EXPLICIT hypothesis. It applies to any full J15 multiplicity-two
normalized rational-witness polynomial with H3 at1 and that parity
condition, not just the repeated-root application. PP2 reconstructs
the repeated-ladder implication directly instead of treating the
earlier unreviewed collision packet as a theorem.

The residual D17 has roots0 and1, exact multiplicity2 at0, and
each lower normalized derivative has root0 or1. This makes a
genuine positive-characteristic degree17 CA polynomial with a
two-value cover. It is not a characteristic-zero counterexample,
and two recycled values in positive characteristic are allowed.

The unit support is a subset of odd indices1,3,...,15 containing
both1 and15. Triangular center recursion lifts it to an integer
vector b_j. Its polynomial F_I(Z)=sum b_j binom(Z,j) agrees,
up to sign, with the classical descent polynomial d(I;Z).
The endpoint D17(1)=0 gives19|d(I;17); the DIVIDED original
root equality gives19^2|d(I;20). Since degree15<19 and1 is an
exact polynomial root, these are equivalently d(I;-2)=0 and
d'(I;1)=0 modulo19.

The precise unresolved target is a joint nonvanishing theorem for
these two endpoints and the support nonvanishing conditions.
I did NOT establish it, assert it true, enumerate the64 possible
odd subsets, rerun any accepted mask data or claim a rational lift.
The reduction itself is recorded because it gives a source-driven
combinatorial question rather than substituting a larger table.

Attribution and source checks:
- Read the original arXiv1710.11033v2 full-text Proposition2.1 and
  its proof, Theorem2.2, Theorem2.3 and Theorem4.1; browsed relevant
  coefficient and root-bound passages. The recurrence and descent
  polynomial are published, not new here.
- Read Marashdeh arXiv2608.14726 introduction TheoremB and its
  explicit multi-root limitation, plus surrounding support results.
  Its general one-nonzero-recycled-root/MacMahon connection is
  attributed. No unrestricted multi-root theorem is imported.
- Searched for parity/descent congruences. No applicable joint
  nonvanishing result was verified in this bounded search; that
  does not establish novelty or absence from the literature.
- Primary Cima--Gasull--Manosas 2020 full-text introduction was
  checked for the meaning of the real-root variant. It assumes
  all roots real, which is stronger than rational witnesses.
  Its uncorrected degree24 status sentence is not used: the
  original2011 erratum separately retracts the degree20 shortcut.
- No source was downloaded into a local file in this step, and no
  byte hash of a live viewer response is invented. URL, version,
  accessed sections and date are retained in the source record.

Unsuccessful conceptual shortcuts:
- Four rational witness values do not mean f splits over Q or R.
- A large Galois group for the unused factor is not a contradiction.
- Archimedean bounds on descent roots do not forbid congruence
  zeros modulo19.
- Positivity of descent counts over Z does not imply they are
  nonzero modulo19, let alone modulo19^2.
- All-odd-support principal minors resemble tangent-number
  recursions, but no assertion that all of them are19-units is
  justified. The all-odd example alone is not an infinite criterion.
- The two endpoint conditions are simultaneous conditions on the
  SAME support. Treating them as conditions on independently
  selected supports would lose the proposed obstruction.

No mathematical program, enumeration, CAS, higher Hensel digits,
mask broadening or old finite certificate rerun was performed.
The only executable work is metadata hashing and JSON creation.
No shared/Git changes, contacts, charges, access bypass, spawning,
or separately billed API.

Requested gpt-6.1-sol/max; effective readback unavailable.
Authoritative weekly total remains23%,reset1792745187,10080-minute
window,ceiling90% total with integration reserve. Two fresh
nonconstructor whole audits are required for PP1/PP2; only root
may accept a result.

