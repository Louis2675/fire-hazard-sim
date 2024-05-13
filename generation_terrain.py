import random
import copy
from parametres_terrain import P_PLAIN, P_FOREST, P_HOUSE, TERRAIN_SIZE, P_WATER
from terrain import Terrain, Cell

def cell_generator(terrain):
    """
    Function to give each cell it's type between the three primary ones : Water, Forest or Plain
    Entry : terrain, wich we will change
    Sortie : the new terrain with each cell now having a type
    """
    for line in range (terrain.size):
        for col in range (terrain.size):
            # We take a number between 0 and 1
            alea = random.random()
            # We check if the number is under the probability for a forest
            if alea < P_WATER:
                terrain.grid[line][col].terrain_type = 'W'
            # Same for a plain
            elif alea < 0.42:
                terrain.grid[line][col].terrain_type = 'P'
            else :
                terrain.grid[line][col].terrain_type = 'F'
    return terrain



def generate_houses(terrain):
    """
    Function to place houses on the terrain

    Paramètres:
    terrain : l'objet terrain sur lequel on veut générer des maisons

    Retourne:
    terrain : le terrain avec les maisons générées
    """
    for line in range(terrain.size):  
        for col in range(terrain.size):
            random_number = random.random()
            if random_number < P_HOUSE and terrain.grid[line][col].terrain_type != "W":  # With a probability of P_HOUSE and if it is not water
                terrain.grid[line][col].terrain_type = 'H'  # The type is then a house
    return terrain


def new_height_randomizer(height):
    random_num = random.random()
    if random_num <= 0.5:
        if height != 0:
            height = height-1
    elif 0.5 < random_num :
        if height != 9:
            height = height + 1
    return height

def generate_heights(terrain):
    for line in range(terrain.size):
        for col in range(terrain.size):
            if col == line == 0:
                terrain.grid[line][col].height = random.randint(0,9)
            elif line == 0:
                new_height = new_height_randomizer(terrain.grid[line][col-1].height)
                terrain.grid[line][col].height = new_height
            elif col == 0 :
                new_height = new_height_randomizer(terrain.grid[line-1][col].height)
                terrain.grid[line][col].height = new_height
            else:
                height1 = new_height_randomizer(terrain.grid[line-1][col].height)
                height2 = new_height_randomizer(terrain.grid[line][col-1].height)

                terrain.grid[line][col].height = (height1 + height2) // 2
    return terrain

def change_cell (terrain, copie, x, y):
    """
    Function that counts the number of each neighbour and give our cell the type of the most numerous neighbour
    """
    nb_F = 0
    nb_P = 0
    nb_W = 0
    if x != terrain.size - 1 and y != terrain.size - 1 : # We make sur the cell is not bordering a side
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if not(i == j == 0):
                    if copie.grid[x + i + 0 ** x][y + j + 0 ** y].terrain_type == 'P':
                        nb_P += 1
                    elif copie.grid[x + i + 0 ** x][y + j + 0 ** y].terrain_type == 'F':
                        nb_F += 1
                    else :
                        nb_W += 1
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


def harmonization (terrain):
    for _ in range (16): # We do 10 turns of harminizing the terrain
        copie = copy.deepcopy(terrain)
        for line in range (terrain.size):
            for col in range (terrain.size):
                change_cell(terrain, copie, line, col)
    
    return terrain


def generate_terrain ():
    terrain = Terrain(TERRAIN_SIZE)
    return generate_houses(harmonization(cell_generator(terrain)))

if __name__ == "__main__":
    terrain = generate_terrain()
    terrain.display_grid()

"""
# Now we check for the height of the cells and give the water type for the ones below the water height
            if terrain.grid[line][col].height <= WATER_HEIGHT:
                terrain.grid[line][col].terrain_type = 'W'
generate_heights()
"""