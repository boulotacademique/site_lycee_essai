# Vecteur<br>Colinéarité

!!! info "Définition"
    On dit que deux vecteurs non nuls $\vec{u}$ et $\vec{v}$ sont colinéaires s'il existe un réel $k$ tel que : $\vec{v}= k \vec{u}$.

    Autrement dit, leurs coordonnées dans le repère $\left(O ; I, J \right)$ sont proportionnelles.

    Par convention, on dit que $\vec{0}$ est colinéaire à tout vecteur. 


!!! abstract "Théorème"
    Soit $\vec{u} \left( \begin{array}{c} x \\ y \end{array} \right)$ et $\vec{v} \left( \begin{array}{c} x' \\ y'\end{array}\right)$ deux vecteurs du plan. Les vecteurs $\vec{u}$ et $\vec{v}$ sont colinéaires si et seulement si : 

    \[ xy'-yx'=0 \]


???- abstract "Démonstration"

    - Si $\vec{u}=\vec{0}$ (ou $\vec{v}=\vec{0}$), alors quelque soit $\vec{v}$ $\coordVec{x'}{y'}$, $\vec{v}$ et $\vec{u}$ sont colinéaires. Et on a bien $xy'-yx'=0$.  
    Réciproquement, pour tout $x',y'$, $0 \times y' - 0 \times x'=0$ et $\vec{0}$ est bien colinéaire à n'importe quel vecteur.
    - Soit $\vec{u}\neq \vec{0}$ et $\vec{v}\neq\vec{0}$, $\vec{u} \coordVec{x}{y} \neq \coordVec{0}{0}$ et $\vec{v} \coordVec{x'}{y'}\neq \coordVec{0}{0}$.
    Si $\vec{u}$ et $\vec{v}$ sont colinéaires, alors il existe $k$ tel que $\vec{u}=k \vec{v}$. Donc $\left\{ \begin{array}{rcl} x &= & k x' \\ y & = & ky' \end{array} \right.$ Comme $\vec{v} \coordVec{x'}{y'}\neq \coordVec{0}{0}$, $x' \neq 0$ ou $y' \neq 0$. Supposons $x' \neq 0$. De $x = k x'$, on a $k= \dfrac{x}{x'}$. Donc $y= \dfrac{x}{x'} y'$. Et donc $xy'-yx'=0$.

!!! warning "... et dans l'espace"
    La définition est importante. Car dans l'espace, la formule $xy'-yx'=0$ n'existe pas.

!!! abstract "Théorème"
    <span di="col_par">On considère quatre points $A$, $B$, $C$ et $D$ avec $A$ distinct de $B$ et $C$ distinct de $D$.</span>

    Les vecteurs $\vect{AB}$ et $\vect{CD}$ sont colinéaires si, et seulement si, les droites $(AB)$ et $(CD)$ sont parallèles.

!!! abstract "Corollaire"
    Trois points $A$, $B$ et $C$ sont alignés si, et seulement si, $\vect{AB}$ et $\vect{AC}$ sont colinéaires.