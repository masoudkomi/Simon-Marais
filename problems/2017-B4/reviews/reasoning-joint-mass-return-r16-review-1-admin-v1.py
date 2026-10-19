"""NEW documentary helper only: fixed paths, bytes/SHA, JSON and literal row IDs.

No mathematical evaluation, source/author/old-helper replay, peer inventory,
network, subprocess, Git or cache write. verify is read-only.
"""
from pathlib import Path
import argparse
import datetime
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/reviews/reasoning-joint-mass-return-r16-review-1-"
BASELINE = PREFIX + "baseline-v1.json"
MANIFEST = PREFIX + "manifest-v1.json"
PAYLOADS = [PREFIX + suffix for suffix in
            ("initial-v1.md", "sources-v1.json", "admin-v1.py", "baseline-v1.json")]
EXPECTED = [
 ("AGENTS.md",4707,"28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"),
 ("problems/2017-B4/statement.md",2140,"e459750064b4e25e3eaa71f25f236c046548147e415b06d8bd097839020228f3"),
 ("problems/2017-B4/notes/reasoning-joint-mass-return-r16-candidate-v1.md",22236,"f202e568a7f48810bfe0d3b567338477c91f09023267eb1e15b356722737b886"),
 ("problems/2017-B4/notes/reasoning-joint-mass-return-r16-sources-v1.json",4222,"c59436cfa0a62ee1bb5d8f3465f603a248c99d702baaf999e7aa5bd59afb1ae7"),
 ("problems/2017-B4/notes/reasoning-joint-mass-return-r16-admin-v1.py",7518,"c9e89a65c1485b89849b535426054d0cd23723fcaa21d8110a8396d928fc985b"),
 ("problems/2017-B4/notes/reasoning-joint-mass-return-r16-baseline-v1.json",4920,"4fab5117d1c80757f5f6db40f849ba4d8325c3185820b74d85f24760fe95aff2"),
 ("problems/2017-B4/notes/reasoning-joint-mass-return-r16-freeze-v1.json",2455,"487d92acc4bb6fe433b656473e487f88bcf17cf6341d9a15364ed6f9be3571ef"),
 ("problems/2017-B4/proofs/reviewed-reasoning-pressure-return-r11-v1.1.md",26687,"56688cd6030db910fbbc9162436b25acbf61a69869e2501dbd6f50b088bc3b60"),
 ("problems/2017-B4/reviews/reasoning-pressure-return-r11-acceptance.md",6651,"c280687595657001f2c5a92f2d9d430ad2bf39b72eb89c0e40308dedd4f33580"),
 ("problems/2017-B4/reviews/reasoning-pressure-return-r11-acceptance.json",3987,"85f5f93a8294af528f487ca9d62eadbc054c98db1ea312e48de9edd8c02547e8"),
 ("problems/2017-B4/proofs/reviewed-reasoning-concentration-return-r12-v1.1.md",24123,"15823ad1a7c54b8e06de3692f19d3395d2458786dcb8d2d51a2eb3c592734554"),
 ("problems/2017-B4/reviews/reasoning-concentration-return-r12-acceptance.md",5074,"8ab812c05255394241048061650c6ee720a3506f2acf11fbbbc3cccfaccf7d83"),
 ("problems/2017-B4/reviews/reasoning-concentration-return-r12-acceptance.json",3824,"f83181566e126280d81c543112c169d80234d6f0aa3995ee3b8abce95f9bc844"),
 ("problems/2017-B4/proofs/reviewed-reasoning-lower-return-r14-v1.1.md",24422,"88eed98d9ae634700fd23d571aad68cb4c59fd2fcd45e44dc48f9634c3d208c7"),
 ("problems/2017-B4/reviews/reasoning-lower-return-r14-acceptance.md",5661,"0e09166d322715b8f35347a985fc1cef64af41df1f6bb4b09f689a77449fdfba"),
 ("problems/2017-B4/reviews/reasoning-lower-return-r14-acceptance.json",3678,"b2c74f0f00ea445f385736f01cc80548b46f291866ec781313ac560673ee0fc0"),
 ("problems/2017-B4/proofs/reviewed-reasoning-joint-return-r15-v1.1.md",35630,"b35e0a5b0bbefbafece8467d010ffe6fdb33629ee45c76aeff78bfdef5e05569"),
 ("problems/2017-B4/reviews/reasoning-joint-return-r15-acceptance.md",5428,"40943693a781354ed60d831aeaf494b26ddb8e592d9ee0dcd8b2a34bed673cbc"),
 ("problems/2017-B4/reviews/reasoning-joint-return-r15-acceptance.json",3121,"52737f14fec5f456c6509d8ca079873e50a58a5d943980f23e1a6d86d79cbeb0"),
 ("problems/2021-B4/reviews/coordinator-dyadic-return-r26-review-2-manifest-v1.json",1863,"fbb6d2f61568708333547c36abe620a3c989628d619aa992e4d95f0566e04729")
]

def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def fp(rel):
    data = (ROOT / rel).read_bytes()
    return {"path": rel, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}

def read_json(rel):
    return json.loads((ROOT / rel).read_text())

def exclusive_json(rel, value):
    assert rel in (BASELINE, MANIFEST)
    with (ROOT / rel).open("x") as out:
        out.write(json.dumps(value, indent=2, ensure_ascii=False) + "\n")

def checked_guards():
    records = []
    for rel, size, sha in EXPECTED:
        record = fp(rel)
        assert record["bytes"] == size and record["sha256"] == sha, record
        records.append(record)
    assert len({r["path"] for r in records}) == len(records) == 20
    return records

def summary(records):
    canonical = json.dumps(sorted(records, key=lambda r:r["path"]),
                           sort_keys=True, separators=(",", ":")).encode()
    return {"occurrences":len(records), "unique_paths":len(records),
            "canonical_deduplicated_sha256":hashlib.sha256(canonical).hexdigest()}

def rows():
    text = (ROOT / PAYLOADS[0]).read_text()
    for number in range(1,33):
        assert text.count(f"|JM16-{number:02d}|") == 1
    assert "No open substantive issue" in text
    return 32

def baseline():
    records = checked_guards()
    value = {"captured_UTC":now(), "guard_summary":summary(records),
             "guards":records, "ONE_exact_OWN_parent_manifest":records[-1],
             "recursive_inventory_expansion":False,
             "mutable_map_observation_is_not_immutable_guard":True,
             "NEW_corresponding_JM16_peer_access":False,
             "forbidden_R27_access":False,
             "documentary_only":True}
    exclusive_json(BASELINE,value)
    print(json.dumps({"baseline":fp(BASELINE),"guards":summary(records)}))

def verify_baseline():
    value = read_json(BASELINE)
    records = checked_guards()
    assert value["guards"] == records
    assert value["guard_summary"] == summary(records)
    return value

def freeze():
    value = verify_baseline()
    count = rows()
    read_json(PAYLOADS[1])
    result = {"frozen_UTC":now(),
              "status":"sealed OTHER independent WHOLE1 initial; not coordinator promotion",
              "reviewer":"/root/review_2022_complexity_r2",
              "constructor_excluded":True,"claims":["JM16A","JM16B","JM16C"],
              "ENTIRE_files":5,"ALL_obligations":count,
              "payloads":[fp(rel) for rel in PAYLOADS],
              "guard_summary":value["guard_summary"],
              "ONE_exact_OWN_parent_manifest":value["ONE_exact_OWN_parent_manifest"],
              "FULL_final_ALL4_payload_MODEL_readbacks_completed":True,
              "FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_REQUIRED":True,
              "corresponding_NEW_peer_access_before_explicit_BOTH":False,
              "findings_sealed_until_explicit_BOTH":True,
              "requested":{"model":"gpt-6.1-sol","reasoning":"max","inherited":True},
              "independent_effective_backend_readback":None,
              "no_mathematical_executable_or_replay":True,
              "quota":{"usedPercent":83,"observed_UTC":"2026-10-19 02:41:16 UTC",
                       "resetsAt":1792874445,"TOTAL_ceiling":90,
                       "review_integration_reserve":True,"automatic_later_window_spending":False}}
    exclusive_json(MANIFEST,result)
    print(json.dumps({"manifest":fp(MANIFEST),"frozen_UTC":result["frozen_UTC"]}))

def verify():
    before = fp(MANIFEST)
    value = read_json(MANIFEST)
    verify_baseline()
    assert value["payloads"] == [fp(rel) for rel in PAYLOADS]
    assert value["ALL_obligations"] == rows() == 32
    assert value["ENTIRE_files"] == 5
    assert fp(MANIFEST) == before
    print(json.dumps({"SEPARATE_readonly_verify_UTC":now(),"status":"PASS",
                      "ENTIRE_files":5,"ALL_literal_obligation_rows":32,
                      "necessary_immutable_paths":20,"manifest":before}))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode",choices=("baseline","freeze","verify"))
    args = parser.parse_args()
    {"baseline":baseline,"freeze":freeze,"verify":verify}[args.mode]()
