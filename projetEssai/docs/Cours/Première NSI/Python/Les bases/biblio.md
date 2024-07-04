# Python<br>Les bibliothèques

## L'importation

!!! info "Définition"
    Une bibliothèque est un fichier comportant des fonctions et des constantes. En l'important dans votre programme, vous pourrez alors utiliser ces fonctions et ces constantes.  
    Naturellement, il est possible de créer ses propres bibliothèques. Pour cette année, il suffit de créer un fichier python &laquo; à côté &raquo; du fichier contenant votre programme.

!!! tip "Méthode pour importer une bibliothèque"
    Par exemple avec la bibliothèque `turtle`.

    - `import turtle` : pour utiliser les fonctions (par exemple `forward()`) de cette bibliothèque, il faut taper `turtle.forward(100)`
    - `import turtle as tu` : permet de donner un alias au nom de cette bibliothèque. Il faut alors taper  `tu.forward(100)`
    - Si vous n'avez besoin que de certaines fonctions, vous pouvez les importer et uniquement elles : `from turtle import forward, left, right, exitonclick`. Il n'est plus utile alors de mettre le nom de la bibliothèque devant ces fonctions. **_ATTENTION : les autres fonctions de la bibliothèque ne seront pas accessibles !!!_**

    Pour avoir de l'aide sur une bibliothèque, il suffit de taper `help(nom_de_la_bibliothèque)` ou `help(alias_de_la_bibliothèque)`.

!!! tip "Organisation"

    Dans un fichier python (et donc dans un éditeur comme pyzo, spyder, VS, ...), vous organiserez votre fichier de la façon suivante :  
    ```python
    ### Importation des bibliothèques
    ...
    ...

    ### Les fonctions (et uniquement des fonctions)
    ...
    ...

    ### Le corps principal (donc pas de fonction)
    ```

???- warning "Une très mauvaise habitude"

    Vous trouverez aussi `from turtle import *`. Dans ce cas, vous pouvez utilisez les fonctions simplement (sans préciser le nom de la bibliothèque ou son alias).  
    Mais, si vous importez plusieurs bibliothèques, vous pourriez avoir un conflit. Par exemple :  
    ```python
    from numpy import *
    from math import *

    L = np.array([1,5])
    print(cos(L)) # déclenche une erreur
    ```  
    ```python
    from math import *
    from numpy import *

    L = np.array([1,5])
    print(cos(L)) # fonctionne !!
    ```  
    En effet, la fonction `cos` existe dans les 2 bibliothèques, mais n'ont pas du tout la même signature !

???- tip "Méthode"
    Si vous créez une bibliothèque, elle ne doit comporter que des fonctions ou des constantes. Il n'y a donc pas de &laquo; corps principal &raquo; dans une bibliothèque.  
    Mais si vous voulez en mettre un (pour tester vos fonctions, par exemple) alors voici une possibilité :  
    ```python
    ### Les fonctions de la bibliothèque
    ...
    ...

    ### Les constantes
    ...
    ...

    if __name__ == "__main__":
        ### Corps principal
        ...
        ...

    ```

!!! warning "Attention au nom de votre fichier"

    - **Ne jamais** donner le nom d'une bibliothèque à votre fichier !
    - Eviter de mettre des espaces dans le nom de votre bibliothèque.

???- question "Exercice"
    Une bibliothèque peut contenir un très grand nombre de fonctions. Utiliser `help(nom_de_la_bibliothèque)` fournit beaucoup trop d'informations.

    1. Après avoir importer la bibliothèque `turtle` avec l'alias `tu`, afficher sa documentation.
    2. Il est possible d'obtenir la liste des fonctions et constantes d'une bibliothèque en tapant `print(dir(tu))`. Faites-le.
    3. Maintenant, il est possible d'avoir de l'aide sur les fonctions avec `help(alias_de_la_bibliothèque.nom_de_la_fonction)` ou  `help(nom_de_la_bibliothèque.nom_de_la_fonction)`.  
    4. Parmi les fonctions de la biliothèque, obtenez des renseignements sur la méthode `clear`. Quelles différences y-a-t-il entre `clear` et `clearscreen` ?
    5. Que fait la méthode `shape` ? 

???- question "Exercice"

    1. Après avoir importé la bibliothèque `random` sous l'alias `rd`, faites apparaitre la liste des fonctions de cette bibliothèque.
    2. Que fait la méthode `randint` ? Quelle(s) différence(s) avec `randrange` ?
    3. Que fait la méthode `random` ?
    4. Soient $a$ et $b$ deux réels tels que $a \leq b$. Quelles sont les valeurs possibles pour `(b-a)*rd.random() + a` ?