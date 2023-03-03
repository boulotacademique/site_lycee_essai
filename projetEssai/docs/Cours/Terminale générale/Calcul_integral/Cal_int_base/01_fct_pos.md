# Intégrale d'une fonction positive sur un intervalle $[a,b]$

## Définition

Soit f une fonction continue et positive sur un intervalle $[a,b]$ et $\mc{C}$ sa courbe représentative dans un repère orthogonal $\rep$.

La partie du plan situé entre la courbe , l'axe des abscisses et les droites d'équations $x=a$ et $x= b$ admet une aire.

!!!- info ""
    **L'intégrale de $a$ à $b$ de $f$** , notée $\int_a^b f(x) \dx$ est l'aire en unités d'aires de la partie du plan située entre la courbe, l 'axe des abscisses et les droites d'équations x=a et x= b.
    
    L'unité d'aire est l'aire du rectangle OIKJ. Elle est notée \textbf{u.a.}.

    

 $\int_a^b f(x) \dx$ se lit \og \textit{intégrale de $a$ à $b$ de $f(x)\dx$} \fg ou \og somme de $a$ à $b$ de $f(x )\dx$ \fg.\\
Les réels $a$ et $b$ sont appelés les bornes de l'intégrale.\\
Le symbole $\int$ est un S stylisé (initiale de somme) afin de rappeler que l'intégrale peut être obtenue comme la limite d'une somme d'aires de rectangles.\\
$f(x)\dx$ est l'aire d'un rectangle de dimension $f(x)$ et $\dx$. Derrière la notation $f(x)\dx$ se cache une multiplication.\\
La variable $x$ est dite muette , elle peut être remplacée par n'importe quelle lettre : $\int_a^b f(x) \dx = \int_a^b f(t) \dx[t]$

\begin{exple}
\begin{enumerate}
\item Calculer l'intégrale $A=\int_1^3 -2x+8 \dx$.
\begin{comment}
\vspace{3cm}
\end{comment}
\begin{Solub}
\\ La fonction $x \mapsto -2x+8$ est continue et positive sur $[1;3]$. Donc $\int_1^3 -2x+8 \dx$ est l'aire, en u.a., du trapèze $IABC$ rectangle en $I$ et en $A$.\\
Donc $\int_1^3 -2x+8 \dx = \dfrac{(IA+AB)\times IA}{2}=\dfrac{(6+2)\times 2}{2}=8$ (u.a.)
\end{Solub}
\item Si $\left(\text{O}; \text{I} , \text{J} \right)$ est un repère orthogonal d'unités graphiques $3$ cm en abscisse et $2$ cm en ordonnée, alors l'unité d'aire est égale à \ans{$2 \times 3=6$ $\text{cm}^2$}. On écrit $1$ u.a. = \ans{$6\ \text{cm}^2$}.\\
Donc dans un tel repère, l'aire serait de  \ans{$8\times 6 = 48\ \text{cm}^2$}. 
\end{enumerate}
\end{exple}

\begin{exple}
Soit $\left(\text{O}; \text{I} , \text{J} \right)$ est un repère orthogonal d'unités graphiques $3$ cm en abscisse et $0.5$ cm en ordonnée.
Soit $f$ la fonction dont la courbe $\mc{C}$ est donnée ci-dessous:
\begin{center}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=3.0cm,y=0.5cm]
\foreach \x in {-3,-2,-1,1}
\draw[shift={(\x,0)},color=black] (0pt,2pt) -- (0pt,-2pt) node[below right] {\footnotesize $\x$};
\draw[->,color=black] (0,-1) -- (0,8);
\foreach \y in {-1,1,2,3,4,5,6,7}
\draw[shift={(0,\y)},color=black] (2pt,0pt) -- (-2pt,0pt) node[left] {\footnotesize $\y$};
\draw[color=black] (0pt,-10pt) node[right] {\footnotesize $0$};
\clip(-3,-1) rectangle (2,8);
\draw[dotted] (-3,-1) grid (2,8);
\draw[->,color=black] (-3,0) -- (2,0);
\draw[domain=-3:2,smooth,variable=\x,line width=1.5pt] plot ({\x},{0.2*(\x+3)*(\x-2)*(\x-5)});
%\draw[line width=1.5pt] (1,0) -- (1,3.2);
%\draw[line width=1.5pt] (-2,0) -- (-2,5.6);
%\draw[fill=black,fill opacity=0.2] plot[raw gnuplot, id=func1] function{set samples 100; set xrange [-2.0:1.0]; plot 0.2*(x+3)*(x-2)*(x-5)} -- (1,0) -- (-2,0) -- cycle;
%\draw[line width=2pt] plot[raw gnuplot, id=func0] function{set samples 100; set xrange [-2.9:1.9]; plot 0.2*(x+3)*(x-2)*(x-5)};
\end{tikzpicture}
\end{center}
Alors $\int_{-2}^1 f(x) \dx$ est l'aire, exprimée en unités d'aire, de la zone grisée.\\
Attention, si (ici) on compte le quadrillage, on aura l'aire en $\text{cm}^2$ : \textbf{ce n'est donc pas } $\int_{-2}^1 f(x) \dx$.

Voici avec un découpage faisant apparaître les unités d'aire.

\begin{center}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=3.0cm,y=0.5cm]
\clip(-3,-1) rectangle (2,8);
\draw[dashed,step=1,color=red, line width=1pt] (-3,-1) grid (2,8);
\draw[dotted] (-3,-1) grid (2,8);
\draw[->,color=black] (-3,0) -- (2,0);
\foreach \x in {-3,-2,-1,1}
\draw[shift={(\x,0)},color=black] (0pt,2pt) -- (0pt,-2pt) node[below right] {\footnotesize $\x$};
\draw[->,color=black] (0,-1) -- (0,8);
\foreach \y in {-1,1,2,3,4,5,6,7}
\draw[shift={(0,\y)},color=black] (2pt,0pt) -- (-2pt,0pt) node[left] {\footnotesize $\y$};
\draw[color=black] (0pt,-10pt) node[right] {\footnotesize $0$};
\draw[domain=-3:2,smooth,variable=\x,line width=1.5pt] plot ({\x},{0.2*(\x+3)*(\x-2)*(\x-5)});
%\draw[fill=black,fill opacity=0.2] plot[raw gnuplot, id=func1] function{set samples 100; set xrange [-2.0:1.0]; plot 0.2*(x+3)*(x-2)*(x-5)} -- (1,0) -- (-2,0) -- cycle;
%\draw[line width=2pt] plot[raw gnuplot, id=func0] function{set samples 100; set xrange [-2.9:1.9]; plot 0.2*(x+3)*(x-2)*(x-5)};
\end{tikzpicture}
\end{center}
En comptant ces petits rectangles, on a :
\[ \int_{-2}^1 f(x) \dx \approx \ans{18} \]
Pour convertir en $\text{cm}^2$, il faut noter que $1$ u.a. = $3 \times 0.5 \text{ cm}^2$.\\
Donc ici l'aire vaut (environ) \ans{$1.5 \times 18=27 \text{ cm}^2$}.\\
\underline{BILAN :} 
\begin{itemize}
\item Comme $f$ est une fonction positive sur $[-2;1]$ : $\int_{-2}^1 f(x) \dx \approx \ans{18}$ u.a.
\item l'aire vaut (environ) \ans{$27 \text{ cm}^2$}.
\end{itemize}
\end{exple}

\begin{exple}
\begin{enumerate}
\item Soit $\left(\text{O}; \text{I} , \text{J} \right)$ est un repère orthogonal d'unités graphiques $2$ cm en abscisse et $0.5$ cm en ordonnée et $f$ la fonction définie par $f(x)=5$.
\begin{enumerate}
\item Tracer la courbe sur l'intervalle $[-3;4]$
\begin{Solub}
\\ \begin{tikzpicture}[x=1cm,y=0.5cm]
\draw[->,line width=2pt] (-3.5,0) -- (5.5,0);
\draw[->,line width=2pt] (0,-1) -- (0,6.5);
\foreach \x in {-3,-2,...,5}
{
	\draw (\x,-0.2) -- (\x,0.2);
	\draw (\x,-0.2) node[below]{\x};
}
\foreach \y in {1,2,...,6}
{
	\draw (-0.2,\y) -- (0.2,\y);
	\draw (-0.2,\y) node[left]{\y};
}
\draw (-3,5) -- (4,5);
\draw[dashed,fill=red!30!white,fill opacity=0.2] (-1,0) -- (-1,5) -- (2,5) -- (2,0) -- cycle ;
\end{tikzpicture} 
\end{Solub}
\item Calculer $\int_{-1}^2 f(x) \dx$
\begin{Solub}
\\
Comme $f$ est positive sur $[-1;2]$, $\int_{-1}^2 f(x) \dx$ est l'aire du rectangle en u.a. Donc $\int_{-1}^2 f(x) \dx = 3 \time 5 = 15 $
\end{Solub}
\end{enumerate}
\item Soit $\left(\text{O}; \text{I} , \text{J} \right)$ est un repère orthogonal d'unités graphiques $1$ cm en abscisse et $0.5$ cm en ordonnée et $f$ la fonction définie par $f(x)=-x+5$.
\begin{enumerate}
\item Tracer la courbe sur l'intervalle $[-3;4]$
\begin{Solub}
\\ \begin{tikzpicture}[x=1cm,y=0.5cm]
\draw[->,line width=2pt] (-3.5,0) -- (5.5,0);
\draw[->,line width=2pt] (0,-1) -- (0,6.5);
\foreach \x in {-3,-2,...,5}
{
	\draw (\x,-0.2) -- (\x,0.2);
	\draw (\x,-0.2) node[below]{\x};
}
\foreach \y in {1,2,...,6}
{
	\draw (-0.2,\y) -- (0.2,\y);
	\draw (-0.2,\y) node[left]{\y};
}
\draw (-3,8) -- (4,1);
\draw[dashed,fill=red!30!white,fill opacity=0.2] (-1,0) -- (-1,6) -- (2,3) -- (2,0) -- cycle ;
\end{tikzpicture} 
\end{Solub}
\item Calculer $\int_{-1}^2 f(x) \dx$ \\
(on rappelle que l'aire d'un trapèze est $\dfrac{(grande\ base\ +\ petite\ base)\times \ hauteur}{2}$)
\begin{Solub}
\\
Comme $f$ est positive sur $[-1;2]$, $\int_{-1}^2 f(x) \dx$ est l'aire du trapèze en u.a. Donc $\int_{-1}^2 f(x) \dx =\dfrac{(6+3)\times 3}{2} = \dfrac{27}{2} $
\end{Solub}

\end{enumerate}
\end{enumerate}
\end{exple}

\subsection{Propriétés}

\begin{theo}
\begin{enumerate}
\item L'intégrale d'une fonction continue et positive sur un intervalle $[a;b]$ est positive.
\[ \text{Si } \forall x \in[a;b] f(x)\geq 0 \text{ alors } \int_a^b f(x) \dx \geq 0  \]
\item Si $f=0$ sur $[a;b]$, alors $\int_a^b f(x) \dx =0$. 
\item Pour tout $a$ réel, $\int_a^a f(x) \dx =0$
\item Relation de Chasles : pour tous réels $a,b$ et $c$
\[ \int_a^c f(x) \dx + \int_c^b f(x) \dx =\int_a^b f(x) \dx \]
%\item Conservation par symétrie : soit $f$ est une fonction définie et continue sur $[-a;a]$, si $f$ est \textbf{paire} alors 
%\[ \int_{-a}^0 f(x) \dx = \int_0^a f(x) \dx \]
%\item Conservation par translation : soit $f$ est une fonction définie et continue sur $\R$, si $f$ est périodique de période $T$ alors :
%\[ \int_0^T f(x) \dx = \int_{a}^{a+T} f(x) \dx \text{ pour tout } a \in \R   \]
\end{enumerate}
\end{theo}

\begin{exple}
Soit $f$ une fonction définie sur $[-1;4]$ par :
\begin{itemize}
\item $f(x)=2x+2$ sur $[-1;0]$
\item $f(x)=\dfrac{1}{2}x+2$ sur $[0;2]$
\item $f(x)=\dfrac{-3}{2}x+6$ sur $[2;4]$
\end{itemize}
\begin{enumerate}
\item Tracer la courbe de $f$.
\begin{Solub}
\\ \begin{tikzpicture}[x=1cm,y=0.5cm]
\draw[->,line width=2pt] (-1.5,0) -- (4.5,0);
\draw[->,line width=2pt] (0,-1) -- (0,6.5);
\foreach \x in {-1,0,...,4}
{
	\draw (\x,-0.2) -- (\x,0.2);
	\draw (\x,-0.2) node[below]{\x};
}
\foreach \y in {1,2,...,6}
{
	\draw (-0.2,\y) -- (0.2,\y);
	\draw (-0.2,\y) node[left]{\y};
}
\draw (-1,0) -- (0,2) -- (2,3) -- (4,0);
\draw[dashed,fill=red!30!white,fill opacity=0.2] (-1,0) -- (0,2) -- (0,0)  -- cycle ;
\draw[dashed,fill=blue!30!white,fill opacity=0.2] (0,0) -- (0,2) -- (2,3) -- (2,0)  -- cycle ;
\draw[dashed,fill=green!30!white,fill opacity=0.2] (2,0) -- (2,3) -- (4,0) -- cycle ;
\end{tikzpicture} 
\end{Solub}
\item A l'aide de la relation de Chasles, se ramener à l'aire de triangles et de trapèzes.
\begin{Solub}
\\ $\int_{-1}^4 f(x) \dx =\int_{-1}^0 f(x) \dx + \int_{0}^2 f(x) \dx + \int_{2}^4 f(x) \dx $\\
Comme $f$ est positive sur $[-1;4]$, $\int_{-1}^4 f(x) \dx$ est l'aire en u.a. de la zone colorée. Il y a donc 2 triangles et un trapèze.
\end{Solub}
\item En déduire $\int_{-1}^4 f(x) \dx$
\begin{Solub}
\\
$\int_{-1}^4 f(x) \dx = \int_{-1}^0 f(x) \dx + \int_{0}^2 f(x) \dx + \int_{2}^4 f(x) \dx = \dfrac{2\times 1 }{2} + \dfrac{(2+3)\times 2}{2} + \dfrac{3 \times 2}{2} = 9$

\end{Solub}
\end{enumerate}
\end{exple}