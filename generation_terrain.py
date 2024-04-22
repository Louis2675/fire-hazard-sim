import random
from parametres_terrain import P_EAU, P_PLAINE, P_FORET, P_MAISON, TAILLE_TERRAIN
from terrain import Terrain, Cell

def generation_case(P_FORET=P_FORET, P_PLAINE=P_PLAINE, P_EAU=P_EAU):
    """
    Fonction initialisant les parametres du terrain aléatoirement
    Entrée : P_EAU, P_PLAINE, P_FORET; les probabilités de la présence de l'eau, de la plaine et de la forêt
    Sortie : List, retourne la valeur de la case : P, E ou F avec 0 car les maisons ne sont pas encore générées.
    """
    # On tire un nombre aléatoire entre 0 et 1
    alea = random()
    # On compare ce nombre à la probabilité de présence de l'eau
    if alea < P_EAU:
        return Cell("W", 0, 0)
    # On compare ce nombre à la probabilité de présence de la forêt
    elif alea < P_EAU + P_FORET:
        return Cell("F", 0, 0)
    # Sinon, on retourne la plaine
    else:
        return Cell("P", 0, 0)


def generer_maisons(terrain, P_MAISON=P_MAISON):
    """
    Cette fonction génère des maisons sur un terrain donné. 
    Elle parcourt chaque cellule du terrain et, avec une probabilité P_MAISON, 
    elle place une maison dans la cellule (en mettant la deuxième valeur de la cellule à 1).

    Paramètres:
    terrain : l'objet terrain sur lequel on veut générer des maisons
    P_MAISON : la probabilité qu'une maison soit générée dans une cellule donnée

    Retourne:
    terrain : le terrain avec les maisons générées
    """
    for line in range(terrain.size):  # Parcourir chaque line du terrain
        for col in range(terrain.size):  # Parcourir chaque colonne du terrain
            if random() < P_MAISON and terrain.grid[line][col].terrain_type != "W":  # Avec une probabilité P_MAISON
                terrain.grid[line][col].is_house = True  # Placer une maison dans la cellule
    return terrain  # Retourner le terrain avec les maisons générées


def new_height_randomizer(height):
    random_num = random.random()
    if random_num <= 0.25:
        if height != 0:
            height = height-1
    if 0.25 < random_num <= 0.5:
        if height != 9:
            height = height + 1
    return height


def generate_terrain_heights(terrain):
    for line in range(terrain.size):
        for col in range(terrain.size):
            if col == line == 0:
                terrain.grid[col][line].height = random.randint(0,9)
            elif col == 0 :
                new_height = new_height_randomizer(terrain.grid[line-1][col].height)
                terrain.grid[col][line].height = new_height
            elif line == 0:
                new_height = new_height_randomizer(terrain.grid[line][col-1].height)
                terrain.grid[col][line].height = new_height
            else:
                if random.random() > 0.5:
                    new_height = new_height_randomizer(terrain.grid[line-1][col].height)
                else:
                    new_height = new_height_randomizer(terrain.grid[line][col-1].height)
                terrain.grid[line][col].height = new_height
    return terrain


if __name__ == "__main__":
    terrain = Terrain(50)
    terrain = generate_terrain_heights(terrain)
    terrain.display_grid()


