# Les réels pour un ordinateur

Représenter un réel dans un ordinateur est compliqué et **imprécis**! Une méthode qui fait cela est expliquée [ici](AFAIRE).

Dans un premier temps, il faut plutôt comprendre que cette imprécision à des conséquences. Conséquences qui impacteront vos programmes.

## La comparaison entre des réels 

Un test d'inégalité ($<, \leq, >, \geq$) entre réels est souvent nécessaire dans un programme (en particulier en math) ! Heureusement, ces tests ne posent pas de problème particulier.

Par contre, un test d'égalité entre deux réels **est fortement déconséillé** (en pratique ne pas le faire) ! 

- En effet, si deux réels sont trop proches, leur représentation pour une machine pourrait bien être la même !
- Et si deux réels sont mathématiquement égaux, il est possible que leur représentation machine ne soit pas identique !

