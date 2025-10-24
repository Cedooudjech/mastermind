
# Mastermind

![Mastermind](Mastermind.jpg)

## Objectif
Réaliser un jeu de Mastermind en Python. Le projet propose deux versions possibles :
- Version terminal (obligatoire) — jeu jouable en ligne de commande.
- Version graphique (optionnelle, bonus) — interface avec Pygame pour une expérience visuelle.

## Introduction
Mastermind est un jeu de déduction où le joueur tente de découvrir une combinaison secrète de 4 éléments (couleurs ou chiffres). Après chaque proposition, le programme donne des indices sur les éléments corrects et leur position.

## Règles du jeu
- La combinaison secrète est composée de 4 éléments choisis aléatoirement parmi 6 possibles.
- Le joueur dispose de 10 tentatives pour deviner la combinaison.
- Après chaque tentative, le programme renvoie :
    - Un symbole (ex. `*`) pour chaque élément correct à la bonne position.
    - Un autre symbole (ex. `-`) pour chaque élément correct mais à la mauvaise position.
- Victoire si la combinaison est trouvée avant la fin des tentatives.
- Défaite si les 10 tentatives sont épuisées — la combinaison secrète est alors révélée.

## Fonctionnalités attendues
- Génération aléatoire d’une combinaison de 4 éléments.
- Validation des propositions (longueur et éléments valides).
- Calcul et affichage des indices après chaque tour.
- Limitation à 10 tentatives.
- Messages clairs de victoire/défaite.
- Bonus : interface graphique avec Pygame (interactions, affichage des pions, historique des tentatives).

## Installation
Prérequis :
- Python 3.8+
- (Optionnel pour la GUI) Pygame

Installation rapide :
- Cloner le dépôt
- (Optionnel) créer un environnement virtuel :
    - python -m venv venv
    - venv\Scripts\activate (Windows) ou source venv/bin/activate (Unix)
- Installer Pygame si besoin :
    - pip install -r requirements.txt

## Exécution
- Version terminal :
    - choisir l'option 1
- Version Pygame (si implémentée) :
    - choisir l'option 2

## Idées d’amélioration (bonus)
- Mode deux joueurs (un joueur saisit la combinaison).
- Différents niveaux de difficulté (longueur de combinaison, nombre de couleurs).
- Historique visuel des tentatives dans la GUI.
- Sons et animations dans la version Pygame.

## Licence & Auteurs
- Projet pédagogique de programmation python.
- Les contributeurs sont https://github.com/Cedooudjech .

Bon développement et amusez-vous bien en implémentant Mastermind !


