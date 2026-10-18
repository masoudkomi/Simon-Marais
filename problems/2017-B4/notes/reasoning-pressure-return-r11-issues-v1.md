# R11 constructor issue ledger

Candidate proof - unverified; no independent review has yet occurred.

| ID | Issue or danger | Resolution / remaining scope |
|---|---|---|
| R11-I01 | Raw sigma2>1 forbids ordinary substochastic flow | Resolved in proposed proof: all rows normalized before flow; exact chi factor retained and paid by chi^2*a<1. |
| R11-I02 | Two reconvergent diamond routes might be counted once | Resolved: first edges disjoint; unfolded prefix tree retains both, mainM3--M4. |
| R11-I03 | High-degree middle successor may have arbitrarily small individual transition | Resolved: if bad, sum full continuation1 with its own discount; individual lower bound only at degree3/4. |
| R11-I04 | Old rho discards the stronger degree2 loss | Resolved: s0/s3 flags retained separately, bottom reverse degree2 pays s0. |
| R11-I05 | Initial/terminal factors and touching trials | Resolved: positive rows only, symmetric R; full product<=disjoint target product, mainM4. |
| R11-I06 | Improving K alone may fail to improve current H | Resolved by separate full-interval hand comparison, mainM6. |
| R11-I07 | Actual-class moment could secretly count words or schedules | Resolved using one canonical largest-label deletion chain per actual marked class, mainM7. |
| R11-I08 | New partial upper might be mistaken for exact entropy/computability | Remains explicitly excluded: exact value, upperR, matching lower/typical law/annual/priority not proved. |

No constructor-identified unresolved defect in PR11A--PR11D is claimed
to be independently resolved. The OTHER whole64 auditors must check all
issues, formulas, endpoints and sources before any promotion.
