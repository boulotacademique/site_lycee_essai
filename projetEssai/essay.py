mot_cache="SeehccraeCt"
mot = ""
for idx in range(len(mot_cache)):
    if idx%2 == 1: # On ne prend ques les indices impairs
        mot = mot_cache[idx] + mot	# On accumule les caractères à la fin (à droite)
print(mot) # affiche terceS