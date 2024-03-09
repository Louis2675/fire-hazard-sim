from random import random
from parametres_terrain import P_EAU, P_PLAINE, P_FORET 

def parametres_terrain(P_FORET=P_FORET, P_PLAINE=P_PLAINE, P_EAU=P_EAU):
    """
    Fonction initialisant les parametres du terrain aléatoirement
    Entrée : P_EAU, P_PLAINE, P_FORET; les probabilités de la présence de l'eau, de la plaine et de la forêt
    """
    # On tire un nombre aléatoire entre 0 et 1
    alea = random()
    # On compare ce nombre à la probabilité de présence de l'eau
    if alea < P_EAU:
        return "Eau"
    # On compare ce nombre à la probabilité de présence de la forêt
    elif alea < P_EAU + P_FORET:
        return "Foret"
    # Sinon, on retourne la plaine
    else:
        return "Plaine"

