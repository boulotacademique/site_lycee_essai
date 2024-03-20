L=[5,3,4,-1,4,6]
rep = len(L)
trouve = False
for idx in range(len(L)):
    if not(trouve) and L[idx] < 0 :
        trouve = True
        rep = idx
print(rep)
