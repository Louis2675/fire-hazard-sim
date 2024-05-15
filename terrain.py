"""
This module contains the class definitions for a game grid.
"""

class Cell:
    """
    Represents a single cell in a grid.

    Attributes:
        terrain_type (str): The type of terrain for this cell.
        fire_strength (int): The strength of fire in this cell, used to calculate the probability of fire spreading to a neighboring cell.
        height (int): Currently unused.
        coors (tuple): The coordinates of this cell on the grid.
        burning (bool): Whether this cell is currently on fire.
        dying (bool): Whether the fire in this cell is currently dying out.
    """
    def __init__(self, terrain_type, fire_strength, height, x, y):
        self.terrain_type = terrain_type
        self.fire_strength = fire_strength
        self.height = height
        self.coors = (x, y)
        self.burning = False
        self.dying = False


class Terrain:
    """
    Represents a grid of cells.

    Attributes:
        size (int): The size of the terrain grid.
        grid (list): The grid itself, initially empty.
    """
    def __init__ (self, size):
        self.size = size
        self.grid = []
        # Populate the grid with cells
        for line in range (size):
            self.grid.append([])
            for col in range (size) : 
                self.grid[line].append(Cell("None", 0, 0, line, col))