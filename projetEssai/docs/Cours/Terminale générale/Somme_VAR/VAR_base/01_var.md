# Variables aléatoires


## Définition

Soit $\Omega$ l'univers des possibles d'une expérience aléatoire, et $\Pb$ une probabilité sur $\Omega$.

!!! info "Définition d'une variable aléatoire"
    Une **variable aléatoire réelle** $X$ définie sur l'univers $\Omega$ est une fonction définie sur $\Omega$ à valeurs dans $E \subset \R$ ($E$ est donc l'ensemble des images de $X$). Donc :
    
    \[
    \begin{array}{rccl}
    X\ :\ & \Omega & \rightarrow & E \subset \R\\
    & \omega & \mapsto & X(\omega)
    \end{array}
    \]

    Si on note $x_i$ un nombre de $E$ (les valeurs que peuvent prendre $X$), alors on définit la loi de probabilité de $X$ par $\Pb(X=x_i)=\Pb(A)$ où $A=\{ \omega \in \Omega\ : \ X(\omega)=x_i \}$.
    
    \[
    \Pb(X=x_i) = \sum_{x_i \in E} \Pb(\omega)
    \]
 


???- example "Exemple"
    On lance <span id="piece">une pièce de monnaie</span>. Si on obtient pile, on gagne 5 &#8364; et si on obtient face on gagne 2 &#8364;.

    On peut définir une variable aléatoire $X$ correspondant au gain obtenu en euro.

    $X$ est définie sur l'univers $\Omega=\{$ pile ; face $\}$ et $X($ pile $)=5$ et $X($ face $)=2$. Donc $E=\{ 2 ; 5\}$.

    Ici, la loi de probabilité est $\Pb(X=5)=\Pb($ pile $)=\dfrac{1}{2}$ et $\Pb(X=2)=\Pb($ face $)=\dfrac{1}{2}$.
 

???- example "Exemple"
    On lance $1$ dé tétraédrique équilibré. Un joueur doit payer $2$ &#8364; pour jouer. Si la face obtenue est paire, il ne gagne rien. Si la face vaut $1$, il gagne $2$ &#8364;. Dans tous les autres cas, il gagne $5$ &#8364;.
    
    On définit la variable aléatoire $X$  qui, à chaque épreuve, associe le gain algébrique du joueur.
    <ol>
    <li>Quelles sont les valeurs possibles pour $X$ ?</li>
    <li>Dresser la loi de probabilité de $X$.</li>
    </ol>
 

!!! info "Variable aléatoire indépendante"
    Deux variables aléatoires $X$ (à valeur dans $E_1$) et $Y$ (à valeur dans $E_2$) sont **indépendantes** si, pour toutes les valeurs $x_i \in E_1$ de $X$ et pour toutes les valeurs $y_j \in E_2$ de $Y$, $\Pb(X=x_i$ et $Y=y_j)=\Pb(X=x_i) \times \Pb(Y=y_j)$.

    De façon analogue : soient $X_1,X_2, \ldots , X_n$, $n$ variables aléatoires à valeurs dans respectivement $E_1,E_2, \ldots , E_n$ ; on dit que $X_1,X_2, \ldots , X_n$ sont indépendantes lorsque pour tout $x_1 \in E_1$, $x_2 \in E_2, \ldots , x_n \in E_n$ :

    \[
    \Pb( X_1 = x_1 \cap X_2 = x_2 \cap \ldots X_n = x_n ) = \Pb( X_1 = x_1 ) \times  \Pb( X_2 = x_2 ) \times \ldots \times  \Pb( X_n = x_n )
    \]
 

## Opérations sur des variables aléatoires indépendantes

### Multiplication par un réel

!!! info "Définition"
    Soit $X$ une variable aléatoire définie sur l'univers $\Omega$ et $a$ un nombre réel.

    On peut définir une variable aléatoire $Y$ telle que, pour tout élément $\omega \in \Omega$,  $Y(\omega) = a X(\omega)$.
    
    On note alors $Y=aX$.
    
    Si on note $x_i$ les valeurs possibles de $X$, alors $\Pb(Y=a x_i)=\Pb(X=x_i)$.


???- example "Exemple"
    Reprenons la situation [avec les pièces](#piece). Il est décidé d'augmenter les gains de $20\%$. Cela revient à multiplier les valeurs de $X(\omega)$ par $1.2$.
    
    Si on note $Y$ la variable aléatoire associée aux nouveaux gains, alors $Y=1.2X$.
 

### Somme de 2 variables aléatoires indépendantes.

!!! info "Définition"
    Soit $X$  (resp. $Y$) une variable aléatoire définie sur un univers fini $\Omega = \{ \omega_1,\omega_2, \ldots ,\omega_n \}$ (resp.  $\Omega' = \{ \omega'_1,\omega'_2, \ldots ,\omega'_n \}$). On note $x_i$ (resp. $y_i$) les valeurs possibles de $X$ (resp. $Y$).

    La somme des variables aléatoires $X$ et $Y$ est la variable aléatoire $S=X+Y$ qui prend toutes les valeurs $x_i+y_j$ pour tout $i$ et $j$.

    La loi de probabilité associée est alors $\Pb(S=s)=\Pb(A)$, où $A=\{X=x_i \text{ et } Y=y_j \ : \ x_i+y_j=s \}$.
    
    Donc $\Pb(S=s)$ est la somme de toutes les probabilités $\Pb\left( \{ X = x_i \} \cap \{ Y=y_j \} \right)$ tels que $x_i+y_j=s$. Comme **$X$ et $Y$ sont indépendantes** :

    \[
    \Pb(S =s) = \sum_{x_i+y_j=s} \left( \Pb(X=x_i)\times \Pb(Y=y_j) \right)
    \]
 

???- example "Exemple"
    Lors des réglages des machines, un contrôleur qualité d'une usine effectue de nombreux prélèvements dans la production et relève, pour chaque pièce, si elle a un défaut A, un défaut B.
    
    On note $X$ (resp. $Y$) la variable aléatoire qui compte le nombre de défaut A (resp. B). Voici le tableau des relevés :

    <div class = "Center2">

    |     | $Y=0$ | $Y=1$ | $Y=3$|
    |:---:|:-----:|:-----:|:----:|
    | X=0 | 0.07  | 0.18  | 0.17 |
    | X=1 | 0.15  | 0.20  | 0.23 |

    </div>

    On note $S$ la variable aléatoire somme : $S=X+Y$.
    
    Déterminer la loi de probabilité de $S$.
 

### Somme de $n$ variables aléatoires indépendantes

!!! info "définition"
    Soient $X_1, X_2, \ldots X_n$ $n$ **variables indépendantes**, on définit la variable aléatoire $S=X_1+X_2+\ldots+X_n$ d'une façon analogue :
    
    \[
    \Pb(S=s) = \sum_{x_1+x_2+\ldots + x_n=s} \left( \Pb(X_1= x_1) \times \Pb(X_2= x_2) \times \ldots \times \Pb(X_n= x_n) \right)
    \]
 

???- example "Exemple"
    Lors de la fabrication d'une pièce, 3 morceaux sont nécessaires. On s'intéresse au poids de ces pièces et on note $X_i$ la variable aléatoire qui, à la pièce $i$ associe  son poids.
    
    Voici la loi de probabilité de ces variables :

    <div class="Cote_tiers">

    |  k  |  20  | 25  | 30  |
    |:---:|:---:|:---:|:---:|
    | $\Pb(X_1 =k)$ | 0.15 | 0.75 | 0.1 |

    </div>
    <div class="Cote_tiers">

    |  k  |  15  | 20  | 25  |
    |:---:|:---:|:---:|:---:|
    | $\Pb(X_2 =k)$ | 0.2 | 0.6 | 0.2 |

    </div>
    <div class="Cote_tiers">

    |  k  |  25  | 30  | 35  |
    |:---:|:---:|:---:|:---:|
    | $\Pb(X_3 =k)$ | 0.1 | 0.85 | 0.05 |

    </div>


    On suppose que $X_1$, $X_2$ et $X_3$ sont indépendantes. Déterminer la loi de probabilité de $S=X_1+X_2+X_3$.
    
    ???- done "Réponse"
        $S$ peut prendre comme valeur $60,65,70,75,80,85,90$.

        $\Pb(S=60)=\Pb(X_1=20) \times \Pb(X_2=15) \times \Pb(X_3=25)=0.003$

        $\Pb(S=65)=\Pb(X_1=20)  \times \Pb(X_2=15) \times \Pb(X_3=30) + \Pb(X_1=25)  \times \Pb(X_2=15) \times \Pb(X_3=25)  + \Pb(X_1=20)  \times \Pb(X_2=20) \times \Pb(X_3=25) = 0.0495$.
 
 

???- example "Exemple : cas où les lois sont les mêmes"
    On lance 3 dés tétraédriques équilibrés et **de couleurs différentes**. On note $X_i$ le numéro affiché par le dé $i$ et on suppose que $X_1, X_2$ et $X_3$ sont indépendantes. Déterminer la loi de probabilité de $S=X_1+X_2+X_3$.
 

## Espérance et variance.

!!! info "Linéarité de l'espérance"
    Soient $X_1, X_2, \ldots, X_n$, $n$ variables aléatoires indépendantes et $a$ un réel, non nul.
    
    \[
    E(aX) = aE(X)
    \]

    \[
    E(X_1+X_2 + \ldots + X_n) = E(X_1) + E(X_2) + \ldots + E(X_n)
    \]

    On dit que l'espérance est linéaire.
 

!!! tip "Variable constante"
    Soit $X$ et $Y$ deux variables aléatoires indépendantes. Si pour tout $\omega$ de l'univers, $Y(\omega)=b \in \R^*$, on note $X+b$ pour $X+Y$. Donc $E(X+Y)=E(X+b)=E(X)+E(Y)=E(X)+b$.
 

!!! info "La variance n'est pas linéaire !"
    Soient $X_1, X_2, \ldots, X_n$, $n$ variables aléatoires indépendantes et $a$ un réel, non nul.
    
    \[
    V(aX) = a^2V(X)
    \]

    \[
    V(X_1+X_2 + \ldots + X_n) = V(X_1) + V(X_2) + \ldots + V(X_n)
    \]
 

!!! tip "Variable constante"
    Soit $X$ et $Y$ deux variables aléatoires indépendantes. Si pour tout $\omega$ de l'univers, $Y(\omega)=b \in \R^*$, on note $X+b$ pour $X+Y$. Donc $V(X+Y)=V(X+b)=V(X)+V(Y)=V(X)$.
 

???- warning "L'écart-type n'est pas linéaire !"
    Les formules précédentes ne fonctionnent pas pour l'écart-type :
    
    \[
    \sigma(aX) = |a|\sigma(X)
    \]

    \[
    \sigma(X_1+X_2 + \ldots + X_n) = \sqrt{\sigma(X_1)^2 + \sigma(X_2)^2 + \ldots + \sigma(X_n)^2}
    \]

## Echantillon d'une loi de probabilité

### Définition

!!! info "Définition"
    Soit $X$ une vairable aléatoire définie sur l'univers $\Omega$. **Un échantillon de taille $n$ de la loi $X$** est une liste $(X_1,X_2, \ldots , X_n)$ de variables aléatoires indépendantes et identiques suivant la même loi que $X$.
 

???- example "Exemple"
    Soit $X$ la variable aléatoire qui, <span id="bonbon">à chaque paquet de bonbons</span> issue d'une chaine de production, associe sa mass en grammes. On note $X_i$ la variable aléatoire qui, à chaque lot de 3 paquets, associe la masse du $i$-ème paquet.
    
    Les variables $X_1,X_2$ et $X_3$ sont indépendantes et suivent la même loi que $X$. Donc $(X_1,X_2,X_3)$ est un échantillon de taille 3 de la loi $X$.
 
!!! info "Définition"
    Dans cette situation, on s'intéresse souvent à la variable aléatoire somme $S_n$ définie précédemment (donc $S_n=X_1+X_2+\ldots+X_n$) mais aussi **la variable aléatoire moyenne** définie par $M_n = \dfrac{1}{n} S_n$.
 

???- example "Exemple"
    Avec l'exemple \ref{bonbon} et notant que la loi de $X$ est 

    <div class="Center2">

    |  k  | 490 | 500 | 505 |
    |:---:|:---:|:---:|:---:|
    |$\Pb(X=k)$ | 0.1 | 0.7 | 0.2 |

    </div>

    Donner la loi de probabilité de $S_3=X_1+X_2+X_3$ et de $M_3 = \dfrac{1}{3} S_3$, où $(X_1;X_2;X_3)$ est un échantillon de taille 3 de la loi $X$.
 

### Espérance, variance et écart-type de $S_n$ et $M_n$

!!! info " "
    Soit $S_n$ la variable aléatoire somme d'un échantillon de taille $n$ de la variable aléatoire $X$, alors 
    
    \[
    E(S_n) = nE(X) \qquad V(S_n) = nV(X) \qquad \sigma(S_n) = \sqrt{n} \sigma(X)
    \]
 

???- abstract "Démonstration"
    Soit $(X_1,X_2, \ldots , X_n)$ des variables aléatoires indépendantes et identiques suivant la même loi que $X$.

    \begin{eqnarray*}
    E(S_n) & = & E(X_1+X_2+\ldots+X_n) \\
    & = & E(X_1)+E(X_2)+\ldots+E(X_n)\\
    & = & E(X)+E(X)+\ldots+E(X) \text{ car ils suivent la même loi que } X\\
    & = & nE(X)
    \end{eqnarray*}

    \begin{eqnarray*}
    V(S_n) & = & V(X_1+X_2+\ldots+X_n) \\
    & = & V(X_1)+V(X_2)+\ldots+V(X_n)\\
    & = & V(X)+V(X)+\ldots+V(X) \text{ car ils suivent la même loi que } X\\
    & = & nV(X)
    \end{eqnarray*}

    Et $\sigma(S_n) = \sqrt{V(S_n)}= \sqrt{nV(X)} = \sqrt{n} \sigma(X)$.
 

!!! info " "
    Soit $S_n$ la variable aléatoire moyenne d'un échantillon de taille $n$ de la variable aléatoire $X$, alors 
    
    \[
    E(M_n) = E(X) \qquad V(M_n) = \frac{1}{n}V(X) \qquad \sigma(S_n) = \dfrac{\sigma(X)}{\sqrt{n}}
    \]
 

???- abstract "Démonstration"
    Soit $(X_1,X_2, \ldots , X_n)$ des variables aléatoires indépendantes et identiques suivant la même loi que $X$.

    \begin{eqnarray*}
    E(M_n) & = & E \left( \dfrac{1}{n} S_n \right) \\
    & = & \dfrac{1}{n} E(S_n) \\
    & = & \dfrac{1}{n}\times n \times E(X)\\
    & = & E(X)
    \end{eqnarray*}

    \begin{eqnarray*}
    V(M_n) & = & V\left( \dfrac{1}{n} S_n \right) \\
    & = & \dfrac{1}{n^2} V(S_n) \\
    & = & \dfrac{1}{n^2}\times n \times V(X)\\
    & = & \dfrac{1}{n} V(X)
    \end{eqnarray*}

    Et $\sigma(M_n) = \sqrt{V(M_n)}= \sqrt{\dfrac{1}{n} \times V(X)} = \dfrac{1}{\sqrt{n}} \sigma(x)$.
 

???- example "Exemple"
    En utilisant l'exemple sur [la fabrication des bonbons](#bonbon), déterminer l'espérance, la variance et l'écart-type de $S_3$ et $M_3$.
 

### Espérance et variance d'une loi binomiale

!!! info " "
    Soit $X$ une variable aléatoire suivant une loi binomiale de paramètre $n$ et $p$. Alors $E(X) = np$, $V(X)=np(1-p)$ et $\sigma(X)=\sqrt{np(1-p)}$.
 

???- abstract "Démonstration : démonstration au programme"
    $X$ est la somme de $n$ variables aléatoires indépendantes de Bernoulli $X_i$. Donc $X=X_1+X_2+\ldots+X_n$ où pour tout $i$, $X_i$ suit la même loi que celle de la variable aléatoire $Y$ de Bernoulli. 
    
    [Rappel du chapitre 5](../../Loi_binomiale/binom_bases/03_loi_binom.md#binom_esp), $E(Y)=p$ et $V(Y)=p(1-p)$.

    D'où $E(X)=nE(Y) = np$ et $V(X)=nV(Y)=np(1-p)$.

    Et $\sigma(X)=\sqrt{V(X)} = \sqrt{np(1-p)}$.
 

## Simulation et python

```python
import matplotlib.pyplot as mp
import random as rd
import scipy.special as sci

def expBern(p):
    nb=int(p*100)
    nbAlea=rd.randint(1,100)
    if nbAlea<=nb:
        return 1
    return 0

def schemaBern(n,p):
    L=[]
    for i in range(n):
        L.append(expBern(p))
    return L

def nbSuc(n,p):
    tot=0
    L=schemaBern(n,p)
    for i in range(len(L)):
        if L[i]==1:
            tot=tot+1
    return tot

def distribution(n,p,nbExp):
    L=[0]*(n+1)
    for i in range(nbExp):
        t=nbSuc(n,p)
        L[t]=L[t]+1
    return L

def binomFD(n,p,k):
    return sci.comb(n,k,exact=True)*p**k*(1-p)**(n-k)    

p=0.78
n=20
nbExp=100
L=distribution(n,p,nbExp)
listeAbs=[i for i in range(0,n+1) ]
LTheo=[nbExp*binomFD(n,p,i) for i in range(0,n+1)]
mp.plot(listeAbs,L,'r')
mp.plot(listeAbs,LTheo,'b')
mp.show()
```

