# Codage en héxadécimal

Voici une [adresse MAC](AFAIRE), c'est-à-dire un identifiant d'une carte réseau :

011110001101011011110000110000100001100001011101

Ceci est difficile à lire et encore plus difficile à écrire pour un humain.

Une première idée serait de découper cette suite de 0 et de 1 une suite de morceaux plus petit puis de convertir chaque morceau en décimal :

120:214:240:194:24:93

C'est plus facile à écrire, mais il est difficile convertir rapidement un octet binaire en un décimal. 

Mais il est possible d'avoir une base dans laquelle l'écriture est plus concise qu'un binaire et les calculs de conversion sont plus simples que ceux à effectuer pour obtenir un décimal : **il s'agit de la base 16** !

## Conversion d'un décimal vers un hexadécimal.

!!! info "Ecriture en base 16"
    Tout entier $a \geq 0$ s'écrit de façon unique sous la forme : 
    
    \[
    a = a_0 + a_1 \times 16 + a_2 \times 16^2 + \ldots + a_n \times 16^n  = \sum_{i=0}^{n} a_i \times 16^i
    \]

    où $n$ est un entier et les $a_i$ sont des entiers compris entre 0 et 16-1=15 et $a_n \neq 0$.

    Il faut donc 16 &laquo; chiffres &raquo; : $0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F$. Donc le chiffre $\left( A\right)_{16}$ vaut 10, $\left( B\right)_{16}$ vaut 11, $\ldots \left( F\right)_{16}$ vaut 15 !
 

???- tip "Autre méthode"
    La deuxième méthode nécessite de connaître les puissances de 16.

???- example "Exemple"
    <ol>
    <li> En utilisant la première méthode, donner l'écriture hexadécimale de $35\,782$.</li>
    <li> En utilisant la première méthode, donner l'écriture hexadécimale de $42\,971$.</li>
    </ol>

    
    ???- done "Réponse"

        <ol>
        <li>
        
        <div class="Center_txt Pas_gris">

        | Dividende | $35\,782$ | $2\,236$ | 139 | 8 |
        |:---:|:---:|:---:|:---:|:---:|
        |Diviseur  | 16 | 16 | 16 | 16 |
        |Quotient  | $2\,236$ | 139   | 8  |  0 |
        |Reste   | 6    | 12(=$C$)   | 11(=$B$) |  8 |

        </div>

        D'où $35\,782=6 + 12\times 16 + 11 \times 16^2 + 8\times 16^3$.
        
        Donc $35\,782 = \base[16]{8BC6}$

        </li>
        <li>
        

        <div class="Center_txt Pas_gris">

        |Dividende | $42\,971$ | $2\,685$ | 167  | 10 |
        |:---:|:---:|:---:|:---:|:---:|
        |Diviseur  | 16   | 16   | 16  | 16 |
        |Quotient  | $2\,685$ | 167   | 10  |  0 |
        |Reste   | 11(=$B$)  | 13(=$D$)  | 7  |  10(=$A$) |
        
        </div>

        D'où $42\,971=11 + 13\times 16 + 7 \times 16^2 + 10\times 16^3$.
        
        Donc $35\,782 = \base[16]{A7DB}$

        </li>
        </ol>


## Conversion d'un hexadécimal vers un décimal.

!!! tip "Hexadécimal en décimal"
    Il suffit d'utiliser la définition ou l'algorithme d'Hörner (cf exercices).
 

???- example "Exemple"
    Donner l'écriture décimale des nombres suivants écrits en hexadécimal :
    <ol>
    <li> $\base[16]{A2}$</li>
    <li> $\base[16]{10}$</li>
    <li> $\base[16]{C10}$</li>
    <li> $\base[16]{ABCD}$</li>
    </ol>
 
    ???- done "Réponse"
        <ol>
        <li> $\base[16]{A2}$ = 162</li>
        <li> $\base[16]{10}$ = 16</li>
        <li> $\base[16]{C10}$ = $3\,088$</li>
        <li> $\base[16]{ABCD}$ = $43\,981$</li>
        </ol>

## Conversion d'un binaire vers un hexadécimal.

!!! tip "Méthode : du binaire vers l'hexadécimal"
    À partir du nombre binaire, il suffit de former des paquets de 4 chiffres (en commençant par le bit de poids faible) et de convertir chaque paquet en hexadécimal.
 

???- example "Exemple"
    Convertir en hexadécimal les nombres suivants écrits en binaire :
    <ol>
    <li> $\base{101011}$</li>
    <li> $\base{10101110}$</li>
    <li> $\base{111100011}$</li>
    </ol>

    ???- done "Réponse"

        <ol>
        <li>
        $a=0010\ 1011$.

        $\left( 10 \right)_2$ s'écrit en décimal $2$ qui s'écrit en hexadécimal $2$.

        $\left( 1011 \right)_2$ s'écrit en décimal $11$ qui s'écrit en hexadécimal $B$.

        Donc $\base{10\ 1011} = \left( 2B\right)_{16}$.
        
        <div class="Center_txt Pas_gris">

        | Binaire   | 10  | 1011 |
        |:---:|:---:|:---:|
        | Pseudo décimal | 2   | 11 |
        | Hexadécimal  | 2  | B |

        </div>
        </li>
        <li>
        $a=\base{1010\ 1110}$.
    
        $\base{1010}$ s'écrit en décimal $10$, qui s'écrit en hexadécimal $A$.
        
        $\base{1110}$ s'écrit en décimal $14$, qui s'écrit en hexadécimal $E$.

        Donc $\base{1010\ 1110} = \base[16]{AE}$.
        </li>
        <li>
        $a=\base{0001\ 1110\ 0011}$.

        $\base{1}$ s'écrit en décimal $1$, qui s'écrit en hexadécimal $1$.
        
        $\base{1110}$ s'écrit en décimal $14$, qui s'écrit en hexadécimal $E$.
        
        $\base{0011}$ s'écrit en décimal $3$, qui s'écrit en hexadécimal $3$.
        
        Donc $\base{1010\ 1110} = \base[16]{1E3}$.
        </li>
        </ol>
    
 
## Conversion d'un hexadécimal vers un binaire.

!!! tip "Méthode: de l'hexadécimal vers le binaire"
    À partir du nombre hexadécimal, il suffit de convertir chacun de ses chiffres en binaire **en utilisant 4 bits**.
 

???- example "Exemple"
    Convertir en binaire les nombres suivants écrits en hexadécimal :
    <ol>
    <li> $\base[16]{A1B}$</li>
    <li> $\base[16]{1001}$</li>
    <li> $\base[16]{2AF3}$</li>
    </ol>
    
    ???- done "Réponse"

        <ol>
        <li>$a=A\ 1\ B$.
        
        $\base[16]{A}$ s'écrit $10$ en décimal qui s'écrit $\base{1010}$.
        
        $\base[16]{1}$ s'écrit $1$ en décimal qui s'écrit $\base{1}=\base{0001}$.

        $\base[16]{B}$ s'écrit $11$ en décimal qui s'écrit $\base{1011}$.

        Donc $\base[16]{A1B}=\base{1010\ 0001\ 1011}$.
        </li>
        <li>
        $a=\base[16]{1\ 0\ 0\ 1}$.
        
        $\base[16]{1}$ s'écrit $1$ en décimal qui s'écrit $\base{1}=\base{0001}$.
        
        $\base[16]{0}$ s'écrit $0$ en décimal qui s'écrit $\base{0}=\base{0000}$.
        
        $\base[16]{0}$ s'écrit $0$ en décimal qui s'écrit $\base{0}=\base{0000}$.
        
        $\base[16]{1}$ s'écrit $1$ en décimal qui s'écrit $\base{1}=\base{0001}$.

        Donc $\base[16]{1001}=\base{0001\ 0000\ 0000\ 0001}$.
        </li>
        <li>
        $a=\base[16]{2\ A\ F\ 3}$.
        
        $\base[16]{2}$ s'écrit $2$ en décimal qui s'écrit $\base{0010}$.
        
        $\base[16]{A}$ s'écrit $10$ en décimal qui s'écrit $\base{1010}$.
        
        $\base[16]{F}$ s'écrit $15$ en décimal qui s'écrit $\base{1111}$.
        
        $\base[16]{3}$ s'écrit $3$ en décimal qui s'écrit $\base{0011}$.
        
        Donc $\base[16]{2AF3}=\base{0010\ 1010\ 1111\ 0011}$.
        </li>
        </ol>
    
!!! tip "En pratique"
    En pratique, seule la conversion entre binaire et hexadécimal est utilisée !

    Revenons sur l'exemple initiale. En hexadécimal, l'adresse MAC 011110001101011011110000110000100001100001011101 se note 78:D6:F0:C2:18:5D
 

