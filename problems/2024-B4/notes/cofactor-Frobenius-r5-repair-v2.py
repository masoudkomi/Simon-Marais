#!/usr/bin/env python3
"""Versioned author text repair and byte preservation; no mathematical test."""
from pathlib import Path
import argparse,datetime,hashlib,json
ROOT=Path(__file__).resolve().parents[3]
P='problems/2024-B4/notes/cofactor-Frobenius-r5-'
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def raw(p):return (ROOT/p).read_bytes()
def obj(p):return json.loads(raw(p))
def fp(p):
 b=raw(p);return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def check(v):
 assert fp(v['path'])=={k:v[k]for k in ['path','bytes','sha256']},v['path']
 return fp(v['path'])
def put(s,v):
 with (ROOT/(P+s)).open('x')as f:
  if isinstance(v,str):f.write(v)
  else:json.dump(v,f,indent=2);f.write('\n')
MAIN_CHANGES=[
 ('Since s is odd,2^s-1 is2 modulo3. The order3 cannot divide Q-1;',
  'Since s is odd,2^s is2 modulo3, so2^s-1 is1 modulo3. The order3 cannot divide Q-1;'),
 ('need not have length1 or s; for s3 a permutation can have order3\nand the diagonal cube-root obstruction changes. No such case is\nsilently included.',
  'need not have length1 or s; for s3 a permutation can have order3\nand the off-diagonal coprimality step fails. The diagonal cube-root\nexclusion still holds at s3, since3 does not divide7. No such case is\nsilently included.')]
LOG_CHANGE=('   permutation argument and diagonal cube-root obstruction change.',
 '   permutation argument fails; the diagonal cube-root exclusion still holds.')
HEADER='''> Author repair v2, 18 October2026 UTC: candidate proof - unverified
> pending BOTH affected reaudits. Corrects the odd-s residue from2 to1
> modulo3, and assigns the s3 failure to the off-diagonal coprimality
> step; its diagonal exclusion still holds. R1 N1/N2 and R2 N1 supplied
> these corrective observations after BOTH entire blind audits froze.
> No theorem/domain/threshold is strengthened. All original bytes remain.

'''
def repair():
 guards=[]
 for name in [P+'freeze-v1.json']+['problems/2024-B4/reviews/cofactor-Frobenius-r5-review-'+str(i)+'-manifest-v1.json'for i in [1,2]]:
  m=obj(name);guards+=[fp(name)]+[check(v)for v in m['artifacts']]
 assert fp(P+'candidate-v1.md')['sha256']=='ff29bb1757d3f24229cb138bdfcca02b4d45c457200afc2ecc78104918c823ee'
 body=raw(P+'candidate-v1.md').decode()
 for old,new in MAIN_CHANGES:
  assert body.count(old)==1;body=body.replace(old,new)
 log=raw(P+'failures-worklog-v1.md').decode();old,new=LOG_CHANGE
 assert log.count(old)==1;log=log.replace(old,new)
 put('candidate-v2.md',HEADER+body)
 put('failures-worklog-v2.md',HEADER+log)
 note='''# Versioned author repair after BOTH full R5 audits

18 October2026 UTC. Root sole constructor, excluded from independent
review. Both ENTIRE initially blind OTHER whole audits reconstructed
all32 obligations, found no substantive theorem defect, and flagged
literal explanatory errors. Root fully read BOTH reports/all64 ledger
rows/issues/sources/logs/code/ALLmetadata before this repair.

R1 N1 and R2 N1: for odd s, 2^s-1 is1 modulo3, not2. The required
nondivisibility is unchanged. R1 N2: at s3 the diagonal calculation
still works, while the off-diagonal coprimality step fails. The s3
extension was already excluded. The old failed-extension log's same
sentence is corrected in a NEW log copy. No old file is overwritten.

The full NEW main differs only by a visible repair header and these two
exact text replacements. The NEW failures/worklog differs only by that
header and its one corresponding sentence. All32 original obligations,
accepted CG/R4 inputs, theorem domains, projective steps, divisibilities,
sign-sensitive maximum and378+2/3 threshold are unchanged. Elementary
hand arithmetic confirms both corrections; no program proves the math.

BOTH original OTHER reviewers must check every affected passage and its
downstream orbit/threshold consequences, versioned byte diff, all new
companions/code/metadata and old preservation before scoped acceptance.
The initial audits have already frozen; affected reaudits may know their
own prior findings. Their new reports must each finish before new peer
repair findings are exchanged. Root cannot promote merely from agreement.

No new primary theorem, code/test/scan, charge/contact/bypass, stronger
prime-s/s3/k1/general-annual result, source-overlap decision or novelty
claim. Férard2017's operative body remains unread. Exact older source
limits remain the original source record. This is a corrected presentation
of the same partial theorem, pending both affected reaudits.
'''
 put('repair-record-v2.md',note)
 for v in guards:check(v)
 put('repair-freeze-v2.json',dict(frozen_at_utc=now(),status='author repair v2 - unverified pending BOTH affected reaudits',
  constructor='/root',constructor_excluded=True,both_original_entire_initials_confirmed_before_findings=True,
  original_whole_obligations=32,claims_unchanged=['R5A','R5B','R5C','R5D'],
  literal_congruence_corrected=True,s3_explanation_and_failure_log_corrected=True,
  full_affected_reaudits_required_from_both_original_OTHER_reviewers=True,
  new_mathematical_theorem_program_scan_or_primary_import=False,
  old_current_guards=guards,old_guard_paths=len({v['path']for v in guards}),
  exact_replacements=dict(main=MAIN_CHANGES,log=LOG_CHANGE),
  artifacts=[fp(P+s)for s in ['candidate-v2.md','failures-worklog-v2.md','repair-record-v2.md','repair-v2.py']]))
 verify()
def verify():
 v=obj(P+'repair-freeze-v2.json')
 for row in v['old_current_guards']+v['artifacts']:check(row)
 b=raw(P+'candidate-v1.md').decode()
 for old,new in MAIN_CHANGES:b=b.replace(old,new)
 assert raw(P+'candidate-v2.md').decode()==HEADER+b
 b=raw(P+'failures-worklog-v1.md').decode().replace(*LOG_CHANGE)
 assert raw(P+'failures-worklog-v2.md').decode()==HEADER+b
 print(json.dumps(dict(postverified=True,administrative_only=True,old_paths=v['old_guard_paths'],
  main=fp(P+'candidate-v2.md'),manifest=fp(P+'repair-freeze-v2.json'),new_files=5)))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('operation',choices=['repair','verify']);{'repair':repair,'verify':verify}[p.parse_args().operation]()
