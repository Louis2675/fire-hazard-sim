import random

def creation_grid():
    n = int(input("Saisir la size de la grid : "))
    grid = [[random.randint(0,1) for _ in range (n)] for  _ in range(n)]
    return grid

def floraison():
    grid = [
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,1,1,1,0],
        [0,0,0,1,1,1,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]
    ]
    return grid

def display_grid(grid):
    for i in range (len(grid)):
        print()
        for j in range(len(grid)):
            print(grid[i][j], end="  ")
    print()


def nb_voisin(grid, i, j):
    """
    Entrée: Une grid et une case
    Sortie: le nombre de voisin de cette casee
    """
    mur_i_haut = 0
    mur_i_bas = 0
    mur_j_gauche = 0
    mur_j_droite = 0
    if i == 0 :
        mur_i_haut = 1
    elif i == len(grid)-1:
        mur_i_bas = 1
    if j == 0:
        mur_j_gauche = 1
    elif j == len(grid)-1:
        mur_j_droite = 1
    
    nb = 0
    for k in range(i-1 + mur_i_haut,i+2 - mur_i_bas):
        for l in range(j-1 + mur_j_gauche, j+2 - mur_j_droite):
            if grid[k][l] == 1:
                if not(k == i and l == j) :
                    nb = nb+1
    
    return nb


def copie_grid(grid):
    copie = []
    for i in range (len(grid)):
        copie.append([])
        for j in range (len(grid)):
            copie[i].append(grid[i][j])
    return copie

def tour_jeu_de_la_vie(grid):
    copie = copie_grid(grid)

    for i in range (len(grid)):
        for j in range (len(grid)):
            nb_voisins = nb_voisin(copie, i, j)
    
            if nb_voisins  == 3 :
                grid[i][j] = 1
            
            elif nb_voisins < 2 or  nb_voisins > 3 :
                grid[i][j] = 0

    return grid

def jeu_de_la_vie (grid):
    nb_tour = int(input("Veuillez saisir le nombre de tour du jeu de la vie : "))

    for i in range (nb_tour):
        grid = tour_jeu_de_la_vie(grid)
        display_grid(grid)
        x = input("continuer ? ")
    return grid

grid=floraison()
display_grid(grid)
jeu_de_la_vie(grid)


