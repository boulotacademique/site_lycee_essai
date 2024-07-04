# Python<br>Les fonctions

## Découverte

!!! info "Définition"
    Une façon pragmatique de concevoir une fonction est de la voir comme une suite d'instructions associée à un nom (le nom de la fonction) pouvant nécessité 0 ou plusieurs arguments et &laquo; renvoyant un résultat &raquo; ou rien (c'est-à-dire ```None``` !) !

    Par exemple, une fonction s'appelle ```moyenne```, prend pour argument 3 nombres et renvoie un nombre (qui est la moyenne).

    En Python, une fonction s'écrit de la façon suivante :

    ```python
    def nom_de_fonction(parametre1, parametre2):
        instruction 1
        instruction 2
        ...
        return resultat_renvoye
    ```

    Pour utiliser une fonction, il faut utiliser son nom toujours suivi de parenthèses avec des valeurs en arguments pour chaque paramètre (dans le même ordre).

    ```python
    nom_de_fonction(valeur_pour_parametre1, valeur_pour_parametre2)
    ```

???+ example "Exemple de définition d'une fonction"

    Voici une fonction

    ```python
    def moyenne(nb1, nb2, nb3):
        num = nb1 + nb2 + nb3
        return num/3
    ```


???+ example "Exemple d'utilisation d'une fonction"

    Voici une fonction

    ```python
    def annee_naiss(age, annee_en_cours):
        annee = annee_en_cours - age
        return annee
    
    mon_annee = annee_naiss(16, 2023) # contient 2007
    ```

L'intérêt d'écrire des fonctions est multiple :

- décomposer un programme complexe en plusieurs fonctions (qui pourront être testées et corrigées plus facilement)
- pouvoir utiliser ces fonctions dans différentes parties du programme (éventuellement ces fonctions sont rangées dans un fichier appelé **bibliothèque**).  
On parle de modularité !

!!! info "Signature d'une fonction"
    Souvent dans un énoncé, une fonction est décrite avec **sa signature**. Par exemple,
    la signature ```Fonction nom_de_fonction(parametre1 : type, parametre2 : type) : type``` précise le nom de la fonction, le nombre de paramètres, leur type et le type renvoyé par la fonction.

    Par exemple, les fonctions précédentes ont pour signature:

    - ```Fonction moyenne(nb1 : int, nb2 : int, nb3 : int) : float```
    - ```Fonction annee_nais(age : int, annee_en_cours : int) : int```

## Les n-uplets

!!! info "Définition : un n-uplet"
    **Un n-uplet** (ou une séquence à $n$ éléments) est une suite finie d'éléments numérotés (ou une collection ordonnée).  
    Ces éléments peuvent être différents ou non.


!!! example "Exemple"

    - Les coordonnées d'un points $(x;y)$ forment un n-uplet à deux éléments.
    - Les 5 premiers termes d'une suite $(u_0,u_1,u_2,u_3;u_4)$ forment un n-uplet à 5 éléments.
    - Par contre, un ensemble n'est pas un n-uplet ! En effet $\{2;3 \}=\{3;2\}$ Donc l'ordre n'a pas d'importance.  
    La définition parle &laquo; d'éléments numérotés &raquo; pour signifier que l'ordre des éléments est important.


!!! tip "Méthode"
    Tous les éléments d'un n-uplet peuvent donc être associés à un entier correspondant à leur position dans le n-uplet.

    !!! warning "On commence à 0"
        En informatique, les positions (ou les indices) commencent à $0$.

    Par exemple, dans le n-uplet $\,(-5,3)$, $-5$ est à la position $0$ et $3$ à la position $1$.


!!! info "Définition"
    En informatique, il est possible de modifier un élément de certains n-uplets : on dit qu'ils sont **mutables**. Il est possible de faire `uplet[indice]=2`.  
    Alors que pour les non mutables, il n'est pas possible de faire `uplet[indice]=2`. Cela déclenche une erreur !  
    Les n-uplets sont donc classés en deux catégories : **les mutables** et **les non mutables**. 

\subsection{Les n-uplets dans Python}

!!! tip "Les différents n-uplets"
    Sous Python, nous travaillerons principalement avec trois types de n-uplets :

    - les tableaux, qui sont de mutables
    - les listes, qui sont mutables
    - les listes de listes (ou matrice), qui sont des mutables
    - les tuples  qui sont des listes non mutables
    - les chaînes de caractères qui sont non mutables

    Il y a plusieurs méthodes (ou fonctions) communes aux n-uplets mutables et non mutables. 

### Les tuples

!!! tip "Le cas des tuples"
    Les tuples sont des listes non mutables. Avec Python, elles se notent entre `(   )`.  
    On utilise les tuples lorsque vous souhaitez avoir une suite d'éléments **qui ne sera pas modifiés** !


!!! tip "Les fonctions sur les tuples"

    - `()` : le tuple vide. 
    - `len(T)` : retourne la taille (le nombre d'élément) du tuple.
    - `T1+T2` : effectue la concaténation des deux tuples. Cela retourne donc un tuple contenant les éléments du tuple `L1` suivis de ceux du tuple `L2`.
    - `T[i]` : retourne l'élément du tuple `T` à la position `i`.
    - `4 in T` : retourne `True` si 4 est dans `T`, `False` sinon.
    - `for elt in T :` : parcourt le tuple `T`

!!! tip "En pratique"

    Les tuples ne seront utilisés que dans des cas très précis :

    - pour un n-uplet dont tous les éléments sont connus à la création du tuple (par exemple les coordonnées de points)
    - mais surtout pour la permutation de 2 éléments
    - mais surtout pour des renvois multiple d'une fonction

!!! example "Exemple - la permutation"
    
    ```python
    a="hello"
    b=2
    a,b=b,a
    print("Maintenant a = 2 et b = 'hello'")
    ```

!!! example "Exemple - renvoi multiple"

    Pour retourner plusieurs éléments dans une fonction :

    ```python
    def milieu(ptA,ptB):
        xMilieu=(ptA[0]+ptB[0])/2
        yMilieu=(ptA[1]+ptB[1])/2
        return xMilieu,yMilieu

    M = (2,3)
    P = (-1,5)
    print(milieu(M,P))
    ```

    Ce programme affiche `(0.5, 4.0)`.

!!! danger "Important - Le décompactage"

    Il est possible de récupérer et stocker dans des variables tous les éléments d'un tuple **en une ligne de code.**  

    ```python
    un_tuple = (2,3,4)
    a,b,c = un_tuple
    ```

    Ainsi `a` vaut 2, `b` vaut 3 et `c` vaut 4 !

    En particulier, lorsqu'une fonction renvoie plusieurs valeurs, il est préférable d'utiliser cette méthode :

    ```python
    def milieu(ptA,ptB):
        xMilieu=(ptA[0]+ptB[0])/2
        yMilieu=(ptA[1]+ptB[1])/2
        return xMilieu,yMilieu

    M = (2,3)
    P = (-1,5)
    abs_mil, ord_mil = milieu(M,P)
    ```
