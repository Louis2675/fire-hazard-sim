"""
Fichier contenant la classe grid définissant une grid de jeu.
"""

class Cell:
    def __init__(self, terrain_type, fire_strength, height):
        self.terrain_type = terrain_type
        self.fire_strength = fire_strength
        self.height = height


class Terrain:
    def __init__ (self, size):
        self.size = size
        self.grid = []
        for i in range (size):
            self.grid.append([])
            for _ in range (size) : 
                self.grid[i].append(Cell("None", 0, 0))
    
    def copie (self, patron):
        for line in range (self.size):
            for col in range (self.size):
                self.grid[line][col] = (self.grid[line][col])
        return 0

    
    # Inutile
    def display_grid(self):
        for line in range(self.size):
            print()
            for col in range(self.size):
                if self.grid[line][col].height <= 0:
                    print("\033[1;36m{}\033[1;37m".format(self.grid[line][col].height), end="")
                else:
                    print("\033[1;32m{}\033[1;37m".format(self.grid[line][col].height), end="")
