mot = "Bonjour"
rep = len(mot)
trouve = False
for idx in range(len(mot)):
    if not(trouve) and mot[idx] == "o":
        trouve = True
        rep = idx
print(rep)