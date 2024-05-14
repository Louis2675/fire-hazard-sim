import pygame
import generation_terrain
import propagation_incendie
from parametres_terrain import TERRAIN_SIZE

if __name__ == "__main__":
    # We start by initialising everything we need

    terrain = generation_terrain.generate_terrain()
    # initializing pygame
    pygame.font.init()

#    pygame.font.get_init()

    # Our main variables
    size = 800 # Hight of the screen, width is 1.3 times the height
    marge = size//10 # The size of the sides of our simulation
    size_grid = size - marge # The size of our 

    turn_count = 0 # The turn count for the simulation

    window = pygame.display.set_mode((size*1.3, size)) # Initialise the window

    running  = True # To start pygame

    color = (255,255,255) # Color of the backgrund

    """

    font1 = pygame.font.SysFont('freesanbold.ttf', 50)

    # The title for the sim
    text1 = font1.render('Welcome to the fire hazard simulator', True, (0, 0, 0))

    # create a rectangular object for the title
    textRect1 = text1.get_rect()

    # setting center for the title
    textRect1.center = (taille//2, 100)
    """

    # The colors for the different rectangles

    colorW = (21, 124, 214)
    colorP = (72, 232, 9)
    colorF = (44, 143, 6)
    colorH = (186, 123, 13)
    colorB = (232, 24, 9)
    colorC = (0,0,0)

    # Title of our window
    pygame.display.set_caption('Fire Hazard Sim')

    while running:
        
        """
        """
        turn_count = turn_count + 1

        for event in pygame.event.get():  
            if event.type == pygame.QUIT :  
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]: # Left click
                    x, y = event.pos
                    print(x,y)
                    if x > size and x < size_grid + marge and y > marge and y < size_grid + marge:
                        print(x,y)
                        propagation_incendie.set_fire(terrain, (x,y))
            
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        window.fill((255,255,255))

        #    The grid is displayed by looking at the cell's type and showing a particular color for this type of cell
        for line in range (terrain.size):
            for col in range (terrain.size):

                if terrain.grid[line][col].terrain_type == "C" :
                    pygame.draw.rect(window, colorC, pygame.Rect(marge//2 + col*(size_grid//terrain.size), marge//2 + line*(size_grid//terrain.size), size_grid//terrain.size, size_grid//terrain.size))
                
                elif terrain.grid[line][col].burning == True:
                    pygame.draw.rect(window, colorB, pygame.Rect(marge//2 + col*(size_grid//terrain.size), marge//2 + line*(size_grid//terrain.size), size_grid//terrain.size, size_grid//terrain.size))
                
                elif terrain.grid[line][col].terrain_type == 'F':
                    pygame.draw.rect(window, colorF, pygame.Rect(marge//2 + col*(size_grid//terrain.size), marge//2 + line*(size_grid//terrain.size), size_grid//terrain.size, size_grid//terrain.size))
                
                elif terrain.grid[line][col].terrain_type == 'W':
                    pygame.draw.rect(window, colorW, pygame.Rect(marge//2 + col*(size_grid//terrain.size), marge//2 + line*(size_grid//terrain.size), size_grid//terrain.size, size_grid//terrain.size))
                
                elif terrain.grid[line][col].terrain_type == 'P':
                    pygame.draw.rect(window, colorP, pygame.Rect(marge//2 + col*(size_grid//terrain.size), marge//2 + line*(size_grid//terrain.size), size_grid//terrain.size, size_grid//terrain.size))
                
                elif terrain.grid[line][col].terrain_type == 'H':
                    pygame.draw.rect(window, colorH, pygame.Rect(marge//2 + col*(size_grid//terrain.size), marge//2 + line*(size_grid//terrain.size), size_grid//terrain.size, size_grid//terrain.size))



        pygame.display.flip() # To refresh the screen

        pygame.time.wait(500) # We wait a bit until the next step

        propagation_incendie.simulation_step(terrain, turn_count)
    