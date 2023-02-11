# Convexité

## Première approche

!!! info "Une sécante, une corde"

    Soit $f$ une fonction et $\mathcal{C}_f$ sa courbe représentative dans un repère. Soient $A$ et $B$ deux points distincts de $\mathcal{C}_f$, la droite $(AB)$ est appelée **sécante**}** de $\mathcal{C}_f$. Par ailleurs, le segement $[AB]$ est appelé **corde** $[AB]$.

    <div class="Center_txt">

    ![Deux sécantes : (AB) et (AC)](../Image/secante.png)

    Deux sécantes : (AB) et (AC)
    </div>

On remarque

!!! info "Convexe"

    Soit une fonction et $\mathcal{C}_f$ sa courbe représentative dans un repère. On dit que $f$ est <span id = "convexe">**convexe**</span> sur un intervalle $I$ si $\mathcal{C}_f$ est en dessous de **toutes** ses sécantes entre les deux points d'intersection, c'est-à-dire en dessous des cordes associées.

???- example "Une fonction convexe sur son domaine"

    <iframe scrolling="no" title="Sécante01" src="https://www.geogebra.org/material/iframe/id/zkhwaskg/width/1906/height/901/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/false/ctl/false" width="1906px" height="901px" style="border:0px;"> </iframe>

    <div class="Center_txt">
    La fonction exponentielle est au-dessous de ses sécantes sur $\mathbb{R}$ ! Elle est convexe sur $\mathbb{R}$ (pas encore démontré).
    </div>

!!! info "Concave"

    Soit une fonction et $\mathcal{C}_f$ sa courbe représentative dans un repère. On dit que $f$ est <span id="concave">**concave**</span> sur un intervalle $I$ si pour tout réel $x$ de $I$, $\mathcal{C}_f$ est au-dessus de chacune de ses sécantes entre les deux points d'intersection.

???- example "Une fonction concave sur son domaine"

    <iframe scrolling="no" title="secante02" src="https://www.geogebra.org/material/iframe/id/rcqfstar/width/1906/height/901/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/false/ctl/false" width="1906px" height="901px" style="border:0px;"> </iframe>

    <div class="Center_txt">
    Cette fonction (qui est la fonction logarithme) est au-dessus de ses sécantes sur $[0; +\infty[$ ! Elle est concave sur $[0; +\infty[$ (pas encore démontré).
    </div>

!!! warning "Attention"

    Il faut toujours préciser **l'intervalle** sur lequel une fonction est convexe (ou concave) !

!!! warning "Attention"

    Une fonction qui n'est pas convexe sur un intervalle $I$ n'est pas une fonction concave sur $I$ !!
    Comme pour le sens de variations, il faudra le plus souvent décrire la convexité d'une fonction.

    Par exemple, une fonction est convexe sur $[-5;2]$, concave sur $[2;10]$ et convexe sur $[10; + \infty[$.

???- example "Une fonction quelconque"

    <iframe scrolling="no" title="Sécante03" src="https://www.geogebra.org/material/iframe/id/qur2rtxv/width/1906/height/901/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/false/ctl/false" width="1906px" height="901px" style="border:0px;"> </iframe>

    <div class="Center_txt">
    Cette fonction est au-dessus de ses sécantes sur $]-\infty; 1]$ ! Elle est concave sur $]-\infty; 1]$ (pas encore démontré).
    
    Cette fonction est au-dessous de ses sécantes sur $[1; +\infty[$ ! Elle est convexe sur $[1; +\infty[$ (pas encore démontré).
    </div>

!!! tip "Une définition presque inutilisable"

    Il est plutôt compliqué de démontrer qu'une courbe est au-dessous au-dessus de **toutes** ses sécantes sur un intervalle. Aussi, ne cherchez pas à le faire !

    Les théorèmes ci-dessous sont beaucoup plus simples d'utilisation.

L'étude de la convexité d'une fonction permet (entre autre) d'affiner la compréhension de son comportement : cela permet de savoir si la croissance &laquo; accélère &raquo; ou &laquo; ralentit &raquo;.

## Convexité et dérivation

!!! info "Convexe et dérivation"

    Soit $f$ une fonction définie et **deux fois dérivable** sur un intervalle I. 

    - $f$ est _convexe_ sur $I$ équivaut à $f'$ est croissante sur $I$.
    - $f$ est _convexe_ sur $I$ équivaut à **$f''$** est **positive** sur $I$.
    - $f$ est _convexe_ sur $I$ équivaut à $\mathcal{C}_f$ est **au-dessus** de ses tangentes sur $I$.

!!! info "Concave et dérivation"

    Soit $f$ une fonction définie et **deux fois dérivable** sur un intervalle I. 

    - $f$ est _concave_ sur $I$ équivaut à $f'$ est décroissante sur $I$.
    - $f$ est _concave_ sur $I$ équivaut à **$f''$** est **négative** sur $I$.
    - $f$ est _concave_ sur $I$ équivaut à $\mathcal{C}_f$ est **au-dessous** de ses tangentes sur $I$.

!!! warning "tangente et convextié"

    Avec la convexité (resp. concavité), la position relative entre une courbe et ses tangentes n'est connue que sur l'intervalle où la fonction est convexe (resp. concave).

???- example "Courbe et tangente"

    <iframe scrolling="no" title="Tgte02" src="https://www.geogebra.org/material/iframe/id/hyxh8zf2/width/1906/height/901/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/false/ctl/false" width="1906px" height="901px" style="border:0px;"> </iframe>

    <div class="Center_txt">
    Cette fonction  est concave sur $]-\infty; 1]$. Elle est _au-dessous_ de ses tangentes **uniquement** sur $]-\infty; 1]$ ! On remarque que la courbe passe _en dessus_ de la tangente tracée un peu plus loin sur $[1; +\infty[$.

    Cette fonction  est convexe sur $[1; +\infty[$. Elle est _au-dessus_ de ses tangentes **uniquement** sur $[1; +\infty[$ ! On remarque que la courbe passe _en dessous_ de la tangente tracée un peu plus loin sur $]-\infty; 1]$.
    </div>

## Point d'inflexion

Il est intéressant de trouver le moment où se produit le changement de convexité. D'où la définition :

!!! info "Point d'inflexion"

    Un **point d'inflexion** est un point où la courbe représentative d'une fonction traverse sa tangente.

    <div class="Center_txt">
    ![Point d'inflexion et tangente](../Image/PtInflex.png)

    </div>

!!! info "Caractérisation d'un point d'inflexion"

    Soit $f$ une fonction définie sur un intervalle $I$ et $a$ un réel de $I$.

    - Le point $A(a;f(a))$ est un point d'inflexion de $\mathcal{C}_f$ si et seulement si la convexité de $f$ change en $a$.
    - Si de plus $f$ est deux fois dérivable sur $I$, alors le point $A(a;f(a))$ est un point d'inflexion si et seulement $f''$ s'annule **et change de signe** en $a$.

???- tip "Astuce"

    Il est évident que, pour trouver un point d'inflexion, le plus simple est d'étudier le signe de $f''$ !

    !!! warning "Attention"

        La seule résolution de $f''(x) = 0$ ne permet pas de conclure ! Il faut en plus savoir si la dérivée seconde change de signe !