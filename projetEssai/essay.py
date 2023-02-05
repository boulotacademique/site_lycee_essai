mot_cache="Saebccrdeetf"
mot = ""
for idx in range(len(mot_cache)):
    if idx%2 == 0: # On ne prend ques les indices pairs
        mot = mot_cache[idx] + mot  # On accumule les caractères à la fin (à droite)
print(mot) # affiche terceS
