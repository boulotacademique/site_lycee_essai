# Codage des caractères : ASCII


## Introduction


L’utilisation d’un ordinateur passe la plupart du temps par le texte. Que ce soit pour lire ou écrire une instruction, utiliser un traitement de texte, naviguer sur internet nous manipulons des mots, des symboles. Mais comment sont-ils représentés et traités en interne ?

En informatique, les caractères (chiffres, alphabets …) sont représentés par des nombres.
Le codage des caractères est une convention de codage.
Il existe de nombreux codages des caractères. Les principaux codages sont :
<ul>
<li> Le code ASCII (ISO 646)</li>
<li> Les codes ISO 8859-1 / ISO 8859-15</li>
<li> L’Unicode avec les codes UTF-8 / UTF-16 / UTF-32</li>
</ul>


## L'ASCII
Le code ASCII (American Standard Code for Information Interchange) créé en 1961 (par Bob Bemer) est un code sur 7+1 bits. Le premier bit (le bit de poids fort) reste à 0. À une époque, on utilisait ce bit comme bit de parité (détection d’erreur).

Le code ASCII code les lettres, les chiffres et d'autres symboles sous forme de nombre entiers binaires de 7 bits.

Les caractères de 0 à 31 ainsi que le 127 ne sont pas affichables et correspondent à des directives (ex.: 13 $\rightarrow$ CR $\rightarrow$ &laquo; retourne à la ligne &raquo;, 27 $\rightarrow$ ESC $\rightarrow$ &laquo; échappe &raquo;, 127 $\rightarrow$ DEL $\rightarrow$ &laquo; efface &raquo;). Le caractère 32 est l’espace blanc. Les autres correspondent aux chiffres, aux lettres majuscules et minuscules et à des symboles de ponctuation.

ASCII est un nom américain, Le nom officiel de cette norme est l’ISO 646.

[![Tableau ASCII](../../Image/TabASCII.jpg){.Center_lien .VignetteMed}](../../Image/TabASCII.jpg)


\begin{exo}
Coder (en hexadécimal) à l'aide de la table de caractère ASCII la phrase suivante : \\
Ceci N'est PAS

\begin{Solub}
\small
\begin{tabular}{*{14}{c}}
C & e & c & i &   & N & ' & e & s & t &   & P & A & S \\%&   & u & n &   & m & e & s & s & a & g & e &   & s & e & c & r & e & t &   & ! \\
43 & 65 & 63 & 69 & 20 & 4E & 27 & 65 & 73 & 74 & 20 & 50 & 41 & 53 %& 20 & 75 & 6E & 20 & 6D & 65 & 73 & 73 & 61 & 67 & 65 & 20 & 73 & 65 & 63 & 72 & 65 & 74 & 20 & 21 \\
\end{tabular}
\end{Solub}
\end{exo}

\begin{exo}
Décoder le message suivant :\\
75 6E 20 6D 65 73 73 61 67 65 20 73 65 63 72 65 74 20 21 

\begin{Solub}
\begin{tabular}{*{19}{c}}
75 & 6e & 20 & 6d & 65 & 73 & 73 & 61 & 67 & 65 & 20 & 73 & 65 & 63 & 72 & 65 & 74 & 20 & 21 \\
u & n &   & m & e & s & s & a & g & e &   & s & e & c & r & e & t &   & ! \\
\end{tabular}
\end{Solub}

\end{exo}

\begin{att}
Le tableau précédent est la table de caractère (ou  jeu de caractère) : elle donne à chaque symbole un nombre. Comme chacun de ces nombres peuvent être représentés sur un octet\footnotemark, la manière dont ce nombre est écrit en mémoire est simple : il suffit de prendre un octet et d'y écrire le code binaire associé au symbole !
\end{att}
\footnotetext{il y a un bit de parité}

Problèmes : Pas d’accents et de nombreuses variantes pour utiliser le 8ème bit (Mac, IBM, \ldots)

Les limites de l’ASCII ont conduit, sur trois périodes différentes, à trois approches de l'internationalisation :
<ul>
<li> L'utilisation de standards régionaux à caractères mono-octets, techniquement les plus faciles à mettre en place (mais attention aux échanges de fichiers entre les différentes langues. Sauriez-vous expliquer pourquoi ?);
</li>
<li> L'utilisation de standards extensibles, où un même octet peut représenter un caractère différent suivant le contexte (famille ISO 2022) ainsi que des extensions où un caractère est codé sur plusieurs octets ;
</li>
<li> L'utilisation du Standard Unicode (famille UTF). C’est celui qui comprend le plus grand nombre de caractères.
</li>
</ul>

\begin{rque}
Les 128 caractères de l’ASCII n’ont pas été placés au hasard. Leurs codes ont été soigneusement étudiés. Ci-dessous, quelques exemples.
<ul>
<li> À l’époque reculée\footnote{celle des dinosaures !} où a été conçu l’ASCII, on communiquait encore parfois des données à l’ordinateur via des cartes perforées. Chaque emplacement codait un bit : 1 s’il y avait un trou, 0 sinon. La perforation était irréversible. Lorsqu'on n’avait pas encore spécifié de caractère particulier, on laissait tous les emplacements intacts et le caractère valait donc 0 (tous les bits à 0). Ce caractère « non spécifié » se retrouve en ASCII avec NUL, le caractère nul, qui vaut 0. De même, lorsqu’on voulait effacer un caractère on perçait tous les emplacements, ce qui donnait 127 (tous les bits à 1) ; le caractère ASCII DEL (delete) correspond justement à cette suppression.
</li>
<li> Les lettres majuscules sont séparées de leurs homologues minuscules par un intervalle de 32. Cela signifie qu’il suffit de modifier un bit (le 6e) pour passer des unes aux autres, ce qui simplifie les traitements.
</li>
</ul>
\end{rque}

## ISO-8859-1}

L’ISO 8859-1 [ou Latin-1] (1992) était utilisé par de nombreuses langues européennes. Le codage se faisait sur 8 bits (il a donc \ans{$2\ \ $} fois plus de caractère que l'ASCII). 

\begin{center}
\incImage[0.6]{ISO}
\end{center}

Mais certains caractères n’étaient pas codés : \oe, \OE \ldots et il manquait le caractère \euro{} de l’euro !! Pour corriger cela, on a créé le code ISO 8859-15 [ou latin 9]
Mais il fallait toute une collection de codes pour chaque groupe de pays.
Au final en 2004, le groupe de normalisation a décidé d’abandonner ce code au profit de l’Unicode et de l’UTF-8.

\begin{center}
\incImage[0.6]{Dif_latin_1_9}
\end{center}

\begin{methode}[Méthode : Lire le tableau précédent.]
Pour le lire, on ajoute le nombre hexadécimal de la ligne (qui représente le &laquo; chiffre des dizaines&raquo;{}) et celui de la colonne (qui représente celui &laquo; des unités &raquo;{}).\\
Par exemple, le caractère £ est codé par A3.
\end{methode}

\begin{att}
Ici aussi, le passage de la table de caractère à l'écriture en mémoire est simple : on retranscrit sur un octet le code du tableau
\end{att}

## UTF-8 et Unicode}

\subsection{ISO 10646}

\begin{quote}
\emph{
ISO 10646 voit le jour en 1990. Il s'agit du Jeu universel de caractères ou JUC (en anglais, UCS pour Universal Character Set). Celui-ci a été pensé pour pouvoir accueillir n'importe quel caractère existant de n'importe quelle langue du monde. Un travail titanesque ! Concrètement, c'est un bête jeu de caractères, sauf que celui-ci offre pas moins de $2^{21} = \np{2 097 152}$ codes ! À l’origine, il allait même jusqu’à $2^{32} = \np{4 294 967 296}$, mais il a rapidement été restreint : c’est déjà bien suffisant.
}
\begin{flushright}
\url{http://sdz.tdct.org/sdz/comprendre-les-encodages.html}
\end{flushright}
\end{quote}

Il s'agit donc d'une très grosse table de caractères, permettant de coder tous les caractères connus\footnote{il y a encore de la place !}.

La bonne nouvelle est que les 256 premiers caractères coïncident avec ceux de ISO 8859-1.

\begin{exo}
Combien de bits utilise ISO 10646 ?\\
Combien (au minimum) de 0 sont affichés pour coder des caractères de la table ISO 8859-1 ?
%\begin{comment}
%\vspace{2cm}
%\end{comment}
\begin{Solub}\\
Il y a 21 bits utilisés.\\
Seuls 8 bits sont nécessaires (au maximum), il y aura donc 13 zéros (au minimum)!
\end{Solub}
\end{exo}

Mais de façon à ne pas occuper de la place mémoire inutilement (avec plein de 0), l'écriture en mémoire diffère du code. C'est la norme \textbf{Unicode} qui précise comment cela est fait !

\subsection{Unicode}

\begin{quote}
\emph{
\textbf{Unicode} est une norme développée par le Consortium Unicode publiée pour la première fois en 1991 (en 2011, elle en est à la version 6.1). On peut la voir comme une surcouche (une extension) d’ISO 10646. En fait, les deux normes sont développées parallèlement et synchronisées en permanence. Là où ISO 10646 liste simplement les caractères du jeu et leur assigne un nom et un code, Unicode va plus loin en leur ajoutant des attributs et en décrivant des relations entre eux (donc en leur donnant un sens).
}
\end{quote}

Unicode est un donc une table de caractère (celle de l'ISO 10646\footnote{avec des caractères supplémentaires}) \textbf{et} des encodages (c'est-à-dire différentes façons de les écrire en mémoire).\\
Vous trouverez la table (par exemple) à \url{https://unicode-table.com/fr/#control-character}

<ul>
<li> La façon la plus simple pour encoder cette table de caractère est UTF-32 : On utilise 32 bits (soit \ans{$4\ \ \ $} octets). Le problème est le gaspillage de mémoire avec beaucoup de zéro
</li>
<li> La deuxième part du principe que la plupart des langues n'aura besoin que de 16 bits. On parle alors d'UTF-16\footnote{Mais se pose alors le problème du boutisme \url{https://fr.wikipedia.org/wiki/Boutisme}}. Si nécessaire, on ajoute des octets.
</li>
<li> Pour l'ASCII, 8 bits est suffisant. On peut alors se contenter de l'UTF-8. Pour latin-9 ou latin-1, on ajoute des octets selon les règles du tableau ci-dessous.
</li>
</ul>

\begin{center}
\incImage[0.5]{UTF8_01}\\
\textbf{\small La partie surlignée correspond au codage en binaire dans la table de caractère Unicode.}
\end{center}

\begin{exple}
En ISO 8859-1, le code (en hexadécimal) de la lettre A est  41.
\begin{enumerate}
</li>
<li> Quel est le nombre binaire associé ?
%\begin{comment}
%\vspace{1cm}
%\end{comment}
\begin{Solub}\\
Il s'agit de $\base{0100\ 0001}$
\end{Solub}
</li>
<li> Quel est son encodage en UTF-32 ?
%\begin{comment}
%\vspace{1cm}
%\end{comment}
\begin{Solub}\\
Il s'agit de $\base{00000000\ 00000000\ 00000000\ 01000001}$
\end{Solub}
</li>
<li> Quel est son encodage en UTF-16 ? Quel est l'économie par rapport à UTF-32?
%\begin{comment}
%\vspace{1cm}
%\end{comment}
\begin{Solub}\\
Il s'agit de $\base{00000000\ 01000001}$. Il permet d'économiser $50\%$ de l'espace mémoire.
\end{Solub}
</li>
<li> Quel est son encodage en UTF-8 ? Quel est l'économie  par rapport à UTF-32 ?
%\begin{comment}
%\vspace{1cm}
%\end{comment}
\begin{Solub}\\
Il s'agit de $\base{01000001}$. Il permet d'économiser $75\%$ de l'espace mémoire.
\end{Solub}
\end{enumerate}

\end{exple}

\begin{exo}
Donner le codage en UTF-8 des caractères suivants:
\begin{colenumerate}{4}
</li>
<li> k
</li>
<li> \verb|DEL|
</li>
<li> §
</li>
<li> É
\end{colenumerate}
%\begin{comment}
%\vspace{3cm}
%\end{comment}
\begin{Solub}
\begin{enumerate}
</li>
<li> D'après le tableau 6B=$\base{01101011}$. Donc, en UTF-8 : $0110 1011$ ou en hexadécimal 6B 
</li>
<li> D'après le tableau A7=$\base{10 100111}$. Il faut donc 8 bits. D'après le tableau,en UTF-8 : 
$\base{110 00010\ 10 100111 }$ ou en hexadécimal C2 A7
</li>
<li> D'après le tableau C9=$\base{11 001001}$. Il faut donc 8 bits. D'après le tableau,en UTF-8 : 
$\base{110 00011\ 10 001001 }$ ou en hexadécimal C3 89.
\end{enumerate}
\end{Solub}
\end{exo}

\begin{obj}
<ul>
<li> Savoir utiliser un tableau de caractères (ASCII, Latin-1 ou Latin -9) pour coder (en binaire et en hexadécimal) une chaîne de caractères ;
</li>
<li> Savoir utiliser un tableau de caractères (ASCII, Latin-1 ou Latin -9) pour traduire un code en binaire ou en hexadécimal) ;
</li>
<li> Avoir compris la différence entre table de caractère et encodage ;
</li>
<li> À partir du tableau fourni dans le cours, déterminer le code UTF-8 associé à un caractère.
</li>
</ul>
\end{obj}