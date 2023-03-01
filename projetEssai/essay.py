avatar = {"Image" : "./Image/av01.png", "code_id" : 21456, "Abonne" : False}

print(avatar["code_id"]) # affiche 21456
# ou une variable contenant une clé
c = "code_id"
print(avatar[c]) # affiche 21456

avatar["Abonne"] = True
print(avatar)
avatar["Pseudo"] = "Last_jedi"
print(avatar)

liste_cle = ["Zeus", "Poseidon", "Hades", "Athena"]
liste_valeur = [ 1000, 900, 950, 1100]
dico_puissance = {}
for idx in range(len(liste_cle)):
    cle = liste_cle[idx]
    val = liste_valeur[idx]
    dico_puissance[cle] = val
print(dico_puissance)

for k in avatar:
    print(k)    

for k in avatar:
   val = avatar[k]
   print("clé : " + str(k) + " et valeur : " + str(val))