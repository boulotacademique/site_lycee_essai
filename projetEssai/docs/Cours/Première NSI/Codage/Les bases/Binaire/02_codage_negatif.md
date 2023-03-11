# Codage d'entier négatif

## Opération sur les binaires

!!! tip " "
    Pour ajouter deux nombres binaires, on procède comme en primaire, mais ne pas oublier que :
    <ul>
    <li> $\base{0}+\base{0}=\base{0}$</li>
    <li> $\base{0}+\base{1}=\base{1}$</li>
    <li> $\base{1}+\base{1}=\base{10}$ il y a donc une retenue !</li>
    </ul>
 

!!! danger "Dépassement de capacité"
    Comme les opérations sont effectuées sur un nombre de bits fini, il peut arriver ce que l'on appelle un **dépassement de capacité**.

    ???- example "Exemple"
        Sur un octet : $\base{0110\ 1001}+\base{1001\ 1110} = \base{0000\ 0111}$ (la dernière retenue est perdue). Ce qui conduit à $105+158 = 7$ !!!
 


!!! tip "Le complément à 1"
    Il est parfois indispensable d'inverser les $0$ et les $1$. Cela s'appelle &laquo; **le complément à un** &raquo;.
 
Nous croiserons à nouveau ces deux notions dans le chapitre sur les booléens.

!!! danger "Le choix d'un bon codage"
    Pour coder un entier négatif, il y a plusieurs possibilités (en voir [un autre en exercice](AFAIRE)). Mais l'idéal serait d'avoir un codage qui permet de faire l'addition précédente (celle vue en primaire) entre un entier positif et un entier négatif.

## Ecriture d'un entier en base 2

!!! tip "Méthode pour écrire un nombre négatif en binaire"
    Soit un entier $a<0$, écrit en décimal.
    <ul>
    <li> Tenir compte (parfois déterminer) le nombre de bits à utiliser.</li>
    <li> Convertir en binaire la valeur absolue de $a$ en utilisant le nombre de bits nécessaire.</li>
    <li> faire le complément à 2 de ce nombre, c'est-à-dire :
    <ul>
    <li> Prendre le complément à un du nombre obtenu.</li>
    <li> Ajouter $1$ au nombre binaire trouvé précédemment. Le résultat obtenu est l'écriture en binaire de $a$.</li>
    </ul>
    </li>
    </ul>
 


???- example "Exemple"
    On obtient donc :

    <table class="AvecBordure">
    <tr><td> Entiers naturels </td> <td class="Center_txt" colspan="5">Binaire </td><td> Entiers relatifs </td></tr>
    <tr><td> 16 </td><td> 1 </td><td> 1 </td><td> 0 </td><td> 0 </td><td> 0 </td><td> </td></tr>
    <tr><td> 15 </td><td>   </td><td> 1 </td><td> 1 </td><td> 1 </td><td> 1 </td><td> -1 </td></tr>
    <tr><td> 14 </td><td>   </td><td> 1 </td><td> 1 </td><td> 1 </td><td> 0 </td><td> -2  </td></tr>
    <tr><td> 13 </td><td>   </td><td> 1 </td><td> 1 </td><td> 0 </td><td> 1 </td><td> -3  </td></tr>
    <tr><td> 12 </td><td>   </td><td> 1 </td><td> 1 </td><td> 0 </td><td> 0 </td><td> -4  </td></tr>
    <tr><td> 11 </td><td>   </td><td> 1 </td><td> 0 </td><td> 1 </td><td> 1 </td><td> -5  </td></tr>
    <tr><td> 10 </td><td>   </td><td> 1 </td><td> 0 </td><td> 1 </td><td> 0 </td><td> -6  </td></tr>
    <tr><td> 9 </td><td>   </td><td> 1 </td><td> 0 </td><td> 0 </td><td> 1 </td><td> -7  </td></tr>
    <tr><td> 8 </td><td>   </td><td> 1 </td><td> 0 </td><td> 0 </td><td> 0 </td><td> -8  </td></tr>
    <tr><td> 7 </td><td>   </td><td> 0 </td><td> 1 </td><td> 1 </td><td> 1 </td><td> 7   </td></tr>
    <tr><td> 6 </td><td>   </td><td> 0 </td><td> 1 </td><td> 1 </td><td> 0 </td><td> 6   </td></tr>
    <tr><td> 5 </td><td>   </td><td> 0 </td><td> 1 </td><td> 0 </td><td> 1 </td><td> 5   </td></tr>
    <tr><td> 4 </td><td>   </td><td> 0 </td><td> 1 </td><td> 0 </td><td> 0 </td><td> 4   </td></tr>
    <tr><td> 3 </td><td>   </td><td> 0 </td><td> 0 </td><td> 1 </td><td> 1 </td><td> 2   </td></tr>
    <tr><td> 2 </td><td>   </td><td> 0 </td><td> 0 </td><td> 1 </td><td> 0 </td><td> 2   </td></tr>
    <tr><td> 1 </td><td>   </td><td> 0 </td><td> 0 </td><td> 0 </td><td> 1 </td><td> 1   </td></tr>
    <tr><td> 0 </td><td>   </td><td> 0 </td><td> 0 </td><td> 0 </td><td> 0 </td><td> 0   </td></tr>
    </table>
    

     
!!! tip "Et si on change le nombre de bits utilisés ?"
    Le nombre de bits à utiliser est un contrainte ! Mais $5$ codé sur 4 chiffres est $\base{0101}$ et sur 8 chiffres $\base{0000\ 0101}$.

    $-5$ codé sur 4 chiffres est $\base{1011}$ et sur 8 chiffres $\base{1111\ 1011}$. Il suffit de répéter le chiffre le plus à gauche!

!!! info "Conséquence pour l'addition"
    L'addition &laquo; classique &raquo; fonctionne, à condition de ne pas tenir compte du 5ème bit (la dernière retenue).

    <div class="Center_txt">

    |   | 0 | 0 | 1 | 0 |
    |:---:|:---:|:---:|:---:|:---:|
    | + | 1 | 1 | 1 | 0 |
    | <span class="Tiny">1</span> | 0 | 0 | 0 | 0 |

    </div>


???- example "Exemple"
    Ecrire en binaire l'entier  $-35$ :
    <ol>
    <li>sur $8$ bits.
    <ul>
    </li>
    <li> Cherchons l'écriture binaire sur $8$ bits de $35$.
    ???- done "Réponse"
        $35 = 32 + 2 +1 =1 \times 2^5 + 0 \times 2^4 + 0 \times 2^3 + 0 \times 2^2 + 1 \times 2^1 + 1 \times 2^0$. Donc $\base[10]{35}=\base{10\ 0011}=\base{0010\ 0011}$.
    </li>
    <li> Prenons le complément à un :
    ???- done "Réponse"
        On obtient $\base{1101\ 1100}$. 
    </li>
    <li> Ajoutons $1$. Conclusion ? Vérification ?
    ???- done "Réponse"
        En ajoutant 1, on obtient $\base{1101\ 1101}$.  
        Donc l'écriture binaire de $-35$ est $\base{1101\ 1101}$.  
        Pour le vérifier, posons l'addition $35+(-35)$ :  
        <div class="Center_txt Pas_gris">  

        |    | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 |
        |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
        |+    | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 1 |
        | <span class="Tiny">1</span> | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  

        </div>
    </li>
    </ul>
    </li>
    <li> sur 2 octets.
    ???- done "Réponse"
        Comme $-35$ s'écrit $\base{1101\ 1101}$ sur 8 chiffres, il s'écrit $\base{1111\ 1111\ 1101\ 1101}$ sur 16 chiffres.
    </li>
    </ol>

???- example "Exemple"
    $-114$ sur 1 octet.

    ???- done "Réponse"
        On a vu que $114 = \base{0111\ 0010}$.

        Donc avec le complément à 1 : $\base{1000\ 1101}$.
        
        En ajoutant $1$ : $\base{1000\ 1110}$.
        
        Donc l'écriture binaire de $-114$ est $\base{1000\ 1110}$
    

!!! tip "Méthode : convertir un binaire &laquo; négatif &raquo; en décimal"
    <ul>
    <li> Tenir compte du  (ou déterminer le) nombre $n$ de bits utilisés en binaire.</li>
    <li> Convertir le nombre binaire en décimal &laquo; comme si c'était un nombre positif &raquo; pour obtenir un nombre $d$</li>
    <li> Le nombre décimal recherché est $d-2^n$.</li>
    </ul>
 

???- example "Exemple"
    Déterminer le nombre décimal correspondant
    <ol>
    <li> au binaire négatif $\base{1011}$ codé sur 4 bits.</li>
    <li> au binaire négatif $\base{1010\ 1111}$ codé sur 8 bits.</li>
    </ol>
    ???- done "Réponse"
        <ol>
        <li>
        <ul>
        <li> $\base{1011}$ correspond à $11$ en décimal.</li>
        <li> donc le nombre recherché est $11-2^4=11-16=-5$</li>
        <li> Vérifions en calculant $5+(-5)$  
        <div class="Center_txt Pas_gris">

        |    | 0 | 1 | 0 | 1|
        |:---:|:---:|:---:|:---:|:---:|
        |+    | 1 | 0 | 1 | 1 |
        |<span class="Tiny"> 1 </span> | 0 | 0 | 0 | 0 |

        </div>
        </li>
        </ul>
        </li>
        <li>
        <ul>
        </li>
        <li> $\base{1010\ 1111}$ correspond à $175$ en décimal.
        </li>
        <li> donc le nombre recherché est $175-2^8=175-256=-81$
        </li>
        <li> Vérifions en calculant $81+(-81)$
        <div class="Center_txt Pas_gris">  

        |    | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
        |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
        |+    | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 1 |
        |<span class="Tiny"> 1 </span> | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

        </div>
        </li>
        </ul>
        </ol>

 

???- example "Exemple"
    Quels sont les entiers (positifs et négatifs) qui pourront être codés sur $8$ bits ?

    ???- done "Réponse"
        On pourra convertir les entiers naturels qu'à la condition que le chiffre le plus à gauche reste un $0$. On commence donc à $\base{0000\ 0000}$ pour terminer à $\base{0111\ 1111}$. On peut donc convertir les entiers naturels compris entre $0$ et $2^7-1=127$.
    
        Les entiers négatifs, eux, occuperont les nombres entre $\base{1000\ 0000}$ et $\base{1111\ 1111}$, soit entre $-128$ et $-1$.
        
        Les entiers qui peuvent donc être écrit en binaire sur 8 bits sont les entiers compris entre $[-128;127]$. Ce qui fait $256$ valeurs.