# Les matrices ou liste de listes

## Définition

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

Une structure pour coder une telle matrice est une &laquo; une liste de listes &raquo; c'est-à-dire une liste ou chaque élément est aussi une liste.

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

    

???- example "Exemple"
    Voici une matrice.

    <div class="Center_ss_bd Encadre Code_cache">

    ```python
    matrice1 = [[1,10,100,1000],[1,2,4,8],[1,3,9,27]]
    print("type de matrice1",type(matrice1))
    print("matrice1 est une instance de list", isinstance(matrice1,list))
    # Plus lisible
    matrice1 = [[1,10,100,1000],
                [1,2,4,8],
                [1,3,9,27]]
    print("Malheureusement, cette affichage ne fonctionne pas avec print !")
    print(matrice1)
    ```

    </div>

    {{ IDE('Python_base_code/matrice_01' ,MAX = 1000) }}


    
Il est aussi naturel d'employer les termes de &laquo; lignes &raquo; et de &laquo; colonnes &raquo;.

!!! info "Les lignes"
    Une matrice est donc codée par une liste de listes. **Une ligne est donc *un* élément de la liste.**

    Avec l'exemple précédent, 

    - l'élément d'indice 0 de ```matrice1``` est la liste ```[1,10,100,1000]``` : c'est la ligne d'indice 0
    - l'élément d'indice 1 de ```matrice1``` est la liste ```[1,2,4,8]``` : c'est la ligne d'indice 1
    - l'élément d'indice 2 de ```matrice1``` est la liste ```[1,3,9,27]``` : c'est la ligne d'indice 2

    **Le nombre de lignes** d'une telle matrice est donc le nombre d'éléments de la liste ```matrice1```, c'est-à-dire ```len(matrice1)``` !

!!! info "Le nombre de colonne"
    **Le nombre de colonnes** d'une matrice est le nombre d'élements d'une ligne d'indice quelconque (pourquoi pas celle d'indice 0 ?), c'est-à-dire ```len(matrice1[0])```.

## Manipulation de matrice

!!! info "Récupérer un élément"
    A partir de l'indice de la ligne et de l'indice de la colonne, il est facile de récupérer un élément ```matrice[idx_lig][idx_col]```.

???+ example "Exemple"
    Dans la matrice m1, écrire le code qui permet d'afficher 

    <ol>
    <li> ad </li>
    <li> bd </li>
    <li> be </li>
    </ol>

    <div class="Center_ss_bd Encadre Code_cache">

    ```python
    m1 = [["ad","bd","cd"],["ae","be","ce"]]
    ```

    </div>

    {{ IDE('Python_base_code/matrice_02' , MAX = 1000) }}


!!! info "Parcours d'une matrice"
    Afin de de récupérer les éléments d'une matrice dans l'ordre &laquo; classique &raquo;, il faut deux boucles :

    ```python
    matrice1 = [[1,10,100,1000],
                  [1,2,4,8],
                  [1,3,9,27]]
    for idx_lig in range(len(matrice1)):
        for idx_col in range(len(matrice1[0])):
            print(matrice1[idx_lig][idx_col])
    ```

???- example "Exemple"
    Ecrire une fonction qui prend en argument une matrice ```mat``` et un entier ```num_lig``` et qui renvoie la ligne de ```mat``` d'indice ```num_lig```.

    Signature : ```Fonction ligne_matrice(mat : list,num_lig : int) : list```

    {{ IDEv() }}

    ???- done "Réponse"

        ```python
        def ligne_matrice(mat, num_lig):
            return mat[num_lig] # Par référence
        
        # Exemple
        matrice1 = [[1,10,100,1000],
                  [1,2,4,8],
                  [1,3,9,27]]
        print(ligne_matrice(matrice1,2))
        ```

    ???- danger "Une liste est un mutable"
        Il y a deux façons d'écrire une telle fonction. Il faut choisir selon qu'il faut une [copie par référence ou par valeur](AFAIRE) de la ligne.

    ???- done "Réponse"

        ```python
        def ligne_matrice(mat, num_lig):
            liste_rep = []
            for idx in range(len(mat[num_lig])):
                liste_rep.append(mat[num_lig][idx])
            return liste_rep # Par valeur
        
        # Exemple
        matrice1 = [[1,10,100,1000],
                  [1,2,4,8],
                  [1,3,9,27]]
        print(ligne_matrice(matrice1,2))
        ```

???- example "Exemple"
    Ecrire une fonction qui prend en argument une matrice ```mat``` et un entier ```num_col``` et qui renvoie une liste contenant les éléments de la colonne de ```mat``` d'indice ```num_col```.

    Signature : ```Fonction colonne_matrice(mat : list, num_col : int) : list```

!!! info "Créer une matrice"

    Le principe est simple : créer des listes pour les lignes et les ajouter comme éléments de la matrice.

    ```python
    nb_lig = 4
    nb_col = 2
    matrice = [] # On va remplir cette matrice
    for num_lig in range(nb_lig):
        ligne = [] # Il faut partir d'une ligne vide
        for num_col in range(nb_col):
            # On ajoute les éléments voulus
            ligne.append(f"elt ({num_lig},{num_col})")
        # Une fois la ligne remplie
        # on l'ajoute à notre matrice
        matrice.append(ligne)    
    ```

    {{ IDEv('Python_base_code/matrice_03' , MAX = 1000) }}