#!/usr/bin/env python3
"""Independent J16 reconstruction. Written before constructor code/data access.
Only stdlib. Does not import constructor or reviewer helpers.
"""
import argparse
import collections
import fractions
import gzip
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import sys
import time

P = 19
C = tuple(tuple(math.comb(j, h) for h in range(j+1)) for j in range(21))
BETA = tuple(0 if j < 2 or j > 18 else C[20][j]//P for j in range(21))
HERE = Path(__file__).resolve().parent
BASE = HERE / 'J16-digits-review-2'

def pack(x):
    return (json.dumps(x, separators=(',', ':'))+'\n').encode()

def save(name, obj):
    Path(str(BASE)+'-'+name+'.json').write_text(json.dumps(obj, indent=2)+'\n')

def valuation(x):
    assert x
    n = 0
    while x % P == 0:
        n += 1
        x //= P
    return n

def constants(mask):
    a = [1, -1]
    for j in range(2, 19):
        a.append(-sum(C[j][h]*a[h] for h in range(j)) if mask & (1<<(j-2)) else 0)
    return a

def mask_cover():
    all_masks, j16 = [], []
    histogram = collections.Counter()
    for mask in range(1<<17):
        a = [1, P-1]
        for j in range(2, 19):
            a.append((-sum(C[j][h]*a[h] for h in range(j))) % P if mask & (1<<(j-2)) else 0)
        if (-1+sum(BETA[j]*a[j] for j in range(2,19))) % P:
            continue
        J = max(j for j in range(2, 19) if a[j] % P)
        if J >= 17:
            continue
        if J == 16 and not mask & ((1<<16)|(1<<15)):
            continue
        if J == 15 and not mask & ((1<<16)|(1<<15)|(1<<14)):
            continue
        all_masks.append(mask)
        histogram[J] += 1
        if J == 16:
            j16.append(mask)
    assert len(all_masks) == 772 and len(j16) == 88
    return all_masks, j16, dict(histogram)

def linear(mask, umask, vmask, a0=None):
    if a0 is None:
        a0 = constants(mask)
    A, B = [0,0], [0,0]
    for j in range(2, 19):
        bit = 1<<(j-2)
        if mask & bit:
            A.append(-sum(C[j][h]*A[h] for h in range(j)) % P)
            B.append(-sum(C[j][h]*B[h] for h in range(j)) % P)
        else:
            z = -j*a0[j-1] % P
            A.append(z if umask & bit else 0)
            B.append(z if vmask & bit else 0)
    c4 = BETA[16]*a0[16] % P
    return ((sum(BETA[j]*A[j] for j in range(2,19)) % P,
             sum(BETA[j]*B[j] for j in range(2,19)) % P),
            (A[18], B[18]),
            ((BETA[17]*A[17]+c4) % P, (BETA[17]*B[17]+c4) % P))

def assign(positions):
    for labels in itertools.product(range(3), repeat=len(positions)):
        u = v = 0
        for j, z in zip(positions, labels):
            if z == 1:
                u |= 1<<(j-2)
            elif z == 2:
                v |= 1<<(j-2)
        yield u, v

def projected_cover(masks):
    branches = []
    bymask = {}
    checks = 0
    for mask in masks:
        a0 = constants(mask)
        q0 = -1+sum(BETA[j]*a0[j] for j in range(2,19))
        assert q0 != 0
        active = [j for j in range(2,19) if not mask & (1<<(j-2)) and a0[j-1] % P]
        inactive = [j for j in range(2,19) if not mask & (1<<(j-2)) and not a0[j-1] % P]
        seen = set()
        before = len(branches)
        for um, vm in assign(active):
            M = linear(mask, um, vm, a0)
            for nu in range(1, valuation(q0)+1):
                checks += 1
                q = P**nu
                if a0[17] % q or a0[18] % q:
                    continue
                constant = (q0//q % P, a0[18]//q % P, BETA[17]*(a0[17]//q) % P)
                for X in range(P):
                    for Y in range(P):
                        if X == Y == 0:
                            continue
                        if any((constant[i]+M[i][0]*X+M[i][1]*Y) % P for i in range(3)):
                            continue
                        h2, h3 = bool(mask & (1<<16)), bool(mask & (1<<15))
                        if h2 != h3:
                            if not X or not Y:
                                continue
                            if h2 and ((X+Y)*(3*X-Y)*(3*Y-X)) % P:
                                continue
                            if h3 and ((3*X-2*Y)*(3*Y-2*X)) % P:
                                continue
                        key = (mask, um, vm, nu, X, Y)
                        assert key not in seen
                        seen.add(key)
                        branches.append((key, M, tuple(inactive)))
        bymask[mask] = {'q0':q0, 'nu_bound':valuation(q0), 'active':active, 'inactive':inactive,
                        'projected_branches':len(branches)-before}
    return branches, bymask, checks

def families(branches):
    for key, M, inactive in branches:
        mask, um, vm, nu, X, Y = key
        for uextra, vextra in assign(inactive):
            yield (mask, um|uextra, vm|vextra, nu, X, Y), M

def coefficients(key, r):
    mask, um, vm, nu, X, Y = key
    q = P**nu
    mod = q*(P**r)
    up, vp = [1], [1]
    emax = min(18, (nu+r-1)//nu)
    u, v = q*X % mod, q*Y % mod
    for e in range(1, emax+1):
        up.append(up[-1]*u % mod)
        vp.append(vp[-1]*v % mod)
    a = [1, mod-1]
    for j in range(2, 19):
        bit = 1<<(j-2)
        if mask & bit:
            a.append(-sum(C[j][h]*a[h] for h in range(j)) % mod)
        elif (um|vm) & bit:
            powers = up if um & bit else vp
            a.append(-sum(C[j][e]*a[j-e]*powers[e] for e in range(1,min(j,emax)+1)) % mod)
        else:
            a.append(0)
    return a

def evaluate(key, r, return_a=False):
    """Full monic-quadratic remainder Horner, no divided h recurrence."""
    nu, X, Y = key[3:]
    q, pr = P**nu, P**r
    D = P*q*pr
    a = coefficients(key, r)
    pvalue = (-1+sum(BETA[j]*a[j] for j in range(2,19))) % (q*pr)
    assert pvalue % q == 0
    u, v = q*X % D, q*Y % D
    s, t = (u+v) % D, u*v % D
    ordinary_descending = [1, -20]+[C[20][j]*a[j] for j in range(2,19)]
    R0 = R1 = 0
    for c in ordinary_descending:
        R0, R1 = (c-t*R1) % D, (R0+s*R1) % D
    assert R0 % (P*q) == 0 and R1 % (P*q) == 0
    E = (pvalue//q, (R0//(P*q))*pow(10,-1,pr) % pr, R1//(P*q))
    return (E,a) if return_a else E

SOLVERS = {}
VALIDATED = set()

def solver(M):
    if M in SOLVERS:
        return SOLVERS[M]
    for i,j in ((0,1),(0,2),(1,2)):
        a,b = M[i]; c,d = M[j]
        det = (a*d-b*c) % P
        if det:
            inv = pow(det,-1,P)
            def solve(rhs, i=i,j=j,a=a,b=b,c=c,d=d,inv=inv):
                x = (d*rhs[i]-b*rhs[j])*inv % P
                y = (a*rhs[j]-c*rhs[i])*inv % P
                return [(x,y)] if all((row[0]*x+row[1]*y-r) % P == 0 for row,r in zip(M,rhs)) else []
            ans = 2, solve
            break
    else:
        nz = next((i for i,row in enumerate(M) if row != (0,0)), None)
        if nz is None:
            ans = 0, lambda rhs: list(itertools.product(range(P), repeat=2)) if not any(rhs) else []
        else:
            a,b = M[nz]
            if a:
                ia = pow(a,-1,P)
                def solve(rhs,a=a,b=b,ia=ia,nz=nz):
                    x0 = rhs[nz]*ia % P
                    if any((row[0]*x0-r) % P for row,r in zip(M,rhs)):
                        return []
                    return sorted(((rhs[nz]-b*y)*ia % P,y) for y in range(P))
            else:
                ib = pow(b,-1,P)
                def solve(rhs,ib=ib,nz=nz):
                    y0 = rhs[nz]*ib % P
                    if any((row[1]*y0-r) % P for row,r in zip(M,rhs)):
                        return []
                    return [(x,y0) for x in range(P)]
            ans = 1, solve
    SOLVERS[M] = ans
    # Enumerate every digit pair once for every encountered matrix, and
    # validate all nonempty fibers. Solving an invertible minor or one
    # nonzero row with consistency check proves empty-fiber completeness.
    all_images = collections.defaultdict(list)
    for x,y in itertools.product(range(P), repeat=2):
        rhs = tuple((row[0]*x+row[1]*y) % P for row in M)
        all_images[rhs].append((x,y))
    rank, solve = ans
    assert len(all_images) == P**rank
    for rhs,pairs in all_images.items():
        assert solve(rhs) == pairs
    VALIDATED.add(M)
    return ans

def exact_state(key, k, M):
    """Untruncated ordinary Hasse/Horner construction; used on ALL late states."""
    mask, um, vm, nu, X, Y = key
    q = P**nu
    u,v = q*X,q*Y
    a = [1,-1]
    for j in range(2,19):
        bit = 1<<(j-2)
        w = 1 if mask & bit else (u if um & bit else v if vm & bit else 0)
        val = 0
        # Horner in descending powers, including the final zero a_j.
        for h in range(j):
            val = val*w+C[j][h]*a[h]
        a.append(-val*w)
    coeffs = [1,-20]+[C[20][j]*a[j] for j in range(2,19)]
    R0=R1=0
    for c in coeffs:
        R0,R1=c-u*v*R1,R0+(u+v)*R1
    P0 = -1+sum(BETA[j]*a[j] for j in range(2,19))
    E = [fractions.Fraction(P0,q), fractions.Fraction(R0,P*q*10),fractions.Fraction(R1,P*q)]
    pr=P**(k+1)
    rem=tuple(z.numerator*pow(z.denominator,-1,pr) % pr for z in E)
    assert rem == evaluate(key,k+1)
    assert all(z.denominator % P for z in E)
    assert all(z % P**k == 0 for z in rem)
    c=tuple(z//(P**k) % P for z in rem)
    rank, solve=solver(M)
    digits=solve(tuple(-z % P for z in c))
    brute=[(x,y) for x,y in itertools.product(range(P),repeat=2)
           if all((M[i][0]*x+M[i][1]*y+c[i]) % P==0 for i in range(3))]
    assert digits==brute
    det=lambda a,b:(a[0]*b[1]-a[1]*b[0]) % P
    lam=(det(M[1],M[2]),det(M[2],M[0]),det(M[0],M[1]))
    assert all(sum(lam[i]*M[i][j] for i in range(3)) % P==0 for j in range(2))
    obstruction=sum(lam[i]*c[i] for i in range(3)) % P
    if rank==2:
        assert any(lam) and bool(obstruction)==(not digits)
    return {'precision':k,'key':key,'a':a,'R':[R0,R1],
            'E':[[z.numerator,z.denominator] for z in E],'M':M,'c':c,
            'rank':rank,'lambda':lam,'obstruction':obstruction,'digits':digits}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--benchmark',action='store_true')
    ap.add_argument('--leading-only',action='store_true')
    args=ap.parse_args()
    mode='benchmark' if args.benchmark else 'full'
    start=time.monotonic()
    all_masks,masks,hist=mask_cover()
    branches,bymask,tests=projected_cover(masks)
    expanded=sum(3**len(inact) for _,_,inact in branches)
    summary={'mode':mode,'pid':os.getpid(),'python':sys.version,
             'mask_histogram':hist,'accepted_masks':all_masks,'j16_masks':masks,
             'leading_masks':[m for m in masks if bymask[m]['projected_branches']],
             'projected_tests':tests,'projected_count':len(branches),
             'full_key_count':expanded,'by_mask':bymask,
             'branches':[[list(key),list(inact)] for key,_,inact in branches]}
    save(mode+'-leading',summary)
    print(json.dumps({'event':'leading','seconds':time.monotonic()-start,
                     'tests':tests,'branches':len(branches),'expanded':expanded}),flush=True)
    if args.leading_only:
        return
    stream=gzip.open(str(BASE)+'-'+mode+'-certificates.jsonl.gz','wb',compresslevel=1)
    late=[]
    stats=[]
    current=families(branches)
    seen_mask=None
    seen=set()
    for k in range(1,6):
        next_nodes=[]
        ranks=collections.Counter(); consistent=collections.Counter()
        parentmasks=collections.Counter(); childmasks=collections.Counter()
        t1=t1pass=0
        h=hashlib.sha256()
        count=0
        for key,M in current:
            if args.benchmark and k==1 and count>=8192:
                break
            if key[0]!=seen_mask:
                seen_mask=key[0];seen.clear()
            assert key not in seen
            seen.add(key)
            E,a=evaluate(key,k+1,True)
            pk=P**k
            assert all(z % pk==0 for z in E)
            c=tuple(z//pk % P for z in E)
            rank,solve=solver(M)
            digits=solve(tuple(-z % P for z in c))
            omit=not key[1] or not key[2]
            if k==1:
                t1+=omit
                t1pass+=bool(digits) and omit
            if k>=4:
                late.append(exact_state(key,k,M))
            row=[k,list(key),list(c),rank,int(omit),digits]
            line=pack(row)
            stream.write(line);h.update(line)
            ranks[rank]+=1
            consistent[(rank,bool(digits))]+=1
            parentmasks[key[0]]+=1
            if not omit:
                for dx,dy in digits:
                    child=key[:4]+(key[4]+pk*dx,key[5]+pk*dy)
                    # A direct re-evaluation is necessary for every child.
                    assert all(z==0 for z in evaluate(child,k+1))
                    next_nodes.append((child,M));childmasks[child[0]]+=1
            count+=1
            if count%16384==0:
                stream.flush()
                print(json.dumps({'event':'checkpoint','precision':k,'count':count,
                                  'children':len(next_nodes),'seconds':time.monotonic()-start}),flush=True)
        stream.flush()
        stat={'precision':k,'parents':count,'children':len(next_nodes),
              'ranks':dict(ranks),'systems':{str(t):n for t,n in consistent.items()},
              'T1_omitted':t1,'T1_omitted_consistent':t1pass,
              'parent_masks':dict(parentmasks),'child_masks':dict(childmasks),
              'row_sha256':h.hexdigest()}
        stats.append(stat)
        save(mode+'-checkpoint',{'layers':stats,'seconds':time.monotonic()-start})
        print(json.dumps({'event':'layer','statistics':stat,'seconds':time.monotonic()-start}),flush=True)
        if args.benchmark or not next_nodes:
            break
        assert len(next_nodes)<=1000000
        if k>=3:
            assert all(solver(M)[0]==2 for _,M in next_nodes)
            assert len(next_nodes)<=90
        next_nodes.sort(key=lambda t:t[0])
        current=iter(next_nodes)
        seen_mask=None;seen.clear()
    stream.close()
    summary.update({'layers':stats,'matrices_bruteforce_checked':len(VALIDATED),
                    'late_exact_states':late,'seconds':time.monotonic()-start,
                    'complete':not args.benchmark and stats[-1]['children']==0})
    save(mode+'-result',summary)
    print(json.dumps({'event':'finished','seconds':summary['seconds'],'complete':summary['complete']}),flush=True)

if __name__=='__main__':
    main()
