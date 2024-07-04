# Suite<br>Suites de référence

## Suite arithmétique

!!! note "Définition"
    Dire qu'une suite $(u_n)$ est **une suite arithmétique** signifie qu'il existe un réel $r$ tel que, pour tout $n \in \N$, $u_{n+1}= u_n +r$.

    Le réel $r$ est appelé la **raison** de la suite $(u_n)$.
 
!!! abstract "Théorème"
    Soit $u$ une suite. Dire que $u$ est une suite arithmétique de raison $r$ équivaut à dire que, pour tout $n \in \N$, $u_{n+1}-u_n=r$

???- tip "Méthode pour démontrer qu'une suite **n'est pas** arithmétique"
    Pour démontrer qu'une suite **n'est pas** une suite arithmétique, il suffit de trouver un contre-exemple au théorème précédent. Il suffit donc de trouver un entier $p \geq 1$ tel que $u_{p+1} - u_{p} \neq u_1 - u_0$.

    En général, il suffit de montrer que $u_2 - u_1 \neq u_1 - u_0$ (ici $p = 1$).

???- tip "Méthode pour démontrer qu'une suite **est** arithmétique"
    Pour démontrer qu'une suite **est** une suite arithmétique, il faut **absolument** montrer que **pour tout entier naturel** $u_{n+1} - u_n$ est égal à une constante.

    !!! warning "Attention"
        Montrer que $u_2 - u_1 = u_1 - u_0$ **ne permet JAMAIS** de démontrer que $u_n$ est une suite arithmétique.

!!! abstract "Théorème"
    Soit $u$ une suite arithmétique de raison $r$.
    
    -  Si $r>0$, alors $u$ est strictement croissante.
    -  Si $r<0$, alors $u$ est strictement décroissante.
    -  Si $r=0$, alors $u$ est constante.

!!! abstract "Théorème"
    Soit $u$ une suite arithmétique de raison $r$, alors :
 
    - Pour tout $n$ et $p$ deux entiers, $u_n=u_p+(n-p)r$.
    - Pour tout $n$ et $p$ deux entiers, 
    
    \[ 
        \sum_{i=p}^{n} u_i = u_p + u_{p+1} + \ldots + u_n = \dfrac{(u_p+u_n)(n-p+1)}{2} 
    \]

    - **Des cas particuliers** à connaitre par c&oelig;ur :
    
    \[ 
        \sum_{i=0}^{n} u_i = u_0 + u_{1} + \ldots + u_n = \dfrac{(u_0+u_n)(n+1)}{2}
    \]
    
    \[ 
        \sum_{i=1}^{n} i = 1 + 2 + \ldots + n = \dfrac{(1+n)n}{2}
    \]

<!-- !!! abstract "Théorème"
    Soit $u$ une suite arithmétique de raison $r$
 
    -  Si $r>0$ alors 
    
    \[ \lim_{n \to + \infty} u_n = + \infty \]

    -  Si $r<0$ alors
    
    \[ \lim_{n \to + \infty} u_n = - \infty \] -->

!!! example "Exemple - A FAIRE"
    Intérêts simples

## Suite géométrique

!!! note "Définition"
    Dire qu'une suite $(u_n)$ est **une suite géométrique** signifie qu'il existe un réel $q$ tel que, pour tout $n \in \N$, $u_{n+1}= q \times u_n$.
    
    Le réel $q$ est appelé la **raison** de la suite $(u_n)$.

!!! abstract "Théorème"
    Soit $u$ une suite. Dire que $u$ est une suite géométrique de raison $q \neq 0$ équivaut à dire que, pour tout $n \in \N$, $\dfrac{u_{n+1}}{u_n}=q$

!!! abstract "Théorème"
    Soit $u$ une suite géométrique de raison $q \neq 0$.
 
    -  Si $q>1$ et si $u_0>0$, alors $u$ est croissante.
    -  Si $0<q<1$ et si $u_0>0$, alors $u$ est décroissante.
    -  Si $q=1$, alors $u$ est constante.
    -  Si $q<0$, alors $u$ n'est pas monotone.

!!! abstract "Théorème"
    Soit $u$ une suite géométrique de raison $q \neq 0$.
 
    -  Si $q>1$ et si $u_0<0$, alors $u$ est décroissante.
    -  Si $0<q<1$ et si $u_0<0$, alors $u$ est croissante.

???- example "Exercice"
    En remarquant qu'une suite géométrique peut s'écrire $u_n=u_0 \times q^n$, démontrer le théorème sur les variations de $u$ (attention au signe de $u_0$)

    ???- done "Solution"
        Soit $(u_n)$ une suite géométrique.
        
        - Si $q > 1$, alors :  
            - Si $u_0 >0$, alors pour tout $n \in \N$, $u_n = u_0 q^n >0$ et $\dfrac{u_{n+1}}{u_n} = q > 1$. [Ainsi](./variations.md#var01), $(u_n)$ est strictement croissante.
            - Si $u_0 <0$, alors pour tout $n \in \N$, $u_n = u_0 q^n <0$ et $\dfrac{u_{n+1}}{u_n} = q > 1$. [Ainsi](./variations.md#var01), $(u_n)$ est strictement décroissante.
        - Si $0< q < 1$, alors :  
            - Si $u_0 >0$, alors pour tout $n \in \N$, $u_n = u_0 q^n >0$ et $0 < \dfrac{u_{n+1}}{u_n} = q < 1$. [Ainsi](./variations.md#var02), $(u_n)$ est strictement décroissante.
            - Si $u_0 <0$, alors pour tout $n \in \N$, $u_n = u_0 q^n <0$ et $0<> \dfrac{u_{n+1}}{u_n} = q > 1$. [Ainsi](./variations.md#var02), $(u_n)$ est strictement croissante.
        - Si $q = 1$, alors $(u_n)$ est constante.


!!! abstract "Théorème"
    Soit $u$ une suite géométrique de raison $q$, alors :

    - Pour tout $n$ et $p$ deux entiers, $u_n=u_p \times q^{n-p}$.  
    - Pour tout $n$ et $p$ deux entiers,  
        - Si $q \neq 1$, alors 
        
        \[ \sum_{i=p}^{n} u_i = u_p + u_{p+1} + \ldots + u_n = \mathbf{u_p} \dfrac{1-q^{n-p+1}}{1-q} = \text{premier terme} \times \dfrac{1 - q^{\text{nb de termes}}}{1 - q} \]

        - Si $q = 1$, alors
        
        \[ \sum_{i=p}^{n} u_i = u_p + u_{p+1} + \ldots + u_n = (n-p+1) \times u_p = \text{nb de termes} \times u_p \]

    -  Des cas particuliers à connaitre par c&oelig;ur :
        
        \[ \sum_{i=0}^{n} u_i = u_0 + u_{1} + \ldots + u_n = u_0 \dfrac{1-q^{n+1}}{1-q} \text{ pour } q \neq 1 \]

        \[ \sum_{i=0}^{n} q^i = 1 + q + q^2 + \ldots + q^n = \dfrac{1-q^{n+1}}{1-q} \text{ pour } q \neq 1 \]

        \[ \sum_{i=0}^{n} u_i = u_0 + u_{1} + \ldots + u_n = u_0 \times (n+1) \text{ pour } q = 1 \]

!!! example "Exemple - A FAIRE"
    Intérêts composés

<!-- !!! abstract "Théorème"
    Soit $q$ un réel.

    -  Si $q>1$ alors 
    
    \[ \lim_{n \to + \infty} q^n = + \infty \]

    -  Si $q=1$ alors ($\left( q^n\right)_{n \in\N}$ est constante et vaut $1$) 
    
    \[ \lim_{n \to + \infty} q^n = 1 \]

    -  Si $-1<q < 1$ alors 
    
    \[ \lim_{n \to + \infty} q^n = 0 \]

    -  Si $q \leq -1$, alors la suite $\left( q^n\right)_{n \in\N}$ n'a pas de limite. -->


## Suite arithmético-géométrique
