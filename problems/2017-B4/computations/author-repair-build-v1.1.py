#!/usr/bin/env python3
"""Build full v1.1 author revisions and exact diffs without touching frozen v1.

Standard library only. No mathematics is recomputed and no child job is run.
Every destination is in the assigned author-repair-* namespace. Existing
destinations are accepted only if byte-identical. Frozen input hashes are
checked before and after generation. This is an author repair, not a review.
"""
from datetime import datetime, timezone
import difflib
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
YEAR = ROOT / "problems/2017-B4"
NOTES = YEAR / "notes"
FROZEN = {
    "secondpass-macmahon-candidate-v1.md": "83f254ec69a31b5bf57dddd241bd0e29277300b4f1ba78dbf3c2c02191913ffe",
    "secondpass-boundary-fiber-candidate-v1.md": "984ecfd11306304dd68310b0b20148577a7e8d43da6761a9bd570f95024cacbc",
    "secondpass-periodic-grid-candidate-v1.md": "6e2a25e0bd94d230892c8c8eb31d931c4a09190826f1f210a97fcb207e852bd7",
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_new(path, text):
    data = text.encode("utf-8")
    if path.exists():
        if path.read_bytes() != data:
            raise RuntimeError(f"refusing to replace nonidentical destination: {path}")
    else:
        with path.open("xb") as out:
            out.write(data)


def replace_once(text, old, new):
    if text.count(old) != 1:
        raise RuntimeError(f"expected exactly one replacement marker: {old[:100]!r}")
    return text.replace(old, new, 1)


def common_revision(text):
    text = replace_once(
        text, "**candidate proof - unverified**\n\n",
        "**candidate proof - unverified**\n\n"
        "Full revised version **v1.1**, 2026-10-17 (Australia/Brisbane). "
        "The revision author is `/root/owner_2017`, the original constructor of "
        "these second-pass packets. Both frozen independent initial reports "
        "were read for this author repair. All frozen v1 notes, manifests and "
        "review reports are preserved. The revised inferences require both "
        "targeted re-audits and coordinator acceptance before any promotion.\n\n")
    return replace_once(text, "Written 2026-10-16.", "Original draft written 2026-10-16.")


preserved_paths = sorted(
    [p for p in NOTES.glob("secondpass-*") if p.is_file()]
    + [YEAR / "reviews/secondpass-review-1.md",
       YEAR / "reviews/secondpass-review-2-initial.md"]
    + [p for p in (YEAR / "computations").glob("secondpass-*") if p.is_file()]
)
preserved_before = {str(p.relative_to(ROOT)): sha(p) for p in preserved_paths}
for name, expected in FROZEN.items():
    assert sha(NOTES / name) == expected, (name, "frozen source differs")

originals = {name: (NOTES / name).read_text() for name in FROZEN}
revised = {}

# M1 and M3 mathematics are retained. M2 gets an explicit full-tree/parity model.
mac = common_revision(originals["secondpass-macmahon-candidate-v1.md"])
mac = replace_once(mac, "# Unequal three-bundle entropy: candidate v1\n",
                   "# Unequal three-bundle entropy: candidate v1.1\n")
mac = replace_once(mac,
    "An ordered rooted ternary tree partitions n singleton strands.",
    "An ordered rooted **full** ternary tree (every internal node has exactly "
    "three children) has n singleton strand leaves. Such a tree exists only "
    "when n is odd; for even n this singleton-leaf family is empty. This is "
    "an upper-counting construction model, not an all-n lower construction. "
    "The fixed bounded-size base-block extension is considered separately below.")
mac = replace_once(mac,
    "Two fresh adversarial reviewers must audit this packet independently before any promotion; one must reconstruct it. Check especially the direction of Jensen, the integral normalization, endpoint treatment in the calculus maximum, the scope of the tree model, and the induction's all-n hypothesis. Finite exact tests in `secondpass-macmahon-bound-output.txt` are evidence only. They are not the proof of (M1).",
    "Both independent initial v1 reports are frozen. This v1.1 adds the explicit "
    "full-ternary/odd-leaf convention in M2; the M1 and M3 mathematical arguments "
    "are unchanged. Both reviewers must perform the requested targeted re-audit "
    "of the revised scope before coordinator acceptance. Finite exact tests in "
    "`secondpass-macmahon-bound-output.txt` remain evidence only, not the proof "
    "of M1. This author revision does not promote any result.")
for start_marker, end_marker in (("## Candidate M1:", "## Candidate M2:"),
                                  ("## Candidate M3:", "## Independent-review obligations")):
    old_block = originals["secondpass-macmahon-candidate-v1.md"].split(start_marker, 1)[1].split(end_marker, 1)[0]
    new_block = mac.split(start_marker, 1)[1].split(end_marker, 1)[0]
    assert new_block == old_block, (start_marker, "unchanged mathematics was altered")
revised["macmahon"] = mac

# F1/F2 source precision; explicit empty slots, facial walks and Jordan boundary;
# F3 proper transverse two-port hypotheses and the empty-patch unit.
fib = common_revision(originals["secondpass-boundary-fiber-candidate-v1.md"])
fib = replace_once(fib, "# Fixed-boundary patches as completion fibers: candidate v1\n",
                   "# Fixed-boundary patches as completion fibers: candidate v1.1\n")
fib = replace_once(fib,
    "A boundary word w is a cyclic sequence in which each of m distinct labels occurs twice. On the boundary of an oriented closed disk D, mark 2m distinct points with those labels in that cyclic order. A minimal chord arrangement consists of m proper simple arcs joining like-labelled endpoints, with only transverse crossings, no three arcs meeting at one point, and each pair crossing at most once. F(w) counts such arrangements up to orientation-preserving homeomorphisms fixing the labelled boundary data. Equivalently for counting, one may use all local crossing orders along the labelled arcs; no rotational/reflection quotient of the objects is taken.",
    "For m≥1, a boundary word w is a cyclic sequence in which each of m distinct "
    "labels occurs twice. On the boundary of an oriented closed disk D, mark "
    "2m distinct points with those labels in that cyclic order. A minimal chord "
    "arrangement consists of m proper simple arcs joining like-labelled endpoints. "
    "Each arc meets the boundary only at its two distinct ports, transversely; "
    "there are no boundary segments or tangencies. Interior intersections are "
    "transverse, no three arcs meet at one point, and each pair crosses at most "
    "once. F(w) counts such arrangements up to orientation-preserving homeomorphisms "
    "fixing the labelled boundary data. Equivalently for counting, one may use "
    "all local crossing orders along the labelled arcs; no rotational/reflection "
    "quotient of the objects is taken. Define **F(empty)=1** for the empty patch. "
    "The completion-fiber assertion below is stated for m≥1; the empty case is "
    "handled by this unit convention and introduces no official C(0) domain.")
fib = replace_once(fib,
    "We use the established correspondence between C(m), simple marked pseudoline arrangements, commutation classes and complete triple-sign patterns. A complete sign pattern assigns a bit to each a<b<c, with the four bits on each increasing four-set changing at most once in their packet order. This correspondence is attributed mathematical context, not newly established here; see Felsner–Valtr, Section 1, [author PDF](https://page.math.tu-berlin.de/~felsner/Paper/new-pla.pdf), and the first-pass references. A bit can be read from the order of ab and bc in a left-to-right wiring diagram.",
    "We use the established correspondence between C(m), simple marked pseudoline "
    "arrangements, commutation classes and complete triple-sign patterns. A complete "
    "pattern assigns a bit to each a<b<c; on each increasing four-set its packet "
    "has at most one sign change. The precise primary theorem is Felsner–Weil, "
    "*Sweeps, Arrangements and Signotopes*, **Theorem 7**, printed p. 15: "
    "the four-set monotonicity condition characterizes triangle-sign functions "
    "of simple marked arrangements. **Theorem 8**, on that page, gives the "
    "equivalent compatibility criterion for their local permutations; the proof "
    "of Theorem 7 is on printed p. 19. See the [author manuscript]"
    "(https://page.math.tu-berlin.de/~felsner/Paper/sas-dam-rev.pdf). "
    "Identify its two signs consistently with our bit values. Packet reversal "
    "or complementing the sign convention preserves the one-change predicate. "
    "A triple fixes all comparisons between its pair crossings on common strands. "
    "Felsner–Valtr, Section 1, [author PDF]"
    "(https://page.math.tu-berlin.de/~felsner/Paper/new-pla.pdf), supplies the "
    "marked-arrangement/local-sequence/tiling dictionary. These are attributed "
    "ingredients. The inspected Felsner–Weil PDF and page-image fingerprints "
    "are recorded in `author-repair-sources-v1.1.json`; full source files remain "
    "only in ignored cache. A bit may be read from the order of ab and bc in "
    "a left-to-right wiring diagram.")
start = fib.index("Take a complete pattern σ on the right side and a wiring realization A.")
end = fib.index("\n## Candidate F2:", start)
fib = fib[:start] + r"""Take a complete pattern σ on the right side and a piecewise-linear wiring realization A. On a strand i, compare any outside crossing ij (meaning ij not in X(w)) with any other crossing ik. The triple ijk is not in T(w), and its fixed sign determines their relative order on the common strand. That order agrees with A0. Consequently the outside crossings have exactly the A0 order, and if inside crossings occur, they form the same contiguous block between the same outside prefix and suffix.

An **empty** inside block needs a construction choice, not an extra sign constraint. In A0 record the gap between its exterior prefix and suffix. The same gap exists in A's identical exterior local sequence; choose two distinct nearby points in that edge and remove the crossing-free segment between them. If all crossings on a strand are inside, put its two cuts on its unbounded tails. In every case retain both cut endpoints as distinct labelled degree-one port vertices.

Remove one inside segment per strand. Add a sufficiently large outer circle, with its strand endpoints in the prescribed marked cyclic order. Every retained prefix and suffix reaches that circle along its own strand, so this finite outside graph is connected, even when the removed crossing network is disconnected or empty. Its isomorphism to the corresponding graph of A0 preserves exterior crossing labels, their order on every strand, both port labels per strand, rotations at crossings, and the labelled outer circle with its outer face. The crossing rotations are fixed by the oriented wiring convention; degree-one ports have no further rotational choice.

For completeness, the connected plane-embedding fact used here can be seen by replacing every vertex by a small oriented disk and every edge by a ribbon attached in its specified cyclic order. The rotation system specifies this regular neighborhood; filling its complementary disks specifies the spherical embedding, and designating the outer face specifies the plane embedding. This allows bridges and degree-one vertices. Agreement of the abstract crossing graph alone would not supply these data.

In A0's retained graph all ports are incident to the same bounded face U0, the one containing the former disk interior. Its facial boundary **walk** lists the labelled port corners in cyclic order w. The walk may repeat bridge edges or cut vertices; a degree-one port has one incident face corner. The preserved rotation system transfers this whole face and port-corner list to one bounded face U of A's retained graph.

Every removed inside arc has endpoint germs in U and cannot cross a retained edge: any pair crossing is classified inside or outside simultaneously on both participating strands. Its open arc is therefore contained in U. Every connected component of the removed crossing network has ports, because it is a union of these proper cut-strand arcs; there is no floating component in another face.

The unthickened facial walk need not itself be a Jordan curve. Choose a sufficiently thin **closed regular neighborhood** of the connected outside graph. Away from small port collars it is disjoint from all removed arcs; at each port trim only a short, crossing-free initial piece of the removed arc. Finiteness and piecewise-linearity allow all these collars and thicknesses to be chosen simultaneously. The closure of the complementary component corresponding to the bounded face U is now a closed disk with a Jordan boundary. It has one distinct transverse boundary port for each trimmed endpoint, in the same cyclic corner order w. All trimmed removed arcs and their crossings remain in that disk. This construction also works for an empty inside slot, for exterior bridges, and for several disconnected interior components.

An orientation-preserving disk homeomorphism sends this disk and its ordered labelled ports to D with the prescribed boundary positions. The trimmed arcs give a minimal patch with the required crossing orders. Gluing it to A0's fixed exterior reproduces every local sequence of A, hence the chosen complete sign pattern σ. This is the proposed surjectivity argument; together with the forward injection it gives (F1). Both reviewers must re-audit this explicit replacement of the v1 face/thickening paragraph.
""" + fib[end:]
fib = replace_once(fib,
    "Conditional on (F1) and the established complete sign-pattern correspondence, F(w) is an exact finite constraint count:",
    "Conditional on (F1) and Felsner–Weil Theorems 7–8 under the marked, fixed-order "
    "conventions just stated, F(w) is an exact finite constraint count:")
fib = replace_once(fib,
    "Suppose one fixed marked complete arrangement on n labelled strands contains disjoint closed disks P1,...,Pr. Their boundaries avoid crossings, and each disk meets any strand in either one connected arc or not at all. Let wj be the labelled boundary word in Pj. Replacing each local patch independently by a minimal realization with that same boundary word gives",
    "Suppose one fixed simple marked complete arrangement on n labelled strands "
    "contains pairwise disjoint closed disks P1,...,Pr. A disk boundary contains "
    "no arrangement crossing. Each strand either misses the disk or meets it "
    "in exactly one **proper simple arc with two distinct transverse boundary "
    "ports**; exclude tangencies and boundary segments. Let wj be the full "
    "labelled paired boundary word in Pj. A disk meeting no strands has "
    "wj=empty and factor F(empty)=1. Replacing each local patch independently "
    "by a minimal realization with that same paired boundary word gives")
fib = replace_once(fib,
    "Two fresh independent adversarial audits, including one full reconstruction, are required before any promotion of F1–F3. A reviewer of this packet must see neither the other initial review nor any author-created review verdict.",
    "Both initial v1 audits are frozen and were completed independently. The "
    "new citation, empty-slot construction, connected exterior/regular-neighborhood "
    "argument, and proper-port/empty-patch hypotheses in v1.1 require targeted "
    "re-audit by both reviewers. This author revision is not an independent "
    "review or a promotion; coordinator acceptance remains required.")
revised["boundary-fiber"] = fib

# G1: use nonnegative superadditivity without unresolved remainder grids.
# G2: every omitted multiple crossing gets one fixed disjoint local resolution.
grid = common_revision(originals["secondpass-periodic-grid-candidate-v1.md"])
grid = replace_once(grid,
    "# A fixed-direction patch entropy and a bounded construction certificate\n",
    "# A fixed-direction patch entropy and a bounded construction certificate — candidate v1.1\n")
grid = replace_once(grid,
    "Also f≥0. Define S4=sup_{L,H≥1} f(L,H)/(LH), allowing infinity initially. For a fixed block (a,b), tile a large rectangle with floor(L/a)floor(H/b) copies and leave its remaining strips in their original grid configuration. Repeated use of (1)–(2) yields",
    r"""Every boundary word has a minimal realization: generic straight chords give one, so Q≥1 and f≥0. Define S4=sup_{L,H≥1} f(L,H)/(LH), allowing infinity initially. For a fixed positive block (a,b), write L=qa+r and H=sb+u, with 0≤r<a and 0≤u<b. Repeatedly apply (1)–(2) and discard their nonnegative remainder terms to obtain
\[
f(L,H)\ge qs\,f(a,b).
\]
If r=0 or u=0, omit the corresponding remainder term rather than invoking f at zero. A positive-width remainder could equivalently be filled with one fixed minimal patch of its own full boundary word; no unresolved raw grid is retained. Dividing the displayed inequality by LH yields""".replace("\\\\", "\\"))
old = r"""Tile the interior of the central diamond by integer translates of the 3 by 3 square patch, omitting only O(m) patches near its boundary. The number is m²/18−O(m). Choose any of its Q(3,3) reroutings independently in each patch. At each of the t3 triple crossings outside the diamond, a disjoint tiny disk permits its two resolutions. Leave all remaining crossings unchanged. Boundary preservation and disjoint crossing-pair assignments give at least
\[
2^{m^2/2-O(m)}\,Q(3,3)^{m^2/18-O(m)}
\]
partial arrangements."""
new = r"""Use the translated 3 by 3 rectangles of the periodic tiling and retain only those whose closures lie inside the central diamond. Their number is K_m=m²/18−O(m): a discarded intersecting rectangle lies in a fixed-width band along a boundary of length O(m). Round and shrink retained supports within sufficiently thin crossing-free collars, retaining their entire paired boundary words and every grid crossing originally inside them. The rational offsets keep all grid vertices a fixed positive distance from the tiling edges, so this separates neighboring closed supports without releasing a multicrossing into an interior corridor. Choose any of the Q(3,3) minimal reroutings in each retained support.

At each of the t3 triple crossings outside the diamond, choose a tiny disk disjoint from all large supports and from the other such disks. It meets exactly its three incident strands in proper transverse two-port arcs and no nonincident line. Count both simple resolutions in each such disk.

### Fixed resolution of every uncovered multicrossing

Before the bundle-tail completion, let R_m be **all original multicrossings outside the retained large supports and the counted triple disks**, including any uncovered corridor point. In this tiling they are fourfold points in the omitted boundary band; there are O(m) of them. In particular (0,t) and (t,0) belong to this set when t≥1. They are not counted triple points and must be resolved.

Choose, once for each m and before varying any counted rerouting, a small closed disk E_v about every v in R_m. These disks can be simultaneously pairwise disjoint, disjoint from every previously selected support, and avoid all other original crossings and all lines not incident to v. Indeed there are finitely many distinct points and supports; no original grid vertex lies on a selected support boundary; and every nonincident straight line has positive distance from v. Take each radius smaller than the corresponding finite positive separation minima. Each of its four incident lines then cuts E_v in a proper transverse arc with two distinct ports. The choices made inside the other supports never alter the original geometry near E_v.

For each E_v fix **one** simple boundary-preserving four-strand resolution, for example one fixed adjacent-swap reversal wiring matched to its cyclic ports. The four incident lines' endpoints alternate pairwise, so this resolution makes every one of the six pairs cross exactly once and has no triple meeting. The same finite local construction would fix any other uncovered multicrossing if one arose under a support variant. No multiplicity is assigned to a fixed repair disk: it has one selected output, not an additional free parameter.

Only the remaining **simple** crossings are left unchanged. All selected patch realizations are simple; all counted triple disks and fixed repair disks are simple; and their boundary collars contain no crossings. Therefore the whole output is now a **simple partial arrangement**: each cross-family pair still crosses exactly once, and same-family pairs are still noncrossing. The original crossing-pair assignments were disjoint across these regions, so no replacement creates a missing or repeated pair crossing or a self-crossing of a global strand.

Every choice of the original counted patch and triple resolutions survives this fixed repair. Their local crossing orders remain recoverable in their designated slots of the global labelled strand orders, while all E_v choices are identical across outputs. Hence the number of simple partial arrangements is still at least
\[
2^{t_3}\,Q(3,3)^{K_m}
\ge 2^{m^2/2-O(m)}\,Q(3,3)^{m^2/18-O(m)}.
\]
The O(m) fixed disks add no counted choices and remove none. The omission error in K_m is the same boundary-band error already present in v1; no new exponent loss or coefficient change is introduced.

### Completion and padding""".replace("\\\\", "\\")
grid = replace_once(grid, old, new)
grid = replace_once(grid,
    "Finally, in a private tail disk for each formerly parallel bundle, insert an arbitrary marked m-strand arrangement. The standard bundle completion construction of Felsner–Valtr Section 4 and Cortés Kühnast et al. Section 4 gives an injective factor C(m)^4. Its hypotheses here are explicit: each disk meets just one bundle, all m strands of that bundle, and no other bundle. Place these disks far beyond the finite cross-family crossing region, in four separate directions.",
    "Now insert an arbitrary marked m-strand arrangement in a private tail disk "
    "for each formerly parallel bundle. The input is the **simple partial "
    "arrangement** just constructed, as required by Felsner–Valtr Section 4 "
    "and Cortés Kühnast et al. Section 4, [full arXiv version]"
    "(https://arxiv.org/abs/2402.13107). All central modifications lie in bounded "
    "supports and leave the distant tails straight and parallel. Place one disk "
    "far along a distinct ray direction of each bundle. A radius O(m) covers "
    "its bundle's width; by choosing the center distance sufficiently large, "
    "angular separation keeps every other-family line and the other tail disks "
    "outside it. Thus the four disks are pairwise disjoint, meet all m strands "
    "of their own bundle in proper transverse arcs, and meet no strand of "
    "another bundle. They are beyond every finite cross-family crossing and "
    "all the fixed repair supports. These are the cited completion construction's "
    "hypotheses and give the injective factor C(m)^4.")
grid = replace_once(grid,
    "The equality on the right uses the finite computational count Q(3,3)=4419734746 and must await its independent audit.",
    "The equality on the right uses the unchanged finite input Q(3,3)=4419734746. "
    "Both frozen initial reviews independently reproduced that input; the revised "
    "construction still requires both targeted re-audits and coordinator acceptance.")
grid = replace_once(grid,
    "Two independent adversarial reviewers, one reconstructing the entire argument, must audit any proposed promotion. In G1 check the exact seam phase, product injection and distinction from C. In G2 check the grid's triple/fourfold counts, the density and omission error of 3 by 3 patches, private bundle-tail disks, padding to all n, the recurrence coefficient, and the exact finite DP count. The unfinished L=4 run must never enter a bound.",
    "Both independent initial reports on frozen v1 are complete. Each reviewer "
    "must re-audit the actual v1.1 changes before the coordinator can accept "
    "them: G1's nonnegative remainder argument; G2's finite separation and "
    "disjoint fixed resolution disks, recovery of simple partial input, survival "
    "of every counted choice, unchanged exponent, and the tail-completion "
    "hypotheses. The full marked-boundary count and all-n padding remain in "
    "force. Q(3,3), the original computation caps and outputs are unchanged; "
    "the unfinished L=4 run must never enter a bound. This author packet "
    "remains candidate proof - unverified and contains no promotion.")
revised["periodic-grid"] = grid

source_pdf = ROOT / ".cache/literature/2017/secondpass-review-2-felsner-weil.pdf"
assert sha(source_pdf) == "a6995529d08034c0735b3f9b0b9a4f9dae01ac0a5f3864d88728c6d04f85c828"
source_images = [ROOT / f".cache/literature/2017/secondpass-review-2-source-fw-p{p}.png"
                 for p in (15, 19)]

records = []
for key, text in revised.items():
    old_name = f"secondpass-{key}-candidate-v1.md"
    new_path = NOTES / f"author-repair-{key}-candidate-v1.1.md"
    diff_path = NOTES / f"author-repair-{key}-v1-to-v1.1.diff"
    write_new(new_path, text)
    diff = "".join(difflib.unified_diff(
        originals[old_name].splitlines(keepends=True), text.splitlines(keepends=True),
        fromfile=str((NOTES / old_name).relative_to(ROOT)),
        tofile=str(new_path.relative_to(ROOT)), n=4))
    write_new(diff_path, diff)
    records.append({"claim_prefix": key, "status": "candidate proof - unverified",
                    "old_path": str((NOTES / old_name).relative_to(ROOT)),
                    "old_sha256": FROZEN[old_name],
                    "revised_path": str(new_path.relative_to(ROOT)),
                    "revised_sha256": sha(new_path),
                    "exact_diff_path": str(diff_path.relative_to(ROOT)),
                    "exact_diff_sha256": sha(diff_path),
                    "targeted_reaudits_required": 2,
                    "targeted_reaudits_completed_by_this_author": 0})

sources = {
    "inspected_local_date": "2026-10-17 Australia/Brisbane",
    "newly_cited_primary_source": {
        "authors": "Stefan Felsner and Helmut Weil",
        "title": "Sweeps, Arrangements and Signotopes",
        "url": "https://page.math.tu-berlin.de/~felsner/Paper/sas-dam-rev.pdf",
        "cache_path": str(source_pdf.relative_to(ROOT)),
        "bytes": source_pdf.stat().st_size, "sha256": sha(source_pdf),
        "inspected": "Theorems 7-8 and Definition 1 on printed p. 15; proof of Theorem 7 on printed p. 19",
        "method": "Author personally inspected existing rendered primary pages and checked cached PDF fingerprint; old-font pypdf extraction is known unusable",
        "image_provenance": "Frozen reviews/secondpass-review-2-sources.json and secondpass-review-2-render.py",
        "images_inspected": [{"path": str(p.relative_to(ROOT)), "sha256": sha(p)} for p in source_images],
        "retrieval": "Reused existing ignored cache; no new download or source redistribution",
        "redistribution_licence_verified_by_repair_author": False,
        "tracked_full_paper": False,
    },
    "other_primary_hypotheses_retained": [
        {"url": "https://page.math.tu-berlin.de/~felsner/Paper/new-pla.pdf",
         "cache_path": ".cache/literature/2017/cited-7f7251133b0c4ebc.pdf",
         "sha256": sha(ROOT / ".cache/literature/2017/cited-7f7251133b0c4ebc.pdf"),
         "role": "MacMahon product and marked bundle completion; no change to M1/M3 proof"},
        {"url": "https://arxiv.org/pdf/2402.13107",
         "cache_path": ".cache/literature/2017/cited-b5bf6499a3fedd25.pdf",
         "sha256": sha(ROOT / ".cache/literature/2017/cited-b5bf6499a3fedd25.pdf"),
         "role": "Section 4 simple partial input and private tail-disk hypotheses restored explicitly"},
    ],
}
write_new(NOTES / "author-repair-sources-v1.1.json", json.dumps(sources, indent=2) + "\n")
preserved_after = {str(p.relative_to(ROOT)): sha(p) for p in preserved_paths}
assert preserved_after == preserved_before, "frozen input changed during repair build"
manifest = {
    "version": "v1.1", "local_date": "2026-10-17 Australia/Brisbane",
    "author": "/root/owner_2017", "authorship": "Original second-pass constructor and author of these revisions",
    "status": "candidate proof - unverified; no promotion",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning_effort": "max"},
    "verified_effective_settings": None,
    "review_inputs": [{"path": str((YEAR / "reviews" / p).relative_to(ROOT)),
                       "sha256": sha(YEAR / "reviews" / p)}
                      for p in ("secondpass-review-1.md", "secondpass-review-2-initial.md")],
    "candidates": records,
    "source_record": {"path": "problems/2017-B4/notes/author-repair-sources-v1.1.json",
                      "sha256": sha(NOTES / "author-repair-sources-v1.1.json")},
    "unchanged_finite_input": {"Q_3_3": 4419734746, "new_computational_runs": 0,
                               "larger_caps": False, "L4_count": None},
    "preserved_inputs_before_equals_after": True,
    "preserved_input_sha256": preserved_before,
    "weekly_context_from_coordinator": {"used_percent_total": 9,
                                        "reset_timestamp": 1792745187,
                                        "stop_percent_total": 90},
}
write_new(NOTES / "author-repair-manifest-v1.1.json", json.dumps(manifest, indent=2) + "\n")
for rec in records:
    print(rec["revised_path"], rec["revised_sha256"])
    print("exact_diff", rec["exact_diff_path"], rec["exact_diff_sha256"])
print("preserved_frozen_inputs", len(preserved_paths), "all hashes unchanged")
print("new computational searches: none; Q(3,3)=4419734746 unchanged; all v1.1 claims unverified")
