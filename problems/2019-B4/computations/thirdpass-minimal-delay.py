#!/usr/bin/env python3
"""Finite DFA for minimal rejected histories of a supplied factorial DFA."""
import argparse,json,time,os

def minimal_bad(edges,start,cap):
 # state (-1,-1) is an initial state before the first letter; (-2,-2)
 # is the accepting terminal, which permits no continuation.
 states=[(-1,-1),(-2,-2)];ids={x:i for i,x in enumerate(states)};trans=[]
 for i,(q,r) in enumerate(states):
  row=[]
  for c in (0,1):
   if i==1: row.append(-1);continue
   if i==0:
    q1,r1=edges[start][c],start
   else:q1,r1=edges[q][c],edges[r][c]
   if r1<0:row.append(-1);continue
   if q1<0:row.append(1);continue
   pair=(q1,r1)
   if pair not in ids:
    if len(states)>=cap:return None,{'complete':False,'states':len(states),'cap':cap}
    ids[pair]=len(states);states.append(pair)
   row.append(ids[pair])
  trans.append(row)
 return (trans,0,1,states),{'complete':True,'states':len(states)}

def coefficients(edges,start,terminal,length):
 v=[0]*len(edges);v[start]=1;ans=[]
 for n in range(length+1):
  ans.append(v[terminal]);w=[0]*len(edges)
  for i,row in enumerate(edges):
   for j in row:
    if j>=0:w[j]+=v[i]
  v=w
 return ans

def main():
 p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True)
 p.add_argument('--state-cap',type=int,default=100000);p.add_argument('--length',type=int,default=80);a=p.parse_args()
 start=time.monotonic();d=json.load(open(a.input));result,meta=minimal_bad(d['edges'],d['start'],a.state_cap)
 print(json.dumps({'checkpoint':meta,'pid':os.getpid()}),flush=True)
 out={'status':'finite evidence; all new unrestricted interpretations pending review','input':a.input,'construction':meta}
 if result:
  edges,s,t,states=result;f=coefficients(edges,s,t,a.length)
  c=d['counts'];h=[0]*len(c)
  for n in range(1,len(c)):h[n]=2*c[n-1]-c[n]-sum(h[j]*c[n-j] for j in range(1,n))
  assert h==f[:len(h)]
  out.update(edges=edges,start=s,terminal=t,states=states,coefficients=f,renewal_coefficients_match=True)
 out['elapsed_seconds']=time.monotonic()-start
 with open(a.output,'w') as file:json.dump(out,file,indent=2);file.write('\n')
 print(json.dumps({'finished':True,'seconds':out['elapsed_seconds'],'output':a.output}),flush=True)
if __name__=='__main__':main()
