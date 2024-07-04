def suiteU(n,u0):
    u=u0
    for i in range(n):
        u=0.75*u+4
    return u

n=10
u0=2
print(suiteU(n,u0))
