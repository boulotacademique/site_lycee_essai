# Théorèmes d'opérations

Dans tout ce qui suit, $\ell$ et $\ell'$ désignent deux nombres réels.

!!! warning
	La notation "FI" désigne une Forme Indéterminée, c'est à dire qu'on ne sait pas calculer par une opération élémentaire.
	
## Limite d'une somme

!!! abstract "Théorème"
	<table class="AvecBordure"> 
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

!!! abstract "Théorème"
	<table class="AvecBordure"> 
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
	<td colspan="2"> </td><td colspan="4"> Règle des signes </td><td colspan="3"> Règle des signes </td><td> </td>
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

!!! abstract "Théorème"
	<table class="AvecBordure"> 
	<tr>
	 <td>Si  $\lim\limits_{n \to +\infty}~v_n$  = </td><td> $\ell\neq  0$</td><td>$0$  avec $v_n>0$ à partir d'un certain rang</td><td>$0$  avec $v_n<0$ à partir d'un certain rang</td><td>$+\infty$ ou $-\infty$</td>
    </tr>
	<tr>
	<td>alors  $\lim\limits_{n \to +\infty }~\dfrac{1}{v_n}$=</td><td>$\dfrac{1}{\ell}$</td><td>$+\infty$</td><td>$-\infty$</td><td>$0$</td>
	</tr>
    </table>


## Limite d'un quotient

!!! tip "Méthode"
	Pour chercher la limite d'un quotient $\dfrac{u_n}{v_n}$ , on l'écrit comme le produit $u_n\times \dfrac{1}{v_n}$



\begin{exo}
  Déterminer les limites des suites $(u_n)$ , $(v_n)$ et $(w_n)$ définies par $ u_n=\dfrac{2}{\left(1+\dfrac{1}{\sqrt{n}}\right)}$ , $v_n=\dfrac{n^2+3n}{3n^2+4}$ et $w_n=\dfrac{n+3}{n^2-2}$
   \begin{enumerate}
  \item $ u_n=$\textcolor{reponse}{$\dfrac{2}{\left(1+\dfrac{1}{\sqrt{n}}\right)}=2\times\dfrac{1}{\left(1+\dfrac{1}{\sqrt{n}}\right)}$\\
  $\Lim{\lim\limits_{n \to +\infty}~2  =  2}{\lim\limits_{n\to +\infty}~\left(\dfrac{1}{\sqrt{n}}\right)=0 \quad \text{et} \lim\limits_{n\to +\infty}~\left(1+\dfrac{1}{\sqrt{n}}\right)=1\quad \text{d'où} \lim\limits_{n\to +\infty}~\dfrac{1}{\left(1+\dfrac{1}{\sqrt{n}}\right)}& =& 1 } \quad \text{par produit} \quad \lim\limits_{n \to +\infty}~u_n=2$.}
    \vspace{2cm}  

  \item $v_n=$\textcolor{reponse}{$\dfrac{n^2+3n}{3n^2+4}=(n^2+3n)\times \dfrac{1}{3n^2+4}$ \\
  $\Lim{\lim\limits_{n \to +\infty}~n^2+3n = +\infty}{\lim\limits_{n\to +\infty}~3n^2+4=+\infty \quad \text{et}\lim\limits_{n\to +\infty}~\dfrac{1}{(3n^2+4)}& =& 0}$ \quad \text{par produit}  on a  une forme indéterminée  
 du type \og $o\times \infty$ \fg{}  \\}
 

\begin{methode}
On factorise par le terme prépondérant au numérateur et le terme prépondérant au dénominateur
\end{methode}
\textcolor{reponse}{\\ 
$v_n=\dfrac{n^2+3n}{3n^2+4}=\dfrac{n^2(1+\dfrac3n)}{n^2(3+\dfrac{4}{n^2})}=\dfrac{1+\dfrac3n}{3+\dfrac{4}{n^2}}=\left(1+\dfrac3n \right)\times \dfrac{1}{{3+\dfrac{4}{n^2}}}$\\
 $\Lim{\lim\limits_{n \to +\infty}~1+\dfrac3n=1}{\lim\limits_{n\to +\infty}~3+\dfrac{4}{n^2}=3\quad \text{d'où} \lim\limits_{n\to +\infty}~\dfrac{1}{\left(3+\dfrac{4}{n^2}\right)}=\dfrac13} \quad \text{par produit} \quad \lim\limits_{n \to +\infty}~v_n=\dfrac13$.\\
\textbf{On ne peut pas conclure pour un quotient par les théorèmes d'opérations quand les suites ($u_n$) et ($v_n$) ont toutes les deux une limite infinie ou pour limite 0 } \cad si l'on a $" \dfrac{\infty}{\infty}"$ ou $" \dfrac{0}{0}"$}
  \item  $w_n=\dfrac{n+3}{n^2-2}$\\
  $\Lim{\lim\limits_{n \to +\infty}~n+3={\color{reponse}+\infty}}{\lim\limits_{n\to +\infty}~n^2-2={\color{reponse}+\infty} }$ \quad \text{par quotient}  on a  une forme indéterminée  
 du type \textcolor{reponse}{\og $\dfrac{\infty}{\infty}$ \fg{}  \\
 $w_n=\dfrac{n+3}{n^2-2}=\dfrac{n(1+\dfrac3n)}{n^2(1-\dfrac{2}{n^2})}=\dfrac{1}{n}\times \left(1+\dfrac3n\right)\times \dfrac{1}{1-\dfrac{2}{n^2}} $\\
 ${\lim\limits_{n \to +\infty}~\dfrac1n=0} {\Lim{\lim\limits_{n \to +\infty}~1+\dfrac3n=1}{\lim\limits_{n\to +\infty}~1-\dfrac{2}{n^2}=1 \quad \text{d'où} \lim\limits_{n\to +\infty}~\dfrac{1}{\left(1-\dfrac{2}{n^2}\right)}=1} \text{ par produit } \lim\limits_{n \to +\infty}~w_n=0}$.\\}

\end{enumerate}     
 \end{exo}

\begin{methode}[En résumé]
En résumé , il y a 4 formes indéterminées:$"\infty-\infty "$ $"0\times \infty"$ ,$" \dfrac{\infty}{\infty}"$ et $" \dfrac{0}{0}"$
\end{methode}