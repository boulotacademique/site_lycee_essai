# Python<br>La boucle for

!!! info "A retenir"

    La boucle ```for``` permet d'exécuter un nombre connu de fois des instructions. Si il faut répéter 10 fois, on écrit :

    ```python
    for co in range(10):
        res = co * 2
        print(" 2 x " + str(co) + " = " + str(res)) 
    ```

    affiche

    <div class = "Center_ss_bd" style="width:10%;">

	```python
	2 x 0 = 0 
    2 x 1 = 2 
    2 x 2 = 4 
    2 x 3 = 6 
    2 x 4 = 8 
    2 x 5 = 10
    2 x 6 = 12
    2 x 7 = 14
    2 x 8 = 16
    2 x 9 = 18
	```

	</div>
    
    Il y a d'autres façons [d'utiliser ```range```](./ortho.md#range) !

{{ IDEv('Python_base_code/for_01', MAX = 1000) }}

???+ example "Un classique important"

    Pour calculer $0+1+2+3+\ldots+9$ , il faut accumuler/ajouter dans une variable initialisée à 0 (valeur qui ne modifie pas le résultat d'une addition) les valeurs utiles. 
    
    Par exemple, pour calculer $0+1+2+3+4+5+6+7+8+9$, on peut écrire :

    ```python
    som = 0
    for co in range(10):
        som = som + co
    print(som)
    ```

    1. Modifier le programme précédent pour calculer $0+1+2+3+\ldots 50$.
    2. Modifier le programme précédent pour calculer $1\times 2\times 3 \times \ldots \times 9$

    Pour aller plus loin avec d'autres questions du même type : cf [ici](AFAIRE)


{{ IDEv('Python_base_code/for_02', MAX = 1000) }}


!!! info "Un nombre connu de répétition"
    Une boucle ```for``` peut donc s'utiliser lorsque le nombre de répétition des instructions est connu (explicitement comme dans l'exemple précédent ou avec une variable cf ci-dessous)


{{ IDEv('Python_base_code/for_03', MAX = 1000) }}



???- danger "Réflechissez !"

    Lorsque vous voulez utiliser une boucle ```for```, vous devez vous poser la question suivante : &laquo; est-ce que mon compteur de boucle est utilisé dans les instructions à répéter ? &raquo;

    Comparez les deux programmes suivants

    <div class = "Cote_gauche"><div class="Center_txt">Le compteur de boucle n'intervient pas dans les instructions</div>

    ```python
    print("Attention : ")
    for co in range(10):
        print("Alerte intrusion !")
    ```

    </div>
    <div class = "Cote_droit"><div class="Center_txt">Le compteur de boucle intervient dans les instructions</div>

    ```python
    print("Attention : ")
    for co in range(10):
        print("Explosion dans " + str(10 - co))
    print("Boum !!!")
    ```

    </div>

    Dans le premier programme, peu importe les valeurs prises par le compteur ```co``` ! Il est donc possible d'écrire :

    ```python
    print("Attention : ")
    for co in range(20, 30):
        print("Alerte intrusion !")
    ```

    Alors que dans le second, une telle modification est beaucoup plus difficile à effectuer (et totalement inappropriée) !

???- question "Exercice"

    Ecrire un programme qui demande à l'utilisateur un nombre de lignes et qui écrit X sur le nombre de lignes recquis.

    Par exemple, sur 5 lignes : on a :

    <div class = "Center_txt" style="width:2em;margin-left:auto;margin-right:auto;">

    ```python
    X
    X
    X
    X
    X
    ```
    </div>

<!--    ???- done "Réponse"

        ```python
        nb_ligne = int(input("Nombre de lignes ? "))
        for co in range(nb_ligne):
            print("X")
        ```
-->

???- question "Exercice"

    Ecrire un programme qui demande à l'utilisateur un nombre de lignes et qui dessine un triangle plein de X sur le nombre de lignes recquis.  
    On utilisera le fait que, pour obtenir `XXX`, on peut taper `"X"*3` ou `"X"*i` avec `i` qui vaut 3.

    Par exemple, sur 5 lignes : on a :

    <div  style="width:5em;margin-left:auto;margin-right:auto;">


    ```python
    X  
    XX  
    XXX  
    XXXX  
    XXXXX
    ```

    </div>

<!--    ???- done "Réponse"

        ```python
        nb_ligne = int(input("Nombre de lignes ? "))
        for co in range(nb_ligne):
            print("X"*(co+1))
        ```
-->

???- question "Exercice"

    Ecrire un programme qui demande à l'utilisateur un nombre de lignes et qui dessine un triangle inversé plein de X sur le nombre de lignes recquis.  
    On utilisera le fait que, pour obtenir `XXX`, on peut taper `"X"*3` ou `"X"*i` avec `i` qui vaut 3.

    Par exemple, sur 5 lignes : on a :

    <div style="width:5em;margin-left:auto;margin-right:auto;">

    ```python
    XXXXX
    XXXX
    XXX
    XX
    X
    ```
    </div>

<!--    ???- done "Réponse"

        ```python
        nb_ligne = int(input("Nombre de lignes ? "))
        for co in range(nb_ligne):
            print("X"*(nb_ligne - co))
        ```
-->

???- question "Exercice plus difficile"

    Ecrire un programme qui demande à l'utilisateur un nombre de lignes et qui dessine un sapin plein de A sur le nombre de lignes recquis.

    Par exemple, sur 5 lignes : on a :

    <div class = "Center_txt" style="width:9em;margin-left:auto;margin-right:auto;">

    ```python
     A
     AAA
     AAAAA
     AAAAAAA
    AAAAAAAAA
    ```

    </div>

<!--    ???- done "Réponse"

        ```python
        nb_ligne = int(input("Nombre de lignes ? "))
        for co in range(nb_ligne):
            print(" "*(nb_ligne - (co+1)) + "^"*(2*co+1) + " "*(nb_ligne - (co+1)))
        ```
-->
