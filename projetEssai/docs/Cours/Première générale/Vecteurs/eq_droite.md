# Vecteurs<br>Équations cartésiennes d'une droite

## Vecteurs directeurs

!!! info "Définition"
    On appelle **vecteur directeur** $\vec{u}$ d'une droite $\mc{D}$ tout vecteur non nul, colinéaire au vecteur $\vect{AB}$ où $A$ et $B$ sont deux points distincts de $\mc{D}$. On dit alors que $\vec{u}$ dirige $\mc{D}$


!!! info "Remarques - Conséquences"

    - La direction d'un vecteur directeur de $\mc{D}$ définit la direction de la droite $\mc{D}$.
    - Deux vecteurs directeurs d'une même droite $\mc{D}$ sont donc non nuls et colinéaires : ils ont la même direction.
    - On peut définir une droite $\mc{D}$ par la donnée d'un point $A$ et d'un vecteur directeur $\vec{u}$ :

    \[ M \in \mc{D} \Leftrightarrow \vect{AM} \text{ et } \vec{u} \text{ sont colinéaires} \]


## Équations cartésienne d'une droite

!!! abstract "Théorème"
    Les coordonnées de tous les points $M$ d'une droite $\mc{D}$ vérifient une équation de la forme :
    
    \[ ax +by+ c =0 \]
    
    où $a,b$ et $c$ sont des réels avec $(a;b) \neq (0;0)$.

    Une telle équation s'appelle une équation cartésienne de $\mc{D}$.

???- abstract "Démonstration"
    Soir une droite $\mc{D}$ passant par un point $A(x_A;y_A)$ et de vecteur directeur (non nul) $\vecCo{u}{\alpha}{\beta}$. Pour tout point $M(x;y)$ du plan,

    \[ \begin{eqnarray*}
    M \in \mc{D} & \Leftrightarrow & \vectCo{AM}{x-x_A}{y-y_A} \text{ et } \vecCo{u}{\alpha}{\beta} \text{ sont colinéaires}\\
    & \Leftrightarrow & \beta \times(x-x_A)-\alpha \times (y-y_A) =0\\
    & \Leftrightarrow & \beta x - \alpha y + (-\beta x_A+\alpha y_A) = 0 \text{ et } (\beta;\alpha)\neq (0;0) \text{ car } \vec{u} \neq \vec{0}
    \end{eqnarray*} \]

!!! info "Remarques"
    Une droite $\mc{D}$ admet une infinité d'équations cartésiennes, dont les coefficients sont deux à deux proportionnels.

!!! abstract "Théorème"
    Soit $a,b,c$ avec $(a;b) \neq (0;0)$.

    L'ensemble des points $M(x;y)$ vérifiant $ax+by+c=0$ est une droite de vecteur directeur $\vecCo{u}{-b}{a}$.

???- abstract "Démonstration"
    Soit $A(x_A;yA)$ un point dont les coordonnées sont solutions de $ax+by+c=0$. Un tel point existe car $(a;b) \neq (0;0)$. On choisit alors $x_A=\dfrac{-c-by_A}{a}$ (si $a\neq 0$) ou $y_A=\dfrac{-c-ax_A}{b}$, sinon.

    Pour tout point $M(x;y)$ vérifiant $ax+by+c=0$, $\vect{AM}$ et $\vecCo{u}{-b}{a}$ sont colinéaires. En effet, $\vectCo{AM}{x - x_A}{y - y_A}$ et :

    \[ \begin{eqnarray*}
    (x - x_A) \times a - (-b) \times (y - y_A) & = & ax + by - (a x_A + b y_A) \\
    & = & ax+by +c\\
    & = & 0
    \end{eqnarray*}
    \]

    En effet, comme $A(x_A;yA)$ un point dont les coordonnées sont solutions de $ax+by+c=0$, $ax_A + by_A +c = 0$. Donc $c = -(a x_A + b y_A)$.

    Ainsi, l'ensemble des points $M(x;y)$ vérifiant $ax+by+c=0$ est une droite de vecteur directeur $\vecCo{u}{-b}{a}$ ( passant par $A$)

!!! abstract "Théorème"
    Récipoquement, si une droite $(d)$ est dirigée par $\vecCo{u}{\alpha}{\beta}$, alors une équation cartésienne de $(d)$ est $\beta x - \alpha y + c = 0$ (avec $c$ à déterminer à l'aide d'un point de $(d)$).

???- abstract "Démonstration"
    Soit $M(x;y)$ un point de $(d)$ :

    \[ \begin{eqnarray*}
    M(x;y) \in (d) & \iff & \vectCo{AM}{x - x_A}{y - y_A} \text{ et } \vecCo{u}{\alpha}{\beta} \text{ sont colinéaires} \\
    & \iff & (x-x_A) \times \beta - (y-y_A) \times alpha = 0 \\
    & \iff & \beta x - \alpha y + (\alpha \times y_A - \beta x_A) = 0\\
    & \iff & \beta x - \alpha y + c = 0 \text{ avec } c = (\alpha \times y_A - \beta x_A)\\
        \end{eqnarray*} \]

!!! tip "Méthode"
    En pratique, c'est la méthode de la démonstration qui permet de déterminer une équation cartésienne d'une droite déterminée par un point et un vecteur directeur.

!!! abstract "Théorème"
    Les droites $\mc{D}$ et $\mc{D'}$ d'équations respectives 

    \[ ax+by+c=0 \text{ et } a'x+b'y+c'=0 \]

    sont parallèles si et seulement si $(a;b)$ et $(a';b')$ sont proportionnels (i.e. $a \times b' - b \times a' = 0$).

???- abstract "Démonstration"
    
    \[ \begin{eqnarray*}
    \mc{D} \text{ et } \mc{D'} \text{ sont parallèles} & \iff & \mc{D} \text{ et } \mc{D'} \text{ont la même direction}\\
    & \iff & \text{un vecteur directeur de } \mc{D} \text{ et un vecteur directeur de } \mc{D'} sont colinéaires\\
    & \iff & \vecCo{u}{-b}{a} \text{ et } \vecCo{u'}{-b'}{a'} \text{ sont colinéaires}\\
    & \iff & -b \times a' - a \times (-b') = 0\\
    & \iff & a \times b' - b \times (a') = 0
    \end{eqnarray*}
    \]

## Equation réduite d'une droite

Soit $\mc{D}$ la droite d'équation $ax+by+c = 0$.

- Si $b \neq 0$, alors $ax +by +c = 0 \iff y = \dfrac{-b}{a}x + \dfrac{-c}{a}$ : on reconnait une expression affine $y = mx + p$.
- Si $b = 0$ (alors $a \neq 0$), alors $ax +c = 0 \iff x =  \dfrac{-c}{a}$

!!! abstract "Théorème et vocabulaire"
    Soit $(d)$ une droite d'équation cartésienne $ax +by $c =0$ avec $(a;b) \neq (0;0)$, alors $(d)$ possède une **unique équation réduite** selon la valeur de $b$.

    - Si $b \neq 0$, alors l'équation réduite de $(d)$ est de la forme $y = mx +p$ (avec $m =\dfrac{-b}{a}$ et $p = \dfrac{-c}{a}$)
    - Si $b = 0$, alors l'équation réduite de $d$ est de la forme $x = k$ où $k$ est une constante (avec $k = \dfrac{-c}{a})

!!! abstract "Théorème"
    Une équation réduite d'une droite est unique !

Si une droite $(d)$ a pour équation réduite $y=mx +p$, alors *une* équation cartésienne est $mx -y + p = 0$. Ainsi, un vecteur directeur de $(d)$ est $\vecCo{u}{1}{m}$. On remarque alors que, si $m = 0$, $(d)$ est parallèle à l'axe des abscisses (pour rappel $\vecCo{i}{1}{0}$).

Si une droite $(d)$ a pour équation réduite $x = k$, alors *une* équation cartésienne est $x - k = 0$. Ainsi, un vecteur directeur de $(d)$ est $\vecCo{u}{0}{1} = \vec{j}$. Dans ce cas, $(d)$ est parallèle à l'axe des ordonnées.

!!! abstract "Théorème"
    
    - $\vecCo{u}{1}{m}$ est un vecteur directeur de la droite $(d)$ d'équation réduite $y = mx +p$. Si de plus $m = 0$, alors $(d)$ est parallèle à l'axe des abscisses ( ou &laquo; horizontale &raquo;).
    - $\vecCo{u}{0}{1}$ est un vecteur directeur de la droite $(d)$ d'équation réduite $x = k$. C'est **toujours** une droite parallèle à l'axe des ordonnées ( ou &laquo; verticale &raquo;).

En utilisant le [théorème sur le parallélisme](./colinearite.md#col_par), on retrouve :

!!! abstract "Théorème"
    - $(d)$ une droite d'équation réduite $y=mx +p$ et $(d')$ une droite d'équation réduite $y=m' x + p'$. $(d)$ et $(d')$ sont parallèles (ou confondues) si et seulement si $m = m'$.
    - $(d)$ une droite d'équation réduite $y=mx +p$ et $(d')$ une droite d'équation réduite $x = k$. $(d)$ et $(d')$ sont **toujours sécants** (en $A(k; mk+p)$).
    - $(d)$ une droite d'équation réduite $x = k'$ et $(d')$ une droite d'équation réduite $x = k$. $(d)$ et $(d')$ sont **toujours parallèles** (ou confondues).