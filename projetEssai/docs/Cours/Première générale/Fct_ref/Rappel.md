# Fonctions de références<br>Rappel

## Sens de variations d'une fonction

!!! note "Définition"
    Soit $f$ une fonction définie sur un intervalle $I$. On dit que :

    - $f$ est **croissante** sur $I$ lorsque pour tous les réels $a$ et $b$ dans $I$:  
    si $a < b$, alors $f(a) \leq f(b)$
    - $f$ est strictement croissante sur $I$ lorsque pour tous les réels $a$ et $b$ dans $I$:  
    si $a < b$, alors $f\left( a \right) < f\left( b\right)$
    - $f$ est **décroissante** sur $I$ lorsque pour tous les réels $a$ et $b$ dans $I$:  
    si $a < b$, alors $f\left( a \right) \ge f\left( b \right)$
    - $f$ est **strictement décroissante** sur $I$ lorsque pour tous les réels $a$ et $b$ dans $I$:  
    si $a < b$, alors $f\left( a \right) > f\left( b \right)$
    - $f$ est monotone sur $I$ lorsque $f$ est croissante sur $I$ ou décroissante sur $I$.

## Fonctions carré et inverse


Fonction carré : $x \mapsto x^2$ définie sur $D = \R$ 

La fonction carré est strictement décroissante sur $\left] - \infty\ ;\ 0 \right]$ et strictement croissante sur $\left[0\ ;\ + \infty \right[$.

- Si $0 \leq a < b$, alors $a^2 > b^2$
- Si $a < b \leq 0$, alors $a^2 < b^2$

Sa courbe représentative est une parabole de sommet $O$, d'axe ($Oy$) 

DESSIN A FAIRE

Fonction inverse :$x \mapsto \dfrac{1}{x}$ définie sur $D = \R \backslash\{0\}$ 

La fonction inverse est strictement décroissante sur $\left] -\infty\ ;\ 0 \right[$ et strictement
décroissante sur $\left] 0\ ;\ +\infty \right[$.
- Si $0 < a < b$, alors $\dfrac{1}{a} >\dfrac{1}{b} > 0$
- Si $a < b < 0$, alors $0 > \dfrac{1}{a} >\dfrac{1}{b}$ 
Sa courbe représentative est une hyperbole de centre de $O$

DESSIN A FAIRE

## Fonction racine carrée

!!! note "Définition"
    La **fonction racine carrée** est la fonction définie sur $\left[ {0\ ;\ +\infty } \right[$ par $f\left( x \right) = \sqrt{x}$.

!!! abstract "Théorème"
    La fonction racine carrée est strictement croissante sur $\left[ 0\ ;\ + \infty \right[$.

DESSIN A FAIRE

???- abstract "Démonstration"
    Posons $f\left( x \right) = \sqrt{x}$. Soit $a$ et $b$ deux réels tels que $0 \leq a < b$.
    Comparons $f\left( a \right)$ et $f\left( b \right)$ en étudiant le signe de leur différence:

    \[ \begin{eqnarray*}
    f\left( a \right) - f\left( b \right) & = & \sqrt{a}  - \sqrt{b} \\
    & = & \dfrac{\sqrt{a} - \sqrt{b}}{\sqrt{a} + \sqrt{b}} \times \left( \sqrt{a} + \sqrt{b} \right) \\
    & = & \dfrac{(\sqrt{a})^2 - (\sqrt{b})^2}{\sqrt{a}  + \sqrt{b}} \\
    & = & \dfrac{a - b}{\sqrt{a} + \sqrt{b}}
    \end{eqnarray*} \]

    $a - b < 0{\text{ et }}\sqrt{a}  + \sqrt{b}  > 0{\text{  donc }}f\left( a \right) - f\left( b \right) < 0{\text{  donc }}f\left( a \right) < f\left( b \right)$.

    Ainsi, $f$ est strictement croissante sur $[0 ; +\infty[$
