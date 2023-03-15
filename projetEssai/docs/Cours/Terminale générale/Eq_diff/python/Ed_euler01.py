# Cas y' = f(x)

import matplotlib.pyplot as plt
import math

def fonc(x):
    return 1/x

def sol_th(x):
    return math.log(x)

def euler(deb, fin, pas, image_deb):
    L_abs = [deb]
    L_ord = [image_deb]
    nb = 0
    x = deb
    f_x = image_deb
    while x < fin :
        f_x = fonc(x)*pas+ f_x
        x = x + pas
        L_abs.append(x)
        L_ord.append(f_x)
    return L_abs, L_ord


Lx, Ly = euler(1,10,0.001,0)
plt.plot(Lx, Ly, 'r')
Lth = [sol_th(x) for x in Lx]

plt.plot(Lx, Lth, 'b')
plt.show()

    

