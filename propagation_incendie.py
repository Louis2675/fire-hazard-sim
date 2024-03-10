"""
Fichier contenant les fonctions liées à la propagation de l'incendie
"""

from parametres_incendie import I_EAU, I_FORET, I_MAISON, I_PLAINE

def evaluer_feu(case, I_EAU=I_EAU, I_FORET=I_FORET, I_MAISON=I_MAISON, I_PLAINE=I_PLAINE):
    """
    Cette fonction évalue l'état d'une case donnée et décide si elle doit brûler ou si l'intensité du feu doit augmenter.
    
    Paramètres:
    case : une liste représentant la case à évaluer. La liste contient trois éléments - le type de terrain, l'état de la maison et l'intensité du feu.
    I_EAU, I_FORET, I_MAISON, I_PLAINE : des constantes représentant les intensités de feu maximales pour différents types de terrains.

    Retourne:
    case : la case mise à jour après évaluation.
    """
    if case[1] == 1:  # Si la case contient une maison
        if case[2] == I_MAISON:  # Si l'intensité du feu a atteint le maximum pour une maison
            case = ["B", 1, case[2] - 1]  # La maison brûle et l'intensité du feu diminue
        else:
            case[2] = case[2] + 1  # Sinon, l'intensité du feu augmente
    else:  # Si la case ne contient pas de maison
        if case[0] == "P":  # Si le terrain est une plaine
            if case[2] == I_PLAINE:  # Si l'intensité du feu a atteint le maximum pour une plaine
                case = ["B", 0, case[2] - 1]  # Le terrain brûle et l'intensité du feu diminue
            else:
                case[2] = case[2] + 1  # Sinon, l'intensité du feu augmente
        elif case[0] == "F":  # Si le terrain est une forêt
            if case[2] == I_FORET:  # Si l'intensité du feu a atteint le maximum pour une forêt
                case = ["B", 0, case[2] - 1]  # Le terrain brûle et l'intensité du feu diminue
            else:
                case[2] = case[2] + 1  # Sinon, l'intensité du feu augmente
    # On saute le cas ou case[0] == "E" car l'eau ne brule jamais
    # On saut le cas ou case[0] == "C" car une fois carbonisée, la case ne peut plus bruler
    return case  # Retourner la case mise à jour
        

