# Automate_cellulaire
Projet de représentation d'Automate Cellulaire et de Machine de Turing réalisé en Python par Baptiste Garnier et Hajar Cherqi

## Bibliothèque à installer avant l'éxecution ducode
1. La bibliothèque Random pour générer des mots aléatoires
2. La bibliothèque inspect qui permet d'afficher sur le terminal le code des fonctions pythons=
3. La bibliotèque ast pour une meilleur prise en charge des tuples en tant que strezsasdzs
4. La bibliothèques sys qui permet de récupérer des éléments choisi par l'utilisateur 
5. Le module Makefile pour WSL ou les équivalents sur Mac et Linux pour un meilleur appel des différentes questions


## Implémentation des fichiers
Les fichier nécessaire pour les Automates Cellulaires sont de la forme :
"element_de_gauche element_centrale_element_de_droite -> element_par_lequelle_on_remplace_celui_du_centre"
et on peut mettre autant de ligne que voulu amis si les éléments de gauche sont mis en double alors seul le dernier sera pris en compte. Et il n'est pas obligé d'écrire une règle pour toute les combinaisons de gauche, s'il n'y en a pas alors l'élément ne changera pas entre deux tours.

Exemple de fichier pour l'automate cellulaire qui répond à la règle 110:
0,0,0 -> 0
0,0,1 -> 1
0,1,0 -> 1
0,1,1 -> 1
1,0,0 -> 0
1,0,1 -> 1
1,1,0 -> 1
1,1,1 -> 0

Le fichier pour les Machines de Turing sont de la forme :
mot_a_mettre_dans_la_machine_au_début
état_de_début
état_de_fin
les transition qui sont dela forme état_début,élément_visible,état_suivant,élément_remplacant,direction

Exemple de fichier pour une Machine de Turing :
101
q0
accept
q0,0,q0,1,>
q0,1,q0,1,>
q0,_,accept,_,_


## Utilisation de l'interface sur le termianl
Pour faire fonctionner notre application il faut sur Windows aller dans WSL et pour Linux et Mac ouvrir un terminal Linux et ensuite utiliser différente commande make :
0. Si on souhaite afficher toutes les questions en même temps il faut juste faire la commande "make".
1. Si l'on souhaite juste afficher la question 1 il suffit de fairela commande "make Question1".
2. Pareil pour la question 2 mais avec la commande "make Question2".
3. Pour la question 3 il y a deux cas. Soit on veut juste afficher le code de la fonction qui est demandé de faire lors de cette question donc on utilise la commande "make Question3" soit on souhiate avoir un exemple dela fonction alors on rajoute à la suite de la commande "Mode=Exemple".
4. Pareil que pour la question 3 il ya 2 modes un avec exemple et l'autre sans donc on doit utiliser la commande "make Question4 Mode=Exemple" dans le premier cas et juste "make Question4" dans le second.
5. Pour la question 5 il y a plus de choix possible : il y a celui dans lequel on voit juste le code et il fait à partir de la commande "make Question5". Si l'on souhaite on peut rajouter un mode qui est soit "Mode=Iteration" soit "Mode=Transition" soit "Mode=Succession" qui correspond pour la première a faire n itération de la configuration de base avec un automate, pour la seconde a faire tourner une configuration sur un automate cellulaire jusqu'à qu'une transition particulière est été effectué et pour la dernière itérer une configuration sur un automate cellualire jusqu'à que celle ci ne change plus.POur les trois modes on peut rajouter a la suite de la commande "Mot=votre_mot" qui permet de choisir une configuration précise. Pour les modes itération et transition on peut en plus rajouter une valeur "Valeur=votre_valeur" qui correspond pour le premier au nombre d'itérations "n" à faire et pour le second la transition a recherché noté "x,y,z" si ce n'est pas fait alors ces valeurs son choisi arbitrairement .
6. Pour la question 6 on fait exacement pareil que pour la quetion 5 en changeant juste le 5 en 6 car on a juste rajouter plus d'explication lors de l'execution du code.
7. La question 7 possède 4 modes en fonction de quelle fichier de donnée vous voulez choisir votre automte : "Mode=Infini" pour un automate qui fera se propager ses valeurs vers les extrémités, "Mode=Cyclic" pour un automate qui fera tourner en boucle n'importe quelle configuration donné, "Mode=Choix1" pour un automate intéressant choisi qui consiste en une suite de valeur qui pourrait corespindre à une sorte d'aléatoire et "Mode=Choix2" qui est unn automate intéressant qui est utilisé pour la représentation de traffic routier.
8. Si l'on souhaite juste afficher la question 1 il suffit de fairela commande "make Question8".
9. Pareil pour la question 2 mais avec la commande "make Question9".
10. Pour la question 10 il y a deux cas possibles : soit on veut juste afficher le code de la fonction qui est demandé de faire lors de cette question donc on utilise la commande "make Question10" soit on souhiate avoir un exemple dela fonction alors on rajoute à la suite de la commande "Mode=Exemple".
11. Pareil que pour la question 10 il ya 2 modes un avec exemple et l'autre sans donc on doit utiliser la commande "make Question12 Mode=Exemple" dans le premier cas et juste "make Question11" dans le second.
12. Pour la question 12 il suffit de faire la commande "make Question12" pour voir le code et rajouter "Mode=Exemple" pour voir un exmple de la fonction avec les éléments qui sont dans le fichier texte "Machine_Turing.txt".
13. Pour la question 13 c'est exactement pareil que pour la question 12 ci-dessus.
14. Pour afficher la réponse à la question 14 il suffit de faire la commande "make Question14".