# Les fonctions

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

???- example "Exemple de définition d'une fonction"

    Voici une fonction

    ```python
    def moyenne(nb1, nb2, nb3):
        num = nb1 + nb2 + nb3
        return num/3
    ```


???- example "Exemple d'utilisation d'une fonction"

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
