# Suite majorée, minorée , bornée

!!! note "Définition"
	Une suite $(u_n)$ est majorée par un nombre réel $M$ si  pour tout  $n\in \mathbb{N}, u_n \leq M$ (attention **$M$ ne dépend pas de $n$**)</br>
	
	Si une suite est majorée par $M$, elle a une infinité de majorants . En particulier , tout nombre supérieur à $M$ est aussi un majorant de la suite.

!!! note "Définition"
	Une suite $(u_n)$ est minorée par un nombre réel $m$ si  pour tout  $n\in \mathbb{N}, m \leq u_n$ (attention **$m$ ne dépend pas de $n$**)
	
	Si une suite est minorée par $m$, elle a une infinité de minorants. En particulier, tout nombre inférieur à $m$ est aussi un minorant de la suite.

!!! note "Définition"
	Une suite $(u_n)$ est bornée si elle est à la fois majorée et minorée.

!!! example "Exemple"
	* Une suite à termes positifs est minorée par 0
	* **A retenir :** Une suite croissante est minorée par son premier terme $u_0$ : $u_0 \leq u_1 \leq \cdots \leq u_n$
	* **A retenir :** Une suite décroissante est majorée par son premier terme $u_0$ : $u_n \leq \cdots \leq u_1 \leq u_0$ **A retenir**
	* La suite $u$ définie par $u_n=\sin n$  est minorée par -1 et majorée par 1 
	* La suite $u$ définie par $u_n=n$ est minorée par 0 et non majorée.
	* la suite définie pour $n \geq 1$ par $u_n=1+\dfrac{2}{n}$ est minorée par 1 et majorée par 3. Elle est bornée.</br>
	En effet pour $n \geq 1$, $\dfrac2n \leq 2$ donc $u_n \leq 3$, la suite est majorée par 3.</br>
	Pour $n \geq 1$, $\dfrac{2}{n} > 0$ donc $u_n > 1$, la suite est minorée par 1.

!!! tip "Méthode"
	* Technique algébrique : on manipule des inégalités ou on étudie le signe de $u_n-M$ ou $u_n-m$.
	* Technique fonctionnelle : si $u_n=f(n)$, le tableau de variations de $f$ permet de trouver (si ils existent) un majorant ou un minorant.
	* Il est possible d'utiliser une démonstration par récurrence.

??? question "Exercice"
	On considère la suite $(u_n)$ définie par 
	
	\[
	\left\{\begin{array}{lcl}
	u_0 & = & 1,8\\
	u_{n+1} & = & f(u_n)
	\end{array}\right.
	\]
	
	avec $f(x) =\dfrac{2}{3-x}$.
	On admet que $f$ est croissante sur $[0,3[$<!--]-->. 

	1. Emettre des conjectures sur la suite : variation ,majorant , minorant.
	2. Démontrer par récurrence les conjectures 
	
	??? done "Solution"
	1. La suite semble être décroissante , minorée par 1 et majorée par 2.
	2. Soit  $P(n)$ la propriété définie par $1 \leq u_{n+1} \leq u_n \leq 2$
	
		* **Initialisation**</br>
		pour $n=0$  on a:
		
		\[
		\left \{\begin{array}{l}
		u_0=1,8\\
		u_1=f(1,8)\approx1,67       
		\end{array}\right.
		\]
		
		donc $1 \leq u_1 \leq u_0 \leq 2$ $P(0)$ est vraie.
		
		* **Hérédité**</br>
		On suppose que pour un entier $k \in \mathbb{N}$, $P(k)$ est vraie , c'est-à-dire $1 \leq u_{k+1} \leq u_k \leq 2$ 
		et on démontre que $P(k+1)$ est vraie , c'est-à-dire : $0 < u_{k+2} \leq u_{k+1} \leq 2$.</br>
		D'après l'hypothèse  de récurrence</br>
		$1 \leq u_{k+1}  \leq  u_k \leq 2$  donc comme $f$ est croissante sur$[0,3[$<!--]--> on a  $f(1) \leq f(u_{k+1}) \leq f(u_k) \leq f(2)$</br>
		C'est-à-dire : $1 \leq u_{k+2} \leq u_{k+1} \leq 2$.</br>
		Donc **si $P(n)$ est vraie alors$P(n+1)$ est vraie**.
	
		* **Conclusion**</br>
		Pour tout entier naturel $n \in \mathbb{N}$ ,$P(n)$ est vraie c'est-à-dire $1 \leq u_{n+1} \leq u_n \leq 2$.

