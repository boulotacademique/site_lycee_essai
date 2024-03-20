# Autour des fonctions polynômiales

## Définition et vocabulaires

!!! info "Définition"
    Une fonction $P$, définie sur $\R$, est une fonction polynôme (ou polynôme) lorsqu'il existe un entier naturel $n$ et des réels $a_0,a_1, \ldots a_n$ tels que, pour tout réel $x$, $P$ s'écrire :
    
    \[ P(x) = a_n x^n + a_{n-1} x^{n-1} + \ldots + a_1 x + a_0 \]
    
    \[ \text{ou} \quad P(x) = \sum_{k=0}^n a_k x^k\]

???- example "Des polynômes bien connus"

    - $\left.  
    \begin{array}{l}
    P_1(x) = 3 \text{ : les fonctions constantes}\\
    P_2(x) = ax+b  \text{ : les fonctions affines}\\
    P_3(x) = x^p \quad \text{avec } p \in \N  \text{ : les fonctions puissances}
    \end{array}
    \right \}$ sont des fonctions polynômes

    - $P(x) =  5x^6+3x^5+2x^3+x^2-1$
    - $Q(x) = 3x(5x^2+2)$ car $Q(x) = 15x^3+6x$

!!! info "Vocabulaire :"
    Soit $P(x) = a_n x^n + a_{n-1} x^{n-1} + \ldots + a_1 x + a_0$ avec $a_n \neq 0$.

    - L'entier $n$ est appelé degré de $P$ (on écrit $n = deg(P)$).  
    Dans l'exemple précédent, $Q$ est de degré $3$.
    - Les réels $a_n,a_{n-1}, \ldots , a_0$ sont les coefficients de $P$. $a_n$ (par exemple) est le coefficient de degré $n$.
    - $a_3 x^3$ (par exemple) est le terme en $x^3$ ou le terme de degré $3$. **Cas particulier :** $a_0$, qui est le terme de degré $0$, est plutôt appelé le terme constant et $a_n x^n$ est le terme de plus haut degré.
    - On appelle racine ou zéro de $P$, tout réel $\alpha$ tel que $P(\alpha) = 0$.
    - Si pour tout $x$ réel $P(x) = 0$, on note $P=0$ et s'appelle le polynôme nul. Par convention, le polynôme nul n'a pas de degré mais n'importe quel polynôme a un degré supérieur à celui du polynôme nul (par convention, le polynôme a pour degré $-\infty$).

!!! info "Unicité de l'écriture polynomiale"
    - $P=0$ équivaut à tous les coefficients de $P$ sont nuls
    - Soient $P$ et $Q$ deux polynômes tels  
        
        \[ P(x) = \sum_{k = 0}^n a_k x^k \text{ et } Q(x) = \sum_{k = 0}^p b_k x^k \]  

        $\forall x \in \R P(x) = Q(x)$ $\iff$ $n=p$ et pour tout $k$ entier compris entre $0$ et $n$, $a_k = b_k$  
        Cela signifie que des polynomes sont égaux si et seulement si ils ont le même degré et les mêmes coefficients.

    Grâce à ce théorème, on pourra utiliser la méthode appelée **par identification**.

!!! info "Théorème sur les degrés"

    Soit $P$ et $Q$ deux polynômes tel que $deg(P) = n$ et $deg(Q) = p$.
    
    - $deg(P \times Q) = deg(P) + deg(Q)$
    - $deg(P + Q) \leq max( deg(P) ; deg(Q))$. Mais si $deg(P) \neq deg(Q)$, alors $deg(P + Q) = max( deg(P) ; deg(Q))$
    - $deg( P \circ Q) = deg(P) \times deg(Q)$

!!! info "Degré et nombre de racines"

    - Soit $P \neq 0$ un polynôme de degré $n$, alors $P$ possède au plus $n$ racines.
    - Soit $P$ un polynôme de degré $n$. Si $P$ possède plus de $n+1$ racines, alors $P = 0$.

## Technique à maîtriser

???- tip "Notation sigma"

    Il est souvent pratique d'écrire un polynôme à l'aide du symbole $\sum$. Par exemple, pour un polynôme de degré $n$ on a

    \[ P(x) = \sum_{k = 0}^n a_k x^k \]

    Par exemple, la dérivation d'une somme se fait terme à terme. Avec cette notation, il est alors immédiat que 

    \[ P'(x) = \sum_{k = 0}^n a_k \times k x^{k-1}  = \sum_{k = 1}^n a_k \times k x^{k-1} \]

    Avec la notation $\sum$, il est possible de modifier la variable muette $k$.  
    Par exemple dans le polynôme dérivé, on peut noter $j = k - 1$ (i.e. $k = j + 1$) et alors :

    \[ P'(x)  = \sum_{k = 1}^n a_k \times k x^{k-1} = \sum_{j = 0}^{n-1} a_{j+1} \times (j + 1) x^{j} \]

???- tip "Produit de 2 polynômes"
    Voici une présentation pour simplifier le produit de 2 polynômes.

    [![Produit de deux polynômes](../Image/Produit_polynome.gif){.Center_lien .Vignette40}](../Image/Produit_polynome.png){:target="_blank"}

    Cette méthode permet d'obtenir des lignes avec des puissances décroissantes.

???- tip "Cas particulier : produit d'un polynôme avecun polynôme de degré 1"

    Voici un exemple de la méthode qui consiste à faire les calculs de façon à obtenir &laquo; ensemble &raquo; des termes de même puissance. Cette approche est particulièrement adaptée au produit de polynômes, avec un facteur de degré 1.

    [![Produit de deux polynômes01](../Image/Produit_polynome01.gif){.Center_lien .Vignette40}](../Image/Produit_polynome01.png){:target="_blank"}

???- tip "Méthode par identification"
    En raison de l'unicité d'écriture d'un polynôme, il est possible (par exemple) de factoriser un polynôme.

    [![Par identification](../Image/polynome03.gif){.Center_lien .Vignette40}](../Image/polynome03.png){:target="_blank"}

???- tip "Méthode par identification : cas d'un polynome de degré 1"
    Avec un polynôme de degré 1, il est possible de faire les calculs de tête :

    [![Par identification](../Image/polynome02b.gif){.Center_lien .Vignette40}](../Image/polynome02b.png){:target="_blank"}

