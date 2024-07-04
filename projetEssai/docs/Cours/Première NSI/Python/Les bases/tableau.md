# Python<br>Les tableaux

## Définition

!!! note "Définition"
    En informatique, un tableau est une suite d'éléments (de même type). Le nombre d'élément d'un tableau est fixé dès la création du tableau. En python, ces éléments sont notés entre crochets.  
    A l'instar des chaînes de caractères, les éléments d'une liste sont repérés par des indices, qui commencent à 0!
	
	<div class = "Center_txt">
	
	|tableau :|[|2|,|13|,|-4|,|25|,|0|]|
	|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
	|Indice :| |0| |1| |2| |3| |4| |

	</div>

!!! warning "Pas de vrai tableau en Python"    
    Pour Python, il y a une confusion entre deux structures (les tableaux et les listes) car la structure implémentée par Python est un mélange des deux. Ils sont tous les deux de type `list` !  
    C'est pourquoi la structure &laquo; tableau &raquo; sera de ce type.  

???- warning "Avantges et limites d'un tableau"

    - Il n'est pas simple **d'ajouter** un élément à un tableau. En effet, lors de la création d'un tableau une zone contingüe de la mémoire (i.e. des blocs mémoires qui sont les uns à côtés des autres) de taille prédéfinie est utilisé.  
    Il faut trouver un zone mémoire plus grande, copier tous les éléments du tableau et ajouter l'élément voulu.  
    - Par contre, il est très aisé **d'accéder** à un élément dans un tableau à partir de l'indice de cet élément.  
    En effet, si un tableau à 5 éléments occupe les blocs mémoires `0011`, `0012`, `0013`, `0014`, `0015`. Ce tableau sera connu par l'addresse du premier bloc `0011` et par sa taille. Pour accéder à un élément d'indice $3$, il suffit d'aller au bloc `0011` + 3.

!!! tip "Méthode"

    Voici un exemple de création d'un tableau de 5 éléments :

    ```python
    tab = [None]*5
    ```

    Remarque : un tel tableau sera considéré comme **non rempli**.  
    
    ou bien en plaçant immédiatement les éléments :  
    ```python
    tab = [12, 5, -4, 30, 15]
    ```  

    - Pour accéder à la taille (i.e. le nombre d'éléments) : `len(tab)`
    - Pour modifier/ajouter un élément à l'indice `i` ($0\leq i < len(tab)$ ), il suffit d'écrire : `tab[i] = ...`
    - Pour accéder à l'élément d'indice `i` ($0\leq i < len(tab)$), il suffit d'écrire : `... = tab[i]`
    - Pour parcourir tout le tableau (soit pour modifier, soit pour accéder), on utilise une boucle `for` (cf méthode un peu plus loin)

!!! tip "Des méthodes communes aux tableaux et aux str ..."

    On retrouve des méthodes communes à celle des ```str``` !

	Dans tout ce qui suit, on utilise l'exemple suivant :

	```python
	tab_a = [1, -5, 10, 15, 2, 3, 6, 13]
	```

	- connaitre le nombre de caractères ou la longueur d'une chaîne : ```len(tab_a)``` correspond à ```8```
	- accéder à un caractère à partir de son indice : ```tab_a[2]``` correspond à ```10```
	- accéder aux derniers caractères : ```tab_a[len(tab_a)-1]``` correspond à ```13```. On peut aussi écrire ```tab_a[-1]```
	- accéder à une tranche : ```tab_a[2:5]``` correspond aux caractères dont les indices sont supérieurs ou égaux à 2 et **strictement inférieur** à 5. Ainsi, ```tab_a[2:5]``` correspond à ```[10,15,2]```
	- accéder à une tranche contenant les premiers caractères : ```tab_a[0:5]``` correspond aux 5 premiers caractères (dont les indices sont supérieurs ou égaux à 0 et **strictement inférieur** à 5). Ainsi, ```tab_a[0:5]``` correspond à ```[1,-5,10,15,2]```. On peut aussi écrire ```tab_a[:5]```
	- accéder à une tranche depuis le dernier caractère : ```tab_a[len(tab_a)-3:len(tab_a)]``` correspond aux 3 derniers caractères. Ainsi, ```tab_a[len(tab_a)-3:len(tab_a)]``` correspond à ```[3, 6, 13]```. On peut aussi écrire ```tab_a[-3:]`
	- accéder à tout le tableau sauf les derniers ; par exemple ```tab_a[0:len(tab_a)-5]``` correspond à toute la chaîne **sauf** les 5 derniers éléments. Ainsi, ```tab_a[0:len(tab_a) - 5]``` correspond à ```[1, -5, 10]```. On peut aussi écrire ```tab_a[:-5]```

    On trouve aussi <span class = "Gras" id = "repet_list">la répétition</span> ```liste_c = [5]*10```

{{ IDEv() }}

## Déclaration d'un tableau par compréhension

Il est possible de créer un tableau en décrivant ses éléments à l'aide d'une boucle ```for``` et d'une expression (ou d'une fonction) : on dit que la liste a été créée **par compréhension**.

Voyons cela sur un exemple :

<div class="Cote_demi">

<div class="Center_txt"> Créer un tableau classiquement </div>

```python
liste_carre = [None]*10
for i in range(10):
    liste_carre[idx] = i**2
```

</div>

<div class="Cote_demi">

<div class="Center_txt"> Créer un tableau par compréhension </div>

```python
liste_carre = [i**2 for i in range(10) ]
```
</div>



## Méthodes spécifiques aux tableaux

!!! warning "... et celles spécifiques aux tableaux"

    Les tableaux sont des [mutables](AFAIRE) ! Ils possèdent donc des méthodes spécifiques qui modifient directement (en place dit-on) la liste en question :

    - modifier un élément en connaissant son indice : ```tab_a[2] = 300```


{{ IDE('Python_base_code/list_02', MAX = 1000) }}

## Parcourir un tableau

!!! info "Parcourir une tableau avec des indices"

    Pour récupérer les éléments d'un tableau les uns après les autres **avec les indices**, il faut utiliser une boucle ```for```, la fonction ```range``` et la longueur du tableau.

	```python
	tab_a = [1,5,2,6,4,7,8]
	for idx in range(len(tab_a)):
		elt = tab_a[idx]
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
tab_a = [1,5,2,6,4,7,8]
for idx in range(len(tab_a)):
    print(tab_a[idx])
```

???- tip "Parcourir un tableau sans les indices"

    Pour récupérer les éléments d'un tableau les uns après les autres **sans les indices**, il faut seulement utiliser une boucle ```for```. Il est alors plus difficile d'accéder aux indices.

	```python
	tab_a = [1,5,2,6,4,7,8]
	for elt in tab_a:
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

!!! info "A apprendre en faisant les exercices"

    - ```[ ]``` : le tableau vide. ```tab == []``` permet de tester si un tableau est vide.
    - ```4 in tab``` : retourne ```True``` si 4 est dans ```tab```, ```False``` sinon.
    - ```tab.index(x)``` : retourne l'indice de l'élément ```x``` (si il est dans ```tab```, sinon il y a un message d'erreur)
    - ```tab1 == tab2``` : retourne ```True``` si ```tab1``` et ```tab2``` sont identiques, ```False``` sinon.

## Les tableaux sont des mutables

Comme en python un tableau n'est qu'une liste, un tableau est un mutable.

!!! warning "Attention à la copie"

    En tant que mutable, la copie d'un tableau ... **n'est pas une vraie copie** ! C'est plutôt une sorte *d'alias*.

    ```python
    tab = [1,2,3,4,5]
    print(tab)
    cp_tap = tab #En fait cp_tab est un simple alias de tab
    cp_tab[3] = 1000 # et donc modifier ainsi cp_tab modifie aussi tab
    print("cp_tab :" + str(cp_tab))
    print("tab :" + str(tab))
    ```

    {{ IDEv() }}

???- done "Explication"

    En fait, la variable `tab` n'est pas directement associée à la zone mémoire où commence le tableau ! En effet, `tab` est associé à **l'adresse** de la zone mémoire où commence le tableau !  
    Et donc la copie ne fait que récupérer cette adresse !

!!! warning "Encore plus d'attention dans une fonction"

    La façon d'utiliser un mutable dans une fonction à des conséquences ... différentes !

    ```python
    def modif_debut_tab(tab, val):
        tab[0] = val
        print("Dans la fonction, tab vaut " + str(tab))

    un_tab = [1,2,3,4,5]
    print(un_tab)
    modif_debut_tab(un_tab,1000)
    print("En dehors de la fonction, tab vaut " + str(un_tab))
    ```

    {{ IDEv() }}

    Mais :

    ```python
    def modif_debut_tab2(tab, val):
        tab = [val] + tab[1:]
        print("Dans la fonction tab vaut " + str(tab))

    un_tab = [1,2,3,4,5]
    print(un_tab)
    modif_debut_tab2(un_tab,1000)
    print("En dehors de la fonction, tab vaut " + str(un_tab))
    ```



## Exercices

???+ question "Exercice - 1"

    On souhaite afficher les tarifs de réservation d'une salle d'un jeu se jouant de 2 à 12 joueurs.  
    Chaque paire de joueur payera 15€ et si il y a un nombre impair de joueur, le joueur supplémentaire payera 5€.

    1. Créer un tableau `nb_joueurs` (de taille adaptée) et le remplir avec les nombres de joueurs possibles (de 2 à 12).
    2. Rappeler la formule qui permet de connaitre le nombre de paire dans une équipe et la formule qui permet de trouver si il y a un joueur supplémentaire.
    3. Créer un tableau `prix` (de taille adaptée) et le remplir avec les prix.
    4. Créer une fonction qui prend en paramètre le nombre de joueur et renvoie le prix (dans cette fonction, copier-coller les codes qui créent les tableaux `nb_joueurs` et `prix`).
    5. Ecrire le code qui permet d'afficher  
    ```python
    "Pour 2 joueurs, le prix est 15 euros."
    "Pour 3 joueurs, le prix est 20 euros."
    ...
    ```

???+ question "Exercice - 2"
    Créer par compréhension les tableaux suivants :

    1. `tab = [1, 3, 5, 7, 9, 11, 13, 15, 17]`
    2. `tab = [0**2+3, 1**2+3, 2**2+3, 3**2+3, 4**2+3, 5**2+3]`
    3. `tab = ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa"]`

???+ question "Exercice - 3"
    
    1. On souhaite dessiner 20 cercles de rayon 10 aléatoirement placés.  
    Pour cela, il est possible de créer un tableau `abs_centre` avec des abscisses aléatoirement choisies entre 100 et 300 et un tableau `ord_centre` avec des ordonnées aléatoirement choisies entre 100 et 300.  

        1. Créer les tableaux `abs_centre` et `ord_centre` de taille adaptée.
        2. En utilisant la bibliothèque `random`, remplir les tableaux précédents.
        3. Faire la même chose mais cette fois par compréhension.
        4. En utilisant la bibliothèque `turtle` et après avoir écrit une fonction qui permet de tracer un cercle à partir de son centre, dessinez les cercles associés au tableau `abs_centre` et `ord_centre`.
