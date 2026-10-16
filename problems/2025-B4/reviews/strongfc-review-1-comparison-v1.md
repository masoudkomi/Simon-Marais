# Strong FC audit 1: post-freeze comparison and source check

Status: **candidate source audit - unverified by a second auditor**. This addendum does not promote a theorem or objection and does not change the frozen blind analysis.

## Sequence and integrity

The blind full reconstruction and issue list were frozen at `2026-10-16T21:38:04.824806+00:00`, before reading `problems/2025-B4/notes/deep-literature-r1-report-v1.md` or any other Strong FC review. The blind report SHA-256 is `84754caab660d3813dca115ea22bada2834510b7b2378a976ad4fea9be3f25b6`; the blind issue JSON SHA-256 is `162e3a3989f45d9ea095c2979420ca4806bc70dd75e384402da838cff18ef73c`. The companion blind manifest records their byte lengths and the hashed primary PDF. Only after that freeze was the permitted earlier literature report read.

The other fresh Strong FC review has not been read. The requested settings remain `gpt-6.1-sol`/`max`; effective-setting readback is unavailable. No Git operation, shared status change, or proof promotion was performed by this reviewer.

## Comparison with the earlier proposed concerns

The earlier report's Strong FC section proposes two concerns, explicitly as unverified. Both occur in the independently frozen reconstruction; neither was accepted merely because the earlier report stated it.

| Earlier proposed concern | Blind result | What remains to resolve |
|---|---|---|
| Lemma 5 infers divisibility by the product from separate divisibilities | Independently derived as SF1-01, with an exact characteristic-prime valuation calculation | The present proof cannot obtain an integral `chi'` by this inference. At any coefficient `n_c>k`, its desired quotient has valuation `mk-mn_c<0`. A replacement argument is required. |
| The nonrationality statement must account for norm group-ring elements `kN` | Independently derived as SF1-04, with the source's own use of `kN` located and an exact `p=5` integral-lattice calculation | Exclude norm elements by an actual valid selection and revisit the proof with that selection. At `p=5`, every element of `J_1` is `N`, so simply invoking Fact 2 does not give the element used by the claimed contradiction. |

The earlier report reasonably left open a possible specialized choice of `t` or disjoint-support repair. The independent audit narrows that option. Within the proof's positive equal-weight setup, coprimality of the two generators forces their group-ring supports to be complementary and `t=kN`. Then the needed nonrationality disappears. More fundamentally, the valuation calculation for `chi/beta(t)` depends only on the non-norm coefficients of `t`, not on how it is decomposed into two pieces. Rechoosing its two positive pieces therefore does not repair the displayed integral divisibility for a non-norm `t`. This is a precise obstruction to that proposed repair, not a proof that no different method can establish the theorem.

The earlier report did not claim to audit the entire proof. The following additional candidate issues arose in the blind reconstruction and are not conclusions borrowed from that report:

- SF1-02: the decomposition-group inference in Lemma 6. The unramified `(p,q,r)=(5,3,2)` example satisfies complete relative splitting over `Q(zeta_5)` but has 2 inert in `Q(zeta_3)`. This is a counterexample to the inference's general field premises, not to the Diophantine theorem.
- SF1-03: the intersection defining the universal ideal is used as a common-divisor ideal; rings, prime powers and ramification are not tracked sufficiently to yield a rational integer `D`.
- SF1-05: the missing `q` exponent and `e=1` denominator at (22). A hand local calculation at `p=11,t=psi_1+psi_2` yields valuation `h-1` for the difference-ideal product where the source asserts the full valuation `h` of `(X+Y)'`.
- SF1-06 and SF1-07: the sign in Lemma 4, division by `p-1` at residue characteristic 2, the normalization sign in (9), and the incompatible ideals/exponents in (18). Some restricted identities can be reconstructed, but they do not repair SF1-01 or SF1-02.
- SF1-08: literal boundary wording needs correction. Actual trivial solutions and the already established `q=2` example concern the literal wording, not the intended nontrivial odd-prime theorem.

## Testing the special nature of the equation against the generic countermodel

The `(5,3,2)` splitting example is deliberately limited. It does not exhibit `X,Y,Z` satisfying Strong FC, and therefore cannot refute the intended theorem. It establishes exactly this: from the relative splitting statement and the stated decomposition-group intersection alone, the claimed absolute splitting conclusion does not follow. The equation might impose extra constraints on the decomposition subgroup, but the proof would need to establish them. At a minimum it must show that the subgroup's projection to `H'` is trivial, rather than merely that its intersection with `H'` is trivial.

Likewise the Gaussian integer example in the blind report is a countermodel to an integral-divisibility rule under the indicated norm and coprimality conditions; it is not in the theorem's field and not a solution of its equation. The stronger obstruction in SF1-01 uses the paper's actual characteristic ideals and shows where the claimed quotient loses integrality under a hypothetical nontrivial solution. It is not an unrestricted Diophantine classification.

## Post-freeze primary-source version check

The version-specific PDF URL <https://arxiv.org/pdf/2509.18275v1> was opened through the web tool after the blind freeze. It is ten pages, and its extracted title-page date is `Version 1.0 September 24, 2025`, matching the cached PDF used in the audit. This makes the experimental HTML's displayed `August 24, 2026` date an HTML/PDF discrepancy, not evidence that the audited PDF has silently acquired that date. No new PDF bytes were downloaded or hash-compared in this post-freeze check; the precise audit identity remains the local SHA-256 in the blind manifest.

The submitted-v1 metadata remains 2025-09-22. Submission date, internal version date, HTML rendering date and audit date are kept separate. No journal acceptance, withdrawal or correction status is inferred from this limited check.

## Relevance and conclusion retained

The earlier report's signed substitution agrees with the independent mapping. Conditional on a valid proof, the theorem would exclude the official sector with prime term count `m=p>3`, `|x|>1`, and an odd prime divisor `q` of the perfect-power exponent that differs from `p`, using `e=0`. The exceptions `p=3`, `q=2`, `q=p`, composite term counts without a further reduction, and official signed/boundary families remain outside that import. No preliminary proof has been reproduced.

The two central proof barriers remain after the charitable notation repairs. The reviewed source should remain an unverified preprint claim until a replacement integral argument and a justified absolute-splitting argument are available and the coordinator's independent review process is complete. This is the audit recommendation; only the coordinator may make the project's status decision.

## Verification and budget record

Post-freeze checks: the blind issue JSON parses, `git diff --check --` on the assigned review paths returned exit 0, and the blind file hashes are checked again in the final manifest. No numerical search or CAS was used. The most recent account-wide weekly telemetry in this addendum's work was 16% total used, same 10080-minute window and reset `1792745187`; no reset was crossed. Runtime dependencies and the completed renderer session are recorded in the blind report. All authored files retain the assigned `strongfc-review-1` prefix.
