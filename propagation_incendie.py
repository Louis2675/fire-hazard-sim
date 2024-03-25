"""
Fichier contenant les fonctions liées à la propagation de l'incendie
"""

from random import randint
from parametres_incendie import S_FOREST, S_HOUSE, S_PLAIN

def update_fire(cell, S_FOREST=S_FOREST, S_HOUSE=S_HOUSE, S_PLAIN=S_PLAIN):
    """
    Cette fonction évalue l'état d'une cell donnée et décide si elle doit brûler ou si l'intensité du feu doit augmenter.
    
    Paramètres:
    La cell, un objet de la classe Cell.
    S_WATER, S_FOREST, S_HOUSE, S_PLAIN : des constantes représentant les intensités de feu maximales pour différents types de terrains.

    Retourne:
    cell : la cell mise à jour après évaluation.
    """
    if cell.terrain_type != "C": # To skip all the following lines if the cell is already burnt
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
    num_cells_terrain = terrain.size ** 2
    num_cell = randint(0, 99)
    cell_struck = terrain.grid[num_cell // 10][num_cell % 10] 
    
    if cell_struck.terrain_type != "W":
        cell_struck.terrain_type = "B"
        
        if cell_struck.terrain_type == "H"
        cell_struck.fire_strength = 
        
        if cell_struck
    
    
    
        

