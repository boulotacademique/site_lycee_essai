# Suite et sens de variations

!!! note "Définition"
	* Une suite $(u_n)$ est  croissante ( à partir d'un certain rang $k$) si  pour tout $n\geqslant k$ , on a $u_{n}\leqslant u_{n+1}$
	* Une suite $(u_n)$ est  décroissante ( à partir d'un certain rang $k$) si  pour tout $n\geqslant k$, on a  $u_{n}\geqslant u_{n+1}$ 
	* Une suite $(u_n)$ est monotone ( à partir d'un certain rang $k$) si elle est croissante ou décroissante ( à partir d'un certain rang $k$) 

!!! warning "ATTENTION"
	Il existe des suites qui ne sont ni croissantes ni décroissantes par exemple $u_n=(-1)^n$ .

## Méthodes pour étudier le sens de variation 

### Suite définie par une relation explicite

!!! tip "**Technique algébrique**"

	On utilise la définition pour cela on étudie le signe de $u_{n+1}-u_n$

    * Si la quantité est positive à partir d'un certain rang $k$ , la suite est croissante pour $n\geqslant k$
    * Si la quantité est négative à partir d'un certain rang $k$ , la suite est décroissante pour $n\geqslant k$

!!! tip "**Technique fonctionnelle**"
	
    Si $u_n=f(n)$ où $f$ est une fonction définie et **monotone** sur $[0,+\infty[$, on étudie le sens de variation de $f$.
	En effet, sous cette hypothèse, la suite a les mêmes variations que la fonction.

	???- warning "ATTENTION"

		Il est possible d'avoir une fonction _non monotone_ sur  $[0,+\infty[$<!--]-->, et pourtant la suite définie par $u_n=f(n)$ est elle monotone.

!!! tip "**Comparaison avec 1**"

    Si la suite $u$ est à **termes strictement positifs** c'est-à-dire si  $u_n>0$ alors on peut comparer $\dfrac{u_{n+1}}{u_n}$ avec 1.
	
	* Si pour tout $n$ , $\dfrac{u_{n+1}}{u_n} \geq 1$ avec $u_n>0$ alors $u_{n+1} \geq u_n$ et la suite $u$ est croissante.
	* Si pour tout $n$ , $\dfrac{u_{n+1}}{u_n} \leq 1$ avec $u_n>0$ alors $u_{n+1} \leq u_n$ et la suite $u$ est décroissante.

	???- tip "Et si $u_n < 0$ ?"
		
        Pour cette méthode, il faut s'adapter si $u_n<0$ pour tout $n$.

        ???- done "Réponse"

            Si la suite $u$ est à **termes strictement négatifs** c'est-à-dire si  $u_n<0$ alors on peut comparer $\dfrac{u_{n+1}}{u_n}$ avec 1.
            
            * Si pour tout $n$ , $\dfrac{u_{n+1}}{u_n} \geq 1$ avec $u_n<0$ alors $u_{n+1} \leq u_n$ et la suite $u$ est décroissante.
            * Si pour tout $n$ , $\dfrac{u_{n+1}}{u_n} \leq 1$ avec $u_n<0$ alors $u_{n+1} \geq u_n$ et la suite $u$ est croissante.

	???- warning "ATTENTION"
    
		Naturellement, cette méthode est inutilisable si $(u_n)$ n'est pas (à partir d'un certain rang) de signe constant.		

!!! tip "**Utiliser une démonstration par récurrence**"

    cf [raisonnement par récurrence](AFAIRE)

Naturellement, il est possible d'utiliser les méthodes précédentes à partir d'un certain rang.

??? question "Exercice"
	Conjecturer à l'aide de la calculatrice le sens de variation de chacune des suites  $(u_n)$ et démontrer la conjecture .

	1. $u_n=- \dfrac{n^2+1}{2n}$ pour $n \geq 1$ 
	2. $u_n=\sqrt{n+1}$ pour $n\geq 0$
	3. $u_n=\dfrac{2^n}{n}$ pour $n\geq 1$

	??? done "Solution"
		1. Pour $n\geq 1$ , on a : $u_{n+1}-u_n=-\dfrac{(n+1)^2+1}{2(n+1)}+\dfrac{n^2+1}{2n}=\dfrac{-n^2-n+1}{2n(n+1)}$. </br>
		Or pour $n\geq 1$, on a $1-n \leq 0$ et donc $-n^2+1-n<0$</br>
		$2n(n+1)$>0 donc $u_{n+1}-u_n<0$ et la suite $(u_n) $ est  décroissante à partir du rang 1.
		2. $u_n=f(n)$ avec $f(x)=\sqrt{x+1}$</br>
		La fonction $f$ est croissante sur $[0,+\infty[$<!--]--> car elle a le même sens de variation que la fonction $x\mapsto x+1$ .</br>
		Pour tout $n\geq0$, on a $n+1\geq n$ donc $f(n+1)\geq f(n)$ soit $u_{n+1}\geq u_n$ et  la suite $(u_n)$ est croissante .</br>
		3. $\dfrac{u_{n+1}}{u_n}=\dfrac{2^{n+1}}{n+1}\times \dfrac{n}{2^n}=\dfrac{2n}{n+1}$</br>
		Pour $n\geq 1$ on a $2n\geq n+1$ donc $\dfrac{u_{n+1}}{u_n}\geq 1$ et  puisque $u_n>0$, $u_{n+1}\geq u_n$.  
		La suite $(u_n)$ est croissante à partir du rang 1.	

### Suite définie par une relation de récurrence

Ici, pas de méthode particulière. Il faut essayer de se ramener à une suite définie explicitement ou utiliser la définition.</br>
Pour ce dernier point, un raisonnement par récurrence est souvent approprié.










