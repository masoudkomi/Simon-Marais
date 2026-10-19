# A rational-root obstruction removes the zero E8 cover

19October2026UTC. **Candidate proof - unverified.** Root is sole NEW
constructor and excluded from TWO OTHER initially blind WHOLE audits.
Only official2021 B4(b) is researched. Requested Sol/max is separate
from unavailable independent effective backend readback. This NEW
argument uses a COMPLETE finite exact polynomial certificate; it is
not a larger residue-depth search or an inference from sampled cases.

## Actual domain and significance

Retain the ENTIRE actual R18(S),(W)/adjacent m4/J15/oriented frameIII
rational-witness domain retained by accepted R24/R26/R27: rational
monic degree20 f, rational root VALUES exactly0,1,r,s, multiplicities
2,1,1,2, ACTUAL irreducible rational degree14 carrier, and ALL original
common-rational-witness,19-adic and center equations. Other roots need
not be rational or real. A derivative's common rational value may vary
with its order. Formal interpolation alone is never an actual CA example.

Put O=Z_(2),h=1/r=4H with H odd,S=s/r an odd unit distinct from1,
t=v2(S-1)>=2. Accepted R26/R27 gives EXACT A9=A10=0, with
F(Z)=r^-20 f(rZ),A_j=r^-j a_j and
E_j(Z)=sum_(i<=j)binom(j,i)A_i Z^(j-i). All A_j belong O.
Write b=E8(1),c=E9(1),k=E10(1),Q=E20(1)=F(1)=0. The ACTUAL
E8 common value is1 or S, E7(1)=0, and E6(1) is an O-unit,
indeed E_j(1)=1mod4 for j<=6. These are exact accepted interfaces.
The original F(S)=F'(S)=0 and all other equations remain hypotheses.

R27 forces higher contact but does not exclude b0. Here the rational
coefficient requirement supplies a global obstruction to that cover:
after A9/A10zero, b0 would make the ORIGINAL Q equation a fixed
univariate polynomial equation over Q with no rational root. Its
mod37 obstruction applies to EVERY rational h at once. The computation
needed is a finite polynomial identity and all37 field elements;
there is no bound on the height or dyadic/19-adic precision of h.

**Proposed R28A.** In this ENTIRE retained actual domain, b!=0.
Consequently the E8 common value must be S, and the FULL monic
rational gcd is gcd(f,H12)=X-s.

**Proposed R28B.** Every retained actual survivor satisfies

    v2(b)=2+2t,
    b/2^(2+2t)=1mod4 in O.

This excludes the zero E8 cover, not the remaining S cover, all higher
contact, full frameIII, degree20 or the annual problem. No actual
rational polynomial, lifting theorem, finite contact cap or priority
is claimed. The other frames were separately treated; all older
accepted results retain their stated scopes.

## 1. Exact specialization before any modular calculation

Accepted integral AFFINE interpolation has

    A0=1,A1=-h,A2=A4=A5=A19=A20=0,A3=2h³,A6=-35h6,
    A7=-1+7h-70h³+245h6,
    A8=7-48h+448h³-980h6+b,
    A9=-28+189h-1680h³+2940h6-9b+c,
    A10=84-560h+4800h³-7350h6+45b-10c+k.

For j11..18 the exact rows are

    A_j=-sum_(i<j)binom(j,i)A_i z_j^(j-i),
    z11=z12=z13=z15=z17=h,z14=z16=z18=1.

Suppose b=0. ACTUAL A9=A10=0 then fixes c,k; equivalently set
A9=A10=0 in these exact low rows and keep A0..8 as displayed with b0.
No independent choice of c,k or arbitrary derivative witness is made.
All subsequent A_j are now fixed INTEGER polynomials in h. Finally

    Q(h)=sum_(i=0)^18 binom(20,i)A_i(h).

The fixed A19=A20=0 boundary is retained. It is invalid to replace
these last coefficients by a homothetic transport. This Q is the
ORIGINAL r^-20 f(r), not an equation imposed only on a formal family.
Thus an actual b0 survivor would give a RATIONAL h with Q(h)=0.

The recurrence gives deg A_j<=j at h-centered rows, while each unit
row cannot increase the preceding maximum degree. In particular the
successive upper bounds at11..18 are11,12,13,13,15,15,17,17, so
deg Q<=17. Coefficientwise parity of the accepted Q identity survives
the integral specialization c(h),k(h),b0; hence W(h)=-Q(h)/2 is in Z[h].
The finite certificate below also checks every exact integer coefficient,
including the highest one, without relying on this parity shortcut.

## 2. COMPLETE finite certificate modulo37

Coefficient order in the following row is DESCENDING h17 through h0:

    W mod37 = [27,11,26,34,13,3,11,26,14,18,28,5,13,12,16,27,28,11].

This is a finite coefficient-identity claim obtained from the EXACT
recurrence above; its complete integer coefficients are recorded in
sources-v1.json. The accompanying short standard-library certificate
reconstructs the polynomials by exact addition, integer scalar
multiplication and exponent shifts, then reduces coefficients. No
floating point, numerical root test or black-box factorization is used
for the certificate. The leading residue27 is NONZERO, so W has
degree17 and a37-adic unit leading coefficient.

Here is the COMPLETE list of W(x)mod37 for x=0,1,...,36, in order:

    [11,27,28,19,10,20,10,6,30,1,10,19,13,29,15,8,31,34,5,
     21,9,8,34,1,22,32,3,10,9,8,6,27,35,27,33,10,8].

Every entry lies in1..36. This exhausts the field F37, not an
unrestricted rational or p-adic domain. The final inference covering
that unrestricted rational domain is supplied next. Every coefficient
and field evaluation is part of the proposed proof obligation and
must be independently verified; a program's PASS alone is not promotion.

## 3. Why this excludes EVERY rational root

Let h=u/v be a rational root of W in lowest terms, v>0. If37 divides v,
multiply W(u/v)=0 by v17 and reduce modulo37. Every term except the
leading term vanishes, while the leading residue is27u17!=0 because
gcd(u,v)=1. This is a contradiction. Therefore37 does not divide v.
Now h has a well-defined residue u/v in F37. Reduction of W(h)=0
would make that residue a root of the displayed polynomial, contradicting
the COMPLETE nonzero list. Hence W, and therefore Q, has NO rational
root. This proves b!=0 in every actual retained case. The argument
does not assume h positive, integral or bounded in height; h0 and
negative rationals are also covered. No irreducibility theorem is needed.

The accepted actual E8 cover now forces E8(S)=0. Put delta=S-1, so
v2(delta)=t>=2. Exact Taylor and E7(1)=0 give

    b=-28E6(1)delta²-56E5(1)delta³-70E4(1)delta4
      -56E3(1)delta5-28E2(1)delta6-8E1(1)delta7-delta8.

Write delta=2^t u with u an odd rational O-unit. After division by
2^(2+2t), the first term is-7E6(1)u². The remaining terms have
additional depths respectively1+t,2t-1,1+3t,4t,1+5t,6t-2.
Each is at least3 for t>=2. Since E6(1)=1mod4 and u²=1mod4,
the quotient is-7=1mod4. It is an O-unit, proving BOTH the exact
depth and normalized congruence in R28B. At t1 the different fourth
term boundary matters; no t1 formula is being extended.

For the FULL gcd, the accepted actual cover excludes every other
rational root value; b!=0 excludes1 in normalized coordinates, so S
is the only rational common value. Taylor of E7 at1 has leading
7E6(1)delta of exact deptht; all higher terms have strictly larger
depth. Thus E7(S)!=0 and E8'(S)=8E7(S)!=0 over Q: the E8 root S
is simple even though F has a double root there. Any nonrational
common factor would contain the ACTUAL irreducible degree14 carrier,
impossible because deg E8=8. Scaling back gives the FULL monic
gcd(f,H12)=X-s. It is insufficient merely to exhibit that factor.

## 4. Failed approaches, computation provenance and source limits

The first bounded exploratory CAS probe constructed the same exact
degree17 Q and returned one degree17 rational factor and no rational
roots. That factorization/ground_roots output is COMPUTATIONAL EVIDENCE
ONLY and is NOT a premise. No certificate of its black-box irreducibility
was imported. A complete small-prime obstruction was sought instead:
23 has roots0,11;29 has6,17,21;31 has3. These failures are preserved.
A subsequent bounded list37..97 stopped immediately at37. No further
prime or coefficient search is needed or authorized by this certificate.

The initial CAS was a NEW private subprocess with explicit30second
timeout, childPID77867, incremental ignoredlocal log, exit0/reaped;
Sympy1.14.0 was already installed, no installation occurred. The exact
command, script, output and failed-prime records are preserved in the
source payload. A NEW independent standard-library implementation then
reconstructed the COMPLETE finite certificate before freeze. It is a
finite certificate needed by this proof, not a routine implementation
test, larger dyadic table or old/source/author-helper replay. All scope,
rational-root, actual-cover, Taylor and full-gcd inferences are hand
reasoning. Documentary code is separate and checks bytes/JSON only.

Root freshly read COMPLETE accepted R27 and EACH current authority in
its preceding reconciliation; the exact R24/R26 interfaces were fully
read for the preceding constructions/reconciliations. Current immutable
authorities are bound here. Older R18/R23/R5 and original Casas--Alvero
foundation reads remain historical, not a fresh whole-source audit or
independent self-certification of root's earlier contributions. Original
official2021 rational-common-value wording67--76/open(b)81 was checked
earlier19October in this rotation; no second full-paper pixel/download
audit is claimed. No NEW external theorem beyond the elementary
rational-root reduction proved here is imported. No separately billed
API, fee, contact, bypass, full third-party upload or priority claim.

No worker supplied a new R28 inference. Its new contents remain forbidden
as premises in already-underway unrelated F15/JT13 initials. All frozen
R24/R26/R27 and prior review bytes remain unchanged. Any new substantive
defect requires author repair and BOTH affected reaudits.

## 5. ALL24 constructor obligations

Every row is a constructor check, not independent acceptance.

|ID|Obligation / constructor disposition|
|---|---|
|O01|RETAINED official2021(b), actual rational common values varying by derivative; no preliminary research.|
|O02|RETAINED ENTIRE(S),(W)/m4/J15/frameIII, multiplicities/carrier14 and all original19/center equations.|
|O03|RETAINED accepted R26/R27 d2,A9/A10zero,t>=2 and precise E8 cover; no stronger local assumptions.|
|O04|CHECKED exact integral interpolation/low rows/fixedA19=A20zero before specialization.|
|O05|CHECKED b0 plus ACTUAL A9/A10zero determines c/k; no arbitrary formal witness replacement.|
|O06|CHECKED each high row and center h/h/h/1/h/1/h/1, exact ORIGINAL Q equation.|
|O07|CHECKED coefficient degree bounds17, integer W and entire finite coefficient identity obligation.|
|O08|CHECKED COMPLETE degree17 W coefficient residues modulo37 and leadingunit27.|
|O09|CHECKED ALL37 field values, including0/negative representatives; nonezero.|
|O10|CHECKED rational denominator divisible37 excluded by unique surviving highest term after clearing.|
|O11|CHECKED denominator coprime37 reduces to an exhausted F37 element; all rational heights/signs covered.|
|O12|CHECKED black-box rational factorization not a premise; no irreducibility claim needed.|
|O13|CHECKED bnonzero forces ACTUAL S cover, not a new cover or rational lift.|
|O14|CHECKED COMPLETE E8 Taylor signs/binomial coefficients and E7zero.|
|O15|CHECKED each of SIX remaining divided-term lower depths at every finite t>=2.|
|O16|CHECKED unit E6 and odd rational square give quotient1mod4 and exact bdepth2+2t.|
|O17|CHECKED E7(S) leading term exactdeptht; E8'(S)nonzero and simple root.|
|O18|CHECKED full rational cover plus carrier14>8 gives FULL gcd, not only a displayed factor.|
|O19|RETAINED S-cover/highercontact/globalrationalcarrier/fullframeIII/degree20/annual gaps.|
|O20|SAVED complete exact finite certificate program/output/commands/dependencies, failed primes, timeout/PID/reaped status.|
|O21|DISCLOSED new mathematical computation versus documentary integrity; no old/source/author executable replay.|
|O22|DISCLOSED exact accepted-source read scopes, old root roles and official wording; no fresh whole-foundation/priority claim.|
|O23|REQUIRED TWO OTHER initially blind ENTIRE whole audits, author excluded, all code/meta/source/failure/issue records.|
|O24|REQUIRED FULL final ALL5payload+manifestMODELreadbacks THEN SEPARATEreadonlyverify before handoff, sameweeklyreserve.|

No known substantive defect after constructor checks; this is NOT an
independent verdict. Six-file packet: main, sources including complete
computational provenance/output, finite certificate program, documentary
helper, compact baseline, freeze. No recursively expanded historical
inventories or mutable-map guards. At86%TOTAL current1792874445 the
remaining four points include both audits and integration; no automatic
later-window spending.
