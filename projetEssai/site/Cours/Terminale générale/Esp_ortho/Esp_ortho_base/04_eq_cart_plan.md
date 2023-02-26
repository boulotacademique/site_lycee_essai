# Equation cartésienne du plan

!!! info "Rappel"
    Un plan peut être déterminé par : 

    - Trois points A,B,C non alignés.
    - Deux droites sécantes (c’est à dire un point et deux vecteurs non colinéaires)
    - Deux droites strictement parallèles.

!!! info "Equation cartésienne d'un plan"
    Dans un repère orthonormal
    
    - Un plan $P$ de vecteur  normal $\V{n}(a,b,c)$ a <span id="eq_cartesienne_plan">**une équation cartésienne**</span> de la forme $ax+by+cz+d=0$ où  $d$ est un réel. 
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
        Soient $H(x_H;y_H;z_H)$ le projeté orthogonal de $A$ sur $\mc{P}$ et $\V{n}(1;-3;2)$ un vecteur normal à $\mc{P}$.

        - $H$ est un point de $\mc{P}$ donc $x_H-3y_H+2z_H-4=0$
        - $H$ est sur la droite $(AH)$ passant par $A$ et dirigée par $\V{n}$. Ainsi, une représentation paramétrique de cette droite $(AH)$ est 

        \[
            \left\lbrace
            \begin{array}{lr}
            x = -1 + t\\
            y = 3 -3t\ ,\qquad t\in \R \\
            z = 2+ 2t
            \end{array}
            \right.
        \]

        Comme $H$ est cette droite et sur le plan $\mc{P}$,

        \[
            \left\lbrace
            \begin{array}{lr}
            x_H = -1 + t\\
            y_H = 3 -3t\ ,\qquad \text{ pour un } t \in \R \\
            z_H = 2+ 2t
            x_H-3y_H+2z_H-4=0
            \end{array}
            \right.
        \]

        On résout $t-1-3(-3t+3)+2(2t+2)-4=0$. On trouve $t = \dfrac{5}{7}$. D'où :

        \[
            \left\{
            \begin{array}{l}
            x_H  =  -\dfrac{2}{7}\\
            y_H  =  \dfrac{6}{7}\\
            \rule[-0.5cm]{0pt}{1.2cm}z_H  =  \dfrac{24}{7}
            \end{array}
            \right.
        \]

        Donc, d'après le théorème, la distance entre $A$ et $\mc{P}$ est la longueur $AH = \sqrt{}AH=\sqrt{\left( -\dfrac{2}{7} +1\right)^2 + \left( \dfrac{6}{7} -3\right)^2+\left( \dfrac{24}{7} -2\right)^2}=\sqrt{\dfrac{50}{7}}=5\dfrac{\sqrt{14}}{7}$.

!!! info "Distance point-droite"
    Soit $(d)$ une droite de l'espace et $A$ un point. La **distance du point $\mathbf{A}$ à la droite $\mathbf{(d)}$**, notée $d(A, d)$, est la plus petite des longueurs $AM$ où $M \in (d)$.

!!! tip "Comment calculer cette distance ?"
    Si on note $H$ le projeté orthogonal de $A$ sur la droite $(\Delta)$, alors $d(A, \Delta)=AH$.

???- example "Exemple"
    On se place dans un repère orthonormé.
    
    Soit $(d)$ la droite passant par $I(1;0;-1)$ et dirigée par $\V{u}(2;-1;1)$. Déterminer la distance entre $A(2;-1;2)$ et la droite $(d)$.

    ???- done "Réponse"
        Notons $H$ le projeté orthogonal de $A$ sur $(d)$.
        
        Et soit $(P)$ le plan passant par $A$ et ayant pour vecteur normal $\V{u}(2;-1;1)$. Donc $\mc{P}$ a pour équation cartésienne $2(x-2)-(y+1)+(z-2)=0$, c'est-à-dire $2x-y+z-7=0$. Or $H$ appartient à ce plan $\mc{P}$. Donc $2x_H-y_H+z_H-7=0$.

        $H$ est un point de $(d)$ qui a pour équation paramétrique $\left\lbrace \begin{array}{lr} x = 1 + 2t\\ y=-t \ \quad t \in \R\\ z = -1+t \end{array}\right.$

        Les coordonnées de $H$ vérifient : $\left\{\begin{array}{l} 2x_H-y_H+z_H-7=0 \\ x_H  =  1 + 2t\\ y_H  =  -t \\ z_H   = -1 + t \end{array} \right.$.

        On résout : $2(2t+1)-(-t)+(t-1)-7=0$. On trouve $t = 1$. D'où :

        \[
            \left\{
            \begin{array}{l}
            x_H  =  3\\
            y_H  =  -1 \\
            z_H  =  0
            \end{array}
            \right.
        \]

        Or d'après le théorème précédent, la distance entre $A$ et la droite $(d)$ est la longueur $AH$.

        Donc $d(A, d)= \displaystyle\sqrt{\left( 3-2\right)^2+\left( -1+1\right)^2+\left( 0-2\right)^2} = \sqrt{5}$.


