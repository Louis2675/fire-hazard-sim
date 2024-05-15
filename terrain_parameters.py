"""
The parameters for the terrain
For a normal terrain:
P_WATER = 0.1
P_PLAIN = 0.48
For a plain terrain:
P_WATER = 0.09
P_PLAIN = 0.7
For a forest:
P_WATER = 0.09
P_PLAIN = 0.3
For an village:
P_WATER = 0.09
P_PLAIN = 0.45
P_HOUSE = 0.2
For a swamp:
P_WATER = 0.125
P_PLAIN = 0.28
"""

# Probability for each cell to be water
P_WATER = 0.1

# Probability for each cell to be forest, it is useless as all remaining cells in the generation are by design forest cells
P_FOREST = 0.4

# Probability for each cell to be plain
P_PLAIN = 0.48

# Probability for a house to appear on the terrain
P_HOUSE = 0.015

# Definition of the size of the grid representing the terrain. 
# An entry of 100 would create a grid of 100x100.
TERRAIN_SIZE = 120

# The height of the water in the terrain
WATER_HEIGHT = 0