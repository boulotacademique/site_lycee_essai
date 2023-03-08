# Les variables et les opérations

## Les variables

!!! info "Un premièr point de vue"
    Vous avez vu en seconde qu'une variable pouvait être vu comme une boîte avec une étiquette et un contenu.

    [![affecter une variable](../Image/affect-var5.png){.Center_lien .Vignette}](../Image/affect-var5.png)

    [![affecter une variable](../Image/var5.png){.Center_lien .Vignette}](../Image/var5.png)

    Cette image n'est valable que pour des contenus &laquo; simples &raquo; : les nombres, les chaînes de caractères.

- Il faut donner des noms compréhensibles aux variables (et aux fonctions).
- Pour la typographie des noms des variables, utiliser de préférence **le snake\_case**. Tous les caractères sont des minuscules et les mots sont séparés par des underscore (ou tiret du 8).

!!! info "Utilisation"
    - Pour affecter une valeur à une variable, on utilise ```=```. Par exemple, ```x = 2``` ou ```firstname = "Anakin"```.
    - Pour afficher le contenu d'une variable, on utilise ```print()``` (mais pas de ""). Par exemple, ```print(x)```.
    - Pour afficher du texte et le contenu d'une variable,on peut utiliser la virgule ```print("Je m'appelle",firstname)``` ou utiliser la concaténation de chaînes de caractères ```print("Je m'appelle " + str(firstname)) ```

{{ IDEv('Python_base_code/variables_01', MAX = 1000) }}

???- warning "Déclarer avant d'utiliser"
    Avant d'utiliser une variable, elle doit être déclarée (i.e. une valeur a été affetée à une variable) ou être un paramètre d'une fonction.

    Par exemple:

    <div class = "Cote_demi">

    <div class = "Center_txt"> Un exemple correct </div>

    ```python
    a = 25 # une affectation
    b = a + 3 # La variable a est utilisée
    ```

    </div>

    <div class = "Cote_demi">

    <div class = "Center_txt"> Un exemple incorrect </div>

    ```python
    c = d + 3 # La variable d est utilisée mais n'a pas été déclarée !
    ```

    Cela déclanche une erreur ```NameError: name 'd' is not defined```
    </div>

    {{ IDEv('Python_base_code/variables_02', MAX = 1000) }}

!!! info "Type d'une variable"
    Une valeur enregistrée dans une variable possède un type, c'est aussi le type de cette variable.

    Les principaux types &laquo; simples &raquo; :
    
    - les entiers : ```int```
    - les réels : ```float```
    - les caractères ou les chaînes de caractères : ```str```
    - les booléens : ```bool```

    Il y a aussi des structures dites construites :

    - les &laquo; listes &raquo; : ```list```
    - les dictionnaires : ```dict```
    - les tuples : ```tuple```


## Les opérations

### Les opérations mathématiques

En python, il est possible d'effectuer les opérations mathématiques usuelles avec les types ```int``` ou ```float``` (même si certains résultats peuvent surprendre !) :

- l'addition ```+```
- la multiplication ```*```
- la division ```/```

Il y a aussi **le quotient d'une division euclidienne** de $a$ par $b$, avec l'opérateur ```//``` (on écrit ```a // b```). Par exemple, comme $13 = 3 \times 4 + 1$, ```13 // 3``` vaut 4 !

Il y a aussi **le reste d'une division euclidienne** de $a$ par $b$, avec l'opérateur ```%``` (on écrit alors ```a % b``` et on lit &laquo; a modulo b &raquo;). Par exemple, comme $13 = 3 \times 4 + 1$, ```13 % 3``` vaut 1 !

En ce qui concerne **la puissance**, il faut utiliser ```**```. Par exemple, pour $5^3$ on écrit ```5**3```.

!!! info "Une propriété importante"

    Afin de savoir si un entier $a$ est dans la table de multiplication d'un autre entier $b$ (i.e. si **$a$ un multiple de $b$**), il suffit de vérifier que le reste de la division euclidienne de $a$ par $b$ vaut 0 !

    Par exemple, comme ```328 % 4``` vaut 0 (en effet : $328 = 4 \times 82 + 0$), 328 est un multiple de 4 !

    Par exemple, comme ```254 % 4``` ne vaut pas 0 (cela vaut 2 car $254 = 4 \times 63 + 2$), 254 n'est pas un multiple de 4.

    ???- tip "Nombre pair, nombre impair"

        En particulier,
        
        - $a$ est **un nombre pair**, c'est-à-dire un multiple de $2$, si et seulement si ```a % 2``` vaut 0 ;
        - $a$ est **un nombre impair**, c'est-à-dire $a$ n'est pas un multiple de $2$, si et seulement si ```a % 2``` vaut 1 ;

{{ IDEv('Python_base_code/variables_03', MAX = 1000) }}

!!! info "Les comparaisons"

    Il est possible de comparer des entiers. Le résultats de tels comparaisons sont des tests qui renvoient ```True``` ou ```False``` !

    - test d'égalité : ```a == b``` (A ne pas faire avec [des flottants](AFAIRE))
    - test de la non égalité : ```a != b``` (A ne pas faire avec [des flottants](AFAIRE))
    - test d'inégailté strict : ```a > b``` ou ```a < b```
    - test d'inégailté large : ```a >= b``` ou ```a <= b```
    - test de type : ```isinstance(a , int)```, ```isinstance(a , float)```

### Opérations sur d'autres types

#### Sur les chaines

Il existe des opérations sur les chaines de caractères (les ```str```) : la [concaténation](./str.md#concat) et la [répétition](./str.md#repet_str) !

Il existe aussi des comparaisons !

!!! info "L'ordre lexicographique"

    <span class="Gras" id="ordre_lexico">L'ordre lexicographique</span> est l'ordre du dictionnaire, mais avec un alphabet comportant tous les caractères possibles classés dans l'ordre de la table de codage des caractères (celle d'[iso](https://fr.wikipedia.org/wiki/ISO/CEI_8859-1#ISO/CEI_8859-15) ).

    On a donc 

    ```" " < "0" < "1" < "2" < ... < "9" < "A" < "B" < ... < "Z" < "a" < "b" < ... < "z"```

    Puis on applique la méthode de classement d'un dictionnaire !

    Par exemple, ```"BAC" < "aab" < "aba" < "b" ``` 

    Par exemple, ```"100" < "9" ``` !!

{{ IDEv('Python_base_code/variables_04', MAX = 1000) }}

#### Sur les listes

Il existe des opérations sur les listes (les ```list```) : la [concaténation](./list.md#concat_list) et la [répétition](./list.md#repet_list) !