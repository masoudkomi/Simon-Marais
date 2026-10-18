"""Create-new constructor integrity only. NO mathematical calculation."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[3]
P="problems/2024-B4/notes/coordinator-neighbor-Frobenius-r1-"
def fp(path):
 b=(ROOT/path).read_bytes()
 return {"path":path,"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest()}
def verify(row):
 assert fp(row["path"])=={k:row[k]for k in ("path","bytes","sha256")},row["path"]
 return row
def write(suffix,obj):
 with(ROOT/(P+suffix)).open("x")as f:json.dump(obj,f,indent=2);f.write("\n")
 return fp(P+suffix)
assert not(ROOT/(P+"freeze-v1.json")).exists()
prose=["candidate-v1.md","obligations-v1.md","source-audit-v1.md","failed-routes-worklog-v1.md"]
for s in prose:assert(ROOT/(P+s)).stat().st_size>1000
ids=re.findall(r"^\|NF-(\d\d)\|",(ROOT/(P+"obligations-v1.md")).read_text(),re.M)
assert ids==[str(i).zfill(2)for i in range(1,37)]
paths=[
"AGENTS.md","problems/2024-B4/statement.md",
"problems/2024-B4/proofs/reviewed-structural-v1.1.md",
"problems/2024-B4/reviews/structural-acceptance.json",
"problems/2024-B4/proofs/reviewed-reasoning-sector3-return-r1-v1.1.md",
"problems/2024-B4/reviews/reasoning-sector3-return-r1-acceptance.json",
"problems/2024-B4/proofs/reviewed-coordinator-three-bit-sector-r2-v1.1.md",
"problems/2024-B4/reviews/coordinator-three-bit-sector-r2-acceptance.json",
"problems/2024-B4/notes/coordinator-three-bit-sector-r2-freeze-v1.json",
"problems/2024-B4/notes/deep-literature-r2-report-v1.md",
".cache/literature/deep-literature-r2/2024-mcguire-thesis-1995.pdf",
".cache/literature/deep-literature-r2/2024-mcguire-thesis-1995-29.png",
".cache/literature/deep-literature-r2/2024-mcguire-thesis-1995-30.png",
".cache/literature/deep-literature-r2/2024-mcguire-thesis-1995-31.png"]
rows=[fp(p)for p in paths]
known={
"AGENTS.md":(4707,"28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"),
"problems/2024-B4/proofs/reviewed-structural-v1.1.md":(17079,"082dc054ce2cdaea80eee009f4c97c877c6968afb54b5a8f3141b7354031dd3f"),
"problems/2024-B4/proofs/reviewed-reasoning-sector3-return-r1-v1.1.md":(20891,"3ac11ac56064b4c8b3468f0463861e77fceb300451a19f28f9d0926bc72a9573"),
"problems/2024-B4/proofs/reviewed-coordinator-three-bit-sector-r2-v1.1.md":(20916,"52e107759f513006a93f141add6130ca31b2d14220c9980ef596e9bebf5d2dab"),
".cache/literature/deep-literature-r2/2024-mcguire-thesis-1995.pdf":(2610589,"d8e8e62d873c5ec69e2fd40473a9aee257bb8d4994cb5ffc1a42cb70f8bcbd24"),
".cache/literature/deep-literature-r2/2024-mcguire-thesis-1995-29.png":(106413,"edb2c7908b91cd9660a642182ada3368d8c158943dc7f9ac5d683887f42d1291"),
".cache/literature/deep-literature-r2/2024-mcguire-thesis-1995-30.png":(109501,"17ef8e3e1059bd3ef92b476de626ed09348e82b3c9a2250e7b092816b2fa8002"),
".cache/literature/deep-literature-r2/2024-mcguire-thesis-1995-31.png":(73663,"cc2748e9d2d00e31a2ab5dfb6e0d7650e52c75133863430d2e3ce1c037c570b8")}
for row in rows:
 if row["path"]in known:assert(row["bytes"],row["sha256"])==known[row["path"]],row["path"]
inputs=write("inputs-v1.json",{
"recorded_at_utc":datetime.now(timezone.utc).isoformat(),
"status":"candidate proof - unverified","administrative_only":True,
"direct_context_records":rows,"occurrences_verified":len(rows),"unique_paths_verified":len(paths),
"old_accepted_T1_S3_three_bit_used_as_mathematical_premise":False,
"all_new_special_mathematics_directly_supplied":True,
"historical_inventories_not_recopied_or_mathematically_replayed":True,
"only_classical_imports":["projective Bezout","local coprime-tangent intersection equality"],
"new_web_source_native_bytes_not_asserted_identical_to_existing_cache":True,
"no_new_peer_NF_reports_findings_metadata_read":True,
"new_download_render_cache_write_mathcode_CAS_scan_or_author_replay":False,
"public_primary_sources":[
{"url":"https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf","scope":"page2 B4 hypothesis/(b)","native_hash_new":None},
{"url":"https://arxiv.org/pdf/0903.2016v4","scope":"Section3 local data/Lemma7/table; Section3.2 Bezout/Cor8; exact Section4/component and Theorem15/16 scope; not whole19pages","native_hash_new":None},
{"url":"https://thesis.caltech.edu/4053/01/McGuire_gm_1995.pdf","scope":"existing images29,30,31 printed24--26 COMPLETE Theorem8 proof; preceding theorem tail only","existing_native_record":rows[10]},
{"url":"https://eprint.iacr.org/2005/096","scope":"primary abstract/metadata; PDF403 and mirrorcachemiss; fullproofnotread"},
{"url":"https://arxiv.org/pdf/2602.01583","scope":"partial returned text globallytruncated; no theorem applied or imported"}]})
artifacts=[fp(P+s)for s in prose+["freeze-v1.py"]]+[inputs]
manifest=write("freeze-v1.json",{
"frozen_at_utc":datetime.now(timezone.utc).isoformat(),
"status":"candidate proof - unverified; COMPLETE constructor checkpoint",
"constructor":"/root","root_sole_NEW_constructor_excluded_from_independent_review":True,
"claims":["NF1 neighbor-Frobenius whole absolute irreducibility","NF2 complete shared-point elimination","NF3 four-bit ell7 corollary"],
"whole_obligations":36,"two_OTHER_fresh_initially_blind_ENTIRE_WHOLE_audits_required":True,
"old_accepted_bodies_context_only_not_mathematical_dependencies":True,
"mathematical_program_CAS_scan_factor_table_author_replay":False,
"method_attributed_original_thesis_special_family_not_novelty_claim":True,
"no_annual_all_four_bit_or_further_reset_spending_claim":True,
"requested_settings":{"model":"gpt-6.1-sol","reasoning":"max"},"effective_settings_readback":None,
"new_window_user_explicitly_authorized":True,"weekly_reset_unix":1792874445,
"weekly_total_ceiling_percent":90,"review_integration_reserve":True,
"administrative_command":".venv/bin/python "+P+"freeze-v1.py",
"direct_context_records_verified":len(rows),"artifacts":artifacts})
for row in rows+artifacts:verify(row)
print(json.dumps({"manifest":manifest,"main":artifacts[0],"whole_obligations":36,
"payloads":len(artifacts),"input_records_verified":len(rows),"mathematical_programs":0},indent=2))
