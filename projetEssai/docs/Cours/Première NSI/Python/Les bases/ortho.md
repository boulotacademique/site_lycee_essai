# Python<br>Bien écrire en python

## L'orthographe !

!!! info "A retenir"

    Pour bien écrire un code python, il est indispensable de savoir écrire des mots, des syntaxes, des phrases (...) en python.

    Ainsi les principaux mots rencontrés sont ```if, else, elif, while, for, range, def, print, input, int, str```. **Ils ne commencent JAMAIS par une majuscule !**

!!! warning "Soyez attentifs"

    Certains éléments ne varient jamais ! Ainsi, les lignes commençant par ```if, else, elif, while, for, def``` se termine **toujours** par un &laquo; ```:``` &raquo;

    De plus la ligne suivante commence **toujours** avec une tabulation de plus que celle avec ```if, else, elif, while, for, def```

???- question "Exercice"

    Corriger les erreurs dans les codes suivants :

    1.
    ```python
    If a>3
        print("C'est plus grand que 3 !")
    ```
    2.
    ```python
    for i in Range(2,5):
    print("Hello !")
    ```

## Cas particuliers des fonctions

!!! info "A retenir"

    Certains mots en python désignent des fonctions. Il sont donc suivis de parenthèses (sauf dans certains cas cf [Callback](AFAIRE) par exemple !). A l'intérieur de ces parenthèses, il peut y avoir entre 0 et plusieurs paramètres qui seront **toujours** séparés par une virgule. Il faut bien respecter l'ordre imposé et le type imposé de chaque paramètre.

    A tout moment dans une console python, vous pouvez obtenir des renseignements sur une fonction en tapant ```help(nom_de_la_fonction)```

    Au début, vous utiliserez principalement les fonctions ```range, print, input, int, str```.

!!! warning "Très important"

    Ainsi, ```print``` est une fonction. Il y a donc **toujours des parenthèses**. Elle peut prendre 0 argument mais aussi plusieurs !

    ```python
    print() # n'affiche rien, puis effectue un retour à la ligne
    print("Hello") # affiche Hello, puis effectue un retour à la ligne
    print(3+5) # affiche 8, puis effectue un retour à la ligne
    print(3+5,"hello") # affiche 8 hello (notez l'espace !!), puis effectue un retour à la ligne
    ```

    {{ IDEv('Python_base_code/ortho_01', MAX = 1000) }}

!!! info "Exemple à retenir"

    <span id = "range">Rque</span> : afin d'avoir une vue pour ```range``` (cf [iterable](AFAIRE)), on le transforme en une liste !

    <!--<div class="Center_ss_bd Code_cache">-->

    - La fonction ```range``` avec **un** argument :

        ```python
        list(range(5)) # affiche [0,1,2,3,4]
        ```

        Plus généralement, ```range(n)``` est une (sorte de) liste à $n$ éléments commençant à $0$. Elle se termine donc {==**à** $\mathbf{n-1}$==} !
    
    - La fonction ```range``` avec **deux** arguments :

        ```python
        list(range(2,7))  # affiche [2,3,4,5,6]
        ```

        Plus généralement, ```range(a,b)``` est une (sorte de) liste à $b - a$ éléments commençant à $a$. Elle se termine donc {==**à** $\mathbf{b-1}$==} !
    
    - Il est possible d'utiliser la fonction ```range``` avec trois arguments :  
    ```python
    list(range(3,12,2)) # affiche [3,5,7,9,11]
    ```  
    Ainsi,`range(a,b,c)` est une (sorte de) liste qui comporte toutes les valeurs $a + k\times c$ supérieures $a$ et strictement inférieures à $b$.  
    Ainsi, pour obtenir des entiers de $5$ à $2$ dans l'ordre décroissant, il suffit  de faire `range(5,1,-1)`
    <!--</div>-->

    {{ IDE('Python_base_code/ortho_03', MAX = 1000) }}


!!! warning "Très important"

    La fonction ```range``` prend **obligatoirement** au moins un paramètre ! Ainsi, {--```range()```--} déclenche une erreur !

    De plus, ces paramètres sont **toujours** de type ```int``` ! Ainsi, si la variable ```liste``` contient une liste, {--```range(liste)```--} déclenche une erreur !

???- question "Exercice"
    1. Ecrire les listes correspondantes à :  
        1. `range(10)`
        2. `range(-5,10)`
        3. `range(2,10,2)`
        4. `range(50,-1,-10)`
    2. Ecrire le range correpondant aux listes suivantes :  
        1. `[3,5,6,7,8]`
        2. `[0,1,2,3,4,5]`
        3. `[0,2,4,6,8,10]`
        4. `[11,13,15,17,19,21]`
        5. `[20,15,10,5,0,-5,-10,-15]`


## Les commentaires

!!! tip "Commentaires"

    Un commentaire est une (ou des) ligne(s) (ou une fin de ligne) qui ne sera pas du tout lue(s) (et encore moins interprétée(s)) par Python.
    
    Il y a deux types de commentaires :

    - ceux qui tiennent sur une ligne ou une fin de ligne : ils commencent par un ```#```
    - ceux qui sont sur plusieurs lignes : ces commentaires sont **encadrés** par des ```"""```

    {{ IDEv('Python_base_code/ortho_04', MAX = 1000) }}


???- warning "Dommage !"

    Il n'est pas possible de mettre un commentaire au milieu d'une ligne de code ! (contrairement au HTML)

???- tip "DOCSTRING"

    En début de fonction, il faudra écrire un descriptif détaillé de cette fonction : c'est son docstring !
    Lorsqu'un utilisateur veut savoir comment utiliser une fonction, il lui suffira d'écrire ```help(nom_de_la_fonction)``` pour afficher le docstring !

!!! tip "Bilan"

    Quand vous écrivez, du code python, en particulier sur feuille, pensez à vérifier ces éléments &laquo; d'orthographe &raquo;

