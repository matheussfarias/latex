#!/usr/bin/env python
import random
def neg(P,p):
        return P[0],(-P[1])%p
def modinv(a,m):
        return pow(a,m-2,m)
def ecadd(P,Q,p,a):
        if P[0]==0.5 and P[1]==0.5:  
                return Q[0],Q[1]
        if Q[0]==0.5 and Q[1]==0.5:
                return P[0],P[1] 
        if P[0]==Q[0] and P[1]==Q[1]:
                return ecdbl(P,p,a)
        if P[0]==Q[0] and P[1]==(-Q[1])%p:
                return 0.5,0.5
        t=((P[1]-Q[1])%p)*modinv(((P[0]-Q[0])%p),p)%p
        Xr=((t**2)%p-Q[0]-P[0])%p
        Yr=(t*(P[0]-Xr)-P[1])%p
        return Xr,Yr
def ecdbl(P,p,a):
        if P[0]==0.5 and P[1]==0.5:
                return P[0],P[1]
        t=(((3*P[0]**2+a)%p)*modinv((2*P[1])%p,p))%p
        Xr=(t**2%p-P[0]-P[0])%p
        Yr=(t*(P[0]-Xr)-P[1])%p
        return Xr,Yr
def binarymethod(P,k,p,a):
        kbin=bin(k)
        Q=[0.5,0.5]
        for x in range(2,len(kbin)):
                Q[0],Q[1]=ecdbl(Q,p,a)
                if kbin[x]=='1':
                        Q[0],Q[1]=ecadd(P,Q,p,a)
        return Q[0],Q[1]
def elgamalkeygen(P,p,a):
        H=[0,0]
        x=random.randrange(p)
        H[0],H[1]=binarymethod(P,x,p,a)
        return H[0],H[1],x   
def encryptelgamal(P,p,a,H,M):
        S=[0,0]
        cypher1=[0,0]
        cypher2=[0,0]
        y=random.randrange(p)
        S[0],S[1]=binarymethod(H,y,p,a)
        cypher2[0],cypher2[1]=ecadd(M,S,p,a)
        cypher1[0],cypher1[1]=binarymethod(P,y,p,a)
        return cypher1[0],cypher1[1],cypher2[0],cypher2[1]
def decryptelgamal(cypher1,cypher2,P,x,p,a):
        S=[0,0]
        M=[0,0]
        S[0],S[1]=binarymethod(cypher1,x,p,a)
        S[0],S[1]=neg(S,p)
        M[0],M[1]=ecadd(S,cypher2,p,a)
        return M[0],M[1]

