# Equation cartésienne du plan

!!! info "Rappel"
    Un plan peut être déterminé par : 

    - Trois points A,B,C non alignés.
    - Deux droites sécantes (c’est à dire un point et deux vecteurs non colinéaires)
    - Deux droites strictement parallèles.

!!! info "Equation cartésienne d'un plan"
    Dans un repère orthonormal
    
    - Un plan $P$ de vecteur  normal $\V{n}(a,b,c)$ a une équation cartésienne de la forme $ax+by+cz+d=0$ où  $d$ est un réel. 
    - Réciproquement : l'ensemble des points $M(x,y,z)$ tels que $ax+by+cz+d=0$  avec $(a,b,c)\neq(0,0,0)$ est un plan qui a pour vecteur normal est $\V{n}(a,b,c)$.

???- tip "Equation de plans particuliers"

    - Le plan $(x O y)$  a pour équation cartésienne $z=0$.
    - Le plan $(xOz)$ a pour équation cartésienne $y=0$.
    - Le plan $(yOz)$ a pour équation cartésienne $x=0$.

???- example "Exemple"
    Chercher une équation du plan  $P$  de vecteur normal  $\V{n}(3,-2,1)$ et qui passe par le point $A(-1,2,-3)$.

    ???- done "Réponse"
        Une équation du  plan est $3x-2y+z+d=0$.
        
        Comme le plan passe par $A$ les coordonnées de $A$ vérifient l'équation du plan et on a : $-3-4 -3+d=0$ d'où $d= 10$. 
        
        **Une équation de $P$ est $3x-2y+z+10=0$**
 
        ???-tip "Autre méthode" 
            On peut aussi écrire que $\V{AM}\cdot \V{n}=0$ ...



???- example "Exemple"
    Dans un repère orthonormal de l'espace on donne les trois points  $A(0,1,-1) , B(2,1,-2)$ et $C(1,0,-2)$.

    1. Démontrer que ces trois points déterminent un plan 
    2. Déterminer un vecteur $\V{n}$ normal du plan (ABC)
    3. Déterminer une équation du plan (ABC)

    ???- done "Réponse"

        <ol>
        <li>Les trois points sont non alignés car $\V{AB} (2,0,-1)$et $\V{AC}  (1,-1,-1)$  sont non colinéaires. Donc ils déterminent un plan.</li>
        <li>On cherche $\V{n}(x,y,z)$ tel que $\V{n}\cdot \V{AB}=0$ et $\V{n}\cdot \V{AC}=0$ \cad on cherche $x,y,z$ tels que

        \[
            \left\lbrace
            \begin{array}{l}
            2x-z=0   \\
            x-y-z=0   
            \end{array}
            \right.
        \]

           En posant $x=1$ , on a $y=-1$ et $z=2$.

           Un vecteur normal au plan (ABC) est $\V{n}(1,-1,2)$.</li>
        <li>Une équation de (ABC) est $x-y+2z+d=0$  or $A \in (ABC)$ donc $d=+3$ ;
        
        Une équation de $(ABC)$ est : $x-y+2z+3=0$.</li>
        </ol>

???- example "Exemple"
    On considère le plan $\mc{P}$ d'équation $3x+y-z-2=0$.
    
    Déterminer les coordonnées du projeté orthogonal du point $A(5;1;3)$ sur le plan $\mc{P}$.

## Distance d'un point à une droite ou à un plan

!!! info "Distance point-plan"
    Soient $\mc{P}$ un plan de l'espace et $A$ un point.
    La **distance du point A au plan** $\mathbf{\mc{P}}$, notée $d(A, \mc{P})$, est la plus petite des longueurs $AM$ où $M \in \mc{P}$.

!!! info "Comment calculer cette distance ?"
    Si on note $H$ le projeté orthogonal de $A$ sur le plan $\mc{P}$, alors $d(A, \mc{P}) = AH$.

???- example "Exemple"
    On se place dans un repère orthonormé.

    Déterminer la distance entre $A(-1;3;2)$ et $\mc{P}$ : $x-3y+2z-4=0$.

    ???- done "Réponse"