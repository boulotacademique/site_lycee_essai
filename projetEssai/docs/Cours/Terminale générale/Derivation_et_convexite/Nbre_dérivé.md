# Le nombre dérivé

!!! info "Définition"
	Soit $f$  une fonction définie sur un intervalle $I$ contenant $a$.

	* $f$ est **dérivable** en $a$  de nombre dérivé $f'(a)$ signifie:
	
	\[
	\lim\limits_{h\to 0}\dfrac{f(a+h)-f(a)}{h}=f'(a)
	\]
	
	ou encore
	
	\[
	\lim\limits_{x\to a}\dfrac{f(x)-f(a)}{x-a}=f'(a)
	\]
	
	(avec $f'(a)$ nombre **fini**).
	
	* $f$ est dérivable sur $I$ signifie que $f$ est dérivable en tout $x$ de $I$.
	* La fonction dérivée de $f$  notée $f'$ est la fonction qui, à tout $x$ de I associe le nombre $f'(x)$ .


<iframe class = "Im_cache" src="https://www.geogebra.org/classic/jqmhwka5?embed" width="100%" height="600" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px; text-align : center;" frameborder="0"></iframe>

???- example "Exemple"
	Etudier la dérivabilité en 2 de la fonction $f:x\mapsto x^2+2$.
	
	???- done "Réponse"
		Soit $h\neq0$</br>
		$\dfrac{f(2+h)-f(2)}{h}=\dfrac{(2+h)^2+2-6}{h}= \dfrac{h^2+4h}{h}=h+4$. Or 
		
		\[
		\lim_{h \to 0}(h+4)=4
		\]
		
		Donc $f$ est dérivable en 2 et $f'(2)=4$.

???- example "Exemple"
	Etudier la dérivabilité en 0 de la fonction $f:x \mapsto \sqrt{x}$.
	
	???- done "Réponse"
		La fonction racine carrée est définie pour $x\geq 0$.</br>
		Soit $h>0$</br>
		$\dfrac{f(0+h)-f(0)}{h}=\dfrac{\sqrt{h}}{h}=\dfrac{1}{\sqrt{h}}$, or
		
		\[
		\lim_{h \to 0} \dfrac{1}{\sqrt{h}}=+\infty
		\]
		
		donc 
		
		\[
		\lim_{h \to 0} \dfrac{f(0+h)-f(0)}{h}=+\infty
		\]
		
		Donc la fonction racine carrée n'est pas dérivable en 0.

???- example "Exemple"
	Etudier la dérivabilité en 0 de la fonction $f:x \mapsto |x|$.

    ???- done "Réponse"
        Pour tout $h \in \R-\{0\}$, $\dfrac{f(0 + h)-f(0)}{h} = \dfrac{|h|}{h}$.

        Si $h>0$,

        \begin{eqnarray*}
        \dfrac{f(0 + h)-f(0)}{h} & = & \dfrac{|h|}{h}\\
        & = & \dfrac{h}{h} \\
        & = & 1
        \end{eqnarray*}

        Donc $\dlim{x}{0^+} \dfrac{f(0 + h)-f(0)}{h} = 1$.

        Si $h<0$,

        \begin{eqnarray*}
        \dfrac{f(0 + h)-f(0)}{h} & = & \dfrac{|h|}{h}\\
        & = & \dfrac{-h}{h} \\
        & = & -1
        \end{eqnarray*}

        Donc $\dlim{x}{0^-} \dfrac{f(0 + h)-f(0)}{h} = -1$.

        Donc $f$ n'est pas dérivable en $0$.