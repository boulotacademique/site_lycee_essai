# Limite d'une fonction lorsque $x$ tend vers un réel

???- example "Exemple"
    Soit $f$ la fonction définie sur $]-\infty,0[\cup]0,+\infty[$  par $f(x)=\dfrac{1}{x^2}$.

    Faire apparaître la table des valeurs de la fonction $f$ au voisinage de 0 ( depuis -0,04 jusqu'à 0,03 en prenant un pas de 0,001).
    
    Comment se comporte $f(x)$  lorsque $x$ devient proche de 0?

    ???- done "Réponse"
        $f$ semble avoir pour limite $+\infty$ en $0$ .
        Pour le démontrer , on se donne un réel  $A > 0$.
        
        $\dfrac{1}{x^2}>A\iff x^2 < \dfrac1A  \text{ avec } x\neq0 \iff -\dfrac{1}{\sqrt{A}}<x<\dfrac{1}{\sqrt{A}}$ avec $x\neq0$.
        
        Donc $]A,+\infty[$ contient toutes les valeurs de $f(x)$ pour $x$ assez proche de 0 et $\dlim{x}{0^0}\dfrac{1}{x^2}=+\infty$.

!!! info "Défintion"
    $f$ a pour limite $+\infty$ quand $x$ tend vers $a$ si $f(x)$ est aussi grand que l'on veut à condition de prendre $x$ assez proche de $a$ .

    C'est-à-dire si tout intervalle $]A,+\infty[$ (avec A réel) contient toutes les valeurs $f(x)$ pour $x$ assez proche de $a$.

    On note :$\dlim{x}{a} f(x)=+\infty$.
    
    **De façon formalisée} :**

    $\dlim{x}{a}f(x)=+\infty$ si et seulement si pour tout réel $A$ , on peut trouver un réel $\alpha >0$ tel que pour tout $x\neq a$ tel que $a-\alpha<x<a+\alpha$, on a $f(x)>A$.

!!! info "Définition"
    $f$ a pour limite $-\infty$ quand $x$ tend vers $a$ si $f(x)$ est négatif et aussi grand en valeur absolue que l'on veut à condition de prendre $x$ assez proche de $a$ .
    
    C'est-à-dire si tout intervalle $]-\infty;A[$ (avec A réel) contient toutes les valeurs $f(x)$ pour $x$ assez proche de $a$.
    
    On note :$\dlim{x}{a} f(x)=-\infty$.

    **De façon formalisée} :**

    $\dlim{x}{a}f(x)=-\infty$ si et seulement si pour tout réel $A$ , on peut trouver un réel $\alpha >0$ tel que pour tout $x\neq a$ tel que $a-\alpha<x<a+\alpha$, on a $f(x)<A$.

!!! info "Asymptote verticale"
    **Interprétation graphique de la limite en a**

    La droite d'équation $x=a$ est **asymptote verticale** à la courbe représentant $f$ en un réel $a$  si et seulement si $\dlim{x}{a}~f(x)~=~+~\infty$ ou $\dlim{x}{a} f(x)=-\infty$.

???- tip "Exemple"
    Si $x$ tend vers 0 avec $x>0$ , $\dfrac1x$ tend vers $+\infty$.
    
    On dit que la fonction inverse qui n'est pas définie en 0 a pour limite $+\infty$  **à droite en 0.**

    On note $\lim\limits_{\substack{x\to0\\x>0}}~\dfrac1x=+\infty$. On note aussi $\dlim{x}{0^+}{\dfrac{1}{x}} = +\infty$.

    [![Suite récurrente dans un plan](../Image/Cours_009.png){.Center_lien .Vignette}](../Image/Cours_009.png)

    Si $x$ tend vers 0 avec $x<0$ , $\dfrac1x $ tend vers $-\infty$.
    
    On dit que la fonction inverse qui n'est pas définie en 0  a pour limite $-\infty$  **à gauche en 0.**
    
    On note $ \lim\limits_{\substack{x\to0\\x<0}}~\dfrac1x=-\infty$. On note aussi $\dlim{x}{0^-}{\dfrac{1}{x}} = +\infty$.

    Comme ces limites sont distinctes , la fonction inverse n'a pas de limite en 0.
