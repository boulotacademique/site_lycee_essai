
nb_lig = 4
nb_col = 2
matrice = [] # On va remplir cette matrice
for num_lig in range(nb_lig):
    ligne = [] # Il faut partir d'une ligne vide
    for num_col in range(nb_col):
        # On ajoute les éléments voulus
        ligne.append(f"elt ({num_lig},{num_col})")
    # Une fois la ligne remplie
    # on l'ajoute à notre matrice
    matrice.append(ligne)

#Pour l'affichage
for idx in range(len(matrice)):
    print(matrice[idx])