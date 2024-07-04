def f(x):
    return 0.75*x+4

def suiteU(n,u0):
    u=u0
    ind=0
    while ind<n:
        ind=ind+1
        u=f(u)
    return u

n=10
u0=2
print(suiteU(n,u0))
