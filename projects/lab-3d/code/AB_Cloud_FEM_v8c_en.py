"""
AB_Cloud_FEM_v8c — English Version
============================================================

FEM on Klein quartic with matrix twisted boundary conditions. Corrected PSL(2,7) generation and conjugacy classes.

This is the English translation of AB_Cloud_FEM_v8c.py.
Russian comments in the code body are preserved for reference.

Original file: AB_Cloud_FEM_v8c.py
"""

import numpy as np
from scipy import sparse
from scipy.linalg import eigh, norm, svd
from collections import deque
import time

PI = np.pi
SQRT7 = np.sqrt(7.0)
ALPHA = (-1.0 + SQRT7 * 1j) / 2.0
ALPHA_BAR = (-1.0 - SQRT7 * 1j) / 2.0

CHAR_TABLE = {
    '1a': np.array([1,  1,  1,  1,  1,        1       ], dtype=complex),
    '3a': np.array([3, -1,  0,  1,  ALPHA,    ALPHA_BAR], dtype=complex),
    '3b': np.array([3, -1,  0,  1,  ALPHA_BAR, ALPHA   ], dtype=complex),
    '6a': np.array([6,  2,  0,  0, -1,       -1       ], dtype=complex),
    '7a': np.array([7, -1,  1, -1,  0,        0       ], dtype=complex),
    '8a': np.array([8,  0, -1,  0,  1,        1       ], dtype=complex),
}
REPS = ['1a', '3a', '3b', '6a', '7a', '8a']
COOK = {'1a': 0.0, '3a': 3.577, '3b': None, '6a': 10.869, '7a': 6.6225, '8a': 2.6779}

# ============================================================================
# PSL(2,7) — МАТРИЦЫ 2×2 НАД F_7
# ============================================================================

def mm(A, B):
    """Умножение матриц над F_7."""
    return np.array([
        [(A[0,0]*B[0,0]+A[0,1]*B[1,0])%7, (A[0,0]*B[0,1]+A[0,1]*B[1,1])%7],
        [(A[1,0]*B[0,0]+A[1,1]*B[1,0])%7, (A[1,0]*B[0,1]+A[1,1]*B[1,1])%7]
    ], dtype=int)

def minv(A):
    """Обратная матрица в SL(2,F_7)."""
    d = (A[0,0]*A[1,1]-A[0,1]*A[1,0])%7
    di = pow(int(d), -1, 7)
    return np.array([[A[1,1]*di%7, (-A[0,1]*di)%7],
                     [(-A[1,0]*di)%7, A[0,0]*di%7]], dtype=int)

def mk(M): return tuple(M.flatten()%7)
def nk(M): return tuple(((-M)%7).flatten())
def eq(A,B): return mk(A)==mk(B) or nk(A)==mk(B)

def order_psl(M):
    """Порядок элемента в PSL(2,7)."""
    I = np.array([[1,0],[0,1]], dtype=int)
    if eq(M, I): return 1
    Mp = M.copy()
    for k in range(2, 8):
        Mp = mm(Mp, M)
        if eq(Mp, I): return k
    return -1

def gen_psl27():
    """Генерация PSL(2,7) через BFS."""
    s = np.array([[0,1],[6,0]], dtype=int)
    u = np.array([[0,1],[6,1]], dtype=int)
    I = np.array([[1,0],[0,1]], dtype=int)
    
    elems = [I]
    seen = {mk(I)}
    q = deque([0])
    while q:
        idx = q.popleft()
        g = elems[idx]
        for gen in [s, u]:
            ng = mm(gen, g)
            k, nk_ = mk(ng), nk(ng)
            if k not in seen and nk_ not in seen:
                seen.add(k)
                elems.append(ng)
                q.append(len(elems)-1)
    assert len(elems) == 168, f"Got {len(elems)}"
    return elems, s, u

def classify(elems, s_mat, u_mat):
    """Классификация элементов по классам сопряжённости."""
    n = len(elems)
    # Предвычисляем порядок
    orders = [order_psl(M) for M in elems]
    
    # Для порядка 7: проверяем сопряжённость с su или его степенями
    su = mm(s_mat, u_mat)
    
    # Вычисляем все степени su
    su_pows = [su.copy()]
    for k in range(1, 7):
        su_pows.append(mm(su_pows[-1], su))
    # su_pows[k] = su^(k+1)
    
    # Для каждого элемента порядка 7 проверяем сопряжённость
    # Полная проверка: h M h⁻¹ = su^k для некоторого h и k
    classes = []
    for i, M in enumerate(elems):
        o = orders[i]
        if o == 1: classes.append(0)
        elif o == 2: classes.append(1)
        elif o == 3: classes.append(2)
        elif o == 4: classes.append(3)
        elif o == 7:
            # Проверяем сопряжённость с su^k
            found = False
            for h in elems:
                hinv = minv(h)
                conj = mm(mm(h, M), hinv)
                for k_idx in range(6):
                    if eq(conj, su_pows[k_idx]):
                        # k_idx+1 = power of su
                        power = k_idx + 1  # 1..6
                        if power in [1, 2, 4]:
                            classes.append(4)  # 7A
                        else:
                            classes.append(5)  # 7B
                        found = True
                        break
                if found: break
            if not found:
                classes.append(-1)  # ошибка
        else:
            classes.append(-1)
    
    return classes, orders

# ============================================================================
# ПРЕДСТАВЛЕНИЯ — ПРЯМЫЕ ФОРМУЛЫ
# ============================================================================

def build_all_reps(s_mat, u_mat, elems):
    """Строит все 6 представлений PSL(2,7) прямыми конструкциями."""
    reps = {}
    
    # 1a: тривиальное
    reps['1a'] = (np.array([[1.0]]), np.array([[1.0]]), 1)
    
    # 7a: представление на P¹(F_7) минус тривиальное
    # P¹(F_7) = {0,1,2,3,4,5,6,∞}, действие: z → (az+b)/(cz+d)
    def psl_action(M, z):
        a,b,c,d = int(M[0,0]), int(M[0,1]), int(M[1,0]), int(M[1,1])
        if z == 7:  # ∞
            return 7 if c == 0 else (a*pow(c,-1,7))%7
        else:
            num = (a*z+b)%7; den = (c*z+d)%7
            return 7 if den == 0 else (num*pow(den,-1,7))%7
    
    s_perm = [psl_action(s_mat, z) for z in range(8)]
    u_perm = [psl_action(u_mat, z) for z in range(8)]
    
    P_s = np.zeros((8,8)); P_u = np.zeros((8,8))
    for i in range(8):
        P_s[i, s_perm[i]] = 1; P_u[i, u_perm[i]] = 1
    
    # 7a = P¹(F_7) − trivial
    v1 = np.ones(8)/np.sqrt(8)
    Q = np.eye(8) - np.outer(v1, v1)
    U7, _, _ = svd(Q)
    B7 = U7[:, :7]
    reps['7a'] = (B7.T @ P_s @ B7, B7.T @ P_u @ B7, 7)
    
    # 7a⊗7a содержит: 1a(×1) + 3a(×1) + 3b(×1) + 6a(×2) + 7a(×2) + 8a(×2)
    # Извлекаем 3a, 3b, 8a, 6a через проекторы характеров из 7a⊗7a
    print("  Извлекаю 3a, 3b, 8a, 6a из 7a⊗7a...")
    
    rho7_s, rho7_u, d7 = reps['7a']
    Rs49 = np.kron(rho7_s, rho7_s)  # 49×49
    Ru49 = np.kron(rho7_u, rho7_u)
    
    # У нас уже есть все элементы группы и их классы
    # Строим все матрицы 7a-представления
    print("  Строю все матрицы 7a-представления...")
    def psl_action(M, z):
        a,b,c,d = int(M[0,0]), int(M[0,1]), int(M[1,0]), int(M[1,1])
        if z == 7: return 7 if c == 0 else (a*pow(c,-1,7))%7
        else:
            num = (a*z+b)%7; den = (c*z+d)%7
            return 7 if den == 0 else (num*pow(den,-1,7))%7
    
    rho7_all = {}
    for g in elems:
        perm = [psl_action(g, z) for z in range(8)]
        P = np.zeros((8,8))
        for i in range(8): P[i, perm[i]] = 1
        rho7_all[mk(g)] = B7.T @ P @ B7  # в базисе 7a
    
    # Предвычисляем классы для всех элементов
    classes, _ = classify(elems, s_mat, u_mat)
    
    rng = np.random.RandomState(42)
    
    # Общая функция извлечения irrep из 7a⊗7a
    def extract_from_7a7a(rep_name, target_dim):
        chi = CHAR_TABLE[rep_name]
        d = target_dim
        print(f"    Извлечение {rep_name} (dim={d})...")
        
        v = rng.randn(49) + 1j*rng.randn(49)
        Pv = np.zeros(49, dtype=complex)
        
        for i, g in enumerate(elems):
            cc = classes[i]
            if cc < 0: continue
            chi_bar = np.conj(chi[cc])
            Rg = np.kron(rho7_all.get(mk(g), rho7_s), rho7_all.get(mk(g), rho7_s))
            Pv += chi_bar * (Rg @ v)
        Pv *= d / 168.0
        
        # SVD для базиса образа
        basis = [Pv.copy()]
        for trial in range(200):
            new_v = Rs49 @ basis[-1] if trial % 2 == 0 else Ru49 @ basis[-1]
            for b in basis:
                new_v -= np.vdot(b, new_v)/max(np.vdot(b,b), 1e-30) * b
            nn = norm(new_v)
            if nn > 1e-8:
                basis.append(new_v/nn)
                if len(basis) >= d*d: break
        
        B = np.array(basis).T
        U, S, _ = svd(B, full_matrices=False)
        mask = S > 1e-6
        rank = np.sum(mask)
        Ub = U[:, mask]
        print(f"      Ранг проектора: {rank} (ожидается {d*d})")
        
        Rs_V = Ub.conj().T @ Rs49 @ Ub
        Ru_V = Ub.conj().T @ Ru49 @ Ub
        
        # Спин-метод
        for attempt in range(30):
            w = rng.randn(rank) + 1j*rng.randn(rank)
            w /= norm(w)
            
            inv_b = [w.copy()]
            q = deque([0])
            done = set()
            while q and len(inv_b) < d:
                idx = q.popleft()
                if idx in done: continue
                done.add(idx)
                b = inv_b[idx]
                for R in [Rs_V, Ru_V]:
                    nb = R @ b
                    for ex in inv_b:
                        nb -= np.vdot(ex, nb) * ex
                    nn = norm(nb)
                    if nn > 1e-10 and len(inv_b) < d:
                        inv_b.append(nb/nn)
                        q.append(len(inv_b)-1)
            
            if len(inv_b) >= d:
                Q = np.array(inv_b[:d]).T
                rho_s = Q.conj().T @ Rs_V @ Q
                rho_u = Q.conj().T @ Ru_V @ Q
                
                es = norm(rho_s@rho_s - np.eye(d))
                eu = norm(rho_u@rho_u@rho_u - np.eye(d))
                esu = norm(np.linalg.matrix_power(rho_s@rho_u, 7) - np.eye(d))
                tr_s = np.trace(rho_s).real; tr_u = np.trace(rho_u).real
                
                ok = es < 1e-4 and eu < 1e-4
                print(f"      S²={es:.1e} U³={eu:.1e} (SU)⁷={esu:.1e} "
                      f"tr(S)={tr_s:.2f}(χ={chi[1].real:.0f}) tr(U)={tr_u:.2f}(χ={chi[2].real:.0f}) [{'✓' if ok else '✗'}]")
                
                if ok: return (rho_s, rho_u, d)
        
        print(f"      НЕ УДАЛОСЬ извлечь {rep_name}")
        return None
    
    r = extract_from_7a7a('3a', 3)
    if r: reps['3a'] = r; reps['3b'] = (r[0].conj(), r[1].conj(), 3)
    
    r = extract_from_7a7a('8a', 8)
    if r: reps['8a'] = r
    
    r = extract_from_7a7a('6a', 6)
    if r: reps['6a'] = r
    
    return reps

# ============================================================================
# СЕТКА, ЛАПЛАСИАН, BC, SOLVER — те же что и в v8b
# ============================================================================

def create_mesh(level):
    a,b,g = PI/2, PI/3, PI/7
    ca,sa = np.cos(a),np.sin(a); cb,sb = np.cos(b),np.sin(b); cc,sc = np.cos(g),np.sin(g)
    cha = (cb*cc+ca)/(sb*sc); chb = (ca*cc+cb)/(sa*sc); chc = (ca*cb+cc)/(sa*sb)
    vA = np.array([0.,0.]); vB = np.array([np.tanh(np.arccosh(chc)/2),0.])
    vC = np.array([0.,np.tanh(np.arccosh(chb)/2)])
    ns = 2**level; verts,elems,bdy,ic,bary = [],[],[],[],{}
    idx = 0
    for i in range(ns+1):
        for j in range(ns+1-i):
            k = ns-i-j; u,v,w = i/ns,j/ns,k/ns
            x = u*vA[0]+v*vB[0]+w*vC[0]; y = u*vA[1]+v*vB[1]+w*vC[1]
            r2 = x*x+y*y
            if r2>=0.999: s=0.998/np.sqrt(r2); x*=s; y*=s
            verts.append([x,y]); bary[(i,j,k)] = idx
            b = 0
            if k==0: b=3
            if j==0: b=2
            if i==0: b=1
            bdy.append(b); ic.append((i==ns and j==0 and k==0) or (i==0 and j==ns and k==0) or (i==0 and j==0 and k==ns))
            idx += 1
    for i in range(ns):
        for j in range(ns-i):
            k = ns-i-j
            v1=bary[(i,j,k)]; v2=bary[(i+1,j,k-1)]; v3=bary[(i,j+1,k-1)]
            elems.append([v1,v2,v3])
            if k>=2: v4=bary[(i+1,j+1,k-2)]; elems.append([v2,v4,v3])
    return np.array(verts),np.array(elems),np.array(bdy),np.array(ic),bary,vA,vB,vC,ns

def om2(x,y): return 4.0/(1.0-x*x-y*y+1e-15)**2

def assemble(verts, elems):
    nv = len(verts); K=np.zeros((nv,nv)); M=np.zeros((nv,nv)); Ae=Ah=0.
    for e in elems:
        i1,i2,i3=e; x1,y1=verts[i1]; x2,y2=verts[i2]; x3,y3=verts[i3]
        Js=(x2-x1)*(y3-y1)-(x3-x1)*(y2-y1); J=abs(Js)
        if J<1e-15: continue
        A=J/2
        gp=[(y2-y3)/Js,(x3-x2)/Js,(y3-y1)/Js,(x1-x3)/Js,(y1-y2)/Js,(x2-x1)/Js]
        for a in range(3):
            for b in range(3): K[e[a],e[b]]+=(gp[2*a]*gp[2*b]+gp[2*a+1]*gp[2*b+1])*A
        w1,w2,w3=om2(x1,y1),om2(x2,y2),om2(x3,y3)
        M[e[0],e[0]]+=A*(3*w1+w2+w3)/30; M[e[1],e[1]]+=A*(w1+3*w2+w3)/30; M[e[2],e[2]]+=A*(w1+w2+3*w3)/30
        M[e[0],e[1]]+=A*(2*w1+2*w2+w3)/60; M[e[1],e[0]]+=A*(2*w1+2*w2+w3)/60
        M[e[0],e[2]]+=A*(2*w1+w2+2*w3)/60; M[e[2],e[0]]+=A*(2*w1+w2+2*w3)/60
        M[e[1],e[2]]+=A*(w1+2*w2+2*w3)/60; M[e[2],e[1]]+=A*(w1+2*w2+2*w3)/60
        Ae+=A; Ah+=A*(w1+w2+w3)/3
    return K,M,Ae,Ah

def build_bc(bary,bdy,ic,ns,rho_s,rho_u,d):
    nv=len(bdy)
    Ra=rho_s; Rb=rho_u; Rc=rho_u@rho_u@rho_s
    def e1m(R,tol=1e-8):
        ev,_=np.linalg.eig(R); return np.abs(ev-1.)<tol
    mA=e1m(Ra); mB=e1m(Rb); mC=e1m(Rc)
    free=set(); slv={}; fix=set()
    def gd(c,v): return c*nv+v
    for i in range(nv):
        if bdy[i]==0 and not ic[i]:
            for k in range(d): free.add(gd(k,i))
    for key,idx,mask in [((ns,0,0),'A',mA),((0,ns,0),'B',mB),((0,0,ns),'C',mC)]:
        if key in bary:
            vi=bary[key]
            for k in range(d):
                if mask[k]: free.add(gd(k,vi))
                else: fix.add(gd(k,vi))
    for j in range(1,ns):
        i=ns-j
        if (i,j,0) in bary and not ic[bary[(i,j,0)]]:
            for k in range(d): free.add(gd(k,bary[(i,j,0)]))
    for kk in range(1,ns):
        i=ns-kk
        if (i,0,kk) not in bary: continue
        ia=bary[(i,0,kk)]
        if ic[ia]: continue
        if i>kk:
            if (i,kk,0) in bary:
                ib=bary[(i,kk,0)]
                for c in range(d):
                    sd=gd(c,ia)
                    for l in range(d):
                        if abs(Ra[c,l])>1e-12: slv.setdefault(sd,[]).append((gd(l,ib),Ra[c,l]))
        elif kk>i:
            for k in range(d): free.add(gd(k,ia))
        else:
            for k in range(d):
                if mA[k]: free.add(gd(k,ia))
                else: fix.add(gd(k,ia))
    for j in range(1,ns):
        kk=ns-j
        if (0,j,kk) not in bary: continue
        ibc=bary[(0,j,kk)]
        if ic[ibc]: continue
        if j>kk:
            if (kk,j,0) in bary:
                iab=bary[(kk,j,0)]
                for c in range(d):
                    sd=gd(c,ibc)
                    for l in range(d):
                        if abs(Rb[c,l])>1e-12: slv.setdefault(sd,[]).append((gd(l,iab),Rb[c,l]))
        elif kk>j:
            if (j,0,kk) in bary:
                iac=bary[(j,0,kk)]
                for c in range(d):
                    sd=gd(c,ibc)
                    for l in range(d):
                        if abs(Rc[c,l])>1e-12: slv.setdefault(sd,[]).append((gd(l,iac),Rc[c,l]))
        else:
            for k in range(d):
                if mA[k]: free.add(gd(k,ibc))
                else: fix.add(gd(k,ibc))
    if ns%2==0:
        h=ns//2
        if (h,h,0) in bary:
            idx=bary[(h,h,0)]
            if not ic[idx]:
                for k in range(d):
                    if mC[k]: free.add(gd(k,idx))
                    else: fix.add(gd(k,idx))
    for g in fix: free.discard(g)
    for g in slv: free.discard(g)
    return sorted(free),slv,sorted(fix),d*nv

def apply_bc(Kg,Mg,fd,sm,fxd,nt,d,nv):
    nf=len(fd); fi={g:i for i,g in enumerate(fd)}
    r,c,v=[],[],[]
    for i,g in enumerate(fd): r.append(g); c.append(i); v.append(1.+0j)
    for sd,ml in sm.items():
        for md,cf in ml:
            if md in fi: r.append(sd); c.append(fi[md]); v.append(complex(cf))
    P=sparse.csr_matrix((v,(r,c)),shape=(nt,nf))
    Id=sparse.eye(d,format='csr')
    Kt=sparse.kron(sparse.csr_matrix(Kg),Id,format='csr')
    Mt=sparse.kron(sparse.csr_matrix(Mg),Id,format='csr')
    KP=Kt.dot(P); Kr=P.conj().T.dot(KP).toarray(); Kr=(Kr+Kr.conj().T)/2
    MP=Mt.dot(P); Mr=P.conj().T.dot(MP).toarray(); Mr=(Mr+Mr.conj().T)/2
    return Kr,Mr

def solve(K,M,ne=20):
    n=K.shape[0]
    if n<2: return np.array([]),None
    Mr=M+1e-12*np.eye(n)
    try: ev,ec=eigh(K,Mr)
    except: Mr=M+1e-10*np.eye(n); ev,ec=eigh(K,Mr)
    ev=np.real(ev); pos=ev>1e-8; ev=ev[pos]
    if len(ev)==0: return np.array([0.]),None
    idx=np.argsort(ev); ne=min(ne,len(idx))
    return ev[idx[:ne]],ec[:,pos][:,idx[:ne]]

# ============================================================================
# MAIN
# ============================================================================

def main():
    t0=time.time()
    print("="*70)
    print("AB-CLOUD v8c — Матричные twisted BC + прямые конструкции представлений")
    print("="*70)
    
    elems, s_mat, u_mat = gen_psl27()
    print(f"  |PSL(2,7)| = {len(elems)}")
    print(f"  ord(s)={order_psl(s_mat)}, ord(u)={order_psl(u_mat)}, ord(su)={order_psl(mm(s_mat,u_mat))}")
    
    # Классы сопряжённости
    classes, orders = classify(elems, s_mat, u_mat)
    cc = [0]*6
    for c in classes:
        if 0<=c<6: cc[c]+=1
    print(f"  Классы: {cc} (ожид. [1,21,56,42,24,24])")
    
    # Строим представления
    reps = build_all_reps(s_mat, u_mat, elems)
    
    # Верификация
    print("\n  Верификация представлений:")
    for rn in REPS:
        if rn not in reps: print(f"  {rn}: ОТСУТСТВУЕТ"); continue
        rs,ru,d = reps[rn]; chi = CHAR_TABLE[rn]
        es=norm(rs@rs-np.eye(d)); eu=norm(ru@ru@ru-np.eye(d))
        esu=norm(np.linalg.matrix_power(rs@ru,7)-np.eye(d))
        trs=np.trace(rs).real; tru=np.trace(ru).real
        ok = "✓" if es<1e-4 and eu<1e-4 and esu<1e-2 else "✗"
        print(f"  {rn}: S²={es:.1e} U³={eu:.1e} (SU)⁷={esu:.1e} "
              f"tr(S)={trs:.2f}({chi[1].real:.0f}) tr(U)={tru:.2f}({chi[2].real:.0f}) [{ok}]")
    
    # FEM
    level=5
    print(f"\n  Сетка level={level}")
    vs,es,bd,ic,by,_,_,_,ns = create_mesh(level)
    nv=len(vs); print(f"  n_v={nv}, n_elem={len(es)}")
    K,M,Ae,Ah = assemble(vs,es)
    print(f"  A_hyp={Ah:.6f} (π/42={PI/42:.6f}), Δ={abs(Ah-PI/42)/PI/42*100:.1f}%")
    
    print(f"\n{'='*70}")
    print("FEM С МАТРИЧНЫМИ СКРУЧЕННЫМИ BC")
    print(f"{'='*70}")
    print(f"  {'ρ':>4s} {'dim':>3s} {'free':>6s} {'slav':>5s} {'fix':>4s} {'λ₁(FEM)':>10s} {'λ₁(Cook)':>10s} {'Δ%':>7s}")
    print("  "+"─"*55)
    
    results = {}
    for rn in REPS:
        if rn not in reps:
            print(f"  {rn:>4s}  — нет представления"); continue
        rs,ru,d = reps[rn]; ck = COOK.get(rn)
        try:
            fd,sm,fx,nt = build_bc(by,bd,ic,ns,rs,ru,d)
            Kr,Mr = apply_bc(K,M,fd,sm,fx,nt,d,nv)
            ev,_ = solve(Kr,Mr,15)
            if rn=='1a' and len(ev)>1: ev=ev[1:]
            l1 = ev[0] if len(ev)>0 else float('nan')
            dl = abs(l1-ck)/ck*100 if ck and ck>0 else float('nan')
            cks = f"{ck:.4f}" if ck else "  —  "
            dls = f"{dl:.1f}" if not np.isnan(dl) else "  — "
            print(f"  {rn:>4s} {d:>3d} {len(fd):>6d} {len(sm):>5d} {len(fx):>4d} {l1:>10.4f} {cks:>10s} {dls:>7s}")
            results[rn] = {'l1':l1, 'cook':ck, 'd':dl, 'ev':ev[:10]}
        except Exception as e:
            print(f"  {rn:>4s} ОШИБКА: {e}")
            import traceback; traceback.print_exc()
    
    # Сводка
    el = time.time()-t0
    print(f"\n{'█'*70}")
    print(f"█  ИТОГ v8c ({el:.0f}с)")
    for rn in REPS:
        if rn not in results: continue
        r=results[rn]; ck=f"{r['cook']:.4f}" if r['cook'] else "—"
        dl=f"{r['d']:.1f}%" if not np.isnan(r.get('d',float('nan'))) else "—"
        print(f"█  {rn}: λ₁={r['l1']:.4f}  Cook={ck}  Δ={dl}")
    print(f"█{''*68}█\n{'█'*70}")

if __name__=='__main__': main()
