from random import random
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
        return Cell("E", 0, 0)
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
            if random() < P_MAISON and terrain.grid[line][col].terrain_type != "E":  # Avec une probabilité P_MAISON
                terrain.grid[line][col].is_house = True  # Placer une maison dans la cellule
    return terrain  # Retourner le terrain avec les maisons générées


def generation_terrain(P_FORET=P_FORET, P_PLAINE=P_PLAINE, P_EAU=P_EAU, TAILLE_TERRAIN=TAILLE_TERRAIN):
    """
    Fonction qui génère un terrain aléatoire
    Entrée : P_EAU, P_PLAINE, P_FORET; les probabilités de la présence de l'eau, de la plaine et de la forêt et la size du terrain
    Sortie : List, le terrain généré avec les biomes et les maisons
    """
    # On initialise un terrain vide
    terrain = Terrain(TAILLE_TERRAIN)
    # On change les cases du terrain avec la fonction generation_case
    for line in range(TAILLE_TERRAIN):
        for col in range(TAILLE_TERRAIN):
            terrain.grid[line][col] = generation_case(P_FORET, P_PLAINE, P_EAU)

    terrain = generer_maisons(terrain)
    # On retourne le terrain avec les cases remplies
    return terrain


if __name__ == "__main__":
    terrain = generation_terrain()
    terrain.display_grid()


