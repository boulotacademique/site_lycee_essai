# Ensemble

## Vocabulaire

!!! info "Définition d'un ensemble"
    **Un ensemble** $E$ est une collection d'objets *distincts* $x$ qu'on appelle **éléments**.

    On dit alors $x$ appartient à $E$ et on le note $x \in E$.
    
    Le nombre d'éléments de $E$ s'appelle **le cardinal** de $E$ et se note $\text{card}(E)$.

???- example "Exemple"

    1. $E=\{a;b;c;d\}$ est un ensemble à 4 éléments. Donc $\text{card}(E)=4$.
    2. $\N$, $\Z$, $\R$ ou $\Q$ sont des ensembles de cardinal infini.
    3. L'ensemble vide noté $\emptyset$ est le seul ensemble qui ne contient aucun élément.


Lorsqu'un ensemble est décrit à l'aide de la collection de ses éléments, on dit qu'il est défini **en extension**. Dans ce cas, l'ordre n'a pas d'importance ( $\{a;b;c;d\} = \{b;d;a;c\}$ ) et il n'y a pas de répétition d'un élément.

!!! info "Partie d'un ensemble"
    On appelle **partie d'un ensemble** $\mathbf{E}$ (ou sous-ensemble de $E$) un ensemble $F$ tel que tous les éléments de $F$ appartiennent aussi à $E$.
    
    On dit alors que $F$ **est inclus** dans $E$ et on note $F \subset E$.

## Opération sur les ensembles

!!! info "Réunion d'ensembles"
    **La réunion** $\mathbf{A \cup B}$ de deux ensembles $A$ et $B$ est l'ensemble des éléments appartenant à $A$ ou (non exclusif) à $B$.

!!! info "Intersection d'ensembles"
    **L'intersection** $\mathbf{A \cap B}$ de deux ensembles $A$ et $B$ est l'ensemble des éléments appartenant à $A$ et $B$.

!!! info "Ensembles disjoints"
    Deux ensembles $A$ et $B$ dont l'intersection est vide sont dits **disjoints** et on écrit $A \cap B = \emptyset$.


!!! info "Complémentaire d'une partie"
    Soit $E$ un ensemble et $A$ une partie de $E$. On appelle **complémentaire de A dans E** et on note $\mathbf{\non{A}}$ l'ensemble qui contient tous les éléments de E *qui ne sont pas* dans $A$.

???- example "Exemple"
    Soit $A$ l'ensemble des nombres pairs entre $0$ et $20$ et $B$ l'ensemble des multiples de $3$ compris entre $0$ et $20$.

    1. Donner en extension les ensembles $A$ et $B$.
    2. Décrire en extension l'ensemble $C$ des multiple de $4$ compris enter $0$ et $20$. Est-ce une partie de $A$ ? de $B$ ?
    3. Décrire $A\cup B$.
    4. Décrire $A\cap B$. Que remarquez-vous ?
    5. Donner l'ensemble des éléments qui sont dans $B$ mais qui ne sont pas dans $A$. On note un tel ensemble $B\smallsetminus A$.

    ???- done "Solution"

        1. $A=\{0;2;4;6;8;10;12;14;16;18;20\}$ et $B=\{0;3;6;9;12;15;18 \}$
        2. $C=\{0;4;8;12;16;20\} \subset A$. Mais ce n'est pas une partie de $B$.
        3. $A \cup B=\{ 0;2;3;4;6;8;9;10;12;14;15;16;18;20 \}$
        4. $A\cap B = \{ 0;6;12;18 \}$. Il s'agit de l'ensemble des multiples de $2 \times 3$ compris entre $0$ et $20$.
        5. $B \smallsetminus A=\{3;9;15\}$


## Le principe additif

!!! info "Le principe additif"

    Si $A$ et $B$ sont deux ensembles finis et disjoints :
    
    \[
    \text{card}(A \cup B) = \text{card}(A)+\text{card}(B)
    \]

    Ce théorème se généralise : soient $E_1, E_2, \ldots, E_n$ $n$ ensembles **deux à deux disjoints** (i.e. pour tout $i$ tel que $1\leq i \leq n$ et pour tout $j$ tel que $1\leq j \leq n$ et $i\neq j$, $E_i \cap E_j = \emptyset$) :

    \[
    \text{card}(E_1 \cup E_2 \cup \ldots \cup E_n) = \text{card}(E_1) + \text{card}(E_2) +\ldots \text{card}(E_n)
    \]

!!! info "Conséquence immédiate"

    Soient $A$ une partie d'un ensemble $E$ fini et $\non{A}$ le complémentaire de $A$ dans $E$.
    
    \[
    \text{card}\left( \non{A} \right) = \text{card}(E)-\text{card}(A)
    \]


???- example "Exemple"
    Soit $A=\{2;3;5;7\}$ et $B=\{0;4;8;12;16\}$. Déterminer le cardinal de $A \cup B$.
 
    ???- done "Solution"
    
        Comme $A$ et $B$ sont disjoints, d'après le principe additif, card$(A \cup B)=\text{card}(A)+\text{card}(B)=4+5=9$



!!! info "Si $A$ et $B$ sont quelconques ... "
    Soit $A$ et $B$ deux ensembles, alors 
    
    \[
    \text{card}(A\cup B) = \text{card}(A) + \text{card}(B) - \text{card}(A \cap B)
    \]

## Le produit cartésien

!!! info "Un $\mathbf{p}$-uplet"
    On appelle **$\mathbf{p}$-uplet** ou **$\mathbf{p}$-liste** une collection **ordonnée** d'objets. Un $p$-uplet se note entre parenthèses. 

    Un 2-uplet s'appelle *un couple* et un 3-uplet *un triplet*. Par analogie à la géométrie repérée, on parle parfois de coordonnées (ou de composantes en physique).


???- example "Exemple"
    Soit $E=\{a;b;c\}$. Dresser l'ensemble de tous les 2-uplets à partir des éléments de $E$.
 
    ???- done "Solution" 
        Il s'agit de $\{(a;a),(a;b),(a;c),(b;a),(b;b),(b;c),(c;a),(c;b),(c;c)\}$.
  
 

!!! info "Le produit cartésien"
    $E,F$ et $G$ sont trois ensembles.
    
    - Le **produit cartésien de $\mathbf{E}$ par $\mathbf{F}$** est l'ensemble des *couples* $(a;b)$ où $a \in E$ et $b \in F$. Il est noté $E \times F$.

    \[
    E \times F = \{ (a;b) : a \in E \text{ et } b \in F \}
    \]

    - Le **produit cartésien $E\times F \times G$** est l'ensemble des *triplet* $(a;b;c)$ où $a \in E$, $b \in F$ et $c \in G$.

    \[
    E \times F \times G= \{ (a;b;c) : a \in E,\ b \in F \text{ et } c \in G \}
    \]

    - Le **produit cartésien $E_1 \times E_2 \times \ldots \times E_p$** de $p$ ensembles $E_1, E_2, \ldots , E_p$ est l'ensemble des *$p$-uplets* $(a_1;a_2; \ldots ; a_p)$ où $a_1 \in E_1,\ a_2 \in E_2, \ldots,\ a_p \in E_p$.
    
    \[
    E_1 \times E_2 \times \ldots \times E_p=\{ (a_1;a_2; \ldots ; a_p) : a_1 \in E_1,\ a_2 \in E_2, \ldots,\ a_p \in E_p \}
    \]

    
!!! tip "Notations"
    $E \times E$ est noté $E^2$ et $\underbrace{E \times E \times \ldots \times E}_{k \text{ fois}}$ est notée $E^k$.


## Le principe multiplicatif

!!! info "Le principe multiplicatif"
    $E_1, E_2, \ldots , E_p$ sont $p$ ensembles finis alors:

    \[
    \text{card}(E_1 \times E_2 \times \ldots \times E_p) = \text{card}(E_1) \times \text{card}(E_2) \times \ldots \text{card}(E_p)
    \]
    
    Cas particulier : si $E$ est un ensemble de cardinal $n$ et si $k \in \N^*$, alors card$(E^k)=n^k$.


???- example "Exemple"
    En informatique, un bit est un $0$ ou un $1$. Combien de mots de 4 bits existe-t-il ?
 
    ???- done "Solution" 
        Soit $E=\{0;1 \}$. On cherche le cardinal de $E^4$ qui est, d'après le principe multiplicatif, $2^4$.

???- example "Exemple"
    Soit deux ensembles $E =\{ a;b \}$ et $F=\{1;2;3;4 \}$. Déterminer le nombre d'éléments de $E \cup F$ et de $E \times F$.
 
    ???- done "Solution" 
        Comme $E$ et $F$ sont disjoints, donc, d'après le principe additif, card$(E \cup F)=\text{card}(E)+\text{card}(F)=2+4=6$.

        Par le principe multiplicatif, $\text{card}(E \times F) = \text{card}(E) \times \text{card}(F) = 2 \times 4 =8$
  
 

???- example "Exemple"
    Un restaurant propose un menu &laquo; plat + dessert &raquo;.
    
    Un client qui décide de prendre ce menu doit choisir un plat parmi les trois viandes et les deux poissons proposés, puis un dessert parmi les quatre desserts proposés.

    Déterminer le nombre de choix différents permettant de construire son menu.

    ???- done "Solution" 
        L'ensemble des viandes $V$ et des poissons $F$ sont disjoints et un plat se choisit dans l'ensemble $P=V \cup F$.
        
        Donc le nombre de plats différents est, d'après le principe additif, $3+2=5$.
        
        Le choix d'un menu est un couple du produit cartésien $P \times D$ (où $D$ est l'ensemble des desserts). Donc d'après le principe multiplicatif, $\text{card}(P \times D) = \text{card}(P) \times \text{card}(D)=5 \times 4=20$.
        
        Il y a donc 20 menus possibles.
  
## L'ensemble des parties d'un ensemble

!!! info "L'ensemble des parties"
    Soit $E$ un ensemble. **L'ensemble des parties** de $E$ se note $\mathcal{P}(E)$ et il contient toutes les parties de $E$ (ou tous les sous-ensembles de $E$).


!!! warning "Attention"
    Une évidence : $E \in \mathcal{P}(E)$ !

    De plus, l'ensemble vide est toujours un sous-ensemble d'un ensemble. 
    
    Ainsi $\mathcal{P}(E)$ n'est jamais vide puisque $\emptyset \in \mathcal{P}(E)$ et $E \in \mathcal{P}(E)$!

???- example "Exemple"
    Soit $E=\{ a;b;c\}$. Décrire $\mathcal{P}(E)$.
    
    ???- done "Solution"
        $\mathcal{P}(E) = \{ \emptyset, \{a\}, \{b\}, \{c\}, \{a,b\}, \{a,c\}, \{b,c\}, E\}$
