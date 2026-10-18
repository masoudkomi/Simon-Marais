# A two-parameter family from exact subfield tensor counts

19 October 2026, Brisbane. **Candidate proof - unverified.** This NEW
packet concerns only the open portion2024 B4(b). Root constructed it;
root and C, whose earlier translation-count perspective was a conceptual
trigger, are both conservatively EXCLUDED from the required TWO OTHER
initially blind ENTIRE whole audits. A/B have supplied no NEW inference.
Requested inherited gpt-6.1-sol/max; effective settings independently
unreadable. No claim of an additional solved annual problem or priority.

## Significance and the precise new question

The official factorization problem is related to APN monomials and
double-error-correcting cyclic codes. The intersection budget for its
actual curve counts additive quadruples in multiplicative root groups.
When a root group is the product of two coprime-degree binary subfield
groups, its additive structure is exactly that of nonzero rank-one
tensors. The accepted TR12 theorem counts these quadruples exactly.
Here consecutive subfield degrees make BOTH root counts in the same
geometric budget accessible, giving a two-parameter irreducibility
family. This extends the separately reviewed105 family as a mathematical
statement; whether the application was already published remains OPEN.

The preserved exploration-v0 note predates TR12 acceptance and correctly
calls that input then unverified. Its bytes are unchanged. The present
packet uses the now accepted GENERAL TR12A/B count, not a conjecture,
and receives its own reviews. No old acceptance covers this NEW family.

## 0. Definitions and exact accepted inputs

Work in K, an algebraic closure of F2. For an odd positive integer s,
H_s denotes ALL s-th roots of unity in K. Let M_s count ORDERED pairs
(x,y) for which 1,x,y,1+x+y are four distinct members of H_s. It is
neither an unordered count nor a count restricted to a later F_q.

Use the established quotient

    phi_n=(X^n+Y^n+Z^n+(X+Y+Z)^n)/[(X+Y)(Y+Z)(Z+X)].

Existence of this polynomial is accepted preliminary context, not
reproved or investigated here. The domain below avoids n1/n3.

The COMPLETE accepted TR12 proof and EACH current authority MD/JSON
are operative input. For COPRIME INTEGER degrees u,v>=2, with
R=2^u-1,S=2^v-1, it proves

    M_(RS)=R^2+S^2+6RS-10R-10S+12.                    (T)

Its proof includes the actual ADDITIVE field multiplication isomorphism,
nonzero rank-one tensor identification, unique binary factor pairs,
rank-one translation countR+S-2, rank-two ORDERED count6, and removal
of exactly two normalized collisions. Multiplicative uniqueness alone
would not justify (T). No noncoprime-degree or larger-base version is
being imported. Root constructed TR12; the accepted input has TWO OTHER
whole audits. Root does not count itself as an independent reviewer.

The COMPLETE accepted FR10 proof and EACH current authority MD/JSON
are the geometric input. For

    n=ell*q+1, ell>=3 odd, q=2^i, i>=2,
    d=gcd(ell,q-1), N=ell*q-2,

it proves reducedness, EVERY absolute component degree at leastq,
and the following implication. If WHOLE phi_n is absolutely reducible,
its ACTUAL least component U of degree e and FULL coprime complement V
satisfy, for THIS SAME PAIR,

    q(N-q)<=e(N-e)
       <=(q-2)^2/4+3(d-1)q^2/4+q*M_ell+q(q-2)*M_d/4. (I)

The accepted budget retains the center, all three noncentral diagonals,
ordinary and nonordinary off-diagonal points and infinity. No
common-center, equal-degree, F2-defined-component, irreducible-complement
or formal-divisor hypothesis is added. In particular we do not improve
one formal assignment and assert it applies to an arbitrary actual pair.
Root was an OLD FR10 other auditor; this disclosed role is not a new
independent re-certification of its inherited foundational inputs.

## Proposed R13A--R13D, all quantifiers

Let a>=3 be any ODD INTEGER, t>=0 any INTEGER, and put

    r=2^a-1, s=2^(a+1)-1=2r+1, ell=r*s,
    i=a*((a+1)*t+2), q=2^i, n=ell*q+1.                (1)

**R13A.** For every such a,t,

    d=gcd(ell,q-1)=3r,
    M_ell=17r^2-20r+3, M_d=r^2+8r-9.                (2)

The two counts have the normalized ordered/full-root-group meaning
above, and (T) applies to both with actual coprime subfield degrees.

**R13B.** For every a,t in (1), WHOLE phi_n is absolutely irreducible.
Consequently this n does NOT satisfy the official coefficientwise
two-nonconstant-factor condition. No converse or full classification.

**R13C.** The a3 subfamily is exactly n=105*2^(12t+6)+1,t>=0,
including6721, already in accepted TR12. The statement for arbitrary
odd a>=5 supplies additional parameter values within this NEW theorem;
this is not a publication-priority assertion.

**R13D, exact sufficient-test comparison only.** The OLD FR10
size-bound polynomial P is strictly NEGATIVE for every member of (1).
Thus R13B cannot be obtained by simply invoking that particular P>0
test on those parameters. No exclusion of every other known method,
published theorem or implication of another packet is asserted.

## 1. Uniform arithmetic and actual degree hypotheses

Since gcd(a,a+1)=1, Euclidean reduction of exponents gives
gcd(r,s)=1. For completeness the identity used is

    gcd(2^u-1,2^v-1)=2^gcd(u,v)-1:

for u>=v, reduce2^u-1 by2^(u-v)(2^v-1) to2^(u-v)-1,
then repeat Euclid on the positive exponents. This is integer gcd,
valid whether the Mersenne numbers themselves are prime or composite.

Here a divides i. Also

    gcd(i,a+1)=gcd(a*((a+1)t+2),a+1)
             =gcd(2,a+1)=2,

because gcd(a,a+1)=1 and a is odd. The same exponent identity yields
gcd(r,q-1)=r and gcd(s,q-1)=3. Since r,s are COPRIME, their product
gcd is the product of these two gcds. Thus d=3r exactly. In addition
2^a=2 mod3, so r=1 mod3 and gcd(3,r)=1. This last fact is also the
coprime degree hypothesis for the second tensor application below.

All other geometric domain conditions really hold: r>=7,s>=15 and
ell>=105 are positive odd; i>=2a>=6, so q>=64>=4. Since ell is odd,
q is the maximal power of two in n-1. Also ell>1 is odd and has at
least two binary1 bits, so n has binary weight at least three after
shifting ell by i and appending the low bit1. Every-component degree
and reducedness in accepted FR10 therefore apply in precisely their
stated domain. No prime hypothesis on r,s,d or ell is needed.

## 2. Apply the accepted count to BOTH actual root groups

For ell=rs, use degrees(a,a+1), which are both>=2 and coprime.
Their field-root product is the complete H_ell in K. Apply (T):

    M_ell=r^2+(2r+1)^2+6r(2r+1)-10r-10(2r+1)+12
         =17r^2-20r+3.                                (3)

For d=3r, use degrees(2,a). They are coprime because a is odd,
both>=2. Thus (T) applies independently to the complete H_d:

    M_d=3^2+r^2+18r-30-10r+12=r^2+8r-9.               (4)

The field containing H_ell need not be the later F_q; the ordinary
fixed-field count in (I) is the DIFFERENT countH_d. Both exact values
are legitimate in the SAME pair's budget. Orderedness and fourth entry1
match (I) without any factor of2,4,6 or24. These substitutions establish
R13A and preserve every inherited intersection contribution.

## 3. The uniform whole-polynomial contradiction

If phi_n were absolutely reducible, (I) would hold. Let B denote its
actual upper expression. Its fourfold gap against q(N-q) is exactly

    4[q(N-q)-B]
       =(4ell-3d-2-M_d)q^2-[4+4M_ell-2M_d]q-4
       =(7r^2-13r+7)q^2-(66r^2-96r+34)q-4.            (5)

Both expansions are over ordinary integers/rationals, not division by4
in K. For example4ell=8r^2+4r and3d=9r give the first coefficient;
4+4(17r^2-20r+3)-2(r^2+8r-9) gives the second. No geometric term is
removed, and no monotonicity of a negative count coefficient is used.

Write A=7r^2-13r+7 and B0=66r^2-96r+34. For every r>=7,
A=r(7r-13)+7>0. Moreover

    16A-B0=46r^2-112r+78
           =46r(r-3)+26r+78>=1548>0.                 (6)

The lower bound uses r(r-3)>=7*4 and r>=7. For EVERY REAL q>=16,

    Aq-B0>=16A-B0>=1548,
    Aq^2-B0q-4>=16*1548-4=24764>0.                  (7)

In particular this holds for EVERY actual q>=64 in (1), including
t0 for every odd a. Thus (5) is positive, contradicting (I).
There cannot be two absolute components. Accepted reducedness excludes
a repeated power of a single component. This proves WHOLE absolute
irreducibility, not merely existence of one F2-defined absolute
component or a statement about polynomial function values on F2^3.

An official pair g,h in Z[X,Y,Z], each nonconstant modulo2, would
reduce coefficientwise to positive-degree factors gbar,hbar in the
integral domain F2[X,Y,Z]. The prescribed nonzero linear product R
cancels from R*phi_n=R*gbar*hbar, giving phi_n=gbar*hbar, impossible.
This argument permits nonhomogeneous g,h and proves the official
exclusion asserted in R13B. It does not redo preliminary part(a).

At a3, r7,s15,ell105,i12t+6,d21 and (5) is
259q^2-2596q-4. This is exactly accepted TR12, establishing R13C
and its t0 inclusion. No finite factor computation is a premise.

## 4. An honest negative comparison and failed directions

For the same actual ell,d,q, accepted FR10's OLD size-bound test is

    P=(4ell-d^2+d-5)q^2
          -[4(ell-2)^2-2(d-1)(d-3)]q-4.

Its leading coefficient equals

    4ell-d^2+d-5=-r^2+7r-5=-r(r-7)-5<=-5.

Its subtracted q coefficient C0 is strictly positive: ell-2=2r^2+r-2
>=2r^2, and2(3r-1)(3r-3)<18r^2. Consequently

    C0>16r^4-18r^2>0 for r>=7.

Thus P<0 for EVERY positive q in our family. This proves only R13D's
literal comparison. A nonpositive test has no converse and is not a
claim of reducibility. It does not refute FR10 or compare every other
criterion. In particular no assertion about FR11 on all parameters is
needed for this proof.

Failed/unavailable extensions: even a makes degrees(2,a) noncoprime and
changes gcd(i,a+1); neither (2) nor this proof may be exported there.
Nonintegral t,negative t,a1/lower degrees and q2 are outside (1).
Replacing the additive tensor isomorphism by multiplicative uniqueness,
or restricting H_ell to F_q, would invalidate the counts. Strengthening
a formal component assignment would not prove the whole conclusion.
Replacing absolute irreducibility by the general exceptional-APN
component theorem would also leave the official inference unjustified.
All these routes are excluded; none is silently used as a shortcut.

## 5. ALL32 constructor obligations

These are author checks, NOT independent reviews. EACH OTHER ENTIRE
whole reviewer must reconstruct every row and the entire packet.

|ID|Exact inference/constructor disposition|
|---|---|
|R13-O01|Official positive oddn/coefficientwise target,only open(b),all domains retained.|
|R13-O02|TR12 COMPLETE accepted body and EACH current MDJSON read;general count(T),not just M21/M105.|
|R13-O03|FR10 COMPLETE accepted body and EACH MDJSON read;actual full-pair budget/reducedness/every-degree retained.|
|R13-O04|Root NEW constructor/C conceptual trigger excluded;old input roles disclosed;twoOTHERwholeaudits required.|
|R13-O05|a oddinteger>=3,t integer>=0,r/s/ell/i/q/n defined uniformly includingt0.|
|R13-O06|Integer exponent Euclidean identity proved and used without Mersenne primality.|
|R13-O07|Consecutive degrees gcd1 imply gcd(r,s)=1.|
|R13-O08|a dividesi and gcd(i,a+1)=2 exactly for every permittedt.|
|R13-O09|Gcd withq-1 separately r and3;coprime product justifiesd=3r.|
|R13-O10|a odd impliesr1mod3/gcd3r1;degreepair2,a genuinelycoprime.|
|R13-O11|ell>=105 odd,i>=6/q>=64 and maximal two-part verified.|
|R13-O12|Binary weight>=3 and every FR10 domain restriction checked.|
|R13-O13|TR12 count applies with degreesa,a+1>=2 coprime,fullH_ell.|
|R13-O14|ExpansionM_ell=17r²-20r+3 checked by hand.|
|R13-O15|TR12 separately applies todegrees2,a,fullH_d.|
|R13-O16|ExpansionM_d=r²+8r-9 checked by hand.|
|R13-O17|Normalizedfourdistinct/ordered/fullK-root counts matchI;ordinaryH_d separate.|
|R13-O18|SAMEactualleastcomponent/FULLcoprimecomplement and ALL center/diagonal/offdiagonal/infinity terms preserved.|
|R13-O19|Fourfoldgap general coefficient4ell-3d-2-M_d andq coefficient-4-4M_ell+2M_d derived.|
|R13-O20|Substitutedgap exactly(7r²-13r+7)q²-(66r²-96r+34)q-4.|
|R13-O21|Apositiveallr>=7,withnohiddenendpoint.|
|R13-O22|16A-B0=46r(r-3)+26r+78>=1548,allr>=7.|
|R13-O23|UniformREALq>=16 positivity coversEVERYactualq>=64/allodd a/allt>=0.|
|R13-O24|Impossibleactualsplitplusreducedness provesWHOLEabsoluteirreducibility,notonecomponent.|
|R13-O25|Officialintegerproductcoefficientwise reduction/cancellationrulesoutnonconstantg,h includingnonhomogeneous.|
|R13-O26|a3 gives105/exponent12t+6/d21/gap259q²-2596q-4,including6721.|
|R13-O27|OLDleading=-r(r-7)-5<=-5 for everyfamilymember.|
|R13-O28|OLDqcoefficient>16r4-18r²>0,soOLDteststrictlynegative.|
|R13-O29|ComparisononlyliteralFR10P;nofailed-testconverse/generalprior-nonoverlap.|
|R13-O30|Evena/noncoprimedegrees/largerbase/wrongrootdomain/formal-componentfailedroutespreserved.|
|R13-O31|Allliteralprimary/acceptedreadlimits,sources/issues/worklog and openpriority/annual preserved.|
|R13-O32|Completepayload/admin/baseline/freeze FULLfinalmodelreadbacks+SEPARATEverifybeforetwoOTHERblindwholeaudits/acceptance.|

## 6. Issue log, literal source scopes and worklog

OPEN1: this NEW extension has not been independently audited. ALL32
obligations and all companion bytes require TWO OTHER whole reviews,
initially blind to each other's findings/files/actual inventories/hash/
metadata. Both ENTIRE final payload/manifest model readbacks and
SEPARATE verifications must finish before explicit BOTH release.
Root must then read ENTIRE author+BOTH/allledgers/code/meta before any
promotion. A substantive defect requires a separate versioned repair
and both affected whole re-audits; preserve all original bytes.

OPEN2: the unrestricted annual classification remains unresolved.
OPEN3: publication overlap is unresolved; tensor-rank geometry is
classical, and the application may already be in prior work.
CLOSED by exact scope: TR12 now accepted with its complete general
count. Its old unverified exploration status is historical and retained.
CLOSED by domain: t0 included and evena excluded explicitly.
CLOSED by comparison scope: oldP failure is a test comparison only.

Fresh local mathematical reads for THIS target: complete accepted TR12
body/currentMDJSON and complete accepted FR10 body/currentMDJSON;
local official-normalization statement; AGENTS; preserved exploration.
Combined tool output clipped some accepted-body text; targeted full
missing-range readback recovered it before this construction. The
older TR12/root construction, FR10/root audit, R6/Fulton/Hernando-McGuire
foundational chains remain disclosed historical scopes, NOT newly
repeated entire foundational source audits or a third OTHER audit.
No old source/author executable or certificate replay supplied proof.

Fresh primary official2024PaperB p2: designation57--59/setup60--63;
open(b)68--71/coefficientwise definition72--74. URL:
https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf .
No preliminary(a) proof investigated. The browser's adjacent context
includes the preliminary statement only, not a new investigation.

Primary literature discovery/read18Oct2026UTC:
Eric Férard, On the irreducibility of the hyperplane sections of Fermat
varieties in P3 in characteristic2.II,Cryptogr.Commun.9(2017),749--767,
DOI10.1007/s12095-017-0213-1,
https://link.springer.com/article/10.1007/s12095-017-0213-1 . Publisher
metadata/ENTIRE abstract33 and references ONLY were read,not the article
body. It treats exponents1mod4 with conditions on the odd part; its
exact criterion may overlap and is NOT inferred from the abstract.
The author laboratory's primary publications page
https://gaati.org/publications/fr/ line170 links institutional record
hal-03417811. Public HAL document retrieval through the web tool was
inaccessible; a bounded curl to
https://upf.hal.science/hal-03417811/document returned404. No full
PDF was obtained/cached, no purchase/access bypass or contact occurred.
This failure is not evidence of no overlap or no available manuscript.

Férard2014,Adv.Math.Commun.8,497--509,
https://www.aimsciences.org/article/doi/10.3934/amc.2014.8.497 : primary
publisher metadata/ENTIRE abstract78--80 ONLY freshly read. Its described
criterion concerns5mod8; our n1mod64 is only a literal residue comparison,
not a theorem-level nonoverlap claim. Original Jedlicka2007 and Férard2017
operative proofs remain UNREAD. Delsarte1978 publisher metadata/abstract
are historical classical-context attribution through TR12, not newly
fetched or used as an external rank theorem. All required rank counts
are in the accepted elementary proof. No literature theorem is imported
from secondary search snippets; unrelated hits were discarded.

Worklog: root recorded exploration while OTHER TR12 audits were still
blind, without peer findings. After both ENTIRE TR12 reviews completed,
explicit release and complete reconciliation accepted the GENERAL
count. Root then preserved exploration bytes, freshly checked both
accepted input bodies/current authorities and official scope, expanded
both actual counts and the uniform gap by hand, and checked all arithmetic
domains/endpoints. Primary searches newly identified the2017 DOI and
author-lab HAL record, preserving actual retrieval failures/abstract-only
scope. This main embeds significance,fullproof,ALL32checks,allissues/
failures/sourceMD/worklog. SourceJSON,documentary admin,baseline andfreeze
complete ENTIRE5. Actual freeze/readback/separate-verify times will be
reported only after they occur,not invented here.

No mathematical Python/CAS,finite-field enumeration,factor scan,routine
test,paid source,source/author routine or old-certificate replay was used.
Documentary Python only binds byte identities and creates metadata.
No third-party paper binary is uploaded. Latest actual weekly reading
67%TOTAL/accountwide22:39:26UTC,reset1792874445/90%TOTAL with reserve;
research continues independently on2017/2020/2021 while this packet
awaits OTHER audits. Internal review does not establish external priority.
