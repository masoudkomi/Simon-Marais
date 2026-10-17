# Independent source and dependency checks

Checked 2026-10-17 UTC by `review_2017_coarsening_r1`, before reading any
peer divisor review. These are exact hypothesis and attribution checks,
not an assertion that every page of every cited paper has been re-proved.
No new source paper was downloaded or redistributed. Cached source PDFs
remain ignored; local byte hashes are in the review manifest. Web-viewed
versioned PDFs have no independently saved local-byte hash in this audit.

## Official statement

[Official 2024 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf),
page2: checked the odd positive domain, the coefficientwise meaning of
congruence, and the condition that both factors are nonconstant modulo2.
The cached source hash is
`1401f21218ad4c387c4d537ed8fd7de119b376cba52957ef788c772dc5ab4ddc`.
The local mathematical normalization matches. Only part(b) was audited.

## Actual irreducibility premise

[Gary M. McGuire, Caltech thesis (1995)](https://thesis.caltech.edu/4053/01/McGuire_gm_1995.pdf),
printed pages15--16 and19--20, was inspected as full-page cached images.
The definitions identify the homogeneous quotient with phi_t here and its
affine part with phi_t(X,Y,1). Theorem2.1' gives absolute irreducibility
for t>3, t congruent3 modulo4. Both7 and11 satisfy it. The complete
short proof on pages19--20 was read; earlier local geometry remains
published background. The candidate separately checks that rehomogenizing
has no factor at infinity. Attribution to Janwa--McGuire--Wilson is
retained. This source supports a property of each whole fixed divisor,
not just existence of an absolute component. Cached thesis SHA256:
`d8e8e62d873c5ec69e2fd40473a9aee257bb8d4994cb5ffc1a42cb70f8bcbd24`.

## Generic effective zero sets

[Harm Derksen, arXiv:math/0510583v1](https://arxiv.org/pdf/math/0510583v1):
I read the recurrence definition, Theorems1.8--1.10 on printed pages3--4,
Theorem4.14 on page20, and the effective-comparison argument on page25.
Theorem1.10 requires a finitely generated characteristic-p field and an
explicit recurrence. Theorem4.14 gives automaticity for recurrences over
any characteristic-p field. The effectiveness argument reduces general
recurrences before using its simple/nondegenerate estimates. The packet's
explicit fraction field and monic recurrence meet the general hypotheses.
No theorem that all coefficient values over an infinite field form a
finite-valued automatic sequence is invoked. Full proof not re-audited.

[Boris Adamczewski--Jason P. Bell, arXiv:1205.4091v1](https://arxiv.org/pdf/1205.4091v1):
I read the definitions and Theorems1.4--1.5 with discussion on printed
pages5--7. Their object is the zero coefficient set of a formal series
algebraic over a rational function field in positive characteristic.
The effective statement produces an automaton and permits emptiness,
finiteness and periodicity decisions. This accurately supplies broader
published context, and is not needed for the explicit fifteen-state
certificate. The packet distinguishes zero-set automaticity from ordinary
coefficient-value automaticity over an infinite coefficient field.

## Other gcd papers: scope only, not premises

[Delgado--Janwa, arXiv:1207.5528v1](https://arxiv.org/pdf/1207.5528v1):
I read the decomposition statements, all of Lemma1 and its short proof
on printed pages4--5. It concerns designated Gold/Kasami-Welch/Welch
families and includes coprimality for distinct Welch indices. It does not
state C7 or C11 against arbitrary odd n. Its family restrictions are not
silently removed in this packet.

[Delgado--Janwa, arXiv:1602.02576v1](https://arxiv.org/pdf/1602.02576v1):
I checked the setup, Theorem10 and its surrounding proof and application
on printed pages8--10. The designated fixed exponent is of the form
2^k+1, with an exception for another such exponent sharing a parameter
divisor. Seven and eleven are outside that designated fixed family.
Accordingly the packet cites its scope rather than using it to prove
C7/C11. No claim of independent validation of that paper's entire proof
or its later applications is required for the current argument.

[Anbar--Kalayci--Yurdakul, WCC2022 primary-hosted paper](https://www.wcc2022.uni-rostock.de/storages/uni-rostock/Tagungen/WCC2022/Papers/WCC_2022_paper_64.pdf):
I read its abstract, definitions and Lemma1 on printed pages1--3. Its
geometric criterion distinguishes an absolute component over the base
field from irreducibility of the whole polynomial. The checked passages
do not supply either exact singleton set. The packet uses no theorem
from its later proofs.

[Florian Caullery, author-uploaded public paper text](https://www.researchgate.net/publication/280793382_A_divisibility_criterion_for_exceptional_APN_functions),
DOI10.1090/conm/632/12619: I read the abstract, context, Theorem3.1,
and nearby lemma statements. The main hypothesis is an exceptional APN
polynomial of degree4e, e odd, and the conclusions constrain possible
factor shapes. That is the scope accurately stated in the candidate,
not an unrestricted fixed phi7/phi11 divisibility theorem. No deduction
from this source is used. I did not re-audit its full proof.

The constructor reports prior ordinary-route limits for Férard's full
2014/2017 texts and the original Janwa--Wilson1993 chapter. I did not
repeatedly retry those routes in this independent audit. Those unread
texts are not premises of C7/C11. Neither their absence nor the bounded
search record supports a priority claim; none is made. The reported
anti-bot and mirror failures were not bypassed.

## Accepted local tools and finite certificate provenance

The accepted local `zero-automaton-criterion-reviewed-v1.1.md` has SHA256
`362f2541b2bb1ab1e22ba768b41d55e7282f08631b0ad39522682244d213f226`.
I read its generating identity, section invariant and complete integral
normality bridge. Each is also reconstructed in the new divisor candidate
and in my whole report. The new proof does not depend on the earlier
phi13 graph, earlier bounded small-divisor scans, or the unreviewed
structural T1--T4 packet. No preliminary part(a) result was reproduced.

The new static phi11 certificate has SHA256
`7250fe21f0953d43a995b3773e39e7c1b943306bb163699843fdfd6de77c4f0e`.
It was copied byte for byte into the assigned review prefix. I fixed K
and N0 independently from the rational function, rebuilt polynomial
sections using exponent supports, and checked all complete state and
transition spaces. The constructor implementation was read only after
my successful run. Its code was neither imported nor executed. Both
implementations and all frozen constructor outputs remain untouched.

No fee, subscription, account contact, access bypass or separately billed
API was used. Authoritative account-wide weekly usage was20% during the
audit, reset1792745187; the stop ceiling is90% total used. Requested
model/reasoning settings are recorded separately from unavailable
effective-setting readback.
