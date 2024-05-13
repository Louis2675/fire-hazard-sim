"""
Fichier contenant les fonctions liées à la propagation de l'incendie
"""

import random
from parametres_incendie import S_WATER, S_FOREST, S_HOUSE, S_PLAIN

def update_fire(cell, S_FOREST=S_FOREST, S_HOUSE=S_HOUSE, S_PLAIN=S_PLAIN):
    """
    Cette fonction évalue l'état d'une cell donnée et décide si elle doit brûler ou si l'intensité du feu doit augmenter.
    
    Paramètres:
    La cell, un objet de la classe Cell.
    S_WATER, S_FOREST, S_HOUSE, S_PLAIN : des constantes représentant les intensités de feu maximales pour différents types de terrains.

    Retourne:
    cell : la cell mise à jour après évaluation.
    """
    if cell.terrain_type != "C" and cell.terrain_type != "W": # To skip all the following lines if the cell is already burnt
        if cell.terrain_type == "B": # For all burning cells
            cell.fire_strength = cell.fire_strength - 1
        else : # If it is not burning or charred, then it gains fire strength 
            cell.fire_strength = cell.fire_strength + 1
            if cell.terrain_type in ["P","F","H"]: # For the cells not burning that gained fire strength, we are checking whether they should be burning or not
                if cell.terrain_type == "P": # For plains
                    if cell.fire_strength == S_PLAIN:
                        cell.terrain_type = "B"
                elif cell.terrain_type == "F": # For forests
                    if cell.fire_strength == S_FOREST:
                        cell.terrain_type = "B"
                elif cell.terrain_type == "H": # For houses
                    if cell.fire_strength  == S_HOUSE:
                        cell.terrain_type = "B"
        if cell.fire_strength == 0 : # We are checking if the burning cells become charred
            cell.terrain_type = "C"


def thunder(turn_count, S_THUNDER, terrain):
    """
    Function to make thunderstrikes, it takes the turn count, the probability of a thunderstrike and the terrain as arguments
    """

    if turn_count % 10 == 0 : # Every 10 turns
        
        chance = random.random
        if chance < S_THUNDER : # the chance of a thunderstrike
            valid_cell_list = [] # We create a list for all of the valid cell (the ones that can be burnt)
            for line in terrain.grid:
                for cell in line:
                    if cell.terrain_type != "B" and cell.terrain_type != "W" and cell.terrain_type != "C":
                        valid_cell_list.append(cell)

            cell_struck = valid_cell_list[random.randint(0, len(valid_cell_list))] # the cell is struck at random
            
            if cell_struck.terrain_type == "P":
                cell_struck.fire_strength = S_PLAIN
            elif cell_struck.terrain_type == "F":
                cell_struck.fire_strength = S_FOREST
            elif cell_struck.terrain_type == "H":
                cell_struck.fire_strength = S_HOUSE
            
            cell_struck.terrain_type = "B"


def calculate_distance_factor(cell1, cell2):
    x1, y1 = cell1.coordinates
    x2, y2 = cell2.coordinates
    
    distance_squared = (x1 - x2) ** 2 + (y1 - y2) ** 2
    
    if distance_squared == 1:
        return 25
    elif distance_squared == 2:
        return 75
    else:
        assert False, "Les cellules ne sont ni diagonales ni voisines."


def calculate_propagation_chance(cell, cell2, S_WATER, S_FOREST, S_HOUSE, S_PLAIN):
    if cell.terrain_type == "W":
        s_max = S_WATER
    elif cell.terrain_type == "F":
        s_max = S_FOREST
    elif cell.terrain_type == "H":
        s_max = S_HOUSE
    elif cell.terrain_type == "P":
        s_max = S_PLAIN
    dist = calculate_distance_factor(cell, cell2)
    if cell2.terrain_type == "H" or cell2.terrain_type == "P":
        terrain_type_fact = 0.5
    if cell2.terrain_type == "F":
        terrain_type_fact = 1
    else:
        terrain_type_fact = 0
    return dist * terrain_type_fact * (0,75) ** (s_max-cell2.fire_strength)