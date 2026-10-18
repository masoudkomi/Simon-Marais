# R12 whole independent initial review 1

18 October 2026 UTC. **Complete initially blind NONCONSTRUCTOR WHOLE audit; not coordinator acceptance.** Reviewer: `/root/review_2022_complexity_r2`. Requested inherited gpt-6.1-sol/max; independent effective-setting readback unavailable.

I reconstructed all three proposed claims, every one of the sixty author obligations, both finite-field certificates, and the actual-witness applications. I found **no substantive defect or required mathematical repair** in the exact frozen R12A–R12C statements. This is one whole audit. The other independent whole audit and the coordinator's complete reconciliation remain required before promotion.

Exact target: `problems/2021-B4/notes/reasoning-return-r12-candidate-v1.md`, 17602 bytes, SHA256 `7600005b20756bf9613e2b02177d5ae50aa5d3f573a6aa267bf245ee0a5c8f19`. Constructor freeze: `reasoning-return-r12-freeze-v1.json`, 4087 bytes, SHA256 `3ed49540ef24d6b947add1abc2db155f6c3bda82c8e2a40c7615547aa3351f02`.

The NEW R12 proof is A's construction. I did not contribute to it. I have reviewed several older 2021 packets, including R3, R5–R7, R10 and R11, and constructed the OLD R9 packet. Those roles are disclosed; separately accepted inputs are used at their exact accepted scopes, not represented as fresh independent recertifications of my old work. The root's assignment supplied no new R12 mathematical inference. I did not open any NEW root R12 report, ledger, findings, source record, integrity file or manifest before completing and freezing this entire initial. An earlier acceptance record's references to OLD R11 reviews are not NEW R12 findings.

## 1. Exact problem, conditional branch and authority

The official 2021 B4(b) asks for the possible degrees under a rational-coefficient polynomial's requirement that each derivative share an **actual rational root** with the polynomial. The witness can vary with the derivative. This audit concerns only the specified degree20 residual branch. Other roots need not be real or rational. No preliminary construction or proof is investigated.

The candidate retains the accepted normalized domain

    f=X^20-20X^19+sum_(j=2)^18 binom(20,j)a_j X^(20-j),
    a_j in Z_(19), a0=1, a1=-1, ord_0(f)=2,
    f(1)=0, J=15, H3(1)=0, H2(1)H4(1)!=0,

and, importantly, the ADDITIONAL actual double-root hypothesis

    f=X²(X-r)(X-s)²(X-1)g,
    Q-root values={0,1,r,s},
    v19(r)=v19(s)=nu>=1, s/r=2 mod19,
    H2(r)=H4(r)=0.

These four rational values are distinct; r and1 are simple, 0 and s double. This is not an inference that two residue slots must collide. The allowed case s=2r is exact equality of rational numbers; arbitrary finite displacement depth is also retained. The hypotheses must hold for an actual polynomial satisfying all contest witness conditions.

I read the complete accepted R11, R8, R5 and PN bodies, the return-r3 proof register and the exact frozen TA1 transfer body, together with their complete acceptance scopes. Their operative statements are:

* R11B excludes simultaneous H6(r),H8(r),H10(r),H12(r)=0 in this exact actual double-s branch.
* R8B applies at the first higher even break. It gives a nonzero NONUNIT essential-center constant at one of three consecutive orders, or the four-depth block, or one of its explicitly classified cubic alternatives. Its Euler estimate makes the first-break constant nonunit. At m6 the cubic alternatives both have v(a6)>=nu+sigma with 0<=sigma<nu; the four-depth case has v(a6)>=2nu.
* PN3 says some even a2,a4,...,a18 is a unit. Its accepted older 64-case argument is not rerun here.
* TA1, for 3<=m<=8, requires the preceding actual even ladder, a unit a_(19-2m), and an ACTUAL rational noncenter H_(2m) witness. It then forces that witness to be the actual r. It does not create a witness from a residue root or dispense with the unit hypothesis.
* R5C/G1 excludes the GLOBAL rational irreducible carrier from every derivative, including the equal-degree H6 boundary. This is used only for R12C's full-gcd conclusion.

These exact premises have accepted authority. R12 does not depend on a new unreviewed packet. The proposed result remains a partial restriction even when all its premises are accepted.

## 2. Derivative indexing and witness products

For H_k=f^(k)/k!, direct differentiation gives

    H_(20-j)(f)=binom(20,j)D_j,
    D_j(X)=sum_(k=0)^j binom(j,k)a_k X^(j-k).

This follows from binom(20,k)binom(20-k,20-j)=binom(20,j)binom(j,k). All operations take place over Q before reduction. For 2<=j<=18 the binomial scalar has valuation1 and D_j is integral monic.

At each actual small rational root w in{0,r,s}, w is in19Z_(19), so D_j(w) reduces to a_j. An actual derivative witness is either one of these three values or1. Hence

    a_j D_j(1)=0 in F19

is necessary. It is not sufficient for a rational lift. A unit a_j forces the ACTUAL witness to be1 and therefore the exact equality D_j(1)=0 over Q. In particular a15 is a unit, so D15(1)=0 is an actual H5 center; stipulated H3(1)=0 gives actual D17(1)=0. Confusing D15 with H15 would invalidate the proof, but the candidate does not do so.

Under Q6, the only possible nonzero residues beyond a0,a1 are

    A=a2, B=a3, C=a4, E=a5, V=a6,
    x=a7, y=a9, z=a11, w=a13, u=a15.

The six even indices8,10,12,14,16,18 vanish modulo19. J15 makes a17 nonunit and ord_0(f)=2 makes a19=a20=0 exactly. In particular V has NOT been discarded. The field proof permits u=0 despite the true unit a15; this enlarges the relaxed necessary system and is legitimate because no coefficient is divided.

## 3. Independent reconstruction of all three global rows

After cancelling the rational factor19,

    beta_j=binom(20,j)/19 = (-1)^j/[j(j-1)] mod19.

Every denominator here is invertible. At indices2,3,4,5,6 the beta values are10,3,8,-1,7. At7,9,11,13,15 they are14,5,5,14,18. Since 1-20=-19, dividing f(1)=0 by19 gives -1+sum beta_j a_j=0. Multiplying its odd part by -1 gives exactly

    5x+14y+14z+5w+u=-1+10A+3B+8C-E+7V=L.

Reducing f(1) without the prior division would give no such row. This is an essential compatibility equation, rather than a new assertion that the unscaled reduction carries information.

For D15 the constant/low coefficients at 0,2,...,6 are

    5,10,-1,-3,1,8,

and its coefficients at7,9,11,13,15 are13,8,16,10,1. For D17 they are respectively

    3,3,15,5,13,7  and  11,9,7,5,3.

The constant entries are 1-15 and1-17. For example binom(15,6)=5005=8, binom(17,6)=12376=7, binom(17,9)=24310=9 modulo19. Thus their actual center equations give exactly the displayed R and S rows, including -8V and -7V on their right sides.

Put K=R-L and N=S-3L. Direct subtraction gives

    K=15-A-2B-5C+4V,
    N=5A-5B+9C+9E+10V,
    K=8x+13y+2z+5w,
    N=15x+5y+3z+9w.

The last two rows have determinant 2*9-5*3=3 in their z,w columns. Inverting this fixed nonzero scalar gives

    z=3K-8N+x+y=Z+x+y,
    w=7N-K+17x+16y=W-2x-3y,
    Z=7+14A+15B+8C+4E+8V,
    W=4-2A+5B+11C+6E+9V.

I also checked these formulas by substituting the K,N linear forms: the x,y cross coefficients cancel modulo19 and the z,w coefficients become the identity. No potentially zero x,y,z,w,u, root or displacement is inverted.

## 4. Complete small product equations and root sets

Direct Pascal rows give

    A(A-1)=0,
    B(B-2+3A)=0,
    C(C-3+6A+4B)=0,
    E(E-4+10A+10B+5C)=0.

Consequently (A,B) is exactly 00,02,10,1(-1). For each, C is0 or C*=3-6A-4B; E is0 or E*=4-10A-10B-5C. No nonzero value or root choice has been silently assumed.

The next Pascal rows give the following independent coefficient check. Entries are at A,B,C,E,V, followed by the additional odd coefficients:

|Derivative|constant|A,B,C,E,V|odd terms|
|---|---:|---|---|
|D7|13|2,16,16,2,7|x|
|D9|11|17,8,12,12,8|-2x+y|
|D11|9|17,13,7,6,6|7x-2y+z|
|D13|7|2,1,12,14,6|6x+12y+2z+w|
|D8|12|9,-1,13,-1,9|8x|

For instance binom(13,5)=1287=14 and binom(13,6)=binom(13,7)=1716=6. Let p,q,d,c be the first four constant-plus-low forms above. Then the necessary products are

    x(x+p)=0, y(y-2x+q)=0,
    z(z+7x-2y+d)=0, w(w+6x+12y+2z+c)=0.

Using z=Z+x+y, the two middle products are exactly the requirement

    y in {0,2x-q} intersect {-Z-x,Z+8x+d}.

The first member of the second set comes from z=0; the second from the center factor's vanishing. Repeated set entries do not change this equivalence. Both y=0 and z=0 remain covered. For brevity write S7=x+p and S8=12+9A-B+13C-E+9V+8x. These are the exact reduced D7(1),D8(1).

## 5. Whole V=0 reconstruction

With V=0, PN3 forces A or C nonzero. The six possible triples are exactly

    003, 0(2)(14), 100, 10(16), 1(-1)0, 1(-1)1.

I recomputed ALL twelve x=0 rows. To expose independent intermediate arithmetic, this table records Z,q,d at E=0 and at the permitted E*. The set pairs follow by negating q,Z and adding Z+d, rather than by an executable search.

|A,B,C|E*|(Z,q,d) at E=0|(Z,q,d) at E*|
|---|---:|---|---|
|0,0,3|8|(12,9,11)|(6,10,2)|
|0,2,14|9|(16,5,0)|(14,18,16)|
|1,0,0|13|(2,9,7)|(16,13,9)|
|1,0,16|9|(16,11,5)|(14,5,2)|
|1,-1,0|4|(6,1,13)|(3,11,18)|
|1,-1,1|18|(14,13,1)|(10,1,14)|

For these rows the resulting Y9/Y11 pairs, in the same order E=0 then E*, are

    {0,10}/{7,4};   {0,9}/{13,8};
    {0,14}/{3,16};  {0,1}/{5,11};
    {0,10}/{17,9};  {0,6}/{3,6};
    {0,8}/{3,2};    {0,14}/{5,16};
    {0,18}/{13,0};  {0,8}/{16,2};
    {0,6}/{5,15};   {0,18}/{9,5}.

Only two intersections remain. At (A,B,C,E,x,y)=(1,0,0,13,0,6), Z=16,W=4,z=3,w=5,c=1, and the last center factor is5+72+6+1=84=8. Its prefactor w=5 is nonzero. At (1,-1,0,0,0,0), Z=6,W=16,z=6,w=16,c=8; the last center factor is16+12+8=36=17 and again w is nonzero. Thus the last actual witness product excludes both. This proves x!=0 for V=0 without excluding any zero coefficient in advance.

Now x=-p. Substitution in S8 gives

    S8=3+12A+4B-C+2E.

If S8=0 and C=0, PN3 gives A=1. B=0 requires E=2, outside {0,13}; B=-1 requires E=4 and is retained. If C!=0, substituting C* gives E=10A-4B. E=0 leaves only (A,B)=(0,0), whereas E!=0 compared with E*=8+A+10B gives9A+5B=8. Its four values0,10,9,4 never equal8. The two surviving quadruples are therefore0030 and1(-1)04.

At0030, p=4,x=15,Z=12,q=9,d=11; the sets are{0,2} and{11,10}. At1(-1)04, p=7,x=12,Z=3,q=11,d=18; the sets are{0,13} and{4,3}. Both are disjoint. Thus V=0 forces x!=0 and S8!=0. No claimed actual lift was used in the finite elimination.

## 6. Whole V!=0 reconstruction

A unit V forces the ACTUAL D6 witness to be1. Reducing that exact equality gives

    V=5-15A-B-15C-6E.

Substituting this into p and S8 gives

    p=10+11A+9B+6C-2E,
    S8=T+8x, T=7A+9B+11C+2E.

Here the constant of T is zero because12+9*5=57. I recomputed all eight pairs of allowed E choices, retaining even the choices for which V=0 and marking their exclusion only at this stage:

|A,B,C|E*|V at0,E*|p at0,E*|T at0,E*|
|---|---:|---|---|---|
|0,0,0|4|5,0|10,2|0,8|
|0,0,3|8|17,7|9,12|14,11|
|0,2,0|3|3,4|9,3|18,5|
|0,2,14|9|2,5|17,18|1,0|
|1,0,0|13|9,7|2,14|7,14|
|1,0,16|9|16,0|3,4|12,11|
|1,-1,0|4|10,5|12,4|17,6|
|1,-1,1|18|14,1|18,1|9,7|

If x=0, every p entry is nonzero, so S7!=0. The only T=0 entries with V nonzero are000E0V5 and0(2)(14)E9V5. The former gives Z=9,q=13,d=1, hence sets{0,6}/{10}; the latter gives Z=16,q=1,d=8, hence{0,18}/{3,5}. Both are disjoint. Thus x=0 also forces S8!=0. This covers a7=0 exactly as well as nonzero a7 of any positive valuation.

If x!=0, its product forces x=-p. Then S8=0 is equivalent to

    E=15-5A-6B+C.

For C=0 the four required E values are15,3,10,16; their allowed choices are{0,4},{0,3},{0,13},{0,4}. Only (A,B,C,E)=(0,2,0,3) survives. For C!=0, substitution gives E=-1+8A+9B. E=0 would require8A+9B=1, but the four values are0,18,8,18. E!=0 compared with E*=8+A+10B would require7A-B=9, but the four values are0,17,7,8. Thus no C!=0 case survives.

The sole remaining prefix has V=4,p=3,x=16,Z=5,q=0,d=1. Its sets{0,13}/{17,1} are disjoint. Therefore S8!=0 here too. The four V/x zero/nonzero regimes are exhaustive. This proves all of R12A: D8(1) unit; V or x unit; and x=0 implies V and D7(1) units.

Care is needed with scaling: D8(1) is a unit but H12(1)=binom(20,8)D8(1) has valuation1, not0. That still proves actual H12(1)!=0. The analogous H13 conclusion when x=0 follows the same way. The candidate states these implications correctly.

## 7. Full actual first-break application

Assume H6(r)=H8(r)=H10(r)=0. Together with the fixed H2,H4 equations, R11B forces H12(r)!=0, so the first break is exactly m6, e=12,j=8. Evaluating the preceding actual D_j(r)=0 equations modulo19 makes a10,a12,a14,a16,a18 nonunit. The accepted Euler estimate at j8 gives v(a8)>=nu. Thus Q6 holds. No unsupported support restriction from the older m7 calculation has been recycled.

R12A makes D8(1) a unit, hence H12 cannot share center1. The contest property therefore supplies an actual rational noncenter witness. If a7 were a unit, TA1 at m6 would force that actual witness to be r, contradicting H12(r)!=0. Its exact hypotheses are all satisfied: m6 is in range, the full preceding ladder is present, roots are the four values in W, the double-s branch and unit-linear condition are retained. Hence a7 is nonunit.

R12A then forces a6 unit and D7(1) unit. Thus H13 cannot share1. In the complete R8B fork:

* EC12 is excluded by H12(1)!=0.
* EC13 is excluded by H13(1)!=0.
* EC14 has a NONUNIT a6 by its theorem statement, incompatible with the forced unit. A unit-centered derivative at H14 is not itself asserted impossible; it simply cannot fulfill this particular nonunit EC alternative.
* T4 requires v(a6)>=2nu.
* Each m6 cubic requires v(a6)>=nu+sigma, 0<=sigma<nu.

All five possibilities are excluded, including sigma=0, infinite valuations for zero coefficients, exact displacement0 and arbitrary finite displacement depth. This establishes R12B, without any additional odd-unit assumption, upper depth bound, ordinary height comparison or Q19-to-Q lift.

## 8. R12C and the global/nonrational boundary

Assume only the extra units a13,a11,a9. If each of H6,H8,H10 has a rational noncenter common root, TA1 applies successively at m3,m4,m5. The preceding ladder for each application was established at the previous step, and the relevant unit is respectively a13,a11,a9. It forces all three values at the actual r to vanish, contrary to R12B. Hence some selected derivative has NO rational noncenter common-root value. The contest hypothesis supplies a rational witness, so1 is its sole rational value.

This alone would not exclude nonrational common roots. The separately accepted R5C/G1 does: its global irreducible carrier contains all fourteen cluster roots and is coprime to every derivative. In the degree-equality H6 case, its trace coefficient is divisible by19 whereas normalized D14 has X13 coefficient -14, a unit. Thus even that boundary is covered by the accepted theorem. The only possible common values are the four rational ones in W;1 is simple. The full monic gcd is consequently X-1. The candidate has not silently replaced global coprimality by a local root calculation.

The three extra units are not established automatically. R12C is a conditional essential-center consequence, not a contradiction to the existence of the whole branch.

## 9. Adversarial attempts and limits

I checked the cases most likely to break the argument: V=x=0, zero y/z/w/u, repeated Y-set entries, C=0 versus C=C*, E=0 versus E=E*, a7=0 exactly, the V=0 entries appearing in the second certificate, sigma=0 in the cubic case, infinite coefficient/displacement valuations, and both double-origin normalizations. All are either explicitly present or outside a clearly stated subsection and handled in another one. No counterexample to the claimed statements emerged.

The essential dependence is on actual rational witnesses: the field products merely eliminate necessary assignments, while TA1 is invoked only after actual existence and center nonvanishing are known. A residue solution would not supply an actual witness; the proof never needs that converse. It also neither assumes every root rational nor applies a CA theorem to the degree-six quotient. Missing-unit cases are not converted into injective maps.

R12A uses Q6. Earlier first breaks m3,m4,m5 can carry other even units; their contributions must be retained in the global rows, and the displayed Q6 formulas cannot be reused there. Distinct2R slots, multiplicity3, other center patterns, lower J, the full degree20 problem and the annual classification remain open. R12 does not establish novelty, a rational lift, an effective height bound or a general valuation maximum.

The accompanying issue record retains four scope notes, all resolved by the existing exact text, and zero required repairs. No candidate/old/shared/cache/Git byte was changed. No mathematical code, native child, CAS, mask scan, author program or old certificate was run. The compact immutable parents, precise source read limits and all sixty per-inference checks accompany this frozen initial.
