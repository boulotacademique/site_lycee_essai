# Python<br>Les dictionnaires

!!! question "Exercice - (EP 24-02-02)"
    On considère au plus 26 personnes A, B, C, D, E, F ... qui peuvent s'envoyer des messages avec deux règles à respecter :

    - chaque personne ne peut envoyer des messages qu'à une seule personne (éventuellement elle-même),
    - chaque personne ne peut recevoir des messages qu'en provenance d'une seule personne (éventuellement elle-même).

    Voici un exemple - avec 6 personnes - de « plan d'envoi des messages » qui respecte les règles ci-dessus, puisque chaque personne est présente une seule fois dans chaque colonne :

    - A envoie ses messages à E
    - E envoie ses messages à B
    - B envoie ses messages à F
    - F envoie ses messages à A
    - C envoie ses messages à D
    - D envoie ses messages à C

    Et le dictionnaire correspondant à ce plan d'envoi est le suivant :  
    `plan_a = {'A':'E', 'B':'F', 'C':'D', 'D':'C', 'E':'B', 'F':'A'}`.  
    Un cycle est une suite de personnes dans laquelle la dernière est la même que la première.  
    Sur le plan d'envoi `plan_a` des messages ci-dessus, il y a deux cycles distincts : un premier cycle avec A, E, B, F et un second cycle avec C et D.  
    En revanche, le plan d’envoi `plan_b` ci-dessous : `plan_b = {'A':'C', 'B':'F', 'C':'E', 'D':'A', 'E':'B', 'F':'D'}` comporte un unique cycle : A, C, E, B, F, D. Dans ce cas, lorsqu’un plan d’envoi comporte un *unique cycle*, on dit que le plan d’envoi est *cyclique*.  
    Pour savoir si un plan d'envoi de messages comportant N personnes est cyclique, on peut utiliser l'algorithme ci-dessous :

    - on part d’un expéditeur (ici A) et on inspecte son destinataire dans le plan d'envoi,
    - chaque destinataire devient à son tour expéditeur, selon le plan d’envoi, tant qu’on ne « retombe » pas sur l’expéditeur initial,
    - le plan d’envoi est cyclique si on l’a parcouru en entier.

    Compléter la fonction `est_cyclique` en respectant la spécification.  
    On rappelle que la fonction Python `len` permet d'obtenir la longueur d'un dictionnaire.  

    ```python linenums='1'
    def est_cyclique(plan):
        '''Prend en paramètre un dictionnaire `plan` correspondant à 
        un plan d'envoi de messages (ici entre les personnes A, B, C,
        D, E, F).
        Renvoie True si le plan d'envoi de messages est cyclique et 
        False sinon.'''
        expediteur = 'A'
        destinataire = plan[...] 
        nb_destinataires = 1

        while destinataire != expediteur:
            destinataire = ... 
            nb_destinataires = ... 

        return nb_destinataires == ... 
    ```

    Exemples :

    ```python
    >>> est_cyclique({'A':'E', 'F':'A', 'C':'D', 'E':'B', 'B':'F', 'D':'C'})
    False
    >>> est_cyclique({'A':'E', 'F':'C', 'C':'D', 'E':'B', 'B':'F', 'D':'A'})
    True
    >>> est_cyclique({'A':'B', 'F':'C', 'C':'D', 'E':'A', 'B':'F', 'D':'E'})
    True
    >>> est_cyclique({'A':'B', 'F':'A', 'C':'D', 'E':'C', 'B':'F', 'D':'E'})
    False
    ``` 

!!! question "Exercice - (EP 24-06-02)"
    On considère dans cet exercice l’élection d’un vainqueur à l’issue d’un vote. Les résultats du vote sont stockés dans un tableau : chaque vote exprimé est le nom d’un ou d’une candidate.  
    Par exemple, les résultats pourraient correspondre au tableau :

    ```python
    urne = ['A', 'A', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B']
    ```

    indiquant que 3 candidats ont obtenu au moins un vote chacun : A, B et C.

    On cherche à déterminer le ou les candidats ayant obtenu le plus de suffrages. Pour cela, on propose d’écrire deux fonctions :

    La fonction depouille doit permettre de compter le nombre de votes exprimés pour chaque artiste. Elle prend en paramètre un tableau et renvoie le résultat dans un dictionnaire dont les clés sont les noms des issues et les valeurs le nombre de votes en leur faveur.  
    La fonction vainqueurs doit désigner le nom du ou des gagnants. Elle prend en paramètre un dictionnaire non vide dont la structure est celle du dictionnaire renvoyé par la fonction depouille et renvoie un tableau. Ce tableau peut donc contenir plusieurs éléments s’il y a des artistes ex- aequo. Compléter les fonctions depouille et vainqueurs ci-après pour qu’elles renvoient les résultats attendus.

    ```python
    def depouille(urne):
        '''prend en paramètre une liste de suffrages et renvoie un 
        dictionnaire avec le nombre de voix pour chaque candidat'''
        resultat = ... 
        for bulletin in urne:
            if ...: 
                resultat[bulletin] = resultat[bulletin] + 1
            else:
                ...
        return resultat

    def vainqueurs(election):
        '''prend en paramètre un dictionnaire non vide avec le nombre de voix
        pour chaque candidat et renvoie la liste des vainqueurs'''
        nmax = 0
        for candidat in election:
            if ... > ... : 
                nmax = ... 
        liste_finale = [ nom for nom in election if ... ] 
        return ... 
    ```

    Exemples d’utilisation :

    ```python
    >>> depouille([ 'A', 'B', 'A' ])
    {'A': 2, 'B': 1}
    >>> depouille([])
    {}
    >>> election = depouille(['A', 'A', 'A', 'B', 'C',
    'B', 'C', 'B', 'C', 'B'])
    >>> election
    {'A': 3, 'B': 4, 'C': 3}
    >>> vainqueurs(election)
    ['B']
    >>> vainqueurs({ 'A' : 2, 'B' : 2, 'C' : 1})
    ['A', 'B']
    ``` 

!!! question "Exercice - (EP 24-22-02)"
    Une professeure de NSI décide de gérer les résultats de sa classe sous la forme d’un dictionnaire :

    - les clefs sont les noms des élèves ;
    - les valeurs sont des dictionnaires dont les clefs sont les types d’épreuves sous forme de chaîne de caractères et les valeurs sont les notes obtenues associées à leurs coefficients dans une liste.

    Avec :

    ```python
    resultats = {'Dupont': {
                            'DS1': [15.5, 4],
                            'DM1': [14.5, 1],
                            'DS2': [13, 4],
                            'PROJET1': [16, 3],
                            'DS3': [14, 4]
                        },
                'Durand': {
                            'DS1': [6 , 4],
                            'DS2': [8, 4],
                            'PROJET1': [9, 3],
                            'IE1': [7, 2],
                            'DS3': [12, 4]
                        }
                }
    ```

    L’élève dont le nom est Durand a ainsi obtenu au DS2 la note de 8 avec un coefficient 4.  
    Le professeur crée une fonction moyenne qui prend en paramètre le nom d’un de ses élèves et renvoie sa moyenne arrondie au dixième. Si l’élève n’a pas de notes, on considère que sa moyenne est nulle. Si le nom donné n’est pas dans les résultats, la fonction renvoie `None`.

    Compléter le code de la professeure ci-dessous :

    ```python
    def moyenne(nom, resultats):
        '''Renvoie la moyenne de l'élève nom, selon le dictionnaire 
        resultats. Si nom n'est pas dans le dictionnaire, 
        la fonction renvoie None.'''
        if nom in ...: 
            notes = resultats[nom]
            if ...: # pas de notes 
                return 0
            total_points = ... 
            total_coefficients = ... 
            for ...  in notes.values(): 
                note, coefficient = valeurs
                total_points = total_points + ... * coefficient 
                ... = ... + coefficient 
            return round( ... / total_coefficients, 1 ) 
        else:
            return None
    ```

    Exemples :

    ```python
    >>> moyenne("Dupont", resultats)
    14.5
    >>> moyenne("Durand", resultats)
    8.5
    ``` 

!!! question "Exercice - (EP 24-26-01)"
    Écrire une fonction `ajoute_dictionnaires` qui prend en paramètres deux dictionnaires `d1` et `d2` dont les clés sont des nombres et renvoie le dictionnaire `d` défini de la façon suivante :

    - Les clés de `d` sont celles de `d1` et celles de `d2` réunies.
    - Si une clé est présente dans les deux dictionnaires `d1` et `d2`, sa valeur associée dans le dictionnaire `d` est la somme de ses valeurs dans les dictionnaires `d1` et `d2`.
    - Si une clé n’est présente que dans un des deux dictionnaires, sa valeur associée dans le dictionnaire `d` est la même que sa valeur dans le dictionnaire où elle est présente.

    Exemples :

    ```python
    >>> ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11})
    {1: 5, 2: 16, 3: 11}
    >>> ajoute_dictionnaires({}, {2: 9, 3: 11})
    {2: 9, 3: 11}
    >>> ajoute_dictionnaires({1: 5, 2: 7}, {})
    {1: 5, 2: 7}
    ```

!!! question "Exercice - (EP 24-34-01)"
    Le nombre d’occurrences d’un caractère dans une chaîne de caractère est le nombre d’apparitions de ce caractère dans la chaîne.

    Exemples :

    - le nombre d’occurrences du caractère `‘o’` dans `‘bonjour’` est 2 ;
    - le nombre d’occurrences du caractère `‘b’` dans `‘Bébé’` est 1 ;
    - le nombre d’occurrences du caractère `‘B’` dans `‘Bébé’` est 1 ;
    - le nombre d’occurrences du caractère `‘ ‘` dans `‘Hello world !’` est 2.

    On cherche les occurrences des caractères dans une phrase. On souhaite stocker ces occurrences dans un dictionnaire dont les clefs seraient les caractères de la phrase et les valeurs le nombre d’occurrences de ces caractères.  
    Par exemple : avec la phrase `'Hello world !'` le dictionnaire est le suivant :

    `{'H': 1,'e': 1,'l': 3,'o': 2,' ': 2,'w': 1,'r': 1,'d': 1,'!': 1}`

    *L’ordre des clefs n’a pas d’importance.*

    Écrire une fonction `nbr_occurrences` prenant comme paramètre une chaîne de caractères `chaine` et renvoyant le dictionnaire des nombres d’occurrences des caractères de cette chaîne.

!!! question "Exercice - (EP 24-40-01)"
    On considère des tables, c’est-à-dire des tableaux de dictionnaires ayant tous les mêmes clés, qui contiennent des enregistrements relatifs à des animaux hébergés dans un refuge. Les attributs des enregistrements sont `'nom'`, `'espece'`, `'age'`, `'enclos'`.

    Voici un exemple d'une telle table :

    ```python
    animaux = [ {'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2},
                {'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5},
                {'nom':'Tom', 'espece':'chat', 'age':7, 'enclos':4},
                {'nom':'Belle', 'espece':'chien', 'age':6, 'enclos':3},
                {'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]
    ```

    Programmer une fonction `selection_enclos` qui :

    - prend en paramètres :

        - une table `animaux` contenant des enregistrements relatifs à des animaux (comme dans l'exemple ci-dessus),
        - un numéro d'enclos `num_enclos` ;

    - renvoie une table contenant les enregistrements de `animaux` dont l'attribut `'enclos'` est `num_enclos`.

    Exemples avec la table `animaux` ci-dessus :

    ```python
    >>> selection_enclos(animaux, 5)
    [{'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5},
    {'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]

    >>> selection_enclos(animaux, 2)
    [{'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2}]

    >>> selection_enclos(animaux, 7)
    []
    ```

!!! question "Exercice - (EP 24-47-01)"
    Sur le réseau social TipTop, on s’intéresse au nombre de « like » des abonnés. Les données sont stockées dans des dictionnaires où les clés sont les pseudos et les valeurs correspondantes sont les nombres de « like » comme ci-dessous :

    `{'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}`

    Écrire une fonction `max_dico` qui :

    - Prend en paramètre un dictionnaire `dico` non vide dont les clés sont des chaînes de caractères et les valeurs associées sont des entiers ;
    - Renvoie un tuple dont :

        - La première valeur est une clé du dictionnaire associée à la valeur maximale ;
        - la seconde valeur est cette valeur maximale.

    Exemples :

    ```python
    >>> max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50})
    ('Ada', 201)
    >>> max_dico({'Alan': 222, 'Ada': 201, 'Eve': 220, 'Tim': 50})
    ('Alan', 222)
    ```