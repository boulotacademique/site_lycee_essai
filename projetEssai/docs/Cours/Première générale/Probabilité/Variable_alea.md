# Probabilité<br>Variables aléatoires

!!! note "Définition - Variable aléatoire discrète"
    Soit $\Omega = \left\{ e_1; e_2; ...;e_m \right\}$ l'univers fini d'une expérience aléatoire.

    Une variable aléatoire $X$ sur $\Omega$ est une fonction qui, à chaque issue de $\Omega$, associe un nombre réel.

    $x$ est un réel, l'événement « $X$ prend la valeur $x$ » est noté ($X = x$), il est formé de toutes les issues de $\Omega$ ayant pour image $x$.

!!! note "Définition - Loi de probabilité d'une variable aléatoire discrète"
    Soit $X$ une variable aléatoire prenant les valeurs $\left\{ x_1; x_2; ...; x_n \right\}$. Lorsqu'à chaque valeur $x_i$, on associe la probabilité de l'événement ($X = x_{i}$) , on définit **la loi de probabilité** de $X$.

!!! tip "Méthode"
    La loi de probabilité d'une variable aléatoire se présente à l'aide d'un tableau.
    
    \[ \begin{array}{|c|c|c|c|c|}
    \hline
    x_i & x_1 & x_2 & \ldots & x_n \\
    \hline
    \Pb\left( X = x_i \right) & p_1 & p_2 & \ldots & p_n \\
    \hline
    \end{array} \]
  
    On a $\Pb\left( X = x_1 \right) + \Pb\left( X = x_2 \right) + ... + \Pb\left( X = x_n \right) = 1$.

!!! tip "Méthode - Etudier une variable aléatoire"
    Pour déterminer la loi de probabilité d'une variable aléatoire $X$ :

    - on détermine les valeurs $x_i$ que peut prendre $X$ ;
    - on calcule les probabilités $\Pb\left( X = x_i \right)$ ;
    - on résume les résultats dans un tableau.

???- example "Exemple"
    Une urne contient cinq jetons indiscernables au toucher numérotés de 1 à 5.

    Un joueur participe à la loterie en payant 2 &euro;, ce qui lui donne le droit de prélever au hasard un jeton dans l'urne.
    
    - Si le numéro est pair, il gagne en euros le double de la valeur indiquée par le jeton.
    - Si le numéro est impair, il perd sa mise.
    Soit $X$ la variable aléatoire égale au &laquo; gain algébrique &raquo;. 

    Déterminer la loi de probabilité de $X$.

    ???- done "Solution" 
        L'univers est l'ensemble des 5 jetons. 

        Les cinq issues sont équiprobables.

        Les jetons 1, 3 et 5 font perdre 2 euros ; le jeton 2 fait gagner $2 \times 2 - 2 = 2$ euros ; le jeton 4 fait gagner $4 \times 2 - 2 = 6$ euros.  

        $X$ peut prendre les valeurs $- 2, 2$ et $6$.

        L'événement $\left( {X = - 2} \right)$ est réalisé pour les issues 1 ; 3 ; 5 donc $\Pb\left( {X = - 2} \right) = \dfrac{3}{5}$.

        L'événement $\left( {X = 2} \right)$ est réalisé pour l'issue 2 donc $\Pb\left( {X = 2} \right) = \dfrac{1}{5}$.

        L'événement $\left( {X = 6} \right)$ est réalisé pour l'issue 4 donc $\Pb\left( {X = 6} \right) = \dfrac{1}{5}$.

        On présente la **loi de probabilité** de $X$ dans un tableau.

        \[ \begin{array}{|c|c|c|c|}
        \hline
        {x_i} & - 2 & 2 & 6 \\
        \hline
        \Pb\left( {X = {x_i}} \right) & \dfrac{3}{5} & \dfrac{1}{5} & \dfrac{1}{5} \\
        \hline
        \end{array} \]
