# Python<br>Les matrices

!!! question "Exercice - (EP 24-10-02)"

    [![A compléter](../Image/03_coeur.png){.Center_lien }](../Image/03_coeur.png)

    On travaille sur des dessins en noir et blanc obtenus à partir de pixels noirs et blancs. La figure « cœur » ci-dessus va servir d’exemple.  
    On la représente par une grille de nombres, c’est-à-dire par une liste composée de sous-listes de même longueurs.  
    Chaque sous-liste représentera donc une ligne du dessin.  
    Dans le code ci-dessous, la fonction `affiche` permet d’afficher le dessin. Les pixels noirs (1 dans la grille) seront représentés par le caractère "*" et les blancs (0 dans la grille) par deux espaces.  
    La fonction `liste_zoom` prend en arguments une liste `liste_depart` et un entier `k`. Elle renvoie une liste où chaque élément de `liste_depart` est dupliqué `k` fois.  
    La fonction `dessin_zoom` prend en argument la grille `dessin` et renvoie une grille où toutes les lignes de `dessin` sont zoomées `k` fois et répétées `k` fois.  
    Compléter les fonctions `liste_zoom` et `dessin_zoom` du code suivant :

    ```python linenums='1'
    def affiche(dessin):
        ''' affichage d'une grille : les 1 sont représentés par 
            des "*" , les 0 par un espace " " '''
        for ligne in dessin:
            affichage = ''
            for col in ligne:
                if col == 1:
                    affichage = affichage + "*"
                else:
                    affichage = affichage + " "
            print(affichage)


    def liste_zoom(liste_depart,k):
        '''renvoie une liste contenant k fois chaque élément de
        liste_depart'''
        liste_zoomee = ... 
        for elt in ... : 
            for i in range(k):
                ...
        return liste_zoomee

    def dessin_zoom(grille,k):
        '''renvoie une grille où les lignes sont zoomées k fois 
        ET répétées k fois'''
        grille_zoomee=[]
        for ligne in grille:
            ligne_zoomee = ... 
            for i in range(k):
                ... .append(...) 
        return grille_zoomee
    ```

!!! question "Exercice - (EP 24-29-02)"
    On cherche à déterminer les valeurs du triangle de Pascal (Figure 1).  
    Dans le triangle de Pascal, chaque ligne commence et se termine par le nombre 1. Comme l’illustre la Figure 2, on additionne deux valeurs successives d’une ligne pour obtenir la valeur qui se situe sous la deuxième valeur.

    [![A compléter](../Image/17_triangle.png){.Center_lien }](./Image/17_triangle.png)

    Compléter les fonctions `ligne_suivante` et `pascal` ci-dessous. La fonction `ligne_suivante` prend en paramètre une liste d’entiers `ligne` correspondant à une ligne du triangle de Pascal et renvoie la liste correspondant à la ligne suivante du triangle de Pascal. La fonction `pascal` prend en paramètre un entier n et l’utilise pour construire le triangle de Pascal ayant `n+1` lignes sous la forme d’une liste de listes.

    ```python linenums='1'
    def ligne_suivante(ligne):
        '''Renvoie la ligne suivant ligne du triangle de Pascal'''
        ligne_suiv = [...] 
        for i in range(...): 
            ligne_suiv.append(...) 
        ligne_suiv.append(...) 
        return ligne_suiv

    def pascal(n):
        '''Renvoie le triangle de Pascal de hauteur n'''
        triangle = [ [1] ]
        for k in range(...): 
            ligne_k = ... 
            triangle.append(ligne_k)
        return triangle
    ```

    Exemples:

    ```python
    >>> ligne_suivante([1, 3, 3, 1])
    [1, 4, 6, 4, 1]
    >>> pascal(2)
    [[1], [1, 1], [1, 2, 1]]
    >>> pascal(3)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    ``` 

!!! question "Exercice - (EP 24-43-02)"
    On souhaite générer des grilles du jeu de démineur à partir de la position des bombes à placer.  
    On se limite à la génération de grilles carrées de taille $n \times n$ où $n$ est le nombre de bombes du jeu.  
    Dans le jeu du démineur, chaque case de la grille contient soit une bombe, soit une valeur qui correspond aux nombres de bombes situées dans le voisinage direct de la case (au-dessus, en dessous, à droite, à gauche ou en diagonale : chaque case a donc 8 voisins si elle n'est pas située au bord de la grille).  
    Voici un exemple de grille $5 \times 5$ de démineur dans laquelle la bombe est représentée par une étoile :

    [![A compléter](../Image/04grille.png){.Center_lien }](../Image/04grille.png)

    On utilise une liste de listes pour représenter la grille et on choisit de coder une bombe par la valeur -1.  
    L'exemple ci-contre sera donc codé par la liste :

    ```python
    [[1, 1, 1, 0, 0],
    [1, -1, 1, 1, 1],
    [2, 2, 3, 2, -1],
    [1, -1, 2, -1, 3],
    [1, 1, 2, 2, -1]]
    ```

    Compléter le code suivant afin de générer des grilles de démineur, on pourra vérifier que l'appel `genere_grille([(1, 1), (2, 4), (3, 1), (3, 3), (4, 4)])` renvoie bien la liste donnée en exemple.

    ```python
    def voisinage(n, ligne, colonne):
        """ Renvoie la liste des coordonnées des voisins de la case
        (ligne, colonne) en gérant les cases sur les bords. """
        voisins = []
        for l in range(max(0,ligne-1), min(n, ligne+2)):
            for c in range(max(0, colonne-1), min(n, colonne+2)):
                if (l, c) != (ligne, colonne):
                    voisins.append((l,c))
        return voisins


    def incremente_voisins(grille, ligne, colonne):
        """ Incrémente de 1 toutes les cases voisines d'une bombe."""
        voisins = ...
        for l, c in voisins:
            if grille[l][c] != ...: # si ce n'est pas une bombe
                ...  # on ajoute 1 à sa valeur

    def genere_grille(bombes):
        """ Renvoie une grille de démineur de taille nxn où n est
        le nombre de bombes, en plaçant les bombes à l'aide de
        la liste bombes de coordonnées (tuples) passée en
        paramètre. """
        n = len(bombes)
        # Initialisation d'une grille nxn remplie de 0
        grille = [[0 for colonne in range(n)] for ligne in range(n)]
        # Place les bombes et calcule les valeurs des autres cases
        for ligne, colonne in bombes:
            grille[ligne][colonne] = ... # place la bombe
            ... # incrémente ses voisins

        return grille
    ``` 