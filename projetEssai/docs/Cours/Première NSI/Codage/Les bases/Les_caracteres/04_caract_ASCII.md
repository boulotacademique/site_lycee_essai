# Codage des caractères : ASCII


## Introduction


L’utilisation d’un ordinateur passe la plupart du temps par le texte. Que ce soit pour lire ou écrire une instruction, utiliser un traitement de texte, naviguer sur internet nous manipulons des mots, des symboles. Mais comment sont-ils représentés et traités en interne ?

En informatique, les caractères (chiffres, alphabets …) sont représentés par des nombres.
Le codage des caractères est une convention de codage.
Il existe de nombreux codages des caractères. Les principaux codages sont :
<ul>
<li> Le code ASCII (ISO 646)</li>
<li> Les codes ISO 8859-1 / ISO 8859-15</li>
<li> L’Unicode avec les codes UTF-8 / UTF-16 / UTF-32</li>
</ul>


## L'ASCII
Le code ASCII (American Standard Code for Information Interchange) créé en 1961 (par Bob Bemer) est un code sur 7+1 bits. Le premier bit (le bit de poids fort) reste à 0. À une époque, on utilisait ce bit comme bit de parité (détection d’erreur).

Le code ASCII code les lettres, les chiffres et d'autres symboles sous forme de nombre entiers binaires de 7 bits.

Les caractères de 0 à 31 ainsi que le 127 ne sont pas affichables et correspondent à des directives (ex.: 13 $\rightarrow$ CR $\rightarrow$ &laquo; retourne à la ligne &raquo;, 27 $\rightarrow$ ESC $\rightarrow$ &laquo; échappe &raquo;, 127 $\rightarrow$ DEL $\rightarrow$ &laquo; efface &raquo;). Le caractère 32 est l’espace blanc. Les autres correspondent aux chiffres, aux lettres majuscules et minuscules et à des symboles de ponctuation.

ASCII est un nom américain, Le nom officiel de cette norme est l’ISO 646.

[![Tableau ASCII](../../Image/TabASCII.jpg){.Center_lien .VignetteMed}](../../Image/TabASCII.jpg)


!!! tip "Méthode : utiliser un tableau"
    Il faut savoir lire le tableau précédent pour coder les caractères en hexadécimal.

???- example "Exemple"
    Coder (en hexadécimal et en décimal) à l'aide de la table de caractère ASCII la phrase suivante :
    
    ```Ceci N'est PAS```

    ???- done "Réponse"    
        
        <div class="Center_txt Pas_gris">

        | | C | e | c | i |   | N | ' | e | s | t |   | P | A | S |
        |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
        | Hex | 43 | 65 | 63 | 69 | 20 | 4E | 27 | 65 | 73 | 74 | 20 | 50 | 41 | 53 |
        | Dec | 67 | 101 | 99 | 105 | 32 | 78 | 39 | 101 | 115 | 116 | 32 | 80 | 65 | 83 |
 
        </div>

!!! warning "Hexadécimal pour les humains, binaire pour la machine !"
    Naturellement pour un ordinateur, le caractère C n'est pas associé à la valeur 43 (en hexadécimal) ou 67 (en décimal). Il est associé à $\base{100\ 0011}$ !


???- example "Exemple"
    Décoder le message suivant, coder à l'aide la table ASCII et écrit en hexadécimal :
    
    75 6E 20 6D 65 73 73 61 67 65 20 73 65 63 72 65 74 20 21 

    ???- done "Réponse"

        |Hex | 75 | 6e | 20 | 6d | 65 | 73 | 73 | 61 | 67 | 65 | 20 | 73 | 65 | 63 | 72 | 65 | 74 | 20 | 21 |
        |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
        | | u | n |   | m | e | s | s | a | g | e |   | s | e | c | r | e | t |   | ! |

!!! danger "codage $\neq$ cryptage"
    Il ne faut pas confondre codage et cryptage :

    - codage : règles pour qu'un objet soit représenté dans un ordinateur
    - cryptage : règles permettant de rendre un texte illisible pour toutes personnes n'ayant pas la méthode appropriée

???- info "Plus précisément"
    En fait, un codage d'un élément se fait en 2 étapes. Mais parfois, la seconde étape se confond avec la première :
    
    - associer un nombre binaire à l'objet (ou des nombres binaires à différentes parties de l'objet)
    - choisir une manière (éventuellement une structure) d'écrire ce nombre pour une machine

    Par exemple, avec la table ASCII :
    
    - la lettre C est associée au nombre binaire $\base{100\ 0011}$
    - il a été choisi (pour ce codage) d'écrire ce nombre sur un octet, c'est-à-dire : $\base{0100\ 0011}$
 
    Ici, la différence est minime. Mais pour d'autres codages cela peut être plus important !
 
Mais il y a un problème pour les langues autres que l'anglais : pas d’accents. De plus, il y a eu [de nombreuses variantes](https://fr.wikipedia.org/wiki/American_Standard_Code_for_information_Interchange#Extensions_mono-octets) pour utiliser le 8ème bit (Mac, IBM, Microsoft, $\ldots$)

Les limites de l’ASCII ont conduit, sur trois périodes différentes, à trois approches de l'internationalisation :
<ul>
<li> L'utilisation de standards régionaux à caractères mono-octets, techniquement les plus faciles à mettre en place (mais attention aux échanges de fichiers entre les différentes langues. Sauriez-vous expliquer pourquoi ?);
</li>
<li> L'utilisation de standards extensibles, où un même octet peut représenter un caractère différent suivant le contexte (famille ISO 2022) ainsi que des extensions où un caractère est codé sur plusieurs octets ;
</li>
<li> L'utilisation du Standard Unicode (famille UTF). C’est celui qui comprend le plus grand nombre de caractères. Il est devenu la norme !
</li>
</ul>

???- tip "Une disposition réfléchie"
    Les 128 caractères de l’ASCII n’ont pas été placés au hasard. Leurs codes ont été soigneusement étudiés. Ci-dessous, quelques exemples.
    <ul>
    <li> À l’époque reculée où a été conçu l’ASCII, on communiquait encore parfois des données à l’ordinateur via des cartes perforées. Chaque emplacement codait un bit : 1 s’il y avait un trou, 0 sinon. La perforation était irréversible. Lorsqu'on n’avait pas encore spécifié de caractère particulier, on laissait tous les emplacements intacts et le caractère valait donc 0 (tous les bits à 0). Ce caractère « non spécifié » se retrouve en ASCII avec NUL, le caractère nul, qui est associé à 0. De même, lorsqu’on voulait effacer un caractère on perçait tous les emplacements, ce qui donnait 127 (tous les bits à 1) ; le caractère ASCII DEL (delete) correspond justement à cette suppression.
    </li>
    <li> Les lettres majuscules sont séparées de leurs homologues minuscules par un intervalle de 32. Cela signifie qu’il suffit de modifier un bit (le 6e) pour passer des unes aux autres, ce qui simplifie les traitements.
    </li>
    </ul>


