# Ordre et comparaison

## Définition et premières propriétés

Comparer donc deux réels $a$ et $b$, c'est chercher à savoir lequel est le plus grand, ou s'ils sont égaux.

!!! info "Définition" 
  Dire que $a \leq b$, c'est dire que $a - b\leq 0$. 


!!! info "Avec des signes"
	Si $a$ et $b$ sont positifs alors :

	<ul>
    <li> $a+b \geq 0$.</li>
    <li> $ab \geq 0$.</li>
    </ul>
	Si $a$ et $b$ sont négatifs alors :
	<ul>
    <li> $a+b \leq 0$.</li>
    <li> $ab \geq 0$.</li>
    </ul>
	Si $a$ et $b$ sont de signes contraires alors $ab \leq 0$.


## Règles de comparaison

### Ordre et addition.


!!! info "Ajouter ou soustraire un même nombre"
	Soient $a$ et $b$ deux réels, si $a \leq b$, alors $a + c \leq b + c$ et $a - c \leq b -c$.


    ???+ abstract "Démonstration"
	    $a+c -(b+c) = a-b \leq 0$


???+ example "Exercices"
    Soit deux réels $x$ et $y$ tels que $x<y$, comparer ces nombres sans faire de calculs et en précisant les règles utilisées :
	<ul>
    <li> $x+4$ et $y+4$</li>
    <li> $x-4$ et $y-4$</li>
    </ul>

!!! info "&laquo; passer de l'autre côté &raquo;"
	si $x + a \leq b$, alors $x+a-a \leq b-a$, d'où $x\leq b-a$.


!!! info "&laquo; Addition de &raquo; deux inégalités"
	Soient $a$ et $b$ deux réels. Si $a \leq b$ et $c \leq d$, alors $a+c\leq b+d$.


    ???+ abstract "Démonstration"
        $a \leq b\ \Leftrightarrow a-b\leq 0$ et $c \leq d \Leftrightarrow c-d \leq 0$. D'où :
       
        \[
        \begin{eqnarray*}
            (a-b)+(c-d)&\leq& 0\\
            a+c-(b+d) &\leq&0\\
            a+c&\leq&b+d
        \end{eqnarray*}
        \]

???+ example "Exercices"
	Soit deux réels $x$ et $y$ tels que $x<y$, comparer ces nombres sans faire de calculs et en précisant les règles utilisées :
	<ul>
    <li> $4$ et $3$</li>
    <li> $x+4$ et $y+3$</li>
    </ul>

???+ warning "Cela ne fonctionne pas avec une soustraction"
    Attention dans le théorème précédent, on ne parle que d'addition.

    Par exemple, $4\leq 5$ et $6\leq8$ mais $4-6 \geq 5-8$.

    ???+ tip "Méthode pour une soustraction"
        On a $-1 < x < 5$ et $−3 < y < 4$, encadrer : $x+y$, $x − y$.

        ???+ done "Solution"
            - Comme $-1 < x < 5$ et $−3 < y < 4$, d'après la règle sur l'addition : $−4 < x + y < 9$.
            - Comme $-1 < x < 5$ et $−3 < y < 4$  donc $-1 < x < 5$ et $−4 < −y < 3$. Ainsi, d'après la règle sur l'addition : $−5 < x − y < 8$.


???+ example "Exercices"
	Soit deux réels $x$ et $y$ tels que $x<y$, comparer ces nombres sans faire de calculs et en précisant les règles utilisées :
	<ul>
    <li> $4$ et $3$</li>
    <li> $x-3$ et $y-4$</li>
    </ul>

### Ordre et multiplication.


!!! info "Multiplication par une expression de signes constants !"
	Soient $a,b,c$ sont des réels.

	Si $a\leq b$ et $\mathbf{c > 0}$ alors $ac\leq bc$ et $\frac{a}{c} \leq \frac{b}{c}$.
	
	Si $a\leq b$ et $\mathbf{c < 0}$ alors $ac\geq bc$ et $\frac{a}{c} \geq \frac{b}{c}$.


!!! tip "En pratique"
	$-1<0$ donc $a \leq b$ implique $-a \geq -b$.
	
	Pour comparer deux nombres réels négatifs, on compare leur opposé.

???+ example "Exercices"
	Comparer ces nombres sans faire de calculs et en précisant les règles utilisées :
	<ul>
    <li> $-7$ et $-3$</li>
    <li> $-7 \times 4$ et $-3 \times 4$</li>
    <li> $-7 \times (-8)$ et $-3 \times (-8)$</li>
    <li> $-7 \times \frac{-1}{4}$ et $-3 \times \frac{-1}{4}$</li>
    </ul>

!!! info "&laquo;Produit de &raquo; deux inégalités"
	Si $a,b,c$ et $d$ sont des nombres réels **positifs** tels que $a \leq b$ et $c \leq d$ alors $ac \leq bd$.

???+ tip "Pas de signes constants"
    On a $0 < x < 5$ et $−3 < y < 4$, encadrer :  $xy$.

    ???+ done "Solution"
        Comme $0 < x < 5$ et $−3 < y < 4$, $0 < x < 5$ et $−3 < y \leq 0$ ou $0 < x < 5$ et $0 <y < 4$.

        \[
        \begin{array}{c|c|c}
        0 < x < 5 \text{ et } −3 < y \leq 0 &  & 0 < x < 5 \text{ et } 0 <y < 4 \\
        & & \text{D'après la règle sur la multiplication de réels positifs}\\
        0 < x < 5 \text{ et } 0 \geq −y < 3 & \text{ ou } & 0 < xy < 20 \\
        0 \leq −xy < 15 & \text{ ou } & 0 < xy < 20\\
        −15 < xy \leq 0 & \text{ ou } &  0 < xy < 20\\
        & −15 < xy < 20 & 
        \end{array}
        \]

### Passage au carré, à la racine carrée


!!! info "Au carré"
	$a$ et $b$ étant deux nombres **positifs**, $0 \leq a\leq b$ alors $a^2\leq b^2$; et réciproquement, si $a^2\leq b^2$ , alors $a\leq b$.

!!! warning "Et pour des nombres négatifs ?"
    $a$ et $b$ étant deux nombres **négatifs**, $a\leq b \leq 0$ alors $a^2\geq b^2$;

 

!!! info "Avec la racine carrée"
	$a$ et $b$ étant deux nombres **positifs**,$\sqrt{a} \leq \sqrt{b}$ équivaut à $a\leq b$.


???+ example "Exercices"
	Comparer ces nombres sans faire de calculs et en précisant les règles utilisées :
	<ul>
    <li> 0.38 et 1.05</li>
    <li> $0.38^2$ et $1.05^2$</li>
    </ul>

### Passage à l'inverse.


!!! info "Passage à l'inverse"
	$a$ et $b$ étant 2 nombres **strictement positifs**, $0 < a \leq b$ équivaut à $\frac{1}{a} \geq \frac{1}{b}$.

	$a$ et $b$ étant 2 nombres **strictement négatifs**, $a \leq b < 0$ équivaut à $\frac{1}{a} \geq \frac{1}{b}$.

!!! warning "Attention"
    Si $a$ et $b$ ne sont pas de même signes, alors le passage à l'inverse utilise simplement ... les signes.

    Si $a < 0 < b$, alors $\dfrac{1}{a} <0 < \dfrac{1}{b}$.

???+ example "Exercices"
	Comparer ces nombres sans faire de calculs et en précisant les règles utilisées :
	<ul>
    <li> $\pi$ et $3$.</li>
    <li> $\frac{1}{\pi}$ et $\frac{1}{3}$.</li>
    </ul>
 
### Comparaison des puissances de a

???+ example "Exercices"
	Comparer ces nombres sans faire de calculs et en précisant les règles utilisées :
	<ul>
    <li> $3$, $9$ et $27$.</li>
    <li> $\frac{1}{3}$, $\frac{1}{9}$ et $\frac{1}{27}$</li>
    </ul>


!!! info "Avec des puissances différentes"
	$a$ est un réel **strictement positif** :
	<ul>
    <li> si $a > 1$, alors $a^3 > a^2 > a$.</li>
    <li> si $0 < a < 1$, alors $a^3 < a^2 < a$.</li>
    </ul>


### Comparaison de fraction.

!!! info "Division et comparaison"
	Soit $c > 0$, si $a \leq  b$ alors :
	<ul>
    <li> $\frac{a}{c} \leq \frac{b}{c}$</li>
    <li> $\frac{c}{a} \geq \frac{c}{b}$</li>
    </ul>

    ???+ tip "Rappel de vos plus jeunes années"
        - Si deux fractions ont le même dénominateur, alors la fraction la plus grande est celle avec le plus grand numérateur.
        - Si deux fractions ont le même numérateur, alors la fraction la plus grande est celle avec le plus petit dénominateur.
	 

???+ example "Exemple"
	On considère deux réels $x$ et $y$ vérifiant $x < y<3$.
	<ul>
    <li>Démontrer l'inégalité $(x+y-6)(x-y)>0$.</li>
    <li>Développer $(x+y-6)(x-y)$.</li>
    <li>En déduire une comparaison des nombres $A$ et $B$ définis par :
    
    \[A=x^2-6x+1 \quad \text{et} \quad B=y^2-6y+1\]
    
    </li>
    </ul>


<!--# Manipulation d'encadrement


## Addition


<!--On cherche à encadrer $x+y$ sachant que :

On a donc indiqué dans le tableau ci-dessous les cas &laquo;extrêmes&raquo; pour
$2 \leq x \leq 15$ et $-5 \leq y \leq 3$.

Entourer le cas pour lequel $x+y$ sera le plus petit possible ainsi que le cas pour lequel $x+y$ sera le plus grand possible.

| | | | |  
|:---------------------:|:--------------------:|:----------------------:|:---------------------:|
|$x = 2$ et $y = −5$    |$x = 2$ et $y = 3$    |*x* = 15 et *y* = −5    |*x* = 15 et *y* = 3    |
|$x + y =$              |$x + y =$           |*x* + *y* =             |*x* + *y* =            | 


Bilan : on remarque que        $x+y$

On remarque que pour encadrer $x + y$, il suffit d'additionner membre à membre les 2 encadrements.-->

<!--
!!! info "Inégalité et addition"
    Si $a \leq x \leq b$ et $c \leq y \leq d$, alors $a+c \leq x+y \leq b+d$

    ???- abstract "Démonstration"
        Si $a  \leq x$ et $c \leq y$, alors $0 \leq x-a$ et $0 \leq y-c$. Or la somme de deux nombres positifs est positifs.

        Ainsi, $0\leq (x-a) + (y-c)$. D'où $0 \leq x+y -(a+c)$. Et donc $a+c \leq x+y$.




## Soustraction


On cherche à encadrer *x* − *y* sachant que :

Entourer le cas le plus défavorable ainsi que le cas le plus favorable.

  --------------------- -------------------- ---------------------- ---------------------
  *x* = 2 et *y* = −5   *x* = 2 et *y* = 3   *x* = 15 et *y* = −5   *x* = 15 et *y* = 3
  *x* − *y* =           *x* − *y* =          *x* − *y* =            *x* − *y* =
  --------------------- -------------------- ---------------------- ---------------------

Bilan : 

Peut-on soustraire membre à membre les 2 encadrements pour encadrer *x*
− *y* ?


## Multiplication


On cherche à encadrer *x* × *y* sachant que :

Entourer le cas le plus défavorable ainsi que le cas le plus favorable.

  --------------------- -------------------- ---------------------- ---------------------
  *x* = 2 et *y* = −5   *x* = 2 et *y* = 3   *x* = 10 et *y* = −5   *x* = 10 et *y* = 3
  *x* × *y* =           *x* × *y* =          *x* × *y* =            *x* × *y* =
  --------------------- -------------------- ---------------------- ---------------------

Bilan :

Peut-on multiplier membre à membre les 2 encadrements pour encadrer *x*
× *y* ?

Dans quel cas peut-on le faire ?


## Division


On cherche à encadrer sachant que :

Entourer le cas le plus défavorable ainsi que le cas le plus favorable.

  -------------------- -------------------- --------------------- ---------------------
  *x* = 2 et *y* = 1   *x* = 2 et *y* = 4   *x* = 16 et *y* = 1   *x* = 16 et *y* = 4
  =                    =                    =                     =
  -------------------- -------------------- --------------------- ---------------------

Bilan :

Peut-on diviser membre à membre les 2 encadrements pour encadrer ?

### Exemples


**ENONCE :** On a 0 \< *x* \< 5 et −3 \< *y* \< 4, encadrer : *x* + *y*,
*x* − *y*, *x*^2^ + *y*, *y*^2^ , *xy*.

**REDACTION :**

***Encadrement de** **x** **+** **y*** **:**

par (H) 0 \< *x* \< 5 et −3 \< *y* \< 4

donc −3 \< *x* + *y* \< 9

***Encadrement de** **x** **−** **y*** **:**

par (H) 0 \< *x* \< 5 et −3 \< *y* \< 4

donc 0 \< *x* \< 5 et −4 \< −*y* \< 3

donc −4 \< *x* − *y* \< 8

***Encadrement de** **x***^***2***^ ***+** **y*** **:**

par (H) 0 \< *x* \< 5 et −3 \< *y* \< 4

donc 0 \< *x*^2^ \< 25 et −3 \< *y* \< 4 (car la fonction carrée est
croissante sur 

donc −3 \< *x*^2^ + *y* \< 29

***Encadrement de** **y***^***2***^ **:**

par (H) −3 \< *y* \< 4

donc −3 \< *y* 0 ou 0 *y* \< 4

donc 0 *y*^2^ \< 9 ou 0 *y*^2^ \< 16 (car la fonction carrée est
décroissante sur


donc 0  *y*^2^ \< 16

***Encadrement de** **x** **y*** **:**

par (H) 0 \< *x* \< 5 et −3 \< *y* \< 4

donc (0 \< *x* \< 5 et −3 \< *y* 0) ou (0 \< *x* \< 5 et 0 *y* \< 4)

donc (0 \< *x* \< 5 et 0 −*y* \< 3) ou 0 *xy* \< 20

donc 0 −*xy* \< 15 ou 0 *xy* \< 20

donc −15 \< *xy* 0 ou 0 *xy* \< 20

donc −15 \< *xy* \< 20

exercices
=========

1.  0 \< *x* \< 5 et −10 \< *y* \< −2 encadrer *x* + *y* , *xy* , *y* −
    *x* , *x*^2^ + *y*^2^

2.  3 \< *x* \< 5 et 1 *y* \< 4 encadrer *x* − *y* , ,

3.  3 \< *x* \< 5 et − 3 \< *y* \< −1 encadrer , *xy* ,

4.  −2 \< *x* \< 5 et 1 *y* 3 encadrer (*x* + *y* + 1)^2^ , , *x*y ,
    *x*^2^

5.  --1 \< *x* \< 1 et 3 \< *y* \< 10 encadrer *xy* , *y*^2^ , *xy* +
    *y*^2^ , *x* + *y* , (*x* + *y*) *y*\
    Obtenez-vous le même encadrement pour *xy* + *y*^2^ et (*x* + *y*)
    *y* ?

6.  0 \< *x* \< 5 et 3 \< *y* \< 4 encadrer et

7.  3,1415 \< \< 3,1416 et 2,0 R 2,2 encadrer l'aire d'un disque de
    rayon R en arrondissant les bornes de l'encadrement à 0,1 près.
    -->