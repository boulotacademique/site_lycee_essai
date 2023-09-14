<!--# Dénombrement : arrangement

Pour compter le nombre d'éléments d'un ensemble, le principe additif et multiplicatif ne couvrent pas les situations les plus usuelles.

## Factorielle

!!! info "Factorielle"
    Soit $n \in \N$, on appelle **factorielle n** et on note $\mathbf{n!}$, le produit de tous les nombres entiers de $1$ à $n$.
    
    \[
    n! = 1 \times 2 \times \ldots \times n
    \]
 

???- example "Exemple"
    Calculer (sans calculatrice) et/ou simplifier les expressions suivantes :
    
    1. $5!$
    2. $\dfrac{10!}{8!}$
    3. $n!-(n-1)!$ pour tout $n>0$
    4. $\dfrac{n!}{(n-3)!}$ pour tout $n>2$
    
 
    ???- done "Réponse"

        1. $5!=120$
        2. $\dfrac{10!}{8!}=90$
        3. $n!-(n-1)! = (n-1)!(n-1)$
        4. $\dfrac{n!}{(n-3)!}=n \times (n-1) \times (n-2)$


!!!- info "Conséquence"
    
    - $0!=1$ (Convention)
    - Si $n \geq 1$, $n!=n\times (n-1)!$
    - $(n+1)!=(n+1) \times n!$



???- example "Exemple"
    Ecrire en python la fonction qui retourne factorielle $n$.
 
    ???- done "Réponse"

        ```python
        def fact(n):
            p=1
            for i in range(1,n+1):
                p=p*i
            return p

        n=int(input("Valeur de n ? "))
        print(fact(n))
        ```
 

## Nombre de p-uplets

!!!- info "Nombre de $p$-uplets"
    Le nombre de $p$-uplet d'un ensemble à $n$ éléments est $n^p$.

    On rappelle qu'un $p$-uplet est une liste (donc **on tient compte de l'ordre**) de $p$ éléments (**pas forcément distincts**).

???- example "Exemple" 
    On lance 7 fois une pièce de 1 euro pour jouer à pile ou face. Déterminer le nombre de résultats possibles.
 
    ???- done "Réponse"
        $E=\{ P;F \}$. Exemple d'un résultat : $(P;F;F;F;P;F;P)$. La répétition est possible (i.e tous les éléments de la liste ne sont pas forcément distincts) et l'ordre est important !
    
        On s'intéresse aux $7$-uplets de $E$ ou (ce qui est équivalent) au nombre d'élément de $E^7$.
        
        Il y a donc $2^7=128$ résultats possibles.
 
???- example "Exemple"
    Combien de numéros de téléphone commençant par $06$ existe-t-il ? Commençant par $06$ ou $09$ ?
 
    ???- done "Réponse"
        $E=\{0;1;2;3;4;5;6;7;8;9 \}$. La répétition est possible et l'ordre est important.

        On s'intéresse aux $8$-uplets de $E$. Il y a donc $10^8$ numéros possibles.

        Soit $F$ (respectivement $G$) l'ensemble des numéros commençant par $06$ (resp. par $09$). $F$ et $G$ sont disjoints, donc $\text{card}(F \cup G) = \text{card}(F)+\text{card}(G)=10^8+10^8=2\times 10^8$.
 
???- example "Exemple"
    Un immeuble est protégé par un digicode. Ce code peut être constitué de quatre, cinq ou six chiffres allant de 0 à 9, puis d'une lettre sélectionnée parmi les lettres $A,B$ et $C$. Combien de codes peut-on former avec ce système ?
 
    ???- done "Réponse"
        Notons $A_4$ (respectivement $A_5$, $A_6$) l'ensemble des codes à $4$ chiffres (resp. $5$ et $6$ chiffres) et d'une lettre.

        - $\text{card}(A_4)=\text{card}\left( \{0;1;2;3;4;5;6;7;8;9\}^4 \times \{ A;B;C\} \right) = 10^4 \times 3$
        - $\text{card}(A_5)=\text{card}\left( \{0;1;2;3;4;5;6;7;8;9\}^5 \times \{ A;B;C\} \right) = 10^5 \times 3$
        - $\text{card}(A_6)=\text{card}\left( \{0;1;2;3;4;5;6;7;8;9\}^6 \times \{ A;B;C\} \right) = 10^6 \times 3$

        L'ensemble de codes possibles est donc $A_4 \cup A_5 \cup A_6$.

        Comme $A_4,A_5$ et $A_6$ sont deux à deux disjoints, il y a $\text{card}(A _4 \cup A_5 \cup A_5) = \text{card}(A_4)+\text{card}(A_5)+\text{card}(A_6) = 3\ 333\ 000$ codes possibles.
 
 

## Nombre de p-uplets d'éléments *distincts* ou arrangement

!!!- info "Nombre d'arrangements"
    Le nombre de $p$-uplets d'éléments distincts d'un ensemble à $n$ éléments est $\dfrac{n!}{(n-p)!}$.


???- tip "Vocabulaire hors programme"
    Un $p$-uplets d'éléments **distincts** d'un ensemble à $n$ éléments s'appelle aussi *un arrangement de $p$ éléments parmi $n$*.


???- example "Exemple"
    Le tableau final d'un tournoi de judo féminin met en présence quinze athlètes. Le palmarès désigne la gagnante, ainsi que les $2^\text{e}$, $3^\text{e}$, $4^\text{e}$ et $5^\text{e}$ au classement final.
    
    Combien de palmarès différents peut-il exister ?
 
    ???- done "Réponse"
        Soit $E$ l'ensemble de 15 participants. Comme l'ordre est important et qu'un même participant ne peut pas occuper deux places différentes, on recherche le nombre de $5$-uplets d'éléments distincts parmi les 15 participants. Le nombre de palmarès est donc $\dfrac{15!}{(15-5)!}=15 \times 14 \times 13 \times 12 \times 11 = 360\ 360$.
 
 

???- example "Exemple"
    Dans le championnat de France de rugby, composé de 14 équipes, les six premières équipes qui ont le plus de points à la fin des matches aller-retour passent à la deuxième phase du championnat.

    1. Combien de classements composés des six équipes qui atteignent la deuxième phase sont possibles ?
    2. Lors de la saison 2018-2019, c'est le Stade Toulousain qui a fini premier de la phase régulière.  
    Combien de classements composés des six premières équipes de cette phase régulière étaient possibles alors possibles avec le Stade Toulousain en tête ?

 
    ???- done "Réponse"

        1. Comme il n'y a pas de répétitions et que l'ordre est important, il faut trouver le nombre de $6$-uplets parmi les 14 équipes : $\dfrac{14!}{(14-6)!}=14 \times 13 \times 12 \times 11 \times 10 \times 9 = 2\ 162\ 160$.
        2. Il ne reste que 13 équipes pour 5 places : $\dfrac{13!}{(13-5)!}=13 \times 12 \times 11 \times 10 \times 9 = 154\ 400$.

???- example "Exemple"
    Donner l'ensemble des $3$-uplets d'éléments distincts de l'ensemble $E=\{ a;b;c\}$.
 
    ???- done "Réponse"
        Il s'agit de $\{ (a;b;c); (a;c;b); (b;a;c); (b;c;a); (c;a;b); (c;b;a); \}$
 
 

!!!- info "Corollaire et définition"
    Un $n$-uplets d'éléments distincts d'un ensemble $E$ à $n$ éléments est **une permutation de $E$**. Le nombre de ces permutations est donc $n!$ (ce que confirme la formule $\dfrac{n!}{(n-n)!}=\dfrac{n!}{1}=n!$).

???- example "Exemple"
    Dans une classe de terminale, cinq élèves n'ont pas encore été évalués à l'oral. Dans combien d'ordre différents le professeur peut-il les interroger, chaque élève n'étant interrogé qu'une et une seule fois ?
    
    Combien y a-t-il de possibilités s'il n'a le temps d'interroger que trois d'entre eux ?
 
    ???- done "Réponse"
        Soit $E$ l'ensemble des 5 élèves. On cherche le nombre de permutations de $E$ qui est $5!=120$.
        
        On cherche par contre ici les $3$-uplets d'éléments distincts parmi les 5. Il y en a $\dfrac{5!}{(5-3)!}=5 \times 4 \times 3 = 60$.
-->
# Dénombrement : combinaison

## Nombre de parties ou combinaison d'un ensemble fini

On rappelle qu'une partie d'un ensemble est un sous-ensemble : il n'y a donc pas de répétition possible et l'ordre importe peu.

!!!- info "Nombre de parties"
    Soit $E$ un ensemble fini à $n$ éléments. Le nombre de parties de $E$ est $2^n$.

???- abstract "Démonsrtation"
    Soit $A$ une partie de $E$. Construire une telle partie c'est associé le nombre 1 aux éléments  de $E$ qui sont dans $A$ et $0$ aux autres. Il y a donc autant de parties de $E$ que de $n$-uplets de $\{0;1\}$


!!! info "Une combinaison"
    Soit $E$ un ensemble fini à $n$ éléments et $k$ un entier naturel inférieur ou égal à $n$. Une **combinaison** de $k$ éléments de $E$ est une partie de $E$ de cardinal $k$ (on parle alors de combinaisons de $k$ éléments parmi $n$).
    
    Une combinaison est un ensemble : il n'y a donc pas d'ordre et pas de répétitions.

!!!- info "Nombre de combinaison"
    Le nombre de combinaisons de $k$ ($0\leq k \leq n$) éléments parmi $n$ est noté $\comb{n}{k}$ et vaut $\dfrac{n!}{(n-k)!k!}$.

    \[
    \comb{n}{k} = \dfrac{n!}{(n-k)!k!} = \dfrac{\overbrace{n \times (n-1) \times (n-2) \times \ldots \times (n-k+1)}^{k \text{ facteurs }}}{k!}
    \]


???- example "Exemple"
    On dispose d'un jeu de $32$ cartes, toutes différentes. Une &\laquo; main &\raquo; de $4$ cartes est un ensemble de $4$ cartes dont l'ordre n'importe pas.
    
    Combien de &\laquo; mains &\raquo; de 4 cartes peut-on former ?
 
    ???- done "Réponse"
        Une &\laquo; main &\raquo; est une combinaison de $4$ éléments parmi $32$. il y a donc 

        \begin{eqnarray*}
        \comb{32}{4} & = & \dfrac{32!}{(32-4)!4!}\\
        & = & \dfrac{32!}{28!4!}\\
        & = & \dfrac{32 \times 31 \times 30 \times 29}{4 \times 3 \times 2 \times 1}\\
        & = & 35\ 960
        \end{eqnarray*}

 
 
!!! tip "Utilisation de la calculatrice"

    [![Calcul d'une combinaison](../Image/Comb.png){.Center_lien .VignetteMed }](../Image/Comb.png)

???- example "Exemple"
    Calculer sans calculatrice :

    1. $\comb{7}{3}$
    2. $\comb{12}{0}$
    3. $\comb{11}{1}$
    4. $\comb{6}{6}$
    5. $\comb{8}{7}$
    6. $\comb{20}{12}$ (Utilisez une calculatrice)

 
    ???- done "Réponse"
        
        1. $\comb{7}{3} = \dfrac{7!}{(7-3)!3!}=\dfrac{7 \times 6 \times 5}{3 \times 2 \times 1} = 35$
        2. $\comb{12}{0}=\dfrac{12!}{(12-0)!0!}=1$
        3. $\comb{11}{1}=\dfrac{11!}{(11-1)!1!}=11$
        4. $\comb{6}{6}=\dfrac{6!}{(6-6)!6!}=1$
        5. $\comb{8}{7}=\dfrac{8!}{(8-7)!7!}=8$
 

!!!- info "Cas particulier à retenir"
    Pour tout $n \in \N$:
 
    1. $\comb{n}{0}=\comb{n}{n}=1$
    2. $\comb{n}{1}=\comb{n}{n-1}=n$
    3. et pour tout $k \in \N$ tel que $0\leq k \leq n$ : $\comb{n}{k} = \comb{n}{n-k}$  (symétrie)

???- example "Exemple"

    1. En utilisant les résultats de l'exemple précédent, calculer $\comb{7}{4}$.
    2. Déterminer $\comb{5}{k}$ pour tout $k \in \N$, $0\leq k \leq 5$.

 
    ???- done "Réponse"

    1. $\comb{7}{4}=\comb{7}{7-3}=\comb{7}{3}=35$
    2. $\comb{5}{0}=\comb{5}{5}=1$, $\comb{5}{1}=\comb{5}{4}=5$  
    $\comb{5}{3}=\comb{5}{2}=\dfrac{5!}{(5-2)!2!}=\dfrac{5 \times 4}{2\times 1}=10$

 
 

!!!- info "Théorème : Relation de Pascal - Triangle de Pascal"
    Pour tout $n \in \N$ et pour tout $p \in \N$ tel que $0\leq p < n$:

    \[
    \comb{n-1}{p-1}+\comb{n-1}{p} = \comb{n}{p}
    \]

    Cette relation permet la construction du **triangle de Pascal** :

    [![Triangle de Pascal](../Image/TrianglePascal.png){.Center_lien .Vignette}](../Image/TrianglePascalgif.gif)



???- example "Exemple : Différentes situations classiques et dénombrement"
    Une urne contient 5 jetons numérotés de 1 à 5.
    
    1. On tire 3 jetons simultanément et on s'intéresse au numéro des jetons obtenus. Quel est l'univers ? Quel est le cardinal de cet univers ?
    2. On tire successivement 3 jetons sans remise et on s'intéresse au numéro des jetons obtenus. Quel est l'univers ? Quel est le cardinal de cet univers ?
    3. On tire 3 jetons avec remise et on s'intéresse au numéro des jetons obtenus. Peut-on énumérer l'univers ? Quel est le cardinal de cet univers ?

    ???- done "Réponse"
    
        <ol><li> $\Omega_S=\{ \{1,2,3\} ; \{1,2,4\} ; \{1,2,5\} ; \{1,3,4\} ; \{1,3,5\} ; \{1,4,5\} ; \{2,3,4\} ; \{2,3,5\} ; \{2,4,5\} ; \{3,4,5\} \}$.  
            Card$(\omega_S)=10$.  
            L'ordre n'a pas d'importance et la répétition n'est pas possible ! On retrouve le nombre de parties à 3 éléments de l'ensemble $\{1;2;3;4;5 \}$ qui est le nombre de combinaison de 3 parmi 5 : 

            \[
            \comb{5}{3} = \dfrac{5!}{(5-3)!3!} = \dfrac{5 \times 4 \times 3}{3 \times 2 \times 1} = 10
            \]

        </li><li>
            $\Omega_{sr} = \{$(1,2,3) ; (1,3,2) ; (2,1,3) ; (2,3,1) ; (3,1,2) ; (3,2,1) ;  
            (1,2,4) ; (1,4,2) ; (2,1,4) ; (2,4,1) ; (4,1,2) ; (4,2,1) ;  
            (1,2,5) ; (1,5,2) ; (2,1,5) ; (2,5,1) ; (5,1,2) ; (5,2,1) ;  
            (1,3,4) ; (1,4,3) ; (3,1,4) ; (3,4,1) ; (4,1,3) ; (4,3,1) ;  
            (1,3,5) ; (1,5,3) ; (3,1,5) ; (3,5,1) ; (5,1,3) ; (5,3,1) ;  
            (1,4,5) ; (1,5,4) ; (4,1,5) ; (4,5,1) ; (5,1,4) ; (5,4,1) ;  
            (2,3,4) ; (2,4,3) ; (3,2,4) ; (3,4,2) ; (4,2,3) ; (4,3,2) ;  
            (2,3,5) ; (2,5,3) ; (3,2,5) ; (3,5,2) ; (5,2,3) ; (5,3,2) ;  
            (2,4,5) ; (2,5,4) ; (4,2,5) ; (4,5,2) ; (5,2,4) ; (5,4,2) ;  
            (3,4,5) ; (3,5,4) ; (4,3,5) ; (4,5,3) ; (5,3,4) ; (5,4,3) $\}$
    
        Card$(\Omega_{sr})=60$. L'ordre est important et pas de répétition. On retrouve le nombre $3$-uplets d'éléments distincts de l'ensemble $E=\{1;2;3;4;5 \}$ qui est $\dfrac{5!}{(5-3)!}=5 \times 4 \times 3 =60$.

        </li><li> Cette fois, il y en a beaucoup ! Pour trouver son cardinal, il faut comprendre que l'on recherche le nombre de d'éléments de $E^3$, soit $5^3=125$.</li>
        </ol>
 

