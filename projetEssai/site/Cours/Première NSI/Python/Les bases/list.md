# Les listes

## Définition

!!! info "A retenir"

    Une <span id="liste">**liste**</span> (ou du moins ce qui sera [appelée liste pour l'instant](AFAIRE)) est une structure de donnée _très importanate_ !

    C'est une séquence ou une suite (donc l'ordre compte) d'éléments (par forcément distincts) notée entre des crochets.

    ```python
    L = [2, 3, 4, "bonjour", True]
    ```

    A l'instar des chaînes de caractères, les éléments d'une liste sont repérés par des indices, qui commencent à 0!
	
	<div class = "Center_seul" style="width:80%;">
	
	|liste :|[|2|,|3|,|4|,|"bonjour"|,|True|]|
	|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
	|Indice :| |0| |1| |2| |3| |4| |

	</div>

!!! tip "Des méthodes communes aux list et aux str ..."

    On retrouve des méthodes communes à celle des ```str``` !

	Dans tout ce qui suit, on utilise l'exemple suivant :

	```python
	liste_a_ = [1, -5, 10, 15, 2, 3, 6, 13]
	```

	- connaitre le nombre de caractères ou la longueur d'une chaîne : ```len(liste_a)``` correspond à ```8```
	- accéder à un caractère à partir de son indice : ```liste_a[2]``` correspond à ```10```
	- accéder aux derniers caractères : ```liste_a[len(liste_a)-1]``` correspond à ```13```. On peut aussi écrire ```liste_a[-1]```
	- accéder à une tranche : ```liste_a[2:5]``` correspond aux caractères dont les indices sont supérieurs ou égaux à 2 et **strictement inférieur** à 5. Ainsi, ```liste_a[2:5]``` correspond à ```[10,15,2]```
	- accéder à une tranche contenant les premiers caractères : ```liste_a[0:5]``` correspond aux 5 premiers caractères (dont les indices sont supérieurs ou égaux à 0 et **strictement inférieur** à 5). Ainsi, ```liste_a[0:5]``` correspond à ```[1,-5,10,15,2]```. On peut aussi écrire ```liste_a[:5]```
	- accéder à une tranche depuis le dernier caractère : ```liste_a[len(liste_a)-3:len(liste_a)]``` correspond aux 3 derniers caractères. Ainsi, ```liste_a[len(liste_a)-3:len(liste_a)]``` correspond à ```[3, 6, 13]```. On peut aussi écrire ```liste_a[-3:]`
	- accéder à toute la chaîne sauf les derniers : ```liste_a[0:len(liste_a)-5]``` correspond à toute la chaîne **sauf** les 5 derniers caractères. Ainsi, ```liste_a[0:len(liste_a) - 5]``` correspond à ```[1, -5, 10]```. On peut aussi écrire ```liste_a[:-5]```

    On trouve aussi <span class = "Gras" id = "concat_list">la concaténation</span> : ```liste_b = liste_a + [1000]``` et <span class = "Gras" id = "repet_list">la répétition</span> ```liste_c = [5]*10```

    

    En résumé:

    ```python
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
    ```

## Méthodes spécifiques aux listes

!!! warning "... et celles spécifiques aux list"

    Les listes sont des [mutables](AFAIRE) ! Elles possèdent donc des méthodes spécifiques qui modifie directement (en place dit-on) la liste en question :

    - modifier un élément en connaissant son indice : ```liste_a[2] = 300```
    - ajouter un élément à la fin : ```liste_a.append(-25)```

    ```python
    liste_a = [1, -5, 10, 15, 2, 3, 6, 13]
    liste_a[2] = 300
    print(liste_a) # affiche [1, -5, 300, 15, 2, 3, 6, 13]
    liste_a.append(-25) # inutile d'utiliser une affection =
    print(liste_a) # affiche [1, -5, 300, 15, 2, 3, 6, 13, -25]
    ```

## Manipulation des listes

### Parcourir une liste

!!! info "Parcourir une liste avec des indices"

    Pour récupérer les éléments d'une listes les uns après les autres **avec les indices**, il faut utiliser une boucle ```for```, la fonction ```range``` et la longueur de la chaîne.

	```python
	liste_a = [1,5,2,6,4,7,8]
	for idx in range(len(liste_a)):
		elt = liste_a[idx]
		print(elt)
	```

	affiche

	<div class = "Center_ss_bd" style="width:10%;">

	```python
	1
    5
    2
    6
    4
    7
    8
	```

	</div>

Il est aussi possible de ne pas passer par la variable ```elt``` :

```python
liste_a = [1,5,2,6,4,7,8]
for idx in range(len(liste_a)):
    print(liste_a[idx])
```

???- tip "Parcourir une liste sans les indices"

    Pour récupérer les éléments d'une listes les uns après les autres **sans les indices**, il faut seulement utiliser une boucle ```for```. Il est alors plus difficile d'accéder aux indices.

	```python
	liste_a = [1,5,2,6,4,7,8]
	for elt in liste_a:
		print(elt)
	```

	affiche

	<div class = "Center_seul" style="width:10%;">

	```python
	1
    5
    2
    6
    4
    7
    8
	```

	</div>



### Créer une liste

!!! info "Créer une liste"

    Il suffit ce commencer avec une liste vide et d'accumuler les eléments voulus.

    ```python
    une_liste= [102, 104, 97, 97, 100, 97, 98, 99, 104, 99]
    liste = []
    for idx in range(len(une_liste)):
        if une_liste[idx]>=100:
            liste.append(une_liste[idx])
    print(liste) # affiche [102, 104, 100, 104]
    ```

### Diverses méthodes autour des listes

!!! info "A apprendre en faisant les exercices"

    - ```[ ]``` : la liste vide. ```L=[ ]``` permet de créer une liste à laquelle il sera possible d'ajouter des éléments
    - ```4 in L``` : retourne ```True``` si 4 est dans ``` L```, ```False``` sinon.
    - ```L.index(x)``` : retourne l'indice de l'élément ```x``` (si il est dans ```L```, sinon il y a un message d'erreur)
    - ```L.count(x)``` : retourne le nombre d'occurrences  de l'élément ```x``` (si il est dans la liste ```L```)
    - ```L1 == L2``` : retourne ```True``` si ```L1``` et ```L2``` sont identiques, ```False``` sinon.
    - ```for elt in L :``` : parcourt la liste ```L```
    - ```A = L``` : copie [**par référence**](AFAIRE) la liste ```L```



<!--## Exercices

???- question "Exercice"-->