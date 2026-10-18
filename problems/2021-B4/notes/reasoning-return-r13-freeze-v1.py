"""Administrative-only R13 constructor freeze: bytes, JSON, syntax; no mathematics."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2021-B4/notes/reasoning-return-r13-"
rows = []
groups = []


def data(path):
    assert not Path(path).is_absolute() and ".." not in Path(path).parts
    assert not Path(path).name.startswith("reasoning-return-r13-review-")
    return (ROOT / path).read_bytes()


def fp(path):
    value = data(path)
    return {"path": path, "bytes": len(value), "sha256": hashlib.sha256(value).hexdigest()}


def expected(path, size, sha):
    return {"path": path, "bytes": size, "sha256": sha}


def check(item, origin):
    item = {k: item[k] for k in ("path", "bytes", "sha256")}
    assert fp(item["path"]) == item, (origin, item["path"])
    rows.append({"origin": origin, **item})
    return item


def summary(items):
    unique = {}
    for item in items:
        core = {k: item[k] for k in ("path", "bytes", "sha256")}
        if core["path"] in unique:
            assert unique[core["path"]] == core
        unique[core["path"]] = core
    ordered = [unique[path] for path in sorted(unique)]
    digest = hashlib.sha256(json.dumps(ordered, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return {"occurrences": len(items), "unique_paths": len(unique),
            "canonical_deduplicated_summary_sha256": digest}


def save(suffix, value):
    with (ROOT / (P + suffix)).open("x", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")
    return fp(P + suffix)


start = len(rows)
own_parent_path = "problems/2017-B4/reviews/reasoning-value-return-r6-review-1-reaudit-v1.1-manifest.json"
check(expected(own_parent_path, 4296,
               "63b3a552da7508fada692479d4adc0c8d241df4d7e06bc614ca99fa0f1bcb726"),
      "immediate own immutable review parent, NOT mathematical premise")
own_parent = json.loads(data(own_parent_path))
assert len(own_parent["artifacts"]) == 7
for item in own_parent["artifacts"]:
    check(item, "direct own frozen parent payload, NOT mathematical premise")
groups.append({"group": "immediate own immutable parent", "metadata": fp(own_parent_path),
               "selector": "self plus artifacts[0:7]", "verified": summary(rows[start:]),
               "historical_input_summary_bound": own_parent["compact_current_summary"],
               "historical_rows_bound_not_recopied_or_claimed_reread": True})

authorities = [
    expected("problems/2021-B4/reviews/reasoning-return-r5-acceptance.json", 3373,
             "93a204890e6d387a22d89565dbee9ee970c1b80af59f79cbc983d3ba4de6defe"),
    expected("problems/2021-B4/reviews/reasoning-return-r8-acceptance.json", 2507,
             "b5ca7a381393061192beceb0b34b8222c6ae249f1edc3383ac316786c7cd3ef0"),
    expected("problems/2021-B4/reviews/reasoning-return-r12-acceptance.json", 2801,
             "28f2a33fd4cdb39bcd899df9bb450628e928afe483f7a6be443a32d649dbd00b"),
]
for authority_record in authorities:
    start = len(rows)
    check(authority_record, "operative accepted authority metadata")
    authority = json.loads(data(authority_record["path"]))
    md = authority_record["path"].replace(".json", ".md")
    check(fp(md), "complete acceptance scope read")
    for key in ("candidate", "accepted_copy"):
        check(authority[key], "accepted authority exact " + key + " declaration")
    assert data(authority["accepted_copy"]["path"]).endswith(data(authority["candidate"]["path"]))
    groups.append({"group": "operative accepted input", "metadata": authority_record,
                   "selector": "self, acceptance Markdown, candidate, accepted_copy",
                   "verified": summary(rows[start:]),
                   "accepted_body_has_exact_frozen_constructor_suffix": True,
                   "old_constructor_or_reviewer_roles_not_fresh_independent_recertification": True})

start = len(rows)
check(expected("AGENTS.md", 4707,
               "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"),
      "current protocol")
check(fp("problems/2021-B4/statement.md"), "actual local official-domain normalization read")
groups.append({"group": "protocol and domain", "verified": summary(rows[start:]),
               "records": [{k: item[k] for k in ("path", "bytes", "sha256")} for item in rows[start:]]})

start = len(rows)
r12_parent_path = "problems/2021-B4/notes/reasoning-return-r12-freeze-v1.json"
check(expected(r12_parent_path, 4087,
               "3ed49540ef24d6b947add1abc2db155f6c3bda82c8e2a40c7615547aa3351f02"),
      "own prior mathematical constructor packet preservation")
r12_parent = json.loads(data(r12_parent_path))
assert len(r12_parent["artifacts"]) == 10
for item in r12_parent["artifacts"]:
    check(item, "direct prior R12 immutable payload")
groups.append({"group": "prior R12 whole constructor preservation", "metadata": fp(r12_parent_path),
               "selector": "self plus artifacts[0:10]", "verified": summary(rows[start:]),
               "historical_input_summary_bound": r12_parent["compact_input_summary"],
               "R13_uses_accepted_copy_and_scope_not_the_old_unverified_label": True})

obligations = data(P + "obligations-v1.md").decode()
ids = re.findall(r"^\| (\d\d) \|", obligations, flags=re.MULTILINE)
assert ids == [f"{n:02d}" for n in range(1, 45)], ids
payloads = [P + suffix for suffix in (
    "candidate-v1.md", "obligations-v1.md", "constructor-checks-v1.md",
    "failed-routes-v1.md", "source-audit-v1.md", "worklog-v1.md", "freeze-v1.py")]
assert all((ROOT / path).is_file() for path in payloads)
for suffix in ("sources-v1.json", "input-validation-v1.json", "freeze-output-v1.json", "freeze-v1.json"):
    assert not (ROOT / (P + suffix)).exists(), suffix

current_summary = summary(rows)
current_summary.update({"encoding": "UTF8 JSON sorted unique path/bytes/sha256; sorted keys; compact separators",
                        "old_parent_inventory_rows_bound_not_recopied": True})
source_records = [
    {"title": "Official2021 Paper B", "url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf",
     "actual_read": "page2 B4 hypothesis and part(b); no preliminary proof", "native_response_sha256": None},
    {"title": "CLO Constraints on counterexamples", "url": "https://arxiv.org/pdf/1208.5404",
     "actual_read": "served v1; sections3.4-3.5 equations9-13/Lemma17; Proposition19 and unramified remark; not all23pages",
     "role": "published normalization/center context, NOT stronger all-root-rational or unramified exclusion",
     "native_response_sha256": None},
    {"title": "Draisma-de Jong2011 erratum", "url": "https://math-unibe.ch/jdraisma/publications/erratumcasasalvero.pdf",
     "actual_read": "complete original one-page correction,20 extracted lines",
     "role": "preserve excluded prime5 in old degree4 step; no degree20 shortcut", "native_response_sha256": None},
]
save("sources-v1.json", {"verified_date_utc": "2026-10-18", "primary_records": source_records,
                        "operative_local_authority": authorities,
                        "all_browser_calls_bounded_returned_normally": True,
                        "no_native_source_download_cache_edit_charge_contact_or_bypass": True,
                        "requested_model": "gpt-6.1-sol", "requested_reasoning": "max",
                        "independently_verified_effective_setting_readback": None})
payloads.append(P + "sources-v1.json")
save("input-validation-v1.json", {"status": "all necessary current fingerprints verified; immutable parents bound compactly",
                                  "summary": current_summary, "groups": groups,
                                  "all44_obligation_IDs_exact": True,
                                  "root_supplied_NO_new_R13_mathematical_inference": True,
                                  "two_OTHER_whole_audits_required": True,
                                  "no_unrelated_historical_inventory_or_old_mathematical_reread_claim": True})
payloads.append(P + "input-validation-v1.json")
unique = {}
for item in rows:
    unique[item["path"]] = {k: item[k] for k in ("path", "bytes", "sha256")}
for item in unique.values():
    assert fp(item["path"]) == item
output = {"status": "COMPLETE R13 mathematical constructor checkpoint - candidate proof unverified",
          "claims": ["R13A exact quartic weighted-interpolation obstruction",
                     "R13B actual m5 T4+two-noncenter exclusion",
                     "R13C every actual m5 break forces nonunit EC10 or EC11"],
          "whole_obligations": 44, "compact_current_summary": current_summary,
          "all_current_necessary_inputs_rechecked": True,
          "mathematical_program_scan_CAS_author_rerun_or_old_certificate_replay": False,
          "new_finite_certificate_derived_entirely_by_hand": True}
save("freeze-output-v1.json", output)
payloads.append(P + "freeze-output-v1.json")
manifest = {
    "frozen_at_utc": datetime.now(timezone.utc).isoformat(), "status": output["status"],
    "constructor": "/root/review_2021_reasoning_j15_r2", "claims": output["claims"],
    "whole_obligations": 44, "two_OTHER_fresh_initially_blind_ENTIRE_WHOLE_audits_required": True,
    "constructor_excluded_from_independent_review": True,
    "root_supplied_NO_new_R13_mathematical_inference": True,
    "no_full_m5_m3m5_J15_degree20_annual_lift_height_or_novelty_claim": True,
    "remaining_EC10_EC11_not_excluded_T4_not_itself_eliminated": True,
    "no_extra_unit_depth_bound_real_root_quotient_CA_or_field_to_Q_lift_assumption": True,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
    "independently_verified_effective_settings": None,
    "mathematical_program_scan_CAS_author_rerun_old_certificate_replay": False,
    "proof_critical_finite_certificate_entirely_hand_derived": True,
    "old_shared_cache_Git_writes_spawn_contact_charge_bypass": False,
    "authoritative_weekly_snapshot": {
        "tool": "mcp__codex_app__get_usage_limits", "at_utc": "2026-10-18 01:15:03 UTC",
        "total_weekly_used_percent": 7, "window_minutes": 10080, "reset_unix": 1792874445,
        "ordinary_usage_allowed": True, "legacy_and_by_limit_agree": True,
        "new_window_explicitly_user_authorized": True, "ceiling_total_percent": 90,
        "integration_reserve_retained": True, "automatic_further_reset_authorized": False},
    "compact_current_summary": current_summary, "compact_input_groups": len(groups),
    "administrative_command": "python3 " + P + "freeze-v1.py",
    "artifacts": [fp(path) for path in payloads],
}
assert len(manifest["artifacts"]) == 10
result = save("freeze-v1.json", manifest)
print(json.dumps({"manifest": result, "main": fp(P + "candidate-v1.md"), **output}, indent=2))
