# Primitives d'une fonction continue sur un intervalle

## Théorème fondamental

!!! info "Théorème fondamental"
    Si $f$ est **une fonction continue et positive** sur un intervalle $[a,b]$ alors la fonction $F$ définie sur $[a,b]$ par $\displaystyle\int_a^x f(t) \dx[t]$ est dérivable sur $[a,b]$ et a pour dérivée $f$ . On a donc $F'(x)=f(x)$.
 


## Lien entre primitives et intégrales

!!! info "Calcul d'une intégrale"
    Si $f$ est une fonction continue et positive sur un intervalle $[a;b]$ et $F$ une primitive de $f$ sur $[a;b]$ : 
    
    \[
        \displaystyle\int_a^b f(x) \dx = F(b) - F(a)
    \]

    On note $F(b) - F(a) = \left[ F(x) \right]_a^b$
 


???- example "Exemple"
    Calculer $\displaystyle\int_0^1 x^2 \dx$.

    ???- done "Réponse"
    
        $F(x)=\dfrac{x^3}{3}$. Donc $\displaystyle\int_0^1 x^2 \dx = \left[ \dfrac{x^3}{3} \right]_0^1 = \dfrac{1}{3}$.

