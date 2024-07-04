# Dérivation<br>Découverte

!!! abstract "Théorème"
    Un corps en chute libre, lâché sans vitesse initiale a parcouru au bout de $t$ secondes la distance $d(t)$ (en mètres) exprimée par :
    
    \[ d(t) = 5 t^2 \]
    
    $\quad \text{en fait, c'est } d(t)=\dfrac{1}{2}g t^2 \text{ mais on prend } g \approx 10.$


1. Calculer la distance parcourue par le corps en chute libre au bout de $0,1,2,3,4,5$ secondes. Tracer la courbe représentative $\mc{C}$ de la fonction $d$ sur l'intervalle $[0;5]$.
2. **Le point de vue cinématique**
    1. Calculer la vitesse moyenne du corps en chute libre dans les intervalles de temps $[0;1],[1;2],[2;3],[3;4],[4;5]$.
    2. Soit $h$ un réel strictement positif. Calculer la vitesse moyenne du corps en chute libre dans les intervalles de temps $[t;t+h]$ et $[t-h;t]$.  
    *Application numérique :* $t=2\,s$ et $h=0.1\,s$.
    3. &laquo; *La vitesse instantanée à l'instant $t$ est $v(t)=10t \, m.s^{-1}$* &raquo;. Expliquer cette affirmation.
    4. Application : un corps est lâché sans vitesse initiale d'une altitude de $25$ mètres. Quelle est, en $km.h^{-1}$, sa vitesse au moment de l'impact avec le sol ?  
    <div class = "Bord Center_ss_bd Vignette50">La quantité $\dfrac{d(t+h)-d(t)}{h}$ s'appelle **l'accroissement moyen** de la fonction $d$ entre $t$ et $t+h$.</div>  
3. **Le point de vue graphique**  
On considère la courbe représentative $\mc{C}$ de la fonction $t \mapsto d(t)$ au voisinage d'un point $M$ de la courbe d'abscisse $t$. On désigne par $M_h$ le point de la courbe d'abscisse $t+h$ ($h$ étant un réel quelconque).  
    1. Calculer le coefficient directeur de la droite $(MM_h)$. Quel lien peut-on établir avec la question $2. b.$ ?
    2. On considère la droite $\Delta(t)$ passant par $M$ et de pente $10t$. Tracer dans un même repère la courbe $\mc{C}$ et la droite $\Delta(t)$ lorsque $t=0.5$ ; puis lorsque $t=1$.  
    Que constate-t-on ?  
    <div class = "Bord Center_ss_bd Vignette50"> La droite $\Delta(t)$ de pente $v(t)$ et passant par $M$ est **la tangente à la courbe**.</div>
4. **Le point de vue numérique**  
A un instant $t_0$, la vitesse du corps en chute libre est de $v=24 m.s^{-1}$.
    1. Calculer $t_0$, $d(t_0)$.
    2. Calculer (en fonction de $h$) $d(t_0+h)-d(t_0)$.
    3. En déduire que $d(t_0+h)=d(t_0)+24h+5h^2$.
    4. La quantité $d(t_0)+24h$ est donc une approximation (affine) de $d(t_0+h)$. Quelle est l'erreur de cette approximation lorsque $h=1, h=0.1, h=0.01$ ?  
    <div class = "Bord Center_ss_bd Vignette50"> Le nombre $v$ tel que $d(t_0+h)=d(t_0)+v \times h + 5h^2$ s'appelle **le nombre dérivé** de $d$ en $t_0$. Ce nombre se note $d'(t_0)$. </div>
