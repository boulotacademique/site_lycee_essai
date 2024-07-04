# Limite de suites : vers le supérieur

!!! info "Suites monotones **et** convergentes"

    - Si une suite est croissante **et a pour limite** $\mathbf{\ell}$ (c'est donc une suite convergente !) alors tous les termes de la suite sont inférieurs ou égaux à $\ell$ c'est-à-dire, pour tout entier naturel $n$ , $u_n \leq  \ell$ .
    - Si une suite est décroissante **et a pour limite** $\mathbf{\ell}$ (c'est donc une suite convergente !) alors tous les termes de la suite sont supérieurs  ou égaux à $\ell$ c'est-à-dire, pour tout entier naturel $n$ , $u_n \geq \ell$.

    ???- warning "Attention"

        Pour utiliser ces théorèmes, il faut d'abord s'assurer de la convergence de la suite.

???- abstract "Démonstration"
    _Démonstration par l'absurde (non exigible)_

    Supposons qu'il existe un entier $p$ tel que $u_p>\ell$ .

    $\ell-1<\ell$ et $\ell<u_p$ donc $\ell-1<\ell <u_p$ et $I=]\ell-1,u_p[$ est un intervalle ouvert contenant $\ell$.

    Comme $\dlim{n}{+\infty} u_n=\ell$ , par définition l'intervalle $I$ doit contenir  tous les termes de la suite à partir d'un certain rang $N$.

    Comme $(u_n)$  est croissante , pour tout $n \geq p$ , on a : $u_n \geq u_p$  donc si $n \geq p$ , $u_n\not\in I$.

    Il est impossible que $I$ contienne tous les termes de la suite à partir du rang $p$ .

    Ceci contredit le fait que la suite a pour limite $\ell$ . L'hypothèse était fausse et $\forall n$ , $u_n \leq \ell$.