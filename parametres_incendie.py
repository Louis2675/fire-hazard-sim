"""
The parameters for the fire propagation.
The normal parameters are already in it.
We recommand using the following parameters :
RAIN_INTENSITY = 0.5
F_WIND = 0.15
"""


# Intensity of the fire required for each biome to burn
S_PLAIN = 2 # The fire intensity required for plains to burn
S_FOREST = 4 # The fire intensity required for forests to burn
S_HOUSE = 8 # The fire intensity required for houses to burn

# Probabilities of special events
P_THUNDER = 0.8 # Probability of a thunder event

P_RAIN = 0.05 # Probability of rain
T_RAIN = 15 # The time the rain lasts
RAIN_INTENSITY = 0.25 # The higher it is, the more intense the rain is

P_WIND = 0.25 # Probability to change the direction of the wind
T_WIND = 12 # Time to wait before changing the direction
F_WIND = 0.25 # Force of the wind





