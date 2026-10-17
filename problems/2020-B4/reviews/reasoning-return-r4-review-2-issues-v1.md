# R4 whole review2: issue and per-inference ledger

2026-10-17 UTC. Initially blind nonconstructor review of the NEW R4
argument. Old repaired R3 F1/F2 authorship is disclosed and does not
count as an independent re-audit of those accepted dependencies.

## R4R2-01 — final moment congruence is automatic, not essential

- **Status:** open; author versioned correction and affected review needed.
- **Type:** false auxiliary mathematical assertion; the full E2 iff remains valid.
- **Location:** candidate lines351–352 after(E2); closing lines463–465
  should also be qualified insofar as the shortened-list warning covers
  exactly this redundant final row.
- **Claim challenged:** that B_L=-1 is essential and that the preceding
  congruences alone are not sufficient in the stated D_epsilon domain.
- **Exact contradiction:** for ANY actual k-element subset A of F_ell with
  k(k-1)=ell-1, every off-diagonal(a-b)^(ell-1) is1 and each diagonal
  contribution is0. Thus its last difference moment is k(k-1)=-1 mod ell
  automatically. By the candidate's correct moment identity, this is B_L.
- **Independent binomial check:** binom(ell-1,im)=(-1)^(im) mod ell;
  m odd makes every sign-corrected interior summand1. Hence

      B_L = 2m(m+epsilon)+m²(L-1)
          = m²+(2epsilon-1)m = -1 mod ell.

- **Sufficiency of the shorter list:** the earlier congruences plus the
  automatic moments give equality with the target at every j=0,...,ell-2.
  Also mu(0)=nu(0)=k. Delete that known zero column. The square evaluation
  matrix at all ell-1 nonzero residues with degrees0,...,ell-2 is
  invertible, so the two count vectors agree modulo ell. The existing
  bound0<=mu(z)<=k<ell lifts each nonzero count to1. No numerical example
  or search is needed; this proves the purportedly insufficient list
  sufficient throughout the given parameter domain.
- **Requested repair:** retain the full E2 iff if desired, but replace
  the false necessity/insufficiency sentence with an accurate statement
  that the last row is included for completeness and is automatic here.
  Qualify the broad closing shortened-list warning. Check corresponding
  explanatory material without overwriting frozen v1.
- **Unaffected arguments:** R4A–R4D, the full E2 equivalence, its integer
  lifting, the L2 versus interior distinction, E5, and the3|m consequence.
  The final row still has value-1 rather than0; redundancy is not license
  to replace its right-hand side with0.
- **No external claim:** this is not an objection to Cohen, Hall, Xia,
  any old accepted theorem or a full Prime Power Conjecture conclusion.

## Complete36-row inference audit

PASS below means independently reconstructed within the declared input
and attribution scopes. It is not coordinator promotion. The auxiliary
defect is recorded even though the named R4E iff survives it.

| Author ID | Review2 disposition and reconstruction |
|---|---|
| R4-O01 | PASS. Official n>=2, q=n-1; new q>=2 excludes only the separately accepted boundary. No preliminary construction reproduced. |
| R4-O02 | PASS. gcd(k,v)=1 gives one sum-zero translate; kc0 forces every multiplier shift0. |
| R4-O03 | PASS as a separately accepted OLD input. Actual unique difference representation fixes both points for EVERY U member. No false old F4 substitution. |
| R4-O04 | PASS. h1 gives f0/1; h3 gives m1; proper nondegenerate subplane uses external-point line count. Old authorship disclosed. |
| R4-O05 | PASS. q>=6 gives q(q-6)+1>0, contradicting the cover cardinality. |
| R4-O06 | PASS. Prime moduli7,13,31 make each nonidentity fixed group{0}. |
| R4-O07 | PASS. Only size3 and size7 groups can cover five points, with actual counts2,3 and0 absent. Retained difference list and multiplier cycles checked by hand. |
| R4-O08 | PASS. Distinct ordered multiplier pairs imply t1!=t3; uniqueness gives the two-kernel cover without canceling d. |
| R4-O09 | PASS. Ratios t1/t2 and t1/t3 are nonidentity units in M; multiplication by a unit preserves the corresponding kernels. |
| R4-O10 | PASS. Additive Sidon count gives |M|<=q+1; q4 collision has the two actual covering kernels. Classical attribution retained. |
| R4-O11 | PASS WITH EXTERNAL IMPORT. Cohen's actual original definition/Theorem1 checked, 1<k<v-1 satisfied; full sieve proof not reconstructed. |
| R4-O12 | PASS. Both exceptions are(21,5,1), excluded by q!=4. The theorem is applied to the actual normalized D; no translation-invariant unit claim. Missing fresh native hash disclosed. |
| R4-O13 | PASS. Cancellation of UNIT d gives orbit size s and unit orbit members. Orbit selection remains necessary only. |
| R4-O14 | PASS. Every nonidentity U fixes no unit, irrespective of U/T containment. |
| R4-O15 | PASS. Disjoint actual subsets give s+f<=q+1; f=m+1 yields C1 and its exact-cardinality equality case. h1 stays separate. |
| R4-O16 | PASS AS CONDITIONAL OLD INPUT. An actual involution is required; F2 then supplies m=sqrt(q). No squareness converse. |
| R4-O17 | PASS. q<=s<=q+1 gives at most one D-point outside dT. |
| R4-O18 | PASS. Actual F1 on EACH t forbids h_t>1 when its fixed D-intersection has at most one point. |
| R4-O19 | PASS. Prime reduction injectivity follows by quotient t/t'; s divides ell-1. Composite v contradicts the product lower bound, including repeated factors. |
| R4-O20 | PASS. Non-opposite D-pair excludes global negation. Prime v is proved before invoking the unique involution in its unit group. |
| R4-O21 | PASS. Invariant singleton complement is fixed by T and is0; unit scaling gives the exact two shapes. |
| R4-O22 | PASS. s divides |M| in the short interval[q,q+1]; full M=T follows only here. |
| R4-O23 | PASS WITH ACCEPTED HALL IMPORT. Products of prime-divisor multipliers give q; q has exact order3, giving the two mod6 branches. |
| R4-O24 | PASS. Actual affine collineations make the even one-orbit row flag-transitive. No non-Desarguesian or odd-row theorem imported. |
| R4-O25 | PASS. Odd m>=3, epsilon0/1, prime ell imply even L>0, ell-1=mL=k(k-1). Subgroup order m is distinct from cyclotomic index L. |
| R4-O26 | PASS. S0 separately defined; positive power sums over H and zero member correct. |
| R4-O27 | PASS. Every surviving binomial position and sign is accounted for; m not dividing j gives zero. |
| R4-O28 | PASS FOR VALUE; SEE R4R2-01 FOR NECESSITY CLAIM. Odd moments vanish and last target is-1, but this last equation is automatic. |
| R4-O29 | PASS. Constant moments both k²; complete target positive sums correct. |
| R4-O30 | PASS FOR THE WRITTEN FULL MATRIX PROOF; auxiliary insufficiency claim fails. All ell evaluations invert correctly. A shorter matrix on the nonzero residues also works once mu(0) is known. |
| R4-O31 | PASS. Actual mu(0)=k and0<=mu(z)<=k<ell justify exact integer recovery. |
| R4-O32 | PASS FOR STATED FULL E2 IFF. Both directions work only for the prescribed actual shapes. The particular final-row omission also suffices; see issue. |
| R4-O33 | PASS. E5 uses t2 as an interior equation only for L>2; final L2 value is-1. Redundancy does not change that value. |
| R4-O34 | PASS. H preserves the actual shape, which has sum zero by S1=0; q4 cannot occur under these parameter hypotheses. Saturation/Hall then force3|m. |
| R4-O35 | PASS. Classical overlap and explicit import are attributed, with no novelty claim. |
| R4-O36 | PASS. Nonsaturated branch and unbounded congruence system remain unresolved; no new mathematical computation or published cutoff is claimed. |

Open substantive issues within the complete new packet: **one**.
Open objections to the core R4A–R4D conclusions or complete E2 iff: **none
identified in this review**, with the source/proof limits stated above.
No peer findings were read before this ledger and whole report froze.
