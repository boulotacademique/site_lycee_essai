# Suites géométriques

!!! note "Définition"
	Une suite $(u_n)$ est une suite  *géométrique* de *raison* $q$ ($q\neq 0$) si  pour tout $n\in\mathbb{N}$ : $u_{n+1}=qu_n$

!!! abstract "Théorème"
	Pour tous $n,p\in \mathbb{N}$, on a :
	
	* $u_n=u_p\times q^{n-p}$
	* en particulier $u_n= u_0\times q^n$

!!! abstract "Théorème"
	Soit $q$ un réel. La suite géométrique définie par :
	
	\[
	\left\{
	\begin{array}{lcl}
	  u_{0} & = & 1 \\
	  u_{n+1}  & = &  q u_n
	\end{array}
	\right.
	\]
	
	se note aussi $(q^n)_{n \in \mathbb{N}}$.
	
	* Le sens de variations dépend de la valeur de $q$ :
		* la suite $(q^n)_{n \in \mathbb{N}}$ est croissante si $q>1$
		* la suite $(q^n)_{n \in \mathbb{N}}$ est décroissante si $0<q<1$
		* la suite $(q^n)_{n \in \mathbb{N}}$ n'est pas monotone si $q<0$
	* La somme des $(n+1)$ premières puissances d'un nombre réel $q\neq 1$ est :
	
	\[
	S=1+q+q^2+ \dots \,+q^n=\sum_{k=0}^{n} q^k=\dfrac{1-q^{n+1}}{1-q}
	\]
	
	ou plus généralement (pour $p \leq n$):
	
	\[
	S_1=q^p+q^{p+1}+\dots \,+q^n=\sum_{k=0}^{n} q^k=\dfrac{1-q^{n-p+1}}{1-q}
	\]

??? question "Exercice"
	Que pensez-vous des cas $q=0$ et $q=1$ ?

Le théorème précédent permet de trouver des résultats analogues pour les suites géométriques en général.

* Le sens de variations d'une suite géométrique dépend de la valeur de $q$ et de son signe (Pourquoi ? à vous d'y répondre)
* Les formules de la somme conduisent facilement à celle d'une suite géométrique quelconque

!!! abstract "Théorème"
	Si $(u_n)$ est une suite géométrique
	
	* telle que $u_0>0$ et $q>1$, alors $(u_n)$ est croissante.
	* Si $(u_n)$ est une suite géométrique telle que $u_0>0$ et $0<q<1$, alors $(u_n)$ est décroissante.
	* Si $(u_n)$ est une suite géométrique $q<0$, alors $(u_n)$ n'est pas monotone.
	* si $p \leq n$ :
	
	\[
	S_n=\sum_{i=p}^n u_i = u_p+u_{p+1}+ \dots \,+u_n=u_p\dfrac{1-q^{n-p+1}}{1-q}
	\]
	
	En particulier :
	
	\[
	S_n=\sum_{i=0}^n u_i = u_0+u_{1}+ \dots \,+u_n=u_0\dfrac{1-q^{n+1}}{1-q}
	\]

??? question "Exercice"
	Donnez la formule dans le cas où $(u_n)$ est une suite géométrique de raison $q=1$.

??? question "Exercice"
	
	1. Représenter  à la calculatrice les termes de la suite $(u_n)$ définie pour tout $n\geq0$ par : $u_{n+1}=0,5 u _n $ et $u_0=2$
	2. Représenter  à la calculatrice les termes de la suite $(u_n)$ définie pour tout $n\geq0$ par : $u_{n+1}=-0,5 u _n $ et $u_0=2$
	3. Représenter  à la calculatrice les termes de la suite $(u_n)$ définie pour tout $n\geq0$ par : $u_{n+1}=1,2 u _n $ et $u_0=0,5$
	
??? question "Exercice"
	
	1. La suite $u$ définie pour tout entier naturel $n$ par  $u_{n+1} = 3 u_n +1$ avec $u_0=5$ est-elle arithmétique , géométrique ou ni l’une ni l’autre ?
	2. Démontrer que la suite $(v_n)$ définie pour tout entier naturel n , par  $v_n = u_n +\dfrac{1}{2}$   est une suite géométrique dont on
	déterminera le premier terme et la raison.
	3. Exprimer $v_n$ en fonction de $n$
	4. Calculer $S_n= \sum_{k=0}^{n}v_k$
	5. Déduire des questions précédentes l'expression de $u_n$ et de $R_n=\sum_{i=0}^n u_i$ en fonction de $n$.
	
	??? done "Solution"
	
		1. Ni l'un ni l'autre. En effet, comme $u_0=5$, $u_1=16$ et $u_2=49$, $u_1-u_0 \neq u_2-u_1$ et $\dfrac{u_1}{u_0} \neq \dfrac{u_2}{u_1}$.
		2. 
		
		\begin{eqnarray}
			v_{n+1} & = & u_{n+1}+\dfrac 12\\
			 & = & 3u_n+1+\dfrac12\\
			 & = & 3u_n+\dfrac32\\
			 & = & 3(u_n+\dfrac12)\\
			 & = & 3v_n
		\end{eqnarray}
		
		$(v_n)$ est une suite géométrique de raison 3 et de premier terme $v_0= \dfrac{11}{2}$.</br>
		3. $v_n= v_0q^n= \dfrac{11}{2} \times 3^n$.</br>
		4. $S_n=v_0+v_1+\cdots v_n=  \dfrac{11}{2}+\dfrac{11}{2} \times 3+\cdots \dfrac{11}{2} \times 3^n$</br>
		$S_n=  \dfrac{11}{2}(1+3+\cdots 3^n)=  \dfrac{11}{2}\left(\dfrac{1-3^{n+1}}{1-3}\right)=  -\dfrac{11}{4}(1-3^{n+1})=\dfrac{11}{4}(3^{n+1}-1)$
	
		**Remarque** :</br>
		Pour la question 2., lorsque le facteur n'est pas évident ou lorsque l'expression de $v_n$ est plus compliquée,
		il est préférable d'utiliser la méthode suivante :</br>
		De $v_n=u_n+\dfrac{1}{2}$, on trouve $u_n=v_n-\dfrac{1}{2}$.</br>
		Or $v_{n+1} = 3 u_n + \dfrac{3}{2}$, donc $v_{n+1}=3 \left( v_n-\dfrac{1}{2} \right)+\dfrac{3}{2}=3v_n$.
		
		
!!! info "A lire"
	suite arithmético géométrique [Plan de remboursement](https://fr.wikipedia.org/wiki/Plan_de_remboursement)</br>
	Pour une lecture lors des soirées d'hiver [$1+2+3+4+5+\ldots = - \dfrac{1}{12}$](https://images.math.cnrs.fr/La-somme-des-entiers.html)

		