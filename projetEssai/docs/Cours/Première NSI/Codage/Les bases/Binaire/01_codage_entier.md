# Représentation d'entiers


## Introduction et histoire (En construction)

[Aspect historique](AFAIRE)


## Les briques de bases

!!! info "Définition"
    **Le bit** (pour *BInary digiT*) est l'unité la plus simple dans le système de numération binaire. Elle ne peut prendre que deux valeurs, désignées le plus souvent par les chiffres 0 et 1.
 

!!! info "Définition"
    Les bits sont regroupés par paquets adjacents pour représenter de l'information. En particulier, un regroupement de 8 bits s'appellent **un octet** (en anglais *bytes*).
 

???+ example "Exemple"
    Combien d'octet différents peut-on avoir ?\\
 

    ???+ done "Réponse"
        Il y a $2^8$ octets différents.
 
 

!!! info "Définition"
    **Un mot machine** est la quantité de bits standard manipulée par un microprocesseur. Sa taille diffère selon les processeurs : 8, 16, 32, 64 bits.

!!! info "Définition"
    Dans un octet (ou un mot machine), **le bit de poids fort** est le bit le plus à gauche (sur un nombre de bits précis) et **le bit de poids faible** est le bit le plus à droite.
 
## Ecriture d'un entier naturel dans une base quelconque

### Un exemple connu : la base 10

!!! info " "
    Tout entier $a \geq 0$ s'écrit de façon unique sous la forme : 
    
    \[
    a = a_0 + a_1 \times 10 + a_2 \times 10^2 + \ldots + a_n \times 10^n  = \sum_{i=0}^{n} a_i \times 10^i 
    \]

    où $n$ est un entier et les $a_i$ sont des entiers compris entre 0 et 10-1=9 et $a_n \neq 0$.

    On retrouve à travers ces coefficients l'écriture &laquo; naturelle &raquo; du nombre $a$.
 

???+ example "Exemple"
    Soit $a=2\,{\color{green}3}{\color{blue}0}{\color{red}5}$. Alors :
 
    \[
    2\,305 = {\color{red}5} + {\color{blue}0} \times 10 + {\color{green}3} \times 10^2 + 2 \times 10^3
    \]
 
 

!!! info "La division euclidienne"
    Soit $b$ un entier naturel non nul. Tout entier naturel $a$ s'écrit de manière unique sous la forme $a=b \times q +r$, avec $q$ un entier naturel et $0 \leq r <b$. 
    
    Les entiers $q$ et $r$ sont appelés respectivement **le quotient** et **le reste** de la division euclidienne de $a$ par $b$.
    
    On pourra aussi retenir que $a$ s'appelle *le dividende* et $b$ *le diviseur*.
 

???+ example "Exemple"
    Déterminer le quotient et le reste de la division euclidienne de $2\,305$ par $10$.

    ???+ done "Réponse"
        $2\,305 = 10 \times 230 + 5$.
        
        Donc le quotient est 230 et le reste est 5.

!!! tip "Poser une division euclidienne"
    On pose une division euclidienne de la façon suivante :

    [![Division euclidienne](../../Image/Im01.png){.Center_lien .Vignette}](../../Image/Im01.png)

???+ example "Exemple : trouver les chiffres qui composent un naturel"
    <ol>
    <li> Compléter le tableau suivant :

    <div class="Center_txt">

    | Dividende | $2305$ |  230 | ? | ? |
    |:---:|:---:|:---:|:---:|:---:|
    |Diviseur | 10 | 10 | 10 | 10|
    |Quotient | 230 | ? | ? | ? |
    |Reste | 5 | ? | ? | ? |

    </div>
    
    ???+ done "Réponse"

        <div class="Center_txt">

        | Dividende | 2305 |  230 | 23 | 2 |
        |:---:|:---:|:---:|:---:|:---:|
        | Diviseur | 10 | 10 | 10 | 10 |
        | Quotient | 230 | 23 | 2 | 0 |
        | Reste | 5 | 0 | 3 | 2 |

        </div>

    </li>
    <li> Que remarquez-vous à propos de la dernière ligne ?
 
    ???+ done "Réponse"
        Sur la dernière ligne, on retrouve les chiffres qui composent l'écriture décimale du nombre $2\,305$, mais il faut commencer la lecture du tableau par la droite.
    
    </li>
    <li> Vérifiez cette conjecture avec le nombre $12\,008$.
 
    ???+ done "Réponse"

        <div class="Center_txt">    

        | Dividende 	| 12008	|  1200 	| 120 	| 12 	|	1  |
        |:---:|:---:|:---:|:---:|:---:|:---:|
        | Diviseur 	| 10            | 10 			| 10 	| 10	| 	10 |
        | Quotient 	| 1200   | 120 			| 12 	|  1	|	0  |
        | Reste 		| 8 			| 0 			| 0 	|  2 	|	1  |

        </div>
    </li>
    </ol>
 

???+ tip "Présentation usuelle"
    Il est classique de rédiger cette méthode à l'aide de divisions euclidiennes successives.

    [![Division successive](../../Image/Im02.png){.Center_lien .VignetteTer}](../../Image/Im02.png)

### Un exemple indispensable : la base 2

!!! info " "
    Tout entier $a \geq 0$ s'écrit de façon unique sous la forme : 
    
    \[
    a = a_0 + a_1 \times 2 + a_2 \times 2^2 + \ldots + a_n \times 2^n  = \sum_{i=0}^{n} a_i \times 2^i
    \]

    où $n$ est un entier et les $a_i$ sont des entiers compris entre 0 et 2-1=1 et $a_n \neq 0$.\\
    On note alors $a=\overline{a_n a_{n-1} \ldots a_0}^2$ ou $a=\left( a_n a_{n-1} \ldots a_0 \right)_2$ et on appelle cette notation l'écriture binaire de $a$.
    

???+ example "Exemple"
    En utilisant la méthode du paragraphe précédent, donner l'écriture binaire de $114$.

    ???+ done "Réponse"
        <div class="Center_txt Pas_gris">

        |Dividende 	| 114	|  57	| 28 	| 14	|	7	| 3	| 1 |
        |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
        |Diviseur 	| 2		| 2		| 2 	| 2		| 	2	| 2	| 2 |
        |Quotient 	| 57	| 28	| 14 	|  7	|	3	| 1	| 0 |
        |Reste 		| 0		| 1		| 0 	|  0 	|	1	| 1	| 1 |

        D'où $114=0 + 1 \times 2 + 0 \times 2^2 + 0\times 2^3+ 1 \times 2^4 + 1 \times 2^5 + 1 \times 2^6$.
        Donc $114 = \base{1110010}$.

        </div>


!!! tip "Une autre façon de convertir un décimal en binaire"
    On peut utiliser la méthode suivante (surtout si on connaît à l'avance le nombre de chiffres qui composent l'écriture binaire) : 

    <div class="Center_txt Pas_gris">

 	| | 108	| 108 | 44 | ?	| ? | ? | ? | ? |
    |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
    |Puissance de $2$ | $2^7 = 128$ | $2^6=64$ | $2^5=32$ | $2^4=16$ | $2^3=8$ | $2^2=4$ | $2^1=2$ | $2^0=1$ |
    |Différence | $108-128<0$ | $108-64=44$	| ? | ? | ? | ? | ? | ? | 
    |Coefficient | 0 | 1 | ? | ? | ? | ? | ? | ? |
 
    </div>

    ???+ done "Réponse"

        <div class="Center_txt Pas_gris">

        | | 108	| 108 | 44 | 12	| 12 | 4 | 0 | 0 |
        |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
        |Puissance de $2$ | $2^7 = 128$ | $2^6=64$ | $2^5=32$ | $2^4=16$ | $2^3=8$ | $2^2=4$ | $2^1=2$ | $2^0=1$ |
        |Différence | $108-128<0$ | $108-64=44$	| $44-32=12$ | $12-16<0$ | $12-8=4$ | $4-4=0$ | $0-2<0$ | $0-1<0$ | 
        |Coefficient | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
    
        </div>

        D'où $108 = 1\times 2^6 + 1\times 2^5 + 0 \times 2^4 +1 \times 2^3 + 1 \times 2^2 + 0 \times 2 + 0$.

        Donc $108 = \left( 1101100 \right)_2$

???+ example "Exemple"
    Donner l'écriture binaire de $173$.
 
    ???+ done "Réponse"

        <div class="Center_txt Pas_gris">

        | |	173	  | 173   | 45   | 45    | 13  | 13  | 5   | 1   | 1 |
        |:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
        |Puissance de $2$  | $2^8=256$ | $2^7 = 128$ | $2^6=64$  | $2^5=32$  | $2^4=16$ | $2^3=8$ | $2^2=4$ | $2^1=2$ | $2^0=1$ |
        |Différence    | $173-256<0$ | $173-128=45$ | $45-64<0$  | $45-32=13$  | $13-16<0$ | $13-8=5$ | $5-4=1$ | $1-2<0$  | $1-1=0$ |
        |Coefficient   |  0  | 1    | 0    | 1    |  0  | 1   | 1   | 0   | 1 |

        </div>
 
        D'où $173 = 1\times 2^7 +0\times 2^6 + 1 \times 2^5 + 0 \times 2^4 + 1\times 2^3 + 1\times 2^2 + 0 \times 2 + 1$
        Donc $173 = \left( 1010\ 1101 \right)_2$
 
 


!!! tip "Convertir un binaire en décimal"
    À partir de $a=\left( a_n a_{n-1} \ldots a_0\right)_2$, on calcule : $a_0 + a_1 \times 2 + a_2 \times 2^2 + \ldots + a_n \times 2^n  = \displaystyle\sum_{i=0}^{n} a_i \times 2^i$.

    On peut aussi utiliser l'algorithme d'Hörner (cf exercice).
 

???+ example "Exemple"
    Déterminer le plus grand entier naturel qui puisse être codé :
    <ol>
    <li> si on utilise 4 bits</li>
    <li> si on utilise 1 octet</li>
    <li> si on utilise 2 bytes</li>
    </ol>

    ???+ done "Réponse"
        <ol>
        <li> On peut coder $2^4=16$ entiers. Ceux compris entre $0$ et $2^4-1=15$. Le plus grand entier codé sur 4 bits est donc $15$.</li>
        <li> Un octet contient 8 bits. On peut coder $2^8=256$ entiers. Ceux compris entre $0$ et $2^8-1=255$. Le plus grand entier codé sur un octet est donc $255$.</li>
        <li> Deux bytes contient 16 bits. On peut coder $2^{16}= 65\ 536$ entiers. Ceux compris entre $0$ et $2^{16}-1= 65\ 535$. Le plus grand entier codé sur 2 bytes est donc $65\ 535$.</li>
        </ol>
 
 

???+ example "Exemple"
    <ol>
    <li> Ecrire en décimal les nombres suivants écrits en binaire :
    <ol>
    <li> $a=\base{1101}$</li>
    <li> $a=\base{101110}$</li>
    </ol></li>
    <li> Que remarquez-vous entre la parité d'un nombre et son écriture binaire ?</li>
    </ol>

    
    ???+ done "Réponse"
        <ol>
        <li>
        <ol>
        <li> $a=\base{1101}=13$</li>
        <li> $a=\base{101110}=46$</li>
        </ol></li>
        <li> Si le nombre est pair, l'écriture binaire se termine par un $0$. Sinon, il se termine par un $1$.</li>
        </ol>
    
    
    </li>
    </ol>
 





### Un autre exemple indispensable : la base 16 }

\subsubsection{Conversion d'un décimal vers un hexadécimal.}
!!! info " "
Tout entier $a \geq 0$ s'écrit de façon unique sous la forme : 
\[ a = a_0 + a_1 \times 16 + a_2 \times 16^2 + \ldots + a_n \times 16^n  = \sum_{i=0}^{n} a_i \times 16^i \]
où $n$ est un entier et les $a_i$ sont des entiers compris entre 0 et 16-1=15 et $a_n \neq 0$.\\
Il faut donc 16 &laquo; chiffres &raquo; : $0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F$. Donc le chiffre $\left( A\right)_{16}$ vaut 10, $\left( B\right)_{16}$ vaut 11, \ldots $\left( F\right)_{16}$ vaut 15 !
 

\begin{att}
La deuxième méthode nécessite de connaître les puissances de 16.
\end{att}


???+ example "Exemple"
<ol>
<li> En utilisant la première méthode, donner l'écriture hexadécimale de $184$.
 
    ???+ done "Réponse"
\begin{center}
\begin{tabular}{|>{\centering}m{3cm}|*{4}{>{\centering}m{1cm}|}}
\hline
Dividende 	& $\np{35782}$	& $\np{2236}$	& 139 	& 8 \tabularnewline
\hline
Diviseur 	& 16			& 16			& 16 	& 16 \tabularnewline
\hline
Quotient 	& $\np{2236}$	& 139			& 8 	&  0 \tabularnewline
\hline
Reste 		& 6				& 12(=$C$)			& 11(=$B$)	&  8 \tabularnewline
\hline
\end{tabular}
\end{center}
D'où $\np{35782}=6 + 12\times 16 + 11 \times 16^2 + 8\times 16^3$.\\
Donc $\np{35782} = \base[16]{8BC6}$
 
</li>
<li> En utilisant la première méthode, donner l'écriture hexadécimale de $\np{42971}$.\\

 
    ???+ done "Réponse"
\begin{center}
\begin{tabular}{|>{\centering}m{3cm}|*{4}{>{\centering}m{1cm}|}}
\hline
Dividende 	& $\np{42971}$	& $\np{2685}$	& 167 	& 10 \tabularnewline
\hline
Diviseur 	& 16			& 16			& 16 	& 16 \tabularnewline
\hline
Quotient 	& $\np{2685}$	& 167			& 10 	&  0 \tabularnewline
\hline
Reste 		& 11(=$B$)		& 13(=$D$)		& 7		&  10(=$A$) \tabularnewline
\hline
\end{tabular}
\end{center}
D'où $\np{42971}=11 + 13\times 16 + 7 \times 16^2 + 10\times 16^3$.\\
Donc $\np{35782} = \base[16]{A7DB}$
 
</li>
</ol>
 

\subsubsection{Conversion d'un hexadécimal vers un décimal.}

!!! tip " "
Il suffit d'utiliser la définition ou l'algorithme d'Hörner (cf exercices).
 

???+ example "Exemple"
Donner l'écriture décimale des nombres suivants écrits en hexadécimal :
<ol>{4}
</li>
<li> $\base[16]{A2}$ \qquad \ans{162}
</li>
<li> $\base[16]{10}$ \qquad \ans{16}
</li>
<li> $\base[16]{C10}$ \qquad \ans{$\np{3088}$}
</li>
<li> $\base[16]{ABCD}$ \qquad \ans{$\np{43981}$}
</li>
</ol>
 

\vspace{-0.5cm}
\subsubsection{Passage entre l'hexadécimal et le binaire}

!!! tip " "[Méthode: du binaire vers l'hexadécimal]
À partir du nombre binaire, il suffit de former des paquets de 4 chiffres (en commençant par le bit de poids faible) et de convertir chaque paquet en hexadécimal.
 

???+ example "Exemple"
Convertir en hexadécimal les nombres suivants écrits en binaire :
<ol>
<li> $\base{101011}$\\
\begin{minipage}{0.5\linewidth}
$a=0010\ 1011$.\\
$\left( 10 \right)_2$ s'écrit en décimal $2$ qui s'écrit en hexadécimal $2$.\\
$\left( 1011 \right)_2$ s'écrit en décimal $11$ qui s'écrit en hexadécimal $B$.\\
Donc $\base{10\ 1011} = \left( 2B\right)_{16}$.
\end{minipage}
\begin{minipage}{0.5\linewidth}
\begin{center}
\begin{tabular}{|m{3cm}|c|c|}
\hline
Binaire 		& 10 	& 1011	\\
\hline
Pseudo décimal	& 2  	& 11	\\
\hline
Hexadécimal		& 2		& B\\
\hline
\end{tabular}
\end{center}
\end{minipage}
</li>
<li> $\base{10101110}$\\
\begin{comment}
\vspace{4cm}
\end{comment}
    ???+ done "Réponse"
$a=\base{1010\ 1110}$.\\
$\base{1010}$ s'écrit en décimal $10$, qui s'écrit en hexadécimal $A$.\\
$\base{1110}$ s'écrit en décimal $14$, qui s'écrit en hexadécimal $E$.\\
Donc $\base{1010\ 1110} = \base[16]{AE}$.
 
</li>
<li> $\base{111100011}$\\
\begin{comment}
\vspace{4cm}
\end{comment}
    ???+ done "Réponse"
$a=\base{0001\ 1110\ 0011}$.\\
$\base{1}$ s'écrit en décimal $1$, qui s'écrit en hexadécimal $1$.\\
$\base{1110}$ s'écrit en décimal $14$, qui s'écrit en hexadécimal $E$.\\
$\base{0011}$ s'écrit en décimal $3$, qui s'écrit en hexadécimal $3$.\\
Donc $\base{1010\ 1110} = \base[16]{1E3}$.
 
</li>
</ol>
 

!!! tip " "[Méthode: de l'hexadécimal vers le binaire]
À partir du nombre hexadécimal, il suffit de convertir chacun de ses chiffres en binaire \textbf{en utilisant 4 bits}.
 

???+ example "Exemple"
Convertir en binaire les nombres suivants écrits en hexadécimal :
<ol>[a)]
</li>
<li> $\base[16]{A1B}$\\
\begin{comment}
\vspace{4cm}
\end{comment}
    ???+ done "Réponse"
$a=A\ 1\ B$.\\
$\base[16]{A}$ s'écrit $10$ en décimal qui s'écrit $\base{1010}$.\\
$\base[16]{1}$ s'écrit $1$ en décimal qui s'écrit $\base{1}=\base{0001}$.\\
$\base[16]{B}$ s'écrit $11$ en décimal qui s'écrit $\base{1011}$.\\
Donc $\base[16]{A1B}=\base{1010\ 0001\ 1011}$.
 
</li>
<li> $\base[16]{1001}$\\
\begin{comment}
\vspace{4cm}
\end{comment}
    ???+ done "Réponse"
$a=\base[16]{1\ 0\ 0\ 1}$.\\
$\base[16]{1}$ s'écrit $1$ en décimal qui s'écrit $\base{1}=\base{0001}$.\\
$\base[16]{0}$ s'écrit $0$ en décimal qui s'écrit $\base{0}=\base{0000}$.\\
$\base[16]{0}$ s'écrit $0$ en décimal qui s'écrit $\base{0}=\base{0000}$.\\
$\base[16]{1}$ s'écrit $1$ en décimal qui s'écrit $\base{1}=\base{0001}$.\\
Donc $\base[16]{1001}=\base{0001\ 0000\ 0000\ 0001}$.
 
</li>
<li> $\base[16]{2AF3}$\\
\begin{comment}
\vspace{4cm }
\end{comment}
    ???+ done "Réponse"
$a=\base[16]{2\ A\ F\ 3}$.\\
$\base[16]{2}$ s'écrit $2$ en décimal qui s'écrit $\base{0010}$.\\
$\base[16]{A}$ s'écrit $10$ en décimal qui s'écrit $\base{1010}$.\\
$\base[16]{F}$ s'écrit $15$ en décimal qui s'écrit $\base{1111}$.\\
$\base[16]{3}$ s'écrit $3$ en décimal qui s'écrit $\base{0011}$.\\
Donc $\base[16]{2AF3}=\base{0010\ 1010\ 1111\ 0011}$.
 
</li>
</ol>
 %
%
%

\begin{rque}
L'écriture en hexadécimal d'un nombre binaire est beaucoup plus concise que son écriture binaire ! D'où son utilité.
 

### Le cas général }

!!! info " "
Soit $b$ un entier, $b\geq 2$.\\
Tout entier $a \geq 0$ s'écrit de façon unique sous la forme : 
\[ a = a_0 + a_1 \times b + a_2 \times b^2 + \ldots + a_n \times b^n  = \sum_{i=0}^{n} a_i \times b^i \]
où $n$ est un entier et les $a_i$ sont des entiers compris entre 0 et b-1 et $a_n \neq 0$.
 

Cf. la feuille d'exercice.

## Opération sur les binaires}

!!! tip " "
Pour ajouter deux nombres binaires, on procède comme en primaire, mais ne pas oublier que :
\begin{itemize}
</li>
<li> $\base{0}+\base{0}=\base{0}$
</li>
<li> $\base{0}+\base{1}=\base{1}$
</li>
<li> $\base{1}+\base{1}=\base{10}$ il y a donc une retenue !
\end{itemize}
 

\begin{att}
Comme les opérations sont effectuées sur un nombre de bits fini, il peut arriver ce que l'on appelle un \textbf{dépassement de capacité}.
\end{att}

???+ example "Exemple"
Sur un octet : $\base{0110\ 1001}+\base{1001\ 1110} = \base{0000\ 0111}$ (la dernière retenue est perdue). Ce qui conduit à $105+158 = 7$ !!!
 


!!! tip " "
Il est parfois indispensable d'inverser les $0$ et les $1$. Cela s'appelle &laquo; \textbf{le complément à un} &raquo;.
 

Nous croiserons à nouveau ces deux notions dans le chapitre sur les booléens.



%\begin{att}
%Addition\\ &laquo; complément &raquo; \\ Comparaison de binaire, ordre ?
%\end{att}

\begin{comment}
\clearpage
\end{comment}
## \'Ecriture d'un entier en base 2}

!!! tip " "[Méthode pour écrire un nombre négatif en binaire]
Soit un entier $a<0$, écrit en décimal.
\begin{itemize}
</li>
<li> Tenir compte (parfois déterminer) le nombre de bits à utiliser.
</li>
<li> Convertir en binaire la valeur absolue de $a$ en utilisant le nombre de bits nécessaire.
</li>
<li> faire le complément à 2 de ce nombre, c'est-à-dire :
\begin{itemize}
</li>
<li> Prendre le complément à un du nombre obtenu.
</li>
<li> Ajouter $1$ au nombre binaire trouvé précédemment. Le résultat obtenu est l'écriture en binaire de $a$.
\end{itemize}
\end{itemize}
 

%\clearpage

\begin{minipage}{\linewidth}
!!! info " "
On obtient donc :
\begin{center}
\begin{tabular}{|>{\centering}m{2cm}|*{5}{>{\centering}m{0.5cm}}|>{\centering}m{2cm}|}
\hline
\multirow{2}{*}{\begin{minipage}{1.8cm}\begin{center} Entiers\\ naturels \end{center}\end{minipage}} & \multicolumn{5}{>{\centering}m{4cm}|}{\begin{minipage}{\linewidth}\begin{center}Binaire\end{center}\end{minipage}} & \multirow{2}{*}{\begin{minipage}{1.8cm}\begin{center} Entiers\\ relatifs \end{center}\end{minipage}} \tabularnewline
   	&  	&	&	&	&	&		\tabularnewline
\hline
16	& 1 & 1 & 0 & 0 & 0 &  		\tabularnewline
\hline
15	&  	& 1 & 1 & 1 & 1	& -1	\tabularnewline
\hline
14	&  	& 1 & 1 & 1 & 0	& -2	\tabularnewline
\hline
13	&  	& 1 & 1 & 0 & 1	& -3	\tabularnewline
\hline
12	&  	& 1 & 1 & 0 & 0	& -4	\tabularnewline
\hline
11	&  	& 1 & 0 & 1 & 1	& -5	\tabularnewline
\hline
10	&  	& 1 & 0 & 1 & 0	& -6	\tabularnewline
\hline
9	&  	& 1 & 0 & 0 & 1	& -7	\tabularnewline
\hline
8	&  	& 1 & 0 & 0 & 0	& -8	\tabularnewline
\hline
7	&  	& 0 & 1 & 1 & 1	& 7		\tabularnewline
\hline
6	&  	& 0 & 1 & 1 & 0	& 6		\tabularnewline
\hline
5	&  	& 0 & 1 & 0 & 1	& 5		\tabularnewline
\hline
4	&  	& 0 & 1 & 0 & 0	& 4		\tabularnewline
\hline
3	&  	& 0 & 0 & 1 & 1	& 2		\tabularnewline
\hline
2	&  	& 0 & 0 & 1 & 0	& 2		\tabularnewline
\hline
1	&  	& 0 & 0 & 0 & 1	& 1		\tabularnewline
\hline
0	&  	& 0 & 0 & 0 & 0	& 0		\tabularnewline
\hline
\end{tabular}
\end{center}
\begin{itemize}
</li>
<li> Le nombre de bits à utiliser est un contrainte ! Mais $5$ codé sur 4 chiffres est \base{0101} et sur 8 chiffres \base{0000\ 0101}.
$-5$ codé sur 4 chiffres est \base{1011} et sur 8 chiffres \base{1111\ 1011}. Il suffit de répéter le chiffre le plus à gauche!
</li>
<li> L'addition &laquo; classique&raquo; fonctionne, à condition de ne pas tenir compte du 5ème bit (la dernière retenue).
\begin{center}
\begin{tabular}{*{5}{c}}
  & 0 & 0 & 1 & 0\\
+ & 1 & 1 & 1 & 0 \\
\hline
 {\tiny 1 }& 0 & 0 & 0 & 0
\end{tabular}
\end{center}
\end{itemize}
 
\end{minipage}

???+ example "Exemple"
\'Ecrire en binaire les entiers suivants :
<ol>
<li> $-35$ sur $8$ bits.\\
\begin{itemize}
</li>
<li> Cherchons l'écriture binaire sur $8$ bits de $35$.\\
\begin{comment}
\vspace{1cm }
\end{comment}
    ???+ done "Réponse"
$35 = 32 + 2 +1 =1 \times 2^5 + 0 \times 2^4 + 0 \times 2^3 + 0 \times 2^2 + 1 \times 2^1 + 1 \times 2^0$. Donc $\base[10]{35}=\base{10\ 0011}=\base{0010\ 0011}$.
 
</li>
<li> Prenons le complément à un :\\
\begin{comment}
\vspace{1cm }
\end{comment}
    ???+ done "Réponse"
On obtient $\base{1101\ 1100}$. 
 
</li>
<li> Ajoutons $1$. Conclusion ? Vérification ?\\
\begin{comment}
\vspace{4cm}
\end{comment}
    ???+ done "Réponse"
En ajoutant 1, on obtient $\base{1101\ 1101}$.
Donc l'écriture binaire de $-35$ est $\base{1101\ 1101}$.\\
Pour le vérifier, posons l'addition $35+(-35)$ :
\begin{center}
\begin{tabular}{*{9}{c}}
  			& 0 & 0 & 1 & 0 & 0 & 0 & 1 & 1 \\
+ 			& 1 & 1 & 0 & 1 & 1 & 1 & 0 & 1 \\
\hline
 {\tiny 1 }	& 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 
\end{tabular}
\end{center}
 
\end{itemize}
</li>
<li> $-35$ sur 2 octets.\\
\begin{comment}
\vspace{ 2cm}
\end{comment}
    ???+ done "Réponse"
Comme $-35$ s'écrit $\base{1101\ 1101}$ sur 8 chiffres, il s'écrit $\base{1111\ 1111\ 1101\ 1101}$ sur 16 chiffres.
 
</li>
<li> $-114$ sur 1 octet.\\
\begin{comment}
\vspace{ 3cm}
\end{comment}
    ???+ done "Réponse"
On a vu que $114 = \base{0111\ 0010}$.\\
Donc avec le complément à 1 : $\base{1000\ 1101}$\\
En ajoutant $1$ : $\base{1000\ 1110}$. Donc l'écriture binaire de $-114$ est $\base{1000\ 1110}$
 
</li>
</ol>
 

!!! tip " "[Méthode : convertir un binaire &laquo; négatif &raquo; en décimal]
\begin{itemize}
</li>
<li> Tenir compte du  (ou déterminer le) nombre $n$ de bits utilisés en binaire.
</li>
<li> Convertir le nombre binaire en décimal &laquo; comme si c'était un nombre positif &raquo; pour obtenir un nombre $d$
</li>
<li> Le nombre décimal recherché est $d-2^n$.
\end{itemize}
 

???+ example "Exemple"
Déterminer le nombre décimal correspondant
<ol>[a)]
</li>
<li> au binaire négatif $\base{1011}$ codé sur 4 bits.\\
\begin{comment}
\vspace{5cm }
\end{comment}
    ???+ done "Réponse"
\begin{itemize}
</li>
<li> $\base{1011}$ correspond à $11$ en décimal.
</li>
<li> donc le nombre recherché est $11-2^4=11-16=-5$
</li>
<li> Vérifions en calculant $5+(-5)$
\begin{center}
\begin{tabular}{*{5}{c}}
  			& 0 & 1 & 0 & 1\\
+ 			& 1 & 0 & 1 & 1 \\
\hline
 {\tiny 1 }	& 0 & 0 & 0 & 0
\end{tabular}
\end{center}
\end{itemize}
 
</li>
<li> au binaire négatif $\base{1010\ 1111}$ codé sur 8 bits.\\
 
    ???+ done "Réponse"
\begin{itemize}
</li>
<li> $\base{1010\ 1111}$ correspond à $175$ en décimal.
</li>
<li> donc le nombre recherché est $175-2^8=175-256=-81$
</li>
<li> Vérifions en calculant $81+(-81)$
\begin{center}
\begin{tabular}{*{9}{c}}
  			& 0 & 1 & 0 & 1 & 0 & 0 & 0 & 1 \\
+ 			& 1 & 0 & 1 & 0 & 1 & 1 & 1 & 1 \\
\hline
 {\tiny 1 }	& 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 
\end{tabular}
\end{center}
\end{itemize}
 
</li>
</ol>
 

???+ example "Exemple"
Quelles sont les entiers qui pourront être codés sur $8$ bits ?\\
\begin{comment}
\vspace{5cm }
\end{comment}
    ???+ done "Réponse"
On pourra convertir les entiers naturels qu'à la condition que le chiffre le plus à gauche reste un $0$. On commence donc à $\base{0000\ 0000}$ pour terminer à $\base{0111\ 1111}$. On peut donc convertir les entiers naturels compris entre $0$ et $2^7-1=127$.\\
Les entiers négatifs, eux, occuperont les nombres entre $\base{1000\ 0000}$ et $\base{1111\ 1111}$, soit entre $-128$ et $-1$.\\
Les entiers qui peuvent donc être écrit en binaire sur 8 bits sont les entiers compris entre $[-128;127]$. Ce qui fait $256$ valeurs.
 
 

\begin{obj}
\begin{itemize}
</li>
<li> Connaître le vocabulaire : bit, octet, bytes, bit de poids fort, bit de poids faible, complément à 1, complément à 2, dépassement de capacités
</li>
<li> Savoir convertir un entier naturel écrit dans une base (2, 10 ou 16) vers une autre base (2, 10, 16).
</li>
<li> Savoir calculer l'intervalle des entiers naturels qui peuvent être codés sur $n$ bits
</li>
<li> Connaître le principe pour écrire un entier naturel dans une base quelconque.
</li>
<li> Savoir convertir un entier relatif écrit dans une base (2 ou 10) vers une autre base (2 ou 10).
</li>
<li> Savoir étendre l'écriture en binaire d'un entier relatif sur un nombre de bits plus élevés
</li>
<li> Savoir calculer l'intervalle des entiers relatifs qui peuvent être codés sur $n$ bits
</li>
<li> Savoir poser une addition d'entiers relatifs écrits en binaires.
\end{itemize}
\end{obj}
