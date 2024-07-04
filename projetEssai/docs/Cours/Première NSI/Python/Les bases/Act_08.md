# Python<br>Les tris

!!! question "Exercice - (EP 24-01-02)"
    On considère l'algorithme de tri de tableau suivant : à chaque étape, on parcourt le sous-tableau des éléments non rangés et on place le plus petit élément en première position de ce sous-tableau.  
    Exemple avec le tableau : ```t = [41, 55, 21, 18, 12, 6, 25]``` 

    - **Étape 1 :** on parcourt tous les éléments du tableau, on permute le plus petit élément avec le premier. Le tableau devient `t = [6, 55, 21, 18, 12, 41, 25]`
    - **Étape 2 :** on parcourt tous les éléments **sauf le premier**, on permute le plus petit élément trouvé avec le second.  
    Le tableau devient : ```t = [6, 12, 21, 18, 55, 41, 25]``` 

    Et ainsi de suite.  
    Le programme ci-dessous implémente cet algorithme.

    ```python linenums='1'
    def echange(tab, i, j):
        '''Echange les éléments d'indice i et j dans le tableau tab.'''
        temp = ... 
        tab[i] = ... 
        tab[j] = ... 

    def tri_selection(tab):
        '''Trie le tableau tab dans l'ordre croissant
        par la méthode du tri par sélection.'''
        N = len(tab)
        for k in range(...): 
            imin = ... 
            for i in range(..., N): 
                if tab[i] < ...: 
                    imin = i
            echange(tab, ..., ...) 
    ```

    Compléter le code de cette fonction de façon à obtenir :

    ```python
    >>> liste = [41, 55, 21, 18, 12, 6, 25]
    >>> tri_selection(liste)
    >>> liste
    [6, 12, 18, 21, 25, 41, 55]
    ``` 

!!! question "Exercice - (EP 24-07-02)"
    La fonction `tri_insertion` suivante prend en argument un tableau `tab` et trie ce tableau en utilisant la méthode du tri par insertion. Compléter cette fonction pour qu'elle réponde à la spécification demandée.  
    On rappelle le principe du tri par insertion : on considère les éléments à trier un par un, le premier élément constituant, à lui tout seul, un tableau trié de longueur 1. On range ensuite le second élément pour constituer un tableau trié de longueur 2, puis on range le troisième élément pour avoir un tableau trié de longueur 3 et ainsi de suite...  
    A chaque étape, le premier élément du sous-tableau non trié est placé dans le sous-tableau des éléments déjà triés de sorte que ce sous-tableau demeure trié.  
    Le principe du tri par insertion est donc d'insérer à la n-ième itération, le n-ième élément à la bonne place.

    ```python linenums='1'
    def tri_insertion(tab):
        '''Trie le tableau tab par ordre croissant
        en appliquant l'algorithme de tri par insertion'''
        n = len(tab)
        for i in range(1, n):
            valeur_insertion = ... 
            # la variable j sert à déterminer 
            # où placer la valeur à ranger
            j = ... 
            # tant qu'on n'a pas trouvé la place de l'élément à
            # insérer on décale les valeurs du tableau vers la droite
            while j > ... and valeur_insertion < tab[...]: 
                tab[j] = tab[j-1]
                j = ... 
            tab[j] = ... 
    ```

    Exemples :

    ```python
    >>> tab = [98, 12, 104, 23, 131, 9]
    >>> tri_insertion(tab)
    >>> tab
    [9, 12, 23, 98, 104, 131]
    ``` 

!!! question "Exercice - (EP 24-09-01)"
    On veut trier par ordre croissant les notes d’une évaluation qui sont des nombres entiers compris entre 0 et 10 (inclus).  
    Ces notes sont contenues dans un tableau `notes_eval` (type `list`).  
    Écrire une fonction `effectif_notes` prenant en paramètre le tableau `notes_eval` et renvoyant un tableau de longueur 11 tel que la valeur d’indice `i` soit le nombre de notes valant `i` dans le tableau `notes_eval`.  
    Écrire ensuite une fonction `notes_triees` prenant en paramètre le tableau des effectifs des notes et renvoyant un tableau contenant les mêmes valeurs que `notes_eval` mais triées dans l’ordre croissant.

    Exemple :

    ```python
    >>> notes_eval = [2, 0, 5, 9, 6, 9, 10, 5, 7, 9, 9, 5, 0, 9, 6, 5, 4]
    >>> eff = effectif_notes(notes_eval)
    >>> eff
    [2, 0, 1, 0, 1, 4, 2, 1, 0, 5, 1]
    >>> notes_triees(eff)
    [0, 0, 2, 4, 5, 5, 5, 5, 6, 6, 7, 9, 9, 9, 9, 9, 10]
    ```

!!! question "Exercice - (EP 24-12-01)"
    Écrire une fonction `tri_selection` qui prend en paramètre un tableau `tab` de nombres entiers (type `list`) et qui le modifie afin qu’il soit trié par ordre croissant.  
    On utilisera l’algorithme suivant :

    - on recherche le plus petit élément du tableau, en le parcourant du rang 0 au dernier
    rang, et on l’échange avec l’élément d’indice 0 ;
    - on recherche ensuite le plus petit élément du tableau restreint du rang 1 au dernier
    rang, et on l’échange avec l’élément d’indice 1 ;
    - on continue de cette façon jusqu’à ce que le tableau soit entièrement trié.

    Exemple :
    ```python
    >>> tab = [1, 52, 6, -9, 12]
    >>> tri_selection(tab)
    >>> tab
    [-9, 1, 6, 12, 52]
    ```


!!! question "Exercice - (EP 24-16-02)"
    La fonction `tri_bulles` prend en paramètre une liste `tab` d’entiers (type `list`) et le modifie pour le trier par ordre croissant.  
    Le tri à bulles est un tri en place qui commence par placer le plus grand élément en dernière position en parcourant le tableau de gauche à droite et en échangeant au passage les éléments voisins mal ordonnés (si la valeur de l’élément d’indice `i` a une valeur strictement supérieure à celle de l’indice `i + 1`, ils sont échangés). Le tri place ensuite en avant-dernière position le plus grand élément du tableau privé de son dernier élément en procédant encore à des échanges d’éléments voisins. Ce principe est répété jusqu’à
    placer le minimum en première position.

    Exemple : pour trier le tableau `[7, 9, 4, 3]` :

    - première étape : 7 et 9 ne sont pas échangés, puis 9 et 4 sont échangés, puis 9 et 3 sont échangés, le tableau est alors `[7, 4, 3, 9]`
    - deuxième étape : 7 et 4 sont échangés, puis 7 et 3 sont échangés, le tableau est alors `[4, 3, 7, 9]`
    - troisième étape : 4 et 3 sont échangés, le tableau est alors `[3, 4, 7, 9]`

    Compléter le code Python ci-dessous qui implémente la fonction tri_bulles.

    ```python linenums='1'
    def echange(tab, i, j):
        '''Echange les éléments d'indice i et j dans le tableau tab.'''
        temp = ... 
        tab[i] = ... 
        tab[j] = ... 

    def tri_bulles(tab):
        '''Trie le tableau tab dans l'ordre croissant
        par la méthode du tri à bulles.'''
        n = len(tab)
        for i in range(...): 
            for j in range(...): 
                if ... > ...: 
                    echange(tab, j, ...) 
    ```

    Exemples :

    ```python
    >>> tab = []
    >>> tri_bulles(tab)
    >>> tab
    []
    >>> tab2 = [9, 3, 7, 2, 3, 1, 6]
    >>> tri_bulles(tab2)
    >>> tab2
    [1, 2, 3, 3, 6, 7, 9]
    >>> tab3 = [9, 7, 4, 3]
    >>> tri_bulles(tab3)
    >>> tab3
    [3, 4, 7, 9]
    ``` 

!!! question "Exercice - (EP 24-31-02)"
    On s’intéresse dans cet exercice à la recherche dichotomique dans un tableau trié d’entiers. Compléter la fonction suivante en respectant la spécification.

    ```python linenums='1'
    def dichotomie(tab, x):
        """
        tab : tableau d'entiers trié dans l'ordre croissant
        x : nombre entier
        La fonction renvoie True si tab contient x et False sinon
        """
        debut = 0
        fin = len(tab) - 1
        while debut <= fin:
            m = ... 
            if x == tab[m]:
                return ... 
            if x > tab[m]:
                debut = m + 1
            else:
                fin = ... 
        return ... 
    ```

    Exemples :

    ```python
    >>> dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28)
    True
    >>> dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27)
    False
    ``` 

!!! question "Exercice - (EP 24-37-02)"
    On considère un tableau d'entiers `tab` (de type `list`) dont les éléments sont des `0` ou des `1`). On se propose de trier ce tableau selon l'algorithme suivant : à chaque étape du tri, le tableau est constitué de trois zones consécutives, la première ne contenant que des `0`, la seconde n'étant pas triée et la dernière ne contenant que des `1`.  
    Au départ, les zones ne contenant que des `0` et des `1` sont vides.

    <table>
    <tr>
    <td>Zone de 0</td><td>Zone non triée</td><td>Zone de 1</td>
    </tr>
    </table>

    Tant que la zone non triée n'est pas réduite à un seul élément, on regarde son premier élément :

    - si cet élément vaut 0, on considère qu'il appartient désormais à la zone ne contenant
    que des 0 ;
    - si cet élément vaut 1, il est échangé avec le dernier élément de la zone non triée et on
    considère alors qu’il appartient à la zone ne contenant que des 1.

    Dans tous les cas, la longueur de la zone non triée diminue de 1.  
    Compléter la fonction `tri` suivante :

    ```python linenums='1'
    def tri(tab):
        '''tab est un tableau d'entiers contenant des 0 et des 1.
        La fonction trie ce tableau en plaçant tous les 0 à gauche'''
        i = ... # premier indice de la zone non triée 
        j = ... # dernier indice de la zone non triée 
        while i < j:
            if tab[i] == 0:
                i = ... 
            else:
                valeur = ... 
                tab[j] = ... 
                ...
                j = ... 
    ```

    Exemple :

    ```python
    >>> tab = [0,1,0,1,0,1,0,1,0]
    >>> tri(tab)
    >>> tab
    [0, 0, 0, 0, 0, 1, 1, 1, 1]    
    ``` 

!!! question "Exercice - (EP 24-42-02)"
    Le but de l'exercice est de compléter une fonction qui détermine si une valeur est présente dans un tableau de valeurs triées dans l'ordre croissant.  
    Compléter l'algorithme de dichotomie donné ci-après.

    ```python linenums='1'
    def dichotomie(tab, x):
        """applique une recherche dichotomique pour déterminer
        si x est dans le tableau trié tab.
        La fonction renvoie True si tab contient x et False sinon"""

        debut = 0
        fin = ... 
        while debut <= fin:
            m = ... 
            if x == tab[m]:
                return ... 
            if x > tab[m]:
                debut = ... 
            else:
                fin = ... 
        return False
    ```

    Exemples :

    ```python
    >>> dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28)
    True
    >>> dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27)
    False
    >>> dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 1)
    False
    >>> dichotomie([], 28)
    False
    ``` 

!!! question "Exercice - (EP 24-46-01)"
    Écrire une fonction `recherche` qui prend en paramètres un tableau `tab` de nombres entiers triés par ordre croissant et un nombre entier `n`, et qui effectue une recherche dichotomique du nombre entier `n` dans le tableau non vide `tab`.  
    Cette fonction doit renvoyer un indice correspondant au nombre cherché s’il est dans le tableau, `None` sinon.

    Exemples :
    ```python
    >>> recherche([2, 3, 4, 5, 6], 5)
    3
    >>> recherche([2, 3, 4, 6, 7], 5) # renvoie None
    ```