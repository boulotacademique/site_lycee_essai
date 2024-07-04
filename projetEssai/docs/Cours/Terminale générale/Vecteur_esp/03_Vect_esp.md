# Vecteur de l'espace

## Définition

!!! info "Définition d'un vecteur de l'espace"
    Soient $A$ et $B$ deux points de l'espace, la transformation qui à tout point $M$ de l'espace associe l'unique point $M'$ tel que $AM'M$ soit un parallélogramme s'appelle **la translation de vecteur** $\mathbf{AB}$.
    
    Comme, dans le plan, les vecteurs $\vect{AB}$ et $\vect{MM'}$ sont égaux et on dit également qu'ils sont deux **représentants** d'un vecteur noté $\vect{u}$.

!!! tip "Caractérisation d'un vecteur"
    Un **vecteur** $\dvec{u}= \dvec{AB}$ est caractérisé par :

    - sa _direction_ : celle de la droite$(AB)$
    - son _sens_ : celui de A vers B 
    - sa _norme_ (notée $||\vect{u}|| =||\vect{AB}||$) : la distance $AB$. Donc $||\vect{AB}||=AB$

!!! info ""
    Deux vecteurs non nuls $\vect{AB}$ et $\vect{CD}$ sont égaux si et seulement si **ABDC** (attention à l'ordre !) est un parallélogramme(éventuellement aplati)

## Opérations sur les vecteurs

### Colinéarité

Les opérations et propriétés vues pour les vecteurs du plan (addition, multiplication par un réel, relation de Chasles , colinéarité $\cdots$) restent valables pour les vecteurs de l'espace.

!!! info "Colinéaires"
    Deux vecteurs non nuls $\dvec{u}$ et $\dvec{v}$ de l'espace sont colinéaires signifie qu'il existe un nombre réel $k$ tel que $\dvec{v}=k\dvec{u}$.
    
    Par convention, le vecteur nul est colinéaire à tous les vecteurs.

!!! info "Théorème"
    - Trois points $A$, $B$ et $C$ sont alignés si et seulement si les vecteurs $\V{AB}$ et $\V{AC}$ sont colinéaires.
    - Deux droites $(AB)$ et $(CD)$ sont parallèles si et seulement si les vecteurs $\V{AB}$ et $\V{CD}$ sont colinéaires.
    - Soit A et B deux points distincts.
        Un point $M$ appartient à la droite (AB) si et seulement si il existe un réel $t$ tel que $\dvec{AM}=t\dvec{AB}$.

???+ example "Exemple"
    On considère un tétraèdre $ABCD$.
    
    On appelle $I,J,K,L$ les points définis respectivement par :
    
    $\dvec{AI}=\dfrac23 \dvec{AB}$, $\dvec{BJ}=\dfrac13 \dvec{BC}$,   $\dvec{CK}=\dfrac23 \dvec{CD}$,    $\dvec{DL}=\dfrac13 \dvec{DA}$.

    1. Placer $I,J,K$ et $L$ sur le dessin 
    2. Exprimer $\dvec{IJ}$ en fonction de $\dvec{AB} $ et $\dvec{BC}$ , puis démontrer que les vecteurs $\dvec{IJ}$ et $\dvec{AC}$ sont colinéaires.
    3. Démontrer que les vecteurs $\dvec{LK}$ et $\dvec{AC}$ sont colinéaires .
        Justifier que les points $I,J,K,L$ sont coplanaires et que la droite $(AC)$ est parallèle au plan $(IJK)$.
    4. Démontrer que la droite $(BD)$ est parallèle au plan $(IJK)$.

    ???+ done "Réponse"

        1. 
        2. 
        \begin{eqnarray*}
        \vect{IJ} & = & \vect{IA}+\vect{AB} +\vect{BJ}\\
        & = & -\dfrac{2}{3} \vect{AB} + \vect{AB} + \dfrac{1}{3}\vect{BC} \\
        & = & \dfrac{1}{3} \vect{AB} + \dfrac{1}{3} \vect{BC}
        \end{eqnarray*}
        3. Comme $\vect{AB}+\vect{BC} = \vect{AC}$, $\vect{IJ} = \dfrac{1}{3} \vect{AC}$.
            Donc $\vect{IJ}$ et $\vect{AC}$ sont colinéaires.

            \begin{eqnarray*}
            \vect{LK} & = & \vect{LD} + \vect{DC}+\vect{CK}\\
            & = & -\dfrac{1}{3}\vect{DA} + \vect{DC} + \dfrac{2}{3} \vect{CD} \\
            & = & \dfrac{1}{3}\vect{AD}+\dfrac{1}{3}\vect{DC}\\
            & = & \dfrac{1}{3}\vect{AC}
            \end{eqnarray*}

            Ainsi $\vect{LK}$ et $\vect{AC}$ sont colinéaires.

            $\vect{IJ}$ et $\vect{LK}$ sont colinéaires, car colinéaires à $\vect{AC}$. Donc les points $I,J,L,K$ sont coplanaires.

        4. Plusieurs méthodes possibles (comme Thalès, le théorème du toit). Dont :

            \begin{eqnarray*}
            \vect{JK} & = & \vect{JB} + \vect{BC}+\vect{CK}\\
            & = & -\dfrac{1}{3}\vect{BC}+\vect{BC}+\dfrac{2}{3} \vect{CD}\\
            & = & \dfrac{2}{3}\vect{BC}+\dfrac{2}{3}\vect{CD}\\
            & =& \dfrac{2}{3}\vect{BD}
            \end{eqnarray*}

            Donc $(BD)$ est parallèle $(IJ)$ à une droite du plan $(IJK)$. Donc $(BD)$ est parallèle au plan$(IJK)$.

## Caractérisation vectorielle d'une droite, d'un plan

### Caractérisation vectorielle d'une droite

!!! info "Droite et vecteur"
    Soient $A$ et $B$ deux points distincts de l'espace. La droite $(AB)$ est l'ensemble des points $M$ tels que $\vect{AM} = \vect{AB}$, où $k \in \R$.

    On dit que $\vect{AB}$ est un **vecteur directeur** de la droite $(AB)$.

### Plan défini par un point et deux vecteurs directeurs.

!!! info ""
    Soient $\vect{u}$ et $\vect{v}$ deux vecteurs \textbf{non colinéaires} de l'espace.
    
    Le plan $\mc{P}$ passe par un point $A$ et a pour vecteurs directeurs $\vect{u}$ et $\vect{v}$ signifie que $\mc{P}$ est l'ensemble des points $M$ tels que $\vect{AM} = \alpha \vect{u} + \beta \vect{v}$ où $\alpha$ et $\beta$ sont des réels.

    Et réciproquement :
    
    Soient $\vect{u}$ et $\vect{v}$ deux vecteurs \textbf{non colinéaires} et $A$ un point de l'espace.
    
    L'ensemble des points $M$ tels que $\vect{AM}=\alpha \vect{u} + \beta \vect{v}$ avec $\alpha$ et $\beta$ réels est un plan passant par $A$.
    
    Un plan est donc entièrement déterminé par un point et deux vecteurs non colinéaires.

### Plan défini par trois points

!!! info "Caractérisation d'un plan"
    Le plan $(ABC)$ est l'ensemble des points $M$ tels que $\vect{AM} = \alpha \vect{AB} + \beta \vect{AC}$ où $\alpha$ et $\beta$ sont des réels.


Soit $D$  une droite de l'espace passant par $A(x_A,y_A,z_A)$ et de vecteur directeur $\V{u}  (a,b,c)$ .

Un point $M (x,y,z)$ appartient à $D$ si et seulement si il existe un réel $t$  tel que $\V{AM}=t\V{u}$

Ce qui s'exprime à l'aide des coordonnées par : 

\[
\left\lbrace\begin{array}{l}
x-x_A=ta\\
y-y_A=tb  \\
z-z_A=tc
\end{array}\right.
\text{ ou encore } \left\lbrace\begin{array}{l}
x=x_A+ta\\
y=y_A+tb  \\
z=z_A+tc
\end{array}\right.
\]

## Vecteurs coplanaires

!!! info "Vecteurs coplanaires"
    Des vecteurs sont coplanaires si et seulement si leurs représentants de même origine $A$ ont leurs extrémités dans un même plan passant par $A$.

!!! tip "Méthode : à partir de deux vecteurs **non colinéaires**"
    D'après le paragraphe précédent :

    Soient trois vecteurs $\vect{u}, \vect{v}, \vect{w}$ tels que $\vect{u}$ et $\vect{v}$ **non colinéaires**.

    $\vect{u}, \vect{v}, \vect{w}$ sont **coplanaires** si et seulement si il existe deux réels $\alpha$ et $\beta$ tels que $\vect{w} = \alpha \vect{u} + \beta \vect{v}$.

!!! tip "Méthode : à partir de trois vecteurs quelconques"
    Trois vecteurs $\vect{u}, \vect{v}, \vect{w}$ sont coplanaires si et seulement si il existe trois réels $a,b$ et $c$ non tous nuls tel que $a\vect{u} + b \vect{v} + c \vect{w} = \vect{0}$.

???- tip "Vocabulaire"
    Si il existe trois réels $a,b$ et $c$ non tous nuls tel que $a\vect{u} + b \vect{v} + c \vect{w} = \vect{0}$, on dit que les vecteurs $\vect{u},\vect{v}, \vect{w}$ sont liés ou linéairement dépendants.

???- example "Exemple"
    On considère une pyramide $ABCDE$ de sommet $E$ dont la base est le parallélogramme $ABCD$.
    
    Soit $\V{u}=\V{AB}$, $\V{v}=2\V{AD}+\V{DE}$ et $\V{w}=\V{AC}+\V{AE}$.
    
    Démontrer que les vecteurs $\V{u},\V{v}$ et $\V{w}$ sont coplanaires.

    ???- done "Réponse"
        On a $\V{w}=\V{AC}+\V{AE} = \V{AB}+\V{BC}+\V{AE}$.

        Comme $ABCD$ est un parallélogramme, $\V{BC}=\V{AD}$.

        On a alors $\V{w} = \V{AB}+\V{AD}+\V{AE}= \V{AB}+\V{AD}+\V{AD}+\V{DE} = \V{AB}+2\V{AD}+\V{DE} = \V{u}+\V{v}$.
        
        Donc $\V{u},\V{v}$ et $\V{w}$ sont coplanaires.

!!! info "Réciproquement"
    Trois vecteurs $\vect{u}, \vect{v}, \vect{w}$ ne sont pas coplanaires si et seulement si l'égalité $a\vect{u} + b \vect{v} +c \vect{w} = \vect{0}$ implique $a=b=c=0$.

!!! tip "Parallélisme entre droite et plan"
    Un droite $(D)$ est parallèle à un plan $\mc{P}$ si et seulement si un vecteur directeur de $(D)$ est coplanaire avec deux vecteurs non colinéaires de $\mc{P}$.

!!! tip "Parallélisme entre deux plans"
    Deux plans $\mc{P}$ et $\mc{P'}$ sont parallèles si et seulement si deux vecteurs non colinéaires de $\mc{P}$ sont respectivement égaux à deux vecteurs du plans $\mc{P'}$.

!!! tip "A propos"
    Cette partie met en place le vocabulaire et les théorèmes qui seront utilisés avec des coordonnées.

    Mais certaines question du bac portent sur les méthodes vues ici **sans coordonnées**.