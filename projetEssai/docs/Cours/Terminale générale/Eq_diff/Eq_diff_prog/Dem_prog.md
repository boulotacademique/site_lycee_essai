# Démonstration au programme


!!! info "Solution à $y'=ay$"
    Soit $a$ un réel.
    
    L'ensemble des solutions dans $\R$ de l'équation différentielle $y'=ay$ est l'ensemble des fonctions $x \mapsto C\ex^{ax}$, où $C$ est une constante réelle quelconque.


???- Abstract "Démonstration"
    1. Soit la fonction définie sur $\R$ par $f(x) = C \ex^{ax}$, où $C$ est un réel.  
    Démontrer que $f$ est une solution de l'équation différentielle $y'=ay$.

    2. Réciproquement : soit $h$ une solution de l'équation différentielle $y'=ay$.

        1. Calculer la dérivée de $g(x)=\ex^{-ax} h(x)$.
        2. En déduire que $g$ est une constante.
        3. En déduire que $h(x)=C\ex^{ax}$, où $C$ est un réel.

!!! info "Solution à $y'=ay+b$"
    Soit $a$ et $b$ des réels, $a$ non nul.
    
    L'ensemble des solutions dans $\R$ de l'équation différentielle $(E)$ $y'=ay+b$ est l'ensemble des fonctions $x \mapsto h(x)+g(x)$ où 
    
    - $h$ est une solution de $y'=ay$, donc $h(x)=C\ex^{ax}$
    - $g$ est une solution particulière de $y'=ay+b$; ici on choisit la solution constante $g(x)=-\dfrac{b}{a}$


???- abstract "Démonstration"
    On note $(E)$ l'équation $y'=ay+b$ et $(E_0)$ son équation &laquo; sans second membre &raquo; (ou homogène) associée $y'=ay$.
    
    1. Montrer que $f(x)=C\ex^{ax}-\dfrac{b}{a}$ (où $C$ est un réel) sont des solutions de $(E)$.
    2. Réciproquement : soit $f$ une solution de $(E)$.

        1. Montrer que $g(x)=\dfrac{-b}{a}$ est une solution de $(E)$.
        2. En déduire que $h(x)=f(x)-g(x)$ est une solution de $(E_0)$.

<!--

\begin{rque}[Pour aller plus loin]
\normalsize
Les démonstrations précédentes ont démontré les implications qui se cachent derrière l'équivalence du théorème.

A la place de :\\
\fbox{\begin{minipage}{\linewidth}
Soit $a$ un réel.\\
L'ensemble des solutions dans $\R$ de l'équation différentielle $y'=ay$ est l'ensemble des fonctions $x \mapsto C\ex^{ax}$, où $C$ est une constante réelle quelconque.
\end{minipage}
}\\
on aurait pu écrire\\
\fbox{\begin{minipage}{\linewidth}
Soit $a$ un réel.\\
$f$ est une solution de l'équation différentielle $y'=ay$ équivaut à $f(x) = C\ex^{ax}$, où $C$ est une constante réelle quelconque.
\end{minipage}
}\\

Or une équivalence est une double implication $A \equivaut B$  signifie $A \Rightarrow B$ et $B \Rightarrow A$.\\
Les démonstrations précédentes ont utilisé ce principe en démontrant :
\begin{itemize}
\item L'implication \\ \fbox{Si  $f(x) = C\ex^{ax}$, où $C$ est une constante réelle quelconque alors $f$ est  une solution de l'équation différentielle $y'=ay$}
\item puis l'implication\\ \fbox{Si $f$ est une solution de l'équation différentielle $y'=ay$ alors $f(x) = C\ex^{ax}$, où $C$ est une constante réelle quelconque}
\end{itemize}

Dans une implication $A \Rightarrow B$, $A$ s'appelle \textbf{la condition suffisante} et $B$ s'appelle \textbf{la condition nécessaire}. En effet, il suffit d'avoir $A$ pour être certain d'avoir $B$. Mais il est nécessaire (en fait il est indispensable) d'avoir $B$ \textit{pour pouvoir espérer} avoir $A$. Une implication $A \Rightarrow B$ et sa contraposée $non(B) \Rightarrow non(A)$ sont équivalentes.

Une équivalence $A \equivaut B$ signifie donc que $A$ est une condition nécessaire ($B \Rightarrow A$) et suffisante ($A \Rightarrow B$).
\end{rque}

-->