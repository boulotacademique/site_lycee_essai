liste_a = [1, -5, 10, 15, 2, 3, 6, 13]
print(len(liste_a)) # affiche 8
print(liste_a[2]) # affiche 10
print(liste_a[len(liste_a)-1]) # affiche 13
print(liste_a[-1]) # affiche 13
print(liste_a[2:5]) # affiche [10,15,2]
print(liste_a[0:5]) # affiche [1,-5,10,15,2]
print(liste_a[:5]) # affiche [1,-5,10,15,2]
print(liste_a[len(liste_a)-3:len(liste_a)]) # affiche [3, 6, 13]
print(liste_a[-3:]) # affiche [3, 6, 13]
print(liste_a[0:len(liste_a)-5]) # affiche [1, -5, 10]
print(liste_a[:-5]) # affiche [1, -5, 10]
liste_b = liste_a + [1000]
print(liste_b) # affiche [1, -5, 10, 15, 2, 3, 6, 13, 1000]
liste_c = [5]*10
print(liste_c) # affiche [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
