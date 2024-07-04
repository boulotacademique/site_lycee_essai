# Raisonnement par récurrence

Le raisonnement par récurrence s'apparente à la théorie des dominos.</br>
On considère une suite de dominos.</br>
Quelles sont les deux conditions pour que tous les dominos tombent ?

* Faire tomber le premier domino 
* et s'assurer que chaque domino renverse le suivant 

[![Suite récurrente Domino](../Image/Domino2.png){.Center_lien .VignetteMed}](../Image/Domino2.png)
<div class="Source"> <a href="https://www.maths-et-tiques.fr/"><i>D'après  :</i> maths-et-tiques.fr</a></div>

Lire [Wikipédia](https://fr.wikipedia.org/wiki/Raisonnement_par_r%C3%A9currence)

!!! abstract "Le principe"
	Soit une proposition $P(n)$ (on lit &laquo;$P$ au rang n&raquo; ) dépendant d'un entier naturel $n$. 

	* Etape 1: **initialisation**: on vérifie que la proposition est vraie pour la plus petite valeur $n_0$,
    * Etape 2: **hérédité**: on suppose que pour **un** certain rang $k\geq n_0$ la proposition $P(k)$ est vraie 
	(on lit &laquo;$P$ est vraie au rang k&raquo; ) :c'est l'hypothèse de récurrence. Et on démontre que $P(k+1)$  est vraie.
	* Etape 3: **Conclusion**:   la proposition $P(n)$ est vraie pour tout entier naturel $n\geq n_0$.

!!! warning "ATTENTION"
	Une proposition est une phrase qui n'est pas obligatoirement une égalité ou une inégalité :
	
	* Pour $n \geq 2$, $P(n)$ est &laquo; le nombre de diagonale dans un polygone à $n$ sommet est $n$ &raquo; (cette proposition peut être vraie ou fausse).
	* Par contre, &laquo; la suite $u$ est croissante &raquo; est une proposition qui ne dépend pas de $n$. Elle ne convient pas pour un raisonnement 
	par récurrence. On utilisera $P(n)$ : &laquo; $u_{n+1} \geq u_{n}$ &raquo;.

!!! example "Exemple"
	Soit la suite ($u_n$) définie pour tout naturel $n$  par $u_0=2$ et par la relation de récurrence :  $u_{n+1}=3 u_n - 2$</br>
	Démontrer par récurrence que pour tout entier naturel $n$, on a  $u_n = 3^n+1$.
	
	??? done "Choix de la propoosition"
		Soit  $P(n)$ la proposition définie par &laquo; $u_n = 3^n+1$ &raquo;.
	
	??? done "Etape 1 : Initialisation"
		Pour $n=0$  on a:
		
		* $3^0+1=2$
		* et par ailleurs $u_0=2$

		donc  $u_0=3^0+1$.</br>
		La propriété est vraie pour $n=0$ donc  **$P(0)$ est   vraie**.

	??? done "Etape 2 : hérédité"
		On suppose que $P(k)$ est vraie pour un entier $k \geq 0 $, c'est-à-dire $u_k=3^{k}+1$ et on démontre que $P(k+1)$ est vraie, c'est-à-dire : $u_{k+1}=3^{k+1}+1$.<br>
		L'hypothèse de récurrence est donc &laquo; $u_k=3^{k}+1$ &raquo;.
		
		Par définition de la suite, $u_{k+1}=3u_k-2$.</br>
		Par hypothèse de récurrence : $u_k=3^{k}+1$</br>
		Donc $u_{k+1}=3\times(3^{k}+1)-2=3^{k+1}+1$.</br>
		Ainsi **la propriété est héréditaire !**
	
	??? done "Etape 3 : conclusion"
		La propriété est vraie pour $n =0$ et est héréditaire. Nous avons donc démontré par récurrence que pour tout entier naturel $n \in \mathbb{N}$ ,$P(n)$ est vraie c'est-à-dire $u_n = 3^n+1$

???- failure "Remarque"
	Si vous n'utilisez pas votre hypothèse de récurrence dans l'hérédité, il y a une erreur de raisonnement.

??? question "Exercice"
	On considère la suite $u$ définie pour tout entier naturel $n$ par 
	
	\[
	\left\{\begin{array}{l}
	u_0=1\\
	u_{n+1}=\sqrt{u_n+2}
	\end{array}\right.
	\]
	
	1. Quelle conjecture peut-on faire sur le signe de chaque terme de la suite et sur le sens de variation de la suite ?
	2. Démontrer ces conjectures par récurrence.
	
	??? done "Solution"	

		1. La suite semble être à termes positifs et croissante.
		2. Soit  $P(n)$ la propriété définie par $0<u_n \leq u_{n+1}$.
		
			* **Initialisation**</br>
			pour $n=0$  on a:
			
			\[
			\left\{\begin{array}{l}
			u_0=1\\
			u_1=\sqrt{u_0+2}=\sqrt{3}       
			\end{array}\right.
			\]
			
			donc $0<u_0 \leq u_1$. Donc $P(0)$ est   vraie.
			
			* **Hérédité**</br>
			On suppose que pour un entier $n \in \mathbb{N}$ ,$P(n)$ est vraie , c'est-à-dire $0<u_n \leq u_{n+1}$ et 
			on démontre que $P(n+1)$ est vraie, c'est-à-dire : $0<u_{n+1} \leq u_{n+2}$.\\		
			D'après l'hypothèse  de récurrence $0<u_n \leq u_{n+1}$ donc $0+2<u_n+2 \leq u_{n+1}+2$.</br>
			La fonction racine carrée étant strictement croissante sur $[0,+\infty[$<!--]-->, on obtient : </br>
			$\sqrt{2}<\sqrt{u_n+2} \leq \sqrt{u_{n+1}+2}$</br>
			soit $\sqrt{2}<u_{kn+1} \leq u_{n+2}$ \qquad mais $\sqrt{2}>0$ donc $0<u_{n+1} \leq u_{n+2}$
			donc **la propriété est héréditaire**.
			
			* **Conclusion**</br>
			La propriété est vraie pour $n =0$ et est héréditaire. On a donc démontré par récurrence : pour tout entier naturel $n \in \mathbb{N}$, $0<u_n \leq u_{n+1}$.
		
		Donc la suite $u$ est croissante et positive.
	
	
	
	
	
	
	
	
