# Statistique<br>Variance et écart-type

## Définition

Dans tout ce paragraphe $S$ désigne une série statistique, avec les notations suivantes :

\[
\begin{array}{|c|c|c|c|c|}
\hline
\textrm{Valeur} & x_1 & x_2 & \ldots & x_p\\
\hline
\textrm{Effectif} & n_1 & n_2 & \ldots & n_p\\
\hline
\end{array} \]

\[ N = n_1 + n_2+\ldots+n_p = \sum_{i=1}^p n_i \]

Et on note $\overline{x}$ la moyenne de cette série.

!!! note "Définition - Variance"
    La **variance V** de la série statistique est :
    
    \[ V = \frac{1}{N} \sum_{i=1}^p n_i(x_i - \overline{x})^2 \]


En pratique, pour calculer une variance il y a deux possibilités :

- utiliser sa calculatrice qui donne l'écart-type (cf. après) permettant d'avoir la variance
- faire un tableau pour présenter les calculs (cf. ci dessous)



???- example "Exemple"

    \[
    \begin{array}{|c|c|c|c|c|}
    \hline
    \textrm{Valeur} & 8 & 9 & 10 & 11\\
    \hline
    \textrm{Effectif} & 1 & 3 & 5 & 1\\
    \hline
    \end{array}
    \]

    On commence par calculer la moyenne : $\overline{x} = 9.6$. 
    Puis on mène les calculs suivants :

    \[
    \begin{array}{|c|c|c|c|c|}
    \hline
    \textrm{Valeur} & 8 & 9 & 10 & 11\\
    \hline
    \textrm{Effectif} & 1 & 3 & 5 & 1\\
    \hline
    \hline
    x_i - \overline{x} & -1.6 & -0.6 & 0.4 & 1.4\\
    \hline
    (x_i - \overline{x})^2 & 2.56 & 0.36 & 0.16 & 1.96\\
    \hline
    n_i(x_i - \overline{x})^2 & 2.56 & 1.08 & 0.8 & 1.96\\
    \hline
    \end{array}
    \]

    Puis on ajoute les valeurs de la dernière ligne et on divise par $N = 10$. D'où $V=0.64$

!!! note "Définition - Ecart-type"
    L'**écart-type $\mathbf{\sigma}$** de la série statistique est la racine carrée de sa variance : $\sigma = \sqrt{V}$.

!!! info "Remarque"
    Votre calculatrice ne donne pas la variance, mais l'écart-type $\sigma$. On obtient donc la variance avec $V=\sigma^2$\\
    Pour obtenir l'écart-type avec votre calculatrice :

    - Remplir les listes statistiques comme en seconde pour obtenir une moyenne.
    - Faire la manipulation comme en seconde pour obtenir une moyenne.
    - Lire $x \sigma n$ ou $\sigma x$ pour obtenir l'écart-type.

!!! abstract "Théorème"
    
    \[ V = \left(\frac{1}{N} \sum_{i=1}^p n_i x_i ^2\right) - \overline{x}^2 \] 

???- abstract "Démonstration"
    
    \[
    \begin{eqnarray*}
    \frac{1}{N} \sum_{i=1}^p n_i(x_i - \overline{x})^2 & = & \frac{1}{N} \sum_{i=1}^p n_i(x_i^2 - 2 x_i \overline{x} + \overline{x}^2) \\
    &=&\frac{1}{N} (n_ix_i^2 + \ldots + n_px_p^2 -2 \overline{x} (n_1x_1+\ldots+n_px_p)+\overline{x}^2(n_1 + \ldots + n_p))\\
    &=&\frac{1}{N} \left( \sum_{i=1}^p n_i x_i^2 - 2 \left(\sum_{i=1}^p n_i x_i\right) \overline{x} + \sum_{i=1}^p n_i \overline{x}^2 \right) \\
    &=&\frac{1}{N} ( n_ix_i^2 + \ldots + n_px_p^2) - 2\overline{x} \underbrace{\frac{1}{N} (n_1x_1+\ldots+n_px_p)}_{\overline{\textstyle{x}}} + \overline{x}^2\underbrace{\frac{1}{N}(n_1 + \ldots + n_p)}_{\textstyle{1}} 
    \end{eqnarray*}
    \]

    \[ 
    \begin{eqnarray*}
    \frac{1}{N} \sum_{i=1}^p n_i(x_i - \overline{x})^2 &=&\frac{1}{N} \sum_{i=1}^p n_i x_i^2 - 2 \overline{x} \left(\frac{1}{N} \sum_{i=1}^p n_i x_i\right)  + \left(\frac{1}{N} \sum_{i=1}^p n_i\right) \overline{x}^2   \\
    &=&\left(\frac{1}{N} \sum_{i=1}^p n_i x_i^2\right) - 2 \overline{x}^2 + \overline{x}^2   \\
    &=&\left(\frac{1}{N} \sum_{i=1}^p n_i x_i^2\right) - \overline{x}^2   \\
    \end{eqnarray*}
    \]

    Pour passer de la ligne 5 à la ligne 6, pensez à la formule de la moyenne.


!!! abstract "Théorème"
    Cette variance apparait lorsqu'on veut minimiser la fonction suivante :
    
    \[ f(a) = \frac{1}{N} \sum_{i=1}^n n_i(x_i - a)^2 \]

    La fonction $f$ précédente possède un minimum pour $a=\overline{x}$. Ce minimum est donc la variance $V$.


???- abstract "Démonstration"

    \[ \begin{eqnarray*}
    f(a) &=& \frac{1}{N} \sum_{i=1}^p n_i(x_i-a)^2 \\
    &=&\frac{1}{N} \left(n_1(x_1-a)^2 + \ldots + n_p(x_p-a)^2\right) \\
    &=&\frac{1}{N} (n_1(x_1^2-2ax_1+a^2) + \ldots + n_p(x_p^2-2ax_p + a^2)) \\
    &=&\frac{1}{N} \left((n_1x_1^2 + \ldots + n_p x_p^2) -2a \underbrace{(n_1 x_1 + \ldots + n_p x_p)}_{\textstyle{N} \overline{\textstyle{x}}} + a^2 \underbrace{(n_1 + \ldots + n_p)}_{\textstyle{N}}\right) \\
    &=&\left(\frac{1}{N} \sum_{i=1}^p n_ix_i^2\right) -2a\overline{x} + a^2 \\
    \end{eqnarray*}
    \]

    Or

    \[ -2a\overline{x} + a^2 = (\overline{x}-a)^2 - \overline{x}^2 \]

    D'où

    \[ \begin{eqnarray*}
    f(a) & = & \left(\frac{1}{N} \sum_{i=1}^p n_ix_i^2\right) + (\overline{x}-a)^2 - \overline{x}^2 \\
    &=& (\overline{x}-a)^2 + k \quad \textrm{où $k$ est un réel connu à partir des données de $S$}  \\
    \end{eqnarray*} \]

    Donc $f$ atteint son minimum pour $a = \overline{x}$ et son minimum vaut 
    
    \[ f(\overline{x})=\frac{1}{N} \sum_{i=1}^p n_i(x_i-\overline{x})^2=V \] 


!!! info "Remarque"
    D'une façon rapide, on peut dire que l'écart-type mesure la distance moyenne entre la moyenne de la série et les valeurs.



???- info "Remarque - Pour aller plus loin"
    On peut s'intéresser à une autre façon de mesurer des distances. Pour cela on s'intéresse à la fonction $f(a)=\dfrac{1}{N}\sum_{i=1}^p n_i |x_i - a |$. Son minimum est atteint pour $a$ égale à la médiane de la série.


## Transformation affine des données

!!! abstract "Théorème"
    Lorsque on ajoute un même nombre à chacune des valeurs d'une série statistique, la variance, l'écart-type et l'écart interquartile sont inchangés.

!!! abstract "Théorème"
    Lorsqu'on multiplie par un même nombre $a$ strictement positif chacune des valeurs d'une série statistique :

    - la variance est multipliée par $a^2$
    - l'écart-type et l'écart interquartile sont multipliés par $a$


$a$ est un réel strictement positif, $b$ un réel.  

\[
\begin{array}{|c|c|c|c|c|c|c|}
\hline
\text{Valeur de la série} & \text{moyenne} & \text{variance} & \text{écart-type} & 1^{\textrm{er}} \text{quartile} & 3^{\textrm{ème}} \text{quartile} & \text{écart interquartile} \\
\hline
x_i & \overline{x} & V = \sigma^2 & \sigma & Q_1 & Q_3 & Q_3-Q_1 \\
\hline
ax_i+b & a \overline{x} + b & a^2V & a \sigma & aQ_1 + b & aQ_3 + b & a(Q_3-Q_1)\\
\hline
\end{array} 
\]