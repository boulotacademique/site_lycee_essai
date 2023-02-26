# La fonction logarithme népérien

## Définition

La fonction exponentielle étant continue et strictement croissante sur $\R$, pour tout réel $a>0$ l'équation $\ex^x = a$ , a une unique solution appelée logarithme népérien  de $a$ et notée  $\ln(a)$.


<iframe scrolling="no" title="Construction point par point" src="https://www.geogebra.org/material/iframe/id/tmrvs3rf/width/1906/height/862/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/false/ctl/false" width="1906px" height="862px" style="border:0px;"> </iframe>

La fonction exponentielle et la fonction logarithme  népérien sont des fonctions réciproques. Dans un repère orthonormal les courbes représentatives des fonctions exponentielles et logarithme népérien sont symétriques par rapport à la droite d'équation $y = x$.

!!! info "La fonction logarithme"
	
	La fonction définie pour $x>0$ par $f(x)= \ln(x)$  est appelée fonction logarithme népérien. C'est la fonction réciproque de la fonction exponentielle. Ainsi : 
	
	\[
		\left. \begin{array}{lcl}
		y = \ln(x) \\
		\text{ et } x>0
		\end{array} \right\}  \equivaut x=\ex^y 
	\]

	Remarque : l'image d'un réel $x$ par la fonction  $\ln$  se note souvent $\ln x$  au lieu de $\ln(x)$.

!!! info "Conséquence immédiate"

	- Pour tout réel $x>0$, $\ex^{\ln x} = x$.
	- Pour tout réel $x$, $\ln \left( \ex^x \right) = x$.
	- $\ln 1= 0$ car $\ex^0 = 1$
	- $\ln \ex= 1$ car $\ex^1 = \ex$
	- $\ln \left( \dfrac{1}{\ex} \right)= -1$ car $\ex^{-1} = \dfrac{1}{\ex}$


???- example "Exemple"

	Simplifier les écritures :

	1. $\ln \ex^2 =$
	2. $\ln \ex^{-3} =$
	3. $\ex^{\ln 6} =$
	4. $\ex^{\ln 2+\ln 3} =$

	???- done "Réponse"
		
		1. $\ln \ex^2 = 2$
		2. $\ln \ex^{-3} = -3$
		3. $\ex^{\ln 6} = 6$
		4. $\ex^{\ln 2+\ln 3} = \ex^{\ln 2} \times \ex^{\ln 3} = 2 \times 3 = 6$

???- example "Exemple"
	Déterminer une solution aux équations suivantes :

	1. $\ln x = 4$
	2. $\ln x = -2$
	3. $3 \ln x = 2$
	
	???- done "Réponse"
		
		1. $\ln x = 4$  
        $x=\ex^4$
		2. $\ln x = -2$  
        $x = \ex^{-2}$
		3. $3 \ln x = 2$  
        $x = \ex^{\frac{2}{3}}$

## Propriétés

### Calcul et logarithme

!!! info "Propriétés algébriques"
	- Pour tous réels $a>0$ et $b>0$ : $\ln (ab)= \ln a + \ln b$.
	- Pour tout réel $a>0$ : $\ln \left( \dfrac{1}{a} \right) = - \ln a$.
	- Pour tous réels $a>0$ et $b>0$ : $\ln \left( \dfrac{a}{b} \right) = \ln a - \ln b$.
	- Pour tout réel $a>0$ et pour tout entier $n \in \Z$, $\ln \left( a^n \right) = n \ln a$.
	- Pour tout réel $a>0$ : $\ln \left( \sqrt{a} \right) = \dfrac{1}{2} \ln (a)$.
	
???- abstract "Démonstration"

	- Notons $x=\ln(ab)$.
	
	\begin{eqnarray*}
		x = \ln (ab) & \equivaut & \ex^x = \ex^{\ln(ab)}\\
		& \equivaut & \ex^x = ab\\
		& \equivaut & \ex^x = \ex^{\ln(a)} \times \ex^{\ln(b)}\\
		& \equivaut & \ex^x = \ex^{\ln(a)+\ln(b)}\\
		& \equivaut & x = \ln(a)+\ln(b)\\
	\end{eqnarray*}
	
	- Notons $x=\ln \left( \dfrac{1}{a} \right)$.

	\begin{eqnarray*}
		x=\ln \left( \dfrac{1}{a} \right) & \equivaut & \ex^x = \ex^{\ln \left( \frac{1}{a} \right)} \\
		& \equivaut & \ex^x = \dfrac{1}{a} \\
		& \equivaut & \ex^x = \dfrac{1}{\ex^{\ln a}}  \\
		& \equivaut & \ex^x = \ex^{-\ln a}  \\
		& \equivaut & x = -\ln a  
	\end{eqnarray*}

	- En utilisant les deux propriétés pérécedentes:

	- Notons $x=\ln \left( a^n \right)$
	
	\begin{eqnarray*}
		x=\ln \left( a^n \right) & \equivaut  & \ex^x = \ex^{\ln \left( a^n \right)}  \\
		& \equivaut & \ex^x = a^n\\
		& \equivaut & \ex^x = \left( \ex^{\ln a}\right)^n\\
		& \equivaut & \ex^x =  \ex^{n\ln a}\\
		& \equivaut & x = n\ln a
	\end{eqnarray*}

	\item Notons $A = \sqrt{a}$ et $x = \ln(a)$
	
	\begin{eqnarray*}
		x = ln (A^2) & \iff & x = 2\ln(A)\\
		& \iff & \dfrac{1}{2} x = \ln(A)
	\end{eqnarray*}
	
	Donc $\dfrac{1}{2} \ln(a) = \ln(\sqrt{a})$

!!! info "Variations de la fonction logarithme"
	La fonction $\ln$ est strictement croissante sur  $]0, +\infty[$.

### Résolution d'équation et d'inéquation

!!! info "Conséquences"

	- Si $a>0$ et $b>0$ : $\ln a = \ln b$ équivaut à $a=b$.
	- Si $a>0$ et $b>0$ : $\ln a < \ln b$ équivaut à $a < b$.
	- $\ln a >0$ équivaut à $a>1$.
	- $\ln a <0$ équivaut à $0<a<1$.


???- example "Exemple"

	Résoudre dans $\R$ l'équation : $\ln (2x-1) = \ln (x-2)$

	???- done "Réponse"
	
    	- **Domaine d'étude :** on cherche les réels $x$ tels que $2x-1>0$ c'est-à-dire $x>\dfrac{1}{2}$ **et** $x-2>0$   c’est-à-dire $x>2$. Donc $D=\left] \dfrac{1}{2} ; +\infty \right[ \cap ]2 ; +\infty[ = ]2 ; +\infty[$.
    	- On résout alors l'équation sur $D=]2 ;+\infty[$

    	\begin{eqnarray*}
    		\ln(2x-1)= \ln(x-2) & \equivaut & 2x-1 = x-2 \text{ et } x \in ]2 ;+\infty[ \\
    		& \equivaut & x = -1  \text{ et } x \in ]2 ;+\infty[ 
    	\end{eqnarray*}

    	- Mais $-1 \notin ]2 ;+\infty[$ , donc l'équation n'a pas de solution. Donc $S=\{ \emptyset \}$

???- example "Exemple"
	
	Résoudre dans l'équation : $\ln(x+1) + \ln(x+3) = \ln(x+7)$.

	???- done "Réponse"

		- **Domaine d'étude :** on cherche les réels $x$ tels que $x+1>0$ et $x+3>0$ et $x+7>0$. Donc $x\in ]-1;+\infty[ \cap ]-3;+\infty[ \cap ]-7 ; +\infty[ = ]-1 ; +\infty[$ .
		- On résout alors l'équation sur $D=]-1 ; +\infty[$.
		
		\begin{eqnarray*}
			\ln(x+1) + \ln(x+3) = \ln(x+7) & \equivaut & \ln((x+1)(x+3))= \ln(x+7)  \text{ et } x \in ]-1 ;+\infty[ \\
			& \eq &  x^2+4x+3=x+7  \text{ et } x \in ]-1 ;+\infty[ \\
			& \eq &  x^2+3x-4=0  \text{ et } x \in ]-1 ;+\infty[ \\
			& \eq & ( x=-4 \text{ ou } x=1 ) \text{ et } x \in ]-1 ;+\infty[ 
		\end{eqnarray*}

		- Comme $-4 \notin ]-1 ; +\infty[$, $S=\{ 1 \}$.

???- example "Exemple"
	Résoudre dans l'inéquation:  $\ln(x^2 - 4) \leq \ln x$.

	???- done "Réponse"
		- **Domaine d'étude :** On cherche les réels $x$ tels que $x^2-4>0$ et $x>0$. Donc $D=]2 ; +\infty[$.
		- On résout sur $D=]2 ; +\infty[$.
		
		\begin{eqnarray*}
		\ln(x^2 - 4) \leq \ln x & \eq & x^2-4 \leq x   \text{ et } x \in ]2 ;+\infty[ \\
		& \eq & x^2-x-4 \leq 0  \text{ et } x \in ]2 ;+\infty[\\
		& \eq & x\in \left[ \dfrac{1-\sqrt{17}}{2} ; \dfrac{1+\sqrt{17}}{2} \right]   \text{ et } x \in ]2 ;+\infty[
		\end{eqnarray*}

		- Donc $S =  \left] 2 ; \dfrac{1+\sqrt{17}}{2} \right]$.

???- example "Exemple"
	Résoudre dans $\R$ :

	1. L'équation $(E)$ : $2(\ln x )^2 -3 \ln x +1 = 0$
	2. L'inéquation $(F)$ : $2(\ln x )^2 -3 \ln x +1 \geq 0$
	
	???- done "Réponse"
		On pose $X = \ln x$, avec $x>0$.
		
		1. \begin{eqnarray*}
		(E) & \eq & 2X^2-3X+1 = 0 \text{ et } X=\ln x \text{ et } x>0\\
		& \eq & \left( X_1=1 \text{ ou } X_2 = \dfrac{1}{2} \right) \text{ et } X=\ln x \text{ et } x>0\\
		\end{eqnarray*}
		
		On résout alors $\ln x = 1 \eq x = \ex$ et $\ln x =\dfrac{1}{2} \eq x = \sqrt{\ex}$.
		
		Donc $S = \left\{ \ex ; \sqrt{\ex} \right\}$
		
		2. \begin{eqnarray*}
		(F) & \eq & 2X^2-3X+1 \geq 0 \text{ et } X=\ln x \text{ et } x>0\\
		& \eq & \left( X< \dfrac{1}{2} \text{ ou } X>1 \right) \text{ et } X=\ln x \text{ et } x>0\\
		\end{eqnarray*}

		On résout alors $\ln x < \dfrac{1}{2} \eq x < \sqrt{\ex}$ ou $\ln x > 1 \eq x > \ex$. Comme $x>0$, $S=\left]0 ; \sqrt{\ex} \right] \cup [\ex ; +\infty [$


???- example "Exemple"
	Une voiture perd en moyenne $15\%$ de son prix en un an.
	
	Au bout de combien d'années a-t-elle perdu la moitié de sa valeur?


	???- done "Réponse"
		Diminuer un prix de $15\%$ chaque année revient à multiplier le prix précédent par $0.85$. Donc $(P_n)_{n \in \N}$ est une suite géométrique de raison $0.85$ et de premier terme $P_0$. Donc pour tout $n \in \N$, $P_n = P_0 \times 0.85^n$. On veut résoudre $P_n \leq \dfrac{P_0}{2}$
		
		\begin{eqnarray*}
		P_n \leq \dfrac{P_0}{2} & \eq & P_0 \times 0.85^n \leq \dfrac{P_0}{2}\\
		& \eq & 0.85^n \leq \dfrac{1}{2} \text{ car } P_0>0\\
		& \eq & \ln \left( 0.85^n \right) \leq 0.5 \\
		& \eq & n \times \ln 0.85 \leq 0.5\\
		& \eq & n \geq \dfrac{0.5}{\ln(0.85)} \text{ car } \ln 0.85 <0\\
		& \eq & n \geq 4.26
		\end{eqnarray*}

		Donc au bout de 5 ans , la voiture a perdu la moitié de sa valeur.