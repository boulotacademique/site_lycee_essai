# Limites et comparaison

## Théorème semblable à ceux des suites !

!!! abstract "Théorème de comparaison"
    Si $f$ et $g$ sont deux fonctions telles que pour $x$ assez grand  , $f(x) \leq g(x)$

    - Si $\dlim{x}{+\infty}f(x)=+\infty$ alors $\dlim{x}{+\infty}g(x) =+\infty$
    - Si $\dlim{x}{+\infty}g(x)=-\infty$ alors $\dlim{x}{+\infty}f(x) =-\infty$

!!! abstract "Théorème d'encadrement"
    Soit $f ,g, h$ trois fonctions telles que :
    
    $\Lim{\text {Si pour } x \text{ assez grand } f(x) \leq g(x) \leq h(x) }{\text {si} \quad \lim\limits_{x\to +\infty} f(x) =\ell \text{ et si } \quad \lim\limits_{x\to +\infty} h(x) =\ell } \quad \text{ alors } \quad\lim\limits_{x \to +\infty} g(x)=\ell$.

    [![Th d'encadrement](../Image/Cours_010.png){.Center_lien .VignetteMed}](../Image/Cours_010.png)

???- example "Exemple"
    Etudier la limite en $+\infty$ de la fonction $f$ définie sur $]0,+\infty[$ par $f(x)=\dfrac{\sin x}{x}$

    ???- done "Solution"
        Pour tout réel $x$ $-1 \leq \sin x  \leq 1$ donc pour tout $x>0$ , $\dfrac{-1}{x} \leq  f(x) \leq  \dfrac1x$.
        
        Or $\dlim{x}{+\infty} \dfrac{-1}{x}=0$ et $\dlim{x}{+\infty} \dfrac{1}{x}=0$ donc $\dlim{x}{+\infty}\dfrac{\sin x}{x}=0$.

## Théorème avec l'exponentielle

On rappelle que :

!!! abstract "Théorème"

    - $\dlim{x}{+\infty} \ex^x=+\infty$
    - $\dlim{x}{-\infty} \ex^x=0$

    ???- abstract "Démonstration au programme"
        Idée : <span id="lim_exp">démontrer que</span> pour tout réel $x \geq 0$ , on a $e^x>x$ et  en déduire $\dlim{x}{+\infty}e^x=+\infty$

        ???- done "Solution"
            - Soit $g$ la fonction définie pour $x \geq 0$ par $g(x)=\mathrm{e}^x-x$.

            g est dérivable comme différence de fonctions dérivables; pour tout $x$ de $[0~;~+\infty[$, $g'(x)=\ex^x-1$ .
        
            Pour $x\geq 0$, on a $\ex^x\geq 1$, donc $g'(x)\geq 0$ et g est croissante sur $[0~;~+\infty[$ ;
            
            pour $x\geq 0$, on a $g(x)\geq  g(0)$ or  g$(0)=1$ donc,pour tout $x\geq 0$, $g(x)\geq 1$ et donc $g(x)>0$ .
            Ainsi pour tout $x \geq 0$  $e^x> x$

            Or $\dlim{x}{+\infty} x=+\infty$ donc par comparaison, on a  $\dlim{x} {+\infty}\ex^x=+\infty$.

            - Pour tout réel $x$,  $\ex^x=\frac{1}{\ex^{-x}}$ et on pose $X=-x$.
            
            $\Lim{\lim\limits_{x \to -\infty}~(-x)&=&+\infty}{\lim\limits_{X\to +\infty}~ \ex^X&=&+\infty} \text{donc par composition}  \lim\limits_{x \to -\infty}~\ex^{-x}=+\infty$.
            
            Ainsi $\dlim{x}{-\infty} \ex^x = \dlim{x}{-\infty} \frac{1}{e^{-x}}=0$

!!! abstract "Théorème - Croissance comparée"
    
    - <span id="exp_crois_comp">Pour tout</span> $n\in \N$, $\dlim{x}{+\infty}\dfrac{\ex^x}{x^n}=+\infty$
    - Pour tout $n\in \N$, $\dlim{x}{-\infty} x^n \ex^x=0$

    ???- abstract "Démonstration"
        1. Pour $n=0$, voir la [démonstration précédente](#lim_exp)
        2. Pour $n=1$. On considère la fonction $f$ définie sur $\R$ par 

            \[
            f(x) = \ex^x - \frac{x^2}{2}
            \]

            1. Après avoir calculé $f'$ et $f''$, déterminer le sens de variations de $f$ sur $\R$.
            2. En déduire que, pour tout $x>0$, $\frac{\ex^x}{x} > \frac{x}{2}$.
            3. En déduire que $\lim_{x \to +\infty} \frac{\ex^x}{x} = +\infty$
        
        3. Pour $n>1$ :
            1. Montrer que pour tout $n\in \N^*$ et pour tout $x>0$ :

                \[
                    \frac{\ex^x}{x^n} = \left( \frac{\ex^{\frac{x}{n}}}{\frac{x}{n}} \right)^n \times \left( \frac{1}{n} \right)^n
                \]

            2. En utilisant la limite de composées, déduire de la question précédente que $\lim\limits_{x \to +\infty} \frac{\ex^x}{x^n} = +\infty$.

        ???- done "Solution"
            
            1. Fait
            2. 
                1. $f'(x)=\ex^x-x$ et $f''(x)=\ex^x-1$.

                \begin{eqnarray*}
                \ex^x-1 >0 & \Longleftrightarrow & \ex^x >1 \\
                & \equivaut & \ex^x >\ex^0 \\
                & \equivaut & x >0
                \end{eqnarray*}

                [![Th d'encadrement](../Image/Cours_015.png){.Center_lien .VignetteMed}](../Image/Cours_015.png)

                Le minimum de $f'$ sur $\R$ est $1$, donc $f'$ est positive sur $\R$. Donc $f$ est croissante sur $\R$.

                2. Si $x>0$ et comme $f$ est croissante sur $\R$, $f(x)>f(0)$. Or $f(0)=1>0$, donc $f(x)>0$ si $x>0$.
                
                    Donc $\ex^x-\frac{x^2}{2}>0$ si $x>0$. D'où $\frac{\ex^x}{x}>\frac{x}{2}$, si $x>0$.

                3. Comme $\frac{\ex^x}{x}>\frac{x}{2}$ si $x>0$ et que $\lim_{x \to +\infty} \frac{x}{2} =+\infty$, donc par comparaison $\lim\limits_{x \to +\infty} \frac{\ex^x}{x} = +\infty$.

            3. 
                1. Soit $n\in \N^*$ et $x>0$ :

                    \begin{eqnarray*}
                    \frac{\ex^x}{x^n} & = & \frac{\left(\ex^{\frac{x}{n}}\right)^n}{x^n \times \left(\frac{n}{n} \right)^n} \\
                    & = & \frac{(\ex^{\frac{x}{n}})^n}{\left(\frac{x}{n} \right)^n} \times \left( \frac{1}{n} \right)^n \\
                    & = &  \left( \frac{\ex^{\frac{x}{n}}}{\frac{x}{n}} \right)^n \times \left( \frac{1}{n} \right)^n
                    \end{eqnarray*}

                2. Soit $n\in \N^*$ et $x>0$ :
                
                    \[
                    \left.
                    \begin{array}{l}
                    \lim\limits_{x \to +\infty} \frac{x}{n} = +\infty\\
                    \lim\limits_{X \to +\infty} \frac{\ex^X}{X} = +\infty \quad \text{cf 2.}
                    \end{array}
                    \right\} \text{ par composée } \lim\limits_{x \to + \infty} \frac{\ex^{\frac{x}{n}}}{\frac{x}{n}} = +\infty
                    \]

                    Donc $\lim\limits_{x \to + \infty} \left(\dfrac{\ex^{\frac{x}{n}}}{\frac{x}{n}}\right)^n \times \left( \dfrac{1}{n} \right)^n=+\infty$.
        
    ???- abstract "Démonstration"

        4. En posant $X=-x$, montrer que $\lim\limits_{x \to -\infty} x^n \ex^x = \lim\limits_{X \to +\infty} \dfrac{(-X)^n}{\ex^X}$.
        5. Quelle est la limite de $\dfrac{\ex^X}{X^n}$ lorsque $X$ tend vers $+\infty$ ?
        6. En déduire $\lim\limits_{X \to +\infty} \dfrac{X^n}{\ex^X}$
        7. En déduire $\lim\limits_{X \to +\infty} \dfrac{(-X)^n}{\ex^X}$
        8. Conclure.

        ???- done "Solution"
            A FAIRE

!!! abstract "Théorème - Limite et taux d'accroissement"
    
    - $\dlim{x}{0} \dfrac{e^x-1}{x}=1$
    - $\dlim{x}{0} \dfrac{\sin(x)}{x}=1$

???- example "Exemple"
    $\dlim{x}{0} \dfrac{e^{3x}-1}{x}$ ?

    ???- done "Solution"
        On  pose  $X=3x$.

        $\dfrac{e^{3x}-1}{x}= \dfrac{e^{X}-1}{\dfrac{X}{3}}= 3 \dfrac{e^{X}-1}{X}$.

        On utilise le théorème sur la limite d'une fonction composée.
        
        $\Lim{\dlim{x}{0}3x=0}{\dlim{X}{0}\dfrac{e^X-1}{X}=1\quad \text{ (limite du cours)} }$  donc par composition $\dlim{x}{0}\dfrac{e^{3x}-1}{3x}=1$ et par  produit $\dlim{x}{0} f(x)=3$.
