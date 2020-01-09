# Proj531

Ce projet a pour but de coder un jeu d'échec en python.
Nous avons pour objectif de créer un jeu fonctionnel qui respecte les règles du jeu classique (déplacements + coups spéciaux comme le rock) avec une interface graphique qui fonctionne aux clics et affiche les coups jouables quand on clique sur un pion et prend en compte la mise en échec (force à jouer seulement les pions pouvant contrer un échec, et empêcher un joueur de se mettre sois même en échec).
Le jeu doit nous permettre de jouer en 1 contre 1 ou contre une IA.

Pour lancer le jeu il faut récupérer les codes python sur Github: Board, Cases, Main et Pieces. Puis les lire à l'aide d'un logiciel python (idle, spyder...).
Il faut ensuite télécharger IMAGES.zip et en extraire les images. 
Créer un dossier dans lequel on sauvergardera l'ensemble des fichiers pythons ainsi que les images téléchargées.
Enfin lancer le main et le jeu s'affichera.

Pour jouer il suffit de cliquer sur les pions que l'on veut déplacer puis sur la case sur laquelle on veut le déplacer (sachant que les options possibles seront des cases colorées en vert), puis alterner chacun son tour. Ce sont toujours les blancs qui commencent.

La partie se termine lorsqu'il y a échec et mat (un message d'échec s'affiche) ou si l'on ferme la fenêtre.
