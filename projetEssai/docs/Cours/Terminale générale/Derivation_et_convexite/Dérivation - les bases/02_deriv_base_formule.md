# Dérivation et formule

**Il est impératif de connaitre par c&#339;ur les formules suivantes :**

\[
\begin{array}{|c|c|c|c|}
\hline
\rule[-4pt]{0pt}{15pt} \text{Fonction $f$ définie sur} & \text{Par :}& \text{a pour fonction dérivée}&\text{la fonction est dérivable sur}\\
\hline
\rule[-4pt]{0pt}{15pt} \mathbf{R} & f(x) = k \ \text{(cste)} & f'(x) = 0 & \mathbf{R} \\
\hline
\rule[-4pt]{0pt}{15pt} \mathbf{R} & f(x) = x^n \ \  n \in \mathbb{N},\ n>0 & f'(x) = nx^{n-1} & \mathbf{R} \\
\hline
\rule[-4pt]{0pt}{15pt} \mathbf{R}^* & f(x) = x^n \ \   n \in \mathbb{Z},\ n<0 & f'(x) = nx^{n-1} & \mathbf{R}^* \\
\rule[-12pt]{0pt}{30pt}  & \text{Ou } f(x) = \frac{1}{x^n} \ n \in \mathbb{N},\ n \neq 0 & f'(x) = \frac{-n}{x^{n+1}} & \\
\hline
\rule[-12pt]{0pt}{30pt} \left[0;+\infty \right[ & f(x) = \sqrt{x} & f'(x) = \frac{1}{2 \sqrt{x}} & ]0;+\infty[\\
\hline
\rule[-4pt]{0pt}{15pt} \mathbf{R} & f(x) = \cos{x} & f'(x) = -\sin{x} & \mathbf{R}\\
\hline
\rule[-4pt]{0pt}{15pt} \mathbf{R} & f(x) = \sin{x} & f'(x) = \cos{x} & \mathbf{R}\\
\hline
\rule[-12pt]{0pt}{30pt} ]0;+\infty[ & f(x) = \ln (x) & f'(x) = \dfrac{1}{x} & ]0;+\infty[ \\
\hline
\rule[-4pt]{0pt}{15pt} \mathbf{R} & f(x) = \text{e}^{x}=\exp (x) & f'(x) = \text{e}^{x}=\exp (x) & \mathbf{R}\\
\hline
\end{array}
\]

???- example "Exemple"
	Calculer la dérivée des fonctions suivantes :
	<ol>
	<li> $f(x) = x^5$ </li>
	<li> $f(x) = \dfrac{1}{x^3}$ </li>
	</ol>

	Courbe A FAIRE
	
	???- done "Solution"
		A FAIRE

!!! abstract "Théorème"
	Si $u$ et $v$ sont deux fonctions dérivables sur $I$ et $\lambda$ un réel, alors :

	- $u+v$ est dérivable sur $I$ et pour tout $x$ de $I$ $(u+v)'(x) = u'(x) + v'(x)$
	- $\lambda u$ est dérivable sur $I$ et pour tout $x$ de $I$ : $(\lambda u)'(x) = \lambda \times u'(x)$

???- example "Exemple"
	Calculer la dérivée des fonctions suivantes :
	<ol>
	<li> $f(x) = 3x^4-5x^3+2x+1$ </li>
	<li> $f(x) = \dfrac{1}{x^3} - 5\times \text{e}^{x} - 2\sqrt{x}$ </li>
	</ol>

	Courbe A FAIRE
	
	???- done "Solution"
		A FAIRE

???- tip "Astuce"
	
	- $f(x) = \dfrac{k}{x^n} = k \times \dfrac{1}{x^n}$ (c'est plus simple que la formule d'un quotient)
	- $f(x) = \dfrac{x^n}{k} = \dfrac{1}{k} \times x^n$ (c'est plus simple que la formule d'un quotient)

???- example "Exemple"
	Calculer la dérivée des fonctions suivantes :
	<ol>
	<li> $f(x) = 3x^4-5x^3+2x+1$ </li>
	<li> $f(x) = \dfrac{1}{x^3} - 5\times \text{e}^{x} - 2\sqrt{x}$ </li>
	</ol>

	Courbe A FAIRE
	
	???- done "Solution"
		A FAIRE


**Il est impératif de connaitre par c&#339;ur les formules suivantes :**

<span class = "Boite"> Si $u$ et $v$ sont deux fonctions dérivables sur $I$ : </span>

\[
\begin{array}{|c|c|c|c|}
\hline
\rule[-4pt]{0pt}{15pt} \text{Fonction $f$ définie sur} & \text{Par :}& \text{a pour fonction dérivée}&\text{la fonction est dérivable sur}\\
\hline
\rule[-4pt]{0pt}{15pt} I & u + v & u' + v' & I \\
\hline
\rule[-4pt]{0pt}{15pt} I & k \times u \text{ (k un réel constant)} & k \times u' & I \\
\hline
\rule[-4pt]{0pt}{15pt} I & u \times v & u'\times v + u \times v' & I \\
\hline
\begin{array}{c} J \subset I \text{ tel que }\\ \text{pour tout } x \in J,\ v(x) \neq 0 \end{array} & \dfrac{1}{v}
& \dfrac{- v'}{v^2}
&
\begin{array}{c} J \subset I \text{ tel que }\\ \text{pour tout } x \in J,\ v(x) \neq 0 \end{array}\\
\hline
\begin{array}{c} J \subset I \text{ tel que }\\ \text{pour tout } x \in J,\ v(x) \neq 0 \end{array}& \dfrac{u}{v}
& \dfrac{u'v-v'u}{v^2}
& 
\begin{array}{c} J \subset I \text{ tel que }\\ \text{pour tout } x \in J,\ v(x) \neq 0 \end{array}\\
\hline
\begin{array}{c} J \subset I \text{ tel que }\\ \text{pour tout } x \in J,\ u(x) \geq 0 \end{array}& \sqrt{u}
& \dfrac{u'}{2 \sqrt{u}}
&
\begin{array}{c} J \subset I \text{ tel que }\\ \text{pour tout } x \in J,\ u(x) > 0 \end{array}\\
\hline
\begin{array}{c} v \text{ est définie sur } J\\ u \text{ est définie sur } I\\ \text{ et } \forall x \in I,\ u(x) \in J \end{array}& v \circ u
& u' \times \left( v' \circ u \right)
&
I
\\
\hline
\end{array}
\]

Quant à la dernière formule du tableau précédent, elle peut s'appliquer aux cas particuliers les plus rencontrés :<span id="Tab_cas_part"></span>


\[
\begin{array}{|c|c|c|c|}
\hline
\rule[-4pt]{0pt}{15pt} \text{Fonction $f$ définie sur} & \text{Par :}& \text{a pour fonction dérivée}&\text{la fonction est dérivable sur}\\
\hline
I & \text{e}^{u}=\exp (u) & u' \text{e}^{u}=u' \exp (u) & I \\
\hline
\rule[-12pt]{0pt}{30pt}
\begin{array}{c} J \subset I \text{ tel que }\\ \text{pour tout } x \in J,\ u(x) > 0 \end{array}& \ln (u) \ (u>0)
& \dfrac{u'}{u}
&
\begin{array}{c} J \subset I \text{ tel que }\\ \text{pour tout } x \in J,\ u(x) > 0 \end{array}\\
\hline
\rule[-4pt]{0pt}{15pt} I & \cos(u) & -u' \times \sin (u) & I \\
\hline
\rule[-4pt]{0pt}{15pt} I & \sin(u) & u' \times \cos (u) & I \\
\hline
\rule[-12pt]{0pt}{30pt} mx+p>0 & \ln(mx+p) & \dfrac{m}{mx+p} & mx+p>0 \\
\hline
\rule[-4pt]{0pt}{15pt} \mathbf{R} & \exp(mx+p)=\text{e}^{mx+p} & m\exp(mx+p) = m \text{e}^{mx+p} & \mathbf{R} \\
\hline
\mathbf{R} & \cos(mx+p)  & -m\sin(mx+p) & \mathbf{R} \\
\hline
\mathbf{R} & \sin(mx+p)  & m\cos(mx+p) & \mathbf{R} \\
\hline
\end{array}
\]

???- example "Exemple"
	A FAIRE
	
	???- done "Solution"
		A FAIRE

**Il est indispensable de savoir dériver les fonctions en utilisant les formules précédents !**

!!! warning "Attention"

	Il faut faire attention aux parenthèses, invisibles dans les formules précédentes ! Par exemple :

	\[ \left(\dfrac{u}{v}\right)'(x) = \dfrac{(u'(x)) \times (v(x)) - (v'(x)) \times (u(x))}{(u(x))^2} \]

???- example "Exemple"
	Dériver $f(x) = \dfrac{2x^2-3}{x^3-4}$
	
	???- done "Solution"
		A FAIRE
