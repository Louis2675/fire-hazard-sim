"""
Fichier contenant la classe grid définissant une grid de jeu.
"""

class Cell:
    def __init__(self, terrain_type, is_house, fire_strength, height):
        self.terrain_type = terrain_type
        self.is_house = is_house
        self.fire_strength = fire_strength
        self.height = height


class Terrain:
    def __init__ (self, size):
        self.size = size
        self.grid = []
        for i in range (size):
            self.grid.append([])
            for _ in range (size) : 
                self.grid[i].append(Cell("None", False, 0, 0))
    
    def display_grid(self):
        for line in range(self.size):
            print()
            for col in range(self.size):
                if self.grid[line][col].height <= 0:
                    print("\033[1;36m{}\033[1;37m".format(self.grid[line][col].height), end="")
                else:
                    print("\033[1;32m{}\033[1;37m".format(self.grid[line][col].height), end="")

                
                
                
if __name__ == '__main__':
    grid = Terrain(8) 
    grid.display_grid()
