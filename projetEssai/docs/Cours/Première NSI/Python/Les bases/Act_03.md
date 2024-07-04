# Python<br>Découverte de la bibliothèque ```turtle``` ( suite et fin)

???- tip "Rappel des mots clés de `Turtle`"
    - ```turtle.forward(x)``` avance la tortue de $x$.
    - ```turtle.left(x)``` tourne la tortue de $x^{\circ}$ par rapport à sa direction actuelle vers la gauche.
    - ```turtle.right(x)``` tourne la tortue de $x^{\circ}$ par rapport à sa direction actuelle vers la droite.
    - ```turtle.backward(x)``` avance la tortue de $x$.
    - ```turtle.goto(x,y)``` teleporte la tortue à la position $(x;y)$ **en dessinant le déplacement**
    - ```turtle.up()``` lève le crayon : les instructions qui suivront ne laisseront aucune trace.
    - ```turtle.down()``` abaisse le crayon : les instructions qui suivront laisseront une trace.
    - ```turtle.speed(x)``` modifie la vitesse de la tortue : de 1 (lente) à 10 (rapide) (rque : 0 est la vitesse maximale !!!)
    - ```turtle.circle(x)``` trace un cercle de rayon $x$ **en partant d'un point _sur_ le cercle**.
    - ```turtle.color("red")``` change la couleur du tracer en rouge. Il y a aussi blue, purple, olive, magenta, orange, brown, cyan, yellow, green, pink, black, red, gray, white, ... (liste non exhaustive)
    - ```turtle.setheading(x)``` oriente la tortue dans la direction $x$ :  
        - 0 la tortue pointe vers l'est
        - 90 la tortue pointe vers le nord
        - 180 la tortue pointe vers le sud
        - 270 la tortue pointe vers l'ouest
    - ```turtle.begin_fill()``` et ```turtle.end_fill()``` permet remplir la forme dessinée **après** ```turtle.begin_fill()``` et avant ```turtle.end_fill()```  
    - ```turtle.width(x)``` modifie la largeur de la trace, $x >0$.

## Et avec des coordonnées ?

Il est possible de faire des dessins en reliant des points définis par des coordonnées, avec la fonction `goto(...)`

!!! question "Exercice - 1"

    1. **RAPPEL :** Ecrire une fonction qui teleporte la tortue à un point dont les coordonnées sont des paramètres de cette fonction.  
    Signature `fonction teleporte(x : int, y : int) : None`
    2. Ecrire deux fonctions `trace_axe_abs(deb : int, fin : int) : None` et `trace_axe_ord(deb : int, fin : int) : None` qui trace les axes des abscisses et des ordonnées entre `deb` et `fin`. Il faut à la fin des fonctions, ramener la tortue à l'origine du repère.
    3. Ecrire une fonction qui renvoie à un réel $x$ le tuple ($x$, $\dfrac{x^2}{200}$).  
    signature `fonction une_fct(x : float) : float`  
    Exemple, `une_fct(10)` renvoie `(10, 0.5)`
    4. Ecrire une fonction qui dessine la courbe de la fonction précédente en reliant les points dont les abscisses sont les entiers compris entre `deb` et `fin` (`fin` inclus !), passés en argument.  
    Signature `fonction courbe_fct(deb : int, fin : int)`  
    Ainsi, `courbe_fct(-200, 200)` donne :  
    [![Tracer courbe 1](../Image/courbe_01.png){.Center_lien }](../Image/courbe_01.png)  
    5. Tracer les deux axes et la courbe.

!!! danger "A connaitre"

    - Savoir manipuler le `range(a, b)` en faisant attention au **strictement inférieur à b**
    - `return` et tuple

!!! question "Exercice - 2"

    1. Voici une fonction :  
    ```python
    import math as ma

    def fct_mystere(xa,ya,xb,yb):
        return ma.sqrt((xa-xb)**2 + (ya-yb)**2)
    ```  
    Expliquez ce que renvoie cette fonction. Renommez-la en conséquence.
    2. On souhaite déterminer une approximation de la longueur de la courbe. Pour cela, il suffit de calculer d'ajouter toutes les distances entre 2 points consécutifs dessinés par la tortue.  
    Voici un code possible à compléter :  
    ```python
    def long_courbe_fct(deb, fin):
        long = 0
        for i ...
            long = ...
        return ...
    ```
    3. Utiliser ce code pour déterminer la longueur de la courbe tracée précédemment
    4. Modifier la fonction qu'il faut pour tracer la courbe (et déterminer leur longueur) de :
        1. $f(x) = \dfrac{(x-100) \times x \times(x + 150)}{4000}$ sur $[-200; 200]$
        2. $f(x) = \dfrac{5000}{x + 205} + 2*x - 150$ sur $[-200;200]$

!!! danger "A connaitre"

    - Savoir expliquer ce que fait un code simple
    - Savoir compléter un code
    - Savoir utiliser un code classique vu en cours