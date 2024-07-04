# Composition de fonctions

## Définition

!!! note "Définition"

	Soient $u$ une fonction définie sur un intervalle $I$ à valeurs dans un intervalle $J$ et $v$ une fonction définie sur l'intervalle $J$.
	
	**La composée de $\mathbf{u}$ par $\mathbf{v}$**, notée $v \circ u$, est la fonction définie sur $I$ par :

	\[ (v \circ u) (x) = v(u(x)) \]

	image AFAIRE

???- example "Exemple"
	
	On note $u(x)=x^2-1$, et $v(x)=\sqrt{x}$. Déterminer 

	1. $v \circ u$ définie sur  $I=]-\infty ; -1] \cup [1; + \infty[$
	2. $u \circ v$ définie sur $I=[0;+\infty[$

		???- done "Solution"
			
			1. $(v \circ u)(x)=\sqrt{x^2-1}$.
			2. $(u \circ v)(x)=\sqrt{x}^2-1=x-1$.

Vous aurez surtout besoin de savoir écrire une fonction comme étant la composée de deux fonctions de &laquo; référence &raquo;.

???- example "Exemple"

	Ecrire les fonctions suivantes comme la composée de deux fonctions à déterminer :

	1. $f(x)=\text{e}^{x^2+x}$
	2. $g(x)=\cos(3x+1)$
	3. $h(x)=\text{e}^{2x}+3\text{e}^{x}-5$

	???- done "Solution"

		1. $f(x)=(v \circ u)(x)$ où $u(x)=x^2+x$ et $v(x)=\text{e}^x$
		2. $g(x)=(v \circ u)(x)$ où $u(x)=3x+1$ et $v(x)=\cos(x)$
		3. $h(x)=(v \circ u)(x)$ où $u(x)=\text{e}^x$ et $v(x)=x^2+3x-5$
   
## Dérivée d'une composée.

!!! abstract "Théorème"

	Soient $v$  une fonction définie et dérivable sur $J$ et $u$ une fonction définie et dérivable sur $I$ tel que $u(x) \in J$ pour tout $x \in I$, alors la fonction $v \circ u$ est dérivable sur $I$ et :
	
	\[
	(v \circ u)'(x)=u'(x) \times v'(u(x))
	\]
	
	On note cette formule $(v \circ u)'=u' \times (v' \circ u)$


???- example "Exemple"

	Après avoir déterminer le domaine de dérivabilité, calculer la fonction dérivée des fonctions suivantes :
	
	1. $f(x)=\text{e}^{x^2-5x}$
	2. $g(x)=\sqrt{2-5x}$
	3. $h(x)=\text{e}^{4x+7}$
	4. $k(x)=(x^2-2x+1)^3$

	???- done "Solution"

	AFAIRE

???- warning "Remarque"

	Dans [le tableau des formules de dérivations](02_deriv_base_formule.md#Tab_cas_part), les cas particuliers rendent optionnels cette formule ... **cette année de terminale uniquement**.

	Par contre, écrire une fonction comme composée de deux fonctions est **indispensable** pour des calculs de limite. **Et cela dès cette année !**