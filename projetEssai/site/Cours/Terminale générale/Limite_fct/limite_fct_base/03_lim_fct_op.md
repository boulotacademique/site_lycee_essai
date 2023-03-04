# Opération sur les limites

## Résumé : limites de références

 <table class="AvecBordure" style="width:70%;margin:auto;"> 
<tr>
<td style="height:4em;"> $\dlim{x}{+\infty}x^2=+ \infty$ </td><td> $\dlim{x}{+\infty}x^3=+\infty$ </td><td> $\dlim{x}{+\infty}x^p=+ \infty \ (\ p \in \N^*)$ </td><td> $\dlim{x}{+\infty}\sqrt{x}=+ \infty$ </td><td> $\dlim{x}{+\infty}e^x=+ \infty$ </td>
</tr>
<tr>
<td style="height:4em;"> $\dlim{x}{-\infty}x^2=+ \infty$ </td><td> $\dlim{x}{-\infty}x^3=-\infty$ </td><td> $\dlim{x}{-\infty}x^p=+ \infty  \ (\ p \in \N^*, p \text{ pair })$ </td><td> $\dlim{x}{-\infty}x^p=- \infty  \ (\ p \in \N^*, p \text{ impair })$</td><td style="border-right:1px solid white;border-bottom:1px solid white"></td>
</tr>
<tr>
<td style="height:4em;"> $\dlim{x}{\pm\infty}\dfrac 1x=0$ </td><td> $\dlim{x}{\pm\infty}\dfrac{1}{x^2}=0$ </td><td> $\dlim{x}{\pm\infty}\dfrac{1}{x^n}=0$ </td><td> $\dlim{x}{+\infty}\dfrac{1}{\sqrt{x}}=0$</td><td style="border-right:1px solid white;border-bottom:1px solid white"></td>
</tr>
<tr>
<td style="height:4em;"> $\dlim{x}{0}\dfrac{1}{x^2}=+\infty$ </td><td> $\dlim{x}{0}\dfrac{1}{x^n}=+\infty \ (\ n \in \N^* n \text{ pair })$ </td><td style="border-right:1px solid white;"> </td><td style="border-right:1px solid white;"> </td><td style="border-right:1px solid white;border-bottom:1px solid white"></td>
</tr>
<tr>
<td style="height:4em;"> $\dlim{x}{0^+}\dfrac 1x=+\infty$ </td><td> $\dlim{x}{0^-}\dfrac 1x=-\infty$ </td><td> $\dlim{x}{0^+}\dfrac{1}{x^n}=+\infty \ (\ n \in \N^* n \text{ impair })$ </td><td> $\dlim{x}{0^-}\dfrac{1}{x^n}=-\infty \ (\ n \in \N^* n \text{ impair })$</td><td  style="border-right:1px solid white;border-bottom:1px solid white;"></td>
</tr>
 </table>


## Limite et opérations

Dans tout ce qui suit, $\ell$ et $\ell'$ désignent deux nombres réels $a$ désigne un réel ou $+\infty$ ou $-\infty$.

!!! warning "Attention"
	La notation "FI" désigne une Forme Indéterminée, c'est à dire qu'on ne sait pas calculer par une opération élémentaire.
	
### Limite d'une somme

!!! info "Théorème"
	<table class="AvecBordure" style="width:70%;margin:auto;"> 
	<tr>
	 <td>Si $\lim\limits_{xn \to a}~f(x)=\cdots$ </td><td> $\ell$ </td><td> $\ell$ </td><td> $\ell$ </td><td> $+\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td>
	</tr>
	<tr>
	<td>$\text{et si }\lim\limits_{x \to a} g(x)=\cdots$ </td><td> $\ell'$ </td><td> $+\infty$ </td><td> $-\infty$</td><td>$+\infty$ </td><td> $-\infty$ </td><td> $+\infty$ </td>
	</tr>
	<tr>
	<td> alors $\lim\limits_{x \to a}~(f(x) + g(x))=\cdots$ </td><td> $\ell+\ell'$ </td><td> $+\infty$ </td><td> $-\infty$ </td><td> $+\infty$ </td><td> $-\infty$ </td><td> On ne peut pas conclure : $FI$ </td>
	</tr> 
	</table>

### Limite d'un produit

!!! info "Théorème"
	<table class="AvecBordure" style="width:70%;margin:auto;"> 
	<tr>
	 <td>Si $\lim\limits_{x \to a}~f(x)=\cdots$ </td><td> $\ell$ </td><td> $\ell>0$ </td><td> $\ell>0$</td><td>$\ell<0$</td><td>$\ell<0$</td><td>$+\infty$</td><td>$+\infty$</td><td>$-\infty$</td><td>$0$</td><td>0</td>
	</tr>
	<tr>
	<td> et si $\lim\limits_{x \to a}~g(x)=\cdots$</td><td>$\ell'$</td><td>$+\infty$</td><td>$-\infty$</td><td>$+\infty$</td><td>$-\infty$</td><td>$+\infty$</td><td>$-\infty$</td><td>$-\infty$</td><td>$+\infty$</td><td>$-\infty$</td>
	</tr>
	<tr>
	<td>alors $\lim\limits_{x \to a}~(f(x) \times g(x))=\cdots$</td><td>$\ell\times\ell'$</td><td>$+\infty$</td><td>$-\infty$</td><td>$-\infty$</td><td>$+\infty$</td><td>$+\infty$</td><td>$-\infty$</td><td>$+\infty$</td><td>$FI$</td><td>$FI$</td>
	</tr>
	<tr>
	<td colspan="2"  style="border-left:1px solid white;border-bottom:1px solid white;"> </td><td colspan="4"> Règle des signes </td><td colspan="3"> Règle des signes </td><td style="border-right:1px solid white;border-bottom:1px solid white;"> </td><td style="border-right:1px solid white;border-bottom:1px solid white;"> </td>
	</tr>
	</table>

### Limite de l'inverse

!!! info "Théorème"
	<table class="AvecBordure" style="width:70%;margin:auto;"> 
	<tr>
	 <td>Si  $\lim\limits_{x \to a}~f(x)$  = </td><td> $\ell\neq  0$</td><td>$0$  avec $f(x)>0$ au voisinage de $a$</td><td>$0$  avec $f(x)<0$ au voisinage de $a$</td><td>$+\infty$ ou $-\infty$</td>
    </tr>
	<tr>
	<td>alors  $\lim\limits_{x \to a }~\dfrac{1}{f(x)}$=</td><td>$\dfrac{1}{\ell}$</td><td>$+\infty$</td><td>$-\infty$</td><td>$0$</td>
	</tr>
    </table>

### Limite d'un quotient

???- tip "Méthode"
	Parfois, pour chercher la limite d'un quotient $\dfrac{u_n}{v_n}$ , on l'écrit comme le produit $u_n\times \dfrac{1}{v_n}$.

!!! info "Théorème"

	Pour la limite d'un quotient $\frac{f(x)}{g(x)}$, distinguons deux cas :

	- Cas où $\lim\limits_{x \to a} g(x) \neq 0$ :

	<table class="AvecBordure" style="width:70%;margin:auto;"> 
	<tr>
	<td>Si $\lim\limits_{x \to a} f(x) =$ </td><td> $\ell$ </td><td> $\ell$ </td><td> $+\infty$ </td><td> $-\infty$ </td><td> $+\infty$ </td><td> $-\infty$ </td><td> $+\infty$  ou  $-\infty$</td>
	</tr>
	<tr>
	<td>Si $\lim\limits_{x \to a} g(x) =$ </td><td> $\ell' \neq 0$ </td><td> $+ \infty$  ou $-\infty$ </td><td> $\ell' > 0$ </td><td> $\ell' > 0$ </td><td> $\ell' < 0$ </td><td> $\ell' < 0$ </td><td> $+ \infty$ ou $-\infty$</td>
	</tr>
	<tr>
	<td>$\lim\limits_{x \to a} \left( \frac{f(x)}{g(x)} \right) =$ </td><td> $\frac{\ell}{\ell '}$ </td><td> $0$ </td><td> $+\infty$ </td><td> $- \infty$ </td><td> $-\infty$ </td><td> $+\infty$ </td><td>  FI </td>
	</tr>
	</table>

	- Cas où $\lim\limits_{x \to a} g(x) = 0$

	
	<table class="AvecBordure"  style="width:70%;margin:auto;"> 
	<tr>
	<td>Si $\lim\limits_{x \to a} f(x) =$ </td><td> $\ell>0$ ou $+ \infty$ </td><td> $\ell>0$ ou $+ \infty$ </td><td> $\ell<0$ ou $- \infty$ </td><td> $\ell<0$ ou $- \infty$ </td><td> $0$ </td>
	</tr>
	<tr>
	<td>Si $\lim\limits_{x \to a} g(x) =$ </td><td> $0$ en restant positif </td><td> $0$ en restant négatif</td><td> $0$ en restant positif </td><td> $0$ en restant négatif </td><td> $0$ </td>
	</tr>
	<tr>
	<td>$\lim\limits_{x \to a} \left( \frac{f(x)}{g(x)} \right) =$ </td><td> $+\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $+ \infty$ </td><td>  FI </td>
	</tr>
	<tr>
	<td style="border-left:1px solid white;border-bottom:1px solid white;"></td><td colspan="4"> Règle des signes </td><td style="border-right:1px solid white;border-bottom:1px solid white;"> </td>
	</tr>
	</table>

???- example "Exemple"

	1. $\lim\limits_{x \to 0}~\left(e^x+x^3\right)$ ?
	2. $\lim\limits_{x \to -\infty}\left(\dfrac{1}{x}+x^2\right)=$?
	3. $\lim\limits_{x \to +\infty}\left(e^ x+x^2\right)$ = ?
	4. $\lim\limits_{x \to -\infty}\left(x+x^3\right)=$ ?
	5. $\lim\limits_{x \to -\infty}\left(x^2+x^3\right)$  ?
	
	???- done "Réponse"
      	1. $\Lim{\lim\limits_{x \to 0}~e^x&=& 1}{\lim\limits_{x \to 0}~x^3&=& 0 } \quad \text{ par somme}\quad  \lim\limits_{x \to 0}~\left(e^x+x^3\right)= 1$.
      	2. $\Lim{\lim\limits_{x \to -\infty}~\dfrac{1}{x}&=&0^- }{\lim\limits_{x \to -\infty}~x^2&=& +\infty } \quad\text{ par somme}\quad  \lim\limits_{x \to -\infty}\left(\dfrac{1}{x}+x^2\right)=+\infty$
      	3. $\Lim{\lim\limits_{x \to +\infty}~e^x&=& +\infty }{\lim\limits_{x \to +\infty}~x^2&=& {\color{reponse} +\infty }} \quad \text{ par somme}\quad \lim\limits_{x \to +\infty}\left(e^x+x^2\right)={\color{reponse} +\infty }$.
      	4. $\Lim{\lim\limits_{x \to -\infty}~x&=& {\color{reponse}-\infty}}{\lim\limits_{x \to -\infty}~x^3&=&{\color{reponse} -\infty }} \quad \text{ par somme}\quad \lim\limits_{x \to -\infty}\left(x+x^3\right)={\color{reponse} -\infty }$.
      	5.  $\Lim{\lim\limits_{x \to -\infty}~x^2&=& {\color{reponse} +\infty}}{\lim\limits_{x \to -\infty}~x^3&=& {\color{reponse} -\infty }} \quad \text{ par somme}\quad \lim\limits_{x \to -\infty}\left(x^2+x^3\right)$  est une forme indéterminée du type &laquo; $\infty-\infty$ &raquo;. Seule une étude particulière permet de lever l'indétermination.

		???- tip "Lever une FI avec une somme : astuce"
			On transforme l'expression en factorisant par le terme prépondérant.

			Pour un polynôme, le terme prépondérant est le terme de plus haut degré.
		
		  Pour $x\neq0$ , $x^2+x^3= x^3\left(\dfrac1x+1\right)$.

 		  Or $\Lim{\lim\limits_{x \to -\infty}~x^3&=&-\infty}{\lim\limits_{x \to -\infty}~\dfrac1x+1&=&1} \quad \lim\limits_{x \to -\infty}\left(x^2+x^3\right)=-\infty$

!!! info "Pour **les polynômes** au voisinage de **l'infini** !"
	La limite  d'une  **fonction polynôme** en $+ \infty$ et en $-\infty$ est la limite  de son terme de plus haut degré.

???- example "Exemple"
	En utilisant le théorème précédent, trouver  la limite en $\pm \infty$ de  $3x^3+2x+1$.

	???- done "Réponse"
		$\dlim{x}{-\infty} 3x^3+2x+1 = \dlim{x}{-\infty} 3x^3=-\infty$  et $\dlim{x}{+\infty} 3x^3+2x+1 = \dlim{x}{-\infty} 3x^3=+\infty$.

???- example "Exemple"
	1. $\lim\limits_{x \to 0}~[(e^x+3)\times(e^x-2)]$ ?
	2. $\lim\limits_{x \to 0^+}\left[(x-3)\times \dfrac{1}{x}\right]$ ?
	3. $\lim\limits_{x \to -\infty}[(x-1)\times x^3]$ ?
	4. $\lim\limits_{x \to -\infty}\left[(x^2+1)\times \dfrac{1}{x}\right]$?

	???- done "Réponse"
		1. $\Lim{\lim\limits_{x \to 0}~(e^x+3)&=&{\color{reponse} 4} }{\lim\limits_{x\to 0}~(e^x-2)&=&{\color{reponse} -1}} \quad \lim\limits_{x \to 0}~[(e^x+3)\times(e^x-2)]={\color{reponse} -4}$.
		2. $\Lim{\lim\limits_{x \to 0^+}~(x-3)&=&{\color{reponse} -3 }}{\lim\limits_{x \to 0^+}~\dfrac{1}{x}&=& {\color{reponse} +\infty }} \quad \lim\limits_{x \to 0^+}\left[(x-3)\times \dfrac{1}{x}\right]= {\color{reponse}-\infty}$
		3. $\Lim{\lim\limits_{x \to -\infty}~(x-1) &=& {\color{reponse}-\infty}}{\lim\limits_{x \to -\infty}~x^3&=& {\color{reponse}-\infty}} \quad \lim\limits_{x \to -\infty}[(x-1)\times x^3]={\color{reponse}+\infty}$. 
		4. $\Lim{\lim\limits_{x \to -\infty}~(x^2+1)&=&{\color{reponse} +\infty}}{\lim\limits_{x \to -\infty}~\dfrac{1}{x}&=&{\color{reponse} 0^- }} \quad \lim\limits_{x \to -\infty}\left[(x^2+1)\times \dfrac{1}{x}\right]$  est une forme indéterminée du type &laquo; $0\times \infty$ &raquo;

		???- tip "Lever une FI avec un produit : astuce"
			On peut essayer de développer !
		
		$f(x)=(x^2+1)\dfrac{1}{x}={\color{reponse}x+\dfrac{1}{x}}$.

		$\Lim{\lim\limits_{x\to -\infty}~x&=&-\infty}{\lim\limits_{x\to -\infty}~\dfrac{1}{x}&=&0}$ d'où $\lim\limits_{x\to -\infty}f(x)=-\infty$.

???- example "Exemple"
	$f$ est définie pour $x\neq 2$ par $f(x) =\dfrac{1}{2-x}$. Déterminer $\lim\limits_{x \to 2}\left(\dfrac{1}{2-x}\right)$?

	???- done "Réponse"
		Comme $\dlim{x}{2} 2-x = 0$, il faut étudier le signe de la fonction $f(x) = \dfrac{1}{2-x}$ _au voisinage de_ 2. Or $1>0$ au voisinage de 2 (et sur tout $\R$). Il suffit donc d'étudier le signe de $2-x$.

		[![tab de signe](../Image/Cours_011.png){.Center_lien .VignetteMed}](../Image/Cours_011.png)

		$\lim\limits_{x \to 2^+}~(2-x)={\color{reponse}0^-}    \quad \lim\limits_{x \to 2^+}~\dfrac{1}{2-x}={\color{reponse}-\infty }$.
		
		$\lim\limits_{x \to 2^-}~(2-x)={\color{reponse}0^+}    \quad \lim\limits_{x \to 2^-}~\dfrac{1}{2-x}={\color{reponse}+\infty}$.

???- example "Exemple"
	1. $\lim\limits_{x \to -\infty}~\left(\dfrac{e^x+3}{e^x-2}\right)$ ?
	2. $\lim\limits_{x \to -\infty}~\left(\frac{\frac{1}{x}-3}{x^2}\right)?$ ?
	3. $\lim\limits_{x \to 3}\left(\dfrac{x-4}{3-x}\right)$ ?
	4. $\dlim{x}{3}=\dfrac{2x-5}{-x^2+3x}$ ?
	5. $\lim\limits_{x \to -\infty}\left(\dfrac{x-1}{x^3-2}\right)$  ?

	???- done "Réponse"
		<ol>
		<li> $\Lim{\lim\limits_{x \to -\infty}~(e^x+3)={\color{reponse}3}}{\lim\limits_{x\to -\infty}~(e^x-2)={\color{reponse}-2}}$ \quad par quotient $\lim\limits_{x \to -\infty}~\left(\dfrac{e^x+3}{e^x-2}\right)={\color{reponse} -\dfrac32}$.</li>
		<li> $\Lim{\lim\limits_{x \to -\infty}~\frac{1}{x}-3={\color{reponse}-3}}{\lim\limits_{x\to -\infty}~x^2={\color{reponse}+\infty} }$ \quad par quotient $\lim\limits_{x \to -\infty}~\left(\dfrac{\frac{1}{x}-3}{x^2}\right)={\color{reponse} 0}$.</li>
		<li> Quand $x$ tend vers 3, le dénominateur tend vers 0 . On doit étudier le signe de $f(x) = \dfrac{x-4}{3-x}$ au voisinage de 3. Or $x-4$ est proche de $3-4=-1$ au voisinage de $3$. Il est donc inutile de faire un tableau de signe pour le numérateur ! 

		[![tab de signe](../Image/Cours_012.png){.Center_lien .VignetteMed}](../Image/Cours_012.png)

		$\Lim{\lim\limits_{x \to 3^+}~x-4={\color{reponse}-1}}{\lim\limits_{x \to 3^+}~3-x={\color{reponse} 0^-}} \quad \text{ par quotient } \lim\limits_{x \to 3^+}\left(\dfrac{x-4}{3-x}\right)={\color{reponse}+\infty}$.

		$\Lim{\lim\limits_{x \to 3^-}~x-4={\color{reponse}-1}}{\lim\limits_{x \to 3^-}~3-x={\color{reponse} 0^+ } } \quad \text{ par quotient } \lim\limits_{x \to 3^-}\left(\dfrac{x-4}{3-x}\right)={\color{reponse} -\infty}$.</li>
		<li> Quand $x$ tend vers 3, le dénominateur tend vers 0 . On doit étudier le signe de $-x^2+3x$ (en effet, au voisinage de $3$, $2x-5$ est proche de $2\times 3 -5 =1$).

		[![tab de signe](../Image/Cours_013.png){.Center_lien .VignetteMed style="text-align:center;width:40%;"}](../Image/Cours_013.png)

		$\Lim{\dlim{x}{3}2x-5=1}{\dlim{x}{3^-}-x^2+3x={\color{reponse}0^+} }$\quad par quotient $\dlim{x}{3^-}f(x)={\color{reponse}+\infty}$.
  		
		$\Lim{\dlim{x}{3}2x-5=1}{\dlim{x}{3^+}-x^2+3x={\color{reponse}0^-} }$\quad par quotient $\dlim{x}{3^+}f(x)={\color{reponse}-\infty }$.
		</li>
		<li> $\Lim{\lim\limits_{x \to -\infty}~(x-1)={\color{reponse}-\infty}}{\lim\limits_{x\to -\infty}~(x^3-2)={\color{reponse}-\infty}}$ par quotient $ \lim\limits_{x \to -\infty}\left(\dfrac{x-1}{x^3-2}\right)$   est une forme indéterminée du type &laquo; $0\times {\infty}$ &raquo;

		???- tip "Lever une FI pour un quotient : astuce"
			On transforme l'expression en mettant en facteur le terme prépondérant au numérateur et au dénominateur. Puis on simplifie !
		
		Pour $x\neq0$ , on a $\dfrac{x-1}{x^3-2}={\color{reponse}\dfrac{x\left(1-\dfrac{1}{x}\right)}{x^3\left( 1 - \dfrac{2}{x^3}\right)}=\dfrac{\left(1-\dfrac1x\right)}{1 - \dfrac{2}{x^3}} \times \dfrac{1}{x^2}}$

		$\Lim{\lim\limits_{x \to -\infty}~1-\dfrac1x&=&{\color{reponse} 1}}{\lim\limits_{x \to -\infty}~1 - \dfrac{2}{x^3}&=& {\color{reponse} 1}} \quad \text{ par quotient } \lim\limits_{x \to -\infty}\left(\dfrac{1-\dfrac{1}{x}}{1 - \dfrac{2}{x^3}}\right)= {\color{reponse} 1}$

		$\dlim{x}{-\infty} \dfrac{1}{x^2} = 0$. Ainsi, $\dlim{x}{-\infty} \left(\dfrac{x-1}{x^3-2}\right)=0$.
		</li>
		</ol>


???- tip "Limite d'une **fonction rationnelle** au voisinage de **l'infini**"
	La limite en $+\infty$ et en $-\infty$  **d'une fonction rationnelle** (quotient de deux fonctions polynômes)  est la limite du quotient des  termes de plus haut degré du numérateur et du dénominateur (pensez à simplifier).

???- example "Exemple"
	1. $\dlim{x}{-\infty}\dfrac{x+4}{x^2+5}$ ?
	2. $\dlim{x}{+\infty}\dfrac{5x-7}{2x+1}$ ?
	3. $\lim\limits_{x\to -\infty}~\left(\dfrac{x^2+2x+1}{2x^2-3}\right)$ ?

	???- done "Réponse"
		AFAIRE

???- example "Exemple d'une FI &laquo; $\dfrac{0}{0}$ &raquo; "
	$\lim\limits_{x \to 0}~\left(\dfrac{x^2}{\sqrt{x}}\right)$

	???- done "Réponse"
		$\Lim{\lim\limits_{x \to 0}~x^2&=& {\color{reponse} 0} }{\lim\limits_{x \to 0}~\sqrt{x}&=& {\color{reponse} 0} } \quad \lim\limits_{x \to 0}~\left(\dfrac{x^2}{\sqrt{x}}\right)$ est une forme indéterminée  du type &laquo; $\dfrac{0}{0}$ &raquo;.

		$\dfrac{x^2}{\sqrt{x}}={\color{reponse}\dfrac{x^2\sqrt{x}}{x}=x\sqrt{x}}$.
  		
		$\Lim{\lim\limits_{x \to 0}~x&=& {\color{reponse} 0} }{\lim\limits_{x \to 0}~\sqrt{x}&=& {\color{reponse} 0} } \quad \lim\limits_{x \to 0}~x\sqrt{x}={\color{reponse} 0}$.

### Résumé : Opérations sur les limites de fonctions

!!! tip "Opérations sur les limites"
	Soient $f$ et $g$ deux fonctions  définies sur un intervalle I et admettant $\ell$ et $\ell'$ pour limite en $a$ ($\ell$, $\ell'$, $a$ sont  finis ou infinis).

	- La somme de deux fonctions $f+g$   a pour limite en a  ,la somme des limites $\ell +\ell'$   sauf si l'on obtient &laquo; $\infty-\infty$&raquo;
	- Le produit  de deux fonctions$f\times g$   a pour limite en a  le produit des limites $\ell\times \ell$' (règle des signes)   sauf si l'on obtient &laquo; $0\times \infty$ &raquo;
	- si $k$ est un nombre réel alors $\dfrac{k}{g}$ a pour limite en "a", $\dfrac{k}{\ell'}$ (règle des signes ) en particulier si $\left\lbrace\begin{array}{ l} {\dlim{x}{a} g(x) =\,  \text{ alors }\,   \dlim{x}{a} \dfrac{k}{g(x)}=\pm \infty}\\ { \dlim{x}{a} g(x) =\pm \infty\,  \text{ alors }\,  \dlim{x}{a} \dfrac{k}{g(x)}=0} \end{array}\right.$
	- Pour le  quotient de deux fonctions $\dfrac{f}{g}$ on se ramène aux cas précédents en écrivant $\dfrac{f}{g}=f\times \dfrac{1}{g}$  sauf si l'on obtient &laquo; $\dfrac{0}{0}$ &raquo; ou \&laquo; $\dfrac{\infty}{\infty}$ &raquo;
	- Pour lever les indéterminations si l'expression est factorisée on développe et si l'expression est développée on factorise par le terme prépondérant.
	- Pour les **fonctions polynômes** au voisinage de **l'infini** : la limite  d'une  **fonction polynôme** en $+ \infty$ et en $-\infty$ est la limite  de son terme de plus haut degré.
	- Pour les **fonctions rationnelles** au voisinage de **l'infini** : la limite en $+\infty$ et en $-\infty$  **d'une fonction rationnelle** (quotient de deux fonctions polynômes)  est la limite du quotient des  termes de plus haut degré du numérateur et du dénominateur (penser à simplifier).  

## Limite et composée

Soit $f$ la fonction définie par :$f(x)= \sqrt{-2x+4}$

$x \stackrel{u}{\longmapsto} u(x){\color{reponse}=-2x+4 =X} \stackrel{v}{\longmapsto} v(X){\color{reponse}=\sqrt{X}=\sqrt{-2x+4}=f(x)}$.

Ainsi, on a $f(x)={\color{reponse}v[u(x)]=\sqrt{-2x+4}}$ et  $f$ est définie pour tous les $x$ tels que $-2x+4 \geq 0$ c'est-à-dire $x \leq 2$.

!!! info "Limite d'une composée"
	Soient deux fonctions : $u$ , $v$ et $f$ la composée de $u$ suivie de $v$.  $a$ , $b$ , $c$ désignent des réels ou $+\infty$ ou $-\infty$
	
	Si $\quad \Lim{
		\lim\limits_{
			x \to {
				\color{
					red
				}
				a
			}
		}
		u(x)={
			\color{
				blue
			}
			b
		}
	}{
		\lim\limits_{
			X \to {
				\color{
					blue
				}
				b
			}
		}
		v(X)= {\color{green} c}
	}$
	alors par composition $\lim\limits_{
		x \to {
			\color{
				red
			}
			a
		}
	} v \left(u(x) \right)= {\color{green} c}$.

???- example "Exemple"
	Soit $f$ la fonction définie sur $]-\infty, 2[$ par $f(x) =\sqrt{-2x+4}$.
	Déterminer la limite en 2.

	???- done "Réponse"
		$\Lim{\lim\limits_{x \to {\color{red}2}}~(-2x+4)&=& {\color{blue}0} }{\lim\limits_{X\to {\color{blue}0} }~\sqrt{X}&=& {\color{green}0}} \quad \lim\limits_{x \to 2}~\sqrt{-2x+4}= {\color{green}0}$.

???- example "Exemple"
	Soit $g$ la fonction définie sur $\R-\{1\}$ par $g(x) = \exp\left(\frac{x+3}{1-x} \right)$.

	1. Déterminer la limite en $-\infty$.
	2. Déterminer la limite en 1.

	???- done "Réponse"
		<ol>
		<li> $\Lim{\lim\limits_{x \to -\infty}~\dfrac{x+3}{1-x}& = &\lim\limits_{x \to -\infty} \dfrac{x}{-x}=\lim\limits_{x \to -\infty} -1={\color{blue}-1} }{ \lim\limits_{X\to {\color{blue}-1}} e^X &=& {\color{green} \ex^{-1} }} \quad \lim\limits_{x \to -\infty}~\ex^{\frac{x+3}{1-x}}= {\color{green} \ex^{-1} }$
		</li>
		<li> Etude du signe de $1-x$ :

		[![tab signe](../Image/Cours_014.png){.Center_lien .VignetteMed}](../Image/Cours_014.png)

		$\Lim{\Lim{\lim\limits_{x \to 1^+}~x+3&=&{\color{reponse}4}}{\lim\limits_{x \to 1^+}~1-x&=&{\color{reponse}0^-} }\text{donc} \quad \lim\limits_{x \to 1^+} \dfrac{x+3}{1-x}={\color{reponse}-\infty} }{\lim\limits_{X\to -\infty}~e^X={\color{reponse}0}&& }\quad \lim\limits_{x \to 1^+}~\ex^{\frac{x+3}{1-x}}={\color{reponse} 0}$.

		$\Lim{\Lim{\lim\limits_{x \to 1^-}~x+3&=&{\color{reponse} 4}}{\lim\limits_{x \to 1^-}~1-x&=&{\color{reponse}0^+} }\text{donc} \quad \lim\limits_{x \to 1^+}(x+3)\times \dfrac{1}{1-x}={\color{reponse}+\infty} }{\lim\limits_{X\to +\infty}~e^X={\color{reponse}+\infty}&&}\quad \lim\limits_{x \to 1^-}~e^{\frac{x+3}{1-x}}={\color{reponse}+\infty}$.

		Courbe ggb AFAIRE
		</li>
		</ol>

???- example "Exemple"
	Soit $h$ la fonction définie sur $\R-\{0\}$ par $h(x)= \dfrac{\sin(2x)}{x}$.
	
	Déterminer la limite en 0.

	???- done "Réponse"
		On a  une forme indéterminée  du type \og $\dfrac{0}{0}$ \fg.
		
		???- tip "Limite et taux d'accroissement"
			On  utilise la définition du nombre dérivé en 0 de la fonction $\sin$ :  $\lim\limits_{x \to 0}~\dfrac{\sin(x)}{x}=1$.
    
		$\dfrac{\sin(2x)}{x}={\color{reponse}2 \times \dfrac{\sin(2x)}{2x}= 2\times \dfrac{\sin(X)}{X}}$ avec $X = 2x$.

      	$\Lim{\lim\limits_{x \to 0}~2x&=&{\color{reponse}0}}{\lim\limits_{X\to 0}~&\dfrac{\sin X}{X}=&{\color{reponse} 1}} \quad \lim\limits_{x \to 0}~\dfrac{\sin(2x)}{2x}={\color{reponse}1}$
		et ainsi $\dlim{x}{0} \dfrac{\sin(2x)}{x}={\color{reponse}2 }$.