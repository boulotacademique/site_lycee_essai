# Les chaînes de caractères : str

## Les indices

!!! info "A retenir"

	Une chaîne de caractère est de type ```str```. Elle peut être écrite 
	
	- entre des guillemets simples ``` 'Bonjour !' ```
	- entre des guillemets doubles ``` "Bonjour !" ```
	- entre des guillemets doubles répétés trois fois ``` """Bonjour !""" ```
  
	Dans une chaîne, chaque caractère est repéré par un indice !

	
	<div class = "Center_seul">
	
	|chaîne : |B|o|n|j|o|u|r| |!|
	|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
	|Indice : |0|1|2|3|4|5|6|7|8|

	</div>

!!! warning "Attention"

	En python, les indices commencent toujours **à 0 !**

!!! tip "A connaître"

	Dans tout ce qui suit, on utilise l'exemple suivant :

	```python
	mot = "Bonjour !"
	```

	- connaitre le nombre de caractères ou la longueur d'une chaîne : ```len(mot)``` correspond à ```9```
	- accéder à un caractère à partir de son indice : ```mot[2]``` correspond à ```n```
	- accéder aux derniers caractères : ```mot[len(mot)-1]``` correspond à ```!```. On peut aussi écrire ```mot[-1]```
	- accéder à une tranche : ```mot[2:5]``` correspond aux caractères dont les indices sont supérieurs ou égaux à 2 et **strictement inférieur** à 5. Ainsi, ```mot[2:5]``` correspond à ```njo```
	- accéder à une tranche contenant les premiers caractères : ```mot[0:5]``` correspond aux 5 premiers caractères (dont les indices sont supérieurs ou égaux à 0 et **strictement inférieur** à 5). Ainsi, ```mot[0:5]``` correspond à ```Bonjo```. On peut aussi écrire ```mot[:5]```
	- accéder à une tranche depuis le dernier caractère : ```mot[len(mot)-3:len(mot)]``` correspond aux 3 derniers caractères. Ainsi, ```mot[len(mot)-3:len(mot)]``` correspond à ```r !```. On peut aussi écrire ```mot[-3:]`
	- accéder à toute la chaîne sauf les derniers : ```mot[0:len(mot)-5]``` correspond à toute la chaîne **sauf** les 5 derniers caractères. Ainsi, ```mot[0:len(mot) - 5]``` correspond à ```Bonj```. On peut aussi écrire ```mot[:-5]```

En résumé:

```python
mot = "Bonjour !"
print(len(mot)) # affiche 9
print(mot[2]) # affiche n
print(mot[len(mot)-1]) # affiche !
print(mot[-1]) # affiche !
print(mot[2:5]) # affiche njo
print(mot[0:5]) # affiche Bonjo
print(mot[:5]) # affiche Bonjo
print(mot[len(mot)-3:len(mot)]) # affiche r !
print(mot[-3:]) # affiche r !
print(mot[0:len(mot)-5]) # affiche Bonj
print(mot[:-5]) # affiche Bonj
```

!!! warning "Attention"

	Le nombre de caractères **ne correspond pas** au dernier indice ! En effet, le dernier indice est toujours ```len(...) - 1```.

## Concaténation et répétition

!!! tip "A connaître"

	Dans tout ce qui suit, on utilise l'exemple suivant :
	
	```python
	mot = "Bonjour !"
	mot_suiv = "Tout le monde !"
	```

	- La <span class = "Gras" id = "concat">concaténation</span> consiste à coller plusieurs chaines de caractères. Cela s'effectue à l'aide du symbole ```+```. Ainsi, ```mot + " " + mot_suiv``` correspond à ```Bonjour ! Tout le monde !```
	- Pour répéter une chaine : ```mot*2``` correspond à ```'Bonjour !Bonjour !'``` et ```"a"*5``` correpsond à ```aaaaa```

## Manipulation des chaînes de caractères

### Parcourir une chaîne de caractères

!!! info "Parcourir une chaîne de caractères avec des indices"

	POur récupérer les caractères d'une chaîne les uns après les autres **avec les indices**, il faut utiliser une boucle ```for```, la fonction ```range``` et la longueur de la chaîne.

	```python
	mot = "Bonjour !"
	for idx in range(len(mot)):
		car = mot[idx]
		print(car)
	```
	affiche

	<div class = "Center_seul" style="width:10%;">

	```python
	B
	o
	n
	j
	o
	u
	r

	!
	```

	</div>

Il est aussi possible de ne pas passer par la variable ```car``` :

```python
mot = "Bonjour !"
for idx in range(len(mot)):
	print(mot[idx])
```

???- tip "Parcourir une chaîne de caractères sans les indices"

	POur récupérer les caractères d'une chaîne les uns après les autres **sans les indices**, il faut seulement utiliser une boucle ```for``. Il est alors plus difficile d'accéder aux indices !

	```python
	mot = "Bonjour !"
	for car in mot:
		print(car)
	```

	affiche

	<div class = "Center_seul" style="width:10%;">

	```python
	B
	o
	n
	j
	o
	u
	r

	!
	```

	</div>

## Modifier une chaîne de caractères

!!! warning "Attention"

	Une chaîne de caractères (type ```str```) est un [**non mutable**](AFAIRE) (ou **immuable**). Il est donc impossible de faire, par exemple, ```mot[2] = "r"``` !!

Pour modifier une chaîne de caractères, il est possible d'utiliser les tranches. Lire et bien travailler les exemples suivants afin de bien les comprendre.

!!! note "Insérer une chaîne"

	On souhaite insérer une chaîne de caractères (éventuellement un caractère seul) dans une chaîne. Par exemple, on souhaite insérer ```bon``` entre le ```n``` et l'espace dans la chaîne suivante.

	<div class = "Center_seul">
	
	|chaîne : |B|o|n| |!|
	|:-:|:-:|:-:|:-:|:-:|:-:|
	|Indice : |0|1|2|3|4|

	</div>

	Il faut [concaténer](#concat) les chaînes suivantes :
	
	- la chaîne dont les indices commencent à 0 et sont **strictement inférieur à 3** (Faite attention à ce dernier point !!!)
	- la chaîne que l'on souhaite insérer
	- la chaîne dont les indices vont de l'indice 3 jusqu'au dernier
	

	```python
	mot = "Bon !"
	a_inserer = "bon"
	mot2 = mot[0:3] + a_inserer + mot[3:]
	print(mot2) # affiche Bonbon !
	```

!!! note "Modifier **un** caractère"

	On souhaite modifier un caractère d'une chaîne. Par exemple, on souhaite corriger ```chebal```.

	<div class = "Center_seul">
	
	|chaîne : |c|h|e|b|a|l|
	|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
	|Indice : |0|1|2|3|4|5|

	</div>

	Il faut alors [concaténer](#concat) les chaînes suivantes :

	- la tranche du début jusqu'au caractère à remplacer
	- le caractère de remplacement
	- la tranche commençant **après** le caractère à remplacer

	```python
	mot = "chebal"
	mot2 = mot[0:3] + "v" + mot[4:] # voyez la différence avec l'insertion de la méthode précédente
	print(mot2) # affiche cheval !
	```



!!! note "Créer une chaîne de caractères"

	Il suffit de commencer avec une chaîne vide ```""``` et d'accumuler les chaînes de caractères voulues.

	```python
	mot_cache="Saebccrdeetf"
	mot = ""
	for idx in range(len(mot_cache)):
		if idx%2 == 0: # On ne prend ques les indices pairs
			mot = mot + mot_cache[idx]	# On accumule les caractères à la fin (à droite)
	print(mot) # affiche Secret
	```

???- "Accumuler au début"

	Il est possible d'accumuler au début (à gauche)

	```python
	mot_cache="Saebccrdeetf"
	mot = ""
	for idx in range(len(mot_cache)):
		if idx%2 == 0: # On ne prend ques les indices pairs
			mot = mot_cache[idx] + mot	# On accumule les caractères à la fin (à droite)
	print(mot) # affiche terceS
	```