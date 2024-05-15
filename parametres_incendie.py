"""
This module contains the parameters for fire propagation in the game.
"""

from math import inf

# Intensity of the fire required for each biome to burn
S_PLAIN = 2 # The fire intensity required for plains to burn
S_FOREST = 4 # The fire intensity required for forests to burn
S_HOUSE = 8 # The fire intensity required for houses to burn

# Probabilities of special events
P_THUNDER = 0.8 # Probability of a thunder event

P_RAIN = 0.15 # Probability of a rain event
T_RAIN = 10 # Duration of a rain event
RAIN_INTENSITY = 0.25 # Intensity of the rain. Lower values mean more intense rain.

P_WIND = 0.25 # Probability of a wind direction change event
T_WIND = 5 # Time to wait before changing the wind direction
F_WIND = 1.2 # Force of the wind