# Polynôme du second degré<br>Somme et produit des racines

## Somme et produit des racines

Si $\Delta>0$, en identifiant la forme développée de $a(x-x_1)(x-x_2)$ avec $ax^2+bx+c$, on obtient :

\[ a(x-x_1)(x - x_2) = a x^2 - (x_1 + x_2)x + a x_1 x_2 \]

!!! info "Théorème"
    La somme des racines d'un trinôme vaut : $-\frac{b}{a}$ ; et le produit des racines vaut $\frac{c}{a}$.
    
    \[ x_1+x_2=-\frac{b}{a} \quad \text{et} \quad x_1 \times x_2 = \frac{c}{a}\]

!!! note "Utilisation : vérifier les racines"

    A FAIRE

!!! note "Utilisation : trouver des racines simples"
    Exemple : $2x^2-2x-12$
    Le produit des racines vaut $\dfrac{-12}{2} = -6$.  
    On **tente** $x_1 = -1, x_2 = 6$ ou $x_1 = -2, x_2 = 3$ ou $x_1 = -3, x_2 = 2$ ou $x_1 = 1, x_2 = -6$ ou $x_1 = 2, x_2 = -3$ ou $x_1 = 3, x_2 = -2$
    
    Or la somme des racines vaut $\dfrac{-(-2)}{2} = 1$
    
    Parmi les possibilités précédentes, seul $x_1 = 3, x_2 = -2$ convient !

    !!! warning "et si les racines ..."

        Le produit peut faire -6 avec des racines non entières. La méthode précédente est une tentative pour trouver des racines simples. En cas d'échec, revenez à la méthode générale.


!!! note "Utilisation :"
    Résoudre le système suivant :
    
    \[
    \left\{ 
    \begin{array}{rcl} x+y & = & 7 \\ xy & = & 12 \end{array} 
    \right.
    \]
    
    D'après le théorème précédent, $x$ et $y$ sont solutions de l'équation $aT^2+bT+c=0$, en posant que $x+y=-\frac{b}{a}=7$ et $xy=\frac{c}{a}=12$.  
    En choisissant $a=1$, on doit donc rechercher les racines de $T^2-7T+12$. Il s'agit de $3$ et $4$. Donc les solutions du système sont $S=\left\{ \left(3;4\right);\left(4;3\right)\right\}$.