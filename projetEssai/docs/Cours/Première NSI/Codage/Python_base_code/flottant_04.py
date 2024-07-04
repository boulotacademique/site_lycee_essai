som1 = 0
for i in range(1,10**5 + 1):
    som1 = som1 + 1/i
print(som1)

som2 = 0
for i in range(10**5,0,-1):
    som2 = som2 + 1/i
print(som2)