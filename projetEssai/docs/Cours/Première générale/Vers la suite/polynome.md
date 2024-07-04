# Polynômes.

## Définitions.

!!! note "Définition"
    Une fonction $P$, **définie sur $\R$**, est une fonction polynôme (ou polynôme) lorsqu'il existe un entier naturel $n$ et des réels $a_0,a_1, \ldots a_n$ tels que, pour tout réel $x$, $P$ s'écrire :

    \[ P(x) = a_n x^n + a_{n-1} x^{n-1} + \ldots + a_1 x + a_0 \]

    \[ \text{ou} \quad P(x) = \sum_{k=0}^n a_k x^k\]


???- example "Exemple"
    
    - Polynômes particuliers :  
    $\left.  
    \begin{array}{l}
    P_1(x) = 3 \text{ : les fonctions constantes}\\
    P_2(x) = ax+b  \text{ : les fonctions affines}\\
    P_3(x) = x^p \quad \text{avec } p \in \N  \text{ : les fonctions puissances}
    \end{array}
    \right\}$ sont des polynômes
    - $P(x) =  5x^6+3x^5+2x^3+x^2-1$
    - $Q(x) = 3x(5x^2+2)$ car $Q(x) = 15x^3+6x$

???- example "Exercice"

    1. Montrer que $f(x)=\frac{x^4-1}{x^2+1}$ est un polynôme.  
    2. Est-ce-que $h(x)=\frac{(x-3)\left( x^2 -81 \right)}{x+9}$ est un polynôme ?
    

!!! note "Vocabulaire"
    Soit $P(x) = a_n x^n + a_{n-1} x^{n-1} + \ldots + a_1 x + a_0$ avec $a_n \neq 0$.

    - L'entier $n$ est appelé degré de $P$ (on écrit $n = deg(P)$).  
    Dans l'exemple, $Q$ est de degré $3$.
    - Les réels $a_n,a_{n-1}, \ldots , a_0$ sont les coefficients de $P$. $a_n$ (par exemple) est le coefficient de degré $n$.
    - $a_3 x^3$ (par exemple) est le terme en $x^3$ ou le terme de degré $3$.  
      - \underline{Cas particulier :} $a_0$, qui est le terme de degré $0$, est plutét appelé le terme constant - et $a_n x^n$ est le terme de plus haut degré.
    - On appelle racine ou zéro de $P$, tout réel $\alpha$ tel que $P(\alpha) = 0$.

!!! note "Notation :"
    Si pour tout $x$ réel $P(x) = 0$, on note $P=0$ et s'appelle le polynôme nul. Par convention, le polynôme nul a pour degré $-\infty$. Et donc n'importe quel polynôme a un degré supérieur à celui du polynôme nul. Le polynôme nul est le seul polynôme possédant une infinité de zéros.

## Unicité de l'écriture polynomiale.

!!! note "Théorème"
    Dire qu'un polynôme est nul équivaut à dire que tous ses coefficients sont nuls.

???- abstract "Démonstration sur un cas particulier"
    Soit $P(x) = ax^3 +bx^2 +cx + d $
    
    $\Leftarrow$ Si $a=b=c=d=0$, alors pour tout $x$, $P(x)=0$, donc $P=0$.

    $\Rightarrow$ Si $P=0$, alors pour tout réel $P(x)=0$. En particulier :

    - $P(0) = 0$ donc $d=0$
    - $P(1) = 0$ donc $a+b+c=0$
    - $P(-1) = 0$ donc $-a+b-c=0$
    - $P(2) = 0$ donc $8a+4b+2c=0$

    \[\begin{eqnarray*}
    \left \{ \begin{array}{rcl} a+b+c &=&0 \\ -a+b-c & = & 0 \\ 8a+4b+2c & = & 0 \end{array} \right. & \Leftrightarrow & \left \{ \begin{array}{rcl} b &=&0 \\ a+c & = & 0 \\ 8a+2c & = & 0 \end{array}  \right. \\
    & \Leftrightarrow & \left \{ \begin{array}{rcl} b &=&0 \\ a & = & -c \\ -6c & = & 0 \end{array}  \right. \\
    & \Leftrightarrow & \left \{ \begin{array}{rcl} b &=&0 \\ a & = & 0 \\ c & = & 0 \end{array}  \right.    
    \end{eqnarray*}\]
    
    Donc $a=b=c=d=0$.

!!! absrtact "Théorème"
    Deux polynômes non nul sont égaux si et seulement si ces polynômes ont le même degré et si les coefficients des termes de même degré sont égaux.


!!! abstract "Corollaire"
    Tout polynôme non nul $P$ admet une unique écriture sous la forme $P(x)  = a_n x^n + a_{n-1} x^{n-1} + \ldots + a_1 x + a_0$, avec $a_n \neq 0$.

???- tip "Méthode : par Identification"
    Soit $P(x) = x^3+5x^2-3x-15$.
    
    Déterminer les réels $a,b$ et $c$ tel que, pour tout réel $x$, on ait :
    
    \[ P(x) = (x+5) \left( ax^2+bx+c \right) \]
    
    En déduire les racines de $P$.

    ???- tip "Solution"
        $(x+5) \left( ax^2+bx+c \right) = ax^3 + (5a+b)x^2+(5b+c)x + 5c$ et en identifiant (i.e. en comparant les coefficients des termes de même degré) le second membre avec $x^3+5x^2-3x-15$, on trouve que $a=1 \ b =0 \ c = -3$.
        
        Donc $P(x) = (x+5)\left( x^2-3 \right)$ et $S = \left\{-5 ; - \sqrt{3} ; \sqrt{3} \right\}$.  
