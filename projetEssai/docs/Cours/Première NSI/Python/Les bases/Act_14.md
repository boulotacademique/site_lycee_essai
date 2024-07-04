# Python<br>Algorithme glouton

!!! question "Exercice - (EP 24-23-02)"
    On dispose d’un ensemble d’objets dont on connaît, pour chacun, la masse. On souhaite ranger l’ensemble de ces objets dans des boites identiques de telle manière que la somme des masses des objets contenus dans une boîte ne dépasse pas la capacité `c` de la boîte. On souhaite utiliser le moins de boîtes possibles pour ranger cet ensemble d’objets.  
    Pour résoudre ce problème, on utilisera un algorithme glouton consistant à placer chacun des objets dans la première boîte où cela est possible.  
    Par exemple, pour ranger dans des boîtes de capacité `c = 5` un ensemble de trois objets dont les masses sont représentées en Python par la liste `[1, 5, 2]`, on procède de la façon suivante :

    - Le premier objet, de masse 1, va dans une première boite.
    - Le deuxième objet, de masse 5, ne peut pas aller dans la même boite que le premier objet car cela dépasserait la capacité de la boite. On place donc cet objet dans une deuxième boîte.
    - Le troisième objet, de masse 2, va dans la première boîte.

    On a donc utilisé deux boîtes de capacité `c = 5` pour ranger les 3 objets.

    Compléter la fonction Python `empaqueter(liste_masses, c)` suivante pour qu’elle renvoie le nombre de boîtes de capacité `c` nécessaires pour empaqueter un ensemble d’objets dont les masses sont contenues dans la liste `liste_masses`.

    ```python linenums='1'
    def empaqueter(liste_masses, c):
        """Renvoie le nombre minimal de boîtes nécessaires pour
        empaqueter les objets de la liste liste_masses, sachant
        que chaque boîte peut contenir au maximum c kilogrammes"""
        n = len(liste_masses)
        nb_boites = 0
        boites = [ 0 for _ in range(n) ]
        for masse in ...: 
            i = 0
            while i < nb_boites and boites[i] + ... > c: 
                i = i + 1
            if i == nb_boites:
                ...
            boites[i] = ... 
        return ... 
    ```

    Exemples :

    ```python
    >>> empaqueter([1, 2, 3, 4, 5], 10)
    2
    >>> empaqueter([1, 2, 3, 4, 5], 5)
    4
    >>> empaqueter([7, 6, 3, 4, 8, 5, 9, 2], 11)
    5
    ``` 

!!! question "Exercice - (EP 24-45-02)"
On considère dans cet exercice un algorithme glouton pour le rendu de monnaie. Pour rendre une somme en monnaie, on utilise à chaque fois la plus grosse pièce possible et ainsi de suite jusqu’à ce que la somme restante à rendre soit nulle.  
Les pièces de monnaie utilisées sont :

`pieces = [1, 2, 5, 10, 20, 50, 100, 200]`

On souhaite écrire une fonction `rendu_monnaie` qui prend en paramètres 

- un entier `somme_due` représentant la somme à payer ;
- un entier `somme_versee` représentant la somme versée qui est supérieure ou égale à `somme_due` ;

et qui renvoie un tableau de type `list` contenant les pièces qui composent le rendu de la monnaie restante, c’est-à-dire de `somme_versee - somme_due`.

Ainsi, l’instruction `rendu_monnaie(452, 500)` renvoie le tableau `[20, 20, 5, 2, 1]`.

En effet, la somme à rendre est de `48` euros soit `20 + 20 + 5 + 2 + 1`.

Le code de la fonction `rendu_monnaie` est donné ci-dessous :

```python linenums='1'
def rendu_monnaie(somme_due, somme_versee):
    '''Renvoie la liste des pièces à rendre pour rendre la monnaie
    lorsqu'on doit rendre somme_versee - somme_due'''
    rendu = ... 
    a_rendre = ... 
    i = len(pieces) - 1
    while a_rendre > ...: 
        while pieces[i] > a_rendre:
            i = i - 1
        rendu.append(...) 
        a_rendre = ... 
    return rendu
```

Compléter ce code et le tester :

```python
>>> rendu_monnaie(700, 700)
[]
>>> rendu_monnaie(102, 500)
[200, 100, 50, 20, 20, 5, 2, 1]
``` 
