# Les méthodes de bases

## Les entrées/sortie (input/output)

!!! note "A retenir"

	Pour afficher **en console** un résultat, il suffit d'utiliser la fonction ```print``` ! Elle peut prendre 0 argument mais aussi plusieurs !

	```python
	print() # n'affiche rien, puis effectue un retour à la ligne
	print("Hello") # affiche Hello, puis effectue un retour à la ligne
	print(3+5) # affiche 8, puis effectue un retour à la ligne
	print(3+5,"hello") # affiche 8 hello (notez l'espace !!), puis effectue un retour à la ligne
	```

	Cette fonction renvoie ```None``` : c'est-à-dire rien !

Il est préférable d'utiliser une chaine de caractère dans un ```print```. Pour cela, il suffit d'utiliser [la concaténation](AFAIRE) et [le transtypage](AFAIRE) ou la méthode ```format```.



!!! note "A retenir"

	Pour récupérer ce qu'un utilisateur tape au clavier, il suffit d'utiliser la fonction ```input``` ! Elle peut prendre 0 argument mais aussi plusieurs ! En général, on utilisera un argument qui est une chaîne de caractères (c'est-à-dire un texte) qui explique à l'utilisateur ce qu'il doit faire !

	Cette fonction renvoie **une chaîne de caractère** (type ```str```). Il faut donc la récupérer dans une variable !

	```python
	nom = input() # n'affiche rien mais attend que l'utilisateur tape au clavier
	nom = input("Votre nom ? ") # affiche Votre nom ?, puis attend que l'utilisateur tape au clavier
	```

!!! warning "Attention"

	Ce que renvoie ```input``` est un ```str``` ! Il est donc impossible de faire des opérations mathématiques avec !

	Si nécessaire, il faut le transtyper (*cast* en anglais), par exemple, avec les fonctions :
	
	- ```int``` pour avoir un entier
	- ```float``` pour avoir un réel

	```python
	age = input("Votre age ? ") # age est du type str
	annee_naissance = 2023 - age # déclenche une erreur TypeError: unsupported operand type(s) for -: 'str' and 'int'
	```

	```python
	age = int(input("Votre age ? ")) # age est maintenant du type int
	annee_naissance = 2023 - age # le calcul est bien effectué
	```