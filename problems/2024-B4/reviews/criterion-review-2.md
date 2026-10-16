# 2024 B4(b): blind independent criterion review R2

**Review completed 2026-10-16. No substantive objection identified.**
This is an independent adversarial audit, not a coordinator promotion.
The candidate should retain its status until the coordinator has both
independent initial reports and resolves any objections from either.
No absolute-certainty claim is made.

The audited claim is exactly: in F2[x,y,z], for odd n>=3, phi_13 divides
phi_n if and only if n=(64*16^m+1)/5 for an integer m>=0. It concerns one
complete fixed divisor. It does not classify all reducible phi_n or
establish novelty. I find the argument valid within this stated scope,
with its finite certificate independently reconstructed below. R2 requests
no repair.

## Independence, settings, and frozen inputs

I did not construct this candidate. Before completing this report I did
not read any other review's contents or conclusions, shared issue log,
research/status files, or the earlier sufficient-family proof/audits.
A directory listing exposed filenames only. I did not import, execute,
or read the source of the author's builder, verifier, or renderer. Their
bytes were hashed solely to check the frozen manifest. I wrote a fresh
standard-library checker using raw Laurent supports and full sets of
subspace vectors. It reconstructed the orbit before reading the JSON
graph. The candidate note and readable certificate were available while
designing the audit.

Requested reviewer settings, as specified by the coordinator:
gpt-6.1-sol, max reasoning. Verified effective-backend settings:
**not available**. Requested settings are not verified readback.
Authoritative account-wide telemetry during this review reported 5%
total weekly used in the 10080-minute window, below the 90% stop threshold.
No separately billed API, purchase, or access bypass was used.

| Frozen input under problems/2024-B4/ | SHA256 |
|---|---|
| notes/zero-automaton-criterion-v1.md | 59e3bb1f9aba8162ea5b79f0ccec5f56b6f2cb0cc7917cfe81f4aff196ff6ab4 |
| notes/zero-automaton-certificate-v1.md | b384ed3c0b51572e729b1e5486847ebcc5d964f4afa64c43e60a76910ad0ddd3 |
| notes/zero-automaton-v1-manifest.json | 41fef0ca55da72d8efc8fb04f3b0180f77fc43edf28b276a87f7bd033b6687f2 |
| computations/zero-automaton-v1-graph.json | ee818f60e68da70ae2f0f7fa84a2c4dec740d10d03908359a271e354a1a0ce4e |

The independent check JSON additionally records bytehash verification
of all 15 entries in the author's manifest. These hashes fix the reviewed
version; the author's programs/outputs are not independent mathematical
evidence here.

Only criterion-review-2* artifacts in the assigned reviews directory
were written. No proof, shared file, prior review, cached paper, Git
commit, push, promotion, or other owner's job was modified.

## Official statement and boundary audit

I read statement.md and the cached official 2024 Paper B page 2,
extracted it with pypdf, rendered it with bundled pdftoppm, and visually
inspected criterion-review-2-official-page2.png. The official source is
https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf.
The original was already cached at .cache/official/2024-paper_b.pdf;
no new download was needed. The evidence manifest records source and
rendering hashes. Verification date: 2026-10-16.

The official domain is an odd positive integer n, integer coefficient
polynomials g,h, coefficientwise congruence modulo 2, and neither factor
constant modulo 2. The F2 polynomial-ring formulation matches all these
requirements. Polynomial functions on F2^3 would be insufficient; that
interpretation is never used. This is a B4(b) review only; no preliminary
part solution is reconstructed or used as a proof check.

The restriction n>=3 in the criterion is essential: f_1=0, so every
polynomial would divide phi_1 if that zero quotient were defined. For
the official target, n=1 is excluded because R and the two nonconstant
F2 polynomials are nonzero and their product cannot vanish in the
domain F2[x,y,z]. At n=3 the quotient is 1, and the fixed divisor does
not divide it. At n=13, self-divisibility gives cofactor 1; the candidate
correctly withholds a B4(b) reducibility conclusion there. The change of
index j=(n-3)/2>=0 covers exactly the stated odd domain.

## Whole argument reconstruction

### 1. Generating identity and the formal divisor

For x,y,z,w=x+y+z, with multiplicity, direct elementary symmetric
expansion gives e_1=0, e_2=Q, e_3=R, e_4=D. Thus

    E(t)=product(1+a*t)=1+Q*t^2+R*t^3+D*t^4.

Every factor and E have constant coefficient 1, so formal inverses exist.
The product rule gives t E'/E=sum_a a*t/(1+a*t). Characteristic-2
geometric expansion makes this sum equal sum_(n>=1) f_n*t^n.
Since E'=R*t^2, it follows that

    sum_(n>=1) f_n*t^n=R*t^3/E(t).

This establishes divisibility coefficientwise, with no specialization
or numerical division by R. For n>=3, phi_n=[t^(n-3)]1/E. Using
1/E=E/E^2 and extracting even t degrees, with s=t^2, gives

    sum_(j>=0) phi_(2j+3)*s^j
      =(1+Q*s+D*s^2)/(1+Q^2*s^2+R^2*s^3+D^2*s^4).

Abstracting (Q,R^2,D) to independent variables (q,u,d) gives P_j.
Multiplication by the denominator yields

    P_0=1, P_1=q, P_2=q^2+d, P_3=q^3+u,
    P_4=q^4+q^2*d+q*u+d^2,
    P_5=q^5+q*d^2+u*d=A.

The two q^2*u terms in P_5 cancel correctly. Weights (2,6,4) give
weight 2j, consistent with actual degrees. The fresh checker verifies
the elementary symmetric identity, P_5, and f_n=R*P_j(Q,R^2,D) for the
31 odd n from 3 through 63 by direct support algebra. The finite
identities support the general formal derivation; they do not replace it.

### 2. Localization and exact Laurent vanishing

Regard A=d*u+q*(q^4+d^2) as a polynomial over F2[q,d]. Its coefficients
are coprime: a common irreducible would divide d and q^5. It is primitive
and degree one in u over F2(q,d); Gauss's lemma applies since F2[q,d]
is a UFD. Thus A is irreducible in S=F2[q,u,d], hence prime since S
is a UFD. Its u degree shows A does not divide q or d.

In U=S[q^-1,d^-1], d is a unit, so eliminating u gives

    U/(A)=F2[q^+/-1,d^+/-1],  u=q^5/d+q*d.

The Laurent-variable change b=d/q^2 is invertible:
d=q^2*b and u=q^3*(b+b^-1). Substitution s=z/q then gives

    F(z,b)=(1+z+b*z^2)/(1+z^2+(b+b^-1)*z^3+b^2*z^4)=P/K.

The z^j coefficient is the image of q^-j*P_j. Since q is a unit,
vanishing is equivalent to P_j in A*U. Clearing denominators gives
q^a*d^b*P_j in (A); primality and A not dividing q*d then give
P_j in (A). Conversely divisibility extends under localization.
Therefore

    A divides P_j in S iff [z^j]F=0 in F2[b,b^-1].

This explicit contraction is what prevents losing components at q=0
or d=0. No specialization there is assumed invertible in the original
ring. The last statement is an identity in the indeterminate b, never
a finite-field evaluation.

### 3. Cartier identity, support bounds, and conjunctive invariant

The ambient ring is Lambda[[z]], Lambda=F2[b,b^-1]. Each z coefficient
has finite b support, so products and all four sections are legitimate
coefficientwise. Negative h has a unique h=2c+t with t in {0,1};
for example -1=2*(-1)+1 and -2=2*(-1)+0.

K(0,b)=1. Frobenius gives K(z,b)^2=K(z^2,b^2), hence

    N/K=(N*K)/K(z^2,b^2),
    C_(r,t)(N/K)=C_(r,t)(N*K)/K.

The second identity follows by pulling a series with only even z and b
degrees through the section and halving its arguments. Each fixed z
coefficient involves finitely many products with finite Laurent support,
so no uncontrolled double-infinite convolution occurs.

If N has 0<=i<=3, -1<=h<=2, then N*K has 0<=i<=7, -2<=h<=4.
After parity selection and halving, its exponents lie again in
0<=i<=3, -1<=h<=2. At the lower boundary the even h=-2 and odd h=-1
both map to -1 in their respective sections. Thus all four L_(r,t)
preserve V, and P lies in V.

For h_i(b)=[z^i]H, the even and odd Laurent sections reconstruct

    h_(2a+r)(b)=h_even(b^2)+b*h_odd(b^2).

The summands have disjoint supports, including at negative exponents,
so the left side vanishes if and only if both sections vanish.
For a subspace W, the condition for every N in W is equivalent to
the condition on a basis by F2 linearity. Applying both sections to
every vector is equivalent to vanishing on the span of both images,
namely T_r(W). This establishes both directions of (9), with its
universal quantifier. No image independence is needed. In particular,
an existential interpretation of the b branches would be wrong, but
the candidate uses the required conjunction.

Starting at span(P), induction on bits read least significant first gives,
for every a>=0 and ell=sum_(h<k)r_h*2^h,

    [z^(2^k*a+ell)]F=0
      iff [z^a](N/K)=0 for every N in the reached W.

The base case is the one-dimensional initial span; each induction step
is (9). At a=0, K(0,b)=1 makes acceptance equivalent to zero z^0
coefficient of every state numerator, exactly the bottom-four-bit test.
The empty word is rejected because P has constant coefficient 1.
Appending zero bits leaves ell fixed; this same general invariant proves
acceptance invariance under any number of binary leading zeros.

### 4. Independent finite certificate and quotient language

The new checker constructs K,P as sets of actual (z exponent,b exponent)
pairs. Addition is symmetric difference; multiplication is ordinary F2
support multiplication. States are complete sets of Laurent-polynomial
vectors. For a bit r it takes both parity images of every vector and
closes under symmetric difference. No row reduction or author program
is used. The raw orbit closes before the JSON graph is read.

| Item | Freshly checked result |
|---|---|
| Reachable distinct subspaces | 48 |
| Operator matrices | All 64 columns match |
| Outgoing transitions | All 96 match and remain in the 48 states |
| Acceptance outputs | All 48 match; 6 accepting |
| State dimensions 1,2,3,4,5,6 | Respectively 1,3,9,17,12,6 states |
| Largest complete subspace | 64 vectors including zero |
| Listed basis spans and independence | Match every freshly built full space |
| Descending pivots and reduced columns | Checked for every listed basis |
| Readable certificate | Every operator and state row matches |
| Eight-class quotient | Partition, outputs, and both successors all match |

BFS processes both bits at every visited state. Its empty queue after
processing state 47 establishes transition closure. The 256-state cap,
internal 35-second limit, and external 45-second limit were not approached.
This audits the explicit finite algebraic certificate rather than assuming
that a bounded initial word search describes all future behavior.

For the quotient, X is closed and rejecting. The only non-X initial path
is 101, reaching C. C,D,E,Z accept. To read a future 1 and then accept
again, the only possible excursion is the full 0011 cycle
C->D->E->B->C. Final zeros from C remain accepting via D,E,Z,Z,...;
a 1 at any other place reaches X or ends at the rejecting B. Thus both
inclusions of the full finite-word language follow:

    accepted words = 101(0011)*0*.

No minimality assertion is needed. A canonical positive binary word,
read least significant first, ends in 1; it therefore has accepted form
101(0011)^m. The first block represents 5, and each 0011 has local
value 12 shifted by 3+4h bits. Consequently

    j=5+96*sum_(h=0 to m-1)16^h
     =5+96*(16^m-1)/15=(32*16^m-7)/5.

The empty sum gives j=5, and j=0 is excluded. These checks establish
the bit order, shift, sum, zero padding, and canonical representation.
Combined with the invariant and localization, they give the exact formal
criterion for every j>=0.

Extra finite evidence was obtained independently from K*F=P: all Laurent
coefficients through j=65535, represented as bit polynomials with a safe
fixed offset, agree with the fresh machine and regex. The only zero
indices in that range are 5,101,1637,26213. All 131071 words of length
at most 16, including padded representations, also agree with their
encoded integers. These scans remain finite evidence. The unrestricted
deduction rests on the algebraic invariant and closed certificate, not
extrapolation from the scans.

### 5. Actual-to-formal divisibility: injectivity, integrality, normality

Substitution alone gives only formal-to-actual divisibility, so the
converse must be checked separately. Under lexicographic x>y>z, direct
expansion gives

    LM(Q)=x^2, LM(R^2)=x^4*y^2, LM(D)=x^2*y*z.

Their integer exponent vectors have determinant 4 and are independent.
This is a statement about equality of integer exponent vectors, not
a Jacobian over F2; reducing 4 modulo 2 would invalidate the argument.
Thus distinct q^a*u^b*d^c yield distinct leading monomials. In a nonzero
finite linear combination, the largest of these leading monomials cannot
cancel with any summand having a lower leading monomial. This proves
S->T injective and in particular makes the image of A nonzero.
The fresh checker verifies the leading monomials directly.

The root polynomial identity is

    product_(a in {x,y,z,x+y+z})(X+a)=X^4+Q*X^2+R*X+D.

It needs no distinct-root or separability hypothesis. Substituting each
of x,y,z and squaring gives the monic equation

    X^8+Q^2*X^4+R^2*X^2+D^2=0

with coefficients in the embedded S. Thus x,y,z are integral over S,
and T=S[x,y,z] is integral over S. Explicitly, the monic equations
reduce T to the S-span of the 512 monomials with each exponent <8.
A finite module need not be free: the determinant trick still supplies
a monic equation for each element of T. The checker verifies all three
root identities by support multiplication; the general integrality
step is the stated algebraic argument.

S is a polynomial ring over a field, hence a UFD, hence integrally
closed in Frac(S). The last implication can also be checked directly:
a reduced fraction a/b satisfying a monic equation of degree d gives,
after multiplication by b^d, that b divides a^d; coprimality in a UFD
forces b to be a unit. The theorem's hypotheses are thus explicit.

If actual divisibility holds with quotient H in T, the previous identities
give H=P_j/A in Frac(T), and this fraction belongs to the embedded
Frac(S). Since T is integral over S, H is integral over S; since S
is integrally closed in Frac(S), H belongs to S. Hence A divides P_j.
The converse follows by substitution. This proves the exact equivalence
(15). It does not assume A stays irreducible in T or that every factor
of a substituted polynomial belongs to S. Extra splitting cannot add a
divisibility by the whole phi_13, because its quotient must descend as
just proved. No flatness assertion, specialized-variable division, or
extension-field argument is needed.

### 6. Exponents and the limited B4(b) consequence

Putting n=2j+3 gives n=(64*16^m+1)/5. It is integral because 16=1
modulo 5 and 64=-1 modulo 5, and odd because numerator and denominator
are odd. The first five values are 13,205,3277,52429,838861.

For odd n>1 the mixed coefficient at x^(n-1)*y in f_n is n mod 2=1;
none of the pure powers alters it. Thus f_n and phi_n are nonzero.
The homogeneous quotient has degree n-3, while phi_13 has degree 10,
so its nonzero cofactor has degree n-13. This is positive for m>=1
and zero for m=0. Lifting both factors' 0/1 coefficients to integers
gives the required coefficientwise congruence, with both factors
nonconstant for the asserted m>=1 consequence. An extension-field
factorization is never substituted for an F2 factorization. Absence of
the fixed divisor for other exponents says nothing about other factors.

The candidate's priority caveats remain necessary. Its contextual
Hernando--McGuire/Ferard claims were not used or independently verified
here. No novelty is certified by this review. The proof itself uses no
external automata theorem or announced fixed-factor result; its ring
facts have the checked hypotheses above.

## Adversarial issue/attack log

No blocking or unresolved R2 issue remains. These are attempted
objections and their dispositions, not repair requests.

| ID | Attempted failure mode | Resolution |
|---|---|---|
| R2-C01 | Localization loses q=0,d=0 components | Primitive prime A, A not dividing q*d, and explicit contraction. |
| R2-C02 | Negative b degrees invalidate Cartier sections | Unique integer parity residues, finite convolution, and checked lower bounds. |
| R2-C03 | Existential parity branching replaces simultaneous vanishing | Both images span the next state; universal vanishing is equivalent to the conjunction. |
| R2-C04 | Row-reduction collisions or missing edges fake closure | Fresh full-vector support construction matches all distinct states and all edges. |
| R2-C05 | Quotient classes or bit order create extra exponents | Every quotient output/edge checked; complete path language and LS-first value reconstructed. |
| R2-C06 | Leading zeros alter acceptance | General invariant fixes the same ell; exhaustive short-word evidence agrees. |
| R2-C07 | Actual divisibility does not descend | Injective embedding, integral extension, and normality force P_j/A into S. |
| R2-C08 | Characteristic 2 kills determinant 4 | The determinant concerns integer exponent vectors, which are the needed data. |
| R2-C09 | n=1,3,13 gives a spurious official solution | Proper theorem restriction; phi_3=1; self-divisibility at 13 makes no reducibility claim. |
| R2-C10 | Finite scans are promoted to a general classification | Scans are evidence; invariant plus closed graph gives the criterion for one whole divisor only. |

## Reproduction and checkpoint

From /Users/uqmkamga/Documents/ChatGPT/Website:

    .venv/bin/python -u problems/2024-B4/reviews/criterion-review-2-run.py

The harness launches only the new checker as a dedicated child, records
its PID before waiting, redirects incremental stdout/stderr checkpoints,
and enforces a 45-second timeout. On timeout it would kill only its
identified child. The completed run used Python 3.12.14, standard library
only, child PID 17043, return code 0, about 0.687 seconds including launch.
Child checkpoints completed in about 0.641 seconds. No timeout, failed
mathematical check, interruption, or native CAS operation occurred.
The harness reaped the child.

Exact command, parameters, timestamps, PID, exit status and stream hashes
are in criterion-review-2-run.json. Every reconstructed full vector space,
transition, output, leading/root identity support, finite scan parameter
and result, input hash, and checker hash is saved in
criterion-review-2-check.json. The final evidence manifest hashes the
artifacts. There are no random choices, remote computations, or unrecorded
search ranges.

The read-only PDF commands were:

    .venv/bin/python -c 'from pypdf import PdfReader; print(PdfReader(".cache/official/2024-paper_b.pdf").pages[1].extract_text())'
    /Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm -f 2 -l 2 -singlefile -scale-to 1800 -png .cache/official/2024-paper_b.pdf problems/2024-B4/reviews/criterion-review-2-official-page2

Dependency discovery found no PATH pdftotext. Initial fitz probes in
both local/bundled Python environments failed with ModuleNotFoundError;
available pypdf and bundled pdftoppm then succeeded. No installation
was needed. One initial report-file patch failed validation before
writing anything; the corrected write produced this report. These are
tooling failures, not mathematical computation failures.

This report checks the entire criterion argument and certificate,
not the full open reducibility question or literature priority. I have
not seen the other criterion review's findings. The coordinator must
reconcile that independent report and any repairs before promotion.
On the frozen version identified above, R2 recommends acceptance of
the stated fixed-divisor criterion, subject to that coordination step.

