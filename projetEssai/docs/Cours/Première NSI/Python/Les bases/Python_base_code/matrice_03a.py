nb_lig = 4
nb_col = 2
matrice = [None]*(nb_lig)
for idx in len(matrice):
    matrice[idx] = [None]*(nb_col)
for idx_lig in range(len(matrice)):
    for idx_col in range(len(matrice[0])):
        elt = "elt ("+ str(idx_lig)+","+str(idx_col)+")"
        matrice[idx_lig][idx_col] = elt


#Pour l'affichage
for idx in range(len(matrice)):
    print(matrice[idx])