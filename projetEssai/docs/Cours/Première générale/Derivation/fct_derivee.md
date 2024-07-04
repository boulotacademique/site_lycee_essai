# Dérivation<br>Fonctions dérivées

!!! note "Définition"
    $f$ est une fonction dont l'ensemble de définition est $\mathcal{D}_f$ et $D$ désigne un intervalle ou  une réunion d'intervalles inclus dans $\mathcal{D}_f$. On dit que $f$ est dérivable sur $D$ si elle est dérivable en tout point de $D$. Alors la fonction qui à tout $x$ de $D$ associe $f '(x)$, le nombre dérivé de $f$ en $x$, est appelée la fonction dérivée de $f$ sur $D$. On la note $f'$.


## Dérivée de fonctions usuelles.

!!! abstract "Théorème - Fonctions constantes"
    $f$ est la fonction définie sur $\R$ par $f(x) = k$ ($k$ un réel).
    
    $f$ est dérivable sur $\R$ et pour tout réel $x$, $f'(x) = 0$.


???- abstract "Démonstration"
    $f(a + h)-f(a) = 0$ pour tout $a$, donc $f'(a) = 0$ pour tout $a$.


!!! abstract "Théorème - Fonction linéaire"
    $f$ est la fonction définie sur $\R$ par $f(x) = kx$, où $k$ est un réel, $k \neq 0$.
    
    $f$ est dérivable sur $\R$ et pour tout réel $x$, $f '(x) = k$.

???- abstract "Démonstration"
    Pour tout réel $a$, $f(a+h)-f(a) = kh$, donc $\frac{f(a+h) - f(a)}{h}= k$, donc pour tout réel $a$, $f '(a) = k$.

!!! abstract "Théorème - Fonctions puissances"
    $f$ est la fonction définie sur $\R$ par $f(x) = x^n$ avec $n$ un entier naturel $n \geq 2$.
    
    $f$ est dérivable sur $\R$ et pour tout réel $x$, 
    
    \[f '(x) = n \times x^{n-1} \]


???- abstract "Démonstration"
    Uniquement pour le cas particulier $n=2$ : $f(x)=x^2$
    
    Pour tout $a$ réel, 

    \[ \begin{eqnarray*}
    \frac{f(a+h) - f(a)}{h} & = & \frac{(a+h)^2-a^2}{h} \\
    & = & \frac{2ah + h^2}{h} \\
    & = & 2a + h \qquad h \neq 0
    \end{eqnarray*} \]

    Or $\lim_{h \rightarrow 0}{2a+h}=2a$, donc pour tout $a$ réel $f'(a) = 2a$. Et avec la variable plus usuelle $x$, $f'(x) = 2x$.

???- info "Remarque"
    $f(x) = x^n$, avec $n \in \N$. Soit $a \in \R$ :

    La formule du binôme de Newton donne 
    
    \[ (a + h)^n = \sum_{k = 0}^n \begin{pmatrix} n \\ k \end{pmatrix} h^k a^{n-k} \]

    \[ \begin{eqnarray*}
    f(a+h) - f(a) & = & \sum_{k = 0}^n \begin{pmatrix} n\\ k \end{pmatrix} h^k a^{n-k} - a^n\\
    & = & \sum_{k = 1}^n \begin{pmatrix} n\\ k \end{pmatrix} h^k a^{n-k} \\
    & = & \begin{pmatrix} n\\ 1 \end{pmatrix} h a^{n-1} + \sum_{k = 2}^n \begin{pmatrix} n\\ k \end{pmatrix} h^k a^{n-k} \\
    & = & n h a^{n-1} + h^2 \sum_{k = 2}^n \begin{pmatrix} n\\ k \end{pmatrix} h^{k-2} a^{n-k} \\
    \text{Donc } & &\\
    \dfrac{f(a+h) - f(a)}{h} & = & na^{n-1} + h \sum_{k = 2}^n \begin{pmatrix} n\\ k \end{pmatrix} h^{k-2} a^{n-k} \\
    \text{Or} & & \lim_{h \to 0} h \sum_{k = 2}^n \begin{pmatrix} n\\ k \end{pmatrix} h^{k-2} a^{n-k}  = 0\\
    \text{Donc } & & \\
    \lim_{h \to 0} \dfrac{f(a+h) - f(a)}{h} & = & na^{n-1}
    \end{eqnarray*} \]

!!! abstract "Théorème - Fonction inverse"
    $f$ est la fonction définie sur $\R-\{0\}$ par $f(x) = \frac{k}{x}$ avec $k$ un réel non nul.

    $f$ est dérivable sur $\R-\{0\}$ et pour tout réel non nul $x$, 
    
    \[ f '(x) = -\frac{k}{x^2} \]

???- abstract "Démonstration"
    
    \[ f(x)=\frac{k}{x} \]

    Pour tout $a$ réel non nul
    
    \[ \begin{eqnarray*}
    \frac{f(a+h) - f(a)}{h} & = & \frac{\dfrac{k}{a+h}-\dfrac{k}{a}}{h} \\
    & = & \frac{\dfrac{k \times a-k \times (a+h)}{a(a+h)}}{h} \\
    & = & \frac{-k}{a(a+h)} \qquad h \neq 0
    \end{eqnarray*} \]

    Or $\lim_{h \rightarrow 0}{\frac{-k}{a(a+h)}}=\frac{-k}{a^2}$, donc pour tout $a$ réel non nul $f'(a) = \frac{-k}{a^2}$. Et avec la variable plus usuelle $x$, $f'(x) = \frac{-k}{x^2}$.


!!! abstract "Théorème - Fonction racine carrée"
    $f$ est la fonction définie sur $[0;+\infty[$ par $f(x) = \sqrt{x}$ .
    
    $f$ est dérivable sur $]0;+\infty[$ (remarquez la différence avec le domaine de définition de $f$) et pour tout réel strictement positif $x$, 
    
    \[f '(x) = \frac{1}{2 \sqrt{x}} \]

???- abstract "Démonstration"
    **Technique de calcul à connaître**

    \[ \begin{eqnarray*}
    \sqrt{\alpha} + \sqrt{\beta} & = & \frac{\left( \sqrt{\alpha} + \sqrt{\beta} \right) \times \left( \sqrt{\alpha} - \sqrt{\beta} \right)}{\sqrt{\alpha} - \sqrt{\beta}} \\
    & = & \frac{\alpha^2 - \beta^2}{\sqrt{\alpha} - \sqrt{\beta}}\\
    & & \\
    \sqrt{\alpha} - \sqrt{\beta} & = & \frac{\left( \sqrt{\alpha} - \sqrt{\beta} \right) \left( \sqrt{\alpha} + \sqrt{\beta} \right)}{\sqrt{\alpha} + \sqrt{\beta}} \\
    & = & \frac{\alpha^2 - \beta^2}{\sqrt{\alpha} + \sqrt{\beta}}\\
    \end{eqnarray*} \]

    $f(x)=\sqrt{x}$. Pour tout $a$ réel strictement positif, 
    
    \[ \begin{eqnarray*}
    \frac{f(a+h) - f(a)}{h} & = & \frac{\sqrt{a+h}-\sqrt{a}}{h} \\
    & = & \frac{(a+h)-a}{h \times \left(\sqrt{a+h}+\sqrt{a} \right)} \\
    & = & \frac{h}{h \times \left(\sqrt{a+h}+\sqrt{a}  \right)}\\
    & = & \frac{1}{\sqrt{a+h}+\sqrt{a}}  \qquad h \neq 0 
    \end{eqnarray*} \]
    
    Or $\lim_{h \rightarrow 0}{\frac{1}{\sqrt{a+h}+\sqrt{a}}}=\frac{1}{2 \sqrt{a}}$ (à condition que $a \neq 0$) , donc pour tout $a$ réel non nul $f'(a) = \frac{1}{2\sqrt{a}}$. Et avec la variable plus usuelle $x$, $f'(x) = \frac{1}{2\sqrt{x}}$.

## Dérivée d'opérations de fonctions.

$u$ et $v$ sont des fonctions dérivables sur $I$ et $J$.

!!! abstract "Théorème - Dérivée de  $k u$"
    Si $u$ est une fonction dérivable sur $I$, alors $k u$ est dérivable sur $I$ et 
    
    \[ \left( k u\right)' = k \times u'\]

???- abstract "Démonstration"
    Pour tout $a$ de $I$ : 
    
    \[ \begin{eqnarray*}
    \frac{\left(ku\right)(a+h) - \left(ku\right)(a)}{h} & = & k\frac{u(a+h)-u(a)}{h} \\
    \end{eqnarray*} \]

    Or $\lim_{h \rightarrow 0}{\frac{u(a+h)-u(a)}{h}} = u'(a)$, donc $\lim_{h \rightarrow 0}{k \frac{u(a+h)-u(a)}{h}} = k u'(a) = \left(k u' \right)(a)$ 


!!! abstract "Théorème - Dérivée de $u + v$"
    Si $u$ et $v$ sont deux fonctions dérivables sur $I$, alors $u+v$ est dérivable sur $I$ et 
    
    \[ \left(u+v\right)' =  u' + v'\]

???- abstract "Démonstration"
    
    \[ \begin{eqnarray*}
    \frac{\left(u+v\right)(a+h) - \left(u+v\right)(a)}{h} & = & \frac{u(a+h)-u(a)}{h}+\frac{v(a+h)-v(a)}{h} \\
    \end{eqnarray*} \]

    Or $\lim_{h \rightarrow 0}{\frac{u(a+h)-u(a)}{h}} = u'(a)$ et $\lim_{h \rightarrow 0}{\frac{v(a+h)-v(a)}{h}} = v'(a)$, donc 

    $\lim_{h \rightarrow 0}{\frac{u(a+h)-u(a)}{h}+\frac{v(a+h)-v(a)}{h}} = u'(a) + v'(a)= \left( u' + v' \right)(a)$ 

!!! abstract "Théorème - Dérivée  de $u \times v$"
    <span id="der_prod">Si $u$ et $v$ sont deux fonctions dérivables sur $I$</span>, alors $uv$ est dérivable sur $I$ et 
    
    \[ \left(uv\right)' =  u'\times v + u \times v' \]

???- abstract "Démonstration"

    \[ \begin{eqnarray*}
    \frac{\left(uv\right)(a+h) - \left(uv\right)(a)}{h} & = & \frac{u(a+h)v(a+h)-u(a)v(a)}{h} \\
    & = & \frac{u(a+h)v(a+h)-u(a)v(a+h)+u(a)v(a+h) -u(a)v(a)}{h}\\
    & = & \frac{u(a+h)v(a+h)-u(a)v(a+h)}{h}+\frac{u(a)v(a+h) -u(a)v(a)}{h}\\
    & = & \frac{u(a+h)-u(a)}{h}v(a+h)+\frac{v(a+h) -v(a)}{h}u(a)\\
    \end{eqnarray*} \]

    Or $\lim_{h \rightarrow 0}{\frac{u(a+h)-u(a)}{h}} = u'(a)$ et $\lim_{h \rightarrow 0}{v(a+h)}=v(a)$, donc $\lim_{h \rightarrow 0}{\frac{u(a+h)-u(a)}{h}v(a+h)}=u'(a) \times v(a) = \left( u'v\right)(a)$.

    De plus $\lim_{h \rightarrow 0}{\frac{v(a+h)-v(a)}{h}} = v'(a)$ et $\lim_{h \rightarrow 0}{u(a)}=u(a)$, donc $\lim_{h \rightarrow 0}{\frac{v(a+h)-v(a)}{h}u(a)}=v'(a) \times u(a) = \left( uv'\right)(a)$.
    
    D'où $\lim_{h \rightarrow 0}{\frac{\left(uv\right)(a+h) - \left(uv\right)(a)}{h}} = \left( u'v\right)(a) +  \left( uv'\right)(a) = \left( u'v+v'u\right)(a)$


!!! abstract "Corollaire - Cas particulier dérivée de $u^2$"
    Si $u$ est une fonction dérivable sur $I$, alors $u^2$ est dérivable sur $I$ et 
    
    \[ \left(u^2\right)' =  2\times u'\times u\]

???- abstract "Démonstration"
    Appliquer le théorème (pour un produit)[#der_prod] avec $v=u$.

!!! abstract "Théorème - Dérivée de $\frac{k}{v}$"
    Si $v$ est une fonction dérivable sur $I$ où pour tout $x$ de $I$ $v(x) \neq 0$, alors $\frac{k}{v}$ est dérivable sur $I$ et :
    
    \[ \left( \frac{k}{v}\right)' = - \frac{k \times v'}{v^2} \]

???- abstract "Démonstration"

    - **Si $k=1$ :**

    \[ \begin{eqnarray*}
    \frac{\left( \dfrac{1}{v}\right)(a+h)-\left( \dfrac{1}{v}\right)(a)}{h} & = & \frac{ \dfrac{1}{v(a+h)}- \dfrac{1}{v(a)}}{h} \\
    & = & \frac{ \quad\dfrac{v(a)}{v(a+h)v(a)}- \dfrac{v(a+h)}{v(a)v(a+h)} \quad}{h} \\
    & = & \frac{ \quad \dfrac{v(a)- v(a+h)}{v(a) \times v(a+h)}\quad }{h} \\
    & = & \frac{ v(a)- v(a+h)}{h \times v(a) \times v(a+h)}\\
    & = & \frac{ v(a)- v(a+h)}{h} \times \frac{1}{v(a) \times v(a+h)} \\
    \end{eqnarray*} \]

    Or $\lim_{h \rightarrow 0}{\frac{ v(a)- v(a+h)}{h}} = - v'(a)$ et $\lim_{h \rightarrow 0}{\frac{1}{v(a) \times v(a+h)}} = \frac{1}{v(a) \times v(a)} = \frac{1}{\left(v(a)\right)^2}$,

    d'où $\lim_{h \rightarrow 0}{\frac{ v(a)- v(a+h)}{h} \times \frac{1}{v(a) \times v(a+h)}} = - v'(a) \times \frac{1}{\left(v(a)\right)^2} = - \frac{v'(a)}{\left(v(a)\right)^2} = \left( \frac{- v'}{v^2} \right)(a)$.

    - **$k$ est un réel quelconque.**
    
    $\frac{k}{v} = k \times \frac{1}{v}$ donc avec le théorème \Rf{DerProdScal}, $\left( \frac{k}{v} \right)' = k \times \frac{-v'}{v^2} = -\frac{k \times v'}{v^2}$.

!!! abstract "Théorème - Dérivée de $\frac{u}{v}$"
    Si $u$ et $v$ sont deux fonctions dérivables sur $I$ tels que pour tout $x$ de $I$ $v(x) \neq 0$, alors $\frac{u}{v}$ est dérivable sur $I$ et 

    \[ \left(\frac{u}{v}\right)' =  \frac{u'\times v -  v'\times u}{v^2} \]

    !!! warning "Attention"
        Faites très attention à l'ordre ($\mathbf{u'} \times v \mathbf{-} \mathbf{v'} \times u$ et non $\mathbf{v'} \times u \mathbf{-} \mathbf{u'} \times v$)dans cette formule !!

???- abstract "Démonstration"
    On pose $f=u$ et $g=\frac{1}{v}$. Alors $\frac{u}{v} = f\times g$. D'après le théorème \Rf{DerProd}, $\left( fg \right)' = f'g + fg'$. Comme $f' =u'$ et $g'=-\frac{v'}{v^2}$ :

    \[ \begin{eqnarray*}
    \left(\frac{u}{v}\right)' & = & u' \times \frac{1}{v} + u \times \left( -\frac{v'}{v^2}\right) \\
    & = & \frac{u' \times v - u \times v'}{v^2} 
    \end{eqnarray*} \]

## Dérivée et composition.

Dérivée de $f(ax +b)$.

A FAIRE

## Bilan

\[
\begin{array}{|c|c|c|c|}
\hline
 & & &\\
\text{Fonction $f$ définie sur} & \text{Par :}& \text{a pour fonction dérivée}&\text{la fonction est dérivable sur}\\
 & & &\\
\hline
 & & &\\
\R & f(x) = k \ \text{(cste)} & f'(x) = 0 & \R \\
 & & &\\
\hline
 & & &\\
\R & f(x) = x & f'(x) = 1 & \R \\
 & & &\\
\hline
 & & &\\
\R & f(x) = mx+p & f'(x) = m & \R \\
 & & &\\
\hline
 & & &\\
\R & f(x) = x^2 & f'(x) = 2x & \R \\
 & & &\\
\hline
 & & &\\
\R & f(x) = x^n \quad n \in \mathbb{N},\ n>0 & f'(x) = nx^{n-1} & \R \\
 & & &\\
\hline
 & & &\\
]-\infty;0[ \cup ]0;+\infty[ & f(x) = \frac{1}{x} & f'(x) = -\frac{1}{x^2} & ]-\infty;0[ \cup ]0;+\infty[\\
 & & &\\
\hline
 & & &\\
]-\infty;0[ \cup ]0;+\infty[ & f(x) = \frac{1}{x^n} \ n \in \mathbb{N},\ n \neq 0 & f'(x) = -\frac{n}{x^{n+1}} & ]-\infty;0[ \cup ]0;+\infty[\\
 & & &\\
\hline
 & & &\\
\left[0;+\infty \right[ & f(x) = \sqrt{x} & f'(x) = \frac{1}{2 \sqrt{x}} & ]0;+\infty[\\
 & & &\\
\hline
 & & &\\
\R & f(x) = \cos{x} & f'(x) = -\sin{x} & \R\\
 & & &\\
\hline
 & & &\\
\R & f(x) = \sin{x} & f'(x) = \cos{x} & \R\\
 & & &\\
\hline
\\
\hline
 & & &\\
 & ku & k u' & \\
  & & &\\
\hline
 & & &\\
 & u+v & u'+v' & \\
  & & &\\
\hline
 & & &\\
 & uv & u' \times v + v' \times u & \\
  & & &\\
 \hline
  & & &\\
 & u^2 & 2u' \times u & \\
  & & &\\
\hline
 & & &\\
 & \dfrac{k}{v} & -\dfrac{k \times v'}{v^2} & \\
  & & &\\
\hline
 & & &\\
 & \dfrac{u}{v} & \dfrac{u' \times v - v' \times u}
{v^2} & \\
 & & &\\
 \hline
\end{array} \]

