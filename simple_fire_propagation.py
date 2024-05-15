import random
import copy
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


def neighbour_burning(terrain, cell):
    """
    Checks if a neighbour is burning based on a copied precedent version, returns True if yes, False if no
    """
    coor = cell.coors
    for i in range(max(0, coor[0] - 1), min(terrain.size, coor[0] + 2)): 
        for j in range(max(0, coor[1] - 1), min(terrain.size, coor[1] + 2)):
            if i == coor[0] and j == coor[1]:
                continue  # Skip the cell itself
            if terrain.grid[i][j].burning:
                return True
    return False


def propagate_fire_simple(terrain, copy):
    """
    Propagates the fire
    """
    for line in terrain.grid:
        for cell in line:
            if cell.terrain_type != 'W':
                if neighbour_burning(copy,cell):
                    cell.burning = True


def simple_simulation_step(terrain, turn_count):
    """
    Perform a single step in the simple fire simulation.
    """
    copy_terrain = copy.deepcopy(terrain)

    for line in terrain.grid:
        for cell in line:
            update_fire(cell)
    propagate_fire_simple(terrain, copy_terrain)
    return thunder(turn_count, terrain)
    