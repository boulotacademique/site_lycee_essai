# Equation paramétrique d'une droite

Soit $D$  une droite de l'espace passant par $A(x_A,y_A,z_A)$ et de vecteur directeur $\V{u}  (a,b,c)$ .

Un point $M (x,y,z)$ appartient à $D$ \ssi il existe un réel $t$  tel que $\V{AM}=t\V{u}$.

Ce qui s'exprime à l'aide des coordonnées par : 

\[
\left\lbrace\begin{array}{l}
x-x_A=ta\\
y-y_A=tb  \\
z-z_A=tc
\end{array}\right.
\text{ou encore } \left\lbrace\begin{array}{l}
x=x_A+ta\\
y=y_A+tb  \\
z=z_A+tc
\end{array}\right.
\]


!!! info "Equation paramétrique d'une droite"

    Le système d'équations 
    
    \[ 
    \left\lbrace\begin{array}{l}
    x=x_A+a\ t\\
    y=y_A+b\ t  \quad ,(t\in \R ) \\
    z=z_A+c\ t
    \end{array}\right.
    \]

    est une **représentation paramétrique** de la droite $D$ passant par $A(x_A,y_A,z_A)$ et  de vecteur directeur  $\V{u} (a,b,c)$.

    $t$ est le  paramètre de cette représentation paramétrique

!!! danger "Une telle représentation n'est pas unique"

    - Le paramètre $t$ peut-être remplacé par n'importe quelle autre lettre distincte de $x,y,z$.
    - Pour **une représentation paramétrique donnée**, à chaque réel $t$ correspond un unique point $M$ de la droite. Et réciproquement.
    - Il n'y a pas unicité de la représentation paramétrique d'une droite dans l'espace.

???- example "Exemple"
    
    1. Déterminer une représentation paramétrique de la droite $\Delta$ passant par $A(1;0;2)$ et de vecteur directeur $\vectCoEsp{u}{-1}{1}{3}$.
    2. On donne une représentation paramétrique d'une droite $\Delta'$ : 
        $\left\{ \begin{array}{l}
        x=3-2t\\
        y=-2+2t\\
        z=-4+6t
        \end{array}\right.$
    3. Montrer que $\Delta=\Delta'$.

???- example "Exemple"

    1. 
        1. Déterminer une représentation paramétrique de la droite $D$ passant par $A(-2,3,1)$ et $B(5,2,-2)$
        2. Les points $M(-9,4,4)$ et $N(12,1,1)$ appartiennent -ils à cette droite?
    2. Etudier la position de $D$ et $D'$ définies par :

        \[
        (D):\left\lbrace\begin{array}{l}x=1+t\\
        y=-3t+2 \quad ,(t\in \R ) \\
        z=3-3t
        \end{array}\right.
        (D'):\left\lbrace\begin{array}{l}x=t\\
        y=-3-3t \quad ,(t\in \R ) \\
        z=1-t
        \end{array}\right.
        \]

    ???- done "Réponse"

        1. 
            1. La droite(AB) a pour vecteur directeur $\dvec{AB}(7,-1,-3)$
                Une représentation paramétrique de $D$ est :

                \[
                \left\lbrace\begin{array}{l}x=-2+7t
                y=3-t \quad ,(t\in \R ) \\
                z=1-3t
                \end{array}\right.
                \]

            2. Existe-t-il un nombre réel $t$ tel que

                $(D):\left\lbrace\begin{array}{l}
                -2+7t=-9\\
                3-t=4 \quad ,(t\in \R ) \\
                1-3t=4
                \end{array}\right.$ ?

                Ce système équivaut à $t=1$ donc $M \in (AB)$.

                Existe-t-il un nombre réel $t$ tel que
                
                $(D):\left\lbrace\begin{array}{l}
                -2+7t=12\\
                3-t=1 \quad ,(t\in \R ) \\
                1-3t=1
                \end{array}\right.$ ?

                Ce système équivaut à $(D):\left\lbrace\begin{array}{l}
                t=2\\
                t=2 \quad ,(t\in \R ) \\
                t=0
                \end{array}\right.$
                
                Ce système n'a pas de solution, donc $N\not\in(AB)$.

        2. $D$ et $D'$ ont pour vecteurs directeurs $\dvec{u}(1,-3,-3)$ et $\dvec{u'}(1,-3,-1)$. 
        
            Puisque leurs coordonnées ne sont pas proportionnelles, $\V{u}$ et $\V{u'}$ ne sont pas colinéaires.

            Ainsi $D$ et $D'$ sont soit sécantes, soit non coplanaires. 
            
            Précisons leur position en examinant leur intersection
            
            Il s'agit de résoudre le système:

            \[
            \left\lbrace\begin{array}{l}
            t+1=s\\
            -3t+2=-3s-3  \\
            -3t+3=-s+1
            \end{array}\right.
            \]

            \[
            \left\lbrace\begin{array}{l}t-s=1\\
            -3t+3s=-5  \\
            -3t+s=-2
            \end{array}\right.
            \]

            \[
            \left\lbrace\begin{array}{l}t-s=1\\
            t-s=\dfrac53  \\
            -3t+s=-2
            \end{array}\right.
            \]


        Les deux premières équations sont incompatibles et ce système n'admet pas de solution. Donc $D$ et $D'$ ne sont pas sécantes. Elles sont donc sont non coplanaires.

<!--
???- example "Exemple"

    Soit $(\mc{P})$ un plan d'équation cartésienne : $2x-5y+3z-6=0$. Déterminer l'intersection de $(\mc{P})$ avec la droite $(\Delta)$ passant par $A(-1;3;1)$ dirigée par $\dvec{u}(0,-3,2)$.

    ???- done "Réponse"
        Une représentation paramétrique de $(\Delta)$ est :

        \[ 
        \left\lbrace\begin{array}{l}x=-1\\
        y=3-3t \quad ,(t\in \R ) \\
        z=1+2t
        \end{array}\right.
        \]

        Comme $\vectCoEsp{n}{2}{-5}{3}$ n'est pas orthogonale à $\vectCoEsp{u}{0}{-3}{2}$, donc $(\Delta)$ et $(\mc{P})$ sont sécants en un point. Pour le trouver, on 

        \[ 
        \left\{
        \begin{array}{l}
        x=-1\\
        y=3-3t \\
        z=1+2t\\
        2x-5y+3z-6=0
        \end{array}
        \right.
        \]

        On trouve :

        \[ 
        \left\{
        \begin{array}{l}
        x=-1\\
        y=\dfrac{1}{7} \\
        z=\dfrac{61}{21}\\
        t=\dfrac{20}{21}
        \end{array}
        \right.
        \]
-->
<!--
???- example "Exemple"
    Soient $(P)$ : $x-2y-z-8=0$ et $(R)$ : $-5x-2y+2z-11=0$.
    
    1. Montrer que $(P)$ et $(R)$ sont sécants.
    2. Déterminer l'équation paramétrique de la droite d'intersection de $(P)$ et $(R)$.

    ???- done "Reponse"

        1. $\vectCoEsp{n_1}{1}{-2}{-1}$ et  $\vectCoEsp{n_2}{-5}{-2}{2}$ ne sont pas colinéaires. Donc les deux plans ne sont pas parallèles. Ils sont donc sécants en une droite $(d)$.
        2.
            **Méthode 1** Dans le système $\left\{
            \begin{array}{l}
            x-2y-z-8=0\\
            -5x-2y+2z-11=0
            \end{array}
            \right.$, on exprime deux variables en fonction de la troisième (si cela est possible). Ici, on trouve $\left\{
            \begin{array}{l}
            y=\dfrac{-1}{2}x-\dfrac{9}{2}\\
            z=2x+1
            \end{array}
            \right.$. On a alors le paramètre (ici $x$). Donc une équation paramétrique de $(d)$ est :

            \[ 
            \left\{
            \begin{array}{l}
            x=t\\
            y=\dfrac{-1}{2}t-\dfrac{9}{2}\\
            z=2t+1
            \end{array}
            \right.
            \]

            $(\Delta)$ est donc une droite dirigée par $\V{u_1}\left( 1; \dfrac{-1}{2} ; 2 \right)$ passant par $A\left(0; \dfrac{-9}{2} ; 1 \right)$.\\

            **Méthode 2** Un vecteur directeur $\V{u}(\alpha, \beta, \gamma)$ de $(d)$ est normal à $\V{n_1}$ et $\V{n_2}$. on résout :

            \begin{eqnarray*} 
            \left\{
            \begin{array}{l}
            \alpha-2\beta-\gamma = 0 \\
            -5\alpha-2\beta+2\gamma = 0
            \end{array}
            \right.
            & \equivaut & 
            \left\{
            \begin{array}{l}
            \alpha-2\beta-\gamma = 0 \\
            -6\alpha+3\gamma = 0
            \end{array}
            \right.\\
            & \equivaut & 
            \left\{
            \begin{array}{l}
            \beta =\dfrac{-1}{2}\alpha \\
            \gamma = 2\alpha
            \end{array}
            \right.
            \end{eqnarray*}

            On choisit $\alpha=2$ et donc $\V{u}=(2;-1;4)$.
            
            Puis on cherche un point commun à $(P)$ et à $(R)$. Pour cela, on résout :
            \begin{eqnarray*}
            \left\{
            \begin{array}{l}
            x-2y-z-8=0\\
            -5x-2y+2z-11=0
            \end{array}
            \right.
            & \equivaut &
            \left\{
            \begin{array}{l}
            x-2y-z-8=0\\
            -6x+3z-3=0
            \end{array}
            \right.\\
            & \equivaut &
            \left\{
            \begin{array}{l}
            y=\dfrac{-1}{2}x-\dfrac{9}{2}\\
            z=2x+1
            \end{array}
            \right.
            \end{eqnarray*}

            On choisit $x=1$. Donc $B\left(1;-5;3 \right)$.

            Donc, une équation paramétrique de $(d)$ est $\left\{ \begin{array}{l}
            x = 2t +1\\
            y = -t-5 \ , \quad t \in \R\\
            z = 4t+3
            \end{array} \right.$
-->