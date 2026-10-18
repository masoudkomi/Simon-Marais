# Independent hand certificate for the twenty Q7 interval pairs

2026-10-18 UTC. A whole-v3 audit. **Hand algebra, not a script, scan,
CAS, author rerun or sampled table.** This finite table is essential to
the claimed exact all-integer orphan iff. It is reconstructed directly
from the floor parameterization, independently of the author's table.

For input a=30l+r,b=20k+s, let d=a−b and output D=A−B. Then
D=d+2k−3l, so u=d−D=3l−2k; also δ=10D−9d=r−s. Euclidean parity
e∈{0,1} with e≡u mod2 gives l=2z+e and k=3z+(3e−u)/2. Thus
B=66z+C+s, C=33e−10u, and

    max(0,−δ)<=s<=min(19,29−δ).

Conversely those formulas give actual ordinary l,k,r,s and both output
coordinates. This proves an all-integer iff; residue membership requires
no unproved lifting lemma. For specified B, z=(B−C−s)/66 is an ordinary
integer. At B>=43,D∈I, the separately proved inverse inequalities give
official positivity and product for every such parent.

The inverse ceilings give outside d choices
24;24,25;24,25,26;24,25,26,27 for D20,21,22,23, and
−14;−14,−15;−14,−15,−16;−14,−15,−16,−17 for D−10,−11,−12,−13.
No central output can have an orphan, since every ordinary parent then
lies in I. These are exactly the twenty possible pairs.

|D|d|u|δ|e|C before reduction|Allowed s|B mod66 before collision deletion|
|---|---|---|---|---|---|---|---|
|20|24|4|−16|0|−40|16..19|42..45|
|21|24|3|−6|1|3|6..19|9..22|
|21|25|4|−15|0|−40|15..19|41..45|
|22|24|2|4|0|−20|0..19|46..65|
|22|25|3|−5|1|3|5..19|8..22|
|22|26|4|−14|0|−40|14..19|40..45|
|23|24|1|14|1|23|0..15|23..38|
|23|25|2|5|0|−20|0..19|46..65|
|23|26|3|−4|1|3|4..19|7..22|
|23|27|4|−13|0|−40|13..19|39..45|
|−10|−14|−4|26|0|40|0..3|40..43|
|−11|−14|−3|16|1|63|0..13|63..65 and0..10|
|−11|−15|−4|25|0|40|0..4|40..44|
|−12|−14|−2|6|0|20|0..19|20..39|
|−12|−15|−3|15|1|63|0..14|63..65 and0..11|
|−12|−16|−4|24|0|40|0..5|40..45|
|−13|−14|−1|−4|1|43|4..19|47..62|
|−13|−15|−2|5|0|20|0..19|20..39|
|−13|−16|−3|14|1|63|0..15|63..65 and0..12|
|−13|−17|−4|23|0|40|0..6|40..46|

All intervals are inclusive. For example the negative-u−3 rows use e1,
so C63, not a negative-parity representative; adding s up to13,14,15
wraps precisely to10,11,12. The negative-u−1 row has δ−4 and therefore
starts at s4, yielding47, not43. The positive-u1 row has upper s15,
not19, yielding38. These endpoint and parity checks are material.

The two collision deletions require a full fiber check. Q1 partners
always have differences separated by5. The inverse interval at D20
is19..24; d24 has r=s−16 and the four pairs
(0,16),(1,17),(2,18),(3,19). Exactly(1,17) is in R_L. Its partner
has d19 in I and its residue is B=−40+17=43 mod66. Delete43 only.
At D−10 the interval is−14..−9; d−14 has r=s+26 and pairs
(26,0),(27,1),(28,2),(29,3). Exactly(28,2) is in R_H, with inside
partner d−9 and B=40+2=42 mod66. Delete42 only.

Every other outer inverse interval has diameter4, so there cannot be
two parents separated by5. An orphan cannot have two outside parents
either: K={−17..−14,24..27} has component diameters3 and cross-gap at
least38. Thus every surviving table membership really is a UNIQUE
outside parent and no inside parent. Conversely an orphan must occur
in the table. There are no untested corner cases.

Final T_D sets and direct inclusive counts:

|D|T_D|Count|
|---|---|---|
|20|42,44,45|3|
|21|9..22 and41..45|14+5=19|
|22|8..22 and40..65|15+26=41|
|23|7..65|59|
|−10|40,41,43|3|
|−11|0..10,40..44,63..65|11+5+3=19|
|−12|0..11,20..45,63..65|12+26+3=41|
|−13|0..12,20..65|13+46=59|

Total2(3+19+41+59)=244 modulo66 orphan rays, before ALL current-input
mod60 rectangle exclusions and official start filters. The40 birth
rays have differences−1,1,2 and are disjoint from these eight offset
classes. No post-filter seed count or future orbit conclusion follows.
