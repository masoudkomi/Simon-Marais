# Complete R15 hand reconstruction and all affine constants

18 October2026 UTC. **Candidate proof - unverified.** These are
CONSTRUCTOR checks, not either required independent whole audit.
No mathematical executable, table generator, CAS, valuation scan,
coefficient-mask search, finite test or old certificate replay was used.

## Independent arithmetic presentation of the finite certificate

Use the notation of the main. The raw low coefficient checks are:

    D6(1)=−5+15A+B+15C+6E+V,
    D7(1)=−6+2A−3B−3C+2E+7V+W,
    D8(1)=12+9A−B+13C−E+9V+8W+U,
    D9(1)=11+17A+8B+12C+12E+8V+17W+9U+y,
    D10(1)=10+7A+6B+C+5E+V+6W+7U+10y,
    D11(1)=9+17A+13B+7C+6E+6V+7W+13U−2y+z.

Substituting W=6−2A+3B+3C−2E−7V gives T,F9,F10 in the main.
For example the constant/low coefficients of F9 become
(18,2,2,6,16,3,9) in the order(1,A,B,C,E,V,U), and those of F10
become(8,14,5,0,12,16,7). Thus the dropped C term in F10 is an
exact cancellation, not an omitted possible unit.

For the global elimination beta2,...,beta9 have residues

    (10,3,8,18,7,14,18,5).

The remaining relevant weights use beta_(20-j)=beta_j. In particular
beta11=5,beta13=14,beta15=18. The original divided equation is

    −1+10A+3B+8C−E+7V+14W−U+5y+5z+14w−u=0.

The two derivative rows and determinant3 then give the main's exact
z=Z0+W+12U+y. The index11 product reduces to equation(4), retaining
all y/U/W contributions. All arithmetic is in F19 after exact division
over Q, never a division by a vanished residue.

For a second full check of the zero-triple table, the following table
gives the E-INDEPENDENT CONSTANTS of(F9,F10,G) in each case, before
adding their E coefficients. The E coefficient triples are

    I:(16,12,4), II:(17,11,12),
    III:(17,17,18), IV:(7,18,5).

Their inverse triples are I:(6,8,5),II:(9,7,8),III:(9,9,18),IV:(11,18,4).
For every component multiply the displayed constant by minus that
inverse to reconstruct the corresponding UNIQUE zero in the main.
This gives every one of the96 affine zeros without an executable.

|Prefix A,B,C|I constant triple|II constant triple|III constant triple|IV constant triple|
|---|---|---|---|---|
|1:0,0,0|(18,8,18)|(14,12,5)|(10,6,1)|(12,2,15)|
|2:0,0,3|(17,8,9)|(11,14,18)|(17,8,9)|(1,2,11)|
|3:0,2,0|(3,18,7)|(12,9,3)|(18,17,8)|(4,7,5)|
|4:0,2,14|(11,18,3)|(17,12,13)|(0,1,1)|(16,7,18)|
|5:1,0,0|(1,3,12)|(9,14,0)|(18,12,3)|(14,1,13)|
|6:1,0,16|(2,3,2)|(12,12,6)|(11,10,14)|(6,1,17)|
|7:1,−1,0|(18,17,8)|(10,6,1)|(14,16,9)|(18,8,18)|
|8:1,−1,1|(5,17,5)|(9,13,18)|(10,4,18)|(8,8,4)|

For example CaseIII/prefix4 has constants(0,1,1) and coefficients
(17,17,18), hence zeros(0,10,1), with E0 allowed only for F9.
CaseII/prefix5 has constants(9,14,0), coefficients(17,11,12), hence
zeros(14,16,0), with E0 allowed only for G. These include the
zero-constant endpoint cases which cannot be checked by division by E.

The complete eligible critical lists, in the main's order, have:

    y0 products: 13,15,4;
    y!=0 products: 6,9,9,8,13,14.

Each is nonzero. Direct substitution into both the raw D11 formula
and the eliminated formula agrees. As a further independent global-row
check, the unit-y tuple CaseI/prefix3 has (A,B,C,E,V,W,U,y)=
(0,2,0,3,0,6,0,6). The three right sides of equation(2) are10,11,14;
after subtracting y contributions the high rows are

    14z+5w+u=2,
    16z+10w+u=1,
    7z+5w+3u=17.

They give2z+5w=18,3z+9w=11, hence z=4. The RAW D11 formula gives
S11=11, so zS11=6. This also independently checks the PLUS14W
sign of the original row and the corrected coefficient+W in z.

## All48 constructor dispositions

|ID|Hand check / exact boundary|
|---|---|
| R15-01 | Fresh official B4 states actual Q common roots at every order and(b) asks all d. Only the specified degree20 subbranch is treated; no preliminary proof or annual conclusion. |
| R15-02 | Every assertion over actual polynomials explicitly assumes(S); the finite lemma is separate. J15/sole-H3/double0 is not presumed to cover every degree20 candidate. |
| R15-03 | Actual double s and rational set{0,1,r,s}, nu>=1 and s/r=2mod19 are retained; carrier rationality comes from accepted actual factors. |
| R15-04 | Equal residues are never used to infer coincidence or rationality. All other roots may be nonrational and nonreal. |
| R15-05 | D_j is defined over Q as H_(20-j)/binom(20,j), so it is monic integral and evaluates at the same witnesses. beta_j are19-units for j2..18. |
| R15-06 | At rational noncenter0/r/s the reduction is a_j; a unit constant therefore forces actual center1. This proves the product, with no converse or lift. |
| R15-07 | Accepted R13C provides an actual center at10/11 and the corresponding finite positive normalized depth. This is not only availability in a residue pattern. |
| R15-08 | Current accepted R14D explicitly discharges its old R13 conditional by separate R13 acceptance. Its forced unit-a7 conclusion applies in the identical(S),(W),(M5) domain. |
| R15-09 | Actual H2/H4/H6/H8 at r force a18/a16/a14/a12 nonunit. The accepted Euler estimate forces a10 nonunit. a8/a9 remain unrestricted, including zero. |
| R15-10 | Unit a7 excludes all three actual rational noncenter values as H13 witnesses; therefore the required ACTUAL witness is1, giving D7(1)=0 over Q. |
| R15-11 | J15 means a15 is a unit and a17 nonunit. The actual H5 witness must be1. Sole-H3 already supplies D17(1)=0. No extra a13 unit is needed. |
| R15-12 | f(1)/19 is formed over Q, constant term(1-20)/19=-1. Q5/a17 reductions remove exactly those even/high terms and keep W,U,y,z,w,u. |
| R15-13 | Raw binomial expansion D7=-6+2A-3B-3C+2E+7V+W gives the solved W. No W nonzero assumption is needed in the field lemma. |
| R15-14 | beta7=14 lies on the low side of the original equation, so row1 RHS has+14W. Its y/z/w/u coefficients are moved with the displayed signs; the full raw row above checks every coefficient. |
| R15-15 | D15 low coefficients are5,10,-1,-3,1,8 and W/U coefficients13/13. Moving them gives R0-13W+6U; high coefficients8,16,10,1 agree. |
| R15-16 | D17 low coefficients are3,3,15,5,13,7 and W/U coefficients11/9. Moving them gives S0-11W-9U; high coefficients9,7,5,3 agree. |
| R15-17 | Row2-row1 and row3-3row1 give the displayed2x2 system. z=3RHS1-8RHS2; W343=1,U69=12,y58=1; Z0 agrees coefficientwise. Determinant3 is a unit. |
| R15-18 | Raw D11 has7W+13U-2y+z. Substituting W and z gives S11=7+15A+14B+C+13E+15V+6U-y. Only its actual product zS11 is imposed. |
| R15-19 | A is0/1. B is0/2 when A0 and0/-1 when A1. C is0 or3-6A-4B. All four nonzero C alternatives are distinct from0. |
| R15-20 | E is0 or4-10A-10B-5C. The eight E* values4,8,3,9,13,9,4,18 are all nonzero, so no low endpoint is silently duplicated/deleted. |
| R15-21 | Raw D6 gives V*=5+4A-B+4C-6E. V0 is allowed even if V* nonzero; when V*=0 the alternatives coincide and belong to the V0 cases. |
| R15-22 | Raw D8 and W substitution give T=3+12A+4B-C+2E+10V. U0 remains allowed even at T0; unit U is exactly-T with T nonzero. |
| R15-23 | Split independently by V0/nonzero and U0/nonzero. CaseII/IV exclude V*=0; CaseIII/IV exclude T0. Every excluded strict endpoint is retained in I/III or I/II. |
| R15-24 | Raw D9/D10 expansions above produce the general F9/F10, including the exact C cancellation in F10. The index9 witness gives y(y+F9)=0. |
| R15-25 | Setting V=U=0 gives CaseI formulas directly; G constants and E coefficient follow by subtracting10F9. |
| R15-26 | V=V*,U0 gives F9 constant14 and E coefficient-2; F10 constant12 and E coefficient11; G E coefficient12. V*=0 is not a new actual case. |
| R15-27 | U=-T,V0 gives CaseIII coefficients and G=1+2A+13B+9C-E. T0 is already in I, not lost. |
| R15-28 | After U=-T, V effects are8V in F9 and3V in F10. Substituting V* gives CaseIV. All inverse triples multiply their coefficient triples to1 in F19. |
| R15-29 | Prefix1 constants from the full table, multiplied by negative inverse triples, give(6,12,5),(7,11,17),(5,3,1),(1,2,16). None has allowed0/E4 in a relevant coordinate. |
| R15-30 | Prefix2 gives(12,12,12),(15,16,8),(18,4,9),(8,2,13). E8 hits only CaseII G and CaseIV F9; both strict tuples are retained. |
| R15-31 | Prefix3 gives(1,8,3),(6,13,14),(9,18,8),(13,7,18). E3 hits only CaseI G. |
| R15-32 | Prefix4 gives(10,8,4),(18,11,10),(0,10,1),(14,7,4). The sole allowed hit is CaseIII F9 at E0; no division by E is used. |
| R15-33 | Prefix5 gives(13,14,16),(14,16,0),(9,6,3),(17,1,5). E13 hits CaseI F9 and E0 hits CaseII G. |
| R15-34 | Prefix6 gives(7,14,9),(6,11,9),(15,5,14),(10,1,8). Both CaseI/II algebraic G hits have E9; V*=0 makes II ineligible and I retains the actual endpoint. |
| R15-35 | Prefix7 gives(6,16,17),(5,15,11),(7,8,9),(11,8,4). Only CaseIV G has allowed E4. Negative B means18, not an ordinary sign assumption. |
| R15-36 | Prefix8 gives(8,16,13),(14,4,8),(5,2,18),(7,8,3). Only CaseIII G has allowed E18. |
| R15-37 | Every table's second coordinate is nonzero and differs from its E*. Therefore F10 never vanishes, even before strict cases filter any point. |
| R15-38 | At y0, only I/5/E13,III/4/E0,IV/2/E8 can make F9zero. Their (V,U) are(0,0),(0,3),(7,9), exactly inside the stated cases. |
| R15-39 | These y0 tuples give(W,z,S11,product)=(16,13,1,13),(16,11,10,15),(7,6,7,4). All products are nonzero; z was allowed0 before the forced tuples were evaluated. |
| R15-40 | y!=0 and the actual index9 product give y=-F9 with F9!=0. Then S10=0 requires G0. S9 is actually0 in this case and is not asserted unit. |
| R15-41 | All third-coordinate hits are the two CaseI, three algebraic CaseII, one CaseIII and one CaseIV entries. The sole ineligible duplicate is handled separately; none is omitted. |
| R15-42 | CaseII/prefix6/E9 gives V*=0. Its U0 actual tuple is I/prefix6/E9 already included. The strict condition therefore causes no missing endpoint. |
| R15-43 | Six eligible tuples have F9=(13,13,14,9,12,8), y=(6,6,5,10,7,11), z=(4,16,17,6,3,1), S11=(11,16,5,14,17,14), products(6,9,9,8,13,14). Every value follows from equation(4)/raw D11. |
| R15-44 | y0 gives S10nonzero and excludes every S9zero via zS11. yunit excludes every S10zero via the six products. W may be0 in the lemma and is never divided out. |
| R15-45 | Actual f supplies all field hypotheses. A nonzero reduction of D10 or D9 at1 is a19-unit; multiplying by the corresponding binomial scalar of valuation1 yields exact Hasse valuation1. |
| R15-46 | Actual m5 gives Q5 and accepted R14 gives unit a7, hence H13center. R15B contradicts R13 EC10 directly, or EC11 because that option has a9nonunit. Overlap does not leave a third option. |
| R15-47 | No nu/displacement appears in the finite lemma. Its application retains arbitrary depths, exact displacement0, coefficient0, ordinary root ordering and ramified carrier. m3/m4/other branches/degree20/annual remain open. |
| R15-48 | All constructor files/48 obligations/checks/source/failures/log and compact SHA/JSON metadata freeze together. Administrative checks are not math proof; old bytes/Git/shared/cache are untouched; TWO OTHER whole audits are required. |
