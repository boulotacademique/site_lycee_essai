# Trigonométrie<br>Radian

## Enroulement de la droite numérique

!!! note "Définition"
    Le cercle trigonométrique $C$ est le cercle de centre $O$ et de **rayon 1**. Il est muni d'un sens de parcours appelé **sens direct**, qui est le sens inverse des aiguilles d'une montre.

    Avec ce choix, on dit que le **plan est orienté**.

Les points $I$ et $J$ sont situés sur le cercle trigonométrique. La droite ($d$) a pour équation $x = 1$. C'est une droite numérique pour laquelle on considère le repère ($I$ ; $K$) dont l'origine est $I$ et $K(1,1)$ dans le repère ($O$ ; $I$ , $J$).
<!--tel que $IK = 1$.-->

On enroule la demi-droite [$IK$) autour du cercle $C$ dans le sens inverse des aiguilles d'une montre. Ainsi, à tout nombre réel $x$ positif correspond un unique point-image $M$ sur le cercle $C$.

DESSIN A FAIRE

Sur la figure, on voit $M$ le point-image de $KR$ sur le cercle trigonométrique.

En enroulant la demi-droite correspondant aux nombres réels négatifs dans le sens des aiguilles d'une montre, on fait également correspondre à tout nombre réel $x$ négatif un point $M$ sur le cercle $C$.

Dans chacun de ces deux cas, on dit que $x$ a pour point-image $M$ sur le cercle $C$. Si $x'$ est un nombre obtenu à partir de $x$ en ajoutant ou en enlevant un nombre de tours ($k \times 2\pi,k\in \Z$), alors $x$ et $x'$ ont le même point-image sur $C$. Ainsi, un point du cercle est l'image d'une infinité de réels (positifs et négatifs).

!!! abstract "Théorème"
    Tout nombre réel $x$ a un point-image unique sur le cercle $C$.
    
    S'il existe $k\in{}\Z$ tel que $x'=x+k\times{}2\pi{}$, alors $x$ et $x'$ ont le même point-image sur le cercle $C$.

## Le radian

!!! note "Définition- Radian"
    La mesure en **radian** d'un angle est égale à la longueur de l'arc du cercle trigonométrique qu'il intercepte.

    Le radian est noté \textcolor{H1}{rad}. Cette notation est omise en général, contrairement à celle du degré.

    DESSIN A FAIRE

???- example "Exemple"
    Un angle plat (180$^\circ$) mesure exactement $\pi$ radians, soit environ 3,14 radians.

!!! abstract "Théorème"
    Les mesures des angles en degré et en radian sont proportionnelles.

!!! tip "Méthode - Convertir entre degrés et radians"
    Il suffit d'utiliser la propotionnalité et le fait que $180^°$ correspond à $\pi$ rad.
    
    ???- example "Exemple"
        Calculer les nombres $x$, $y$ et $z$ dans le tableau suivant de conversion entre degrés et radians.

        \[ \begin{array}{|l|*5{c|}}
        \hline
        \textbf{Mesure en degré}  &   0  & 30  & y  &   150  &   180  \\
        \hline
        \textbf{Mesure en radian}  &  0  &  x  & \rule[-3ex]{0pt}{1.5cm} \dfrac{\pi}{2} & z  & \pi  \\
        \hline
        \end{array} \]

        ???- done "Solution"

            $\dfrac{180}{30}=6$ donc $x=\dfrac{\pi{}}{6}$rad.  
            $\dfrac{\pi}{2}$ rad est la moitié de $\pi{}$ rad, donc $y$ est la moitié de 180 degrés, c'est-à-dire $y = 90^\circ{}$ et $z=\dfrac{150\times{}\pi{}}{180}=\dfrac{5\pi{}}{6}$.
