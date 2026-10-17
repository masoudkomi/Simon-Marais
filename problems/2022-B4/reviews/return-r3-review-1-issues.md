# 2022 return-r3 whole review R1: claim-by-claim issue ledger

2026-10-17 UTC. Initially blind whole review of the original candidate
SHA-256 `eb3d176680116595015069507f3904a0d048e44d3c2cde06965647010b82764e`
and supplement SHA-256
`a0512f751dc5c648043025948a841fa4ecffb280785641c5e85f9fae5c99bca3`.
No substantive objection remains; no author repair is requested. “Pass”
below means independently reconstructed in the stated scope, not promoted.

| ID | Claim / audit target | Disposition and reason |
|---|---|---|
| RR1-01 | Official domain and simultaneous update | Pass. Positive integers, inclusive product >=600 and time-zero equality match the primary paper. Only B4(b) is investigated. |
| RR1-02 | Full ten-control strip and signed correction bound | Pass using accepted strip closure. The residue formula supplies all ten branches; c in {-3,0,3,6} gives -10<=h<=10 without enumeration. Equality is not a stopping condition for this controller. |
| RR1-03 | Finite lifting versus infinite Z10 lifting | Pass. The accepted finite bijection realizes arbitrarily large positive starts for each finite prefix only. The inverse-limit ring and fixed denominator are handled without field division. |
| RR1-04 | R0 exact sum identity and real growth | Pass. Remainders sum to at most 48; the coefficient series has total weight 1. Product >=600 forces sum >=49, so C>=1, including (24,25). |
| RR1-05 | R1 loop equation and sign | Pass. B contributes 11(-1)+10(1)=-1, giving 100X'=121X-w. Difference 1 persists at the intermediate residue. |
| RR1-06 | R1 block congruences and intermediate integrality | Pass. Classes 0 and 81 modulo 100 give first quotients 110t and 89+110t, hence exactly controls (0,0) and (1,9); the converse is the same congruence calculation. |
| RR1-07 | R1 translation to the ceiling map | Pass. Y=X-1 has corrections 21 or 20 on residues 99 or 80, the unique canonical corrections modulo 100. |
| RR1-08 | R1 reverse direction, positivity and official start | Pass. A positive stopped-map survivor recovers every intermediate quotient, yields X>=81 and the actual pair (60X+1,60X), with difference 1 forever. No product or small-quotient exception is lost. |
| RR1-09 | R1 termination equivalence and conclusion boundary | Pass for positive ordinary integer lifts. Exiting the two residues only exits the A/B family. The singleton source theorem is not applied to a two-residue set. See scope caution N1 below. |
| RR1-10 | R2 nonzero integer in divisibility step | Pass. X_j=0 would force the whole remaining binary word to be zero; the stated hypothesis prevents this. Multiplication by 100 is injective in Z10. |
| RR1-11 | R2 growth, run placement and exceptional tail | Pass. The geometric error constant is 1/21; 100^M divides vX_j, giving the stated alpha<1 bound. The eventually-zero rational exception is retained. |
| RR1-12 | R2 rich word and irrationality | Pass. W_k contains each k-factor, and the appended zero run starts at N_k and has length N_k. Non-eventual-zero and N_k tending to infinity contradict the rational bound. |
| RR1-13 | R2 correction complexity and comparison | Pass. Aligned injective coding yields P_h(2k)>=2^k; right extension gives monotonicity for odd lengths. The asymptotic lower slope is infinite, without producing a rational lift. |
| RR1-14 | R3 real shadow algebra and interval | Pass. The auxiliary real coordinates obey the displayed linear identities using bounded integer symbols u,v; they need not have those symbols as ordinary real remainders. Boundedness gives shat in [0,48] and the exact initial shadow interval. |
| RR1-15 | R3 causal quantifiers and digit permutation | Pass. For a fixed prefix, k is fixed and delta=-e-k modulo 10. All ten controls give all canonical digits once. No probability model for one integer orbit is assumed. |
| RR1-16 | R3 exact averaging and constants | Pass. The bracket is m+9/2+Avg Qhat_0. Its distance from zero is at least 13/120 for integral m; the terminal error is at most 29/2. |
| RR1-17 | R3 actual finite-prefix obstruction | Pass. Finite positive lifting transfers the obstruction to any proposed rule on all ordinary starts with the same causal initialization. It is not a statement about every individual orbit or avoiding sublanguage. |
| RR1-18 | S1 eight constant translates | Pass. All Q>=81; c=1,...,8 keeps shifted states positive and gives digits in [0,9]. For c=2,...,8 the digit is nonzero, so those seven scalar orbits avoid multiples of 10. The residue-escape implication remains conditional. |
| RR1-19 | S2 forced carry continuation | Pass. The closed interval of ten possible values selects exactly k'=ceil((11k-h)/10), including for negative carries. Initial carry is the only free choice. |
| RR1-20 | S2 uniform escape from suitable states | Pass. For 11<=2r+d<=57 the mean bracket has absolute value >=1/40 uniformly in integral m. Selecting r' in {12,...,17} reaches such a state from every full-controller state. |
| RR1-21 | S2 one prefix for every bounded initial carry | Pass. Finite elimination concatenates at most 2K+1 escape words and records historical violations, so a returning carry does not revive an eliminated initializer. The length bound is (2K+1)(N(K)+1). |
| RR1-22 | S2 arbitrary future-aware initialization and actual positivity | Pass. The common prefix defeats all m in [-K,K] before it is lifted to one ordinary Q_0>K. Any future-aware choice on that start is among these m; forced continuation then fails. Q_n>=Q_0 ensures a bounded shifted state would stay positive. |
| RR1-23 | Source alphabet, direction and final boundary | Pass for the mathematical boundary claimed. Published digits include p-1=10, whereas R3/S2 demand only 0,...,9; the right-transducer final boundary is distinct. See source caution N2. |
| RR1-24 | Published complexity, termination and expansion hypotheses | Pass. Attribution and conditional status are retained; neither singleton termination nor the p>=2q-1 expansion result is applied outside its hypotheses. |

## N1: positive-lift wording (nonblocking scope caution)

Original lines 167-170 abbreviate the preceding two positive existence
statements as excluding “all A/B integer lifts.” Read this with the explicit
positive domain of lines 133-165. Taken without that context it would include
the zero lift of the all-A word. The proof and recommendation concern positive
ordinary lifts satisfying the official domain. No mathematical repair is needed
to the stated existence equivalence; repeating “positive” in an accepted scope
summary would avoid an unintended extension.

## N2: published signed-word converter (nonblocking source caution)

Read the candidate's shorthand about finite signed words with the published
converter's final acceptance condition: negative terminal states are not final,
and the proof identifies conversion for words of positive numerical value.
The candidate already mentions the final-output boundary and makes no proof
step requiring conversion of a negative-value word. This does not obstruct
R3 or S2; a later exposition should retain that source qualification as well
as the explicitly stated larger alphabet.

## Unresolved targets, not defects in this packet

No statement proves termination of the specific stopped 121/100 instance,
universal scalar residue escape, absence of every rich rational avoiding
lift, an integer counterexample, or universal equality in the contest problem.
None is recommended for acceptance by this audit. The coordinator alone may
promote the scoped results after the second independent audit and all required
integration checks.
