# Vecteur<br>Opérations sur les vecteurs

## Rappel

!!! abstract "Théorème"
    L'enchaînement de deux translations est également une translation.

!!! abstract "Théorème -Relation de Chasles"
    Soit $A$, $B$, $C$ trois points. 

    L'enchaînement de la translation de vecteur $\vect{AB}$ puis de la translation de vecteur $\vect{BC}$ est la translation de vecteur $\vect{AC}$ et on a: $\vect{AB}+\vect{BC}=\vect{AC}$.

$\vect{AB}+\vect{BA}=\vect{AA}=\vect 0$.

!!! abstract "Théorème"
    Soit $\vect {AB}$ et $\vect {CD}$ deux vecteurs. Alors : 
    - $\vect {AB} +\vect {CD}=\vect {CD} +\vect {AB}$ 
    - $\vect {AB} + \vect 0 = \vect {AB}$

!!! abstract "Théorème - Propriété du parallélogramme"
    Soit $A$, $B$, $C$, $D$ quatre points. 

    Dire que $\vect{AD}=\vect{AB}+\vect{AC}$ équivaut à dire que $ABDC$ est un parallélogramme. 


## Décomposition d'un vecteur

!!! abstract "Théorème" 
    Soient $\vect{u}$ et $\vect{v}$ deux vecteurs du plan non nuls et non colinéaires. Tout vecteur $\vect{w}$ du plan s'écrit de façon unique sous la forme $\vect{w}=x\vect{u}+y\vect{v}$ où $x$ et $y$ sont des réels.

!!! abstract "Théorème - Application aux repères du plan"
    Soient $A$, $B$ et $C$ trois points non alignés du plan.

    Pour tout point $M$ du plan, il existe un unique couple de réels $(x\ ;\ y)$ tel que $\vect{AM}=x\vect{AB}+y\vect{AC}$.

    Le triplet ($A$\ ;\  $\vect{AB}$, $\vect{AC}$) définit donc un repère du plan et le couple $(x\ ;\ y)$ est appelé le couple de coordonnées de $M$ dans ce repère.

## Norme d'un vecteur

Dans cette partie, on se place dans un repère orthonormé.

!!! note "Définition"
    -  Soit $A$ et $B$ deux points. La norme de $\vect{AB}$, notée $\left\Vert{}\vect{AB}\right\Vert{}$, est définie par $\left\Vert{}\vect{AB}\right\Vert{}=AB$.
    -  Soit $\vect{u}$ un vecteur et deux points $A$ et $B$ tels que $\vect{u}=\vect{AB}$.

    La norme de $\vect{u}$ est alors définie par $\left\Vert{}\vect{u}\right\Vert{}=AB$.

!!! abstract "Théorème"
    - Si $\vect{u}\covec{x}{y}$ dans un repère orthonormé alors $||\vect{u}||=\sqrt{x^2+y^2}$.
    - Pour tout réel $k$, on a $\left\Vert{}k\vect{u}\right\Vert{}=|k|\times\left\Vert{}\vect{u}\right\Vert{}$.

!!! tip "Méthode"
    De $\vect{AB}\covec{x_B-x_A}{y_B-y_A}$, on retrouve $\left\Vert{}\vect{AB}\right\Vert{}=\sqrt{(x_B-x_A)^2+(y_B-y_A)^2}=AB$ dans un repère orthonormé.
