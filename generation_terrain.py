from random import random
from parametres_terrain import P_EAU, P_PLAINE, P_FORET, TAILLE_TERRAIN
from grille import Grille

def generation_case(P_FORET=P_FORET, P_PLAINE=P_PLAINE, P_EAU=P_EAU):
    """
    Fonction initialisant les parametres du terrain aléatoirement
    Entrée : P_EAU, P_PLAINE, P_FORET; les probabilités de la présence de l'eau, de la plaine et de la forêt
    Sortie : String, retourne la valeur de la case : P, E ou F
    """
    # On tire un nombre aléatoire entre 0 et 1
    alea = random()
    # On compare ce nombre à la probabilité de présence de l'eau
    if alea < P_EAU:
        return "E"
    # On compare ce nombre à la probabilité de présence de la forêt
    elif alea < P_EAU + P_FORET:
        return "F"
    # Sinon, on retourne la plaine
    else:
        return "P"
    

def generation_terrain(P_FORET=P_FORET, P_PLAINE=P_PLAINE, P_EAU=P_EAU, TAILLE_TERRAIN=TAILLE_TERRAIN):
    """
    Entrée : P_EAU, P_PLAINE, P_FORET; les probabilités de la présence de l'eau, de la plaine et de la forêt et la taille du terrain
    """
    # On initialise un terrain vide
    terrain = Grille(TAILLE_TERRAIN)
    # On change les cases du terrain avec la fonction generation_case
    for ligne in range(TAILLE_TERRAIN):
        for col in range(TAILLE_TERRAIN):
            terrain.grille[ligne][col] = generation_case(P_FORET, P_PLAINE, P_EAU)
    # On retourne le terrain avec les cases remplies
    return terrain


if __name__ == "__main__":
    terrain = generation_terrain()
    terrain.afficher_grille()
