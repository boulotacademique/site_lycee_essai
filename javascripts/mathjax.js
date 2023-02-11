window.MathJax = {
   tex: {
     inlineMath: [["\\(", "\\)"]],
     displayMath: [["\\[", "\\]"]],
     processEscapes: true,
     processEnvironments: true,
     macros:{
      N : '{\\mathbb{N}}',
      R : '{\\mathbb{R}}',
      Syst : ['\\left\\{ \\begin{array}{rcl} #1\\\\ #2 \\end{array} \\right.', 2],
      cad : "c'est-à-dire"
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
 
 