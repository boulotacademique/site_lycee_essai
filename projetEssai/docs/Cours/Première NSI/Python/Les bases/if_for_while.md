# if, elif et les boucles

## if, elif

!!! info "A retenir"

    La boucle ```if``` exécute certaines instructions si une condition (c'est un propriété qui est soit vraie soit fausse) est réalisée et d'autres sinon.
   
    ```python
    if age >= 18:
        print("Je suis majeur(e)")
    else:
        print("Je suis mineur(e)")
    ```

!!! warning "Attention"

    Toutes les lignes des instructions à exécuter dans un ```if``` ou un ```else``` doivent avoir un tabulation de plus que la ligne avec ```if``` ou ```else```.

    ```py
    a = int(input("Donner votre note entre 0 et 20 : "))
    if a < 10:
        print("Il faut revoir les bases") # uniquement pour une note < 10
        print("Vous ferez mieux la prochaine fois") # uniquement pour une note < 10
    else:
        print("Bon ensemble") # uniquement pour une note >= 10
    print("Revoyez les notions où vous vous êtes trompés.")  # pour toutes les notes
    ```