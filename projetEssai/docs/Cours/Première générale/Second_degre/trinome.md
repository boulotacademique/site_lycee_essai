# Polynôme du second degré<br>Forme canonique

<div class="Chap_title">
Polynôme du second degré
</div>

## Le trinôme du second degré

!!! info "Définition"
    Un trinôme du second degré (ou trinôme) est une fonction polynôme de degré 2, c'est-à-dire une fonction $f$ définie sur $\R$ et pouvant s'écrire sous la forme $ax^2+bx+c$ ($a,b,c$ étant des réels) avec $a \neq 0$.

    Les réels $a,b$ et $c$ sont appelés les coefficients du trinôme.


!!! info "Définition"
    Une équation du second degré à une inconnue est une équation qui peut s'écrire $ax^2~+~bx~+~c=~0$ avec $a \neq 0$.

## Forme canonique.

On pose pour la suite $f(x) = ax^2+bx+c$ avec $a\neq 0$.

!!! info "Définition"
    On appelle forme canonique d'un trinôme l'expression de ce trinôme où $x$ n'apparait qu'une fois et avec un coefficient égal à $1$. Donc pour les trinômes \[ ax^2+bx+c=a(x-\alpha)^2+\beta\]


???- example "Exemple"
    $2\left( x-5 \right)^2$ est la forme canonique de $2x^2-20x+50$.

???- example "Exemple"
    Comment trouver la forme canonique ? En suivant les étapes de l'exemple ci-dessous :
    
    \begin{eqnarray*}
    2x^2+6x+1 & = & 2\left( x^2 + 3x \right)+ 1 
    \end{eqnarray*}

    Puis, on remarque que $x^2 + 3x$ est le début d'une identité remarquable. $x^2+3x = x^2 + 2 \times \frac{3}{2} \times x$. Donc de $x^2~+~2~\times~\frac{3}{2}~\times~x~+~\left(~\frac{3}{2}~\right)^2~=~\left(~x~+~\frac{3}{2}~\right)^2$, on déduit $x^2+3x = \left( x + \frac{3}{2} \right)^2 - \left( \frac{3}{2} \right)^2$. D'où :

    \begin{eqnarray*}
    2x^2+6x+1 & = & 2\left( x^2 + 3x  \right) + 1\\
    & = & 2 \left(\left( x + \frac{3}{2} \right)^2 - \left( \frac{3}{2} \right)^2 \right) + 1 \\
    & = & 2 \left(\left( x + \frac{3}{2} \right)^2 \right) - \frac{9}{2} + 1 \\
    & = & 2 \left( x + \frac{3}{2} \right)^2 - \frac{7}{2}
    \end{eqnarray*}

???+ note "A retenir"
    Rappel : A partir de la forme canonique, on peut retrouver les coordonnées du sommet et l'allure (&laquo; vers le haut &raquo; ou &laquo; vers le bas &raquo;).

On note, ici, $f(x) = ax^2+bx+c$, avec $a \neq 0$.

Ecriture de $f$ sous forme canonique : on procède comme dans l'exemple.

Puisque $a\neq 0$ :

\[ \begin{eqnarray*}
f(x) & = & a \left( x^2 + \frac{b}{a}x \right) + c 
\end{eqnarray*} \]

Or 

\[ \begin{eqnarray*}
x^2+\frac{b}{a}x & = & x^2 + 2 \times \frac{b}{2a}x \\
 & = & \underbrace{x^2 + 2 \times \frac{b}{2a}x + \left( \frac{b}{2a} \right)^2}_{\text{Identité remarquable}} - \left( \frac{b}{2a} \right)^2 \\
 & = & \left( x + \frac{b}{2a} \right)^2 - \left( \frac{b}{2a} \right)^2 
\end{eqnarray*} \]

D'où :

\[ \begin{eqnarray*}
f(x) & = & a \left( \underbrace{x^2 + \frac{b}{a}x}_{\text{Cf ci-dessus}}\right)  + c \\
 & = & a \left( \left( x + \frac{b}{2a} \right)^2 - \left( \frac{b}{2a} \right)^2\right)  + c \\
 & = & a \left( \left( x + \frac{b}{2a} \right)^2 -  \frac{b^2}{4a^2}  \right) + c \\
 & = & a \left( x + \frac{b}{2a} \right)^2 -  \frac{b^2}{4a} +c \\
  & = & a \left( x + \frac{b}{2a} \right)^2 -  \frac{b^2-4ac}{4a} 
\end{eqnarray*}
\]

!!! abstract "Théorème"
    La forme canonique de $ax^2+bx+c$ ($a \neq 0$) est $a  \left( x + \frac{b}{2a} \right)^2 -  \frac{b^2-4ac}{4a}$.

    \[ ax^2+bx+c = a\left( x + \frac{b}{2a} \right)^2 -  \frac{b^2-4ac}{4a}\]


!!! info "Définition"
    Le nombre $b^2-4ac$ est appelé le discriminant de l'équation du second degré $ax^2+bx+c=0$. On le note $\Delta$.

    \[ \Delta = b^2-4ac \]

???+ note "Remarques"

    - Le discrimnant est lié aux coefficients du trinôme (et pas à une équation). Il est très utile pour les équations, les inéquations, l'allure de la courbe, ...
    - Il est possible de trouver le discrimant d'une autre façon : $\Delta = -4a \times f\left( \dfrac{-b}{2a}\right)$