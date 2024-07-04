# Python<br>Les mutables

!!! question "Exercice - (EP 24-10-01)"
    Dans cet exercice on cherche à calculer la moyenne pondérée d’un élève dans une matière donnée. Chaque note est associée à un coefficient qui la pondère.  
    Par exemple, si ses notes sont : 14 avec coefficient 3, 12 avec coefficient 1 et 16 avec coefficient 2, sa moyenne pondérée sera donnée par  
    $$\dfrac{14 \times 3 + 12 \times 1 + 16 \times 2}{3+1+2}=14,333... $$

    Écrire une fonction `moyenne` :

    - qui prend en paramètre une liste notes non vide de tuples à deux éléments entiers de la forme `(note, coefficient)` (`int` ou `float`) positifs ou nuls ;
    - et qui renvoie la moyenne pondérée des notes de la liste sous forme de flottant si la somme des coefficients est non nulle, `None` sinon.

    Exemple :

    ```python
    >>> moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)])
    9.142857142857142
    >>> moyenne([(3, 0), (5, 0)])
    None
    ```

!!! question "Exercice - (EP 24-14-01)"
    Écrire une fonction `min_et_max` qui prend en paramètre un tableau de nombres `tab` non vide, et qui renvoie la plus petite et la plus grande valeur du tableau sous la forme d’un dictionnaire à deux clés `min` et `max`.  
    Les tableaux seront représentés sous forme de liste Python.  
    L’utilisation des fonctions natives `min`, `max` et `sorted`, ainsi que la méthode `sort` n’est pas
    autorisée.

    Exemples :

    ```python
    >>> min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1])
    {'min': -2, 'max': 9}
    >>> min_et_max([0, 1, 2, 3])
    {'min': 0, 'max': 3}
    >>> min_et_max([3])
    {'min': 3, 'max': 3}
    >>> min_et_max([1, 3, 2, 1, 3])
    {'min': 1, 'max': 3}
    >>> min_et_max([-1, -1, -1, -1, -1])
    {'min': -1, 'max': -1}
    ```

!!! question "Exercice - (EP 24-19-02)"
    On affecte à chaque lettre de l'alphabet un code selon le tableau ci-dessous :

    | A | B | C | D | E | F | G | H | I | J | K | L | M |
    |:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
    | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |


    | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | 
    |:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
    | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 

    Cette table de correspondance est stockée dans un dictionnaire `dico` où les clés sont les lettres de l’alphabet et les valeurs les codes correspondants.

    ```python
    dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
            "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
            "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
            "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
            "W": 23, "X": 24, "Y": 25, "Z": 26}
    ```

    Pour un mot donné, on détermine d’une part son code alphabétique concaténé, obtenu par la juxtaposition des codes de chacun de ses caractères, et d’autre part, son code additionné, qui est la somme des codes de chacun de ses caractères.  
    Par ailleurs, on dit que ce mot est « parfait » si le code additionné divise le code concaténé.

    Exemples :

    Pour le mot "PAUL", le code concaténé est la chaîne '1612112', soit l’entier 1 612 112. Son code additionné est l’entier 50 car 16 + 1 + 21 + 12 = 50. 50 ne divise pas l’entier 1 612 112 ; par conséquent, le mot "PAUL" n’est pas parfait.  
    Pour le mot "ALAIN", le code concaténé est la chaîne '1121914', soit l’entier 1 121 914. Le code additionné est l’entier 37 car 1 + 12 + 1 + 9 + 14 = 37. 37 divise l’entier 1 121 914 ; par conséquent, le mot "ALAIN" est parfait.  
    Compléter la fonction codes_parfait située à la page suivante et qui prend en paramètre un mot en majuscule et renvoie un triplet constitué du code additionné, du code concaténé et d’un booléen indiquant si le mot est parfait ou non.  
    On rappelle que pour tester si un entier a divise un entier b, on utilise l’opérateur modulo b % a qui renvoie le reste de la division euclidienne de b par a. Sib % a vaut 0, alors a divise b.

    ```python
    def codes_parfait(mot):
        """Renvoie un triplet 
        (code_additionne, code_concatene, mot_est_parfait) où :
        - code_additionne est la somme des codes des lettres du mot ;
        - code_concatene est le code des lettres du mot concaténées ;
        - mot_est_parfait est un booléen indiquant si le mot est parfait."""
        code_concatene = ""
        code_additionne = ... 
        for c in mot:
            code_concatene = code_concatene + ... 
            code_additionne = code_additionne + ... 
        code_concatene = int(code_concatene)
        mot_est_parfait = ... 
        return code_additionne, code_concatene, mot_est_parfait
    ```

    Exemples :

    ```python
    >>> codes_parfait("PAUL")
    (50, 1612112, False)
    >>> codes_parfait("ALAIN")
    (37, 1121914, True)
    ``` 
