# Succession d'épreuves indépendantes

!!! info "Succession d'épreuves"
    Soit $n \in \N$. On note $E_i$, pour $1\leq i \leq n$, $n$ épreuves indépendantes issues respectivement des univers $\Omega_i$. La succession de ces $n$ épreuves successives est une épreuve dont les issues sont les éléments de l'univers $\Omega_1 \times \Omega_2 \times \ldots \times \Omega_n$.

???- example "Exemple"
    Il y a 3 urnes : l'une avec des jetons numérotés entre 1 et 4, la deuxième avec des numéros entre 1 et 6 et la dernière avec des numéros entre 1 et 8. On prélève successivement (dans l'ordre décrit précédemment) un jeton dans ces urnes. Cette succession d'épreuves est associée à l'univers $\{1;2;3;4\} \times \{1;2;3;4;5;6 \} \times \{1;2;3;4;5;6;7;8\}$.
    
    Une issue possible est $(2;6;7)$.

!!! info "Théorème"
    Soit une succession de $n$ **épreuves indépendantes**.

    La probabilité d'obtenir une issue $(x_1;x_2;\ldots;x_n)$ est :

    \[
    \Pb(x_1;x_2;\ldots;x_n) = \Pb(x_1) \times \Pb(x_2) \times \ldots \times \Pb(x_n)
    \]

???- example "Exemple"
    Dans l'exemple précédent, la probabilité de $(2;5;7)$ est 
    
    $\Pb((2;5;7)) = \Pb(2) \times \Pb(5) \times \Pb(7) = \dfrac{1}{4} \times \dfrac{1}{6} \times \dfrac{1}{8} = \dfrac{1}{192}$.

???- tip "Cas des épreuves non indépendantes"
    Dans le cas d'une succession d'épreuve non indépendants, on revient à l'arbre pondéré !

    ???- example "Exemple"
        On tire au sort successivement deux boules sans remise dans une urne contenant 2 boules rouges et 3 boules vertes.
        
        Calculer la probabilité de l'événement $A$ : &laquo; obtenir exactement une boule rouge &raquo;.

        ???- done "Réponse"
            A l'aide d'un arbre, on trouve que $\Pb (A)= 0.4 \times 0.75+0.6 \times 0.5=0.6$.

???- tip "Remarque"
    Ici,  &laquo; succession d'épreuve &raquo; est une modélisation de la réalité. Il est possible d'avoir une situation réelle avec des événements simultanés mais elle serait modélisée par &laquo; une succession d'épreuves &raquo;.

    Par exemple, on lance (simultanément) trois dés de couleurs différentes et on note les numéros (toujours dans le même ordre, grâce aux couleurs). Cette situation peut se modéliser par une succession d'épreuve !

Pour cette année, on considère que des \textbf{épreuves sont indépendantes} lorsque :

- ou l'énoncé le précise clairement
- ou la situation est assimilée à un tirage avec remise.

???- example "Exemple"
    Dans une urne, il y  a 3 jetons rouges et 7 jetons verts. On tire successivement et avec remise 3 jetons de l'urne.
    
    1. Décrire explicitement une épreuve, la succession d'épreuve. Est-ce une succession indépendante ? Expliquer.

    2. Soit $E=\{R;V\}$. Exprimer l'univers $\Omega$ en fonction de $E$.
    
    3. En déduire la probabilité de l'issue $(R,R,V)$.

    ???- done "Réponse"
    
        1. L'épreuve est &laquo; tirer un jeton &raquo;. On répète successivement 3 fois cette épreuve. Il s'agit bien d'une succession indépendante car c'est un tirage avec remise.
        2. $\Omega=E^3$
        3. On note $R_i$ l'événement &laquo; avoir un jeton rouge au i-ème tirage&raquo;, et $V_i$ l'événement &laquo; avoir un jeton vert au i-ème tirage&raquo;.
        
        $\Pb((R,R,V))=\Pb(R_1) \times \Pb(R_2) \times \Pb(V_3)=0.3^2 \times 0.7$
        
        Rque : on notera plus simplement $\Pb((R,R,V))=\Pb(R) \times \Pb(R) \times \Pb(V)$
