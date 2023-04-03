# La perspective cavalière

!!! info "Règles de la perspective cavalière"
    La perspective cavalière permet de représenter un objet en trois dimensions sur une surface à deux dimensions. Cette représentation ne présente pas de point de fuite : la taille des objets **ne diminuent pas lorsqu'ils s'éloignent** En voici les règles

    - Règle 1 : Les lignes et arêtes cachées sont représentées en pointillés, celles qui sont visibles en trait plein.
    - Règle 2 : Les éléments situés dans un **plan frontal** (c'est-à-dire un plan perpendiculaire au regard de l'observateur) sont représentés en vraie grandeur, non déformés : les distances et les angles sur la représentation sont les mêmes que sur l'objet lui-même.
    - Règle 3 : Les droites perpendiculaires au plan frontal, appelées **fuyantes**, sont représentées par des droites parallèles entre elles, formant un angle donné avec l'horizontale, appelé **angle de fuite** (généralement entre $30°$ et $60°$).
    - Règle 4 : Les longueurs représentées dans la direction des fuyantes ne sont pas les longueurs réelles : on les multiplie par un **coefficient de perspective** (parfois précisé).

!!! info "Ce que conserve la perpective cavalière"

    - Deux droites parallèles sont représentées par deux droites parallèles.
    - Des droites concourantes sont représentées par des droites concourantes.
    - Des points alignés sont représentés par des points alignés.
    - Les milieux (ou tout autre division) de segments sont conservés.

!!! danger "Ce que ne conserve pas la perpective cavalière"
    La perspective cavalière **ne conserve pas** : 

    - la mesure : deux segments de même longueur peuvent être représentés par des segments de longueurs différentes ;
    - Les angles : en particulier deux droites perpendiculaires peuvent être représentées par deux droites non perpendiculaires

    Donc un carré peut être représenté par un parallélogramme.
    
    Deux droites peuvent se couper sur la perspective sans être sécantes en réalité !

# Droites et plans dans l'espace

## Définition

!!! info "Qu'est-ce qu'un plan ?"
    Soit $A$, $B$, $C$ trois points de l'espace distincts et non alignés.

    - Pour déterminer un plan, il suffit de donner  3 points non alignés  ou   2 droites sécantes  ou 2 droites parallèles (non confondues).
    - Le **plan** noté $(ABC)$ est constitué par les points des droites passant par $A$ et parallèles ou sécantes à la droite $(BC)$.

    IMAGE GEOGEBRA AFAIRE

???- danger ""
    Un plan est infini ! Mais une partie d'un plan est souvent représentée sous la forme d'un parallélogramme (plus rarement d'un triangle). 

Pour désigner un plan, il suffit de noter entre parenthèses les noms de trois points non alignés de ce plan.

???- tip ""
    Dans chaque plan de l'espace, on peut appliquer tous les théorèmes de géométrie plane.

???+ example "Exemple"
    $ABCDEFGH$ est un parallélépipède rectangle tel que: 
    
    - $AB=7$ cm
    - $AD=6$ cm
    - $I$ est le milieu de $[AB]$
    - $J$ est le milieu de $[AD]$ 

    <ol>
    <li> Nommer le plan colorié. </li>
    <li> Calculer la longueur $BD$.</li>
    <li> Calculer la longueur $IJ$.</li>
    </ol>

    ???- done "Réponse"
        1. Le plan colorié coupe les arêtes du pavé en $I$, $J$, $K$ et $L$, $(IJK)$ est donc un  nom possible.
        2. La face $ABCD$ du pavé est un rectangle donc le triangle $ABD$ est rectangle en $A$. 
        
            D'après le théorème de Pythagore:
            
            $BD^2=BA^2+AD^2=7^2+6^2=49+36=85$.
            
            Une longueur est toujours positive donc $BD=\sqrt{85}$~cm.
        
        3. &laquo; Dans un triangle si un segment joint les milieux de deux côtés alors il mesure la moitié du troisième côté.&raquo;
        
            Ici, dans le triangle $ABD$, $I$ est le milieu du côté $[AB]$ et $J$ celui du côté $[AD]$. 
            
            Donc $[IJ]$ mesure la moitié du troisième côté $[BD]$. 
    
            $IJ=BD\div 2$ soit $IJ=\dfrac{1}{2}\sqrt{85}$~cm.

## Positions relatives de deux droites

!!! info "Droites coplanaires"
    Deux droites incluses dans un même plan sont dites **coplanaires**.

!!! info "Positions relatives de deux droites"
    Deux droites de l'espace sont soit coplanaires soit non coplanaires.

    ???- abstract "Si les deux droites sont coplanaires ..."

        Si deux droites sont coplanaires :
        
        - elles peuvent être parallèles :
            - ou strictement parallèles
            - ou (parallèles) confondues
        - elles peuvent être sécantes
    
    ???- abstract "Si les deux droites sont non coplanaires ..."

        Si les deux droites sont non coplanaires, elles ne peuvent ni être parallèles ni être sécantes !

!!! warning "Différence importante entre le plan et l'espace"
    Dans l'espace, si deux droites ne sont pas parallèles alors cela ne veut pas obligatoirement dire qu'elles sont sécantes !

    En effet, dans l'espace, il y a 3 possibilités (au lieu de 2 dans le plan) :
        
    - parallèles
    - sécantes
    - non coplanaires

## Position relative de deux plans

!!! info "Position relative de deux plans"
    Il n'y a que deux possibilités. En effet, deux plans sont
    
    - soit parallèles (srtictement parallèles ou  confondus)
    - soit sécants

    Si deux plans sont sécants, ils se coupent selon une droite !

???- tip ""
    La position relative de deux plans dans l'espace est dons analogue à celle de 2 droites dans le plan. D'où des théorèmes ressemblant à ce que vous connaissez déjà.

!!! info "Théorème"
    
    - Deux plans parallèles à un même plan sont parallèles entre eux.
    - Soit $P$ et $P'$ deux plans parallèles. Si Un plan coupe l'un, il coupe l'autre suivant deux droites parallèles.

!!! tip "Comment démontrer que deux plans sont parallèles ?"
    Deux plans sont parallèles si et seulement si deux droites sécantes de l'un sont respectivement parallèles à deux droites sécantes de l'autre. 

## Position relative entre un plan et une droite

!!! info "Position relative entre un plan et une droite"

    - Ou une droite $(d)$ et un plan sont parallèles :

        - soit $(d)$ est strictement parallèle à ce plan
        - soit $(d)$ est incluse dans le 

    - Ou une droite $(d)$ et un plan sont sécants. L'intersection est alors un point.

!!! tip "Comment démontrer qu'une droite est parallèle à un plan ?"
    Une droite est parallèle à un plan si et seulement si elle est parallèle à une droite de ce plan.

!!! tip "Le théorème du toit"
    **Théorème du toit :** Soient $\mc{P}$ et $\mc{P'}$ deux plans sécants. Si une droite $d$ de $\mc{P}$ est parallèle à une droite $d'$ de $\mc{P'}$, alors la droite d'intersection de $\mc{P}$ et $\mc{P'}$ est parallèle à $d$ et $d'$.

!!! tip "A propos"
    Cette partie donne le vocabulaire et les théorèmes qui seront pleinement exploités avec des coordonnées. Elle permet aussi d'étudier graphiquement une situation et d'émettre des conjectures.

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
