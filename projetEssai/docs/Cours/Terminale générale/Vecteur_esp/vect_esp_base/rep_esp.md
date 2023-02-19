# Repères de l'espace

## Repère et base

!!! info "Base de l'espace"
    Une **base de l'espace** est formée d'un triplet de vecteurs $(\vec{i}; \vec{j} ; \vec{k})$ non coplanaires.
    

!!! info "Repère de l'espace"
    Un **repère de l'espace** de l'espace est défini par la donnée d'un point $O$ de l'espace et d'une base $(\vec{i}; \vec{j} ; \vec{k})$ de l'espace. On le note alors $(O;\vec{i}; \vec{j} ; \vec{k})$.

    On considère un repère $(O;\vec{i}; \vec{j} ; \vec{k})$.
    
    Pour tout point $M$ de l'espace, il existe un unique triplet de réels $(x;y;z)$ tel que $\vect{OM} = x \vec{i} + y \vec{j} + z \vec{k}$.
    
    $x,y$ et $z$ sont les coordonnées de $M$ dans le repère $(O;\vec{i}; \vec{j} ; \vec{k})$.
    
    $x$ est **l'abscisse**, $y$ est **l'ordonnée** et $z$ **la cote** de $M$.

Dans ce qui suit, l'espace est rapporté à un repère $(O;\vec{i}; \vec{j} ; \vec{k})$.

## Des formules bien connues

!!! info "Coordonnées d'un vecteur"
    On considère les points $A(x_A;y_A;z_A)$ et $B(x_B;y_B;z_B)$. Les coordonnées du vecteur $\vect{AB}$ sont $(x_B-x_A;y_B-y_A;z_B-z_A)$.

???- abstract "Démonstration"
    Comme $\vect{AB}= \vect{AO} + \vect{OB}=-\vect{OA}+\vect{OB}$.
    
    Par définition, $\vect{OA}=x_A\vect{i}+y_A\vect{j} +z_A\vect{k}$ et $\vect{OB}=x_B\vect{i}+y_B\vect{j} +z_B\vect{k}$, donc :

    $\vect{AB} = -(x_A\vect{i}+y_A\vect{j} +z_A\vect{k})+x_B\vect{i}+y_B\vect{j} +z_B\vect{k}$
    
    Ainsi $\vect{AB} = (x_B-x_A)\vect{i}+(y_B-y_A)\vect{j} +(z_B-z_A)\vect{k}$.

!!! info "coordonnées d'un milieu"
    On considère les points $A(x_A;y_A;z_A)$ et $B(x_B;y_B;z_B)$. Les coordonnées du milieu $I$ de $[AB]$ sont $\left( \dfrac{x_A+x_B}{2} ; \dfrac{y_A+y_B}{2} ; \dfrac{z_A+z_B}{2} \right)$

???- abstract "Démonstration"
    $I$ est le milieu de $[AB]$. Ainsi, $\vect{AI}=\dfrac{1}{2}\vect{AB}$ et donc $\vect{AO}+\vect{OI} = \dfrac{1}{2}\vect{AB}$. Ainsi,

    \begin{eqnarray*}
    \vect{OI} & = & \dfrac{1}{2}\vect{AB} - \vect{AO}\\
    & = & \dfrac{1}{2}\vect{AO}+\dfrac{1}{2}\vect{OB}-\vect{AO}\\
    & = & \dfrac{1}{2}\vect{OA}+\dfrac{1}{2}\vect{OB}\\
    & = & \dfrac{1}{2}(x_A\vect{i}+y_A\vect{j} +z_A\vect{k}) + \dfrac{1}{2}(x_B\vect{i}+y_B\vect{j} +z_B\vect{k})\\
    & =& \dfrac{x_A+x_B}{2}\vect{i}+ \dfrac{y_A+y_B}{2}\vect{j}+ \dfrac{z_A+z_B}{2}\vect{k}
    \end{eqnarray*}

!!! info "Opérations et coordonnées"
    On considère les vecteurs $\vec{u}\left( x_{\vec{u}};y_{\vec{u}};z_{\vec{u}} \right)$ et $\vect{v}\left( x_{\vec{v}};y_{\vec{v}};z_{\vec{v}} \right)$ et $\alpha$ un nombre réel.

    - $\vec{u}+\vec{v}$ a pour coordonnées $\left( x_{\vec{u}}+x_{\vec{v}};y_{\vec{u}}+y_{\vec{v}};z_{\vec{u}}+z_{\vec{v}} \right)$.
    - $\alpha \vec{u}$ a pour coordonnées $\left(\alpha x_{\vec{u}};\alpha y_{\vec{u}};\alpha z_{\vec{u}} \right)$.

???- example "Exemple"
    Dans la base $\left( \V{i}; \V{j}; \V{k} \right)$, on donne les vecteurs $\V{u}=\V{i}+\V{j}+\V{k}$, $\V{v}=-\V{i}+\V{j}$, $\V{w}=\V{i}+\V{k}$.

    1. Déterminer les coordonnées des vecteurs $\V{u},\ \V{v}$ et $\V{w}$.
    2. Montrer que $\V{u}$, $\V{v}$ et $\V{w}$ ne sont pas coplanaires (ils sont linéairement indépendant).

    ???- done "Réponse"
        
        1. On a $\V{u}=(1;1;1)$, $\V{v}=(-1;1;0)$, $\V{w}=(1;0;1)$.
        2. Montrons que les seuls réels $a,b$ et $c$ tels que $a \V{u}+b \V{v}+c \V{w}=\V{0}$ sont $a=b=c=0$.

            \begin{eqnarray*}
            a \V{u}+b \V{v}+c \V{w}=\V{0} & \equivaut & 
            \left\{
            \begin{array}{lcl}
            a-b+c &= & 0\\
            a+b & = & 0\\
            a+c &=& 0
            \end{array}
            \right.\\
            & \equivaut & 
            \left\{
            \begin{array}{lcl}
            a+a-a &= & 0\\
            b & = & -a\\
            c &=& -a
            \end{array}
            \right.\\
            & \equivaut & 
            \left\{
            \begin{array}{lcl}
            a &= & 0\\
            b & = & 0\\
            c &=& 0
            \end{array}
            \right.
            \end{eqnarray*}
            
            Donc $\V{u}$, $\V{v}$ et $\V{w}$ ne sont pas coplanaires.
        
