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

    On trouve auusi la concaténation : ```liste_b = liste_a + [1000]``` et la répétition ```liste_c = [5]*10```

    

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

### Insérer une chaîne

Pour insérer des éléments dans une liste, il est possible d'utiliser les tranches. <!--Lire et bien travailler les exemples suivants afin de bien les comprendre.-->

!!! note "Insérer une chaîne"

	On souhaite insérer une liste (éventuellement contenant un seul élément) dans une chaîne. Par exemple, dans la liste ```liste_a = [1,5,2,6,4,7,8]```, on souhaite insérer ```100``` entre le ```2``` et le ```6```.

	<div class = "Center_seul">
	
	|chaîne :|[|1|,|5|,|2|,|6|,|4|,|7|,|8|]|
	|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
	|Indice :| |0| |1| |2| |3| |4| |5| |6| |7| |

	</div>

	Il faut [concaténer](#concat) les chaînes suivantes :
	
	- la sous liste dont les indices commencent à 0 et sont **strictement inférieur à 3** (Faite attention à ce dernier point !!!)
	- la liste que l'on souhaite insérer
	- la sous liste dont les indices vont de l'indice 3 jusqu'au dernier
	

	```python
	liste_a = [1,5,2,6,4,7,8]
	a_inserer = [100] # ATTENTION il faut une liste ! Même pour un élément !
	liste_a = liste_a[0:3] + a_inserer + liste_a[3:]
	print(liste_a) # affiche Bonbon !
	```

???- tip "Ajouter une liste à la fin"

	Il est inutile d'utiliser des tranches ! Il suffit de [concaténer](#concat) à droite.

	```python
	liste_a = [1,5,2,6,4,7,8]
	a_inserer = [100, 150] # ATTENTION il faut une liste ! Même pour un élément !
	liste_a = liste_a + a_inserer
	print(liste_a) # affiche [1,5,2,6,4,7,8,100,150]
	```

!!! warning "Ajouter **un** élément à la fin d'une liste : append"

    Pour ajouter un élément à la fin, il est préférable d'utiliser ```liste_a.append(100)``` !

???- tip "Ajouter une liste au début"

	Cela revient à ajouter une liste à la fin, non ?

	```python
	liste_a = [1,5,2,6,4,7,8]
	debut = [100, 150] # ATTENTION il faut une liste ! Même pour un élément !
	liste_a = debut + liste_a
	print(liste_a) # affiche [100,150,1,5,2,6,4,7,8]
	```

???- danger "Les listes sont des mutables !"

    En tant que [mutable](AFAIRE), une affectation ```liste_a =``` doit être utilisée en connaissance de cause, en particulier dans des [fonctions](AFAIRE) ! Il est souvent préférable d'utiliser une boucle ```for``` et la méthode ```append``` !

	```python
	liste_a = [1,5,2,6,4,7,8]
	a_inserer = [100, 150] # ATTENTION il faut une liste ! Même pour un élément !
    for idx in range(len(a_inserer)):
	    liste_a.append(a_inserer[idx])
	print(liste_a) # affiche [1,5,2,6,4,7,8,100,150]
	```

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

## Exercices

???- question "Exercice"