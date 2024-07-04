# Théorèmes de comparaison

## Limite infinie et comparaison

!!! info "Comparaison et limites infinies"

    Soit $(u_n)$ et $(v_n)$ sont deux suites telles que :
    
    - si $u_n  \leq v_n$  à partir d'un certain rang 
    - si $\lim\limits_{n\to +\infty}~u_n = +\infty$

    alors $\lim\limits_{n \to +\infty}~v_n=+\infty$.

    ???- abstract "Démonstration"

        Soit $A$ un nombre réel.

        - $\dlim{n}{+\infty}u_n=+\infty$ alors il existe un entier $n_1$ tel que $\forall n \geq n_1 ,  u_n>A$
        - Comme $u_n <v_n$ à partir d'un certain rang , il existe un rang $n_0$ tel que $\forall n \geq n_0 , u_n  \leq v_n$

        Si $N$ désigne le plus grand des deux nombres $n_0$ et $n_1$ alors $\forall n \geq N, v_n \geq u_n>A$

        Ceci signifie que tout intervalle $]A,+\infty[$ contient tous les $u_n$ à partir d'un certain rang. 
        
        Ainsi $\dlim{n}{+\infty} v_n=+\infty$.

???- example "Exemple"

    Etudier la convergence de la suite définie par $v_n=n^2+(-1)^n$

    ???- done "Réponse"

        $(-1)^n$ vaut -1 ou 1 donc $(-1)^n \geq -1$ et $n^2+(-1)^n \geq n^2-1$ donc $v_n \geq  n^2-1$  .
        
        Or $\dlim{n}{+\infty }(n^2-1)=+\infty$ donc $\dlim{n}{+\infty}v_n=+\infty$

## Limite finie et comparaison

???- info "Un théorème important ... pour plus tard"

    Une suite convergente est bornée.

!!! info "Thèorème d'encadrement"
    Soit $(u_n)$ ,$(v_n)$ et $(w_n)$ sont 3 suites telles que :
    
    - Si $u_n \leq v_n \leq w_n$ à partir d'un certain rang 
    - Si $\lim\limits_{n\to +\infty}~u_n=\ell$ et $\lim\limits_{n\to +\infty}~w_n=\ell$
    
    alors $\lim\limits_{n \to +\infty}~v_n=\ell$.

    [![Th d'encadrement](../Image/Cours_004.png){.Center_lien .Vignette}](../Image/Cours_004.png)
    

???- example "Exemple"

    Etudier la convergence de la suite $(v_n)$ définie par $v_n=1+\dfrac{\sin n}{n}$  pour $n \geq 1$.

    ???- done "Réponse"

        La fonction  sinus n'a pas de limite , on est donc obligé d'utiliser un théorème d'encadrement .
    
        On a $-1 \leq  \sin n  \leq  1$  donc  en multipliant par $\dfrac1n$ strictement positif , on a : $-\dfrac1n \leq  \dfrac{\sin n}{n}  \leq  \dfrac1n$ .
        
        Donc 
        
        $\forall ~ n \geq 1$ ,  $1-\dfrac1n  \leq  v_n  \leq  1+\dfrac1n$ .
        
        Or $\dlim{n}{+\infty} 1-\dfrac1n=1$ et $\dlim{n}{+\infty} 1+\dfrac1n =1$ donc d'après le théorème d'encadrement $\dlim{n}{+\infty} v_n= 1$.

???- example "Exemple"

    Etudier la convergence de la suite $(u_n)$ définie par $u_n=2-\dfrac{(-1)^n}{n}$  pour $n \geq 1$.

## Thèorème de convergence des suites monotones

!!! info "Suites monotones **et** convergentes"

    - <span id="mono_conv">Si une suite</span> est croissante **et a pour limite** $\mathbf{\ell}$ (c'est donc une suite convergente !) alors tous les termes de la suite sont inférieurs ou égaux à $\ell$ c'est-à-dire, pour tout entier naturel $n$ , $u_n \leq  \ell$ .
    - Si une suite est décroissante **et a pour limite** $\mathbf{\ell}$ (c'est donc une suite convergente !) alors tous les termes de la suite sont supérieurs  ou égaux à $\ell$ c'est-à-dire, pour tout entier naturel $n$ , $u_n \geq \ell$.

    ???- warning "Attention"

        Pour utiliser ces théorèmes, il faut d'abord s'assurer de la convergence de la suite.



!!! info "Théorème de convergence des suites monotones"

    - Si une suite est croissante et majorée par $M$ alors elle converge vers $\ell$ et $\ell \leq M$ (attention , on connait pas la limite).
    - Si une  suite est décroissante et minorée par $m$ alors elle converge vers $\ell$ et $\ell \geq m$.

    ???- warning "ATTENTION"
        Le majorant (ou le minorant) du théorème **ne permet pas** de déterminer la valeur de la limite. 

        Les exemples (purement scolaires) les plus rencontrés utilisent souvent la limite comme majorant ou minorant. 

        Mais ce n'est pas une raison pour utiliser le théorème précédent et conclure sur la valeur de la limite !

!!! abstract "Conséquence"

    - Une suite croissante non majorée a pour limite $+\infty$.
    - Une suite décroissante et non minorée a pour limite $-\infty$.

    ???- abstract "Démonstration"

        Une suite $(u_n)$ est majorée lorsqu'il existe un réel  $M$ tel que   pour tout  $n\in \N , u_n  \leq  M$.
        
        ???+ tip "Méthode"
            Le contraire de   **il existe** est **pour tout** et le contraire de  **pour tout** est **il existe**.

        Ainsi une suite $(u_n)$ n'est pas majorée lorsque pour tout  réel  $M$ , il existe   $p\in \N , u_p > M$.
        
        $(u_n)$ est croissante , pour tout $n \geq p$ , on a $u_n \geq u_p$ et donc $u_n>M$.
        
        Donc tous les termes de la suite sont dans l'intervalle $]M,+\infty[$ à partir du rang $p$ c'est-à-dire $\dlim{n}{+\infty}u_n=+\infty$.


???- example "Exemple"

    On considère la suite $(u_n)$ définie par $\Syst{u_0 & = &1,8}{u_{n+1} & = & f(u_n)}$ avec $f(x) =\dfrac{2}{3-x}$.

    On a vu que la suite $(u_n)$ est décroissante et que pour tout $n\in \N$, $u_n\in [1,2]$ (cf <a href="../../Suites_et_recurrence/Suites_bases/07_majoree_minoree_bornee.html#ex2_16">Exple 2.16</a>)

    1. Montrer que la suite $(u_n)$ converge et justifier que sa limite appartient à $[1;1,8]$.
    2. Conjecturer graphiquement sa limite .Puis déterminer la limite par le calcul.

    ???- done "Réponse"

        1. La suite est décroissante et minorée par 1 donc elle converge vers $\ell$ d'après le théorème de convergence des suites monotones. De plus, $\ell>1$.

            Par ailleurs, comme $(u_n)$ est une suite cdécroissante et convergente, pour tout $n\in\N$, $u_n \geq \ell$ (cf [ce th](#mono_conv)).

            De plus  la suite $(u_n)$ est décroissante donc $u_n \leq u_0$  donc pour tout $n\in\N$ on a $1< \ell \leq u_n  \leq u_0$. D'où $1 \leq \ell \leq  1,8$.
  
        2. $u_{n+1}=\dfrac{2}{u_n-3}$ par opérations sur les limites : 
       
            $\dlim{n}{+\infty} u_{n+1}=\dlim{n}{+\infty} \dfrac{2}{3-u_n}=\dfrac{2}{3-\lim\limits_{n \to +\infty}u_n}=\dfrac{2}{3-\ell}$ (possible car $3-\ell \neq 0$ puisque $1 \leq \ell \leq  1,8$)

            Or  $\dlim{n}{+\infty} u_{n+1}=\ell$ donc

            $u_{n+1}$ tend à la fois vers $\ell$ et vers $\dfrac{2}{3-\ell}$ donc par  unicité de la limite on a : $\ell= \dfrac{2}{3-\ell}$ soit $\ell^2-3\ell+2=0$ d'où $\ell=1$ ou $\ell=2$. 
        
            Comme $1 \leq \ell \leq  1,8$ alors $\ell=1$.

## Une démonstration classique (et au programme)

!!! info "Théorème"

    $q$ désigne un nombre réel.

    - Si $q>1$ alors $\dlim{n}{+\infty} q^n=+\infty$  
    - Si $q=1$ alors $\dlim{n}{+\infty} q^n=1$
    - Si $-1<q<1$ alors $\dlim{n}{+\infty} q^n=0$

    ???- abstract "Démonstration"

        _Préliminaire_
        
        Démontrez par récurrence que pour tout $n \geq 0$ ,  et $a>0$ , $(1+a)^n  \geq  1+na$. (Cette inégalité a été démontrée en 1689 par Jacques  Bernoulli).
        
        ???- done "Réponse"
        
            Soit  $P(n)$ la propriété définie par : &laquo; $(1+a)^n  \geq  1+na$ &raquo;.

            - **Initialisation** : pour $n=0$  on a  $(1+a)^0=1$ car $1+a\neq 0$ or $1+0a=1$ , donc $(1+a)^0  \geq  1+0a$  et  ainsi $P(0)$ est   vraie.
            - **Hérédité** : on suppose que pour un entier $k \geq 0$ $P(k)$ est vraie  , c'est-à-dire $(1+a)^k  \geq  1+ka$ et on veut démontrer que $P(k+1)$ est vraie , c'est-à-dire : $(1+a)^{k+1}  \geq  1+(k+1)a$.

            D'après l'hypothèse de récurrence $(1+a)^k  \geq  1+ka$ or comme $a>0$ alors $1+a>0$ donc en multipliant les deux membres de $(1+a)^k \geq  1+ka$ par $1+a$  on a : 
            
            $(1+a)^k \times (1+a) \geq  (1+ka)(1+a)$ .
            
            Mais $(1+ka)(1+a)=1+a+ka+ka^2=1+(k+1)a+ka^2$ alors comme $ka^2 \geq 0$ ,on a :
            
            $1+(k+1)a+ka^2 \geq 1+(k+1)a$.

            Par conséquent : $(1+a)^{k+1}  \geq  1+(k+1)a$. Ainsi, la propriété est héréditaire.

            - **Conclusion** : la propriété est vraie pour $n=0$ et est héréditaire, donc on a démontré par récurrence que quel que soit $n \in \N,(1+a)^n  \geq  1+na$.

        - Soit $q>1$ alors il existe un nombre réel $a>0$ tel que  $q=1+a$ .

            Alors $q^n=(1+a)^n$ Donc d'après l'inégalité de Bernoulli , on a $q^n  \geq 1+na$ .
        
            Comme $a>0$ alors $\dlim{n}{+\infty} (1+na)=+\infty$ et d'après le théorème de comparaison  , $\dlim{n}{+\infty} q^n=+\infty$.

        - Si $0<q<1$, on pose $a=\dfrac{1}{q}$. Alors $a>1$ et d'après ce qui précède $\dlim{n}{+\infty}a^n=+\infty$, donc $\dlim{n}{+\infty} \dfrac{1}{q^n}=+\infty$.
        - Si $-1<q<0$, on pose $a=-q$. Alors $0<a<1$ et d'après ce qui précède $\dlim{n}{+\infty}a^n=0$. Or pour tout $n\in \N$, $-a^n<q^n<a^n$. Comme $\dlim{n}{+\infty} -a^n = 0$ et $\dlim{n}{+\infty} a^n = 0$, donc d'après le théorème de l'encadrement : $\dlim{n}{+\infty} q^n=0$.
        - Si $q=0$, alors pour tout $n>0$ $q^n=0$, donc $\dlim{n}{+\infty} q^n=0$
        - Si $q=1$, alors pour tout $n \in \N$ $q^n=1$, donc $\dlim{n}{+\infty} q^n =1$.