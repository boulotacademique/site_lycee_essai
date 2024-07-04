# Probabilité<br>Espérance et variance

## Définitions et formules

!!! note "Définition"
    Soit $X$ une variable aléatoire prenant les valeurs $x_1; x_2; ...; x_n$ avec les probabilités $p_1; p_2; ...; p_n$.

    - On appelle **espérance** de $X$ le nombre: $E\left( X \right) = p_1 x_1 + p_2 x_2 + ... + p_n x_n =
    \sum\limits_{i = 1}^{i = n} p_i x_i$.  
    - On appelle **variance** de $X$ le nombre:
    
    \[ \begin{eqnarray*}
      V\left( X \right) &= & p_1 \left(x_1 - E\left( X \right) \right)^2 + p_2\left(x_2 - E\left( X \right) \right)^2 + ... + p_n \left(x_n - E\left( X \right)\right)^2 \\
      & = & \sum\limits_{i = 1}^{i = n} p_i\left(x_i - E\left(X\right)\right)^2.
    \end{eqnarray*} \]
    
    - On appelle **écart-type** de $X$ le nombre $\sigma \left(X \right) = \sqrt {V\left( X \right)}$.

- Le mot «espérance» vient du langage des jeux : lorsque $X$ désigne le gain, $E(X)$ est le gain moyen que peut espérer un joueur sur un grand nombre de parties.
- Une autre formule de la variance est $V\left( X \right) = \sum\limits_{i = 1}^{i = n} p_i x_i^2 - \left[ E\left( X \right) \right]^2$.

!!! note "Vocabulaire"
    Un jeu est **équitable** lorsque l'espérance du gain est nulle.

???- example "Exemple"

    On donne la loi de probabilité d'une variable aléatoire $X$. 

    Calculer $E\left( X \right)$ et $\sigma \left( X \right)$ sans puis avec une calculatrice.

    \[ \begin{array}{|c|c|c|c|c|}
    \hline
    x_i & -3 & - 1 & 2 & 5 \\
    \hline
    p_i & 0,1 & 0,4 & 0,3 & 0,2 \\
    \hline
    \end{array} \]

    ???- done "Solution"
        A FAIRE SANS ET AVEC CALCULATRICE

!!! tip "Méthode - Interpréter l'espérance et la variance"

    ???- example "Exemple"
        On donne les lois de probabilités du gain $X$ et $Y$ de deux jeux.  
        **Jeu $\no$ 1**

        \[ \begin{array}{|c|c|c|c|c|c|}
        \hline
        x_i & -5 & -1 & 0 & 1 & 3 \\
        \hline
        \Pb( X = x_i) & 0,2  & 0,3 & 0,1 & 0,1 & 0,3 \\
        \hline
        \end{array} \]

        **Jeu $\no$ 2**

        \[ \begin{array}{|c|c|c|c|c|c|}
        \hline
        y_i & -3 & -1 & 0 & 1 & 2 \\
        \hline
        \Pb( Y = y_i) & 0,1  & 0,4  & 0,2 & 0,2 & 0,1 \\
        \hline
        \end{array} \]

        Quel jeu peut-on conseiller au joueur ?

        ???- done "Solution"
            Pour le jeu $\no$ 1 : $E\left( X \right) = - 0,3$, $V\left( X \right) = 8,01$ et $\sigma \left( X \right) \approx 2,83$.
            
            Pour le jeu $\no$ 2 : $E\left( Y \right) = - 0,3$, $V\left( Y \right) = 1,81$ et $\sigma \left( Y \right) \approx 1,35$.

            Les deux jeux ont la même espérance de gain, celle-ci étant négative. Les jeux sont **défavorables** aux joueurs, on peut donc les déconseiller.  

            L'écart-type mesure la dispersion des gains autour de l'espérance, donc il évalue le **risque du jeu**. Ici, $\sigma \left( Y \right) < \sigma (X)$.

            Si un joueur veut vraiment participer, il vaut mieux lui conseiller le jeu $\no$ 2 pour lequel le degré de risque est moins grand.

## Transformation affine d'une variable aléatoire

!!! note "Définition"
    Soit $X$ une variable aléatoire prenant les valeurs $x_1\ ;\ x_2\ ;\ ...\ ;\ x_n$.

    Pour tous réels $a$ et $b$, on peut définir une autre variable aléatoire, en associant à chaque issue donnant la valeur $x_i$, le nombre $a x_i + b$. On note cette variable aléatoire $aX + b$.


!!! abstract "Théorème"

    \[ E\left( {aX + b} \right) = aE(X) + b\ \text{ et } \ V\left( {aX} \right) = {a^2}V\left( X \right). \]

    ???- abstract "Démonstration"
    
        \[
        \begin{eqnarray*}
        E\left( aX + b \right) & = & p_1\left( a x_1 + b \right) + p_2\left( a x_2 + b \right) + ... + p_n \left( a x_n + b \right) \\
        & = & a p_1 x_1 + b p_1 + a p_2 x_2 + b p_2 + ... +  a p_n x_n + b p_n\\
        & = & a p_1 x_1 + a p_2 x_2  + ... + a p_n x_n  +  b p_1 + b p_2 + ... + b p_n\\
        & = & a\left( p_1 x_1  +  p_2 x_2  + ... +  p_n x_n  \right) +  b\left(  p_1  +  p_2  + ... +  p_n \right)\\
        & = & aE\left( X \right) + b \times 1 \\
        E\left( aX + b \right) & = & aE\left( X \right) + b
        \end{eqnarray*} \]

        D'après la seconde formule de la variance :

        $V\left( aX \right) = p_1\left( a x_1 \right)^2 + p_2 \left( a x_2 \right)^2 + ... + p_n \left( a x_n \right)^2 - \left[ E\left( aX \right) \right]^2$

        D'après la formule précédente: $E\left( a X \right) = a E\left( X \right)$, donc:

        \[
        \begin{eqnarray*}
        V\left( aX \right) & = & p_1 a^2 x^2_1 + p_2 a^2 x^2_2 + ... + p_n a^2 x^2_n - \left[ a E\left( X \right) \right]^2 \\
        & = &  a^2 \left(  p_1 x^2_1 +  p_2 x^2_2 + ... +  p_n x^2_n  \right) -  a^2 \left[  E\left( X \right) \right]^2\\
        & = &  a^2 \left(  p_1 x^2_1 +  p_2 x^2_2 + ... + p_n x^2_n - \left[ E\left( X \right) \right]^2 \right)\\
        V\left( aX \right) & = & a^2 V\left( X \right)
        \end{eqnarray*}
        \]

        $V\left( aX + b \right) = a^2 V\left( X \right) \text{ et } \sigma \left( aX + b \right) = \left| a \right|\sigma \left( X \right)$

        En effet :

        -  

        \[ \begin{eqnarray*}
        V\left( aX + b \right) & = & \sum\limits_{i = 1}^{i = n} p_i \left( a x_i  + b - E\left( aX + b \right) \right)^2\\
        & = & \sum\limits_{i = 1}^{i = n} p_i \left( a x_i + b - aE\left( X \right) - b \right)^2\\
        & = & \sum\limits_{i = 1}^{i = n} p_i \left( a x_i - aE\left( X \right) \right)^2\\
        & = & \sum\limits_{i = 1}^{i = n} p_i a^2 \left( x_i - E\left( X \right) \right)^2\\
        V\left( aX + b \right) & = & a^2 V\left( X \right)
        \end{eqnarray*} \]

        - 

        \[ \begin{eqnarray*}
        \sigma \left( aX + b \right) & = & \sqrt{V\left( aX + b \right)}\\
        & = & \sqrt{a^2} V\left( X \right) = \left| a \right|\sqrt{V\left( X \right)}\\
        \sigma \left( {aX + b} \right)&= \left| a \right|\sigma \left( X \right)
        \end{eqnarray*} \]

???- example "Exemple"
    On donne $E(X) = 3$ et $V(X) =16$.  

    Calculer: 
  
    1. $E(-2X + 5)$
    2. $V(-2X + 5)$
    3. $\sigma(-2X + 5)$


    ???- done "Solution"

        1. $E(-2X + 5) = -2E(X) + 5 = -2 \times 3 + 5 = -1$
        2. $V(-2X + 5) = (-2)^2 \times V(X) = 4 \times 16 = 64$
        3. $\sigma(-2X + 5) = |-2| \sigma (X) = 2\sqrt{V(X)} = 2 \times \sqrt{16} = 8$

!!! tip "Méthode - Appliquer une transformation affine"

    ???- example "Exemple"
        Un coiffeur se déplace à domicile. 

        On note $X$ le nombre de rendez-vous sur une journée.

        La loi de probabilité de $X$ est donnée par le tableau ci-dessous.

        \[ \begin{array}{|c|c|c|c|c|c|c|}
        \hline
        x_i & 0    & 1    & 2    & 3    & 4    & 5    \\
        \hline
        p_i & 0,03 & 0,09 & 0,15 & 0,38 & 0,18 & 0,17 \\
        \hline
        \end{array} \]

        Chaque rendez-vous lui rapporte 30 euros, et ses frais de fonctionnement quotidiens s'élèvent à 15 euros. 

        On note $Y$ son gain journalier.

        1) Calculer $E(X)$.  
        2) Quelle relation lie $X$ et $Y$ ?  
        3) En déduire $E(Y$).

        ???- done "Solution"

            1)

            \[ \begin{eqnarray*}
            E\left( X \right) & = & 0,03 \times 0 + 0,09 \times 1 + 0,15 \times 2 + 0,38 \times 3 + 0,18\\
            & & \phantom{0,03 \times 0 + 0,09 \times 1 + 0,15 \times 2 + 0,38} \times 4 + 0,17 \times 5\\
            E\left( X \right) & = & 3,1.
            \end{eqnarray*} \]

            2) Le gain journalier $Y$ est tel que $Y = 30X - 15$.  
            3)

            \[ \begin{eqnarray*}
            E\left( Y \right) & = & E\left( {30X - 15} \right)\\
            & = & 30E\left( X \right) - 15\\
            & = & 30 \times 3,1 - 15 \\
            & = & 93 - 15\\
            E\left( Y \right) & = & 78 \text{ (en euros).}
            \end{eqnarray*} \]

            Ainsi, le coiffeur peut espérer gagner 78 euros en moyenne par jour.