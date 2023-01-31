# Suites et python

## Suite définie de façon explicite

<!--!!! tip "Méthode"-->
Pour déterminer, dans le cas d'une suite définie explicitement, il suffit d'utiliser la même méthode que pour calculer une image d'une fonction.

```python
def f(x):
	return -5+7*x

def suiteU(n):
	return f(n)

n=5
print("u("+str(n)+") = "+str(suiteU(5)))
```

affiche

```python
u(5) = 30
```

L'utilisation d'une fonction python pour $f$ simplifie le calcul pour une autre suite : 
il suffit de modifier cette fonction python.

??? question "Exercice"
	Quelle est la suite définie par le programme précédent ?
	
??? question "Exercice"
	Ecrire un programme qui fait la même chose, mais sans utiliser la fonction `def f(x)`.

## Suite définie par une relation de récurrence - Boucle `for`

!!! warning "Rappel"
	La boucle `for`

!!! tip "Méthode"
	Pour calculer $u_n$ avec une suite définie par récurrence
	
	```python
	def suiteU(n,u0):
		u=u0
		for i in range(n):
			u=0.75*u+4
		return u
	
	n=10
	u0=2
	print("u("+str(n)+") = "+str(suiteU(n,u0)))
	```
	
	affiche
	
	```python
	u(10) = 15.211610794067383
	```
	
??? question "Exercice"
	
	1. Quelle est la suite définie par le programme précédent ? Que pouvez-vous modifier facilement ?
	2. En vous inspirant de l'exemple de la partie précédente, améliorez-le !
	3. Modifiez ce programme pour qu'il affiche toutes les valeurs intermédiares de la suite.

	??? done "Solution"	
		1. 
		2.	
			```python
			def f(x):
				return 0.75*x+4

			def suiteU(n,u0):
				u=u0
				for i in range(n):
					u=f(u)
				return u

			n=10
			u0=2
			print("u("+str(n)+") = "+str(suiteU(n,u0)))
			```
		3. 
			```python
			def f(x):
				return 0.75*x+4

			def suiteU(n,u0):
				u=u0
				for i in range(n):
					print(u)
					u=f(u)
				return u

			n=10
			u0=2
			print("u("+str(n)+") = "+str(suiteU(n,u0)))
			```
			
			La place du `print(u)` est important. Essayez de la positionner après `u=f(u)`
		
## Suite définie par une relation de récurrence - Boucle `while`

??? question "Exercice" 
	1. Quelle est l'énorme erreur du code suivant ? **ERREUR A NE JAMAIS FAIRE**</br>
	```python
	def f(x):
		return 0.75*x+4
	
	def suiteU(n,u0):
		u=u0
		ind=0
		while ind<n:
			u=f(u)
		return u

	n=10
	u0=2
	print("u("+str(n)+") = "+str(suiteU(n,u0)))
	```
	2. Modifiez-le !
	
	??? done "Solution" 
		1. Il ya une boucle infinie, car la condition du `while` n'est jamais modifiée !
		2. 
		```python
		def f(x):
			return 0.75*x+4
		
		def suiteU(n,u0):
			u=u0
			ind=0
			while ind<n:
				ind=ind+1
				u=f(u)
			return u

		n=10
		u0=2
		print("u("+str(n)+") = "+str(suiteU(n,u0)))
	```

## Somme des termes d'une suite

Pour calculer une somme de termes, il faut une variable qui va accumuler en les ajoutant les termes
au fur et à mesure.

```python
def f(x):
	return -5+7*x

def suiteU(n):
	return f(n)
	
def somme(n):
	S=0
	for i in range(n+1):
		S=S+suiteU(i)
	return S

n=10
print('Sa somme u(0)+...+u('+str(n)+') = ',somme(n))
```

??? question "Exercice"
	Soit 
	
	\[
	\left\{
	\begin{array}{lcl}
	u_0 = 3000 \\
	u_{n+1} = 0.9u_n+100
	\end{array}
	\right.
	\]
	
	Ecrivez le programme qui retourne $u_0+u_1+\ldots+u_{n}$ en fonction de $n$.

## Calcul de l'indice d'une valeur seuil

Le but est de déterminer un indice $p$ tel que $u_p > v$, où $v$ est une valeur précisée par le contexte.

A FAIRE