# allumettes_py

Le jeu des allumettes se joue à deux joueurs. Un tas d'allumettes, généralement X est déposé
sur une table. Chaque joueur à tour de rôle prend de une à trois allumettes du tas. Le gagnant
est celui qui parvient à prendre la (les) dernière(s) allumette(s) du tas.

On demande de réaliser un programme qui permet de jouer au jeu des allumettes contre
l'ordinateur. Dès qu'il en aura l'opportunité, l'ordinateur devra appliquer la stratégie gagnante.
Le programme choisira un nombre d'allumettes aléatoire entre 15 et 30 puis demandera à
l'utilisateur s'il souhaite jouer en premier. La partie démarre ensuite. Quand c'est le tour
du joueur, le programme lui proposera d'entrer le nombre d'allumettes qu'il souhaite prendre
et contrôlera que ce nombre est compris entre 1 et 3 (si ce n'est pas le cas, le joueur sera invité
à recommencer). Quand c'est au tour de l'ordinateur de jouer, si c'est possible, il prendra un
nombre d'allumettes (toujours entre 1 et 3) de sorte qu'il n'en reste qu'un multiple de 4 dans
le tas. Si ce n'est pas possible, l'ordinateur prendra un nombre aléatoire entre 1 et 3. A chaque
coup du joueur et de l'ordinateur, le programme achera le nombre d'allumettes restantes.
Lorsque la partie est terminée, le programme demandera au joueur s'il souhaite jouer une autre
partie.
