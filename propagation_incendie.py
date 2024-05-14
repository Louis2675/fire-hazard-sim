"""
Fichier contenant les fonctions liées à la propagation de l'incendie
"""

import random
from parametres_incendie import S_WATER, S_FOREST, S_HOUSE, S_PLAIN, P_THUNDER

def set_fire (terrain, coor):
    """
    Function to put a cell whose coordinates we gave on fire
    """
    print(coor[0], coor[1])
    if terrain.grid[coor[0]][coor[1]].terrain_type != 'W':
        terrain.grid[coor[0]][coor[1]].burning = True

def update_fire(cell):
    """
    This Function activates at the end of the turn and updates the status on burning cells.
    It increases fire strength on cell that are close to burning and decreases it on cells that are burning.
    It changes the terrain type to 'C' if the cell is totally burnt.
    """
    if cell.terrain_type != "C" and cell.terrain_type != "W": # To skip all the following lines if the cell is already carbonized or water
        if cell.burning == True: # For all burning cells
            if cell.dying == True: # If the fire is dying
                cell.fire_strength = cell.fire_strength - 1
                if cell.fire_strength == 0: # If the fire is totally burnt
                    cell.terrain_type = "C" # The cell becomes charred
            else :# Now we increase the fire and check if the fire is dying
                cell.fire_strength = cell.fire_strength + 1 # If the fire is not dying, it increases its strength
                if cell.fire_strength >= S_PLAIN and cell.terrain_type == 'P':
                    cell.burning = True
                elif cell.fire_strength >= S_FOREST and cell.terrain_type == 'F':
                    cell.dying = True
                elif cell.fire_strength >= S_HOUSE and cell.terrain_type == 'H':
                    cell.dying = True


def thunder(turn_count, terrain):
    """
    Function to make thunderstrikes, it takes the turn count, the probability of a thunderstrike and the terrain as arguments
    """

    if turn_count % 50 == 0 : # Every 50 turns
        
        chance = random.random()
        if chance < P_THUNDER : # the chance of a thunderstrike
            valid_cell_list = [] # We create a list for all of the valid cell (the ones that can be burnt)
            for line in terrain.grid:
                for cell in line:
                    if cell.burning != True and cell.terrain_type != "W" and cell.terrain_type != "C":
                        valid_cell_list.append(cell)

            cell_struck = valid_cell_list[random.randint(0, len(valid_cell_list))] # the cell is struck at random
            
            if cell_struck.terrain_type == "P":
                cell_struck.fire_strength = S_PLAIN
            elif cell_struck.terrain_type == "F":
                cell_struck.fire_strength = S_FOREST
            elif cell_struck.terrain_type == "H":
                cell_struck.fire_strength = S_HOUSE
            
            cell_struck.burning = True


def rain():
    pass


def wind():
    pass


def calculate_distance_factor(cell1, cell2):
    coor1 = cell1.coors
    coor2 = cell2.coors
    x1, y1 = coor1[0], coor1[1]
    x2, y2 = coor2[0], coor2[1]
    
    distance_squared = (x1 - x2) ** 2 + (y1 - y2) ** 2
    
    if distance_squared == 1:
        return 25
    elif distance_squared == 2:
        return 75
    else:
        assert False, "Les cellules ne sont ni diagonales ni voisines."


def calculate_propagation_chance(cell, cell2):
    if cell.terrain_type == "F":
        s_max = S_FOREST
    elif cell.terrain_type == "H":
        s_max = S_HOUSE
    elif cell.terrain_type == "P":
        s_max = S_PLAIN
    dist = calculate_distance_factor(cell, cell2)
    if cell2.burning == True :
        if cell2.terrain_type == "H" or cell2.terrain_type == "P":
            terrain_type_fact = 0.5
        elif cell2.terrain_type == "F":
            terrain_type_fact = 1
        else :
            terrain_type_fact = 0
    else:
        terrain_type_fact = 0
    return dist * terrain_type_fact * (0.75) ** (s_max - cell2.fire_strength)


def cell_total_propagation_chance(terrain, cell):
    total_chance = 0
    coor = cell.coors
    
    for i in range(max(0, coor[0] - 1), min(terrain.size, coor[0] + 2)):
        for j in range(max(0, coor[1] - 1), min(terrain.size, coor[1] + 2)):
            if i == coor[0] and j == coor[1]:
                continue  # Skip the cell itself
            total_chance += calculate_propagation_chance(cell, terrain.grid[i][j])
                
    return total_chance

def will_cell_burn(terrain, cell):
    if cell.terrain_type != 'W' and cell.terrain_type != 'C':
        random_nb = random.randint(1, 100)
        if random_nb <= cell_total_propagation_chance(terrain,cell):
            return True
    return False


def propagate_fire(terrain):
    for i in range(terrain.size):
        for j in range(terrain.size):
            if will_cell_burn(terrain, terrain.grid[i][j]):
                terrain.grid[i][j].burning = True


def simulation_step(terrain, turn_count):
    for line in terrain.grid:
        for cell in line:
            update_fire(cell)
    thunder(turn_count, terrain)
    propagate_fire(terrain)
    turn_count = turn_count + 1
    return turn_count