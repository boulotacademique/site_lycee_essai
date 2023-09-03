# Bien écrire en python

!!! info "A retenir"

	Pour bien écrire un code python, il est indispensable de savoir écrire des mots, des syntaxes, des phrases (...) en python.

	Ainsi les principaux mots rencontrés sont ```if, else, elif, while, for, range, def, print, input, int, str```. **Ils ne commencent JAMAIS par une majuscule !**

!!! warning "Soyez attentifs"

	Certains éléments ne varient jamais ! Ainsi, les lignes commençant par ```if, else, elif, while, for, def``` se termine **toujours** par un &laquo; ```:``` &raquo;

	De plus la ligne suivante commence **toujours** avec une tabulation de plus que celle avec ```if, else, elif, while, for, def```

???- question "Exercice"

	Corriger les erreurs dans les codes suivants :

	1.
	```python
	If a>3
		print("C'est plus grand que 3 !")
	```
	2.
	```python
	for i in Range(2,5):
	print("Hello !")
	```

	???- success "Solution"

		AFAIRE

!!! info "A retenir"

	Certains mots en python désignent des fonctions. Il sont donc suivis de parenthèses (sauf dans certains cas cf [Callback](AFAIRE) par exemple !). A l'intérieur de ces parenthèses, il peut y avoir entre 0 et plusieurs paramètres qui seront **toujours** séparés par une virgule. Il faut bien respecter l'ordre imposé et le type de chaque paramètre imposé.

	A tout moment dans une console python, vous pouvez obtenir des renseignements sur une fonction en tapant ```help(nom_de_la_fonction)```

	Au début, vous utiliserez principalement les fonctions ```range, print, input, int, str```.

Ainsi, ```print``` est une fonction. Il y a donc toujours des parenthèses. Elle peut prendre 0 paramètre mais aussi plusieurs !

```python
print() # n'affiche rien, puis effectue un retour à la ligne
print("Hello") # affiche Hello, puis effectue un retour à la ligne
print(3+5) # affiche 8, puis effectue un retour à la ligne
print(3+5,"hello") # affiche 8 hello (notez l'espace !!), puis effectue un retour à la ligne
```
<div>

{{ IDEv('Python_base_code/ortho_01', MAX = 1000) }}

</div>

!!! warning "Très important"

	La fonction ```range``` prend **obligatoirement** au moins un paramètre ! Ainsi, {--```range()```--} déclenche une erreur !

	De plus, ces paramètres sont **toujours** de type ```int``` ! Ainis, si la variable ```liste``` contient une liste, {--```range(liste)```--} déclenche une erreur !

!!! info "Exemple à retenir" 

	<span id = "range">Rque</span> : afin d'avoir une vue pour ```range``` (cf [iterable](AFAIRE)), on le transforme en une liste !

	- La fonction ```range``` avec **un** argument :

		```python
		list(range(5)) # affiche [0,1,2,3,4]
		```

		Plus généralement, ```range(n)``` est une (sorte) de liste à $n$ éléments commençant à $0$. Elle se termine donc {==**à** $\mathbf{n-1}$==} !
	
	- La fonction ```range``` avec **deux** arguments :

		```python
		list(range(2,7)) # affiche [2,3,4,5,6]
		```

		Plus généralement, ```range(a,b)``` est une (sorte) de liste à $b - a$ éléments commençant à $a$. Elle se termine donc {==**à** $\mathbf{b-1}$==} !
	
	Il est possible d'utiliser la fonction ```range``` avec trois arguments : cf [ici](AFAIRE)


{{ IDEv('Python_base_code/ortho_02', MAX = 1000) }}

!!! tip "Bilan"

	Quand vous écrivez, du code python, en particulier sur feuille, pensez à vérifier ces éléments &laquo; d'orthographe &raquo;

