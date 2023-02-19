# La boucle while

!!! info "A retenir"

	Lorsqu'il faut répéter des instructions sans connaître à l'avance le nombre d'itération, il faut utiliser la boucle ```while```.

	```python
	choix="y"
	while choix=="y":
		print("Si vous voulez continuer, taper 'y'")
		choix=input()
	print("Au revoir")
	```

???- danger "ATTENTION"

	Le principal danger d'une boucle ```while``` est la boucle infinie. Il faut donc impérativement vérifier qu'au minimum les instructions dans la boucle permettent de faire évoluer la condition !

	Par exemple:

	```python
	a = 5 
	while a < 10: # la condition porte sur a
		b = a + b
	```

	Ici, la condition porte sur ```a``` et les instructions dans la boucle ````while``` ne font jamais évoluer cette condition ! Il y a donc une boucle infinie.

	Malheureusement, cette vérification indispensable n'est pas une condition suffisante pour éviter une boucle infinie ! L'utilisation de [variants de boucle](AFAIRE) permet de s'assurer de la terminaison d'une boucle ```while``` !

???- tip "for vs While"

	Même si, en théorie, il est possible de remplacer les boucles ```for``` par des boucles ```while```, il ne faut pas le faire !

	En effet, le risque d'une boucle infinie n'existe pas avec la boucle ```for``` !

	Par contre, lorsqu'il faut parcourir une liste ou une chaine ou un dictionnaire **et** vérifier une condtion, une boucle ```while``` est plus adaptée !

	<div class = "Cote_tiers"><div class = "Center_txt">A éviter</div>

    ``` python
    L=[5,3,4,-1,4,6]
    rep = len(L)
    trouve = False
	for idx in range(len(L)):
		if not(trouve) and L[idx] < 0 :
			trouve = True
            rep = idx
	print(rep)
    ```

    </div>
	<div class = "Cote_tiers"><div class = "Center_txt">Mieux !</div>

    ``` python
    L=[5,3,4,-1,4,6]
	for idx in range(len(L)):
		if L[idx] < 0 :
			break
	print(idx)
    ```

    </div>
    <div class = "Cote_tiers"><div class = "Center_txt">A préférer</div>

    ``` python
    idx = 0
    L=[5,3,4,-1,4,6]
    while idx < len(L) and L[idx] >=0 :
        idx = idx + 1
    print(idx)
    ```
    </div>