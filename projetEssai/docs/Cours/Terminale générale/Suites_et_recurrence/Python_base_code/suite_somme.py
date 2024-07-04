def f(x):
    return -5+7*x

def suiteU(n):
    return f(n)

def somme(n):
    S=0
    for i in range(n+1):
        S=S+suiteU(i)
    return S

n=10
print(somme(n))
