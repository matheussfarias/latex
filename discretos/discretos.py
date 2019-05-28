#!/usr/bin/env python
import random
import math
def cod(a):
        if a==" ":
                return 0
        n=ord(a)-96
        return n
def decod(n):
        if n==0:
                return " "
        else:
                a=chr(n+96)
                return a
def codetext(text):
        m=0
        i=0
        for a in text:
                m+=cod(a)*27**i
                i+=1
        return m
def decodetext(m):
        s=decod(m%27)
        q=m//27
        while q>0:
                s+=decod(q%27)
                q=q//27
        return s
        
def fermat(bignumber):
        if bignumber%2==0:
                return 1;
        f=pow(2,bignumber-1,bignumber)
        if f==1:
                return 1
        else:
                return 0
def miller(bignumber,k,m):
        if bignumber==2:
                return 1
        if bignumber%2==0:
                return 0
        r=random.randint(1,bignumber-1)
        b=pow(r,m,bignumber)
        if m==1:
                return 1;
        if b==1:
                return 1
        for i in range(1,k+1):
                if b==1 or b==bignumber-1:
                        return 1
                else:
                        b=pow(b,2,bignumber)
        return 0                               
def isprime(a):
        n=a-1
        k=0
        while n%2==0:
                n=n//2
                k=k+1
                if n==0:
                        break
        m= (a-1) //(2**k)
        for i in range(1,100):
                b=miller(a,k,m)
                if b==0:
                        break
        if m==1:
               a=fermat(a)
        else:
                a=b and fermat(a)   
                
        return a
def tamanho (bignumber):
        return int(math.log(bignumber,2)+1)    
def randomprime(a,N):
        if tamanho(a)==N:
                b=random.randint(a,2**N-1)
                while isprime(b)==0:
                        b=random.randint(a,2**N-1)
        else:
                b=random.randint(2**(N-1),2**N-1)
                while isprime(b)==0:
                        b=random.randint(2**(N-1),2**N-1)
        return b                        
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
def generatepub():
        p=randomprime(2**512,512)
        a=0
        P=[0,0]
        P[0],P[1],a=random.randrange(p),random.randrange(p),random.randrange(p)
        while p%4!=3 and p%4!=(-1):
                p=randomprime(2**520,520)
        return p,a,P[0],P[1]
def encodemes(string,a,P,p):
        num=codetext(string)
        b=P[1]**2-P[0]**3-a*P[0]
        return num,pow((num**3+num*a+b),(p+1)//4,p)
def decodemes(M):
        string=decodetext(M[0])
        return string
 
P=[0,0]
H=[0,0]
c1=[0,0]
c2=[0,0]
M=[0,0]
p,a,P[0],P[1]=generatepub()
print("geradores")
print("primo")
print(p)
print("a")
print(a)
print("P")
print(P[0])
print(P[1])
M[0],M[1]=encodemes("acabamos",a,P,p)
print("M")
print(M[0])
print(M[1])
H[0],H[1],X=elgamalkeygen(P,p,a)
print("X")
print(X)
print("H")
print(H[0])
print(H[1])
c1[0],c1[1],c2[0],c2[1]=encryptelgamal(P,p,a,H,M)
print("c1")
print(c1[0])
print(c1[1])
print("c2")
print(c2[0])
print(c2[1])
M[0],M[1]=decryptelgamal(c1,c2,P,X,p,a)
string=decodemes(M)
print(string)
  
