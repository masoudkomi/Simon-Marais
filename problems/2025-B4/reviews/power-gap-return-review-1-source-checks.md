# PG1–PG4 R1: source and provenance checks

Checked 2026-10-17 UTC. No peer new PG report or findings read before this
whole initial packet was frozen. No source theorem is inferred from an
abstract. The publication theorem interfaces below were checked in full;
their entire external proofs were not independently reconstructed.

## Official source

[Official 2025 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2025_paper_b.pdf),
PDF page 2, B4(b), read directly through the web PDF extraction. The variables
x,y,n,q are integers, n,q>=2, and n is the degree. Hence the geometric quotient
with exponent m uses m=n+1. The packet and both literature translations use
this convention correctly. Part (a) was not researched or reproduced.

The frozen `statement.md` was also read, including its explicit indexing
warning. Its constructor-listed hash is checked by this review's freeze.

## Accepted elementary dependencies

Read the complete `proof.md` SHA-256
`c422139567ee3e2f4eafd852c9a3f5fac73cb6c8e0bfdf9e2c9c5311a9348b0d`,
`proofs/reviewed-partial-v1.1.md`, and `reviews/acceptance.md`. The acceptance
covers C1–C4 only, and not the conjectural final classification. Used here:
C1 nontrivial magnitude, C2 signed odd-prime LTE, C4 exact block gcd and
coprime-factor valuation rule. Their concrete used hypotheses and algebra
are reconstructed in the whole report. C3/preliminary material is not used
to replace the new arguments.

## Bennett–Levin, signed published input

M. A. Bennett and A. Levin, *The Nagell–Ljunggren equation via Runge's method*,
Monatsh. Math. 177 (2015), 15–31, DOI 10.1007/s00605-015-0748-1.
[Author-posted published primary PDF](https://personal.math.ubc.ca/~bennett/BeLe-Mona-2015.pdf).

Fresh web opens returned the complete primary PDF, including its title,
Equation (1) and full relevant statements on printed pages 15–17. The source
domain has |x|,|y|>1, n>2 and integer q>=2. Its n is project m. Proposition 1
is qualified by the four known examples and yields the least-prime-factor
restriction used by PG4. Theorem 1 bounds Omega(n) by 3. The surrounding
text expressly distinguishes positive-base improvements from this signed
setting. It also explains that its elementary argument's special case
(n,q)=(p^5,5), p|(x-1), is eliminated by reference [10]. PG4 imports the
complete theorem including that resolution. This audit does not claim to
have reconstructed the entire external proof or [10].

No private access, subscription or bypass was used. The existing local
primary PDF is among the constructor-listed records, SHA-256
`ac38ad33a480068a707054a0a9acc7c937f70af84171cb7465b7d0fdd99b2b99`.
The freeze validates those local bytes. The fresh web viewer does not provide
a binary retrieval hash, so I do not claim an independently hashed new binary
or identify fresh-view bytes with the cached binary solely by a new hash.

## Bugeaud–Mihailescu, positive-base overlap

Y. Bugeaud and P. Mihailescu, *On the Nagell–Ljunggren equation*, Math. Scand.
101 (2007), 177–183, DOI 10.7146/math.scand.a-15038.
[Journal page](https://journals.msp.org/mscand/article/view/659),
[primary PDF URL](https://journals.msp.org/mscand/article/download/659/658).

The fresh web PDF attempt returned an Internal Error. I read the complete
already cached seven-page primary paper and independently extracted its
entire text directly from the cached PDF with bundled pypdf. Equation (1)
restricts x,y>1. Theorem 1 on printed p.178 has a known-example qualification
and, among its complete conclusions, supplies the divisible-term-count
assertion cited by the candidate. The only relevant known odd-prime example
also has m=q. This verifies the overlap attribution without extending a
positive-domain theorem to negative x. It is not a PG1–PG4 premise.

The primary PDF SHA-256 is
`105ea336a19143e6c9189843686185c4da6cf5d68ffdcc565664d4829fd8567c`;
the existing extracted text has SHA-256
`64ed9583e8ea5e8b2bde3a2c3aad05b8be037496b583c19d4ada18b5f4a1e96a`.
Both are validated as constructor inputs. No new full paper was tracked or
redistributed.

## Exact tools and commands

Read-only shell commands used `cat`, `nl -ba`, and `rg --files` on the named
candidate/dependencies and prior own freeze metadata. Web calls opened the
three primary URLs above and the relevant already returned PDF references.
The complete new candidate, source note, worklog and freeze were read.

The first extraction attempt

    pdftotext -layout .cache/literature/2025/bugeaud-mihailescu-2007.pdf -

returned exit 127 because pdftotext is not installed. A system-python pypdf
attempt returned ModuleNotFoundError. The bundled workspace dependency path
was then obtained through `load_workspace_dependencies`, and this succeeded:

    /Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -c 'from pypdf import PdfReader; r=PdfReader(".cache/literature/2025/bugeaud-mihailescu-2007.pdf"); print("\n\n".join("PDF page "+str(i+1)+"\n"+p.extract_text() for i,p in enumerate(r.pages)))'

This is source extraction, not mathematical computation. It installed nothing,
wrote no new paper and did not require escalation. The other Python command
is the review's own one-time administrative freeze script. No arithmetic
search, external separately billed API, CAS, author-code rerun or enumerator
was used. No processes required termination.

The account-wide usage tool returned 25% total weekly used in the 10080-minute
window, reset 1792745187. The 90%-total cutoff and integration reserve remain
in force. No Git commands, shared-file edits or subagent launches occurred.
