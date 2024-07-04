# Les listes (suite)



## Insérer une liste dans une liste

Pour insérer des éléments dans une liste, il est possible d'utiliser les tranches. <!--Lire et bien travailler les exemples suivants afin de bien les comprendre.-->

!!! note "Insérer une liste"

	On souhaite insérer une liste (éventuellement contenant un seul élément) dans une autre liste. Par exemple, dans la liste ```liste_a = [1,5,2,6,4,7,8]```, on souhaite insérer ```[100 , 101]``` entre le ```2``` et le ```6```.

	<div class = "Center_ss_bdseul">
	
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
	a_inserer = [100 , 101] # ATTENTION il faut une liste ! Même pour un élément !
	liste_a = liste_a[0:3] + a_inserer + liste_a[3:]
	print(liste_a) # affiche [1,5,2,100,101,6,4,7,8]
	```

???+ tip "Ajouter une liste à la fin"

	Il est inutile d'utiliser des tranches ! Il suffit de [concaténer](#concat) à droite.

	```python
	liste_a = [1,5,2,6,4,7,8]
	a_inserer = [100, 150] # ATTENTION il faut une liste ! Même pour un élément !
	liste_a = liste_a + a_inserer
	print(liste_a) # affiche [1,5,2,6,4,7,8,100,150]
	```

!!! warning "Ajouter **un** élément à la fin d'une liste : append"

    Pour ajouter un élément à la fin, il est préférable d'utiliser ```liste_a.append(100)``` !

???+ tip "Ajouter une liste au début"

	Cela revient à ajouter une liste à la fin, non ?

	```python
	liste_a = [1,5,2,6,4,7,8]
	debut = [100, 150] # ATTENTION il faut une liste ! Même pour un élément !
	liste_a = debut + liste_a
	print(liste_a) # affiche [100,150,1,5,2,6,4,7,8]
	```

???+ danger "Les listes sont des mutables !"

    En tant que [mutable](AFAIRE), une affectation ```liste_a =``` doit être utilisée en connaissance de cause, en particulier dans des [fonctions](AFAIRE) ! Il est souvent préférable d'utiliser une boucle ```for``` et la méthode ```append``` !

	```python
	liste_a = [1,5,2,6,4,7,8]
	a_inserer = [100, 150] # ATTENTION il faut une liste ! Même pour un élément !
    for idx in range(len(a_inserer)):
	    liste_a.append(a_inserer[idx])
	print(liste_a) # affiche [1,5,2,6,4,7,8,100,150]
	```