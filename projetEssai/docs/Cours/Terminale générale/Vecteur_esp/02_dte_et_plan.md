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


