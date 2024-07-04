# Python<br>

!!! question "Exercice - 1 (EP 24-12-02)"

    Le jeu du « plus ou moins » consiste à deviner un nombre entier choisi entre 1 et 99.

    Une élève de NSI décide de le coder en langage Python de la manière suivante :

    - le programme génère un nombre entier aléatoire compris entre 1 et 99 ;
    - si la proposition de l’utilisatrice est plus petite que le nombre cherché, l’utilisatrice en
    est avertie. Elle peut alors en tester un autre ;
    - si la proposition de l’utilisatrice est plus grande que le nombre cherché, l’utilisatrice en
    est avertie. Elle peut alors en tester un autre ;
    - si l’utilisatrice trouve le bon nombre en 10 essais ou moins, elle gagne ;
    - si l’utilisatrice a fait plus de 10 essais sans trouver le bon nombre, elle perd.

    La fonction `randint` est utilisée.  
    Si a et b sont des entiers tels que `a <= b`, `randint(a,b)` renvoie un
    nombre entier compris entre `a` et `b`.


    Compléter le code ci-dessous et le tester :

    ```python linenums='1'
    from random import randint

    def plus_ou_moins():
        nb_mystere = randint(1,...)
        nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
        compteur = ...

        while nb_mystere != ... and compteur < ... :
            compteur = compteur + ...
            if nb_mystere ... nb_test:
                nb_test = int(input("Trop petit ! Testez encore : "))
            else:
                nb_test = int(input("Trop grand ! Testez encore : "))

        if nb_mystere == nb_test:
            print ("Bravo ! Le nombre était ",...)
            print("Nombre d'essais: ",...)
        else:
            print ("Perdu ! Le nombre était ",...)
    ```

!!! question "Exercice - 2 (EP 24-15-02) (EP 24-17-02)"

    On considère la fonction `binaire`. Cette fonction prend en paramètre un entier positif `a` en écriture décimale et renvoie son écriture binaire sous la forme d’une chaine de caractères.  
    L’algorithme utilise la méthode des divisions euclidiennes successives comme l’illustre l’exemple ci-après.

    [![A compléter](../Image/30_divisions.png){.Center_lien }](../Image/30_divisions.png)

    Compléter le code de la fonction `binaire`.

    ```python linenums='1'
    def binaire(a):
        '''convertit un nombre entier a en sa representation
        binaire sous forme de chaine de caractères.'''
        if a == 0:
            return ...
        bin_a = ...
        while ... :
            bin_a = ... + bin_a
            a = ...
        return bin_a
    ```

    Exemples :

    ```python
    >>> binaire(83)
    '1010011'
    >>> binaire(127)
    '1111111'
    >>> binaire(0)
    '0'
    ```

??? question "Exercice - 3 (EP 24-16-01)"

    Écrire une fonction `ecriture_binaire_entier_positif` qui prend en paramètre un
    entier positif `n` et renvoie une une chaine de caractère correspondant à l‘écriture binaire de `n`.

    On rappelle que :

    - l’écriture binaire de 25 est 11001 car $25 = 1 \times 2^4 + 1 \times 2^3 + 0 \times 2^2 + 0 \times 2^1 + 1 \times 2^0$ ;
    - `n % 2` vaut 0 ou 1 selon que `n` est pair ou impair ;
    - `n // 2`  donne le quotient de la division euclidienne de `n` par 2.

    Il est interdit dans cet exercice d’utiliser la fonction `bin` de Python.

    Exemples :

    ```python
    >>> 5 % 2
    1
    >>> 5 // 2
    2
    >>> ecriture_binaire_entier_positif(0)
    '0'
    >>> ecriture_binaire_entier_positif(2)
    '10'
    >>> ecriture_binaire_entier_positif(105)
    '1101001'
    ```

!!! question "Exercice - 4 (EP 24-26-02)"

    On considère une piste carrée qui contient 4 cases par côté. Les cases sont numérotées de 0 inclus à 12 exclu comme ci-dessous :

    [![A compléter](../Image/20_carre.png){.Center_lien }](../Image/20_carre.png)


    L’objectif de l’exercice est d’implémenter le jeu suivant :  
    Au départ, le joueur place son pion sur la case 0. A chaque coup, il lance un dé équilibré à six faces et avance son pion d’autant de cases que le nombre indiqué par le dé (entre 1 et 6 inclus) dans le sens des aiguilles d’une montre.  
    Par exemple, s’il obtient 2 au premier lancer, il pose son pion sur la case 2 puis s’il obtient 6 au deuxième lancer, il le pose sur la case 8, puis s’il obtient à nouveau 6, il pose le pion sur la case 2.  
    Le jeu se termine lorsque le joueur a posé son pion sur **toutes les cases** de la piste.  
    Compléter la fonction `nombre_coups` ci-dessous de sorte qu’elle renvoie le nombre de lancers aléatoires nécessaires pour terminer le jeu.

    Proposer ensuite quelques tests pour en vérifier le fonctionnement.

    ```python linenums='1'
    from random import randint

    def nombre_coups():
        '''Simule un jeu de plateau avec 12 cases et renvoie le nombre
        minimal de coups pour visiter toutes les cases.'''
        nombre_cases = 12
        # indique si une case a été vue
        cases_vues = [ False ] * nombre_cases
        nombre_cases_vues = 1
        cases_vues[0] = True
        case_en_cours = 0
        n = ... 
        while ... < ...: 
            x = randint(1, 6)
            case_en_cours = (case_en_cours + ...) % ... 
            if ...: 
                cases_vues[case_en_cours] = True
                nombre_cases_vues = ... 
            n = ... 
        return n
    ``` 
