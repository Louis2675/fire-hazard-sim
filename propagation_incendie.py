"""
Fichier contenant les fonctions liées à la propagation de l'incendie
"""

from parametres_incendie import I_EAU, I_FORET, I_MAISON, I_PLAINE

def evaluer_feu(case, I_EAU=I_EAU, I_FORET=I_FORET, I_MAISON=I_MAISON, I_PLAINE=I_PLAINE):
    """
    Fonction qui évalue l'intensité de l'incendie sur une case
    Entrée : case, la case à évaluer
    Sortie : Int, l'intensité de l'incendie sur la case
    """
    if case[1] == 1:
        if 

