# Python<br>Découverte de la bibliothèque ```turtle```

!!! bug "Objectif"

    - Découvrir l'environnement CAPYTALE
    - Découvrir la bibliothèque `turtle`
    - Manipulation de variables
    - Utilisation de la boucle `for`
    - Méthodologie : Que faut-il apprendre ?

Pour faire des dessins simples, il est possible d'utiliser la bibliothèque ```turtle```. Dans une zone de dessin, il y a un pointeur (appelé &laquo; tortue &raquo;) qui pointe dans une direction. Lorsque cette tortue se déplace, elle laisse un trait. Il est donc possible de faire un dessin en déplaçant cette tortue !

Voici un code de base :

!!! tip "Méthode - dans un éditeur (pyzo, spyder, VSC, ...)"

    ```python
    import turtle

    turtle.forward(200)
    turtle.left(90)
    turtle.left(200)

    turtle.exitonclick()
    ```  
    Il faut terminer par ```turtle.exitonclick()```

!!! tip "Méthode - dans CAPYTALE"

    ```python
    import turtle

    turtle.forward(200)
    turtle.left(90)
    turtle.left(200)

    turtle.done()
    ```  
    Il faut terminer par ```turtle.done()```

!!! warning "Attention"
    La bibliothèque `turtle` ne doit être importé **qu'une seule fois**. Ainsi, `import turtle` ne doit être écrite qu'une seule fois dans un fichier (pour l'éditeur pyzo, spyder, VSC, ...) et qu'une seule fois dans une page CAPYTALE.


!!! note "Les premières méthodes"

    - ```turtle.forward(x)``` avance la tortue de $x$.
    - ```turtle.left(x)``` tourne la tortue de $x^{\small\circ}$ par rapport à sa direction actuelle vers la gauche.
    - ```turtle.right(x)``` tourne la tortue de $x^{\small\circ}$ par rapport à sa direction actuelle vers la droite.
    - ```turtle.backward(x)``` avance la tortue de $x$.

!!! question "Exercice - 1"

    1. Ecrire les instructions qui permettront de tracer un carré de coté 200.
    2. Faire la même chose en utilisant la boucle ```for```
    3. Ecrire les instructions qui permettront de tracer un triangle équilatéral de coté 200.
    4. Ecrire les instructions qui permettront de tracer un hexagone régulier de coté 200.
    5. Une méthode semble apparaitre. Recopier et compléter le code suivant afin de tracer un polygone régulier :  
    ```python
    nb_cote = 4
    angle = 360/nb_cote
    longeur_cote = 150
    for ...
        ...
        ...
    ```
    6. Modifier certaines valeurs afin de tracer un cercle.

!!! danger "A connaitre"
    - Savoir utiliser des variables
    - Savoir utiliser une boucle `for`
    - Savoir manipuler les `range(...)`

!!! note "D'autres méthodes"

    - ```turtle.goto(x,y)``` teleporte la tortue à la position $(x;y)$ **en dessinant le déplacement**
    - ```turtle.up()``` lève le crayon : les instructions qui suivront ne laisseront aucune trace.
    - ```turtle.down()``` abaisse le crayon : les instructions qui suivront laisseront une trace.
    - ```turtle.speed(x)``` modifie la vitesse de la tortue : de 1 (lente) à 10 (rapide) (rque : 0 est la vitesse maximale !!!)

!!! question "Exercice - 2"

    1. On souhaite tracer côte à côte un carré, un triangle équilatéral et un hexagone de côté 200. Compléter le code suivant :  
    ```python
    turtle.goto(-300,0)
    # Code pour dessiner un carré
    ...
    ...
    # on se décale pour le dessin suivant
    turtle.forward(250)
    # Code pour dessiner un triangle équilatéral
    ...
    ...
    # on se décale pour le dessin suivant
    turtle.forward(250)
    # Code pour dessiner un hexagone
    ...
    ...
    ```
    2. Modifier ce code pour eviter d'avoir les traces inutiles liées au déplacement de la tortue.

Pour dessiner une spirale, il suffit de tracer un polygone en modifiant la longueur de chaque côté après chaque &laquo; tournant &raquo;.

```python
nb_etape = 20
angle = 90
pas = 2
for i in range(nb_etape):
    turtle.forward(pas + i * pas)
    turtle.left(angle)
```

!!! question "Exercice - 3"
    En vous inspirant de l'exemple précédent :

    1. tracer une spirale basée sur un triangle équilatéral ;
    2. tracer une spirale basée sur un hexagone

    Rque : que se passe-t-il si l'angle est légèrement modifié ?

!!! danger "A connaitre"
    - Savoir modifier/adapter un code
    - Savoir utiliser le compteur d'une boucle (c'est le `i` de `for i in range(...)`)

