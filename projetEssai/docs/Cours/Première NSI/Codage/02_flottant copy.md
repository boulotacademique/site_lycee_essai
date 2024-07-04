# Codage des réels : les flottants

## Introduction 

Il existe des solutions pour représenter les réels de manière exacte en machine. Cependant, les contraintes de performance restreignent l’usage de ces méthodes au calcul formel. Les autres usages utilisent ainsi systématiquement **des représentations approximatives des réels**, qui sont les seules à remplir les exigences principales pour le calcul numérique, à savoir l’amplitude, la précision, et la performance.

**L’amplitude d’une représentation** correspond aux ordres de grandeur des nombres représentables. Il est nécessaire de pouvoir représenter à la fois des nombres très grands et très petits pour que les scientifiques s’y retrouvent.

**La précision d’une représentation** est encore plus importante que son amplitude. La précision correspond au nombre de chiffres significatifs qui peuvent être stockés.

**La performance** correspond à la rapidité avec laquelle les calculs peuvent s’effectuer. Il est en effet hors de question d’attendre l’éternité pour obtenir un résultat. Il s’agit aussi d’être performant sur toutes les machines couramment utilisées.

Il existe différentes familles de représentation des réels qui remplissent les critères d’amplitude, précision et performance, mais la plus utilisée est sans conteste **la représentation à virgule
flottante**.

## Notation scientifique

### En base 10

!!! note "Définition de l'écriture scientifique en base 10"
    Soit $x$ un décimal, c'est à dire un réel écrit en base 10. Il existe $M$ un décimal compris appartenant à $[1;10[$ et $e$ un entier tel que 
    
    \[
    x=signe(x) \times M \times 10^{e} 
    \]

    Cette notation s'appelle l'écriture scientifique du décimal $x$.

    $M$ sera appelé dans ce cours **la mantisse**.
 

???+ example "Exemple"
    <ul>
    <li> l'écriture scientifique de $251\ 354\ 001.2$ est $2.513\ 540\ 012e8$.</li>
    <li> l'écriture scientifique de $0.003\ 248\ 2$ est $3.248\ 2e-3$.</li>
    </ul>
 

En fait, l'écriture en base 10 d'un entier se généralise à un nombre décimal (et à un nombre rationnel) en base 10.

!!! info "Décomposition"
    Tout nombre décimal $d>0$ s'écrit sous la forme :

    \[
    d = a_n \times 10^n + a_{n-1} \times 10^{n-1} + \ldots + a_1 \times 10 + a_0 + a_{-1} \times 10^{-1} + \ldots + a_{-(p-1)} \times 10 ^{-(p-1)} + a_{-p} \times 10^{-p}
    \]

    avec $a_i$ ($i$ est un entier entre $-p$ et $n$) un entier entre 0 et 9.
 

???+ example "Exemple"
    <ul>
    <li> $521,013=5 \times 10^2 + 2 \times 10 + 1 + 0 \times 10^{-1}+1e-2 +3e-3$</li>
    <li> $0.003\ 015= 3e-3+0e-4+1e-5+5e-6$</li>
    </ul>
 

### En base 2

Le théorème précédent va nous permettre d'étendre la notion de nombre à virgule en binaire.

!!! note "Définition et méthode"

    \[
    \base{a_n a_{n-1} \ldots a_0,\,a_{-1} a_{-2} \ldots a_{-p}} = a_n \times 2^n + a_{n-1} \times 2^{n-1} + \ldots + a_1 \times 2 + a_0 + a_{-1} \times 2^{-1} + \ldots + a_{-(p-1)} \times 2 ^{-(p-1)} + a_{-p} \times 2^{-p}
    \]

    avec $a_i$ ($i$ est un entier entre $-p$ et $n$) un entier naturel entre 0 et 1.
    
    $\base{a_n a_{n-1} \ldots a_0,\,a_{-1} a_{-2} \ldots a_{-p}}$ est une écriture décimale en binaire.
 
???+ example "Exemple"
    
    <ul>
    <li> 
    
    $\base{101,0011} = 1 \times 2^2 + 0 \times 2 + 1 + 0 \times 2^{-1}+ 0 \times 2^{-2}+ 1 \times 2^{-3}+ 1 \times 2^{-4}$.
    
    Il représente donc le nombre décimal : $4+1+0.125+0.0625=5,1875$ 
    
    </li>
    <li> 
    
    $\base{1000,0101}$  $= 1 \times 2^3 + 0\times 2^2 +0 \times 2 + 0 + 0 \times 2^{-1}+ 1 \times 2^{-2}+ 0 \times 2^{-3}+ 1 \times 2^{-4}$.
    
    Il représente donc le nombre décimal : $8+0.25+0.0625=8.3125$.
    
    </li>
    </ul>
 

!!! note "Définition de l'écriture scientifique en base 2"
    Un décimal binaire en base 2 peut s'écrire sous la forme $x= signe(x) \times M \times 2^{e}$, où $M$ s'écrit $\base{1,a_{-1} \ldots a_{-p}}$ (c'est donc un réel dans l'intervalle $[1;2[$).

    Dans l'écriture $s \times M \times 2^{e}$ :
    <ul>
    <li> $M$ s'appelle la mantisse</li>
    <li> $e$ s'appelle l'exposant</li>
    </ul>
 

???+ example "Exemple"
    <ul>
    <li> $\base{101.0011}$ a pour écriture scientifique $1.010011 \times 2^{2}$.</li>
    <li> $\base{0.001011}$ a pour écriture scientifique  $1.011 \times 2^{-2}$}.</li>
    </ul>
 

C'est cette dernière forme qui sera utilisé pour stocker un un binaire au format **IEEE 754**.


!!! tip "Méthode pour convertir un décimal &laquo; en binaire à virgule&raquo;"
    On utilise la méthode avec les puissance de $2$ mais cette fois on continue avec les puissances négatives, aussi longtemps que nécessaire.


???+ example "Exemple"
    Donner l'écriture binaire de $2.625$.

    <div class="Center_txt Pas_gris">

    | | $2.625$ | $2.625$  | $0.625$ |  $0.625$ |  $0.125$  |  $0.125$  |
    |:---:|:---:|:---:|:---:|:---:|:---:|:---:|
    | Puissance de $2$ | $2^2=4$ | $2^1 = 2$  |  $2^0=1$ |  $2^{-1}=0.5$ |  $2^{-2}=0.25$ |  $2^{-3}=0.125$ | 
    | Différence | $2.625-4<0$ | $2.625-2=0.625$ |  $0.625-1<0$ |  $0.625-0.5=0.125$ |  $0.125-0.25<0$ |  $0.125-0.125=0$ | 
    | Coefficient | 0 | 1   |  0  |  1 |  0  | 1   |
    
    </div>
 
    D'où $2.625 = 1\times 2^1 +0 + 1 \times 2^{-1} + 0 \times 2^{-2} + 1\times 2^{-3}$
    Donc $2.625 = \base{ 10.101}$

 

???+ example "Exemple"
    <ol>
    <li> Donner l'écriture binaire de $0.2$ avec 8 chiffres après la virgule. Puis donner l'écriture scientifique.</li>
    <li> Donner l'écriture binaire de $0.1$ avec 8 chiffres après la virgule. Puis donner l'écriture scientifique.</li>
    <li> Donner l'écriture binaire de $0.3$ avec 8 chiffres après la virgule. Puis donner l'écriture scientifique.</li>
    <li> Donner l'écriture binaire de $\dfrac{1}{3}$ avec 8 chiffres après la virgule. Puis donner l'écriture scientifique.</li>
    </ol>
 
 
 
 
 
| | $0.2$ | $0.2$ | $0.2$ | $0.2$ | $0.075$ | $0.0125$ | $0.125$ | $0.125$  | $0.004\ 687\ 5$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Puissance de $2$ | $2^0$ | $2^{-1}$ | $2^{-2}$ | $2^{-3}$ | $2^{-4}$ | $2^{-5}$ | $2^{-6}$ | $2^-7$  | $2^{-8}$ |
| Différence | $<0$ | $<0$ | $<0$ | $0.075$ | $0.0125$ | $<0$ | $<0$ | $0.004\ 687\ 5$ | $0.00078125$ |
| Coefficient | 0 | 0  | 0  | 1 | 1  | 0  | 0  | 1   | 1 |
 
 
 
D'où $0.2 \approx 0 + 0 \times 2^{-1} + 0 \times 2^{-2} + 1\times 2^{-3}+ 1\times 2^{-4}+ 0\times 2^{-5}+ 0\times 2^{-6}+ 1\times 2^{-7}+ 1\times 2^{-8}$
Donc $0.2 \approx \base{0.00110011}$ qui s'écrit $1.10011 \times 2^{-3}$.



        | | $0.1$ | $0.1$ | $0.1$ | $0.1$ | $0.1$  | $0.037\ 5$ | $0.006\ 25$ | $0.006\ 25$ | $0.004\ 687\ 5$ | 
        |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
        | Puissance de $2$ | $2^0$ | $2^{-1}$ | $2^{-2}$ | $2^{-3}$ | $2^{-4}$ | $2^{-5}$ | $2^{-6}$  | $2^{-7}$  | $2^{-8}$ |
        | Différence | $<0$ | $<0$ | $<0$ | $<0$  | $0.037\ 5$ | $0.006\ 25$| $<0$  | $<0$   | $0.002\ 343\ 75$ |
        | Coefficient | 0 | 0  | 0  | 0 | 1  | 1  | 0   | 0   | 1 |
 
 
 
D'où $0.1 \approx 0 + 0 \times 2^{-1} + 0 \times 2^{-2} + 0\times 2^{-3}+ 1\times 2^{-4}+ 1\times 2^{-5}+ 0\times 2^{-6}+ 0\times 2^{-7}+ 1\times 2^{-8}$
Donc $0.1 \approx \base{0.00011001}$ qui s'écrit $1.1001 \times 2^{-4}$.


 
 
 
%\begin{tabular}{|>{\centering}m{1.5cm}|*{4}{>{\centering}m{1cm}|}*{5}{>{\centering}m{1.5cm}|}}
 
 
| | $0.3$ | $0.3$ | $0.3$ | $0.05$ | $0.05$ | $0.05$ | $0.018\ 75$ | $0.003\ 125$ | $0.
003\ 125$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Puissance de $2$ | $2^0$ | $2^{-1}$ | $2^{-2}$ | $2^{-3}$ | $2^{-4}$ | $2^{-5}$ | $2^{-6}$  | $2^{-7}$  | $2^{-8}$ |
| Différence | $<0$ | $<0$ | $0.05$ | $<0$  | $<0$ | $0.018\ 75$| $0.003\ 125$ | $<0$   | $<0$ |
| Coefficient | 0 | 0  | 1  | 0 | 0  | 1  | 0   | 0   | 0 |
 
 
 
D'où $0.3 \approx 0 + 0 \times 2^{-1} + 1 \times 2^{-2} + 0\times 2^{-3}+ 0\times 2^{-4}+ 1\times 2^{-5}+ 0\times 2^{-6}+ 0\times 2^{-7}+ 0\times 2^{-8}$
Donc $0.3 \approx \base{0.01001000}$ qui s'écrit $1.001 \times 2^{-2}$.


 
 
 
| | $\dfrac{1}{3}$ | $\dfrac{1}{3}$ | $\dfrac{1}{3}$ | $\dfrac{1}{12}$ | $\dfrac{1}{12}$ | $\dfrac{1}{48}$ | $\dfrac{1}{48}$ | $\dfrac{1}{192}$ | $0.003\ 125$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Puissance de $2$ | $2^0$  | $2^{-1}$  | $2^{-2}$  | $2^{-3}$  | $2^{-4}$  | $2^{-5}$  | $2^{-6}$  | $2^-7$  | $2^{-8}$ |
| Différence | $<0$  | $<0$  | $\dfrac{1}{12}$ | $<0$  | $\dfrac{1}{48}$ | $<0$   | $\dfrac{1}{192}$ | $<0$  | $\dfrac{61}{49\ 920}$ |
| Coefficient | 0   | 0   | 1   | 0 | 1   | 0   | 1   | 0   | 1 |
 
 
 
D'où $\dfrac{1}{3} \approx 0 + 0 \times 2^{-1} + 1 \times 2^{-2} + 0\times 2^{-3}+ 1\times 2^{-4}+ 0\times 2^{-5}+ 1\times 2^{-6}+ 0\times 2^{-7}+ 1\times 2^{-8}$.

Donc $\dfrac{1}{3} \approx \base{0.01010101}$ qui s'écrit $1.010101 \times 2^{-2}$.




## Virgule flottante - La norme **IEEE 754**

### Remarques préliminaires

\hspace{0.5cm} En informatique, un nombre à virgule flottante est tout simplement la donnée d’une mantisse et d’un exposant. Comme, il n’est pas simple de stocker efficacement des chiffres en base 10, les représentations à virgule flottante sont fondées sur la notation scientifique des nombres en base 2.

\hspace{0.5cm} Stocker un nombre à virgule flottante est très simple, car il suffit de stocker les chiffres (binaires) de la mantisse, son signe et l’exposant. Un seul bit suffit pour le signe, auquel on adjoint un certain nombre de bits pour stocker les chiffres de la mantisse et l’exposant. Il n’y a pas besoin d’utiliser d’astuces ou de structures de données compliquées.


\hspace{0.5cm} Combien de bits sont nécessaires pour obtenir une amplitude et une précision satisfaisantes ? Pour le savoir, revenons un peu sur les ordres de grandeur et rappelons que $2^{10} = 1024 \approx 10^3$. La notation scientifique d'un réel en base 2 est notée $s \times m \times 2^e$.\\
\underline{Pour satisfaire l’amplitude}, il faut stocker l’exposant, qui est un entier relatif. En calculant avec largesse, il suffit d’avoir quelques centaines d’entiers pour un exposant $e$ compris entre $-510$ et $510$ (dans la notation scientifique en base 2). En effet, on atteint alors des ordres de grandeurs entre $10^{-153}$ et $10^{153}$\footnote{$2^{510} =\lp 2^{10} \rp^{51} \approx \lp 10^3 \rp^{51} = 10^{153}$} . Une petite dizaine de bits suffit donc, car 10 bits permettent déjà de stocker $2^{10} = 1024$ valeurs.\\
\underline{Pour satisfaire la précision}, il faut stocker une petite quinzaine de chiffres en base 10. Cela
correspond à une précision de l’ordre de $10^{-15}$ (15 décimales) sur la mantisse, soit de l’ordre de $2^{-50}$ (50 bits de partie fractionnaire). Il faut donc environ 50 bits pour stocker la mantisse.\\

\hspace{0.5cm} Par ailleurs, comme l’exposant et la mantisse sont stockés indépendamment, l’ordre de grandeur (qui vient de l'exposant) n’a aucune influence sur la précision de la mantisse, ce qui est parfait pour les calculs mêlant divers ordres de grandeur. En somme, il suffit de quelques dizaines de bits pour stocker tout le nécessaire, c’est-à-dire la taille des mots machine usuels. Par conséquent, on arrive à obtenir assez facilement une représentation performante des réels.\\

\hspace{0.5cm} Le nombre et l’organisation exacte des bits formant un flottant sont définis dans ce qu’on appelle des formats (des normes) de nombres à virgule flottante. Il existe différents formats standards, dont le plus utilisé est un format binaire sur 64 bits (ou double précision). Pour des raisons de longueur d'écriture, nous traiterons plutôt des exemples avec un format binaire sur 32 bits (simple précision).

%+parler de la virgule fixe.\\
%+expliquer pourquoi le $e-127$
%{\color{red}Pourquoi ne pas avoir coder comme les négatifs l'exposant ? rep : on perd un bit et pas d'opération en général sur les exposant ?}



### La méthode

Notation : L'écriture d'un nombre scientifique d'un nombre binaire est donc $signe \times mantisse \times 2^{exposant}$.

Comme la mantisse pourra toujours s'écrire sous la forme $1,m$, on le notera $s \times 1,m \times 2^e$.

Pour le représenter, il faut coder ces éléments. On notera alors $c(s)$ le codage (en binaire) associé $s$, $c(m)$ celui associé à $m$ et $c(e)$ celui associé à $e$.


 

 
| | $c(s)$ | $c(e)$ | $c(m)$ | total | Décalage $d$ ou biais |
|:-:|:-:|:-:|:-:|:-:|:-:|
|Simple précision | 1 bit | 8 bits | 23 bits | 32 bits | 127 |
|Double précision | 1 bit | 11 bits | 52 bits | 64 bits | \np{1023}|
|Précision étendue | 1 bit | 15 bits | 64 bits | 80 bits | \np{16383} |
 

!!! tip "Organisation du codage"
    <ul>
    <li> Un bit pour le signe $0$ si le réel est positif, $1$ sinon. Donc $c(s)=0$ ou $c(s) = 1$.</li>
    <li> On écrit ensuite la valeur absolue du réel sous la forme d'un nombre binaire à virgule (avec autant de bits que nécessaires\footnotemark) $1,m \times 2^e$ avec $e$ compris entre $-d-1$ et $d$.</li>
    <li> Alors le code de l'exposant $c(e)$ se trouve avec la relation $\base[10]{c(e)}=e+d$. Comme $c(e)\geq 0$, on l'écrit en binaire comme un entier naturel sur le nombre de bits nécessaires.</li>
    <li> À partir de $1,m$, on trouve la mantisse (en base 2). On ne code pas le premier $1$. On conserve et/ou on rajoute des $0$ pour obtenir le nombre de chiffres qu'il faut (cf tableau plus haut)</li>
    <li> On range alors dans l'ordre (et sans les espaces !): 

    signe exposant mantisse 
    </li>
    </ul>


\footnotetext{cela dépend de la précision, mais aussi de la position du premier 1}

???+ example "Exemple"
    Convertir en binaire à virgule flottant selon la norme \textbf{IEEE 754}, les réels suivants :
    <ol>
    <li> $\base[10]{-5.375}$ en simple précision.</li>
    <li> $\base[10]{1039,0}$ (vu comme un réel) en simple précision.</li>
    </ol>


    ???+ done "Réponse"
        <ol>
        <li>
        <ul>
        <li> le bit de signe : $c(s)=1$.
        </li>
        <li> On écrit $5.375$ en nombre à virgule binaire. $5.375=1\times 2^2 + 0\times 2 + 1 + 0\times 2^{-1}+ 1\times 2^{-2}+ 1\times 2^{-3}$. Donc l'écriture scientifique est $1.01011 \times 2^2$.
        </li>
        <li> Donc $e=2$ et pour une simple précision le décalage est 127. D'où $\base[10]{c(e)}=2+127=129$. $129$ écrit en binaire sur un octet est $\base{c(e)}=1000\ 0001$
        </li>
        <li> De $1.01011$, on ne conserve que $01011$. On rajoute les $0$ pour avoir 23 bits (en simple précision). Donc la mantisse est $010\ 1100\ 0000\ 0000\ 0000\ 0000$.
        </li>
        <li> Donc $-5.375$ va s'écrire (sans les espaces) :
        \[ {\color{green!50!black}1}\ {\redP1000\ 0001}\ {\blu 010\ 1100\ 0000\ 0000\ 0000\ 0000} \]
        Rque : le découpage naturel en binaire est :$1100\ 0000\ 1010\ 1100\ 0000\ 0000\ 0000\ 0000$.\\
        Ce qui permettra d'écrire en hexadécimal : $C0\ AC\ 00\ 00 $
        </li>
        </ul>
        </li>
 
        <li>
        <ul>
        <li> le bit de signe : $c(s)=0$.
        </li>
        <li> On écrit $1039$ en nombre à virgule binaire. $1039=1024+8+4+2+1=1\times 2^{10}+1 \times 2^3+1 \times 2^2+1 \times 2+1=\base{100\ 0000\ 1111}$. Donc l'écriture scientifique est $1.0000001111 \times 2^{10}$.
        </li>
        <li> Donc $e=10$ et pour une simple précision le décalage est 127. D'où $\base[10]{c(e)}=10+127=137$. $137$ écrit en binaire sur un octet est $c(e)=1000\ 1001$
        </li>
        <li> De $1.0000001111$, on ne conserve que $0000001111$. On rajoute les $0$ pour avoir 23 bits (en simple précision). Donc la mantisse est $000\ 0001\ 1110\ 0000\ 0000\ 0000$.
        </li>
        <li> Donc $1039.0$ va s'écrire (sans les espaces) :
        \[ {\color{green!50!black}0}\ {\redP1000\ 1001}\ {\blu 000\ 0001\ 1110\ 0000\ 0000\ 0000} \]
        Rque : le découpage naturel en binaire est :$0100\ 0100\ 1000\ 0001\ 1110\ 0000\ 0000\ 0000$.\\
        Ce qui permettra d'écrire en hexadécimal : $44\ 81\ E0\ 00 $
        </li>
        </ul>
        </li>
        </ol>
 

 


\begin{att}
La norme IEEE 754 impose à certains codes une association. Il faut retenir qu'en simple précision :
<ul>
<li> Zéro : \[ {\color{green!50!black}?}\ {\redP0000\ 0000}\ {\blu 000\ 0000\ 0000\ 0000\ 0000\ 0000} \] est associé au 0 (zéro). C'est le code où il n'y a que des zéros (sauf pour le signe qui peut-être un 0 ou un 1).
</li>
<li> des nombres &laquo; dénormalisés &raquo;
\[ {\color{green!50!black}?}\ {\redP0000\ 0000}\ {\blu \text{au moins un bit à 1} } \]
Pour des nombres très petits !
</li>
<li> l'infini \[ {\color{green!50!black}?}\ {\redP1111\ 1111}\ {\blu 000\ 0000\ 0000\ 0000\ 0000\ 0000} \] est associé à l'infini. C'est le code où il n'y a que des uns pour l'exposant.
</li>
<li> Not a Number \[ {\color{green!50!black}1}\ {\redP1111\ 1111}\ {\blu \text{au moins un bit à 1}} \] est associé à \lstinline|NaN| (comme $0/0$, $\infty / \infty$, $\sqrt{-2}$ \ldots).
</li>
</ul>
\end{att}


\begin{rque}
En devoir, le tableau est fourni ! Mais il est possible de trouver le biais si on connaît le nombre de bit de l'exposant~!\\
En effet, si l'exposant est codé sur $n$ bits, alors on peut écrire  $2^n\ \ \ $} entiers naturels (de  $0\ $} à  $2^n-1\ \ $}). Comme deux codages de l'exposant sont réservés, il reste donc  $2^n-2 \ \ \ $} entiers naturels. Il faut donc les séparer en deux paquets de même effectif (un paquet pour les strictement négatifs et un paquet pour les positifs) qui auront donc chacun  $2^{n-1}-1\ \ \ $} entiers. On retrouve ici le biais !
\end{rque}

\begin{rque}
Vous pourrez vérifier votre codage en allant (par exemple) sur \url{http://www.binaryconvert.com/result_unsigned_int.html?decimal=049048051057}.
\end{rque}