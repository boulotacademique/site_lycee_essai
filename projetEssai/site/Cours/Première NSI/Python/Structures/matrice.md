# Les matrices ou liste de listes

!!! info "Vocabulaire"
    Un tableau (3 lignes et 4 colonnes) pour être humain ressemble à cela 
    
    \[
    \begin{array}{|c|c|c|c|}
    \hline
    1 & 10 & 100 & 1000\\
    \hline
    1 & 2 & 4 & 8 \\
    \hline
    1 & 3 & 9 & 27 \\
    \hline
    \end{array}
    \]

    Comme le terme &laquo; tableau &raquo; a un sens bien précis en informatique, nous parlerons ici de **matrice**.

Une structure pour coder une telle matrice est une &laquo une liste de listes &raquo; c'est-à-dire une liste ou chaque élément est aussi une liste.

Ainsi, pour coder la matrice de l'exemple précédent, on écrirait :

```python
matrice1 = [[1,10,100,1000],[1,2,4,8],[1,3,9,27]]
```

Ainsi, le type d'une matrice est ... ```list```. C'est bien une liste !

???- tip "Vue plus lisible pour un humain"
    En jouant avec les espaces, il est possible d'écrire (dans un code python) une matrice de la façon suivante :

    ```python
    matrice1 = [[1,10,100,1000],
                  [1,2,4,8],
                  [1,3,9,27]]
    ```

Il est aussi naturel d'employer les termes de &laquo; lignes &raquo; et de &laquo; colonnes &raquo;.

!!! info "Les lignes"
    Une matrice est donc codée par une liste de listes. Une ligne est donc un élément de la liste.

    Avec l'exemple précédent, 

    - l'élément d'indice 0 de ```matrice1``` est la liste ```[1,10,100,1000]``` : c'est la ligne d'indice 0
    - l'élément d'indice 1 de ```matrice1``` est la liste ```[1,2,4,8]``` : c'est la ligne d'indice 1
    - l'élément d'indice 2 de ```matrice1``` est la liste ```[1,3,9,27]``` : c'est la ligne d'indice 2

    Le nombre de lignes d'une telle matrice est donc le nombre d'éléments de la liste ```matrice1```, c'est-à-dire ```len(matrice1)``` !

???- example "Exemple"
    Ecrire une fonction qui prend en argument une matrice ```mat``` et un entier ```num_lig``` et qui renvoie la ligne de ```mat``` d'indice ```num_lig```.

    Signature : ```Fonction ligne_matrice(mat : list,num_lig : int) : list```

!!! info "Le nombre de colonne"
    Le nombre de colonnes d'une matrice est le nombre d'élements d'une ligne d'indice quelconque (pourquoi pas celle d'indice 0 ?), c'est-à-dire ```len(matrice1[0])```.

???- example "Exemple"
    Ecrire une fonction qui prend en argument une matrice ```mat``` et un entier ```num_col``` et qui renvoie une liste contenant les éléments de la colonne de ```mat``` d'indice ```num_col```.

    Signature : ```Fonction colonne_matrice(mat : list, num_col : int) : list```