import json
O={"1":{0}}
for k in range(8):
 for w,marks in sorted(O.items()):
  if len(marks)>1:
   lo,hi=min(marks),max(marks)
   missing=[i for i in range(lo+1,hi) if w[i]=="1" and i not in marks]
   if missing:
    print(json.dumps({"status":"counterexample_found","k":k,"length":len(w),"word":w,"zero_based_viable_marks":sorted(marks),"missing_internal_one_marks":missing,"claim":"viable marks form an interval in the order of one positions"}));raise SystemExit
 if k==7:break
 P={}
 for w,marks in O.items():
  for v,shift in [("10"+w,2),("1"+w+"0",1),("0"+w+"1",1),(w+"01",0)]:
   P.setdefault(v,set()).update(i+shift for i in marks)
 O=P
print(json.dumps({"status":"no_counterexample_in_bounded_domain","max_length":15,"last_distinct_words":len(O),"no_general_interval_theorem":True}))
