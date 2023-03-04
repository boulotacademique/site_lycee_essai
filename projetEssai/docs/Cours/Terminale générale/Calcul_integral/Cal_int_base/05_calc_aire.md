# Application : calcul d'aire

## Aire sous une courbe


!!! info "Cas d'une fonction positive"
    Soit une fonction $f$ continue sur un intervalle $[a;b]$ et $\mc{C}$ sa courbe représentative de $f$ dans un repère orthogonal. On note $\mc{D}$ la partie du plan limitée par :
    <ul>
    </li>
    <li> la courbe $\mc{C}$</li>
    <li> l'axe des abscisses</li>
    <li> les droites verticales d'équations $x=a$ et $x=b$.</li>
    </ul>

    Si $f$ est positive sur $[a;b]$, alors l'aire de $\mc{D}$ en u.a. est $\displaystyle\int_a^b f(x) \dx$

    [![ aire ](../Image/Im09.png){.Center_lien}](../Image/Im09.png)

    $\text{Aire}(\mc{D}) = \displaystyle\int_a^b f(x) \dx$ en u.a.

!!! info "Cas d'une fonction négative"
    Si $f$ est négative sur $[a;b]$, alors l'aire de $\mc{D}$ est $-\displaystyle\int_a^b f(x) \dx=\displaystyle\int_a^b (-f(x)) \dx$

    [![ aire ](../Image/Im10.png){.Center_lien}](../Image/Im10.png)

    $\text{Aire}(\mc{D}) = -\displaystyle\int_a^b f(x) \dx$ en u.a.

!!! tip "Cas des fonctions de signes quelconques"
    Si $f$ change de signe sur $[a;b]$, alors on calcule les aires sur chaque intervalle de $[a;b]$ où $f$ est de signe constant. L'aire totale est alors la somme des aires calculées.

    $\text{Aire}(\mc{D})=\left( -\displaystyle\int_1^3 f(x) \dx \right) + \left( \displaystyle\int_3^4 f(x) \dx \right) $

!!! example "Exemple : cas où $f$ est négative sur $I$"

    Soit $\left(\text{O}; \text{I} , \text{J} \right)$ est un repère orthogonal d'unités graphiques $2$ cm en abscisse et $1$ cm en ordonnée.

    Soit $f(x)=-x^2-x-1$ définie sur $\R$ et $\mc{C}$ sa courbe représentative. Calculer l'aire de la zone $\mc{D}$ limitée par :
    <ul>
    <li> la courbe $\mc{C}$</li>
    <li> l'axe des abscisse</li>
    <li> les droites d'équation $x=-1$ et $x=0$</li>
    </ul>

    \begin{eqnarray*}
    \displaystyle\int_{-1}^0 f(x) \dx & = & \ldots
    \displaystyle\int_{-1}^0 -x^2-x-1 \dx\\
    & = & \left[ -\dfrac{x^3}{3}-\dfrac{x^2}{2}-x \right]_{-1}^0\\
    & = & \left( -\dfrac{0^3}{3}-\dfrac{0^2}{2}-0 \right)-\left( -\dfrac{(-1)^3}{3}-\dfrac{(-1)^2}{2}-(-1) \right)\\
    & = & 0-\left( \dfrac{5}{6} \right)\\
    & = & -\dfrac{5}{6} 
    \end{eqnarray*}

    Comme $f$ négative sur $[-1;0]$, alors $\text{Aire}(\mc{D})={\color{white}-\displaystyle\int_{-1}^0 f(x) \dx}$ u.a.
    
    Donc $\text{Aire}(\mc{D})={\color{white}\dfrac{5}{6}}$ u.a.

    Comme $1$ u.a. $={\color{white}2} \text{ cm}^2$, $\text{Aire}(\mc{D})={\color{white}2 \times \dfrac{5}{6} = \dfrac{5}{3}} \cm^2$.
 

!!! example "Exemple : cas où $f$ change de signes sur $I$"

    Soit $\left(\text{O}; \text{I} , \text{J} \right)$ est un repère orthogonal d'unités graphiques $1.5$ cm en abscisse et $3$ cm pour $20$ unités en ordonnée.

    Soit $f(x)=2x^2+2x-24$ définie sur $\R$ et $\mc{C}$ sa courbe représentative. Calculer l'aire de la zone $\mc{D}$ limitée par :
    <ul>
    <li> la courbe $\mc{C}$</li>
    <li> l'axe des abscisse</li>
    <li> les droites d'équation $x=1$ et $x=4$</li>
    </ul>

    <ul>
    <li> Ici, $f$ est négative sur $[1;3]$.
    
    \begin{eqnarray*}
    \displaystyle\int_1^3 f(x) \dx & = & \ldots
    \displaystyle\int_1^3 2x^2+2x-24 \dx\\
    & = & \left[ 2\dfrac{x^3}{3} + x^2 -24x \right]_1^3\\
    & = & \left( 2\dfrac{3^3}{3} + 3^2 -24 \times 3 \right) - \left( 2\dfrac{1^3}{3} + 1^2 -24 \times 1 \right)\\
    & = & \left( -45 \right) - \left( \dfrac{-67}{3} \right)\\
    & = & \dfrac{-68}{3}
    \end{eqnarray*}
    
    Donc $\Aire(\mc{D}_1)={\color{white}-\displaystyle\int_1^3 f(x) \dx=\dfrac{68}{3}}$ u.a.
    </li>
    <li> Ici, $f$ est positive sur $[3;4]$.

    \begin{eqnarray*}
    \displaystyle\int_3^4 f(x) \dx & = & \ldots
    \displaystyle\int_3^4 2x^2+2x-24 \dx\\
    & = & \left[ 2\dfrac{x^3}{3} + x^2 -24x \right]_3^4\\
    & = & \left( 2\dfrac{4^3}{3} + 4^2 -24 \times 4 \right) - \left( 2\dfrac{3^3}{3} + 3^2 -24 \times 3 \right)\\
    & = & \left( \dfrac{-112}{3} \right) - \left( -45 \right)\\
    & = & \dfrac{23}{3}
    \end{eqnarray*}

    Donc $\Aire(\mc{D}_2)={\color{white}\displaystyle\int_3^4 f(x) \dx=\dfrac{23}{3}}$ u.a.
    </li>
    <li> Donc $\Aire(\mc{D})={\color{white}\dfrac{68}{3}+\dfrac{23}{3}=\dfrac{91}{3}}$ u.a.
    
    Comme $1 \ua = {\color{white}1.5 \times 0.15} \cm^2$, $\Aire(\mc{D})={\color{white}\dfrac{91}{3} \times 0.225=\dfrac{273}{40} =6.825} \cm^2$
    </li>
    </ul>
 

## Aire entre deux courbes

!!! info "Aire entre deux courbes"
    Soit deux fonctions $f$ et $g$ continues sur un intervalle $[a;b]$ de courbe respective $\mc{C}_f$ et $\mc{C}_g$ telles que, pour tout $x$ de  $[a;b]$, $f(x) \leq g(x)$.
    
    Alors l'aire, en unité d'aire, de la partie du plan notée $\mc{D}$ limitée par :
    <ul>
    </li>
    <li> la courbe $\mc{C}_f$
    </li>
    <li> la courbe $\mc{C}_g$
    </li>
    <li> les droites d'équations $x=a$ et $x=b$
    </li>
    </ul>
    est $\displaystyle\int_a^b (g(x)-f(x)) \dx$.

    Ici, comme $g(x)\geq f(x)$ sur $[a;b]$, $\Aire(\mc{D})=\displaystyle\int_a^b (g(x)-f(x)) \dx$

\begin{rque}
Naturellement, si les deux courbes se croisent, il faut calculer les aires de différentes zones et les ajouter.
\end{rque}Calcul d'aire

\section{Application au calcul d'aire}

\subsection{Aire sous une courbe}

!!! info " "
Soit une fonction $f$ continue sur un intervalle $[a;b]$ et $\mc{C}$ sa courbe représentative de $f$ dans un repère orthogonal. On note $\mc{D}$ la partie du plan limitée par :
<ul>
</li>
<li> la courbe $\mc{C}$
</li>
<li> l'axe des abscisses
</li>
<li> les droites verticales d'équations $x=a$ et $x=b$.
</li>
</ul>
\begin{enumerate}[a)]
</li>
<li> Si $f$ est positive sur $[a;b]$, alors l'aire de $\mc{D}$ en u.a. est $\displaystyle\int_a^b f(x) \dx$
\begin{center}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.5cm,y=0.3cm]

\draw [color=black,dotted, xstep=1.5cm,ystep=0.3cm] (-3.5,-1) grid (5.5,12);
\draw[->,color=black] (-3.5,0) -- (5.5,0);
\foreach \x in {-3,-2,-1,1,2,3,4,5}
\draw[shift={(\x,0)},color=black] (0pt,2pt) -- (0pt,-2pt) node[below left] {\footnotesize $\x$};
\draw[->,color=black] (0,-1) -- (0,12);
\foreach \y in {-1,1,5,10}
\draw[shift={(0,\y)},color=black] (2pt,0pt) -- (-2pt,0pt) node[left] {\footnotesize $\y$};
\draw[color=black] (0pt,-10pt) node[right] {\footnotesize $0$};
\clip(-3.5,-1) rectangle (5.5,12);
\draw[fill=black,fill opacity=0.1,domain=-1:2] plot({\x},{10*(2.718281828)^(-\x*\x/10)}) -- (2,0) -- (-1,0) -- cycle;
%\draw[fill=black,fill opacity=0.1] plot[raw gnuplot, id=func1] function{set samples 100; set xrange [-1.0:2.0]; plot 10*2.718281828**((-x**2)/10)} -- (2,0) -- (-1,0) -- cycle;
%\draw[line width=2.4pt,domain=-1:5] plot({\x},{2*(\x-3)*(\x+4)});
\draw[line width=2pt,domain=-3:5] plot({\x},{10*(2.718281828)^(-\x*\x/10)});
%\draw[line width=2pt] plot[raw gnuplot, id=func0] function{set samples 100; set xrange [-3:5]; plot 10*2.718281828**((-x**2)/10)};
\draw [line width=2.4pt] (-1,0)-- (-1,9.05);
\draw [line width=2.4pt] (-1,0)-- (2,0);
\draw [line width=2.4pt] (2,0)-- (2,6.7);
%\begin{scriptsize}
\draw[color=black] (-1.14,4.7) node[rotate=90] {$x=a$};
\draw[color=black] (2.13,3.52) node[rotate=90] {$x=b$};
\draw (1.5,9) node{$\mc{C}$};
\draw (0.5,5) node{$\mc{D}$};
%\end{scriptsize}
\end{tikzpicture}\\
$\text{Aire}(\mc{D}) = \displaystyle\int_a^b f(x) \dx$ en u.a.
\end{center}
</li>
<li> Si $f$ est négative sur $[a;b]$, alors l'aire de $\mc{D}$ est $-\displaystyle\int_a^b f(x) \dx=\displaystyle\int_a^b (-f(x)) \dx$
\begin{center}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.5cm,y=0.3cm]
\draw[color=black] (0pt,1pt) node[above right] {\footnotesize $0$};
\draw [color=black,dotted, xstep=1.5cm,ystep=0.3cm] (-5.5,-11) grid (3.5,1);
\draw[->,color=black] (-5,0) -- (3.5,0);
\foreach \x in {3,2,1,-1,-2,-3,-4,-5}
\draw[shift={(\x,0)},color=black] (0pt,2pt) -- (0pt,-2pt) node[above left] {\footnotesize $\x$};
\draw[->,color=black] (0,-12) -- (0,1);
\foreach \y in {-1,-5,-10}
\draw[shift={(0,\y)},color=black] (2pt,0pt) -- (-2pt,0pt) node[left] {\footnotesize $\y$};
\clip(-5.5,-12) rectangle (3.5,1);
\draw[fill=black,fill opacity=0.1,domain=-1:2] plot({\x},{-10*(2.718281828)^(-\x*\x/10)}) -- (2,0) -- (-1,0) -- cycle;
%\draw[fill=black,fill opacity=0.1] plot[raw gnuplot, id=func1] function{set samples 100; set xrange [-1.0:2.0]; plot -10*2.718281828**((-x**2)/10)} -- (2,0) -- (-1,0) -- cycle;
\draw[line width=2pt,domain=-3:5] plot({\x},{-10*(2.718281828)^(-\x*\x/10)});
%\draw[line width=2pt] plot[raw gnuplot, id=func0] function{set samples 100; set xrange [-5:3]; plot -10*2.718281828**((-x**2)/10)};
\draw [line width=2.4pt] (-1,0)-- (-1,-9.05);
\draw [line width=2.4pt] (-1,0)-- (2,0);
\draw [line width=2.4pt] (2,0)-- (2,-6.7);
%\begin{scriptsize}
\draw[color=black] (-1.14,-4.7) node[rotate=90] {$x=a$};
\draw[color=black] (2.13,-3.52) node[rotate=90] {$x=b$};
\draw (1.5,-9) node{$\mc{C}$};
\draw (0.5,-5) node{$\mc{D}$};
%\end{scriptsize}
\end{tikzpicture}\\
$\text{Aire}(\mc{D}) = -\displaystyle\int_a^b f(x) \dx$ en u.a.
\end{center}
%\end{enumerate}
%\end{theo}
%!!! info " "[Theorème (suite)]
%\begin{enumerate}
</li>
<li>%[c)]%
 Si $f$ change de signe sur $[a;b]$, alors on calcule les aires sur chaque intervalle de $[a;b]$ où $f$ est de signe constant. L'aire totale est alors la somme des aires calculées.
\begin{center}
\definecolor{uuuuuu}{rgb}{0.27,0.27,0.27}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=0.8cm,y=0.07cm]
\draw [color=black,dotted, xstep=0.8cm,ystep=0.7cm] (-1.5,-26) grid (5,27);
\draw[->,color=black] (-1.5,0) -- (5,0);
\foreach \x in {-1,1,2,3,4}
\draw[shift={(\x,0)},color=black] (0pt,2pt) -- (0pt,-2pt) node[below] {\footnotesize $\x$};
\draw[->,color=black] (0,-26) -- (0,27);
\foreach \y in {-25,-10,1,10,25}
\draw[shift={(0,\y)},color=black] (-2pt,0pt) node[left] {\footnotesize $\y$};
\draw[color=black] (0pt,-10pt) node[right] {\footnotesize $0$};
\clip(-1.5,-26) rectangle (5,27);
\draw[fill=black,fill opacity=0.1,domain=1:4] plot({\x},{2*(\x-3)*(\x+4)})  -- (4,0) -- (1,0) -- cycle;
%\draw[fill=black,fill opacity=0.1] plot[raw gnuplot, id=func5] function{set samples 100; set xrange [1.0:4.0]; plot 2*(x-3)*(x+4)} -- (4,0) -- (1,0) -- cycle;
\draw[line width=2.4pt,domain=-1:5] plot({\x},{2*(\x-3)*(\x+4)});
%\draw[line width=2.4pt] plot[raw gnuplot, id=func4] function{set samples 100; set xrange [-1:5]; plot 2*(x-3)*(x+4)};
\draw [line width=2pt] (1,0)-- (1,-20);
\draw [line width=2pt] (1,0)-- (3,0);
\draw [line width=2pt] (3,0)-- (4,0);
\draw [line width=2pt] (4,0)-- (4,16);
%\begin{scriptsize}
\fill [color=black] (1,0) circle (1.5pt);
%\draw[color=black] (1.04,0.97) node {$A$};
\fill [color=black] (4,0) circle (1.5pt);
%\draw[color=black] (4.05,0.97) node {$B$};
\fill [color=black] (3,0) circle (1.5pt);
%\draw[color=black] (2.98,1.11) node {$C$};
\fill [color=uuuuuu] (1,-20) circle (1.5pt);
%\draw[color=uuuuuu] (1.06,-20.34) node {$D$};
\fill [color=uuuuuu] (4,16) circle (1.5pt);
%\draw[color=uuuuuu] (3.96,17.6) node {$E$};
%\end{scriptsize}
\end{tikzpicture}\\
$\text{Aire}(\mc{D})=\left( -\displaystyle\int_1^3 f(x) \dx \right) + \left( \displaystyle\int_3^4 f(x) \dx \right) $
\end{center}
\end{enumerate}
\end{theo}
%
%!!! example "Exemple"[Cas où $f$ est négative sur $I$]
%Soit $\left(\text{O}; \text{I} , \text{J} \right)$ est un repère orthogonal d'unités graphiques $2$ cm en abscisse et $1$ cm en ordonnée.\\
%Soit $f(x)=-x^2-x-1$ définie sur $\R$ et $\mc{C}$ sa courbe représentative. Calculer l'aire de la zone $\mc{D}$ limitée par :
%<ul>
%</li>
<li> la courbe $\mc{C}$
%</li>
<li> l'axe des abscisse
%</li>
<li> les droites d'équation $x=-1$ et $x=0$
%</li>
</ul>
%\begin{center}
%\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=2.0cm,y=0.5cm]
%\draw [color=black,dotted, xstep=2.0cm,ystep=0.5cm] (-2.2,-6) grid (2,1);
%\draw[->,color=black] (-2.2,0) -- (2,0);
%\foreach \x in {-2,-1,1}
%\draw[shift={(\x,0)},color=black] (0pt,2pt) -- (0pt,-2pt) node[below] {\footnotesize $\x$};
%\draw[->,color=black] (0,-6) -- (0,1);
%\foreach \y in {-6,-5,-4,-3,-2,-1}
%\draw[shift={(0,\y)},color=black] (2pt,0pt) -- (-2pt,0pt) node[left] {\footnotesize $\y$};
%\draw[color=black] (0pt,0pt) node[above right] {\footnotesize $0$};
%\clip(-2.2,-6) rectangle (2,1);
%\draw[fill=black,fill opacity=0.1] plot[raw gnuplot, id=func3] function{set samples 100; set xrange [-1.0:0.0]; plot -x**2-x-1} -- (0,0) -- (-1,0) -- cycle;
%\draw[line width=2.4pt] plot[raw gnuplot, id=func2] function{set samples 100; set xrange [-1.9:1.4]; plot -x**2-x-1};
%\end{tikzpicture}
%\end{center}
%\begin{eqnarray*}
%\displaystyle\int_{-1}^0 f(x) \dx & = & \ldots
%%\displaystyle\int_{-1}^0 -x^2-x-1 \dx\\
%% & = & \left[ -\dfrac{x^3}{3}-\dfrac{x^2}{2}-x \right]_{-1}^0\\
%% & = & \left( -\dfrac{0^3}{3}-\dfrac{0^2}{2}-0 \right)-\left( -\dfrac{(-1)^3}{3}-\dfrac{(-1)^2}{2}-(-1) \right)\\
%% & = & 0-\left( \dfrac{5}{6} \right)\\
%% & = & -\dfrac{5}{6} 
%\end{eqnarray*}
%
%Comme $f$ négative sur $[-1;0]$, alors $\text{Aire}(\mc{D})={\color{white}-\displaystyle\int_{-1}^0 f(x) \dx}$ u.a.\\
%Donc $\text{Aire}(\mc{D})={\color{white}\dfrac{5}{6}}$ u.a.\\
%Comme $1$ u.a. $={\color{white}2} \text{ cm}^2$, $\text{Aire}(\mc{D})={\color{white}2 \times \dfrac{5}{6} = \dfrac{5}{3}} \cm^2$
% 

%!!! example "Exemple"[Cas où $f$ change de signes sur $I$]
%Soit $\left(\text{O}; \text{I} , \text{J} \right)$ est un repère orthogonal d'unités graphiques $1.5$ cm en abscisse et $3$ cm pour $20$ unités en ordonnée.\\
%Soit $f(x)=2x^2+2x-24$ définie sur $\R$ et $\mc{C}$ sa courbe représentative. Calculer l'aire de la zone $\mc{D}$ limitée par :
%<ul>
%</li>
<li> la courbe $\mc{C}$
%</li>
<li> l'axe des abscisse
%</li>
<li> les droites d'équation $x=1$ et $x=4$
%</li>
</ul>
%\begin{center}
%\definecolor{uuuuuu}{rgb}{0.27,0.27,0.27}
%\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.5cm,y=0.15cm]
%\draw [color=black,dotted, xstep=1.5cm,ystep=0.15cm] (-1.5,-26) grid (5,27);
%\draw[->,color=black] (-1.5,0) -- (5,0);
%\foreach \x in {-1,1,2,3,4}
%\draw[shift={(\x,0)},color=black] (0pt,2pt) -- (0pt,-2pt) node[below] {\footnotesize $\x$};
%\draw[->,color=black] (0,-26) -- (0,27);
%\foreach \y in {-25,-10,1,10,25}
%\draw[shift={(0,\y)},color=black] (-2pt,0pt) node[left] {\footnotesize $\y$};
%\draw[color=black] (0pt,-10pt) node[right] {\footnotesize $0$};
%\clip(-1.5,-26) rectangle (5,27);
%\draw[fill=black,fill opacity=0.1] plot[raw gnuplot, id=func5] function{set samples 100; set xrange [1.0:4.0]; plot 2*(x-3)*(x+4)} -- (4,0) -- (1,0) -- cycle;
%\draw[line width=2.4pt] plot[raw gnuplot, id=func4] function{set samples 100; set xrange [-1:5]; plot 2*(x-3)*(x+4)};
%\draw [line width=2pt] (1,0)-- (1,-20);
%\draw [line width=2pt] (1,0)-- (3,0);
%\draw [line width=2pt] (3,0)-- (4,0);
%\draw [line width=2pt] (4,0)-- (4,16);
%%\begin{scriptsize}
%\fill [color=black] (1,0) circle (1.5pt);
%%\draw[color=black] (1.04,0.97) node {$A$};
%\fill [color=black] (4,0) circle (1.5pt);
%%\draw[color=black] (4.05,0.97) node {$B$};
%\fill [color=black] (3,0) circle (1.5pt);
%%\draw[color=black] (2.98,1.11) node {$C$};
%\fill [color=uuuuuu] (1,-20) circle (1.5pt);
%%\draw[color=uuuuuu] (1.06,-20.34) node {$D$};
%\fill [color=uuuuuu] (4,16) circle (1.5pt);
%%\draw[color=uuuuuu] (3.96,17.6) node {$E$};
%\draw (1.8,-8) node{$\mc{D}_1$};
%\draw (3.7,4) node{$\mc{D}_2$};
%%\end{scriptsize}
%\end{tikzpicture}
%\end{center}
%<ul>
%</li>
<li> Ici, $f$ est négative sur \ldots {\color{white} $[1;3]$}.
%\begin{eqnarray*}
%\displaystyle\int_1^3 f(x) \dx & = & \ldots
%%\displaystyle\int_1^3 2x^2+2x-24 \dx\\
%% & = & \left[ 2\dfrac{x^3}{3} + x^2 -24x \right]_1^3\\
%% & = & \left( 2\dfrac{3^3}{3} + 3^2 -24 \times 3 \right) - \left( 2\dfrac{1^3}{3} + 1^2 -24 \times 1 \right)\\
%% & = & \left( -45 \right) - \left( \dfrac{-67}{3} \right)\\
%% & = & \dfrac{-68}{3}
%\end{eqnarray*}
%Donc $\Aire(\mc{D}_1)={\color{white}-\displaystyle\int_1^3 f(x) \dx=\dfrac{68}{3}}$ u.a.
%</li>
<li> Ici, $f$ est positive sur \ldots {\color{white}$[3;4]$ }.
%\begin{eqnarray*}
%\displaystyle\int_3^4 f(x) \dx & = & \ldots
%% \displaystyle\int_3^4 2x^2+2x-24 \dx\\
%% & = & \left[ 2\dfrac{x^3}{3} + x^2 -24x \right]_3^4\\
%% & = & \left( 2\dfrac{4^3}{3} + 4^2 -24 \times 4 \right) - \left( 2\dfrac{3^3}{3} + 3^2 -24 \times 3 \right)\\
%% & = & \left( \dfrac{-112}{3} \right) - \left( -45 \right)\\
%% & = & \dfrac{23}{3}
%\end{eqnarray*}
%Donc $\Aire(\mc{D}_2)={\color{white}\displaystyle\int_3^4 f(x) \dx=\dfrac{23}{3}}$ u.a.
%</li>
<li> Donc $\Aire(\mc{D})={\color{white}\dfrac{68}{3}+\dfrac{23}{3}=\dfrac{91}{3}}$ u.a.\\
%Comme $1 \ua = {\color{white}1.5 \times 0.15} \cm^2$, $\Aire(\mc{D})={\color{white}\dfrac{91}{3} \times 0.225=\dfrac{273}{40} =6.825} \cm^2$
%</li>
</ul>
% 

\subsection{Aire entre deux courbes}

!!! info " "
Soit deux fonctions $f$ et $g$ continues sur un intervalle $[a;b]$ de courbe respective $\mc{C}_f$ et $\mc{C}_g$ telles que, pour tout $x$ de  $[a;b]$, $f(x) \leq g(x)$.\\
Alors l'aire, en unité d'aire, de la partie du plan notée $\mc{D}$ limitée par :
<ul>
</li>
<li> la courbe $\mc{C}_f$
</li>
<li> la courbe $\mc{C}_g$
</li>
<li> les droites d'équations $x=a$ et $x=b$
</li>
</ul>
est $\displaystyle\int_a^b (g(x)-f(x)) \dx$.
\begin{center}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.5cm,y=0.5cm]
\draw [color=black,dotted, xstep=1.5cm,ystep=0.5cm] (-1,-3) grid (3,3);
\draw[->,color=black] (-1,0) -- (3,0);
\foreach \x in {-1,1,2}
\draw[shift={(\x,0)},color=black] (0pt,2pt) -- (0pt,-2pt) node[below] {\footnotesize $\x$};
\draw[->,color=black] (0,-3) -- (0,3);
\foreach \y in {-3,-2,-1,1,2}
\draw[shift={(0,\y)},color=black] (2pt,0pt) -- (-2pt,0pt) node[left] {\footnotesize $\y$};
\draw[color=black] (0pt,-10pt) node[right] {\footnotesize $0$};
\clip(-1,-3) rectangle (3,3);
\draw[fill=black,fill opacity=0.1,domain=-0.3333:1.6667] plot({\x},{2.5*sin((deg(\x+1.3))})  -- (1.67,-1.98) --  plot({1.33-\x},{2*cos((deg(1.33-\x+1.3))}) --(-0.33,2.1) -- cycle;
%\draw[fill=black,fill opacity=0.1] { plot[raw gnuplot, id=func2] function{set samples 100; set xrange [-0.3333333333333333:1.6666666666666667]; plot 2.5*sin((x+1.3))}} -- (1.67,-1.98) {-- plot[raw gnuplot, id=func3] function{set parametric ; set samples 100; set trange [-0.3333333333333333:1.6666666666666667]; plot 1.33-t,2*cos((1.33-t+1.3))}} -- (-0.33,2.1) -- cycle;
\draw[line width=2pt,domain=-0.6:2.3] plot({\x},{2.5*sin(deg(\x+1.3))});
%\draw[line width=2pt] plot[raw gnuplot, id=func0] function{set samples 100; set xrange [-0.6:2.3]; plot 2.5*sin((x+1.3))};
\draw[line width=2pt,domain=-0.6:2.3] plot({\x},{2*cos(deg(\x+1.3))});
%\draw[line width=2pt] plot[raw gnuplot, id=func1] function{set samples 100; set xrange [-0.6:2.3]; plot 2*cos((x+1.3))};
\draw [line width=1.6pt] (-0.33,1.12)-- (-0.33,2.08);
\draw [line width=1.6pt] (1.67,-1.95)-- (1.67,0.4);
\draw (0.8,2.5) node {$\mc{C}_g$};
\draw (0.5,-0.9) node {$\mc{C}_f$};
\end{tikzpicture}\\
Ici, comme $g(x)\geq f(x)$ sur $[a;b]$, $\Aire(\mc{D})=\displaystyle\int_a^b (g(x)-f(x)) \dx$
\end{center}
\end{theo}

\begin{rque}
Naturellement, si les deux courbes se croisent, il faut calculer les aires de différentes zones et les ajouter.
\end{rque}