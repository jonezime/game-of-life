## Description des règles du jeu de la vie

_Julien Onézime - CDAN_

---

à T=0 deux cas possibles:

-   la cellule est allumée
    Si elle dispose de 2 ou 3 cellules allumées dans son voisinnage proche (8 voisines) alors elle reste allumée à T+1 et s'éteint sinon.
-   la cellule est éteinte
    Si elle a exactement 3 voisines proches d'allumées alors elle s'allume sinon elle reste éteinte.

Réaliser en programmation fonctionnelle une simulation du jeu de la vie.

Le programme pourra être paramétré par fichier ou en argument concernant la taille de la grille (en x et en y) et savoir si les bords de la grille sont connectés entre eux.

Les configurations de base seront stockées dans des fichiers au format :

-   5 //taille en x
-   5 //taille en y
-   0 // wrap ou non
-   (1,2) //coordonnées des cellules actives
-   (3,5)
-   (3,3)

L'affichage est laissé à l'appréciation du/de la programmeur(se).
Le format texte est encouragé.

~~Bonus :
Modifier votre programme pour permettre la description de règles différentes de celles de Conway.~~ : pas fait...
