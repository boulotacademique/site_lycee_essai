# Python<br>if, elif

## Test conditionnel if

!!! info "A retenir"

    La boucle ```if``` exécute certaines instructions si une condition (c'est un propriété qui est soit vraie soit fausse) est réalisée et d'autres sinon.
   
    ```python
    if age >= 18:
        print("Je suis majeur(e)")
    else:
        print("Je suis mineur(e)")
    ```

!!! warning "Attention"

    Toutes les lignes des instructions à exécuter dans un ```if``` ou un ```else``` doivent avoir un tabulation de plus que la ligne avec ```if``` ou ```else```.

    ```py
    a = int(input("Donner votre note entre 0 et 20 : "))
    if a < 10:
        print("Il faut revoir les bases") # uniquement pour une note < 10
        print("Vous ferez mieux la prochaine fois") # uniquement pour une note < 10
    else:
        print("Bon ensemble") # uniquement pour une note >= 10
    print("Revoyez les notions où vous vous êtes trompés.")  # pour toutes les notes
    ```

## elif

Il est possible de remplacer un 

```python
else:
    if ... :
```

par 

```python
elif ... :
```

???+ example "Exemple à bien comprendre"

    <div class = "Cote_demi"><div class = "Center_txt">Programme 1</div>

    ``` py
    un_nb = int(input("Choisir un entier entre 0 et 99 (inclus) "))
    if un_nb <= 20:
        print("Jeton bleu")
    if un_nb <= 50:
        print("Jeton vert")
    if un_nb <= 75:
        print("Jeton rouge")
    else:
        print("Jeton jaune")
    ```

    </div>
    <div class = "Cote_demi"><div class = "Center_txt">Programme 2</div>

    ``` python
    un_nb = int(input("Choisir un entier entre 0 et 99 (inclus) "))
    if un_nb <= 20:
        print("Jeton bleu")
    elif un_nb <= 50:
        print("Jeton vert")
    elif un_nb <= 75:
        print("Jeton rouge")
    else:
        print("Jeton jaune")
    ```

    </div>

    1. Qu'affiche le programme 1 si :
        1. ```un_nb``` vaut 18
        2. ```un_nb``` vaut 45
        3. ```un_nb``` vaut 72
        4. ```un_nb``` vaut 83
    2. Qu'affiche le programme 2 si :
        1. ```un_nb``` vaut 18
        2. ```un_nb``` vaut 45
        3. ```un_nb``` vaut 72
        4.  ```un_nb``` vaut 83

{{ IDEv('Python_base_code/if_elif_01', MAX = 1000) }}

{{ IDEv('Python_base_code/if_elif_02', MAX = 1000) }}

## Les conditions

!!! info "A retenir"

    Les conditions (dans un ```if``` ou un ```while```) sont des [**booléens**](AFAIRE). Elles ne peuvent donc prendre que deux valeurs : ```True``` ou ```False```

    Elles peuvent être obtenue de différentes façon :

    - un test 
    - des booléens séparés par ```or``` ou ```and```
    - un booléen retourné par une fonction
    - ```True``` ou ```False``` (A éviter si possible)
    - ...

!!! info "Les tests"

    Voici un liste (non exhaustive) des tests possibles :

    - test d'égalité : ```a == b``` (A ne pas faire avec [des flottants](AFAIRE))
    - test de la non égalité : ```a != b``` (A ne pas faire avec [des flottants](AFAIRE))
    - test d'inégailté strict : ```a > b``` ou ```a < b``` (avec des ```str``` voir [l'ordre lexicographique](./variables.md#ordre_lexico))
    - test d'inégailté large : ```a >= b``` ou ```a <= b``` (avec des ```str``` voir [l'ordre lexicographique](./variables.md#ordre_lexico))
    - test d'appartenance à une liste : ```x in liste1 ```
    - test d'appartenance à une chaîne de caractères : ```x in ch1 ```
    - test d'appartenance &laquo; aux clés d'un dictionnaires &raquo; : ```x in dico1 ```
    - test de type : ```isinstance(a , int)```, ```isinstance(a , bool)```, ```isinstance(a , list)```, ```isinstance(a , dict)```, ...
 
???- warning "Un bon usage"

    Il est inutile de tester si un booléen est égal à ```True``` !

    <div class = "Cote_demi"><div class = "Center_txt">A éviter</div>

    ``` python
    def est_mention_TB(note):
        if note >= 16:
            return True
        return False
    
    ma_note = int(input("Votre note ? "))
    if est_mention_TB(ma_note) == True: # Inutile !!
        print("Félicitation pour votre mention TB!")
    ```

    </div>
    <div class = "Cote_demi"><div class = "Center_txt">A préférer</div>

    ``` python
    def est_mention_TB(note):
        if note >= 16:
            return True
        return False
    
    ma_note = int(input("Votre note ? "))
    if est_mention_TB(ma_note):
        print("Félicitation pour votre mention TB!")
    ```
    </div>

    De façon analogue avec un ```False```, il est préférable d'utiliser un ```not``` !

    <div class = "Cote_demi"><div class = "Center_txt">A éviter</div>

    ``` python
    def avoir_le_bac(note):
        if note >= 10:
            return True
        return False
    
    ma_note = int(input("Votre note ? "))
    if avoir_le_bac(ma_note) == False: # Inutile !!
        print("Dommage ! Mais peut-être êtes-vous au rattrapage ?")
    ```

    </div>
    <div class = "Cote_demi"><div class = "Center_txt">A préférer</div>

    ``` python
    def avoir_le_bac(note):
        if note >= 10:
            return True
        return False
    
    ma_note = int(input("Votre note ? "))
    if not(avoir_le_bac(ma_note)):
        print("Dommage ! Mais peut-être êtes-vous au rattrapage ?")
    ```

    </div>

## Opérations sur les booléens

!!! info "L'opération OR"

    Si ```un_bool_01``` et ```un_bool_02``` sont deux variables de type booléens, alors ```un_bool_01 or un_bool_02``` :

    - renvoie ```True``` si <span class = "Gras">au moins</span> l'un des deux booléens (```un_bool_01```, ```un_bool_02```) vaut ```True``` 
    - et renvoie ```False``` si <span class = "Gras"> les deux </span> booléens (```un_bool_01```, ```un_bool_02```) valent ```False```

    Cette opération correspond au &laquo; ou non exclusif &raquo; du langage courant.

???- tip "Avec plus de deux termes"

    ```b1 or b2 or b3 or ... or bn``` :

    - renvoie ```True``` si <span class = "Gras">au moins</span> l'un des booléens (```b1, b2, b3, ..., bn```) vaut ```True``` 
    - et renvoie ```False``` si <span class = "Gras"> TOUS LES </span> booléens (```b1, b2, b3, ..., bn```) valent ```False```

!!! info "L'opération AND"

    Si ```un_bool_01``` et ```un_bool_02``` sont deux variables de type booléens, alors ```un_bool_01 and un_bool_02``` :

    - renvoie ```True``` si <span class = "Gras"> les deux </span> booléens (```un_bool_01```, ```un_bool_02```) valent ```True``` 
    - et renvoie ```False``` si <span class = "Gras"> au moins </span> l'un des deux booléens (```un_bool_01```, ```un_bool_02```) vaut ```False```

    Cette opération correspond au &laquo; et &raquo; du langage courant.

???- tip "Avec plus de deux termes"

    ```b1 and b2 and b3 and ... and bn``` :

    - renvoie ```True``` si <span class = "Gras">TOUS LES</span> booléens (```b1, b2, b3, ..., bn```) valent ```True``` 
    - et renvoie ```False``` si <span class = "Gras">au moins </span> l'un des booléens (```b1, b2, b3, ..., bn```) vaut ```False```

!!! info "L'opération NOT"

    Si ```un_bool_01``` est une variable de type booléen, alors ```not(un_bool_01)``` :

    - renvoie ```True``` si le booléen (```un_bool_01```) vaut ```False``` 
    - et renvoie ```False``` si le booléen (```un_bool_01```) vaut ```True``` 

    Cette opération correspond à la négation du langage courant.
