"""
Fichier contenant les fonctions liées à la propagation de l'incendie
"""

import random
from fire_parameters import S_FOREST, S_HOUSE, S_PLAIN, P_THUNDER, RAIN_INTENSITY, F_WIND

def set_fire (terrain, coor):
    """
    Function to put a cell whose coordinates we gave on fire
    """
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
                if cell.fire_strength <= 0: # If the fire is totally burnt
                    cell.terrain_type = "C" # The cell becomes charred
            else :# Now we increase the fire and check if the fire is dying
                cell.fire_strength = cell.fire_strength + 1 # If the fire is not dying, it increases its strength
                if cell.fire_strength >= S_PLAIN and cell.terrain_type == 'P':
                    cell.dying = True
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

            if len(valid_cell_list) > 0 :
                cell_struck = valid_cell_list[random.randint(0, len(valid_cell_list))] # the cell is struck at random
            # If the cell is not already burning, we set it on fire and give it the right fire strength
                if cell_struck.terrain_type == "P":
                    cell_struck.fire_strength = S_PLAIN
                elif cell_struck.terrain_type == "F":
                    cell_struck.fire_strength = S_FOREST
                elif cell_struck.terrain_type == "H":
                    cell_struck.fire_strength = S_HOUSE
                
                cell_struck.burning = True
    
                return True
    return False

def calculate_distance_factor(cell1, cell2):
    """
    Function to calculate the distance between two cells
    """
    coor1 = cell1.coors # We get the coordinates of the two cells
    coor2 = cell2.coors
    x1, y1 = coor1[0], coor1[1]
    x2, y2 = coor2[0], coor2[1]
    # We calculate the squared distance between the two cells
    distance_squared = (x1 - x2) ** 2 + (y1 - y2) ** 2
    # We return the factor depending on the distance
    if distance_squared == 1:
        return 25
    elif distance_squared == 2:
        return 75
    else:
        assert False, "The cells are more than one cell away from each other"

def calculate_propagation_chance(cell, cell2, rain, wind):
    if cell2.burning: # Makes the simuation faster because it doesn't do any calculations for cells that are not burning
        
        if cell.terrain_type == "F":
            s_max = S_FOREST
        elif cell.terrain_type == "H":
            s_max = S_HOUSE
        elif cell.terrain_type == "P":
            s_max = S_PLAIN
        dist = calculate_distance_factor(cell, cell2)
        
        if cell2.terrain_type == "H" or cell2.terrain_type == "P":
            terrain_type_fact = 0.5
        elif cell2.terrain_type == "F":
            terrain_type_fact = 1
        else :
            terrain_type_fact = 0
        
        propa_chance = dist * terrain_type_fact * (0.75) ** (s_max - cell2.fire_strength)

        if wind != 'n':
            if cell2.coors[0] > cell.coors[0] and wind == 'u':
                propa_wind = propa_chance * F_WIND
            elif cell2.coors[0] < cell.coors[0] and wind == 'd':
                propa_wind = propa_chance * F_WIND
            elif cell2.coors[1] > cell.coors[1] and wind == 'l':
                propa_wind = propa_chance * F_WIND
            elif cell2.coors[1] < cell.coors[1] and wind == 'r':
                propa_wind = propa_chance * F_WIND
            else :
                propa_wind = 0
        else :
            propa_wind = 0 # If there is no wind, then there is no chance to propagate the fire faster
        
        if rain == True:
            return propa_chance + propa_wind - propa_chance * RAIN_INTENSITY # We gat the chance of a propagation is P + P * w - P * r (propagation + (propagation times the force of the wind) - (propagation times the intensity of the rain))
        return propa_chance + propa_wind
    return 0

def cell_total_propagation_chance(terrain, cell, rain, wind):
    """
    Calculate the total propagation chance of a cell in a given terrain.

    Args:
        terrain (Terrain): The terrain object containing the grid.
        cell (Cell): The cell for which to calculate the propagation chance.
        rain (float): The rain factor.
        wind (float): The wind factor.

    Returns:
        float: The total propagation chance of the cell.
    """
    total_chance = 0
    coor = cell.coors

    up, right, down, left = 0, 0, 0, 0

    # If there is a direction to the wind, we add 1 to the directions, making the calculation skip the cells on the other side of the wind
    if wind != 'n': # If the direction of the wind is not none
        if wind == 'u':
            up = 1
        elif wind == 'r':
            right = 1
        elif wind == 'd':
            down = 1
        else :
            left = 1

    for i in range(max(0, coor[0] - 1) + up, min(terrain.size, coor[0] + 2) - down): 
        for j in range(max(0, coor[1] - 1) + left, min(terrain.size, coor[1] + 2) - right):
            if i == coor[0] and j == coor[1]:
                continue  # Skip the cell itself
            total_chance += calculate_propagation_chance(cell, terrain.grid[i][j], rain, wind)
                
    return total_chance

def will_cell_burn(terrain, cell, rain, wind):
    """
    Determines if a cell will burn based on its terrain type, rain, and wind conditions.

    Args:
        terrain (Terrain): The terrain object representing the cell's terrain type.
        cell (Cell): The cell object to check for burning.
        rain (float): The rain intensity.
        wind (float): The wind intensity.

    Returns:
        bool: True if the cell will burn, False otherwise.
    """
    if cell.terrain_type != 'W' and cell.terrain_type != 'C':
        random_nb = random.randint(1, 100)
        if random_nb <= cell_total_propagation_chance(terrain, cell, rain, wind):
            return True
    return False

def propagate_fire(terrain, rain, wind):
    """
    Propagates fire in the given terrain based on rain and wind conditions.

    Args:
        terrain (Terrain): The terrain object representing the fire hazard simulation.
        rain (float): The amount of rain present in the environment.
        wind (float): The strength and direction of the wind.

    Returns:
        None
    """
    for i in range(terrain.size):
        for j in range(terrain.size):
            if will_cell_burn(terrain, terrain.grid[i][j], rain, wind):
                terrain.grid[i][j].burning = True

def proba_simulation_step(terrain, turn_count, rain, wind):
    """
    Perform a single step in the fire simulation.

    Args:
        terrain (Terrain): The terrain object representing the fire spread area.
        turn_count (int): The current turn count.
        rain (float): The amount of rain.
        wind (float): The wind speed.

    Returns:
        None
    """
    # Update fire status for each cell in the terrain
    for line in terrain.grid:
        for cell in line:
            update_fire(cell)
    propagate_fire(terrain, rain, wind)
    return thunder(turn_count, terrain)
