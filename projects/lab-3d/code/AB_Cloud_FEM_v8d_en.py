"""
AB_Cloud_FEM_v8d — English Version
============================================================

FEM on Klein quartic with gauge field and Neumann boundary conditions. Uses natural Neumann BC instead of erroneous slave-master identification.

This is the English translation of AB_Cloud_FEM_v8d.py.
Russian comments in the code body are preserved for reference.

Original file: AB_Cloud_FEM_v8d.py
"""

import numpy as np
from scipy.linalg import eigh, norm, svd
from collections import deque
import time

PI = np.pi; SQRT7 = np.sqrt(7.0)
ALPHA = (-1.0 + SQRT7*1j)/2.0; ALPHA_BAR = (-1.0 - SQRT7*1j)/2.0
CHAR_TABLE = {
    '1a': np.array([1,1,1,1,1,1], dtype=complex),
    '3a': np.array([3,-1,0,1,ALPHA,ALPHA_BAR], dtype=complex),
    '3b': np.array([3,-1,0,1,ALPHA_BAR,ALPHA], dtype=complex),
    '6a': np.array([6,2,0,0,-1,-1], dtype=complex),
    '7a': np.array([7,-1,1,-1,0,0], dtype=complex),
    '8a': np.array([8,0,-1,0,1,1], dtype=complex),
}
REPS = ['1a','3a','3b','6a','7a','8a']
COOK = {'1a':0.0,'3a':3.577,'3b':None,'6a':10.869,'7a':6.6225,'8a':2.6779}

# === PSL(2,7) ===
def mm(A,B): return np.array([[(A[0,0]*B[0,0]+A[0,1]*B[1,0])%7,(A[0,0]*B[0,1]+A[0,1]*B[1,1])%7],[(A[1,0]*B[0,0]+A[1,1]*B[1,0])%7,(A[1,0]*B[0,1]+A[1,1]*B[1,1])%7]],dtype=int)
def minv(A): d=(A[0,0]*A[1,1]-A[0,1]*A[1,0])%7; di=pow(int(d),-1,7); return np.array([[A[1,1]*di%7,(-A[0,1]*di)%7],[(-A[1,0]*di)%7,A[0,0]*di%7]],dtype=int)
def mk(M): return tuple(M.flatten()%7)
def nk(M): return tuple(((-M)%7).flatten())
def eq(A,B): return mk(A)==mk(B) or nk(A)==mk(B)
def order_psl(M):
    I=np.array([[1,0],[0,1]],dtype=int)
    if eq(M,I): return 1
    Mp=M.copy()
    for k in range(2,8):
        Mp=mm(Mp,M)
        if eq(Mp,I): return k
    return -1
def gen_psl27():
    s=np.array([[0,1],[6,0]],dtype=int); u=np.array([[0,1],[6,1]],dtype=int)
    I=np.array([[1,0],[0,1]],dtype=int)
    elems=[I]; seen={mk(I)}; q=deque([0])
    while q:
        idx=q.popleft(); g=elems[idx]
        for gen in [s,u]:
            ng=mm(gen,g); k,nk_=mk(ng),nk(ng)
            if k not in seen and nk_ not in seen:
                seen.add(k); elems.append(ng); q.append(len(elems)-1)
    assert len(elems)==168; return elems,s,u
def classify(elems,s_mat,u_mat):
    su=mm(s_mat,u_mat); su_pows=[su.copy()]
    for k in range(1,7): su_pows.append(mm(su_pows[-1],su))
    classes=[]
    for M in elems:
        o=order_psl(M)
        if o==1: classes.append(0)
        elif o==2: classes.append(1)
        elif o==3: classes.append(2)
        elif o==4: classes.append(3)
        elif o==7:
            found=False
            for h in elems:
                hinv=minv(h); conj=mm(mm(h,M),hinv)
                for ki in range(6):
                    if eq(conj,su_pows[ki]):
                        classes.append(4 if ki+1 in [1,2,4] else 5); found=True; break
                if found: break
            if not found: classes.append(-1)
        else: classes.append(-1)
    return classes

# === REPRESENTATIONS ===
def build_reps(s_mat,u_mat,elems):
    reps={}
    reps['1a']=(np.array([[1.0]]),np.array([[1.0]]),1)
    def psl_action(M,z):
        a,b,c,d=int(M[0,0]),int(M[0,1]),int(M[1,0]),int(M[1,1])
        if z==7: return 7 if c==0 else (a*pow(c,-1,7))%7
        else: num=(a*z+b)%7; den=(c*z+d)%7; return 7 if den==0 else (num*pow(den,-1,7))%7
    sp=[psl_action(s_mat,z) for z in range(8)]; up=[psl_action(u_mat,z) for z in range(8)]
    Ps=np.zeros((8,8)); Pu=np.zeros((8,8))
    for i in range(8): Ps[i,sp[i]]=1; Pu[i,up[i]]=1
    v1=np.ones(8)/np.sqrt(8); Q=np.eye(8)-np.outer(v1,v1)
    U7,_,_=svd(Q); B7=U7[:,:7]
    reps['7a']=(B7.T@Ps@B7, B7.T@Pu@B7, 7)
    
    # Extract 3a from 7a⊗7a
    rho7_s,rho7_u,_=reps['7a']
    classes=classify(elems,s_mat,u_mat)
    rho7_all={}
    for g in elems:
        perm=[psl_action(g,z) for z in range(8)]; P=np.zeros((8,8))
        for i in range(8): P[i,perm[i]]=1
        rho7_all[mk(g)]=B7.T@P@B7
    
    Rs49=np.kron(rho7_s,rho7_s); Ru49=np.kron(rho7_u,rho7_u)
    chi_3a=CHAR_TABLE['3a']; d3=3
    rng=np.random.RandomState(42)
    v=rng.randn(49)+1j*rng.randn(49); Pv=np.zeros(49,dtype=complex)
    for i,g in enumerate(elems):
        cc=classes[i]; chi_bar=np.conj(chi_3a[cc])
        Rg=np.kron(rho7_all.get(mk(g),rho7_s),rho7_all.get(mk(g),rho7_s))
        Pv+=chi_bar*(Rg@v)
    Pv*=d3/168.0
    basis=[Pv.copy()]
    for trial in range(200):
        nv=Rs49@basis[-1] if trial%2==0 else Ru49@basis[-1]
        for b in basis: nv-=np.vdot(b,nv)/max(np.vdot(b,b),1e-30)*b
        nn=norm(nv)
        if nn>1e-8: basis.append(nv/nn); 
        if len(basis)>=9: break
    B=np.array(basis).T; U,S,_=svd(B,full_matrices=False)
    mask=S>1e-6; Ub=U[:,mask]
    Rs_V=Ub.conj().T@Rs49@Ub; Ru_V=Ub.conj().T@Ru49@Ub
    w=rng.randn(Ub.shape[1])+1j*rng.randn(Ub.shape[1]); w/=norm(w)
    inv_b=[w.copy()]; q=deque([0]); done=set()
    while q and len(inv_b)<3:
        idx=q.popleft()
        if idx in done: continue
        done.add(idx); b=inv_b[idx]
        for R in [Rs_V,Ru_V]:
            nb=R@b
            for ex in inv_b: nb-=np.vdot(ex,nb)*ex
            nn=norm(nb)
            if nn>1e-10 and len(inv_b)<3: inv_b.append(nb/nn); q.append(len(inv_b)-1)
    if len(inv_b)>=3:
        Q3=np.array(inv_b[:3]).T
        rho_3a_s=Q3.conj().T@Rs_V@Q3; rho_3a_u=Q3.conj().T@Ru_V@Q3
        reps['3a']=(rho_3a_s,rho_3a_u,3)
        reps['3b']=(rho_3a_s.conj(),rho_3a_u.conj(),3)
    return reps

# === MESH ===
def create_mesh(level):
    a,b,g=PI/2,PI/3,PI/7
    ca,sa=np.cos(a),np.sin(a); cb,sb=np.cos(b),np.sin(b); cc,sc=np.cos(g),np.sin(g)
    cha=(cb*cc+ca)/(sb*sc); chb=(ca*cc+cb)/(sa*sc); chc=(ca*cb+cc)/(sa*sb)
    vA=np.array([0.,0.]); vB=np.array([np.tanh(np.arccosh(chc)/2),0.])
    vC=np.array([0.,np.tanh(np.arccosh(chb)/2)])
    ns=2**level; verts,elems_m,bdy,ic,bary=[],[],[],[],{}
    idx=0
    for i in range(ns+1):
        for j in range(ns+1-i):
            k=ns-i-j; u,v,w=i/ns,j/ns,k/ns
            x=u*vA[0]+v*vB[0]+w*vC[0]; y=u*vA[1]+v*vB[1]+w*vC[1]
            r2=x*x+y*y
            if r2>=0.999: s=0.998/np.sqrt(r2); x*=s; y*=s
            verts.append([x,y]); bary[(i,j,k)]=idx
            bd=0
            if k==0: bd=3
            if j==0: bd=2
            if i==0: bd=1
            bdy.append(bd); ic.append((i==ns and j==0 and k==0)or(i==0 and j==ns and k==0)or(i==0 and j==0 and k==ns))
            idx+=1
    for i in range(ns):
        for j in range(ns-i):
            k=ns-i-j
            v1=bary[(i,j,k)]; v2=bary[(i+1,j,k-1)]; v3=bary[(i,j+1,k-1)]
            elems_m.append([v1,v2,v3])
            if k>=2: v4=bary[(i+1,j+1,k-2)]; elems_m.append([v2,v4,v3])
    return np.array(verts),np.array(elems_m),np.array(bdy),np.array(ic),bary,vA,vB,vC,ns

def om2(x,y): return 4.0/(1.0-x*x-y*y+1e-15)**2

# === GAUGE ASSEMBLY ===
def assemble_with_gauge(verts, elems_m, cone_pts, cone_orders, omega_A, omega_B, omega_C):
    nv=len(verts)
    K=np.zeros((nv,nv),dtype=complex); M=np.zeros((nv,nv))
    phi_A=np.angle(omega_A); phi_B=np.angle(omega_B); phi_C=np.angle(omega_C)
    phases=[phi_A,phi_B,phi_C]
    for e in elems_m:
        i1,i2,i3=e; x1,y1=verts[i1]; x2,y2=verts[i2]; x3,y3=verts[i3]
        Js=(x2-x1)*(y3-y1)-(x3-x1)*(y2-y1); J=abs(Js)
        if J<1e-15: continue
        Ae=J/2.0
        gp=[(y2-y3)/Js,(x3-x2)/Js,(y3-y1)/Js,(x1-x3)/Js,(y1-y2)/Js,(x2-x1)/Js]
        xc=(x1+x2+x3)/3; yc=(y1+y2+y3)/3
        # Gauge at centroid
        Ax,Ay=0.0,0.0
        for cp,ph in zip(cone_pts,phases):
            dx=xc-cp[0]; dy=yc-cp[1]; r2=dx*dx+dy*dy+1e-10
            Ax+=ph/(2*PI)*(-dy)/r2; Ay+=ph/(2*PI)*dx/r2
        for a in range(3):
            for b in range(3):
                kinetic=(gp[2*a]*gp[2*b]+gp[2*a+1]*gp[2*b+1])*Ae
                A_grad_b=Ax*gp[2*b]+Ay*gp[2*b+1]
                convective=-2j*A_grad_b*Ae/3.0
                A2=Ax*Ax+Ay*Ay
                pot_coeff=Ae/6.0 if a==b else Ae/12.0
                potential=A2*pot_coeff
                K[e[a],e[b]]+=kinetic+convective+potential
        w1,w2,w3=om2(x1,y1),om2(x2,y2),om2(x3,y3)
        M[e[0],e[0]]+=Ae*(3*w1+w2+w3)/30; M[e[1],e[1]]+=Ae*(w1+3*w2+w3)/30; M[e[2],e[2]]+=Ae*(w1+w2+3*w3)/30
        M[e[0],e[1]]+=Ae*(2*w1+2*w2+w3)/60; M[e[1],e[0]]+=Ae*(2*w1+2*w2+w3)/60
        M[e[0],e[2]]+=Ae*(2*w1+w2+2*w3)/60; M[e[2],e[0]]+=Ae*(2*w1+w2+2*w3)/60
        M[e[1],e[2]]+=Ae*(w1+2*w2+2*w3)/60; M[e[2],e[1]]+=Ae*(w1+2*w2+2*w3)/60
    K=(K+K.conj().T)/2.0
    return K,M

# === EIGENVALUE TRIPLES ===
def find_triples(rho_s, rho_u, d):
    rho_Rc=rho_u@rho_u@rho_s
    eA=np.linalg.eigvals(rho_s); eB=np.linalg.eigvals(rho_u); eC=np.linalg.eigvals(rho_Rc)
    triples=[]
    for wa in eA:
        for wb in eB:
            wc_need=1.0/(wa*wb)
            for wc in eC:
                if abs(wc-wc_need)<0.05:
                    triples.append((wa,wb,wc)); break
    # deduplicate
    ut=[]
    for t in triples:
        dup=False
        for u in ut:
            if abs(t[0]-u[0])<0.05 and abs(t[1]-u[1])<0.05: dup=True; break
        if not dup: ut.append(t)
    return ut

def cone_fixed(bary,nsub,wa,wb,wc,tol=0.1):
    fix=[]
    if (nsub,0,0) in bary and abs(wa-1.0)>tol: fix.append(bary[(nsub,0,0)])
    if (0,nsub,0) in bary and abs(wb-1.0)>tol: fix.append(bary[(0,nsub,0)])
    if (0,0,nsub) in bary and abs(wc-1.0)>tol: fix.append(bary[(0,0,nsub)])
    return fix

def solve_dir(K,M,fixed,ne=20):
    n=K.shape[0]; free=sorted(set(range(n))-set(fixed)); nf=len(free)
    if nf<2: return np.array([])
    Kf=K[np.ix_(free,free)]; Mf=M[np.ix_(free,free)]
    if np.max(np.abs(Kf.imag))<1e-10: Kf=Kf.real
    if np.max(np.abs(Mf.imag))<1e-10: Mf=Mf.real
    Mf=Mf+1e-12*np.eye(nf)
    try: ev,_=eigh(Kf,Mf)
    except: Mf=Mf+1e-10*np.eye(nf); ev,_=eigh(Kf,Mf)
    ev=np.real(ev); pos=ev>1e-8; ev=ev[pos]
    if len(ev)==0: return np.array([0.0])
    idx=np.argsort(ev); ne=min(ne,len(idx))
    return ev[idx[:ne]]

# === MAIN ===
def main():
    t0=time.time()
    print("="*70)
    print("AB-CLOUD v8d — Калибровочное поле + BC Неймана")
    print("="*70)
    elems,s_mat,u_mat=gen_psl27()
    print(f"  |PSL(2,7)|={len(elems)}")
    reps=build_reps(s_mat,u_mat,elems)
    for rn in REPS:
        if rn not in reps: print(f"  {rn}: ОТСУТСТВУЕТ"); continue
        rs,ru,d=reps[rn]; chi=CHAR_TABLE[rn]
        es=norm(rs@rs-np.eye(d)); eu=norm(ru@ru@ru-np.eye(d))
        esu=norm(np.linalg.matrix_power(rs@ru,7)-np.eye(d))
        ok="✓" if es<1e-4 and eu<1e-4 else "✗"
        print(f"  {rn}: S²={es:.1e} U³={eu:.1e} (SU)⁷={esu:.1e} tr(S)={np.trace(rs).real:.1f}({chi[1].real:.0f}) tr(U)={np.trace(ru).real:.1f}({chi[2].real:.0f}) [{ok}]")

    level=5
    vs,es,bd,ic,by,vA,vB,vC,ns=create_mesh(level)
    nv=len(vs); cone_pts=[vA,vB,vC]; cone_orders=[2,3,7]
    print(f"  n_v={nv}, level={level}")

    # Проверка: Neumann BC (1a, без калибровки)
    print("\n  ТЕСТ: Neumann BC (1a, без калибровки)")
    K_geo=np.zeros((nv,nv)); M_geo=np.zeros((nv,nv)); Ae=Ah=0.0
    for e in es:
        i1,i2,i3=e; x1,y1=vs[i1]; x2,y2=vs[i2]; x3,y3=vs[i3]
        Js=(x2-x1)*(y3-y1)-(x3-x1)*(y2-y1); J=abs(Js)
        if J<1e-15: continue
        A=J/2.0
        gp=[(y2-y3)/Js,(x3-x2)/Js,(y3-y1)/Js,(x1-x3)/Js,(y1-y2)/Js,(x2-x1)/Js]
        for a in range(3):
            for b in range(3): K_geo[e[a],e[b]]+=(gp[2*a]*gp[2*b]+gp[2*a+1]*gp[2*b+1])*A
        w1,w2,w3=om2(x1,y1),om2(x2,y2),om2(x3,y3)
        M_geo[e[0],e[0]]+=A*(3*w1+w2+w3)/30; M_geo[e[1],e[1]]+=A*(w1+3*w2+w3)/30; M_geo[e[2],e[2]]+=A*(w1+w2+3*w3)/30
        M_geo[e[0],e[1]]+=A*(2*w1+2*w2+w3)/60; M_geo[e[1],e[0]]+=A*(2*w1+2*w2+w3)/60
        M_geo[e[0],e[2]]+=A*(2*w1+w2+2*w3)/60; M_geo[e[2],e[0]]+=A*(2*w1+w2+2*w3)/60
        M_geo[e[1],e[2]]+=A*(w1+2*w2+2*w3)/60; M_geo[e[2],e[1]]+=A*(w1+2*w2+2*w3)/60
        Ae+=A; Ah+=A*(w1+w2+w3)/3
    print(f"  A_hyp={Ah:.6f} (π/42={PI/42:.6f})")

    # Neumann: все узлы свободны → K_geo v = λ M_geo v
    ev_neu=solve_dir(K_geo,M_geo,[])
    if len(ev_neu)>1: ev_neu=ev_neu[1:]  # skip λ=0
    if len(ev_neu)>0: print(f"  Neumann λ₁={ev_neu[0]:.4f} (первые 5: {ev_neu[:5].round(2)})")

    # Теперь с калибровкой для каждого представления
    print(f"\n{'='*70}")
    print("FEM С КАЛИБРОВОЧНЫМ ПОЛЕМ + NEUMANN BC")
    print(f"{'='*70}")
    print(f"  {'ρ':>4s} {'сект':>4s} {'λ₁(min)':>10s} {'λ₁(Cook)':>10s} {'Δ%':>7s}")
    print("  "+"─"*40)

    for rn in REPS:
        cook=COOK.get(rn)
        if rn in reps:
            rs,ru,d=reps[rn]
            triples=find_triples(rs,ru,d)
        else:
            # Для 8a и 6a: используем известные собственные значения
            if rn=='8a':
                # ρ(s): eigenvalues ±1, tr=0, dim=8 → 4×(+1), 4×(-1)
                # ρ(u): eigenvalues, tr=-1, dim=8 → 2×1, 3×ω₃, 3×ω₃²
                w3=np.exp(2j*PI/3)
                eA=[1]*4+[-1]*4; eB=[1,1]+[w3]*3+[w3**2]*3
                # Compute ρ(u²s) eigenvalues from trace
                # tr(u²s) = χ(7A) = 1 for 8a, dim=8
                # eigenvalues are 7th roots: need sum = 1
                # 8 = n1+n2+...+n8, 1 = sum of 7th roots
                # Just enumerate: ω₇^k where ω₇=e^{2πi/7}
                w7=np.exp(2j*PI/7)
                eC_candidates=[[w7**k for k in combo] for combo in __import__('itertools').product(range(7),repeat=8)]
                # Too many! Use simpler approach
                # From character: χ(7A)=1, and eigenvalues are 7th roots
                # The constraint ω_A·ω_B·ω_C=1 gives ω_C = 1/(ω_A·ω_B)
                triples=[]
                for wa in [1.0,-1.0]:
                    for wb in [1.0,w3,w3**2]:
                        wc=1.0/(wa*wb)
                        triples.append((wa,wb,wc))
            elif rn=='6a':
                w3=np.exp(2j*PI/3)
                # ρ(s): tr=2, dim=6 → 4×(+1), 2×(-1)
                # ρ(u): tr=0, dim=6 → 2×1, 2×ω₃, 2×ω₃²
                triples=[]
                for wa in [1.0,-1.0]:
                    for wb in [1.0,w3,w3**2]:
                        wc=1.0/(wa*wb)
                        triples.append((wa,wb,wc))
            else:
                triples=[]

        if not triples:
            print(f"  {rn:>4s}    — нет секторов"); continue

        all_lam=[]
        for wa,wb,wc in triples:
            K_r,M_r=assemble_with_gauge(vs,es,cone_pts,cone_orders,wa,wb,wc)
            fix=cone_fixed(by,ns,wa,wb,wc)
            ev=solve_dir(K_r,M_r,fix)
            is_trivial=abs(wa-1)<0.1 and abs(wb-1)<0.1 and abs(wc-1)<0.1
            if rn=='1a' and is_trivial and len(ev)>1: ev=ev[1:]
            if len(ev)>0: all_lam.append(ev[0])

        if all_lam:
            lam1=min(all_lam)
            dl=abs(lam1-cook)/cook*100 if cook and cook>0 else float('nan')
            ck=f"{cook:.4f}" if cook else "—"
            dls=f"{dl:.1f}" if not np.isnan(dl) else "—"
            print(f"  {rn:>4s} {len(triples):>4d} {lam1:>10.4f} {ck:>10s} {dls:>7s}")
        else:
            print(f"  {rn:>4s} {len(triples):>4d}    — нет секторов")

    el=time.time()-t0
    print(f"\n  Время: {el:.0f}с")

if __name__=='__main__': main()
