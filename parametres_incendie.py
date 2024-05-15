"""
Fichier contenant les paramètres de la propagation de l'incendie
"""

from math import inf

# Intensité de l'incendie pour que chaque biome brule
S_PLAIN = 2
S_FOREST = 4 
S_HOUSE = 8

# Probabilités des évenements spéciaux
P_THUNDER = 0.8

P_RAIN = 0.15 # Probability of rain
T_RAIN = 10 # The time the rain lasts
RAIN_INTENSITY = 0.25 # The lower it is, the more intense the rain is

P_WIND = 0.25 # Probability to change the direction of the wind
T_WIND = 5 # Time to wait before changing the direction
F_WIND = 1.2 # Force of the wind





