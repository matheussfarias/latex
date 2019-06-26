import matplotlib.pyplot as plt
import math
import numpy as np


#Valores utilizados para as constantes alfa,mi,gama,beta,teta,tau .

'''PARAMETERS
α Change requests Increasing of project
μ Resignment Fair dismissal Labor accident Diseases
γ Productivity
β Cost with remuneration (wages, bonuses, etc.).Cost with social charges.
θ Cost with hiring/firing Cost with training/adaptation/transfer
τ Ending time
'''
alpha,mi,gama,beta,teta,tau = 0.12,0.1,0.0008,1100,100,180
tempo=tau + 1 # Empresa 3


#achando os valores das contantes de integração

a=1/(4*teta*mi)
b= -gama/((2*teta)*(alpha**2-mi**2))
c = gama/((4*teta*mi)*(alpha+mi))
d=gama/(alpha-mi)
f=-(gama**2)/(4*teta*alpha*(alpha**2-mi**2))
g= math.exp(mi*tau)/(4*teta*mi)
h=math.exp(-mi*tau)
i=-gama*math.exp(alpha*tau)/(2*teta*(alpha**2-mi**2))
j= gama*math.exp(mi*tau)/(4*teta*mi*(alpha+mi))
l= gama*math.exp(-mi*tau)/(alpha-mi)
m= math.exp(-alpha*tau)
n= -gama**2*math.exp(alpha*tau)/(4*teta*alpha*(alpha**2-mi**2))
u=beta/(2*teta*mi**2)
v=gama*beta/(2*teta*alpha*mi**2)
x=(alpha/gama) + beta/(2*teta*mi**2)
z= 1 + gama*beta/(2*teta*alpha*mi**2)



A=((m*v -z)*(a*h - g) + (u*g - x*a)*(d*m - l) + (u*h - x)*(j-c*m))/((m*f - n
)*(a*h - g) + (b*g - i*a)*(d*m-l) +(b*h-i)*(j-c*m))
B=(i-b*h)*A/(a*h-g) -(x-u*h)/(a*h-g)
C=u-b*A -a*B
D=(v-u*d) -(f - b*d)*A -(c- a*d)*B




U,N,P=[],[],[]
for t in range(tempo):
    U.append(-beta/(2*teta*mi)-(gama*A*math.exp(alpha*t)/(2*teta*(alpha-mi)))+(B*math.exp(mi*t))/(2*teta))
    N.append(-beta/(2*teta*(mi**2))-(gama*A*math.exp(alpha*t))/(2*teta*((alpha**2)-(mi**2)))+(B*math.exp(mi*t)/(4*teta*mi))+C*math.exp(-mi*t))


    P.append(-gama*beta/(2*teta*alpha*mi**2)-(gama**2*A*math.exp(alpha*t))/(4*teta*alpha*(alpha**2-mi**2))+
        (gama*B*math.exp(mi*t))/(4*teta*mi*(alpha + mi))+(gama*C*math.exp(-mi*t))/(alpha-mi)+D*math.exp(-alpha*t))



plt.figure(figsize=(8, 6), dpi=150)
plt.plot(list(range(tempo)), N,'r')
plt.title("Quantidade de trabalhadores em um determinado instante de tempo.")
plt.xlabel("Tempo(Meses)")
plt.ylabel("N (Número de trabalhadores)")
#plt.legend()
plt.savefig("empresa4_n.png")

plt.figure(figsize=(8, 6), dpi=150)
plt.plot(list(range(tempo)), U,'b')
plt.title("Política de contratação")
plt.xlabel("Tempo(Meses)")
plt.ylabel("U (Número de contratações/demissões)")
#plt.legend()
plt.savefig("empresa4_u.png")

plt.figure(figsize=(8, 6), dpi=150)
plt.plot(list(range(tempo)), [i*100 for i in P],'g')
plt.title("Evolução do percentual de atividades completas no projeto.")
plt.xlabel("Tempo(Meses)")
plt.ylabel("P (Percentual)")
#plt.legend()
plt.savefig("empresa4_p.png")

#print(U)
#    P.append()
