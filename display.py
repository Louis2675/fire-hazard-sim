# Import necessary libraries and modules
import pygame
import generation_terrain
import propagation_incendie
import random
from parametres_terrain import TERRAIN_SIZE
from parametres_incendie import P_RAIN, T_RAIN, P_WIND, T_WIND

# Function to calculate if it's raining or not
def calculate_rain(rain, time_rain):
    """
    Function to know if it is raining or not
    """
    # Generate a random number
    nb_rand = random.random()
    # If the random number is less than or equal to the probability of rain and it's not currently raining
    if nb_rand <= P_RAIN and rain == False:
        # Start raining and set the time of rain
        rain = True
        time_rain = T_RAIN
    # If it's currently raining
    elif rain == True:
        # If the time of rain is 0, stop raining
        if time_rain == 0:
            rain = False
        # If the time of rain is not 0, decrease the time of rain by 1
        else :
            time_rain -= 1
    # Return the state of rain and the time of rain
    return rain, time_rain

# Function to calculate the wind direction
def wind (direction, values, time):
    """
    Function to calculate the wind direction
    """
    # Generate a random number
    rand = random.random()
    # If the random number is less than or equal to the probability of wind and the time is 0
    if rand <= P_WIND and time == 0:
        # Choose a random wind direction and set the time of wind
        nb_rand = random.randint(0,4)
        time = T_WIND
        return values[nb_rand], time
    # If the time is greater than 0, maintain the current wind direction and decrease the time by 1
    elif time > 0 :
        return direction, time -1
    # If the time is 0, maintain the current wind direction
    else :
        return direction, time

# Main function
if __name__ == "__main__":
    # Generate the terrain
    terrain = generation_terrain.generate_terrain()
    # Initialize pygame
    pygame.font.init()

    # Initialize the main variables
    size = 800 # Height of the screen, width is 1.3 times the height
    marge = size//10 # The size of the sides of our simulation
    size_grid = size - marge # The size of our grid

    turn_count = 0 # The turn count for the simulation

    # Initialize the window
    window = pygame.display.set_mode((size*1.3, size)) 

    running  = True # To start pygame

    color = (255,255,255) # Color of the background

    # Initialize the state of rain and the time of rain
    rain = False
    time_rain = 0
    
    # Initialize the possible wind directions and the current wind direction and the time of wind
    wind_values = ['n','l', 'u', 'r', 'd'] # the values are none, left, up, right, down
    wind_direction = wind_values[0]
    time_wind = 0

    # Initialize the colors for the different rectangles
    colorW = (21, 124, 214)
    colorP = (72, 232, 9)
    colorF = (44, 143, 6)
    colorH = (186, 123, 13)
    colorB = (232, 24, 9)
    colorC = (0,0,0)

    # Set the title of our window
    pygame.display.set_caption('Fire Hazard Sim')

    # Main loop
    while running:
        # Increase the turn count by 1
        turn_count = turn_count + 1

        # Get the events
        events = pygame.event.get()

        # Loop through the events
        for event in events:
            # If the event is QUIT, stop the loop
            if event.type == pygame.QUIT :  
                running = False

            # If the event is MOUSEBUTTONDOWN
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the button is left click
                if event.button == 1: 
                    # Get the position of the mouse
                    x, y = event.pos
                    
                    # If the position is within the grid
                    if x > marge//2 and x < size_grid + marge//2 and y > marge//2 and y < size_grid + marge//2:
                        # Calculate the coordinates
                        x, y = (x- marge //2)//(size_grid//TERRAIN_SIZE), (y - marge // 2)//(size_grid//TERRAIN_SIZE)
                        coors = (y, x)
                        # Set fire at the coordinates
                        propagation_incendie.set_fire(terrain, coors)
            
            # If the event is KEYDOWN
            elif event.type == pygame.KEYDOWN:
                
                # If the key is ESCAPE, stop the loop
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Fill the window with the background color
        window.fill((255,255,255))

        # Display the grid by looking at the cell's type and showing a particular color for this type of cell
        for line in range (terrain.size):
            for col in range (terrain.size):

                # If the cell's type is "C", draw a rectangle with the colorC
                if terrain.grid[line][col].terrain_type == "C" :
                    pygame.draw.rect(window, colorC, pygame.Rect(marge//2 + col*(size_grid//terrain.size), marge//2 + line*(size_grid//terrain.size), size_grid//terrain.size, size_grid//terrain.size))
                
                # If the cell is burning, draw a rectangle with a color based on the fire strength
                elif terrain.grid[line][col].burning == True:
                    pygame.draw.rect(window, (170 + (terrain.grid[line][col].fire_strength * 9), 10+ (terrain.grid[line][col].fire_strength * 10), 10+ (terrain.grid[line][col].fire_strength * 10)), pygame.Rect(marge//2 + col*(size_grid//terrain.size), marge//2 + line*(size_grid//terrain.size), size_grid//terrain.size, size_grid//terrain.size))
                
                # If the cell's type is 'F', draw a rectangle with the colorF
                elif terrain.grid[line][col].terrain_type == 'F':
                    pygame.draw.rect(window, colorF, pygame.Rect(marge//2 + col*(size_grid//terrain.size), marge//2 + line*(size_grid//terrain.size), size_grid//terrain.size, size_grid//terrain.size))
                
                # If the cell's type is 'W', draw a rectangle with the colorW
                elif terrain.grid[line][col].terrain_type == 'W':
                    pygame.draw.rect(window, colorW, pygame.Rect(marge//2 + col*(size_grid//terrain.size), marge//2 + line*(size_grid//terrain.size), size_grid//terrain.size, size_grid//terrain.size))
                
                # If the cell's type is 'P', draw a rectangle with the colorP
                elif terrain.grid[line][col].terrain_type == 'P':
                    pygame.draw.rect(window, colorP, pygame.Rect(marge//2 + col*(size_grid//terrain.size), marge//2 + line*(size_grid//terrain.size), size_grid//terrain.size, size_grid//terrain.size))
                
                # If the cell's type is 'H', draw a rectangle with the colorH
                elif terrain.grid[line][col].terrain_type == 'H':
                    pygame.draw.rect(window, colorH, pygame.Rect(marge//2 + col*(size_grid//terrain.size), marge//2 + line*(size_grid//terrain.size), size_grid//terrain.size, size_grid//terrain.size))

        # Refresh the screen
        pygame.display.flip() 

        # Wait a bit until the next step
        pygame.time.wait(100) 

        # Calculate the state of rain and the time of rain
        rain, time_rain = calculate_rain(rain, time_rain)

        # Calculate the wind direction and the time of wind
        wind_direction, time_wind = wind(wind_values)

        # Perform a simulation step
        propagation_incendie.simulation_step(terrain, turn_count, rain, wind_direction)