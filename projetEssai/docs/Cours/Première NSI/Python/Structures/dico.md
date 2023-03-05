# les dictionnaires

## Définition

Un dictionnaire est basé sur les ensembles (une autre structure informatique) qui possède les principales caractéristiques d'un ensemble mathématiques :

- il n'y a pas d'ordre (en effet $S = \{0;3;1 \} = \{ 3;0 ; 1\} = \{ 1;0 ; 3\}$)
- il n'y a pas de répétition possible {-- {0;0;2;3} --}

???- warning "Pas d'ordre donc pas d'indice"
    Comme un ensemble n'a pas d'ordre, parler de premier élément ou d'élément d'indice 0 n'a pas de sens !

!!! info "Définition d'un dictionnaire"
    Un **dictionnaire** en python est un ensemble d'élément composé d'une clé et d'une valeur. Un dictionnaire s'écrit de la façon suivante :

    ```py
    dico = {cle1 : valeur1, cle2 : valeur2, ...}
    ```

    Il est impossible d'avoir 2 fois la même clé dans un dictionnaire. Mais les valeurs pour des clés différentes peuvent être identiques.

    Les clés sont de préférence des immuables. Dans ce cours, les clés seront des chaines de caractères.

!!! tip "Dictionnaire vide"
    Le dictionnaire vide est noté ```{}```

???- example "Exemples de dictionnaire"

    Voici différents exemples de dictionnaire :

    - les valeurs sont des entiers
    
    ```python
    numPrison = {'Jack' : 104020305, 'Averell' : 8888888888, 'William' : 142014338}
    ```

    - les valeurs sont des listes

    ```python
    liste_note = {"Francais" : [10,12,20], "NSI" : [15,12,16,8], "Math" : [8,10,13]}
    ```

    - les valeurs sont de types différents

    ```python
    avatar = {"Image" : "./Image/av01.png", "code_id" : 21456, "Abonne" : False}
    ```

    - les valeurs sont des ...dictionnaires

    ```python
    contacts = {"Luke Skywalker" : {"Age" : 27, "Planete" : "Tatooine", "Jedi" : True},
    "Han Solo" : {"Age" : 35, "Planete" : "Corellia", "Jedi" : False}}
    ```

## Manipulation d'un dictionnaire

Dans la suite, on utilisera 

```python
avatar = {"Image" : "./Image/av01.png", "code_id" : 21456, "Abonne" : False}
```

!!! info "Accéder à une valeur"
    Accéder à une valeur à partir d'une clé : ```dico[clé]```

    ```python
    print(avatar["code_id"]) # affiche 21456
    # ou une variable contenant une clé
    c = "code_id"
    print(avatar[c]) # affiche 21456
    ```

!!! info "Modifier une valeur"
    Modifier une valeur associée à une clé : ```dico[clé] = nouvelle_valeur```

    ```python
    avatar["Abonne"] = True
    print(avatar)
    # affiche {"Image" : "./Image/av01.png", "code_id" : 21456, "Abonne" : True}
    ```

!!! info "Ajouter une paire clé:valeur"
    **Si la clé n'existe pas dans un dictionnaire** : ```dico[nouvelle_clé] = valeur```

    ```python
    avatar["Pseudo"] = "Last_jedi"
    print(avatar)
    # affiche
    # {"Image" : "./Image/av01.png", "code_id" : 21456, "Abonne" : False, "Pseudo" : "Last_jedi"}
    ```

## Créer un dictionnaire

!!! info "Créer un dictionnaire"
    Comme pour créer une liste, pour créer un dictionnaire, il faut partir d'un dictionnaire vide et ajouter les paires clé:valeur voulues.

    ```python
    liste_cle = ["Zeus", "Poseidon", "Hades", "Athena"]
    liste_valeur = [ 1000, 900, 950, 1100]
    dico_puissance = {}
    for idx in range(len(liste_cle)):
        cle = liste_cle[idx]
        val = liste_valeur[idx]
        dico_puissance[cle] = val
    print(dico_puissance)
    # affiche
    # {"Zeus" : 1000, "Poseidon" : 900, "Hades" : 950, "Athena" : 1100}
    ```

## Parcourir un dictionnaire

!!! info "Parcourir un dictionnaire avec des clés"

    La boucle ```for``` permet de parcourir les clés d'un dictionnaire.

    Par exemple :

    ```python
    for k in avatar:
        print(k)
    ```

    affiche

    ```python
    Image
    code_id
    Abonne
    Pseudo
    ```

    Et il est alors facile de récupérer les valeurs:

    ```python
    for k in avatar:
        val = avatar[k]
        print("clé : " + str(k) + " et valeur : " + str(val))
    ```

    affiche

    ```python
    clé : Image et valeur ./Image/av01.png
    clé : code_id et valeur 21456
    clé : Abonne et valeur True
    clé : Pseudo et valeur Last_jedi
    ```

???- tip "Parcourir avec clé et valeurs"
    Il est possible d'avoir la clé et la valeur avec ```items()```

    ```python
    for k,v in avatar.items():
        print("clé : " + str(k) + " et valeur : " + str(v))
    ```

    affiche

    ```python
    clé : Image et valeur ./Image/av01.png
    clé : code_id et valeur 21456
    clé : Abonne et valeur True
    clé : Pseudo et valeur Last_jedi
    ```    

