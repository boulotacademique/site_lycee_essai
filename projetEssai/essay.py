import matplotlib.pyplot as mp
import random as rd
import scipy.special as sci
import time

def expBern(p):
    nb=int(p*100)
    nbAlea=rd.randint(1,100)
    if nbAlea<=nb:
        return 1
    return 0

def schemaBern(n,p):
    L=[]
    for i in range(n):
        L.append(expBern(p))
    return L

def nbSuc(n,p):
    tot=0
    L=schemaBern(n,p)
    for i in range(len(L)):
        if L[i]==1:
            tot=tot+1
    return tot

def distribution(n,p,nbExp):
    L=[0]*(n+1)
    for i in range(nbExp):
        t=nbSuc(n,p)
        L[t]=L[t]+1
    return L

def binomFD(n,p,k):
    return sci.comb(n,k,exact=True)*p**k*(1-p)**(n-k)    

p=0.78
n=20
nbExp=100
L=distribution(n,p,nbExp)
listeAbs=[i for i in range(0,n+1) ]
LTheo=[nbExp*binomFD(n,p,i) for i in range(0,n+1)]
mp.plot(listeAbs,L,'r')
mp.plot(listeAbs,LTheo,'b')
mp.show()
