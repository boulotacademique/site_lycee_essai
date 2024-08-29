# Python<br>Utilisation des chaînes de caractères

!!! bug "Objectif"
    
    - Utiliser des fonctions
    - Manipuler des chaines de caractères
    - Découvrir des fonctionnalités (non exigibles dans le programme) mais indispensables pour un programmeur

## Des petites fonctions utiles

???- tip "Rappel"

    - Le retour à la ligne est un caractère spécial : `\n`

!!! question "Exercice - 1"

    1. Ecrire la fonction ```repete_ch``` qui prend en argument une chaine ```ch``` et un entier ```nb``` et qui retourne une chaine contenant ```ch``` répétée ```nb``` fois.  
    Signature `fonction repet_ch(ch : str, nb : int) : str`  
    Ainsi, par exemple, `repete_ch('Hello',5)` renvoie `HelloHelloHelloHelloHello`.
    2. Utiliser la fonction ```repete_ch``` et une boucle pour écrire :  
    ```python
    ron
    ronron
    ronronron
    ronronronron
    ronronronronron
    ronronronronronron
    ```  
    3. Ecrire la fonction ```ecrit_pyr``` qui utilise la fonction ```repete_ch``` et qui fait comme l'exemple précédent.  
    Voici sa signature `fonction ecrit_pyr(ch : str, nb_lig : int) : rien`.  
    Cette fonction ne retourne rien, car nous allons utiliser des ```print```.  
    Ne pas oublier le commentaire.  
    L'essayer avec des chaines différentes et des nombres de lignes différents.

!!! question "Exercice - 2"

    1. Ecrire une fonction qui supprime, dans une chaine de caractères, toutes les occurrences d'un caractère précis.  
    Signature : `Fonction enlever_car(mot : str, car : str) : str`  
    Exemple :
    ```python
    un_mot="Bonjour a tous !"
    print(enlever_car(un_mot,'o'))
    ```
    affiche
    ```python
    Bnjur a tus !
    ```  
    2. Il faut écrire une fonction qui remplace, dans une chaine de caractères, toutes les occurrences d'un caractère précis par un caractère ou  une chaine de caractères.  
    Signature : `Fonction remplace_car(mot : str, car_a_enl : str, car_de_rempl : str) : str`  
    Exemple :
    ```python
    un_mot="Bonjour a tous !"
    print(remplace_car(un_mot,'o', 'ananas'))
    ```
    affiche
    ```python
    Bananasnjananasur a tananasus !
    ```

    {{ IDE() }}

!!! question "Exercice - 3"

    1. Ecrire une fonction qui prend en argument une chaine et qui retourne la chaine dans l'ordre inverse.
    Signature `fonction retourne_mot(mot : str) -> str`  
    Par exemple,  
    ```python
    un_mot="Bonjour a tous !"
    print(retourne_mot(un_mot))
    ```  
    affiche `! suot a ruojnoB`  
    2. Ecrire une fonction qui prend en argument une chaine de caractère et qui retourne ```True``` si il s'agit d'un palindrome (c'est à dire une chaine qui peut se lire de droite à gauche ou de gauche à droite, sans tenir compte des accents, des espaces ou des majuscules).  
    Signature `fonction est_palindrome(mot : str) : bool`  
    Par exemple,  
    ```python
    print(est_palindrome('KAYAK')) # Affiche `True`
    print(est_palindrome('Bonjour')) # Affiche `False`
    ```  

    {{ IDE() }}  

!!! question "Exercice - 4"
    Revenons sur la tortue !

    On souhaite dessiner un chemin selon un code basé sur des lettres :

    - `F` : fait avancer la tortue de $dist$ (distance précisée à l'avance)
    - '+` : fait tourner à gauche de l'angle $angle$ (mesure précisée à l'avance)
    - '-` : fait tourner à droite de l'angle $angle$ (mesure précisée à l'avance)

    Par ailleurs, chaque avancée de la tortue sera alternativement rouge puis noir (couleurs à choisir).

    Ecrire une fonciton qui fait cela. Voici sa signature :  
    `fonction tracer_chaine(mot : str, coul1 : str, coul2 : str, dist : int, angle) : None`

    Par exemple, `tracer("F+F-F-F+F", "red", "black", 100, 90)` affiche  

    [![L_systeme 01](../Image/L_syst_01.png){.Center_lien }](../Image/L_syst_01.png)

## A propos de la bibliothèque ```random```

La bibliothèque ```random``` permet d'exploiter l'aléatoire. En particulier, ```random.randint(a,b)``` renvoie un entier $N$ aléatoirement choisi tel que $a \leq N \leq b$.

!!! question "Exercice - 5"

    1. Voici un programme :
    ```python
    import random

    mot = "Bonjour"
    idx_alea = random.randint(0, len(mot) - 1)
    car_alea = mot[idx_alea]
    print(car_alea)
    ```  
        1. Que fait ce programme ? 
        2. Que se serait-il passé si on avait écrit : `idx_alea = random.randint(0, len(mot))` (faire éventuellement plusieurs essais pour voir apparaitre un problème).
    2. Ecrire une fonction qui renvoie un mot (qui n'a pas forcément de sens) de taille `taille` dont les caractères sont choisis aléatoirement dans `car_possible`.  
    Signature `fonction mot_alea(taille : int, car_possible : str) : str`  
    Par exemple,  
    ```python
    c_p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(mot_alea(5,c_p)) # Affiche un mot de 5 lettres
    ```  
    Par exemple,  
    ```python
    c_p = "0123456789"
    print(mot_alea(8,c_p)) # Affiche un code à 8 chiffres
    ```

## Epreuve pratique


!!! question "Exercice (EP 24-11-01)"
    Dans cet exercice, on considère des phrases composées de mots.

    - On appelle « mot » une chaîne de caractères composée avec des caractères choisis parmi les 26 lettres minuscules ou majuscules de l'alphabet,
    - On appelle *phrase* une chaîne de caractères :
    - 
        - composée avec un ou plusieurs *mots* séparés entre eux par un seul caractère espace `' '`,
        - se finissant :

            - soit par un point `'.'` qui est alors collé au dernier mot,
            - soit par un point d'exclamation `'!'` ou d'interrogation `'?'` qui est alors séparé du dernier mot par un seul caractère espace `' '`.

    Voici deux exemples de phrases :

    - 'Cet exercice est simple.'
    - 'Le point d exclamation est separe !'

    Après avoir remarqué le lien entre le nombre de mots et le nombres de caractères espace dans une phrase, programmer une fonction `nombre_de_mots` qui prend en paramètre une phrase et renvoie le nombre de mots présents dans cette phrase.

    ```python
    >>> nombre_de_mots('Cet exercice est simple.')
    4
    >>> nombre_de_mots('Le point d exclamation est séparé !')
    6
    >>> nombre_de_mots('Combien de mots y a t il dans cette phrase ?')
    10
    >>> nombre_de_mots('Fin.')
    1
    ```



!!! question "Exercice (EP 24-02-01)"

    On considère des chaînes de caractères contenant uniquement des majuscules et des caractères `*` appelées *mots à trous*.  
    Par exemple `INFO*MA*IQUE`, `***I***E**` et `*S*` sont des mots à trous.  
    Programmer une fonction `correspond` qui :

    - prend en paramètres deux chaînes de caractères `mot` et `mot_a_trous` où `mot_a_trous` est un mot à trous comme indiqué ci-dessus, 
    - renvoie :

        - `True` si on peut obtenir `mot` en remplaçant convenablement les caractères `'*'` de `mot_a_trous`.
        - `False` sinon.

    Exemple :

    ```python
    >>> correspond('INFORMATIQUE', 'INFO*MA*IQUE')
    True
    >>> correspond('AUTOMATIQUE', 'INFO*MA*IQUE')
    False
    >>> correspond('STOP', 'S*')
    False
    >>> correspond('AUTO', '*UT*')
    True
    ```

!!! question "Exercice (EP 24-33-01)"

    Programmer une fonction `renverse`, prenant en paramètre une chaîne de caractères `mot` et renvoie cette chaîne de caractères en ordre inverse.

    Exemple :

    ```python
    >>> renverse("")
    ""
    >>> renverse("abc")
    "cba"
    >>> renverse("informatique")
    "euqitamrofni"
    ```

!!! question "Exercice (EP 24-35-02)"

    Un mot palindrome peut se lire de la même façon de gauche à droite ou de droite à gauche : *kayak*, *radar*, et *non* sont des mots palindromes.  
    De même certains nombres ont des écritures décimales qui sont des palindromes : 33, 121, 345543.

    L’objectif de cet exercice est d’obtenir un programme Python permettant de tester si un nombre est un nombre palindrome.

    Pour remplir cette tâche, on vous demande de compléter le code des trois fonctions ci-dessous qui s’appuient les unes sur les autres :

    - `inverse_chaine` : qui renvoie une chaîne de caractères inversée ;
    - `est_palindrome` : qui teste si une chaîne de caractères est un palindrome ;
    - `est_nbre_palindrome` : qui teste si un nombre est un palindrome.

    Compléter le code des trois fonctions ci-dessous.

    ```python linenums='1'
    def inverse_chaine(chaine):
        '''Retourne la chaine inversée'''
        resultat = ... 
        for caractere in chaine:
            resultat = ... 
        return resultat

    def est_palindrome(chaine):
        '''Renvoie un booléen indiquant si la chaine ch
        est un palindrome'''
        inverse = inverse_chaine(chaine)
        return ... 

    def est_nbre_palindrome(nbre):
        '''Renvoie un booléen indiquant si le nombre nbre 
        est un palindrome'''
        chaine = ... 
        return est_palindrome(chaine)
    ```

    Exemples :

    ```
    >>> inverse_chaine('bac')
    'cab'
    >>> est_palindrome('NSI')
    False
    >>> est_palindrome('ISN-NSI')
    True
    >>> est_nbre_palindrome(214312)
    False
    >>> est_nbre_palindrome(213312)
    True
    ``` 


!!! question "Exercice - 6 (EP 24-36-01)"

    Écrire une fonction `occurrences(caractere, chaine)` qui prend en paramètres `caractere`, une chaîne de caractère de longueur 1, et `chaine`, une chaîne de caractères.  
    Cette fonction renvoie le nombre d’occurrences de `caractere` dans `chaine`, c’est-à-dire le nombre de fois où `caractere` apparaît dans `chaine`.

    Exemples :
    ```python
    >>> occurrences('e', "sciences")
    2
    >>> occurrences('i',"mississippi")
    4
    >>> occurrences('a',"mississippi")
    0
    ```

!!! question "Exercice - 7 (EP 24-46-02)"

    Le codage de César transforme un message en changeant chaque lettre en la décalant dans l’alphabet.  
    Par exemple, avec un décalage de 3, le A se transforme en D, le B en E, ..., le X en A, le Y en B et le Z en C. Les autres caractères (‘!’,’ ?’ ...) ne sont pas codés.

    La fonction `position_alphabet` ci-dessous prend en paramètre un caractère `lettre` et renvoie la position de `lettre` dans la chaîne de caractères `alphabet` s’il s’y trouve.  
    La fonction `cesar` prend en paramètres une chaîne de caractères `message` et un nombre entier `decalage` et renvoie le nouveau message codé avec le codage de César utilisant le décalage `decalage`.  

    ```python linenums='1'
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def position_alphabet(lettre):
        '''Renvoie la position de la lettre dans l'alphabet'''
        return ord(lettre) - ord('A')

    def cesar(message, decalage):
        '''Renvoie le message codé par la méthode de César
        pour le decalage donné'''
        resultat = ''
        for ... in message: 
            if 'A' <= c and c <= 'Z':
                indice = (...) % 26 
                resultat = resultat + alphabet[indice]
            else:
                resultat = ... 
        return resultat
    ```

    Compléter la fonction `cesar`.

    Exemples

    ```python
    >>> cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4)
    'FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !'
    >>> cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5)
    'BONJOUR A TOUS. VIVE LA MATIERE NSI !'
    ```

!!! question "Exercice - 8 (EP 24-48-02)"

    On considère dans cet exercice la suite de nombre suivante : 1, 11, 21, 1211, 111221, ...

    Cette suite est construite ainsi : pour passer d’une valeur à la suivante, on la lit et on l’écrit sous la forme d’un nombre. Ainsi, pour 1211 :

    - on lit *un 1, un 2, deux 1* ;
    - on écrit donc en nombre *1 1, 1 2, 2 1* ;
    - puis on concatène *111221*.

    Compléter la fonction `nombre_suivant` qui prend en entrée un nombre sous forme de
    chaine de caractères et qui renvoie le nombre suivant par ce procédé, encore sous forme de
    chaîne de caractères.

    ```python linenums='1'
    def nombre_suivant(s):
        '''Renvoie le nombre suivant de celui representé par s
        en appliquant le procédé de lecture.'''
        resultat = ''
        chiffre = s[0]
        compte = 1
        for i in range(...): 
            if s[i] == chiffre:
                compte = ... 
            else:
                resultat += ... + ... 
                chiffre = ... 
                ...
        lecture_... = ... + ... 
        resultat += lecture_chiffre
        return resultat
    ```

    Exemples :

    ```python
    >>> nombre_suivant('1211')
    '111221'
    >>> nombre_suivant('311')
    '1321'
    ```
