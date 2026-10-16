#!/usr/bin/env python3
"""Independent grid checks for the finite separation monitor."""
import argparse,collections,itertools,json,os,time
from pathlib import Path


def context(h):
 u=[];v=[]
 for t,c in enumerate(h):(u if c=='L' else v).append(t%2)
 return u,v


def min_delay(h):
 """Minimax over *strictly* upper equal-tape grid paths, independent of queues."""
 u,v=context(h);m=len(u);n=len(v);N=len(h)
 baseline=[0]
 for c in h:baseline.append(baseline[-1]+(c=='L'))
 inf=N+1
 best={(0,0):0}
 for t in range(N):
  nxt={}
  for (i,j),cost in best.items():
   for di,dj,tape,index in ((1,0,u,i),(0,1,v,j)):
    if index>=len(tape) or tape[index]!=t%2:continue
    x,y=i+di,j+dj
    gap=x-baseline[t+1]
    # The path must be strictly upper internally and rejoin at the endpoint.
    if (t+1<N and gap<=0) or (t+1==N and gap!=0):continue
    key=(x,y);value=max(cost,gap)
    nxt[key]=min(nxt.get(key,inf),value)
  best=nxt
 return best.get((m,n))


def any_bounded_bubble(h,D):
 # Independent DP along the complete tape grid with a flag recording whether
 # the path has ever been strictly above h. Zero gaps may separate bubbles.
 u,v=context(h);m=len(u);n=len(v);baseline=[0]
 for c in h:baseline.append(baseline[-1]+(c=='L'))
 possible={(0,0,False)}
 for t in range(len(h)):
  new=set()
  for i,j,flag in possible:
   for di,dj,tape,index in ((1,0,u,i),(0,1,v,j)):
    if index>=len(tape) or tape[index]!=t%2:continue
    x,y=i+di,j+dj;gap=x-baseline[t+1]
    if 0<=gap<=D:new.add((x,y,flag or gap>0))
  possible=new
 return (m,n,True) in possible


def accepts(h,data):
 q=data['start']
 for c in h:
  q=data['edges'][q][c=='R']
  if q<0:return False
 return True


def main():
 p=argparse.ArgumentParser();p.add_argument('--max-length',type=int,default=13)
 p.add_argument('--prefix',required=True);p.add_argument('--obstructions',required=True);p.add_argument('--output',required=True)
 a=p.parse_args();t=time.monotonic();assert a.max_length<=15
 automata={D:json.load(open(a.prefix+str(D)+'.json')) for D in (3,4,5,6,7)}
 rows=[]
 for n in range(a.max_length+1):
  count=0
  for letters in itertools.product('LR',repeat=n):
   h=''.join(letters)
   for D in (3,4):
    assert accepts(h,automata[D]) == (not any_bounded_bubble(h,D)),(D,h)
   count+=1
  rows.append({'length':n,'histories':count,'delays_checked':[3,4]})
  print(json.dumps({'checkpoint':rows[-1],'pid':os.getpid()}),flush=True)
 bad=json.load(open(a.obstructions))['all_minimal_forbidden_in_complete_layers']
 widths=collections.Counter();records=[]
 for row in bad:
  h=row['larger'];D=min_delay(h);assert D is not None
  widths[(len(h),D)]+=1
  for limit,data in automata.items():assert accepts(h,data)==(D>limit),(h,D,limit)
  records.append({'history':h,'length':len(h),'minimum_separation':D})
 exact=json.load(open(a.prefix+'7-exact.json'));v=exact['positive_vector'];edges=exact['edges']
 numerator=1834856083;denominator=1000000000
 slacks=[numerator*v[i]-denominator*sum(v[j] for j in row if j>=0) for i,row in enumerate(edges)]
 assert min(v)>0 and min(slacks)>0
 out={'status':'finite independent implementation evidence only; not an independent agent audit',
      'parameters':vars(a),'rows':rows,'width_distribution':[
       {'length':n,'minimum_separation':D,'count':num} for (n,D),num in sorted(widths.items())],
      'obstruction_widths':records,'upper_certificate':{'numerator':numerator,'denominator':denominator,
       'strict_integer_inequalities':len(slacks),'minimum_slack':min(slacks),'min_vector_entry':min(v)},
      'elapsed_seconds':time.monotonic()-t}
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({'finished':True,'seconds':out['elapsed_seconds'],'certificate':out['upper_certificate']}),flush=True)

if __name__=='__main__':main()
