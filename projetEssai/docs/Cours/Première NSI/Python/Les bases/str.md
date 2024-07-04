# Python<br>Les chaînes de caractères : str

## Les indices

!!! info "A retenir"

    Une chaîne de caractère est de type ```str```. Elle peut être écrite 
    
    - entre des guillemets simples ``` 'Bonjour !' ```
    - entre des guillemets doubles ``` "Bonjour !" ```
    - entre des guillemets doubles répétés trois fois ``` """Bonjour !""" ```
  
    Dans une chaîne, chaque caractère est repéré par un indice !

    
    <div class = "Center_seul">
    
    |chaîne :|B|o|n|j|o|u|r| |!|
    |:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
    |Indice : |0|1|2|3|4|5|6|7|8|

    </div>

!!! warning "Attention"

    En python, les indices commencent toujours **à 0 !**

!!! tip "A connaître"

    Dans tout ce qui suit, on utilise l'exemple suivant :

    ```python
    mot = "Bonjour !"
    ```

    - connaitre le nombre de caractères ou la longueur d'une chaîne : ```len(mot)``` correspond à ```9```
    - accéder à un caractère à partir de son indice : ```mot[2]``` correspond à ```n```
    - accéder aux derniers caractères : ```mot[len(mot)-1]``` correspond à ```!```. On peut aussi écrire ```mot[-1]```
    - accéder à une tranche : ```mot[2:5]``` correspond aux caractères dont les indices sont supérieurs ou égaux à 2 et **strictement inférieur** à 5. Ainsi, ```mot[2:5]``` correspond à ```njo```
    - accéder à une tranche contenant les premiers caractères : ```mot[0:5]``` correspond aux 5 premiers caractères (dont les indices sont supérieurs ou égaux à 0 et **strictement inférieur** à 5). Ainsi, ```mot[0:5]``` correspond à ```Bonjo```. On peut aussi écrire ```mot[:5]```
    - accéder à une tranche depuis le dernier caractère : ```mot[len(mot)-3:len(mot)]``` correspond aux 3 derniers caractères. Ainsi, ```mot[len(mot)-3:len(mot)]``` correspond à ```r !```. On peut aussi écrire ```mot[-3:]`
    - accéder à toute la chaîne sauf les derniers : ```mot[0:len(mot)-5]``` correspond à toute la chaîne **sauf** les 5 derniers caractères. Ainsi, ```mot[0:len(mot) - 5]``` correspond à ```Bonj```. On peut aussi écrire ```mot[:-5]```

    {{ IDEv('Python_base_code/str_01', MAX = 1000) }}

!!! warning "Attention"

    Le nombre de caractères **ne correspond pas** au dernier indice ! En effet, le dernier indice est toujours ```len(...) - 1```.

## Concaténation et répétition

Dans tout ce qui suit, on utilise l'exemple suivant :
    
```python
mot = "Bonjour !"
mot_suiv = "Tout le monde !"
```

!!! info "Concaténation"

    La <span class = "Gras" id = "concat">concaténation</span> consiste à coller plusieurs chaines de caractères. Cela s'effectue à l'aide du symbole ```+```. Ainsi, ```mot + " " + mot_suiv``` correspond à ```Bonjour ! Tout le monde !```

!!! info "Répétition"

    Pour <span class = "Gras" id = "repet_str">répéter une chaine</span>: ```mot*2``` correspond à ```'Bonjour !Bonjour !'``` et ```"a"*5``` correpsond à ```aaaaa```

!!! warning "Attention"

    Il faut avoir uniquement des ```str``` pour une concaténation ! Par exemple {-- ```"Bonjour```+1000 --} déclenche une erreur : ```TypeError: can only concatenate str (not "int") to str```

!!! info "Transtypage"

    Il est possible de transformer presque tous les types en ```str``` en utilisant la fonction ```str``` ! C'est un <span class = "Gras" id = "cast">transtypage</span>.

    ```python
    mot = "Bonjour " + str(1000)
    print(mot) # Affiche Bonjour 1000
    ```

    {{ IDEv('Python_base_code/str_02', MAX = 1000) }}

## Manipulation des chaînes de caractères

### Parcourir une chaîne de caractères

!!! info "Parcourir une chaîne de caractères avec des indices"

    Pour récupérer les caractères d'une chaîne les uns après les autres **avec les indices**, il faut utiliser une boucle ```for```, la fonction ```range``` et la longueur de la chaîne.

    ```python
    mot = "Bonjour !"
    for idx in range(len(mot)):
        car = mot[idx]
        print(car)
    ```

    affiche

    <div class = "Center_ss_bd" style="width:10%;">

    ```python
    B
    o
    n
    j
    o
    u
    r

    !
    ```

    </div>

Il est aussi possible de ne pas passer par la variable ```car``` :

```python
mot = "Bonjour !"
for idx in range(len(mot)):
    print(mot[idx])
```

???- tip "Parcourir une chaîne de caractères sans les indices"

    Pour récupérer les caractères d'une chaîne les uns après les autres **sans les indices**, il faut seulement utiliser une boucle ```for``. Il est alors plus difficile d'accéder aux indices !

    ```python
    mot = "Bonjour !"
    for car in mot:
        print(car)
    ```

    affiche

    <div class = "Center_ss_bd" style="width:10%;">

    ```python
    B
    o
    n
    j
    o
    u
    r

    !
    ```

    </div>

## Modifier une chaîne de caractères

!!! warning "Attention"

    Une chaîne de caractères (type ```str```) est un [**non mutable**](AFAIRE) (ou **immuable**). Il est donc impossible de modifier facilement un caractère, en faisant par exemple {-- ```mot[2] = "r"``` --} !!

<!--Pour modifier une chaîne de caractères, il est possible d'utiliser les tranches.--> 

Lire et bien travailler les exemples suivants afin de bien les comprendre.

### Créer une chaîne

!!! note "Créer une chaîne de caractères"

    Il suffit de commencer avec une chaîne vide ```""``` et d'accumuler les chaînes de caractères voulues.

    ```python
    mot_cache="SeehccraeCt"
    mot = ""
    for idx in range(len(mot_cache)):
        if idx%2 == 0: # On ne prend que les indices pairs
            mot = mot + mot_cache[idx]	# On accumule les caractères à la fin (à droite)
    print(mot) # affiche Secret
    ```

???- tip "Accumuler au début"

    Il est possible d'accumuler au début (à gauche)

    ```python
    mot_cache="SeehccraeCt"
    mot = ""
    for idx in range(len(mot_cache)):
        if idx%2 == 1: # On ne prend ques les indices impairs
            mot = mot_cache[idx] + mot	# On accumule les caractères au début (à gauche)
    print(mot) # affiche Cache
    ```

### Insérer une chaîne

!!! note "Insérer une chaîne"

    On souhaite insérer une chaîne de caractères (éventuellement un caractère seul) dans une chaîne. Par exemple, on souhaite insérer ```bon``` entre le ```n``` et l'espace dans la chaîne suivante.

    <div class = "Center_seul">
    
    |chaîne : |B|o|n| |!|
    |:-:|:-:|:-:|:-:|:-:|:-:|
    |Indice :|0|1|2|3|4|

    </div>

    Il faut [concaténer](#concat) les caractères :
    
    - dont les indices commencent à 0 et sont **strictement inférieur à 3** (Faite attention à ce dernier point !!!)
    - que l'on souhaite insérer
    - dont les indices vont de l'indice 3 jusqu'au dernier  
    ```python
    mot = "Bon !"
    a_inserer = "bon"
    mot_rep = ""
    for idx in range(3):
        mot_rep = mot_rep + mot[idx]
    for idx in range(len(a_inserer)):
        mot_rep = mot_rep + a_inserer[idx]
    for idx in range(3, len(mot)):
        mot_rep = mot_rep + mot[idx]
    print(mot_rep_) # affiche Bonbon !
    ```

    Remarque : il sera possible de faire la même chose avec une boucle `while` !

???- tip "Avec les tranches"
    On peut aussi utiliser les tranches !
    
    ```python
    mot = "Bon !"
    a_inserer = "bon"
    mot2 = mot[0:3] + a_inserer + mot[3:]
    print(mot2) # affiche Bonbon !
    ```

???- tip "Ajouter une chaîne à la fin"

    Pour ajouter un chaîne à la fin d'une autre chaîne, il est inutile d'utiliser des tranches ! Il suffit de [concaténer](#concat) à droite.

    ```python
    mot = "Hello"
    mot2 = " world !"
    mot3 = mot + mot2
    print(mot3) # affiche Hello world !
    ```

???- tip "Ajouter une chaîne au début"

    Pour ajouter un chaîne au début d'une autre chaîne, il est inutile d'utiliser des tranches ! Il suffit de [concaténer](#concat) à gauche.

    ```python
    mot = "Jedi"
    mot2 = "Maitre "
    mot3 = mot2 + mot
    print(mot3) # affiche Maitre Jedi
    ```

### Modifier un caractère

!!! note "Modifier **un** caractère"

    On souhaite modifier un caractère d'une chaîne. Par exemple, on souhaite corriger ```chebal```.

    <div class = "Center_seul">
    
    |chaîne : |c|h|e|b|a|l|
    |:-:|:-:|:-:|:-:|:-:|:-:|:-:|
    |Indice : |0|1|2|3|4|5|

    </div>

    Un exemple :
    ```python
    mot = "chebal"
    mot_rep = ""
    for idx in range(len(mot)):
        if idx == 3:
            mot_rep = mot_rep + "v"
        else:
            mot_rep = mot_rep + mot[idx]
    print(mot_rep) # affiche cheval !
    ```

???- tip "Avec les tranches"
    On peut aussi utiliser les tranches !

    ```python
    mot = "chebal"
    mot2 = mot[0:3] + "v" + mot[4:] # voyez la différence des indices avec l'insertion de la méthode précédente
    print(mot2) # affiche cheval !
    ```



## Diverses méthodes autour des str

!!!- tip "A retenir en faisant les exercices"

    - ```''``` ou ```""``` (sans espace) : la chaîne vide.
    - les caractères spéciaux : ```\n``` pour le retour à la ligne, ```\t``` pour une tabulation
    - ```'rrr' in C``` : retourne ```True``` si ```'rrr'``` est dans ```C```, ```False``` sinon (cf [les booléens](AFFAIRE) ).
    - ```C.index(x)``` : retourne l'indice de l'élément ```x``` (si il est dans ```C```, sinon il y a un message d'erreur)
    - ```C.find(x)```: retourne l'indice de l'élément ```x``` (si il est dans ```C```, sinon il retourne -1)
    - ```C.count(x)``` : retourne le nombre d’occurrences  de l'élément ```x```. 
    - ```C1 == C2``` : retourne ```True``` si ```C1``` et ```C2``` sont identiques, ```False``` sinon. \textbf{Attention à la casse (majuscule, minuscule) !}

## Les `str` sont des non mutables

!!! note "A retenir"

    Une chaine de caractère est immuable (ou non mutable ou immutable). Elle ne peut être modifiée qu'avec un code de la forme :

    ```python
    ch="un mot"
    ch=ch+" !"
    print(ch)
    ```

    Des opérations de modifications comme ```ch[2]='z'``` ( ou ```ch.append('!')``` méthode pour les listes) provoqueront des erreurs.

!!! abstract "Copie par valeur"

    Ainsi, pour un non mutable, après avoir créé une copie, les modifications de la copie **n'impactent pas** l'original ! *Cela peut paraitre naturel, mais ce n'est pas le cas de toutes les structures.*

    ```python
    mot = "Bonjour"
    print(mot) # Affiche "Bonjour"
    cp_mot = mot
    cp_mot = cp_mot + " à tous !"
    print(mot) # Affiche "Bonjour"
    print(cp_mot) # Affiche "Bonjour à tous !"
    ```

    {{ IDEv() }}  

???- note "Remarque"

    Voici un code (les éléments seront vus plus tard). Comme les listes sont mutables, *certaines méthodes* pour modifier une copie **impactent l'original** !

    ```python
    liste1 = [1,2,3,4]
    print(liste1) # Affiche [1,2,3,4]
    cp_liste1 = liste1
    cp_liste1.append(100)
    print(liste1) # Affiche [1,2,3,4,100]
    print(cp_liste1) # Affiche [1,2,3,4,100]
    ```

    {{ IDEv() }}  

!!! note "A retenir : conséquence avec les fonctions"

    Ainsi, si une chaine de caractères (et plus généralement un non mutable) est passée en argument dans un fonction, des modifications au sein de la fonction n'impacte pas le chaine de caractères passée en argument.

    ```python
    def modif_mot(mot):
        mot = mot + ' ajout'
        print("Dans la fonction la variable mot vaut " + mot)
    
    un_mot = "Hello"
    modif_mot(un_mot)
    print(un_mot)
    ```

    {{ IDEv() }}  

???- note "Remarque"

    Voici un code (les éléments seront vus plus tard). Comme les listes sont mutables, *certaines méthodes* pour modifiant la liste passée en argument d'une fonction **modifient l'original** !

    ```python
    def modif_liste(L):
        L.append(100)
        print("Dans la fonction la variable L vaut", L)

    liste1 = [1,2,3,4]
    print(liste1) # Affiche [1,2,3,4]
    modif_liste(L)
    print(liste1) # Affiche [1,2,3,4,100]
    ```

    {{ IDEv() }}  


!!! danger "A connaitre"

    Toutes les structures vues jusqu'à présent (`int`, `float`, `bool` et `str`) sont des non mutables !

!!! tip "Méthode"

    Un méthode pour modifier un non mutable à l'aide d'une fonction ets de tout simplement ... le renvoyer !

    ```python
    def modif_mot(mot):
        mot = mot + ' ajout'
        print("Dans la fonction la variable mot vaut " + mot)
        return mot
    
    un_mot = "Hello"
    un_mot = modif_mot(un_mot)
    print(un_mot)
    ```

    {{ IDEv() }}  

???- note "Remarque"

    Il existe une autre méthode. Mais il faut l'éviter autant que faire ce peut. Il faut déclarer la variable en `global` (et ne plus la passer en paramètre).

    ```python
    def modif_mot():
        global un_mot
        un_mot = un_mot + ' ajout'
        print("Dans la fonction la variable mot vaut " + mot)
    
    un_mot = "Hello"
    modif_mot(un_mot)
    print(un_mot)
    ```

    {{ IDEv() }}  


## Exercice à maitriser

???- question "Exercice"

    Demander un prénom et un age et dire bonjour à l'utilisateur en lui donnant son age.

    Pour une personne de 20 ans qui s'appelle Luke, l'affichage attendu est ```Bonjour Luke. Vous avez 20 ans.```

    ???- done "Réponse"

        ```python
        nom = input("Votre nom ? ")
        age = int(input("Votre age ? "))
        reponse = "Bonjour " + nom + ". Vous avez " + str(age) + " ans."
        print(reponse)
        ```

???- question "Exercice"

    A l'aide des tranches, compléter le programme suivant pour obtenir une chaîne où l'alphabet aura été remis dans le bonne ordre.

    ```python
    melange = "QRSTABCDELMNUVFGHIJKWXYZOP"
    alphabet = ... # compléter avec des tranches
    print(alphabet) # affiche ABCEFGHIJKLMNOPQRSTUVWXYZ
    ```

<!--
    ???- done "Réponse"

        ```python
        melange = "QRSTABCDELMNUVFGHIJKWXYZOP"
        alphabet = melange[4:9] + melange[14:20] + melange[9:12] + melange[-2:] + melange[:4] + melange[12:14] + melange[20:24]
        print(alphabet) # affiche ABCEFGHIJKLMNOPQRSTUVWXYZ
        ```
-->

???- question "Exercice"

    ```mots="La revolution informatique"```. En utilisant les méthodes précédentes :

    1. Donner le code qui affiche :
        
        1. le nombre de caractère de ```mots```;
        2. True si le mot ```"la"``` est dans ```mots```, ```False``` sinon.
        3. la position de la première lettre ```r``` ; Et (plus difficile) la seconde ;

    2. Donner le code :
        
        1. qui affiche les deux premiers caractères de ```mots```
        2. qui extrait le mot "revolution" de ```mots```
        3. qui teste le résultat précédent : c'est-à-dire qui renvoie ```'True'``` si le code a bien trouvé le mot ```revolution``` (```False``` sinon)
        4. en utilisant des tranches de la chaîne de caractères \verb```mots```, affecter à la variable ```modif``` la chaîne de caractère ```"informatique revolution La"```.

<!--
    ???- done "Réponse"

        ```python
        # Quesiton 1.a.
        print(len(mots))
        # Quesiton 1.b.
        print('la' in mots)
        # Question 1.c.
        print(mots.find('r'))
        premier = mots.find('r')
        print(m[premier + 1:].find('r'))
        # Question 2.a.
        print(mots[0:2]) 
        #ou
        print(mots[:2])
        # Question 2.b.
        print(mots[3:13])
        # Question 2.c.
        essai = mots[3:13]
        motCherche = "revolution"
        print(essai == motCherche)
        # Question 2.d.
        modif = mots[14:] + mots[2:14] + mots[:2]
        print(modif)
        ```
-->

???- question "Exercice"

    Pour un spectacle, le tarif normal est de 25 &#8364; et le tarif réduit est de 18 &#8364;. Écrire un programme qui demande à l'utilisateur le nombre de place total, puis le nombre de place à tarif réduit. Afficher alors le prix à payer.

    Par exemple, pour 10 places dont 3 au tarif réduit, il faut afficher :
    
    ```Le coût total est de 229 euros.```

<!--
    ???- done "Réponse"

        ```python
        nbPlace=int(input("Nombre de place ? "))
        nbReduit=int(input("Nombre de tarif réduit ? "))
        cout=nbReduit*18+(nbPlace-nbReduit)*25
        print("Le coût total est de", cout, "euros")
        print("Le coût total est de "+str(cout)+" euros")
        ```
-->

???- question "Exercice"

    Pour cette exercice, **revoir le cours sur ```if``` et ```elif```**.

    Écrire un programme qui compte le nombre de voyelles dans la phrase : 
    
    &laquo; Cela n'a aucun sens d'embaucher des gens intelligents et de leur dire quoi faire; Nous embauchons des gens intelligents pour qu'ils puissent nous dire quoi faire.&raquo; [^1]

    ```python
    phrase = "Cela n'a aucun sens d'embaucher des gens intelligents et de leur dire quoi faire; Nous embauchons des gens intelligents pour qu'ils puissent nous dire quoi faire."
    # A COMPLETER
    ```

<!--
    ???- done "Réponse"

        ```python
        phrase = "Cela n'a aucun sens d'embaucher des gens intelligents et de leur dire quoi faire; Nous embauchons des gens intelligents pour qu'ils puissent nous dire quoi faire."
        compt = 0
        for elt in phrase:
            if elt == 'a':
                compt = compt + 1
            if elt == 'e':
                compt = compt + 1
            if elt == 'i':
                compt = compt + 1
            if elt == 'o':
                compt = compt + 1
            if elt == 'u':
                compt = compt + 1
        print(compt)
        ```
-->

[^1]: Steve Jobs
    

