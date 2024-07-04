# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 14:20:30 2024

@author: Papa
"""

import turtle as tu
import math as ma

### Dessiner un carré

#for i in range(4):
#    tu.forward(100)
#    tu.left(90)

### Dessiner un triangle équilatéral

#for i in range(3):
#    tu.forward(100)
#    tu.left(120)

### Dessiner un hexagone régulier

#for i in range(6):
#    tu.forward(100)
#    tu.left(60)

### Dessiner côte à côte

#tu.up()
#tu.backward(400)
#tu.down()
#
#n = 4
#L = 200
#for i in range(n):
#    tu.forward(L)
#    tu.left(360//n)
#
#tu.up()
#tu.forward(L + 50)
#tu.down()
#
#n = 3
#for i in range(n):
#    tu.forward(L*2*ma.sqrt(3)/3)
#    tu.left(360//n)
#
#tu.up()
#tu.forward(L + 50)
#tu.down()
#
#n = 6
#for i in range(n):
#    tu.forward(L*ma.sqrt(3)/3)
#    tu.left(360//n)

### Dessiner une spirale

#nb_etape = 20
#angle = 60
#pas = 2
#for i in range(nb_etape):
#    tu.forward(pas + pas*i)
#    tu.left(angle)



### Dessiner un cercle
#
#nb_etape = 360
#angle = 1
#pas = 2
#for i in range(nb_etape):
#    tu.forward(1)
#    tu.left(angle)

### Dessiner carrés emboités

#nb_etape = 10
#long = 200
#reduction = ma.sqrt(2)/2
#for i in range(nb_etape):
#    for i in range(4):
#        tu.forward(long)
#        tu.left(90)
#    tu.forward(long/2)
#    tu.left(45)
#    long = long*reduction

### Dessiner triangles emboités

#nb_etape = 10
#long = 300
#reduction = 1/2
#for i in range(nb_etape):
#    for i in range(3):
#        tu.forward(long)
#        tu.left(120)
#    tu.forward(long/2)
#    tu.left(60)
#    long = long*reduction


### Dessiner hexagones emboités

#tu.up()
#tu.goto(-300,-300)
#tu.down()
#
#nb_etape = 10
#long = 300
#reduction = ma.sqrt(3)/2
#for i in range(nb_etape):
#    for i in range(6):
#        tu.forward(long)
#        tu.left(60)
#    tu.forward(long/2)
#    tu.left(30)
#    long = long*reduction

### Dessiner carrés emboités en spirale

#tu.up()
#tu.goto(-300,-300)
#tu.down()
#
#tu.speed(0)
#nb_etape = 50
#long = 400
#dec = 0.5
#reduction = ma.sqrt(dec**2 + (1-dec)**2)
#angle = ma.degrees(ma.atan(dec/(1-dec)))
#for i in range(nb_etape):
#    for i in range(4):
#        tu.forward(long)
#        tu.left(90)
#    tu.forward(long*dec)
#    tu.left(angle)
#    long = long*reduction

### Dessiner etoile à 5 branches

tu.up()
tu.goto(-200,-200)
tu.down()

tu.speed(0)
nb_etape = 5
long = 300
tu.left(180/nb_etape)
for i in range(nb_etape):
    tu.forward(long)
    tu.left((nb_etape -1)*180/nb_etape)
    
    
tu.exitonclick()