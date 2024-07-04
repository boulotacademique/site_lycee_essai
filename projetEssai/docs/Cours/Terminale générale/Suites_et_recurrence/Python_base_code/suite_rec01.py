def f(x):
    return 0.75*x+4

def suiteU(n,u0):
    u=u0
    for i in range(n):
        u=f(u)
    return u

n=10
u0=2
print(suiteU(n,u0))


def suiteU2(n,u0):
    u=u0
    for i in range(n):
        print(u)
        u=f(u)
    return u

n=10
u0=2
print(suiteU2(n,u0))