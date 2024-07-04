# Python<br>Les listes

!!! question "Exercice - 1 (EP 24-33-02)"

    Un nombre premier est un nombre entier naturel qui admet exactement deux diviseurs distincts entiers et positifs : 1 et lui-même.  
    Le crible d’Ératosthène permet de déterminer les nombres premiers plus petit qu’un certain nombre `n` fixé.  
    On considère pour cela un tableau `tab` de `n`booléens, initialement tous égaux à `True`, sauf `tab[0]` et `tab[1]` qui valent `False`, 0 et 1 n’étant pas des nombres premiers.  

    On parcourt alors ce tableau de gauche à droite.  

    Pour chaque indice `i` :

    - si `tab[i]` vaut `True` : le nombre `i` est premier et on donne la valeur `False` à toutes les
    cases du tableau dont l’indice est un multiple de `i`, à partir de `2*i` (c’est-à-dire `2*i`, `3*i` ...).

    - si `tab[i]` vaut `False` : le nombre `i` n’est pas premier et on n’effectue aucun
    changement sur le tableau. 

    On dispose de la fonction `crible`, incomplète et donnée ci-dessous, prenant en paramètre un
    entier `n` strictement positif et renvoyant un tableau contenant tous les nombres premiers plus
    petits que `n`.

    ```python linenums='1'
    def crible(n):
        """Renvoie un tableau contenant tous les nombres premiers
        plus petits que n."""
        premiers = []
        tab = [True] * n
        tab[0], tab[1] = False, False
        for i in range(n):
            if tab[i]:
                premiers.... 
                multiple = ... 
                while multiple < n:
                    tab[multiple] = ... 
                    multiple = ... 
        return premiers

    Exemples :

    >>> crible(40)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    >>> crible(5)
    [2, 3]
    ``` 


!!! question "Exercice (EP 24-32-01)"

    L'opérateur « ou exclusif » entre deux bits renvoie 0 si les deux bits sont égaux et 1 s'ils sont différents. Il est symbolisé par le caractère ⊕. Ainsi :

    - 0 ⊕ 0 = 0
    - 0 ⊕ 1 = 1
    - 1 ⊕ 0 = 1
    - 1 ⊕ 1 = 0

    Écrire une fonction `ou_exclusif` qui prend en paramètres deux tableaux de 0 ou de 1 de même longueur et qui renvoie un tableau où l’élément situé à position `i` est le résultat, par l’opérateur « ou exclusif », des éléments à la position `i` des tableaux passés en paramètres.

    ```python
    >>> ou_exclusif([1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 0, 1, 0, 0])
    [1, 1, 0, 1, 1, 0, 0, 1]
    >>> ou_exclusif([1, 1, 0, 1], [0, 0, 1, 1])
    [1, 1, 1, 0]
    ```

!!! question "Exercice - (EP 24-05-02)"
    L’ordre des gènes sur un chromosome est représenté par un tableau `ordre` de `n` cases d’entiers distincts deux à deux et compris entre 1 et `n`.  
    Par exemple, `ordre = [5, 4, 3, 6, 7, 2, 1, 8, 9]` dans le cas `n = 9`.  
    On dit qu’il y a un point de rupture dans `ordre` dans chacune des situations suivantes :

    - la première valeur de `ordre` n’est pas 1 ;
    - l’écart entre deux gènes consécutifs n’est pas égal à 1 ;
    - la dernière valeur de `ordre` n’est pas n.

    Par exemple, si `ordre = [5, 4, 3, 6, 7, 2, 1, 8, 9]` avec `n = 9`, on a

    - un point de rupture au début car 5 est différent de 1
    - un point de rupture entre 3 et 6 (l’écart est de 3)
    - un point de rupture entre 7 et 2 (l’écart est de 5)
    - un point de rupture entre 1 et 8 (l’écart est de 7)

    Il y a donc 4 points de rupture.  
    Compléter les fonctions Python `est_un_ordre` et `nombre_points_rupture` proposées à la page suivante pour que :

    - la fonction `est_un_ordre` renvoie `True` si le tableau passé en paramètre représente bien un ordre de gènes de chromosome et `False` sinon ;
    - la fonction `nombre_points_rupture` renvoie le nombre de points de rupture d’un tableau passé en paramètre représentant l’ordre de gènes d’un chromosome.

    ```python linenums='1'
    def est_un_ordre(tab):
        '''
        Renvoie True si tab est de longueur n et contient tous les
        entiers de 1 à n, False sinon
        '''
        n = len(tab)
        # les entiers vus lors du parcours
        vus = ... 

        for x in tab:
            if x < ... or x >... or ...: 
                return False
            ... .append(...) 
        return True

    def nombre_points_rupture(ordre):
        '''
        Renvoie le nombre de point de rupture de ordre qui représente 
        un ordre de gènes de chromosome
        '''
        # on vérifie que ordre est un ordre de gènes
        assert ... 
        n = len(ordre)
        nb = 0
        if ordre[...] != 1: # le premier n'est pas 1 
            nb = nb + 1
        i = 0
        while i < ...: 
            if ... not in [-1, 1]: # l'écart n'est pas 1 
                nb = nb + 1
            i = i + 1
        if ordre[i] != ...: # le dernier n'est pas n 
            nb = nb + 1
        return nb
    ```

!!! question "Exercice - (EP 24-08-01)"
    Le codage par différence (*delta encoding* en anglais) permet de compresser un tableau d’entiers dont les valeurs sont proches les unes des autres. Le principe est de stocker la première donnée en indiquant pour chaque autre donnée sa différence avec la précédente plutôt que la donnée elle-même.  
    On se retrouve alors avec un tableau de données plus petit, nécessitant moins de place en mémoire. Cette méthode se révèle efficace lorsque les valeurs consécutives sont proches.  
    Programmer la fonction `delta(liste)` qui prend en paramètre un tableau non vide de nombres entiers et qui renvoie un tableau contenant les valeurs entières compressées à l’aide cette technique.

    Exemples :

    ```python
    >>> delta([1000, 800, 802, 1000, 1003])
    [1000, -200, 2, 198, 3]
    >>> delta([42])
    [42] 
    ```

!!! question "Exercice - (EP 24-19-01)"
    On rappelle que :

    - le nombre $a^n$ est le nombre $a \times a \times a \times \dots \times a$, où le facteur $a$ apparaît $n$ fois,
    - en langage Python, l’instruction `t[-1]` permet d’accéder au dernier élément du tableau `t`.

    Dans cet exercice, l’opérateur ```**```  et la fonction `pow` ne sont pas autorisés.  
    Programmer en langage Python une fonction `liste_puissances` qui prend en arguments un nombre entier `a`, un entier strictement positif `n` et qui renvoie la liste de ses puissances $\rm{[a^1, a^2, ..., a^n]}$.  
    Programmer également une fonction `liste_puisssances_borne` qui prend en arguments un nombre entier `a` supérieur ou égal à 2 et un entier `borne`, et qui renvoie la liste de ses puissances, à l’exclusion de $\rm{a^0}$, strictement inférieures à `borne`.

    Exemples :

    ```python
    >>> liste_puissances(3, 5)
    [3, 9, 27, 81, 243]
    >>> liste_puissances(-2, 4)
    [-2, 4, -8, 16]
    >>> liste_puissances_borne(2, 16)
    [2, 4, 8]
    >>> liste_puissances_borne(2, 17)
    [2, 4, 8, 16]
    >>> liste_puissances_borne(5, 5)
    []
    ```

!!! question "Exercice - (EP 24-22-01)"
    Écrire une fonction `recherche_indices_classement` qui prend en paramètres un entier `elt` et un tableau d’entiers `tab`, et qui renvoie trois listes :

    - la première liste contient les indices des valeurs du tableau `tab` strictement
    inférieures à `elt` ;
    - la deuxième liste contient les indices des valeurs du tableau `tab` égales à `elt` ;
    - la troisième liste contient les indices des valeurs du tableau `tab` strictement
    supérieures à `elt`.

    Exemples :

    ```python
    >>> recherche_indices_classement(3, [1, 3, 4, 2, 4, 6, 3, 0])
    ([0, 3, 7], [1, 6], [2, 4, 5])
    >>> recherche_indices_classement(3, [1, 4, 2, 4, 6, 0])
    ([0, 2, 5], [], [1, 3, 4])
    >>>recherche_indices_classement(3, [1, 1, 1, 1])
    ([0, 1, 2, 3], [], [])
    >>> recherche_indices_classement(3, [])
    ([], [], [])
    ```

!!! question "Exercice - (EP 24-27-01)"
    Écrire une fonction `couples_consecutifs` qui prend en paramètre un tableau de nombres entiers `tab` non vide (type `list`), et qui renvoie la liste Python (éventuellement vide) des couples d'entiers consécutifs successifs qu'il peut y avoir dans `tab`.

    Exemples :
    ```python
    >>> couples_consecutifs([1, 4, 3, 5])
    []
    >>> couples_consecutifs([1, 4, 5, 3])
    [(4, 5)]
    >>> couples_consecutifs([1, 1, 2, 4])
    [(1, 2)]
    >>> couples_consecutifs([7, 1, 2, 5, 3, 4])
    [(1, 2), (3, 4)]
    >>> couples_consecutifs([5, 1, 2, 3, 8, -5, -4, 7])
    [(1, 2), (2, 3), (-5, -4)]
    ```

!!! question "Exercice - (EP 24-21-01)"
    Écrire une fonction `recherche_motif` qui prend en paramètre une chaîne de caractères `motif` non vide et une chaîne de caractères `texte` et qui renvoie la liste des positions de `motif` dans `texte`. Si `motif` n’apparaît pas, la fonction renvoie une liste vide.

    Exemples:

    ```python
    >>> recherche_motif("ab", "")
    []
    >>> recherche_motif("ab", "cdcdcdcd")
    []
    >>> recherche_motif("ab", "abracadabra")
    [0, 7]
    >>> recherche_motif("ab", "abracadabraab")
    [0, 7, 11]
    ```

!!! question "Exercice - (EP 24-22-01)"
    Écrire une fonction `recherche_indices_classement` qui prend en paramètres un entier `elt` et un tableau d’entiers `tab`, et qui renvoie trois listes :

    - la première liste contient les indices des valeurs du tableau `tab` strictement inférieures à `elt` ;
    - la deuxième liste contient les indices des valeurs du tableau `tab` égales à `elt` ;
    - la troisième liste contient les indices des valeurs du tableau `tab` strictement supérieures à `elt`.

    Exemples :

    ```python
    >>> recherche_indices_classement(3, [1, 3, 4, 2, 4, 6, 3, 0])
    ([0, 3, 7], [1, 6], [2, 4, 5])
    >>> recherche_indices_classement(3, [1, 4, 2, 4, 6, 0])
    ([0, 2, 5], [], [1, 3, 4])
    >>>recherche_indices_classement(3, [1, 1, 1, 1])
    ([0, 1, 2, 3], [], [])
    >>> recherche_indices_classement(3, [])
    ([], [], [])
    ```

!!! question "Exercice - (EP 24-28-02)"
    On considère la fonction `eleves_du_mois` prenant en paramètres `eleves` et `notes` deux tableaux de même longueur, le premier contenant le nom des élèves et le second, des entiers positifs désignant leur note à un contrôle de sorte que `eleves[i]` a obtenu la note `notes[i]`.  
    Cette fonction renvoie le couple constitué de la note maximale attribuée et des noms des élèves ayant obtenu cette note regroupés dans un tableau.  
    Ainsi, l’instruction `eleves_du_mois(['a', 'b', 'c', 'd'], [15, 18, 12, 18])` renvoie le couple `(18, ['b', 'd'])`.

    ```python linenums='1'
    def eleves_du_mois(eleves, notes):
        note_maxi = 0
        meilleurs_eleves =  ...

        for i in range(...) :
            if notes[i] == ... :
                meilleurs_eleves.append(...)
            elif notes[i] > note_maxi:
                note_maxi = ...
                meilleurs_eleves = [...]

        return (note_maxi,meilleurs_eleves)
    ```