# 2019 B4(b): deeper literature and setter-source investigation

2026-10-16 UTC (2026-10-17 in Brisbane). Research by
`owner_2019_structure3`; requested `gpt-6.1-sol`, `max`, with no independent
effective-setting readback. This note distinguishes published work,
source evidence and proposed applications. No exact published solution to
B4(b) was located; that negative search result is not a proof that none
exists. All mathematical claims newly made in the companion
`thirdpass-bounded-separation-v1.md` remain **candidate proof - unverified**.
No preliminary part (a) was investigated as a target.

## Direct searches for this exact problem

- The [official 2019 statement](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-paper-b_1.pdf)
  remains the authoritative definition. The official as-issued open label
  establishes historical status, not current universal absence of a solution.
- A direct contemporary primary account is Anthony Henderson and
  S. Ole Warnaar, [*The 2019 Simon Marais Mathematics Competition*](https://austms.org.au/wp-content/uploads/2025/02/Mar20-471.pdf),
  *Gazette of the Australian Mathematical Society* 47(1) (2020), 39–41
  (PDF pages 40–42). It explicitly identifies B4(b) as the unsolved
  asymptotic binary-string enumeration in that competition. It does not
  give a B4 proposer or a new bound. Full issue cached, relevant pages read.
- The exact target has an [unanswered public reference request](https://math.stackexchange.com/questions/3706460/reference-request-the-number-of-binary-string-with-some-special-condition-ope)
  posted by `ililiil` on 2020-06-05. The directly authored comments by
  `joriki` report a Java computation through `b_30=29280686`, agreeing
  with our overlapping saved counts. The page's current unanswered
  listing reports zero answers. This is a primary discussion record and
  finite evidence, not a peer-reviewed solution or a theorem imported
  here. A comment's speculative limit is not used.
- Searches used exact problem/year/title phrases, the literal insertion
  wording, and distinctive consecutive terms
  `1417222 2596086 4756834` and `1,2,3,5,9,16,29,52,94`.
  The retrieved exact-problem hits were the official sources, the
  contemporary report, that discussion and mirrors. No source giving an
  exact growth constant or later rigorous improvement was located.
  No conclusion that the sequence is currently absent from OEIS is made;
  the discussion's OEIS remark is dated 2020.

## Committee and possible-setter leads: attribution limits

The 2020 Gazette report above directly credits **Norman Do** as chair of
the Problem Committee for the preceding three competitions and says
**Christopher Tuffley** takes over in 2020. This establishes committee
leadership for 2019, not authorship of B4. Norman Do's own 2019
[problem-donation appeal](https://archive.austms.org.au/Publ/Gazette/2019/May19/46%282%29Web.pdf)
also identifies him as the then chair, and makes clear that problems can
be donated from the wider mathematical community. No B4 donor is named
in the checked primary sources.

The [current official committee roster](https://www.simonmarais.org/aboutus.html)
is explicitly headed **2026**. Its members cannot automatically be treated
as the 2019 roster. A [first-person 2017 committee statement by Peter J.
McNamara](https://petermc.net/blog/2017/10/) verifies his participation in
2017 only; no 2019 B4 attribution follows. His mathematics site and
[author-posted publication comments](https://petermc.net/maths/papers/comments.pdf)
identify **Peter J. McNamara**, the representation theorist. Searches
also return **Peter R. W. McNamara**, a different combinatorialist; their
publications must not be conflated.

Research-profile checks provide leads, not setter evidence:

- Norman Do's [Monash research overview and selected publications](https://www.monash.edu/science/schools/school-of-mathematics/Our-People/staff/norman-do)
  concern geometry, topology and enumerative combinatorics, especially
  topological recursion, maps and Hurwitz numbers. This makes generating
  functions a sensible methodological lead; it supplies no theorem about
  our binary-string language and does not identify him as its setter.
- Peter J. McNamara's author publication list is centered on representation
  theory, KLR algebras and canonical bases. No exact-language match or
  direct B4 donor statement was found in the checked author material.
- Tuffley's coauthored tandem-repeat parsing work was located through
  primary institutional thesis metadata; it studies sequence parsing,
  not the present insertion enumeration. This is a possible thematic
  lead only. No theorem from it is used and no setter inference is made.

The next responsible attribution step would be an archived 2019 donor
credit or a direct author statement. No person was contacted: sending
messages was not authorized, and no contact is necessary for this
read-only research phase.

## Published methods that materially inform the current work

1. **Mehryar Mohri, *Edit-Distance of Weighted Automata: General Definitions
   and Algorithms***, *International Journal of Foundations of Computer
   Science* 14 (2003), 957–982. [Author-posted full text](https://cs.nyu.edu/~mohri/pub/edit.pdf).
   Relevant reading: §4.3, PDF pages 11–15. Its synchronization algorithm
   stores finite residual strings at states; bounded path delay makes
   the state set finite. It also describes compact suffix-tree storage.
   **Application:** the pending-queue construction in our new candidate is
   a problem-specific use of established residual-buffer synchronization,
   followed by ordinary subset determinization. The source's theorem
   assumes bounded delays; the unrestricted B4 relation has not been
   shown to have one. We impose a cap and prove a converging hierarchy,
   rather than claiming the theorem synchronizes the full relation.
   **Next idea:** intern and precompute residual queue transitions before
   any higher cap, or use suffix links to avoid repeated string copying.
   This addresses state-construction cost without enlarging mathematical
   scope. Full PDF cached; no redistribution licence verified.

2. **Christiane Frougny and Jacques Sakarovitch, *Rational relations with
   bounded delay***, STACS 1991, LNCS 480, 50–63,
   [publisher record](https://link.springer.com/chapter/10.1007/BFb0020787),
   DOI `10.1007/BFb0020787`; and *Synchronized rational relations of finite
   and infinite words*, *Theoretical Computer Science* 108 (1993), 45–82,
   [publisher record](https://www.sciencedirect.com/science/article/pii/030439759390230Q),
   DOI `10.1016/0304-3975(93)90230-Q`.
   Publisher abstracts and Mohri's attribution were checked. Full texts
   were not obtained here; no theorem is imported beyond the more directly
   checked finite construction. **Use:** clear prior-art attribution for
   bounded-delay synchronization, and a warning to distinguish a general
   rational relation from a synchronized one.

3. **Marie-Pierre Béal and Olivier Carton, *Asynchronous sliding block
   maps***, *RAIRO—Theoretical Informatics and Applications* 34(2) (2000),
   139–156. [Primary archive full text](https://www.numdam.org/item/ITA_2000__34_2_139_0.pdf).
   Relevant reading: introduction and synchronization hypotheses. It
   treats state splitting under constant transmission-rate assumptions,
   with additional care for non-strongly-connected machines. **Use:**
   warns against assuming a small finite presentation or locality is
   preserved by synchronization. Our all-row vector certificate needs no
   strong-connectivity assumption. Its hypotheses are not established for
   the unrestricted two-tape relation. Full PDF cached; no redistribution
   licence verified.

4. **M.-P. Béal, M. Crochemore, F. Mignosi, A. Restivo and M. Sciortino,
   *Computing forbidden words of regular languages***,
   *Fundamenta Informaticae* 56(1–2) (2003), 121–135.
   [Institutional publication record](https://kclpure.kcl.ac.uk/portal/en/publications/computing-forbidden-words-of-regular-languages),
   [author-posted text location](https://igm.univ-mlv.fr/~beal/Recherche/Publications/fialgo.pdf).
   The primary indexed introduction and institutional metadata were read;
   the full-file retrieval failed TLS certificate verification, so no
   full-text reading is claimed. Its known quadratic construction of
   minimal forbidden words of a factorial regular language explains the
   two-copy DFA used in our computation. This is an existing general
   method, not a new algorithm claimed here. Earlier context:
   Crochemore–Mignosi–Restivo, [*Automata and forbidden words*](https://www.sciencedirect.com/science/article/pii/S0020019098001045),
   *Information Processing Letters* 67 (1998), 111–117; publisher abstract
   checked, no full text retrieved.

5. **Martin Huschenbett, Dietrich Kuske and Georg Zetzsche,
   *The monoid of queue actions***, 2014;
   [author-posted conference version](https://eiche.theoinf.tu-ilmenau.de/kuske/Publications/HusKZ14.pdf),
   [full-version record](https://arxiv.org/abs/1404.5479).
   Relevant reading: §§1, 4–5 and 8. It gives normal forms for FIFO queue
   **transformations**, involving read/write projections and overlap
   width; it also places products of free monoids inside the queue monoid.
   **New direction suggested:** translate the two coupled residual queues
   into queue-action normal forms and investigate overlap-width
   recursions. This might handle unbounded separation more efficiently
   than literal words. **Gap:** equality of these queue transformations
   is not yet proved to coincide with our context equality; its finite
   rewriting presentation cannot simply be transferred to our generators.
   The accepted no-finite-presentation result remains untouched. Full
   conference PDF cached; no redistribution licence verified.

6. **Jérôme Buzzi, *Subshifts of quasi-finite type***,
   [author arXiv record](https://arxiv.org/abs/math/0305164),
   *Inventiones Mathematicae* 159 (2005), 369–406.
   Relevant reading: introduction, constraint-entropy definitions and
   Lemmas 10–11 in the cached version. It distinguishes the growth of
   minimal forbidden words, follower sets and other constraint data.
   **New direction suggested:** attempt a rigorous entropy estimate for
   high-separation minimal factors; that is exactly the missing tail
   information in the present renewal root. **Gap:** small observed
   obstruction counts or an apparent slow finite automaton do not prove
   the strict entropy hypothesis needed for quasi-finite-type results.
   No maximum-entropy, meromorphy or exponential tail conclusion is
   imported. Full PDF cached; no redistribution licence verified.

7. **C. Aiswarya, Amaldev Manuel and Saina Sunny, *Edit Distance of Finite
   State Transducers***, ICALP 2024, LIPIcs 297, 125:1–125:20,
   [official full text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol297-icalp2024/LIPIcs.ICALP.2024.125/LIPIcs.ICALP.2024.125.pdf),
   DOI `10.4230/LIPIcs.ICALP.2024.125`.
   Relevant reading: introduction and the discussion of bounded-delay
   rational relations. It concerns decidability/computation of distances
   between functional transducers and relation diameters; it does not
   enumerate our distinct contexts. **Use:** modern terminology and an
   algorithmic lead for certifying special bounded-delay subsystems.
   This is supporting context, not an exact-growth theorem. The PDF
   explicitly states CC-BY 4.0; it still remains ignored cache material.

8. **L. J. Guibas and A. M. Odlyzko, *String overlaps, pattern matching,
   and nontransitive games***, *Journal of Combinatorial Theory A* 30
   (1981), 183–208,
   [publisher record](https://doi.org/10.1016/0097-3165%2881%2990005-4).
   Publisher abstract and author bibliography checked; the full article
   was not downloaded. The standard correlation/avoidance framework is
   prior context for renewal denominators once overlap is controlled.
   No claim is made that the accepted elementary no-overlap proof or
   generating-function manipulation is a novel general enumeration tool.

## Failed approaches preserved and next structural question

A small residual-state probe checked the tempting hypothesis that the two
queues are always cyclic rotations of the same word. It is false already
at separation four: reachable queues include `0011` and `0101`, which
are not conjugate. They do always have equal symbol multiplicities,
by the transition table, but that invariant alone does not encode their
future behavior. Thus cyclic-word normal forms cannot be substituted
without further information. This failure is saved in
`thirdpass-literature-probes.json`.

The important unresolved question suggested by the papers is whether
queue-action overlap structure yields a provable count of high-separation
minimal factors, or a small recursively defined state family. Finite delay
is deliberately imposed in the current candidate; its increasing-state
trend is not evidence that the unrestricted relation synchronizes. No
bigger brute-force word enumeration was attempted during this pass.

## Retrieval and operational record

Six full PDFs, their local paths, original URLs, SHA-256 hashes, byte
counts and UTC file retrieval timestamps are recorded in
`thirdpass-literature-sources.json`. They live only in ignored
`.cache/2019-B4-thirdpass/`, along with derived extraction text. No full
paper was added to a tracked directory, no purchase or subscription was
made, and no access restriction was bypassed. The exact public curl
command template was

    curl -L --fail --silent --show-error --max-time 30 URL -o CACHE_PATH

All six successful downloads used certificate verification. The failed
`fialgo.pdf` retrievals at hosts `igm.univ-mlv.fr` and
`www-igm.univ-mlv.fr` returned curl status 60 (TLS certificate name
mismatch). A proposed current-host URL `igm.univ-eiffel.fr` did not resolve
(status 6). No certificate bypass was attempted; its source is recorded
at abstract/indexed-introduction level only. Primary HTML source contents
were read through the browser tool; no local raw-source hash is claimed
for uncached web pages. Search dates here are verification dates, not
publisher crawl dates.
