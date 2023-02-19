window.MathJax = {
   tex: {
     inlineMath: [["\\(", "\\)"]],
     displayMath: [["$$", "$$"],["\\[", "\\]"]],
     processEscapes: true,
     processEnvironments: true,
     macros:{
      N : '{\\mathbb{N}}',
      R : '{\\mathbb{R}}',
      lp : '{\\left(}',
      rp : '{\\right)}',
      ex : '{\\text{e}}',
      equivaut : '{\\iff}',
      Syst : ['\\left\\{ \\begin{array}{rcl} #1\\\\ #2 \\end{array} \\right.', 2],
      dlim : ['\\displaystyle{\\lim_{#1 \\to #2}}',2],
      Pb : '{\\mathbb{P}}',
      comb : ['\\displaystyle{\\left(\\begin{array}{c} #1 \\\\ #2 \\end{array}\\right)}',2],
      dvec : ['\\overrightarrow{#1}',1],
      vect : ['\\overrightarrow{#1}',1],
      vec : ['\\overrightarrow{#1}',1],
      V : ['\\overrightarrow{#1}',1],
      mc : ['\\mathcal{#1}',1],
      coordVecEsp: ['\\left(\\begin{array}{c} #1 \\\\ #2 \\\\ #3\\end{array}\\right)',3],
      vectCoEsp : ['\\vect{#1}=\\coordVecEsp{#2}{#3}{#4}',4],
      Lim: ['\\displaystyle{\\left. \\begin{array}{lcl} #1 \\\\ #2 \\\\ \\end{array} \\right\\} }',2],
      Oij: '{\\left( O;\\vec{i},\\vec{j}\\right)}',
      Oijk: '{\\left( O;\\vec{i},\\vec{j},\\vec{k}\\right)}',
        
     }
   },
   options: {
     ignoreHtmlClass: ".*|",
     processHtmlClass: "arithmatex"
   }
 };
 
 document$.subscribe(() => {
   MathJax.typesetPromise()
 })
 
 