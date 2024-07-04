# Théorèmes d'opérations

Dans tout ce qui suit, $\ell$ et $\ell'$ désignent deux nombres réels.

!!! warning "Attention"
	La notation "FI" désigne une Forme Indéterminée, c'est à dire qu'on ne sait pas calculer par une opération élémentaire.
	
## Limite d'une somme

!!! info "Théorème"
	<table class="AvecBordure" style="width:70%;margin:auto;"> 
	<tr>
	 <td>Si $\lim\limits_{n \to +\infty}~u_n=\cdots$ </td><td> $\ell$ </td><td> $\ell$ </td><td> $\ell$ </td><td> $+\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td>
	</tr>
	<tr>
	<td>$\text{et si }\lim\limits_{n \to +\infty} v_n=\cdots$ </td><td> $\ell'$ </td><td> $+\infty$ </td><td> $-\infty$</td><td>$+\infty$ </td><td> $-\infty$ </td><td> $+\infty$ </td>
	</tr>
	<tr>
	<td> alors $\lim\limits_{n \to +\infty}~(u_n+v_n)=\cdots$ </td><td> $\ell+\ell'$ </td><td> $+\infty$ </td><td> $-\infty$ </td><td> $+\infty$ </td><td> $-\infty$ </td><td> On ne peut pas conclure : $FI$ </td>
	</tr> 
	</table>

??? question "Exercice"
	Calculer les  limites des suites $(a_n)$ , $(b_n)$ et $(c_n)$ définies par $a_n=n^2+4n+1$ ,~$b_n=\dfrac1n-n^2$ et $c_n=n^3-n^2$ 
	
	1. $a_n=n^2+4n+1$
	
	??? done "Solution"
		
		\[
		\left.
		\begin{array}{l}
		\lim\limits_{n \to +\infty}~n^2 = +\infty \\
		\lim\limits_{n\to +\infty}~n = +\infty \quad \text{et} \lim\limits_{n\to +\infty}~4n=+\infty \quad\text{et} \lim\limits_{n\to +\infty}~4n+1 & = & +\infty
		\end{array}
		\right\}
		\quad \text{par somme} \quad \lim\limits_{n \to +\infty}~\left(n^2+4n+1\right)=+\infty.
		\]
  
	2. $b_n=\dfrac1n-n^2$ 

	??? done "Solution"

		\[
		\left.
		\begin{array}{l}
		\lim\limits_{n \to +\infty}~\dfrac{1}{n}&=&0\\
		\lim\limits_{n \to +\infty}~-n^2&=&-\infty 
		\end{array}
		\right\}
		\quad \text{par somme} \quad \lim\limits_{n \to +\infty}\left(\dfrac{1}{n}-n^2\right)=-\infty
		\]

	3. $c_n=n^3-n^2$

	??? done "Solution"
  
		\[
		\left.
		\begin{array}{l}
		\lim\limits_{n\to +\infty}~n^3&=&+\infty\\
		\lim\limits_{n \to +\infty}~-n^3&=&-\infty
		\end{array}
		\right\}
		\quad \lim\limits_{x \to -\infty}\left(n^3-n^2\right)$ \quad\text{ est une forme indeterminee du type }\infty-\infty.
		\]



## Limite d'un produit

!!! info "Théorème"
	<table class="AvecBordure"  style="width:70%;margin:auto;"> 
	<tr>
	 <td>Si $\lim\limits_{n \to +\infty}~u_n=\cdots$ </td><td> $\ell$ </td><td> $\ell>0$ </td><td> $\ell>0$</td><td>$\ell<0$</td><td>$\ell<0$</td><td>$+\infty$</td><td>$+\infty$</td><td>$-\infty$</td><td>$0$</td><td>0</td>
	</tr>
	<tr>
	<td> et si $\lim\limits_{n \to +\infty}~v_n=\cdots$</td><td>$\ell'$</td><td>$+\infty$</td><td>$-\infty$</td><td>$+\infty$</td><td>$-\infty$</td><td>$+\infty$</td><td>$-\infty$</td><td>$-\infty$</td><td>$+\infty$</td><td>$-\infty$</td>
	</tr>
	<tr>
	<td>alors $\lim\limits_{n \to +\infty}~(u_n\times v_n)=\cdots$</td><td>$\ell\times\ell'$</td><td>$+\infty$</td><td>$-\infty$</td><td>$-\infty$</td><td>$+\infty$</td><td>$+\infty$</td><td>$-\infty$</td><td>$+\infty$</td><td>$FI$</td><td>$FI$</td>
	</tr>
	<tr>
	<td colspan="2"  style="border-left:1px solid white;border-bottom:1px solid white;"> </td><td colspan="4"> Règle des signes </td><td colspan="3"> Règle des signes </td><td style="border-right:1px solid white;border-bottom:1px solid white;"> </td><td style="border-right:1px solid white;border-bottom:1px solid white;"> </td>
	</tr>
	</table>

??? question "Exercice"
	En utilisant les suites de l'exemple 3 , calculer les limites des suites 
	
	1. $p_n=a_n \times b_n$ 
	2. $c_n$.
	
	??? done "Solution"
		
		1. Pour $p_n$
		
			\[
			\left.
			\begin{array}{l}
			\lim\limits_{n \to +\infty}~a_n&=&+\infty\\
			\lim\limits_{n \to +\infty}~b_n&=&-\infty
			\end{array}
			\right\}
			\quad \text{par produit } \quad \lim\limits_{n\to +\infty}p_n=-\infty
			\]
		
		2. On a une forme indéterminée $(\infty-\infty)$.
		
		!!! tip "Méthode"
			On factorise par le terme prépondérant c'est-à-dire celui qui tend le plus vite vers $+\infty$.
		
		$c_n=n^3-n^2=n^3(1-\dfrac1n)$
		
		\[
		\left.
		\begin{array}{l}
		\lim\limits_{n \to +\infty}~n^3 =  +\infty\\		
		\lim\limits_{n\to +\infty}~1=1 \quad \text{et} \lim\limits_{n\to +\infty}~-\dfrac1n=0 \quad\text{et par somme } \lim\limits_{n\to +\infty}~1-\dfrac1n & =& 1
		\end{array}
		\right\}
		\quad \text{par produit } \quad \lim\limits_{n \to +\infty}~c_n=+\infty.
		\]


## Limite de l'inverse

!!! info "Théorème"
	<table class="AvecBordure"  style="width:70%;margin:auto;"> 
	<tr>
	 <td>Si  $\lim\limits_{n \to +\infty}~v_n$  = </td><td> $\ell\neq  0$</td><td>$0$  avec $v_n>0$ à partir d'un certain rang</td><td>$0$  avec $v_n<0$ à partir d'un certain rang</td><td>$+\infty$ ou $-\infty$</td>
    </tr>
	<tr>
	<td>alors  $\lim\limits_{n \to +\infty }~\dfrac{1}{v_n}$=</td><td>$\dfrac{1}{\ell}$</td><td>$+\infty$</td><td>$-\infty$</td><td>$0$</td>
	</tr>
    </table>


## Limite d'un quotient

???- tip "Méthode"
	Parfois, pour chercher la limite d'un quotient $\dfrac{u_n}{v_n}$ , on l'écrit comme le produit $u_n\times \dfrac{1}{v_n}$.

!!! info "Théorème"

	Pour la limite d'un quotient $\frac{u_n}{v_n}$, distinguons deux cas :

	- Cas où $\lim\limits_{n \to +\infty} v_n \neq 0$ :
	
	<table class="AvecBordure" style="width:70%;margin:auto;"> 
	<tr>
	<td>Si $\lim\limits_{n \to +\infty} u_n =$ </td><td> $\ell$ </td><td> $\ell$ </td><td> $+\infty$ </td><td> $-\infty$ </td><td> $+\infty$ </td><td> $-\infty$ </td><td> $+\infty$  ou  $-\infty$</td>
	</tr>
	<tr>
	<td>Si $\lim\limits_{n \to +\infty} v_n =$ </td><td> $\ell' \neq 0$ </td><td> $+ \infty$  ou $-\infty$ </td><td> $\ell' > 0$ </td><td> $\ell' > 0$ </td><td> $\ell' < 0$ </td><td> $\ell' < 0$ </td><td> $+ \infty$ ou $-\infty$</td>
	</tr>
	<tr>
	<td>$\lim\limits_{n \to +\infty} \left( \frac{u_n}{v_n} \right) =$ </td><td> $\frac{\ell}{\ell '}$ </td><td> $0$ </td><td> $+\infty$ </td><td> $- \infty$ </td><td> $-\infty$ </td><td> $+\infty$ </td><td>  FI </td>
	</tr>
	</table>

	- Cas où $\lim\limits_{n \to +\infty} v_n = 0$

	
	<table class="AvecBordure"  style="width:70%;margin:auto;"> 
	<tr>
	<td>Si $\lim\limits_{n \to +\infty} u_n =$ </td><td> $\ell>0$ ou $+ \infty$ </td><td> $\ell>0$ ou $+ \infty$ </td><td> $\ell<0$ ou $- \infty$ </td><td> $\ell<0$ ou $- \infty$ </td><td> $0$ </td>
	</tr>
	<tr>
	<td>Si $\lim\limits_{n \to +\infty} v_n =$ </td><td> $0$ en restant positif </td><td> $0$ en restant négatif</td><td> $0$ en restant positif </td><td> $0$ en restant négatif </td><td> $0$ </td>
	</tr>
	<tr>
	<td>$\lim\limits_{n \to +\infty} \left( \frac{u_n}{v_n} \right) =$ </td><td> $+\infty$ </td><td> $-\infty$ </td><td> $-\infty$ </td><td> $+ \infty$ </td><td>  FI </td>
	</tr>
	<tr>
	<td style="border-left:1px solid white;border-bottom:1px solid white;"></td><td colspan="4"> Règle des signes </td><td style="border-right:1px solid white;border-bottom:1px solid white;"> </td>
	</tr>
	</table>



???+ example "Exemple"
	
    Déterminer les limites des suites $(u_n)$ , $(v_n)$ et $(w_n)$ définies par $u_n=\dfrac{2}{\left(1+\dfrac{1}{\sqrt{n}}\right)}$ , $v_n=\dfrac{n^2+3n}{3n^2+4}$ et $w_n=\dfrac{n+3}{n^2-2}$

    ???- done "Réponse pour $u_n$"
	
        $u_n=\dfrac{2}{\left(1+\dfrac{1}{\sqrt{n}}\right)}=2\times\dfrac{1}{\left(1+\dfrac{1}{\sqrt{n}}\right)}$

        $\displaystyle\lim_{n \to +\infty} 2  =  2$

        $\lim\limits_{n\to +\infty}~\left(\dfrac{1}{\sqrt{n}}\right)=0 \quad \text{et} \lim\limits_{n\to +\infty}~\left(1+\dfrac{1}{\sqrt{n}}\right)=1\quad \text{d'où} \lim\limits_{n\to +\infty}~\dfrac{1}{\left(1+\dfrac{1}{\sqrt{n}}\right)} = 1$

        par produit : $\lim\limits_{n \to +\infty}~u_n=2$
    
    ???- done "Réponse pour $v_n$"

        $v_n=\dfrac{n^2+3n}{3n^2+4}$

        $\lim\limits_{n \to +\infty}~n^2+3n = +\infty$

        $\lim\limits_{n\to +\infty}~3n^2+4=+\infty$

        par quotient, on a  une forme indéterminée du type &laquo; $\dfrac{\infty}{\infty}$ &raquo;.

        ???- tip "Méthode"

            On factorise par le terme prépondérant au numérateur et le terme prépondérant au dénominateur. Puis il faut simplifier !


        $v_n=\dfrac{n^2+3n}{3n^2+4}=\dfrac{n^2(1+\dfrac3n)}{n^2(3+\dfrac{4}{n^2})}=\dfrac{1+\dfrac3n}{3+\dfrac{4}{n^2}}$

        $\lim\limits_{n \to +\infty}~1+\dfrac3n=1$

        $\lim\limits_{n\to +\infty}~3+\dfrac{4}{n^2}=3$

        Par quotient $\lim\limits_{n \to +\infty}~v_n=\dfrac13$

    ???- done "Réponse pour $w_n$"

        $w_n=\dfrac{n+3}{n^2-2}$

        $\lim\limits_{n \to +\infty}~n+3=+\infty$

        $\lim\limits_{n\to +\infty}~n^2-2=+\infty$

        par quotient, on a  une forme indéterminée du type &laquo; $\dfrac{\infty}{\infty}$ &raquo;

        $w_n=\dfrac{n+3}{n^2-2}=\dfrac{n(1+\dfrac3n)}{n^2(1-\dfrac{2}{n^2})}=\dfrac{1}{n}\times \dfrac{1+\dfrac3n}{1-\dfrac{2}{n^2}} = \dfrac{1}{n}\times \left(1+\dfrac3n\right)\times \dfrac{1}{1-\dfrac{2}{n^2}}$

        $\lim\limits_{n \to +\infty}~\dfrac1n=0$

        $\lim\limits_{n \to +\infty}~1+\dfrac3n=1$

        $\lim\limits_{n\to +\infty}~1-\dfrac{2}{n^2}=1$ d'où $\lim\limits_{n\to +\infty}~\dfrac{1}{\left(1-\dfrac{2}{n^2}\right)}=1$

        Ainsi, par produit, $\lim\limits_{n \to +\infty}~w_n=0$

!!! tip "Bilan"
    En résumé , il y a 4 formes indéterminées: &laquo; $\infty-\infty$ &raquo;,  &laquo; $0\times \infty$ &raquo;, &laquo; $\dfrac{\infty}{\infty}$ &raquo; et &laquo;$\dfrac{0}{0}$ &raquo; .
