"""
Fichier contenant la classe grid définissant une grid de jeu.
"""

class Cell:
    def __init__(self, terrain_type, is_house, fire_strength):
        self.terrain_type = terrain_type
        self.is_house = is_house
        self.fire_strength = fire_strength


class Terrain:
    def __init__ (self, size):
        self.size = size
        self.grid = []
        for i in range (size):
            self.grid.append([])
            for _ in range (size) : 
                self.grid[i].append(Cell("None", False, 0))
    
    def display_grid(self):
        for line in range(self.size):
            print()
            for col in range(self.size):
                cell = self.grid[line][col]
                
                
                
if __name__ == '__main__':
    grid = Terrain(8) 
    grid.display_grid()
