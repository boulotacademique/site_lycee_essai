# Suites arithmétiques

!!! note "Définition"
	* Une suite $(u_n)$ est une suite  *arithmétique* de *raison* $r$ si  pour tout $n\in\mathbb{N}$ : $u_{n+1}=u_n+r$

!!! abstract "Théorème"
	* Une suite arithmétique est croissante si $r >0$ et décroissante si $r <0$	  
	* Pour tous $n,p\in \mathbb{N}$, on a :
		* $u_n=u_p+(n-p)r$
		* en particulier $u_n= u_0+nr$  
	* Dans un repère ,les points de coordonnées $(n,u_n)$ sont alignés sur une droite de coefficient directeur $r$.
	* La somme des $n$ premiers nombres entiers non nuls est: 
	
	\[
	1+2+3+\cdots +n=\sum_{k=1}^{n} k=\dfrac{n(n+1)}{2}
	\]
	
	*Histoire* : lisez l'article sur [Carl Friedrich Gauss](https://www.maths-et-tiques.fr/index.php/histoire-des-maths/mathematiciens-celebres/gauss)
	
	* Plus généralement, si $(u_n)$ est une suite arithmétique et $p\leqslant n$ :
	
		* $\sum\limits_{i=p}^n u_i = u_p+u_{p+1}+ \ldots + u_{n} = \dfrac{(u_p+u_n)(n-p+1)}{2}$
		* en particulier :
		
		\[
		\sum_{i=0}^n u_i = u_0+u_1+ \ldots + u_{n} = \dfrac{(u_0+u_n)(n+1)}{2}
		\]

!!! tip "Méthode"
	Cette dernière formule se retient sous la forme :
	
	$u_p+u_{p+1}+ \ldots + u_{n} = \dfrac{(\text{ premier terme }+\text{ dernier terme })(\text{ nombre de termes})}{2}$

	???- warning "ATTENTION"
		Le nombre de termes entre $u_p$ et $u_n$ ($p\leqslant n$ ) est $n-p+1$ !
		
		Vous pouvez aller voir [ici](https://warmaths.fr/MATH/geometr/Vocabulaire%20de%20base/intervalarith.htm) 
		ou [là](https://le-castillon.etab.ac-caen.fr/IMG/pdf/Intervalles_-_Cours_et_exercices.pdf)
	
Vous devez savoir justifier qu'une suite est une suite arithmétique (par le calcul ou dans un contexte d'évolution avec une valeur fixe).</br>
Vous devez savoir démontrer qu'une suite *n'est pas* une suite arithmétique.

??? question "Exercice"
	Les suites $(u_n)$ suivantes définies pour $n \in \mathbb{N}$ sont-elles arithmétiques?

	1. $u_n= 3n + 1$
	2. $u_n = n^2 +1$
	
	??? done "Solution"
		1. $u_{n+1}=3(n+1)+1=3n+1+3=u_n+3$ donc suite arithmétique de raison 3 et de premier terme 1.
		En effet, on a démontré que pour tout $n \in \mathbb{N}$, $u_{n+1} = u_n+3$.
		2. $u_{n+1}=(n+1)^2+1=n^2+2n+1+1=u_n+2n+1$ donc $u_n$ ne semble pas arithmétique. On peut alors le prouver avec un contre-exemple :</br>
		$u_1-u_0=1 \neq u_2-u_1$ ($=3$)
	
!!! warning "ATTENTION"
	Le calcul des premiers valeurs (même en très grand nombre) ne permet pas de justifier qu'une suite est une suite arithmétique !
	
	??? question "Exercice"
		Soit $(u_n)$ la suite définie sur $\mathbb{N}$ par 
		
		\[
		u_n=0.5n+4+n(n-1)(n-2)(n-3)(n-4)(n-5)\times 0.4^n
		\]
		
		1. Calculer les 5 premiers termes de la suite $(u_n)$.
		2. Que pouvez-vous conjecturer ?
		3. Comment se situent les points associés à une suite arithmétique ?
		4. Tracer le nuage de points de $(u_n)$ pour les dix premiers termes. Qu'en concluez-vous ?
		5. Modifier $u_n$ afin qu'elle semble arithmétique sur les $1000$ premiers termes.

??? question "Exercice"
	
	1. Représenter  à la calculatrice les termes de la suite $(u_n)$ définie pour tout $n\geq0$ par :
	
	\[
	\left\{
	\begin{array}{lcl}
	  u_{0} & = & 2 \\
	  u_{n+1}  & = &  u_n + 0.5
	\end{array}
	\right.
	\]
	
    2. Quelle est la nature de la suite $(u_n)$
	3. Exprimer $u_n$ en fonction de $n$ 
	4. Calculer $S_n= u_0+u_1+\ldots + u_n$
	
	