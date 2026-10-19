"""NEW R20 documentary metadata only; never executes mathematical code.

Allowed modes: prepare (create NEW source JSON and baseline), freeze (bind
the four payloads), verify (read-only verification). It hashes only the
explicitly named necessary paths. It does not traverse peer directories,
run other source/author/freezer code, or calculate mathematical examples.
"""
import datetime
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2020-B4/notes/reasoning-global-return-r20-"
MAIN = PREFIX + "candidate-v1.md"
SOURCES = PREFIX + "sources-v1.json"
BASELINE = PREFIX + "baseline-v1.json"
ADMIN = PREFIX + "admin-v1.py"
FREEZE = PREFIX + "freeze-v1.json"
PAYLOADS = [MAIN, SOURCES, ADMIN, BASELINE]


def stamp():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def info(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def create(path, obj):
    destination = ROOT / path
    with destination.open("x", encoding="utf-8") as stream:
        json.dump(obj, stream, ensure_ascii=False, indent=2)
        stream.write("\n")


def read_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def check_record(record):
    actual = info(record["path"])
    for key in ("bytes", "sha256"):
        if actual[key] != record[key]:
            raise SystemExit("DOCUMENTARY MISMATCH " + record["path"] + " " + key)


def check_guards():
    baseline = read_json(BASELINE)
    for guard in baseline["immutable_guards"]:
        check_record(guard)
    return baseline


def prepare():
    guards = [
        "AGENTS.md",
        "problems/2020-B4/statement.md",
        "problems/2020-B4/proofs/reviewed-reasoning-actual-return-r18-v1.1.md",
        "problems/2020-B4/reviews/reasoning-actual-return-r18-acceptance.md",
        "problems/2020-B4/reviews/reasoning-actual-return-r18-acceptance.json",
        "problems/2020-B4/proofs/reviewed-reasoning-realization-return-r19-v1.1.md",
        "problems/2020-B4/reviews/reasoning-realization-return-r19-acceptance.md",
        "problems/2020-B4/reviews/reasoning-realization-return-r19-acceptance.json",
        "problems/2025-B4/notes/reasoning-exception-return-r12-freeze-v1.json",
        "problems/2019-B4/reviews/reasoning-critical-law-return-r16-review-2-manifest-v1.json",
    ]
    declared = {
        guards[0]: (4707, "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"),
        guards[2]: (43966, "f38609238baaa9909dfd7655220794a89bf7e00a5f128253d56167507f2d48cf"),
        guards[5]: (36261, "1318589dd05ccf4b1a78e8200b87e9f77148eacbe27c485358a81a10698ef7a2"),
        guards[8]: (2517, "79e7c6bd6746a38b1cceb44a773f7b267795560ed7439a88564994ec93e3d68b"),
        guards[9]: (2884, "4ae35fa60820cd6974a8181a94eaeb4537a1ff6c7ff284b925e9668f6abc80a7"),
    }
    records = [info(p) for p in guards]
    for record in records:
        if record["path"] in declared:
            expected_bytes, expected_sha = declared[record["path"]]
            if (record["bytes"], record["sha256"]) != (expected_bytes, expected_sha):
                raise SystemExit("DECLARED OLD FINGERPRINT MISMATCH " + record["path"])
    baseline = {
        "schema": "R20-compact-preservation-v1", "created_utc": stamp(),
        "immutable_guards": records,
        "guard_occurrences": len(records), "guard_deduplicated_paths": len(set(guards)),
        "own_immediate_parents": [
            {"path": guards[8], "role": "own sole-author ET12, frozen unverified; no other review access",
             "historical_necessary_guard_occurrences": 10, "historical_deduplicated_paths": 10},
            {"path": guards[9], "role": "own CM16 whole2, complete and explicitly released before R20",
             "historical_necessary_guard_occurrences": 26, "historical_deduplicated_paths": 26},
        ],
        "ancestry_policy": "Bind parent manifests exactly; do not copy their historical inventories or replay them.",
        "mutable_observations_not_immutable_guards": [
            info("problems/2020-B4/research.md"), info("problems/2020-B4/references.md")],
        "mutable_policy": "Living maps may be updated by coordinator; observations are historical, not frozen proof guards.",
        "peer_access": "No corresponding NEW active peer files/inventory/hash/metadata accessed.",
        "mathematical_computation": False,
    }
    create(BASELINE, baseline)
    sources = {
        "schema": "R20-source-scope-v1", "created_utc": stamp(),
        "status": "candidate proof - unverified; two OTHER whole audits required",
        "role": {"constructor": "B /root/review_2022_complexity_r2", "root": "generic assignment only; no new R20 inference",
                 "old_roles": "B constructed R18/AR19/SQ14 and other accepted inputs; no independent self-recertification",
                 "requested_model": "gpt-6.1-sol", "requested_reasoning": "max", "verified_effective_readback": None},
        "accepted_inputs": [
            {"body": guards[2], "acceptance_md": guards[3], "acceptance_json": guards[4],
             "read_scope": "COMPLETE current body and EACH authority; clipped339--510 recovered before final reasoning",
             "operative_use": "Actual cyclic normalization, exact integral and ALL-character scope boundaries; not a composite sufficiency theorem"},
            {"body": guards[5], "acceptance_md": guards[6], "acceptance_json": guards[7],
             "read_scope": "COMPLETE current body and EACH authority; final611--619 recovered",
             "operative_use": "Full-field quadratic unit repair remains mandatory; general content/reciprocal theorem needs ALL orders; no family exclusion"},
        ],
        "primary_sources": [
            {"id": "official2020", "url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2020-paper-b_1.pdf",
             "read_scope": "Fresh setup/open(b)98--105; complete saved statement. No preliminary proof or neighboring problem investigated.",
             "use": "Exact open domain only", "raw_pdf_sha256": None},
            {"id": "Turyn1965", "title": "Character sums and difference sets",
             "url": "https://msp.org/pjm/1965/15-1/pjm-v15-n1-p32-p.pdf",
             "read_scope": "COMPLETE Lemma5 statement/proof605--625, surrounding572--636; other returned fragments not whole-paper certification. Screenshot had no inspectable pixels.",
             "use": "Attributed existing coefficient bound and overlap comparison only; new proof is self-contained.",
             "raw_pdf_sha256": None},
            {"id": "LamLeung1995", "url": "https://arxiv.org/pdf/math/9511209",
             "read_scope": "Theorem2.2 and full proof153--264; Theorem3.3/full proof381--413; explicit characteristic0 warning95--96.",
             "use": "Classical kernel context; NOT imported as finite-field classification", "whole_paper_read": False,
             "original_earlier_reference_proofs_read": False, "raw_pdf_sha256": None},
            {"id": "MahatabSampath2015", "url": "https://arxiv.org/pdf/1401.7696",
             "read_scope": "Returned0--449, including complete Lemmas2.1/2.2 and Theorem2.4 proofs; not complete later Smith-form proof/algorithm chain.",
             "use": "Classical integral CRT warning; no algorithm or mathematical certificate executed", "raw_pdf_sha256": None},
            {"id": "ReedOrthogonality", "url": "https://people.reed.edu/~jerry/361/lectures/kummer.pdf",
             "read_scope": "Fresh COMPLETE Appendix9.2,1505--1553; other returned nearby text not whole-note audit",
             "use": "Orthogonality comparison; characteristic-ell geometric sums and inverse proved in main", "raw_pdf_sha256": None},
            {"id": "AlexeevMixon2026", "url": "https://arxiv.org/pdf/2510.19804",
             "read_scope": "Returned299--335 only", "use": "Qualified cyclic/PPC versus Desarguesian context; no exhaustive status or priority claim",
             "raw_pdf_sha256": None},
        ],
        "literature_limit": "No claim that the proposed refinement is unpublished; no original de Bruijn/Redei/Schoenberg or complete current literature audit.",
        "new_claims": ["GR20A radical blocks and primitive characteristic-ell vanishing", "GR20B Sidon obstruction including content2",
                       "GR20C actual single-primitive content1 and reciprocal iff in omega(v)<=2 sector", "GR20D fixed contentful primitive ideal cannot have any actual completion"],
        "remaining_gap": "Three-or-more-prime conductors, content1 alternatives, actual mixed-q class/unit choices and full compatible binary realization unresolved.",
        "preservation_baseline": BASELINE,
        "access": {"public_free_only": True, "pdf_download_or_cache_write": False,
                   "redistribution": False, "fees_contact_bypass": False},
        "budget": {"authorized_reset": 1792874445, "ceiling_total_weekly_used_percent": 90,
                   "last_direct_total_weekly_used_percent": 81, "last_direct_utc": "2026-10-19 02:20:00 UTC",
                   "window_minutes": 10080, "ordinary_usage_allowed": True, "account_label": "...ac3a",
                   "reserve_required": True, "automatic_later_window_spending": False},
    }
    create(SOURCES, sources)
    print(json.dumps({"mode": "prepare", "utc": stamp(), "payloads_created": [BASELINE, SOURCES],
                      "immutable_guards": len(records)}, indent=2))


def freeze():
    baseline = check_guards()
    text = (ROOT / MAIN).read_text(encoding="utf-8")
    for i in range(1, 41):
        if text.count("|GR20-" + str(i).zfill(2) + "|") != 1:
            raise SystemExit("LITERAL OBLIGATION LABEL FAILURE " + str(i))
    manifest = {
        "schema": "R20-complete-author-freeze-v1", "frozen_utc": stamp(),
        "status": "candidate proof - unverified", "whole_obligations": 40,
        "claims": ["GR20A", "GR20B", "GR20C", "GR20D"],
        "constructor_excluded_from_reviews": "B", "other_whole_reviews_required": 2,
        "requested_model": "gpt-6.1-sol", "requested_reasoning": "max", "verified_effective_readback": None,
        "payloads": [info(p) for p in PAYLOADS], "entire_file_count_including_manifest": 5,
        "parent_baseline": BASELINE, "necessary_guard_occurrences": baseline["guard_occurrences"],
        "necessary_guard_deduplicated_paths": baseline["guard_deduplicated_paths"],
        "final_payload_model_readback": "Completed on final bytes before this freeze; manifest MODEL readback then SEPARATE read-only verification must follow.",
        "mathematical_executables_or_scans": False,
        "authorized_weekly_reset": 1792874445, "total_weekly_stop_percent": 90,
        "reserve_required": True,
    }
    create(FREEZE, manifest)
    print(json.dumps({"mode": "freeze", "utc": stamp(), "manifest": info(FREEZE)}, indent=2))


def verify():
    manifest = read_json(FREEZE)
    if [p["path"] for p in manifest["payloads"]] != PAYLOADS:
        raise SystemExit("PAYLOAD INVENTORY MISMATCH")
    for record in manifest["payloads"]:
        check_record(record)
    baseline = check_guards()
    read_json(SOURCES)
    text = (ROOT / MAIN).read_text(encoding="utf-8")
    for i in range(1, 41):
        if text.count("|GR20-" + str(i).zfill(2) + "|") != 1:
            raise SystemExit("LITERAL LABEL MISMATCH")
    print(json.dumps({"mode": "SEPARATE_READ_ONLY_VERIFY", "verified_utc": stamp(), "result": "PASS",
                      "entire_files": len(PAYLOADS) + 1, "literal_obligation_labels": 40,
                      "immutable_guards": baseline["guard_occurrences"],
                      "manifest": info(FREEZE), "payloads": [info(p) for p in PAYLOADS],
                      "mathematics_certified_by_code": False}, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ("prepare", "freeze", "verify"):
        raise SystemExit("Use prepare, freeze, or verify (documentary only)")
    {"prepare": prepare, "freeze": freeze, "verify": verify}[sys.argv[1]]()
