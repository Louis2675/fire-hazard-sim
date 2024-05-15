import random
import copy
from terrain_parameters import P_PLAIN, P_FOREST, P_HOUSE, TERRAIN_SIZE, P_WATER
from terrain import Terrain, Cell

def cell_generator(terrain):
    """
    Assigns a type (Water, Forest, or Plain) to each cell in the terrain.

    Args:
        terrain (Terrain): The terrain object to be modified.

    Returns:
        Terrain: The updated terrain object with each cell now having a type.
    """
    # Iterate over each cell in the terrain
    for line in range (terrain.size):
        for col in range (terrain.size):
            # Generate a random number
            alea = random.random()
            # Assign a type to the cell based on the random number
            if alea < P_WATER:
                terrain.grid[line][col].terrain_type = 'W'
            elif alea < P_PLAIN:
                terrain.grid[line][col].terrain_type = 'P'
            else :
                terrain.grid[line][col].terrain_type = 'F'
    return terrain

def generate_houses(terrain):
    """
    Places houses on the terrain.

    Args:
        terrain (Terrain): The terrain object on which houses are to be generated.

    Returns:
        Terrain: The terrain object with the generated houses.
    """
    # Iterate over each cell in the terrain
    for line in range(terrain.size):  
        for col in range(terrain.size):
            # Generate a random number
            random_number = random.random()
            # If the random number is less than the probability of a house and the cell is not water, place a house
            if random_number < P_HOUSE and terrain.grid[line][col].terrain_type != "W":
                terrain.grid[line][col].terrain_type = 'H'
    return terrain

def new_height_randomizer(height):
    """
    Randomly increments or decrements the given height.

    Args:
        height (int): The current height.

    Returns:
        int: The new height after random increment or decrement.
    """
    # Generate a random number
    random_num = random.random()
    # If the random number is less than or equal to 0.5 and the height is not 0, decrement the height
    if random_num <= 0.5:
        if height != 0:
            height = height-1
    # If the random number is greater than 0.5 and the height is not 9, increment the height
    elif 0.5 < random_num :
        if height != 9:
            height = height + 1
    return height

def generate_heights(terrain):
    """
    Generates heights for each cell in the terrain.

    Args:
        terrain (Terrain): The terrain object.

    Returns:
        Terrain: The terrain object with updated heights.
    """
    # Iterate over each cell in the terrain
    for line in range(terrain.size):
        for col in range(terrain.size):
            # If the cell is at the top-left corner, assign a random height
            if col == line == 0:
                terrain.grid[line][col].height = random.randint(0,9)
            # If the cell is on the top edge, assign a height based on the cell to the left
            elif line == 0:
                new_height = new_height_randomizer(terrain.grid[line][col-1].height)
                terrain.grid[line][col].height = new_height
            # If the cell is on the left edge, assign a height based on the cell above
            elif col == 0 :
                new_height = new_height_randomizer(terrain.grid[line-1][col].height)
                terrain.grid[line][col].height = new_height
            else:
                # If the cell is not on an edge, assign a height based on the cells above and to the left
                height1 = new_height_randomizer(terrain.grid[line-1][col].height)
                height2 = new_height_randomizer(terrain.grid[line][col-1].height)

                terrain.grid[line][col].height = (height1 + height2) // 2
    return terrain

def change_cell (terrain, copie, x, y):
    """
    Changes the type of a cell based on the types of its neighbors.

    Args:
        terrain (Terrain): The terrain object.
        copie (Terrain): A copy of the terrain object.
        x (int): The x-coordinate of the cell.
        y (int): The y-coordinate of the cell.
    """
    # Initialize counters for each type of neighboring cell
    nb_F = 0
    nb_P = 0
    nb_W = 0
    # If the cell is not on the bottom or right edge, check all neighboring cells
    if x != terrain.size - 1 and y != terrain.size - 1 :
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if not(i == j == 0):
                    if copie.grid[x + i + 0 ** x][y + j + 0 ** y].terrain_type == 'P':
                        nb_P += 1
                    elif copie.grid[x + i + 0 ** x][y + j + 0 ** y].terrain_type == 'F':
                        nb_F += 1
                    else :
                        nb_W += 1
    # If the cell is on the bottom edge, check the neighboring cells above and to the sides
    elif x == terrain.size - 1:
        for i in [-1, 0]:
            if y == terrain.size - 1:
                for j in [-1, 0]:
                    if copie.grid[x + i][y + j].terrain_type == 'P':
                        nb_P += 1
                    elif copie.grid[x + i][y + j].terrain_type == 'F':
                        nb_F += 1
                    else :
                        nb_W += 1
            else :
                for j in [-1, 0, 1]:
                    if copie.grid[x + i][y + j].terrain_type == 'P':
                        nb_P += 1
                    elif copie.grid[x + i][y + j].terrain_type == 'F':
                        nb_F += 1
                    else :
                        nb_W += 1
    # If the cell is on the right edge, check the neighboring cells to the left and above
    else :
        for i in [-1, 0, 1]:
            if y == terrain.size - 1:
                for j in [-1, 0]:
                    if copie.grid[x + i][y + j].terrain_type == 'P':
                        nb_P += 1
                    elif copie.grid[x + i][y + j].terrain_type == 'F':
                        nb_F += 1
                    else :
                        nb_W += 1
            else :
                for j in [-1, 0, 1]:
                    if copie.grid[x + i][y + j].terrain_type == 'P':
                        nb_P += 1
                    elif copie.grid[x + i][y + j].terrain_type == 'F':
                        nb_F += 1
                    else :
                        nb_W += 1

    # If the cell is not a house, change its type based on the types of its neighbors
    if terrain.grid[x][y].terrain_type != 'H':
        if nb_F > 5 :
            terrain.grid[x][y].terrain_type = 'F'
        elif nb_P > 4 :
            terrain.grid[x][y].terrain_type = 'P'
        elif nb_W > 2:
            terrain.grid[x][y].terrain_type = 'W'
        else :
            if terrain.grid[x][y].terrain_type == 'W':
                random_nb = random.random()
                if random_nb < 0.6:
                    terrain.grid[x][y].terrain_type = 'P'
                else :
                    terrain.grid[x][y].terrain_type = 'F'

def harmonization(terrain):
    """
    Harmonizes the terrain by changing the type of each cell based on its neighbors.

    Args:
        terrain (Terrain): The terrain object.

    Returns:
        Terrain: The harmonized terrain object.
    """
    # Repeat the process 16 times
    for _ in range (16):
        # Create a copy of the terrain
        copie = copy.deepcopy(terrain)
        # Change the type of each cell based on its neighbors
        for line in range (terrain.size):
            for col in range (terrain.size):
                change_cell(terrain, copie, line, col)
    
    return terrain

def generate_terrain ():
    """
    Generates a terrain object.

    Returns:
        Terrain: The generated terrain object.
    """
    # Create a new terrain object
    terrain = Terrain(TERRAIN_SIZE)
    # Generate the types of each cell, place houses, and harmonize the terrain
    return generate_houses(harmonization(cell_generator(terrain)))

if __name__ == "__main__":
    # Generate a terrain and display it
    terrain = generate_terrain()
    terrain.display_grid()