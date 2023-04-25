# Intégration par partie

!!! info " "
    Soient $u$ et $v$ deux fonctions dérivables sur un intervalle $I$ et dont les dérivées sont $u'$ et $v'$ sont continues sur $I$. Soient $a$ et $b$ deux réels de $I$.

    \[ 
        \displaystyle\int_a^b u(x) v'(x) \dx = \left[ u(x) v(x) \right]_a^b - \displaystyle\int_a^b u'(x) v(x) \dx
    \]
 

???- tip "En pratique"
    Après avoir écris une expression sous la forme d'un produit $A(x) \times B(x)$, il faut choisir le facteur qui jouera le rôle de $u$ et celui pour $v'$.

    <ul>
    <li> Si l'un des deux facteurs (par exemple $A(x)$) ne possède pas une primitive possédant une expression &laquo; simple &raquo;, alors $A(x)$ correspond à $u(x)$ et $B(x)$ à $v'(x)$. Cf [exple](#ipp01).</li>
    <li> Sinon, il faut choisir pour $u$ le facteur dont la dérivée est la plus simple. Cf [exple](#ipp02).</li>
    <li> Attention : parfois il faut faire apparaitre les produits ! Cf [exple](ipp03).</li>
    </ul>
 

???- example "Exemple"
    <span id="ipp01">En utilisant une intégration par partie</span>, calculer $I=\displaystyle\int_1^{\ex} x \ln(x) \dx$.
    
    ???- done "Réponse"
        Ici, $x \mapsto \ln x$ ne possède pas de primitive &laquo; simple &raquo;. Donc :
    
        \[ 
        \begin{array}{ccc}
        u(x) = \ln(x) & \text{ et } & v'(x)=x \\
        \text{ on dérive } & & \text{on &laquo; primitive &raquo;}\\
        u'(x) = \dfrac{1}{x} & & v(x) = \dfrac{x^2}{2}
        \end{array}
        \]

        D'où :
        
        \begin{eqnarray*}
        I &  = & \left[ \dfrac{x^2}{2} \ln(x) \right]_1^{\ex} - \displaystyle\int_1^{\ex} \dfrac{1}{x} \times \dfrac{x^2}{2} \dx\\
        & = & \left( \dfrac{\ex^2}{2}-0 \right) - \left[ \dfrac{x^2}{4} \right]_1^{\ex}\\
        & = & \dfrac{\ex^2}{2} -\left( \dfrac{\ex^2}{4} - \dfrac{1}{4} \right) \\
        & = & \dfrac{\ex^2}{4}+\dfrac{1}{4}
        \end{eqnarray*}
 
 

???- example "Exemple"
    <span id="ipp02">En utilisant une intégration par partie</span>, calculer $I=\displaystyle\int_0^{\ln 2} (x-1)\ex^x \dx$.

    ???- done "Réponse"
        Ici, les deux facteurs possèdent des primitives &laquo; simples &raquo;. Mais, la dérivée de $x \mapsto x-1$ est plus &laquo; simple &raquo; que celle de $x \mapsto \ex^x$. Donc : 

        \[ 
        \begin{array}{ccc}
        u(x) =x-1 & \text{ et } & v'(x)=\ex^x \\
        \text{ on dérive } & & \text{on &laquo; primitive &raquo;}\\
        u'(x) = 1 & & v(x) = \ex^x
        \end{array}
        \]

        D'où :

        \begin{eqnarray*}
        I &  = & \left[ (x-1)\ex^x \right]_0^{\ln 2} - \displaystyle\int_0^{\ln 2} 1 \times \ex^x \dx\\
        & = & \left( (\ln(2)-1)\times 2 - (-1) \right) - \left[ \ex^x \right]_0^{\ln 2}\\
        & = & 2\ln(2) -1 -\left( 2-1 \right) \\
        & = & 2\ln(2) -2
        \end{eqnarray*}
 
 

???- example "Exemple"
    <span id="ipp03">En utilisant une intégration par partie</span>, calculer $I=\displaystyle\int_1^{3} \ln x \dx$.

    ???- done "Réponse"
        Ici, il faut voir que $I=\displaystyle\int_1^{3} 1 \times \ln x \dx$.

        \[ 
        \begin{array}{ccc}
        u(x) =\ln(x) & \text{ et } & v'(x)=1 \\
        \text{ on dérive } & & \text{on &laquo; primitive &raquo;}\\
        u'(x) = \dfrac{1}{x} & & v(x) = x
        \end{array}
        \]

        D'où :

        \begin{eqnarray*}
        I &  = & \left[ x \times \ln(x) \right]_1^{3} - \displaystyle\int_1^{3} \dfrac{1}{x} \times x \dx\\
        & = & \left( 3\ln(3) - 0 \right) - \left[ x \right]_1^{3}\\
        & = & 3\ln(3) -\left( 3-1 \right) \\
        & = & 3\ln(3) -2
        \end{eqnarray*}
 
 

???- example "Exemple"
    On considère la suite $(I_n)$, définie pour tout entier naturel $n$, supérieur  ou égal à $1$, par : $I_n=\displaystyle\displaystyle\int_0^1 x^n \ex^{1-x} \dx$.
    
    <ol>
    <li> Montrer que $I_1=\ex^1-2$</li>
    <li> 
    <ol>
    <li> Montrer, à l'aide d'une intégration par parties que, pour tout entier naturel $n$ supérieur ou égal à $1$, on a :

    \[ 
    I_{n+1} =(n+1)I_n -1
    \]

    </li>
    <li> En déduire la valeur de $I_2$</li>
    </ol>
    </li>
    </ol>
 
