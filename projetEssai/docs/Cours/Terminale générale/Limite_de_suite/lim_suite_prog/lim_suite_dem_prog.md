# Limite de suites : démonstration au programme

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

!!! info "Conséquence"

    - Une suite croissante non majorée a pour limite $+\infty$.
    - Une suite décroissante et non minorée a pour limite $-\infty$.

???- abstract "Démonstration"

    Une suite $(u_n)$ est majorée lorsqu'il existe un réel  $M$ tel que   pour tout  $n\in \N , u_n  \leq  M$.
    
    ???+ tip "Méthode"
        Le contraire de   **il existe** est **pour tout** et le contraire de  **pour tout** est **il existe**.

    Ainsi une suite $(u_n)$ n'est pas majorée lorsque pour tout  réel  $M$ , il existe   $p\in \N , u_p > M$.
    
    $(u_n)$ est croissante , pour tout $n \geq p$ , on a $u_n \geq u_p$ et donc $u_n>M$.
    
    Donc tous les termes de la suite sont dans l'intervalle $]M,+\infty[$ à partir du rang $p$ c'est-à-dire $\dlim{n}{+\infty}u_n=+\infty$.

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