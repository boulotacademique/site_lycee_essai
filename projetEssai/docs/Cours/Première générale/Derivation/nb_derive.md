# Dérivation<br>Nombre Dérivée

## Le nombre dérivée.

### Limite réelle d'une fonction en 0.

Dans l'activité précédente,  $\frac{d(2.4+h) - f(2.4)}{h} = 24 + 5h$ pour $h \neq 0$.

On remarque que l'on peut rapprocher ce rapport de plus en plus de $24$ en donnant à $h$ des valeurs de plus en plus proche de $0$. On dit que &laquo; $\frac{f(2.4+h) - f(2.4)}{h}$ tend vers $24
$ lorsque $h$ tend vers $0$ &raquo; ou que &laquo; la limite de $\frac{f(2.4+h) - f(2.4)}{h}$  lorsque h tend vers $0$ vaut $24$ &raquo; et on écrit alors $\lim_{x \rightarrow 0}{\frac{f(2.4+h) - f(2.4)}{h}} = 24$.

### Le nombre dérivé.
!!! info "Définition"
    $t(h) = \frac{f(a+h) - f(a)}{h}$ s'appelle le taux de variation de $f$ entre $a + h$ et $a$.


!!! info "Définition"
    $f$ est une fonction et $a$ un réel de son ensemble de définition. Dire que la fonction $f$ est **dérivable en $a$** signifie que la fonction $t(h) = \frac{f(a+h) - f(a)}{h}$  admet une limite réelle $l$ en $0$ qu'on appelle alors **le nombre dérivé** de $f$ en $a$. On le note $f '(a)$.

### Tangente à une courbe.

$\mathcal{C}_f$ est la courbe représentative d'une fonction $f$ qui est dérivable au point d'abscisse $a$. $A$ est le point de $\mathcal{C}_f$ de coordonnées $(a ; f(a))$.

Notons $M$ le point de $\mathcal{C}_f$ d'abscisse $a + h$, $h \neq 0$.

$t(h) = \frac{f(a+h) - f(a)}{h}$ est le coefficient directeur de la sécante $(AM)$.

Comme $f$ est dérivable en $a$  $\lim_{h \rightarrow 0}{\frac{f(a+h) - f(a)}{h}}   = f '(a)$.

La droite $T$, qui passe par $A$ et de coefficient directeur $f ' (a)$, peut se voir comme la &laquo; position limite &raquo; des sécantes $(AM)$ lorsque $M$ se rapproche de $A$. La droite $T$ correspond à l'idée intuitive de &laquo; tangente à une courbe &raquo;.

!!! info "Définition"
    $\mathcal{C}_f$ est la courbe représentative d'une fonction $f$ qui est dérivable au point $a$. La tangente à $\mathcal{C}_f$ au point $A(a ; f(a))$ est la droite qui passe par $A$ et dont le coefficient directeur est $f '(a)$.

!!! abstract "Théorème"
    Une équation de la tangente à $\mathcal{C}_f$ au point $A(a ; f(a))$ est $y = f '(a)(x - a) + f(a)$.


???- info "Approximation affine."

    Si $\mathcal{C}_f$ est la courbe représentative d'une fonction $f$ dérivable au point d'abscisse $a$ et $T$ la tangente à $\mathcal{C}_f$ au point $A(a ; f(a))$.

    Comme $T$ &laquo;semble&raquo; proche de la courbe $\mathcal{C}_f$ autour du point $A$, on pense remplacer $\mathcal{C}_f$ par $T$ autour de $A$.

    Soit $M$ de $\mathcal{C}_f$ d'abscisse $a + h$, et $N$ de $T$ d'abscisse $a + h$.

    $M(a + h ; f(a + h))$ et $N(a + h ; f'(a) \times (a + h - a) + f(a))$. D'où $N(a + h ; f'(a)  \times h + f(a))$.

    $MN = \left| f(a+h)-f(a) -f'(a)\times h \right|$.

    Or $\frac{f(a+h) - f(a)}{h} = f'(a) +  \Phi(h)$ où $\lim_{h \mapsto 0} \Phi(h) = 0$ donc $f(a + h) - f(a) - h f'(a) = h \Phi(h)$.
    
    Comme $\lim_{h \rightarrow 0}{h \Phi(h)}=0$, on a \\$f(a + h) \approx f(a) + hf'(a)$ pour $h$ proche de $0$.

???- example "Exemple"
    \[ f(x) = x^3 \]

    - Déterminez l'approximation affine locale de $f(1+ h)$ puis prouvez que l'erreur commise est inférieure à $4h$ lorsque $0<h<1$.
    - Déduisez-en une valeur approchée de $(1,001 47)^3$ en précisant l'erreur commise.

    ???- done "Solution"

        - $t(h) = \frac{(1+h)^3-1}{h} = \frac{1+ 3h+3h^2+h^3-1}{h} = \frac{h(3+3h+h^2)}{h} = 3 + 3h +h^2$ pour $h \neq 0$.  
        $f '(1) = 3$ et $\Phi(h) = 3h + h^2$.  
        Donc $f(1+h) \approx f(1) + h f '(1) = 1+ 3h$.  
        L'erreur :  
        $E(h) = f(1+h) - (f(1) + h f'(1)) = h \Phi(h) = h^2(3 + h)$ donc  

        \[ \begin{eqnarray*}
        0  <  h  <  1 & \iff & 0 < 3 < h+3 < 4 \\
        0  <  h  <  1 & \iff & 0 < h^2 < h \\
         \text{Donc } &  & 0  < E(h) < 4h \\
        \end{eqnarray*} \]
        
        - $(1, 00147)^3 \approx 1 + 3 \times 0,00147 = 1,00441$ l'erreur commise est inférieure à $4 \times 0.00147 = 0,0588$.  
        $1,00441-0,0058 < (1,00147)^3 < 1,00441+0,0058$.

