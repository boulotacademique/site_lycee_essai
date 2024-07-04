# Les réels pour un ordinateur

Représenter un réel dans un ordinateur est compliqué et **imprécis**! Une méthode qui fait cela est expliquée [ici](AFAIRE).

Dans un premier temps, il faut plutôt comprendre que cette imprécision à des conséquences. Conséquences qui impacteront vos programmes.

## La comparaison entre des réels 

Un test d'inégalité ($<, \leq, >, \geq$) entre réels est souvent nécessaire dans un programme (en particulier en math) ! Heureusement, ces tests ne posent pas de problèmes particuliers.

Par contre, un **test d'égalité** entre deux réels **est fortement déconséillé** (en pratique ne pas le faire) ! 

- En effet, si deux réels sont trop proches, leur représentation pour une machine pourrait bien être la même !
- Et si deux réels sont mathématiquement égaux, il est possible que leur représentation machine ne soit pas identique !

???+ example "Exemple"
    Voici quelques exemples de test d'égalité problématique :

    {{ IDE('Python_base_code/flottant_01', MAX = 1000) }} 

!!! danger "Attention"
    Ne jamais utiliser ```x == y``` ou ```x != y``` avec des réels ```x``` ou ```y```.

## Les opérations

Lors des opérations mathématiques sur les flottants, plusieurs phénomènes indésirables peuvent se produire.

### Le dépassement de capacité. 

Il y a deux types de dépassements :

- si le résultat est, en valeur absolue, trop grand, la machine retourne l'infini
- si le résultat est, en valeur absolue, trop petit, la machine retourne zéro


### L'absorption. 

Ajouter un très grand nombre avec un petit nombre, revient à ne garder que le grand nombre (qui va donc &laquo; absorber &raquo; le petit )

{{ IDE('Python_base_code/flottant_02', MAX = 1000) }} 

!!! warning "Une addition pas toujours commutative"
    En raison de ce phénomène, modifier l'ordre dans lequel est effectué une addition sur des réels peut modifier le résultat !

    Par exemple pour calculer $1 + \dfrac{1}{2} + \ldots + \dfrac{1}{10^5 - 1} + \dfrac{1}{10^5}$ et éviter le phénomène d'absorbtion, il est préférable d'effectuer le calcul de la façon suivante $\dfrac{1}{10^5} + + \dfrac{1}{10^5 - 1} + \ldots + \dfrac{1}{2} + 1$ !

    {{ IDE('Python_base_code/flottant_04', MAX = 1000) }} 

### L'annulation catastrophique.

Par exemple, $A=\sqrt{2}\left( 1 +10^{-14} \right)$ et $B=\sqrt{2}$. Donc $A-B=\sqrt{2} \times 10^{-14} \approx 1,414\ 213\ 562\ 373\ 095 \times 10^{-14}$. Et pourtant

{{ IDE('Python_base_code/flottant_03', MAX = 1000) }}  

Soit une erreur dès la deuxième décimale (de la mantisse) !!

Pour comprendre le phénomène, faisons l'opération sur des réels avec uniquement 16 chiffres après la virgule :

\[
M - m = 1,414\ 213\ 562\ 373\ 109 - 1,414\ 213\ 562\ 373\ 095 = 0,000\ 000\ 000\ 000\ 014 = 1,40 \times 10^{-14}
\]

