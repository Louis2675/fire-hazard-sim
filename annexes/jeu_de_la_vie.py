import random

def creation_grille():
    n = int(input("Saisir la taille de la grille : "))
    grille = [[random.randint(0,1) for _ in range (n)] for  _ in range(n)]
    return grille

def floraison():
    grille = [
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,1,1,1,0],
        [0,0,0,1,1,1,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]
    ]
    return grille

def afficher_grille(grille):
    for i in range (len(grille)):
        print()
        for j in range(len(grille)):
            print(grille[i][j], end="  ")
    print()


def nb_voisin(grille, i, j):
    """
    Entrée: Une grille et une case
    Sortie: le nombre de voisin de cette casee
    """
    mur_i_haut = 0
    mur_i_bas = 0
    mur_j_gauche = 0
    mur_j_droite = 0
    if i == 0 :
        mur_i_haut = 1
    elif i == len(grille)-1:
        mur_i_bas = 1
    if j == 0:
        mur_j_gauche = 1
    elif j == len(grille)-1:
        mur_j_droite = 1
    
    nb = 0
    for k in range(i-1 + mur_i_haut,i+2 - mur_i_bas):
        for l in range(j-1 + mur_j_gauche, j+2 - mur_j_droite):
            if grille[k][l] == 1:
                if not(k == i and l == j) :
                    nb = nb+1
    
    return nb


def copie_grille(grille):
    copie = []
    for i in range (len(grille)):
        copie.append([])
        for j in range (len(grille)):
            copie[i].append(grille[i][j])
    return copie

def tour_jeu_de_la_vie(grille):
    copie = copie_grille(grille)

    for i in range (len(grille)):
        for j in range (len(grille)):
            nb_voisins = nb_voisin(copie, i, j)
    
            if nb_voisins  == 3 :
                grille[i][j] = 1
            
            elif nb_voisins < 2 or  nb_voisins > 3 :
                grille[i][j] = 0

    return grille

def jeu_de_la_vie (grille):
    nb_tour = int(input("Veuillez saisir le nombre de tour du jeu de la vie : "))

    for i in range (nb_tour):
        grille = tour_jeu_de_la_vie(grille)
        afficher_grille(grille)
        x = input("continuer ? ")
    return grille

grille=floraison()
afficher_grille(grille)
jeu_de_la_vie(grille)


