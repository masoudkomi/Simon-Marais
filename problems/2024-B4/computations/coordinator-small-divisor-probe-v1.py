#!/usr/bin/env python3
"""Bounded exploratory fixed-divisor Cartier graphs. Not independent reviews."""
from pathlib import Path
import hashlib,json,os,sys,time,subprocess,platform

HERE=Path(__file__).resolve().parent
MODELS={
 'phi7':{'bounds':(0,1),'K':[(0,0),(2,0),(3,1),(4,0)],'P':[(0,0),(1,0),(2,0)],'formal_divisor':'d+q^2; invert q; b=u/q^3'},
 'phi9':{'bounds':(0,2),'K':[(0,0),(2,0),(3,0),(4,2)],'P':[(0,0),(1,0),(2,1)],'formal_divisor':'u+q^3; invert q; b=d/q^2'},
 'phi11':{'bounds':(0,2),'K':[(0,0),(2,0),(3,0),(3,1),(3,2),(4,2)],'P':[(0,0),(1,0),(2,1)],'formal_divisor':'q*u+q^4+q^2*d+d^2; invert q; b=d/q^2'},
}
def rref(rows):
 piv={}
 for row in rows:
  for k in sorted(piv,reverse=True):
   if row>>k&1: row^=piv[k]
  if row:
   k=row.bit_length()-1
   for j in list(piv):
    if piv[j]>>k&1:piv[j]^=row
   piv[k]=row
 return tuple(piv[k] for k in sorted(piv,reverse=True))
def apply(row,cols):
 ans=0
 while row:
  bit=row&-row;ans^=cols[bit.bit_length()-1];row^=bit
 return ans
def graph(name,model):
 start=time.monotonic();lo,hi=model['bounds']
 mons=[(i,h) for i in range(4) for h in range(lo,hi+1)];idx={v:i for i,v in enumerate(mons)}
 def encode(terms):
  ans=0
  for term in terms:ans^=1<<idx[term]
  return ans
 ops={}
 for r in range(2):
  for t in range(2):
   cols=[]
   for i,h in mons:
    terms=[]
    for a,b in model['K']:
     if (i+a)%2==r and (h+b)%2==t:
      v=((i+a-r)//2,(h+b-t)//2);assert v in idx;terms.append(v)
    cols.append(encode(terms))
   ops[r,t]=cols
 states=[rref([encode(model['P'])])];lookup={states[0]:0};edges=[];complete=True;reason='closed'
 for cursor in range(10000):
  if cursor>=len(states):break
  if time.monotonic()-start>7:complete=False;reason='7-second cap';break
  successors=[]
  for r in range(2):
   state=rref(apply(row,ops[r,t]) for row in states[cursor] for t in range(2))
   if state not in lookup:
    if len(states)==10000:complete=False;reason='10000-state cap';break
    lookup[state]=len(states);states.append(state)
   successors.append(lookup[state])
  if not complete:break
  edges.append(successors)
 else:complete=False;reason='processed-state cap'
 mask=encode((i,h) for i,h in mons if i==0)
 accepts=[not any(row&mask for row in state) for state in states]
 result={'model':name,'normalization':model,'status':'exploratory computational evidence; algebraic bridge and graph not independently reviewed','complete':complete,'reason':reason,'states':len(states),'edges':len(edges)*2,'accepting_count':sum(accepts),'basis_monomials':mons,'operators':{f'{r}{t}':cols for (r,t),cols in ops.items()},'state_bases':states,'transitions':edges,'accepting':accepts,'elapsed_seconds':time.monotonic()-start}
 if complete:
  colors=[int(a) for a in accepts]
  while True:
   ids={};new=[]
   for a,e in zip(accepts,edges):
    key=(a,colors[e[0]],colors[e[1]])
    if key not in ids:ids[key]=len(ids)
    new.append(ids[key])
   if new==colors:break
   colors=new
  classes=[]
  for c in range(max(colors)+1):
   members=[i for i,v in enumerate(colors) if v==c];s=members[0]
   classes.append({'class':c,'members':members,'accepting':accepts[s],'next':[colors[x] for x in edges[s]]})
  result['quotient_classes']=classes;result['initial_class']=colors[0]
  zeros=[]
  for j in range(8192):
   s=0;n=j
   while n:s=edges[s][n&1];n>>=1
   if accepts[s]:zeros.append(j)
  result['accepted_indices_below8192']=zeros
 return result
def child():
 print(json.dumps({'pid':os.getpid(),'python':platform.python_version(),'limits':'7s per model,10000 states; external25s','scope':'one fixed divisor at a time, no full reducibility claim'}),flush=True)
 results=[]
 for name,model in MODELS.items():
  ans=graph(name,model);results.append(ans)
  print(json.dumps({k:ans[k] for k in ['model','complete','states','edges','accepting_count','elapsed_seconds']}),flush=True)
  (HERE/'coordinator-small-divisor-probe-v1.json').write_text(json.dumps(results,indent=2)+'\n')
  if ans['complete']:print(json.dumps({'quotient_size':len(ans['quotient_classes']),'quotient':ans['quotient_classes'],'accepted_indices_below8192':ans['accepted_indices_below8192']}),flush=True)
def supervisor():
 out=HERE/'coordinator-small-divisor-probe-v1-output.txt';err=HERE/'coordinator-small-divisor-probe-v1-stderr.txt';job=HERE/'coordinator-small-divisor-probe-v1-job.json';started=time.monotonic()
 cmd=[sys.executable,'-u',str(Path(__file__).resolve()),'--child'];record={'command':cmd,'timeout_seconds':25,'status':'launching','dependencies':'Python standard library only'}
 with out.open('w') as f,err.open('w') as e:
  p=subprocess.Popen(cmd,stdout=f,stderr=e);record.update(pid=p.pid,status='running');job.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record),flush=True)
  try:p.wait(timeout=25);record['status']='completed' if p.returncode==0 else 'failed'
  except subprocess.TimeoutExpired:p.kill();p.wait();record['status']='timeout; identified child killed'
  record.update(return_code=p.returncode,elapsed_seconds=time.monotonic()-started)
 for path in [Path(__file__),out,err,HERE/'coordinator-small-divisor-probe-v1.json']:
  if path.exists():record.setdefault('sha256',{})[path.name]=hashlib.sha256(path.read_bytes()).hexdigest()
 job.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record),flush=True)
if __name__=='__main__':
 if '--child' in sys.argv:child()
 else:supervisor()
