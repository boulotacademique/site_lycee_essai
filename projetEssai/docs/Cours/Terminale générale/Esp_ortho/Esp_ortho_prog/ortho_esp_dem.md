# Démonstration au programme

!!! info "Equation cartésienne d'un plan"
    Dans un repère orthonormal
    
    - Un plan $P$ de vecteur  normal $\V{n}(a,b,c)$ a une équation cartésienne de la forme $ax+by+cz+d=0$ où  $d$ est un réel. 
    - Réciproquement : l'ensemble des points $M(x,y,z)$ tels que $ax+by+cz+d=0$  avec $(a,b,c)\neq(0,0,0)$ est un plan qui a pour vecteur normal est $\V{n}(a,b,c)$.

???- abstract "Démonstration"
    - Soit  $\mathcal{P}$ passant par $A(x_0 ;y_0 ;z_0)$ et de vecteur normal $\V{n}(a,b,c)$
    
    \begin{eqnarray*}
    M(x,y,z) \in \mathcal{P} & \iff & \V{AM}\cdot \dvec{n} =0 \\
        & \iff & a(x-x_0)+b(y-y_0)+c(z-z_0)=0\\
        & \iff & ax+by+cz -ax_0-by_0-cz_0=0\\
        & \iff & ax+by+cz+d=0 \text{ en posant } d = -(ax_0+by_0+cz_0)
    \end{eqnarray*}

    - Comme $(a,b,c)\neq(0,0,0)$ , il existe un triplet $(x_0 ; y_0 ; z_0)$ tel que $ax_0 + by_0 + cy_0 +d =0$ donc $d= -ax_0-by_0-cz_0$
    
    Soit $M(x,y,z)$ : 
    
    \begin{eqnarray*}
    ax+b y + cz+ d =0 & \iff & ax + by + cz -ax_0-by_0-cz_0=0 \\
        & \iff & a(x-x_0) + b(y-y_0) + c(z -z_0)=0\\
        & \iff & \V{AM}\cdot \V{n}=0
    \end{eqnarray*}

    en posant $A(x_0 ;y_0 ;z_0)$ et $ \V{n}(a,b,c)$.
    
    Donc l'ensemble des points  $M(x , y ,z)$ tels que $a x +b y + c z + d = 0$ où a, b ,c sont des réels non tous nuls ,  est le plan passant par $A$ et de vecteur normal $\V{n}$.

!!! info "Distance point-plan"
    Soient $\mc{P}$ un plan de l'espace et $A$ un point.
    La **distance du point A au plan** $\mathbf{\mc{P}}$, notée $d(A, \mc{P})$, est la plus petite des longueurs $AM$ où $M \in \mc{P}$.

!!! info "Comment calculer cette distance ?"
    Si on note $H$ le projeté orthogonal de $A$ sur le plan $\mc{P}$, alors $d(A, \mc{P}) = AH$.

???- abstract "Démonstration"
    Pour tout $M \neq H$, le triangle $AHM$ est rectangle en $H$, donc $AM>AH$. Ainsi, $AH$ est bien la plus petite des longueurs et $d(A, \mc{P}) = AH$. (Faire un dessin)