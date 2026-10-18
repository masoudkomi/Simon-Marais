# Exact plane-boundary recovery from finite completion

2026-10-18 UTC. **Candidate proof - unverified.** Root is the sole NEW
constructor. TWO OTHER initially blind whole audits and coordinator
reconciliation are required. No mass variational principle, upper hypothesis
R, numerical value, annual solution or novelty is claimed.

This deduction uses the separately accepted repaired PM1–PM4 and US_D1–3.
It was constructed AFTER both PM affected whole audits and reconciliation.
It changes no frozen PM proof or reviewer statement. PM3 itself asserted
only an upper plane interface; this packet supplies a separately reviewable
lower interface with the exact original plane reference kept outside a
fixed dilated replacement disk.

## 1. Definitions and exact accepted inputs

Fix D>=3, v_i=(1,i-1), and the actual integer plane tilings X_D defined in
PM1. A tile is an integer translate of [0,v_i]+[0,v_j]. Its anchored integer
lift a integrates the colored edge increments and satisfies Va(x)=x.
No arbitrary local bit block or formal boundary decoration is assumed to
have a plane realization.

For an actual positive-area finite Jordan tile disk Omega in a plane
tiling T, define T^(M), for integer M>=1, by dilating T by M and subdividing
every enlarged tile into its M-by-M parallelogram grid. Grids agree along
each shared edge. Every new vertex is integer and the canonical fine lift
satisfies a_(T^(M))(Mx)=M a_T(x), with affine interpolation. In particular
this is an actual integer plane tiling. Denote by R_M^pl(T,Omega) the number
of fillings of the EXACT disk M Omega, with its complete dilated physical,
colored and lifted boundary, while keeping T^(M) outside. The region is
fixed from the ORIGINAL Omega, rather than newly extracted at scale M.

The count is finite: the region is bounded, tile origins are integer and
the tile alphabet is finite. It is positive because the subdivided original
patch supplies one filling. A filling is counted by its actual tile set,
with no outside tiling, translation or lift-anchor multiplicity.

The accepted premises, and only their stated scopes, are:

1. Repaired PM2 completes every actual finite plane Jordan patch into a
   full zonogon, preserving the marked patch up to ONE integer translation
   and ONE common integer lift rebase. It gives one exterior for the entire
   complete-boundary fibre. Missing ambient colors are allowed.
2. The actual Jordan-crop construction in accepted PM3 section5 supplies
   a finite Jordan tile disk containing any prescribed buffered bounded
   convex region in its interior. This is an actual patch in the given
   plane, not a boundary-only or nonextendable finite decoration.
3. Accepted US_D1 fixes, for rational J' in a compact STRICT domain and
   one denominator q/phase, the SAME counts C_m, density e, bounds
   log2 C_m<=e(qm)^2 for EVERY m, 0<=e<=H, and the all-integer-size limit.
   Its fixed end-lobe factor is B_end.
4. Accepted US_D2 gives, at t=sqrt(epsilon), L>=C(q+1)/t, a Jordan CUT
   disk in an actual full reference, containing the C_cut tL erosion of
   P_L and contained in its C_cut tL enlargement. Its exact-dilation
   LOWER construction gives C_(k_M)/B_end fillings, with
   k_M=floor((ML-2A0 tML)/q), for all sufficiently large integers M.
5. Accepted PM3 gives the plane-family UPPER estimate with the same
   rational receiving family: log2|F|<=log2 C_(m_+)+K'(tL²+L+1),
   m_+=ceil((L+2A0 tL)/q), in the same common-offset/whole-buffer domain.

The accepted US_D1 section7 rounding formula permits translating that ONE
receiving frame to any physical starting corner and any c in ker V, with
uniform bounded errors. Thus C_m is not changed when source coordinates
or height anchors are rebased. No equality of densities for DIFFERENT
rational frames or DIFFERENT phases is assumed.

## 2. PUS1: complete-boundary counts are exterior-independent

Let S be any actual full completion of Omega supplied by PM2. Write its
physical coordinates as x'=x-x_out on the marked patch and its full
canonical lift as a_S(x')=a_T(x)-b there, with b integer and Vb=x_out.
Let Omega'=Omega-x_out be the corresponding patch of S.

For EVERY integer M>=1 there is an exact bijection

    R_M^pl(T,Omega)=R_M^full(S,Omega').                 (P1)

On the right the finite full reference S is uniformly subdivided after
dilation, and its exterior of M Omega' is fixed. To construct the map,
restrict a full replacement to M Omega', translate it physically by
M x_out and its lift by M b, and glue it to T^(M) outside M Omega.
On every fine boundary edge and vertex the old subdivided marked patches
are identical under this translation. The tile supports are the same
Jordan disk; their interiors are disjoint from the fixed exterior and
there is no seam gap. Colored boundary increments and ONE anchor give
the same full lift boundary. Thus this is an actual edge-to-edge plane
tiling, not just a local diagram. PM1 then supplies its train-track
properties; no new matching rule across distant exterior tracks is imposed.

Conversely, restrict a plane replacement to M Omega, translate by
-M x_out and rebase by -M b, and glue it to the subdivided full S exterior.
The same boundary argument gives an actual full tiling. Restricting in
either direction recovers exactly the same tile set, so the maps are
inverse. Distinct interiors are never identified. The argument uses the
complete boundary and an actual reference on EACH side; it does not say
that arbitrary boundary data can be filled.

In fact this bijection works for any two actual exteriors realizing the
same complete boundary. The full completion is useful to obtain the
separately accepted LOWER theorem, not an extra restriction on plane
replacement interiors. Every M is allowed in(P1), including M1.

## 3. PUS2: the lower construction keeps the ORIGINAL plane exterior

Use the exact compact-strict rational setup of US_D2: fixed D, rational
J', q, one phase, one allowed physical frame,

    P_L=x0+{s u_h+t v_h:0<=s,t<=L},
    VJ'=I, det(J'_i,J'_j)>=rho>0,
    ||a_T(x)-J'x-c||_infinity<=epsilon L, Vc=0,

on the WHOLE required US buffer of P_L. Here t in the error formulas
below denotes sqrt(epsilon), rather than the frame's second coordinate.
Assume L>=C_*(q+1)/t and epsilon small enough for all accepted thresholds;
the constants depend on the fixed compact strict family, not q or T.

Choose a larger bounded convex W whose interior contains that entire
closed buffer with an additional tile margin. Crop and fill bounded
holes as in accepted PM3 to get an ACTUAL Jordan tile disk P in T
containing W. Its boundary has O(L) edges. Apply repaired PM2 to P,
obtaining a full S which agrees with T on P after its one translation
and lift rebase. Consequently S contains the ENTIRE required buffer,
including all its source tiles and affine interpolations.

In S coordinates x'=x-x_out, the same affine estimate has offset

    c*=J'x_out+c-b,
    Vc*=x_out+0-x_out=0.                              (P2)

This is one offset for the entire S reference. Apply accepted US_D2's
lower construction to this SINGLE full reference (using a singleton
family if its statement is presented jointly with the upper one). Its
J', q, phase and counts C_m are the already fixed ones. The physical
translation changes the starting corner and c*, handled by US_D1's
rounding formula; it does not select another phase or density e.

US_D2 extracts one Jordan disk Omega' inside its buffered region and
fixes it at the original scale. Every tile in that disk is in the marked
P, where S agrees with T. Set Omega_T=Omega'+x_out. It is therefore an
ACTUAL Jordan tile disk in the ORIGINAL T, with

    P_L eroded by C_cut tL subset Omega_T
      subset P_L+closed_ball(0,C_cut tL).              (P3)

For all sufficiently large integer M, accepted US_D2 gives

    R_M^full(S,Omega')>=C_(k_M)/B_end.

Apply the exact boundary bijection(P1), now to Omega_T and this S.
It gives

    R_M^pl(T,Omega_T)>=C_(k_M)/B_end.                 (P4)

The exterior kept on the left is T^(M) at EVERY point outside the EXACT
M Omega_T. It is not the completed full exterior, and the region is not
re-extracted at M. The exterior S outside the original P was a finite
auxiliary device only and has been discarded. The proof never requires
preserving that completion while also preserving the original plane.

The completion may depend on T and have macroscopic size. Its only use
here is existence of a full reference on a specified buffer; no collar
area, minimum added angle or ambient track count enters an error bound.
Hence C_* and the epsilon threshold remain independent of q. For a fixed
original T,L the large-M threshold may depend on those actual data, as
in the accepted theorem; no new uniform rate of convergence is asserted.

## 4. PUS3: same-density recovery for a plane family and plane reference

Let nonempty F be distinct restrictions to P_L with ACTUAL integer plane
representatives, and let T be ONE actual plane reference. All satisfy the
SAME J',c affine estimate on the WHOLE required buffer. T need not belong
to F. Apply accepted PM3 to F for its upper estimate, and PUS2 separately
to T for the lower estimate on its ONE original Omega_T. The upper
proof's joint trace/anchor class and completed exterior need NOT equal
T's auxiliary completion. Both inequalities nevertheless use EXACTLY
the same FIXED J',q,phase receiving counts C_m. Absolute physical/lift
offsets are handled by translation, not by changing those counts.

The every-m upper and the all-size density limit give

    log2|F|<=e[(1+2A0t)L+q]^2+K'(tL²+L+1),
    liminf_M M^-2 log2 R_M^pl(T,Omega_T)
                      >=e[(1-2A0t)L]^2.              (P5)

The second limit is at FIXED original L,T,q,phase. In particular it
does not assume a convergence modulus uniform in q or replace the
region by one depending anew on M. For q<=tL,t<=1 the two squared
spans differ by at most(12A0+3)tL². Using e<=H and L>=1/t,

    log2|F|<=liminf_M M^-2 log2 R_M^pl(T,Omega_T)
                         +C_loss*sqrt(epsilon)L²,    (P6)
    C_loss*=H(12A0+3)+3K'.

No unknown density is estimated numerically or cancelled between
different frames/phases. It is the SAME e in both lines of(P5).

For a REAL compact strict family K, the exact US_D3 order of choices
now gives: for every eta>0 there are epsilon>0, a finite rational net
with fixed q/phase per net point, and L0<infinity, chosen in that order,
such that whenever L>=L0 and F,T have the same real tangent J in K,
common c and required whole-buffer epsilon L estimate,

    log2|F|<=liminf_M M^-2 log2 R_M^pl(T,Omega_T)+eta L². (P7)

Indeed first choose epsilon so C_loss*sqrt(2epsilon)<=eta and all
fixed geometric margins hold. Then approximate J by a rational net
within epsilon/C_box, keeping the compact strict chart. The common
offset becomes c+(J-J')x0 for BOTH F and T, in ker V. The whole-buffer
error is at most2epsilon L; enlarge the buffer constant once for its
sqrt2 factor. Choose each period/phase only after that tolerance, then
L0 as the maximum of the finitely many rational scale thresholds.
Apply(P6) at2epsilon. No tolerance shrinks after its denominator is seen.
The extraction in(P7) is the one obtained for the chosen approximant and
ORIGINAL T at ORIGINAL L. Its dilations are exact and preserve T^(M).

## 5. Limits and failed shortcuts

This is a local strict recovery theorem at every scale where actual
references exist. It supplies neither all-scale reference existence nor
a global mass variational principle. Arbitrary inserted interiors can
deviate by O(L) in lift, not an asserted O(epsilon L). No density-one
packing, negligible completion collar, free/balanced entropy equality,
boundary-stratum induction, growing-D uniformity, upper hypothesis R,
numerical scalar, annual solution or novelty is established.

One must not apply US_D2 directly to an incomplete plane graph. The
finite completion is performed first, with the ENTIRE buffer retained.
One must not require T to be in the upper proof's largest trace class;
the two applications are separate and use the same receiving counts.
One must not keep the completed exterior and call it the original plane
exterior; the exact boundary bijection is what transfers the LOWER
count. One must not move a physical translation only once after dilation;
the correct translation and height rebase are M x_out and M b.

Root contributed the older integer-grid lead to PM, but is excluded from
the OTHER audit count for THIS new construction. C's old PM authorship
and A's old US authorship are separately accepted input roles; neither
would be a fresh independent recertification of its own old theorem.
No reviewer has yet audited this NEW whole argument. Sources, obligations,
failed routes and compact immutable input records accompany this version.
