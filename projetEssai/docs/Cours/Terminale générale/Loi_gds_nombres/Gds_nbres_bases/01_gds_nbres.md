# Loi des grands nombres

## Variables aléatoires réelles

### Rappel

!!! info "Echantillon"
    Soit $X$ une vairable aléatoire définie sur l'univers $\Omega$. **Un échantillon de taille $n$ de la loi $X$** est une liste $(X_1,X_2, \ldots , X_n)$ de variables aléatoires indépendantes et identiques suivant la même loi que $X$.
 

!!! info "Variable aléatoire somme, moyenne"
    Dans cette situation, on s'intéresse souvent à **la variable aléatoire somme** $S_n$ définie précédemment (donc $S_n=X_1+X_2+\ldots+X_n$) mais aussi **la variable aléatoire moyenne** définie par $M_n = \dfrac{1}{n} S_n$.
 

### Variable aléatoire positive

!!! info "Varaible aléatoire réelle positive"
    Une **variable aléatoire réelle positive** $X$ définie sur l'univers $\Omega$ est une fonction définie sur $\Omega$ à valeurs dans $E \subset \R_+$ ($E$ est donc l'ensemble des images de $X$). Donc :

    \[
    \begin{array}{rccl}
    X\ :\ & \Omega & \rightarrow & E \subset \R_+\\
    & \omega & \mapsto & X(\omega)=x_i
    \end{array}
    \]

    Si on note $x_i$ un nombre de $E$ (les valeurs que peuvent prendre $X$), alors les $x_i$ sont positifs.
 

!!! info "Théorème : Inégalité de Markov"
    Soit $X$ une variable aléatoire réelle positive d'espérance $E(X)$. Alors, pour tout réel $a>0$, $\Pb(X \geq a) \leq \dfrac{E(X)}{a}$.

    Cette inégalité est appelée **l'inégalité de Markov.**
 

## Loi des grands nombres

### Inégalité de Bienaymé-Tchebychev

!!! info "Inégalité de Bienaymé-Tchebychev"
    Soit $X$ une variable aléatoire d'espérance $E(X)$ et de variance $V(X)$.

    Alors, pour tout réel $a>0$ , $\Pb\left( \left| X - E(X) \right| \geq a \right) \leq \dfrac{V(X)}{a^2}$.
 

???- abstract "Démonstration"
    Comme $a>0$, $\left| X - E(X) \right| \geq a$ équivaut à $\left[ X - E(X) \right]^2 \geq a^2$, c'est-à-dire que c'est le même ensemble des issues qui réalisent ces deux événements. 
    
    Donc $\Pb(\left| X - E(X) \right| \geq a) = \Pb(\left[ X - E(X) \right]^2 \geq a^2)$.

    Comme la variable $[X-E(X)]^2$ est positive. D'après l'inégalité de Markov : 
    
    \[
    \Pb\left( \left[ X - E(X) \right]^2 \geq a^2 \right) \leq \dfrac{E([X-E(X)]^2)}{a^2}
    \]

    Or, $E([X-E(X)]^2)=V(X)$. Donc $\Pb\left( \left[ X - E(X) \right]^2 \geq a^2 \right) \leq \dfrac{V(X)}{a^2}$.

    Donc $\Pb\left( \left| X - E(X) \right| \geq a \right) \leq \dfrac{V(X)}{a^2}$.
 

???- example "Exemple"
    Lors d'une saison de football, le nombre moyen de buts par match est de 2.5, avec une variance de 1.1.
    
    Majorer la probabilité que le match suivant ne se termine pas avec deux ou trois buts.
    
    ???- done "Réponse"
        Soit $X$ la variable aléatoire donnant le nombre de buts. On veut la probabilité que $X\leq 1$ ou $X \geq 4$. Cela revient donc à calculer $\Pb(|X-E(X)| \geq 1.5)$

        D'après l'inégalité de Bienaymé-Tchebytchev :

        $\Pb(|X-E(X)| \geq 1.5)\leq \dfrac{1.1}{1.5^2} < 0.49$
 
 

!!! info "Conséquence"
    Pour tout réel $a>0$ :

    \begin{eqnarray*}
    \Pb\left( \left| X - E(X) \right| \geq a \right) \leq \dfrac{V(X)}{a^2} %& \equivaut & \Pb\left( \left| X - E(X) \right| \geq a \right) \leq \dfrac{V(X)}{a^2} \\
    & \equivaut & \Pb\left( X \notin [E(X) - a ; E(X) + a] \right) \leq \dfrac{V(X)}{a^2} \\
    & \equivaut & \Pb\left( X \in ]E(X) - a ; E(X) + a[ \right) \geq 1-\dfrac{V(X)}{a^2} \\
    & \equivaut & \Pb\left( |X - E(X)|< a \right) \geq 1- \dfrac{V(X)}{a^2} 
    \end{eqnarray*}
 

???- example "Exemple"
    On lance $3\,600$ fois une pièce de monnaie non truquée. Soit $X$ la variable aléatoire qui associe à cette expérience le nombre de Pile obtenus.
    
    <ol>
    <li> Ecrire l'inégalité de Bienaymé-Tchebychev relative à la variable $X$.</li>
    <li> Minorer la probabilité que le nombre d'apparitions de Pile soit strictement compris entre $1600$ et $2000$.</li>
    </ol>
    
    ???- done "Réponse"
        <ol>
        <li> $X$ suit une loi binomiale de paramètres $n=3\,600$ et $p=0.5$. Donc $E(X)=1\,800$ et $V(X)=900$.

        D'après l'inégalité de Bienaymé-Tchebytchev :
        
        $\Pb(|X-1800| \geq a)\leq \dfrac{900}{a^2}$</li>
        <li> $X\in ]1600 ; 2000[ = ]1800-200 ; 1800+ 200[$, ce qui équivaut à $|X - 1800|<200$
        
        \begin{eqnarray*}
        \Pb(X\in ]1600 ; 2000[) & = & \Pb(|X - 1800|<200)  \\
        & = & 1 - \Pb(|X - 1800| \geq 200)
        \end{eqnarray*}
        
        D'après l'inégalité de Bienaymé-Tchebytchev :
        
        $\Pb(|X-1800| \geq 200)\leq \dfrac{900}{200^2}$
        
        Donc $1-\Pb(|X-1800| \geq 200) \geq 1 - \dfrac{9}{400}$ donc $\Pb(X\in ]1600 ; 2000[) \geq 0.9775$</li>
        </ol>

### L'inégalité de concentration

!!! info "Inégalité de concentration"
    Soit $M_n$ la variable aléatoire moyenne d'un échantillon de taille $n$ d'une variable aléatoire d'espérance $\mu$ et de variance $V$.

    Alors, pour tout réel $a>0$, on a $\Pb\left( |M_n - \mu| \geq a \right) \leq \dfrac{V}{n a^2}$.
    
    Cette inégalité est appelée **l'inégalité de concentration.**
 

???- example "Exemple"
    On effectue $n$ lancers successifs supposés indépendants d'une pièce équilibrée. On associe à chaque tirage $i$ la variable aléatoire $X_i$, prenant comme valeur $0$ si on obtient Face et $1$ sinon. On pose $S_n=X_1 + \ldots + X_n$ la variable aléatoire donnant le nombre de piles obtenus. On pose $M_n = \dfrac{S_n}{n}$, c'est donc ici la proportion (ou la fréquence) des piles.

    <ol>
    <li> Pour tout $i \in \N^*$, $i\leq n$, calculer $E(X_i)$ et $V(X_i)$.</li>
    <li> Ecrire l'inégalité de la concentration.</li>
    </ol>

 

## La loi faible des grands nombres

!!! info "La loi faible des grands nombres"
    Soit $M_n$ la variable aléatoire moyenne d'un échantillon de taille $n$ d'une variable aléatoire d'espérance $E(X)=\mu$ et de variance V.

    Alors pour tout réel $\delta>0$, on a : $\lim_{n \to +\infty} \Pb\left(|M_n-\mu| \geq 0 \right) = 0$.
 
