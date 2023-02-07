nb_ligne = int(input("Nombre de lignes ? "))
for co in range(nb_ligne):
    print(" "*(nb_ligne - (co+1)) + "^"*(2*co+1) + " "*(nb_ligne - (co+1)))