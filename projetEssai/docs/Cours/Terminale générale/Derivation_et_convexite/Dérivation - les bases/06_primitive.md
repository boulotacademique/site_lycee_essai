# Calcul de primitive

## Primitives des fonctions usuelles


\[
\begin{array}{|c|c|c|c|}
\hline
\rule[-4pt]{0pt}{15pt} \text{Fonction $f$ définie sur} & \text{Par :}& \text{a pour primitive}& \text{sur} \\
\hline
\rule[-4pt]{0pt}{15pt} \R & f(x) = k & F(x) = kx  \ \text{(k cste)} & \R \\
\hline
\rule[-12pt]{0pt}{30pt} \R & f(x) = x^n \quad n \in \mathbb{N},\ n \geq 1 & F(x) = \dfrac{x^{n+1}}{n+1} & \R \\
\hline
\rule[-12pt]{0pt}{30pt} ]-\infty;0[ \text{ou}  ]0;+\infty[  & f(x) = x^n \quad n \in \mathbb{Z},\ n \leq -2 & F(x) = \dfrac{x^{n+1}}{n+1} & ]-\infty;0[ \text{ou}  ]0;+\infty[ \\
\hline
\rule[-12pt]{0pt}{30pt} ]-\infty;0[ \text{ou}  ]0;+\infty[  & f(x) = \dfrac{1}{x^n} \quad n \in \mathbb{N},\ n \geq 2 & F(x) = \dfrac{-1}{(n-1)x^{n-1}} & ]-\infty;0[ \text{ou}  ]0;+\infty[ \\
\hline
\rule[-12pt]{0pt}{30pt}]-\infty;0[ \text{ou}  ]0;+\infty[ & f(x) = \frac{1}{x} & F(x) = \ln (|x|) & ]-\infty;0[ \text{ou}  ]0;+\infty[\\
\hline
\rule[-12pt]{0pt}{30pt} \left]0;+\infty \right[ & f(x) = \dfrac{1}{\sqrt{x}} & F(x) = 2\sqrt{x} & ]0;+\infty[\\
\hline
\rule[-4pt]{0pt}{15pt} \R & f(x) = \cos{x} & F(x) = \sin{x} & \R\\
\hline
\rule[-4pt]{0pt}{15pt} \R & f(x) = \sin{x} & F(x) = -\cos{x} & \R\\
\hline
\rule[-12pt]{0pt}{30pt} \R & f(x) = \cos{(ax+b)} & F(x) = \dfrac{1}{a}\sin{(ax+b)} & \R\\
\hline
\rule[-12pt]{0pt}{30pt} \R & f(x) = \sin{(ax+b)} & F(x) = \dfrac{-1}{a}\cos{(ax+b)} & \R\\
\hline
\rule[-4pt]{0pt}{15pt} \R & f(x) = \ex^{x}=\exp (x) & F(x) = \ex^{x}=\exp (x) & \R\\
\hline
\rule[-12pt]{0pt}{30pt} \R & f(x) = \ex^{ax+b}=\exp (ax+b) & F(x) =\dfrac{1}{a} \ex^{ax+b}=\dfrac{1}{a}\exp (ax+b) & \R\\
\hline
\end{array}
\]


## Primitives et opération

!!! info "Primitive et opérations"
    Si $F$ et $G$ sont des primitives des fonctions $f$ et $g$ sur $I$
    <ul>
    <li> alors une primitive de $f+g$ est $F+G$</li>
    <li> alors une primitive de $\alpha f$ et $\alpha F$, pour $\alpha$ un nombre réel.</li>
    </ul>

???- example "Exemple"
    Déterminer les primitives des fonctions suivantes sur $I$ :
    <ol>
    <li> $f(x)=5x^3+3x^2-2x+7$ et $I=\R$</li>
    <li> $f(x)=\dfrac{1}{x}-\dfrac{1}{x^2}$ et $I=]0 ; +\infty[$</li>
    <li> $f(x) = \dfrac{3}{x^3} + \dfrac{1}{5x^2}$ et $I=]0 ; +\infty[$</li>
    <li> $f(x) = \ex^{2x}+5\ex^{-x+4}+3$ et $I=\R$</li>
    </ol>


???- example "Exemple"
    Déterminer la primitive $F$ de $f$ sur $I$ telle que $F(x_0)=y_0$:
    <ol>
    </li>
    <li> $f(x)=5x^3+3x^2-2x+7$, $I=\R$ et $F(-1)=4$
    </li>
    <li> $f(x)=\dfrac{1}{x}-\dfrac{1}{x^2}$, $I=]0 ; +\infty[$  et $F(2)=-5$
    </li>
    <li> $f(x) = \dfrac{3}{x^3} + \dfrac{1}{5x^2}$, $I=]0 ; +\infty[$  et $F(1)=0$
    </li>
    <li> $f(x) = \ex^{2x}+5\ex^{-x+4}+3$, $I=\R$  et $F(0)=3$
    </li>
    </ol>



\[
\begin{array}{|c|c|c|}
\hline
u \text{ est une fonction dérivable sur } I & \text{une primtive } F \text{ de } f \text{est : } & \text{Conditions sur } u\\
\hline
\rule[-12pt]{0pt}{30pt}  u' \times u^{n} (n\in \Z^* \text{ et } n\neq -1) & \dfrac{u^{n+1}}{n+1}  &  \text{si } n<-1, \text{ pour tout } x \text{ de } I :  u(x) \neq 0\\
\hline
\rule[-12pt]{0pt}{30pt}  \dfrac{v'}{v^2} & \dfrac{-1}{v} &  \text{Pour tout } x \text{ de } I : u(x) \neq 0 \\
\hline
\rule[-12pt]{0pt}{30pt}  \dfrac{u'}{u^{n}} \ \fbox{$\mathbf{n \geq 2}$} & \dfrac{-1}{(n-1)u^{n-1}}  &  \text{Pour tout } x \text{ de } I : u(x) \neq 0 \\
\hline
\rule[-12pt]{0pt}{30pt}  \dfrac{u'}{u}  & \ln (|u|)  &  \text{Pour tout } x \text{ de } I : u(x)\neq 0\\
\hline
\rule[-4pt]{0pt}{15pt} u' \ex^{u}=u' \exp (u) & \ex^{u}=\exp (u) & \\
\hline
\rule[-4pt]{0pt}{15pt} \dfrac{u'}{\sqrt{u}} & 2\sqrt{u} &  \text{Pour tout } x \text{ de } I : u(x)> 0 \\
\hline
\rule[-4pt]{0pt}{15pt}  u' \times \sin (u) & -\cos(u) & \\
\hline
\rule[-4pt]{0pt}{15pt}  u' \times \cos (u) & \sin(u) & \\
\hline
%\rule[-4pt]{0pt}{15pt} \dfrac{u'}{1+u} & \arctan(u) & \\
%\hline
\end{array}
\]

???- example "Exemple"
    Déterminer les primitives de $f$ sur $I$:
    <ol>
    <li> $f(x)= 6x(x^2-5)^3$, $I=\R_+$</li>
    <li> $f(x)=\dfrac{5}{2x+4}$, $I=\R_+$</li>
    <li> $f(x)=\dfrac{3x}{(x^2+5)^3}$, $I=\R_+$</li>
    <li> $f(x) = \dfrac{2}{\sqrt{3x+4}}$, $I=\R_+$</li>
    </ol>
