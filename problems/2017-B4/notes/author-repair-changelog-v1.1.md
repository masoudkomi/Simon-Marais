# Author repair checkpoint v1.1 — 2026-10-17

**candidate proof - unverified**

Revision author: `/root/owner_2017`, the original constructor of the 2017 second-pass packets. This is an author repair after reading both completed, frozen independent initial reports. It is not a third review, a claim that a reviewer has withdrawn an objection, or a coordinator promotion. The revised mathematical inferences need both targeted re-audits and coordinator acceptance.

## Preserved inputs and complete revised versions

All frozen `notes/secondpass-*` files, both initial review reports, and original `computations/secondpass-*` files remain byte-identical. The build manifest records all 17 input hashes before and after generation. Exact original candidate hashes matched the frozen review targets.

| Full revised packet | SHA-256 |
|---|---|
| `author-repair-macmahon-candidate-v1.1.md` | `a225f0042fc098d8a827093a3e680612848caf392db64cad24339d399769bcf0` |
| `author-repair-boundary-fiber-candidate-v1.1.md` | `e2891eafc6fa8449f6c70c817c2e21416a43f1893120929df02f2aa2dac86a8b` |
| `author-repair-periodic-grid-candidate-v1.1.md` | `1a6acb042e1e21bc0992cddbd7188c47e81249b5888faabaa4e73a45be0f5c6e` |

Each is a complete full version, not an addendum requiring the reviewer to assemble a proof from a patch. The same-prefix `-v1-to-v1.1.diff` files contain exact unified differences with four lines of context. Their hashes, old/new packet hashes and required re-audit count are in `author-repair-manifest-v1.1.json`.

## Repair map and remaining review obligations

| Frozen-review point | Author change in v1.1 | Why it is intended to address the issue | Status |
|---|---|---|---|
| **R1-G2-01; R2-G2-1**: uncovered boundary fourfold crossings survive frozen v1 | Defines R_m as every uncovered original multicrossing; explicitly includes (0,t) and (t,0). Places one fixed simple resolution in each disjoint small E_v before tail completion. Leaves only remaining simple crossings unchanged. | Finite positive separations allow disks avoiding large/counting supports, other vertices and nonincident lines. Proper ports and one fixed complete local wiring preserve all six crossing pairs at each fourfold point. The output is a simple partial arrangement, restoring the cited completion theorem's input. | **Proposed repair; both targeted re-audits required** |
| Same G2 point: choice count and exponent | E_v and its resolution are fixed before varying any counted choices; no new free parameters. All counted large-patch/triple choices survive and remain recoverable. K_m and t3 have their previous values/errors. | The fixed disks contribute one output each. They neither multiply the count by 8 nor delete previously counted parameter choices. The lower exponent and final coefficient are unchanged. | **Both targeted re-audits required** |
| Same G2 point: omitted band and corridors | Explicitly retains only interior translated cells, then shrinks/rounds in a vertex-free collar without losing a grid crossing. Any remaining multicrossing is nevertheless included in R_m. | The omitted support area remains in an O(m) boundary band. The fixed rational phases allow crossing-free collars. Hence there are O(m) residual fourfold points; none is silently left unresolved. | **Both targeted re-audits required** |
| G2 completion source hypotheses | Makes “simple partial arrangement” explicit and describes distant, disjoint O(m)-radius tail disks meeting just their own bundle. Retains the fixed reversal reconnection rather than treating parallel-child insertion as F3. | Central repairs preserve straight distant tails. Angular separation gives the private-disk hypotheses in the cited Section 4. Cross-family crossings and fixed marked labellings are maintained. | **Both targeted re-audits required** |
| **R1-G1-01; R2-G1-1**: original raw grid in remainder strips can have multicrossings | Replaces that instruction by iterated superadditivity and f≥0. States the positive remainders and omits zero-width terms. | No unresolved raw remainder grid is used. A positive remainder may instead take one fixed minimal realization of its full boundary word. | **Both targeted re-audits required** |
| **R1-F1-01; R2-F2-1**: exact four-packet theorem citation | Cites Felsner–Weil Theorems 7–8, printed p. 15, and Theorem 7's proof on p. 19. Retains the marked/fixed-left-order conventions and sign identification. | The source directly supplies four-set sufficiency and the local-permutation correspondence. Felsner–Valtr remains the tiling/local-sequence dictionary source. | **Both targeted re-audits required** |
| **R2-F1-1** and R1 exposition request: empty slots, bridges, designated face and Jordan boundary | An empty slot chooses A0's same exterior gap; two distinct port vertices are retained. The outer circle makes the retained graph connected. Rotations transfer the bounded face's port-corner walk. A thin regular neighborhood, with trimmed port collars, gives an actual Jordan disk. | It handles repeated facial-walk edges, empty slots and disconnected interior components without assuming that an abstract crossing graph determines an embedding. All removed components have ports and stay in the designated face. | **Both targeted re-audits required** |
| **R2-F3-1**: precise boundary hypotheses | States one proper simple arc with two distinct transverse boundary ports per participating strand, excluding tangencies and boundary segments. Defines F(empty)=1; F1 is stated for m≥1. | Disk boundary words and product factors are well-defined, including empty supports, without extending the official C(n) domain to zero. | **Both targeted re-audits required** |
| M2 full ternary / odd singleton-leaf convention | Defines a full ternary tree and states that its singleton-leaf family is empty for even n; bounded base blocks remain a separate extension. | Clarifies the model of an upper-counting obstruction. It makes no all-n lower-construction claim. M1 and M3 mathematics is byte-identical to v1. | **Both targeted re-audits required for revised wording** |

The author does not mark these review objections closed. Their actual resolution is for the reviewers and coordinator to decide from the frozen v1.1 bytes.

## Source record

The newly precise primary citation is the [Felsner–Weil author manuscript](https://page.math.tu-berlin.de/~felsner/Paper/sas-dam-rev.pdf), reused from ignored `.cache/literature/2017/secondpass-review-2-felsner-weil.pdf`:

```text
bytes: 395712
SHA-256: a6995529d08034c0735b3f9b0b9a4f9dae01ac0a5f3864d88728c6d04f85c828
```

I personally inspected the existing rendered primary pages 15 and 19 and checked the cached PDF fingerprint. The source record identifies those images and their frozen rendering provenance; old-font `pypdf` extraction was not treated as readable evidence. Theorems 7 and 8 are on printed page 15; the proof of Theorem 7 is on printed page 19. `author-repair-sources-v1.1.json` preserves URL, PDF/image hashes, inspection scope and cache-only status. No full paper or page image is included in the repair's tracked artifacts, and no new download or charge occurred.

## Reproduction and checks

From the repository root:

```sh
/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 problems/2017-B4/computations/author-repair-build-v1.1.py > problems/2017-B4/computations/author-repair-build-output-v1.1.txt
```

This standard-library builder checks the frozen candidate fingerprints, writes only its assigned `author-repair-*` destinations, generates full notes and exact diffs, asserts that the M1/M3 mathematical sections are unchanged, records the primary citation, and rechecks all 17 preserved input hashes. Its second execution regenerated identical bytes without warnings. A benign Python string-literal escape warning during the first build was removed by making the unchanged marker string raw; it changed no generated candidate or mathematical output.

There was **no new enumeration, CAS operation, native job, timeout, or higher-cap attempt**. Q(3,3)=4419734746 is unchanged. The original L=4 failed/capped run still supplies no count and enters no bound. Both initial reports independently reproduced Q(3,3), but that does not by itself accept the repaired construction. All source and finite-output status distinctions remain in force.

The coordinator supplied 9% total weekly used, reset timestamp 1792745187, with the 90% total-used cutoff unchanged. This author repair did not use a paid API, alter shared status/source files, commit, push, or promote a result. Requested launch settings remain `gpt-6.1-sol` / `max`; effective-setting readback is unavailable.

## Targeted handoff

Both reviewers should inspect the actual v1.1 files and exact diffs. The highest-priority changed inference is the G2 passage from counted local choices to a simple partial arrangement before private-tail completion. They must check simultaneous separation, proper ports, fixed resolutions, preservation and recoverability of counted choices, and the unchanged exponent. F1's explicit regular-neighborhood construction and the remaining source/scope/hypothesis clarifications also need targeted re-audits. Only the coordinator may accept the revised packets after both reports and resolution of all substantive objections.
