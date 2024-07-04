# Polynôme du second degré<br>Résolution d'équations

## Factorisation

On rappelle que 

\[ 
\begin{eqnarray*}
f(x) & = & ax^2+bx+c \\
& = & a\left( x + \frac{b}{2a} \right)^2 -  \frac{\Delta}{4a} \quad \text{ avec } \Delta = b^2-4ac \\
& = & a \left[ \left( x + \frac{b}{2a} \right)^2 -  \frac{\Delta}{4a^2} \right]
\end{eqnarray*}
\]

Comme $4a^2>0$, $\frac{\Delta}{4a^2}$ est du signe de $\Delta$.

- Si $\Delta < 0$, alors il n'est pas possible d'écrire $\frac{\Delta}{4a^2}$ comme un carré.
- Si $\Delta = 0$, alors $f(x) = ax^2 + bx + c = a \left( x + \frac{b}{2a} \right)^2$ est factorisée.
- Si $\Delta > 0$, alors $\frac{\Delta}{4a^2} = \left(\dfrac{\sqrt{\Delta}}{2a}\right)^2$

\[ 
\begin{eqnarray*}
f(x) & = & a \left[ \left( x + \frac{b}{2a} \right)^2 -  \frac{\Delta}{4a^2} \right]\\
& = & a \left[ \left( x + \frac{b}{2a} \right)^2 -  \left( \frac{\sqrt{\Delta}}{2a}\right)^2 \right]\\
 & = & a \left[ \left(x+\frac{b}{2a} \right) - \frac{\sqrt{\Delta}}{2a} \right] \left[ \left(x+\frac{b}{2a} \right) + \frac{\sqrt{\Delta}}{2a} \right] \\
 & = & a \left[ x+\frac{b}{2a}  - \frac{\sqrt{\Delta}}{2a} \right] \left[ x+\frac{b}{2a}  + \frac{\sqrt{\Delta}}{2a} \right]
\end{eqnarray*}
\]

!!! info "Théorème"
    Soit $f(x) = ax^2 + bx +c$, avec $a \neq 0$. Son discriminant est $\Delta = b^2 - 4ac$.

    - Si $\Delta < 0$, alors il n'est pas possible de factoriser $f(x) = ax^2 + bx +c$ ;
    - Si $\Delta = 0$, alors la forme factorisée de $f$ est $ax^2+bx+c = \left( x + \frac{b}{2a} \right)^2$ ;
    - Si $\Delta > 0$, alors la forme factorisée de $f$ est $ax^2+bx+c = a \left[ x+\frac{b}{2a}  - \frac{\sqrt{\Delta}}{2a} \right] \left[ x+\frac{b}{2a}  + \frac{\sqrt{\Delta}}{2a} \right]$.

    En pratique, ce dernier cas n'est pas à apprendre par coeur. On verra un peu plus loin comment faire.

## Equation

On souhaite résoudre l'équation $ax^2 + bx + c = 0$. La méthode générale consiste à s'appuyer une éventuelle factorisation.

- Si $\Delta = b^2 - 4ac < 0$, alors 

\[
\begin{eqnarray*}
ax^2 + bx + c = 0 & \iff & a \left[ \left( x + \frac{b}{2a} \right)^2 -  \frac{\Delta}{4a^2} \right] = 0\\
& \iff & \left( x + \frac{b}{2a} \right)^2 -  \frac{\Delta}{4a^2} = 0 \quad \text{ car } a \neq 0\\
& \iff & \left( x + \frac{b}{2a} \right)^2 =  \frac{\Delta}{4a^2} < 0\\
\end{eqnarray*}
\]

Or un carré est toujours positif. Donc, si $\Delta <0$, $ax^2+bx+c = 0$ n'a pas de solution réelle.

- Si $\Delta = b^2 - 4ac = 0$, alors 

\[
\begin{eqnarray*}
ax^2 + bx + c = 0 & \iff & a \left( x + \frac{b}{2a} \right)^2 = 0\\
& \iff & \left( x + \frac{b}{2a} \right)^2 = 0 \quad \text{ car } a \neq 0\\
& \iff &  x + \frac{b}{2a}  =  0\\
& \iff & x = \frac{-b}{2a}
\end{eqnarray*}
\]

Donc, si $\Delta = 0$, $ax^2+bx+c = 0$ possède une unique solution $x_0 = \dfrac{-b}{2a}$.

- Si $\Delta = b^2 - 4ac > 0$, alors 

\[
\begin{eqnarray*}
ax^2 + bx + c = 0 & \iff & a \left[ x+\frac{b}{2a}  - \frac{\sqrt{\Delta}}{2a} \right] \left[ x+\frac{b}{2a}  + \frac{\sqrt{\Delta}}{2a} \right] = 0\\
& \iff & \left[ x+\frac{b}{2a}  - \frac{\sqrt{\Delta}}{2a} \right] \left[ x+\frac{b}{2a}  + \frac{\sqrt{\Delta}}{2a} \right]= 0 \quad \text{ car } a \neq 0\\
& \iff & x = -\frac{b}{2a}  + \frac{\sqrt{\Delta}}{2a} \quad \text{ ou } \quad x = -\frac{b}{2a}  - \frac{\sqrt{\Delta}}{2a} \\
& \iff & x = \dfrac{-b + \sqrt{\Delta}}{2a} \quad \text{ ou } \quad x = \dfrac{-b - \sqrt{\Delta}}{2a}
\end{eqnarray*}
\]

Donc, si $\Delta > 0$, $ax^2+bx+c = 0$ possède deux solutions $x_1 = \dfrac{-b + \sqrt{\Delta}}{2a}$ et $x_2 = \dfrac{-b - \sqrt{\Delta}}{2a}$.

!!! info "Théorème et définition"
    Soit $f(x) = ax^2 +bx +c$ avec $a \neq 0$ et le discriminant associé $\Delta = b^2 - 4ac$.

    - Si $\Delta < 0$, $f(x) = 0$ n'a pas de solution réelle.
    - Si $\Delta = 0$, $f(x) = 0$ possède <span id="sol_double_sec_deg">une unique solution</span> $x_0 = \dfrac{-b}{2a}$, appelée **racine double**.
    - Si $\Delta > 0$, $f(x) = 0$ possède <span id="sol_sec_deg">deux solutions</span>, appelées **racines** de $f$, $x_1 = \dfrac{-b + \sqrt{\Delta}}{2a}$ et $x_2 = \dfrac{-b - \sqrt{\Delta}}{2a}$.

Remarque : il est possible d'ordonner les deux racines en fonction du signe de $a$. En effet, pour tout réel $b$ et pour tout réel strictement positif $\Delta$, $-b - \sqrt{\Delta} < -b + \sqrt{\Delta}$. Donc :

- si $a > 0$, $\dfrac{-b + \sqrt{\Delta}}{2a} >  \dfrac{-b - \sqrt{\Delta}}{2a}$;
- si $a < 0$, $\dfrac{-b + \sqrt{\Delta}}{2a} <  \dfrac{-b - \sqrt{\Delta}}{2a}$;