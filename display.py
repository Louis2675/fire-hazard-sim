import pygame
import generation_terrain
import propagation_incendie
import random
from parametres_terrain import TERRAIN_SIZE
from parametres_incendie import P_RAIN, T_RAIN, P_WIND, T_WIND

def calculate_rain(rain, time_rain):
    """
    Function to know if it is raining or not
    """
    nb_rand = random.random()
    if nb_rand <= P_RAIN and rain == False:
        rain = True
        time_rain = T_RAIN
    elif rain == True:
        if time_rain == 0:
            rain = False
        else :
            time_rain -= 1
    return rain, time_rain

def wind (direction, values, time):
    rand = random.random()
    if rand <= P_WIND and time == 0:
        nb_rand = random.randint(0,4)
        time = T_WIND
        return values[nb_rand], time
    elif time > 0 :
        return direction, time -1
    else :
        return direction, time

def fill_grid(terrain):
    #    The grid is displayed by looking at the cell's type and showing a particular color for this type of cell
    for line in range (terrain.size):
        for col in range (terrain.size):

            if terrain.grid[line][col].terrain_type == "C" :
                pygame.draw.rect(window, (0,0,0), pygame.Rect(marge//2 + col*(size_grid//terrain.size), marge//2 + line*(size_grid//terrain.size), size_grid//terrain.size, size_grid//terrain.size))
            
            elif terrain.grid[line][col].burning == True:
                pygame.draw.rect(window, (170 + (terrain.grid[line][col].fire_strength * 9), 10+ (terrain.grid[line][col].fire_strength * 10), 10+ (terrain.grid[line][col].fire_strength * 10)), pygame.Rect(marge//2 + col*(size_grid//terrain.size), marge//2 + line*(size_grid//terrain.size), size_grid//terrain.size, size_grid//terrain.size))
            
            elif terrain.grid[line][col].terrain_type == 'F':
                pygame.draw.rect(window, (44, 143, 6), pygame.Rect(marge//2 + col*(size_grid//terrain.size), marge//2 + line*(size_grid//terrain.size), size_grid//terrain.size, size_grid//terrain.size))
            
            elif terrain.grid[line][col].terrain_type == 'W':
                pygame.draw.rect(window, (21, 124, 214), pygame.Rect(marge//2 + col*(size_grid//terrain.size), marge//2 + line*(size_grid//terrain.size), size_grid//terrain.size, size_grid//terrain.size))
            
            elif terrain.grid[line][col].terrain_type == 'P':
                pygame.draw.rect(window, (72, 232, 9), pygame.Rect(marge//2 + col*(size_grid//terrain.size), marge//2 + line*(size_grid//terrain.size), size_grid//terrain.size, size_grid//terrain.size))
            
            elif terrain.grid[line][col].terrain_type == 'H':
                pygame.draw.rect(window, (186, 123, 13), pygame.Rect(marge//2 + col*(size_grid//terrain.size), marge//2 + line*(size_grid//terrain.size), size_grid//terrain.size, size_grid//terrain.size))

def scale_img(img, scale):
    """
    Function to scale an image
    """
    img = pygame.transform.scale(img, scale)
    return img

def rotate_img(img, wind_direction):
    """
    Function to rotate the arrow image to the right direction when the wind is blowing.
    """
    if wind_direction == 'l':
        img2 = pygame.transform.rotate(img, 180)
    elif wind_direction == 'u':
        img2 = pygame.transform.rotate(img, 90)
    elif wind_direction == 'd':
        img2 = pygame.transform.rotate(img, -90)
    else :
        img2 = img
    
    return img2

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

    rain = False
    time_rain = 0
    
    wind_values = ['n','l', 'u', 'r', 'd'] # the values are none, left, up, right, down
    wind_direction = wind_values[0]
    time_wind = 0

    thunder = False


    font1 = pygame.font.SysFont('freesanbold.ttf', 50)

    # Now we do the text boxes :
    
    # The text for the wind
    textwind = font1.render('Wind', True, (0, 0, 0))
    # The text for the thunder
    textthunder = font1.render('Thunder', True, (0, 0, 0))
    # The text for the rain
    textrain = font1.render('Rain', True, (0, 0, 0))
    # The text for the turn count
    textturn = font1.render(str(turn_count), True, (0, 0, 0))

    # create a rectangular object for the text
    textwindRect = textwind.get_rect()
    textthunderRect = textthunder.get_rect()
    textrainRect = textrain.get_rect()
    textturnRect = textturn.get_rect()

    # setting center for the title
    textwindRect.center = (size*1.13, 100)
    textthunderRect.center = (size*1.13, 300)
    textrainRect.center = (size*1.13, 500)
    textturnRect.center = (size*1.3 // 2, 20)

    # Now for the images :
    scale = (100,100)
    img_wind = scale_img(pygame.image.load("images\\arrow.jpg").convert(), scale)
    img_thunder = scale_img(pygame.image.load("images\\thunder.jpg").convert(), scale)
    img_rain = scale_img(pygame.image.load("images\\rain.jpg").convert(), scale)

    img_wind_rect = img_wind.get_rect()
    img_thunder_rect = img_thunder.get_rect()
    img_rain_rect = img_rain.get_rect()

    img_wind_rect.center = (size*1.13, 200)
    img_thunder_rect.center = (size*1.13, 400)
    img_rain_rect.center = (size*1.13, 600)


    # The colors for the different rectangles

    # Title of our window
    pygame.display.set_caption('Fire Hazard Sim')

    while running:
        
        turn_count = turn_count + 1

        textturn = font1.render(str(turn_count), True, (0, 0, 0))

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT :  
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left click
                    x, y = event.pos
                    
                    if x > marge//2 and x < size_grid + marge//2 and y > marge//2 and y < size_grid + marge//2:
                        x, y = (x- marge //2)//(size_grid//TERRAIN_SIZE), (y - marge // 2)//(size_grid//TERRAIN_SIZE)
                        coors = (y, x)
                        propagation_incendie.set_fire(terrain, coors)
            
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        window.fill((255,255,255)) # Fill the background

        # Now we put the text
        window.blit(textturn, textturnRect)
        window.blit(textwind, textwindRect)
        window.blit(textthunder, textthunderRect)
        window.blit(textrain, textrainRect)

        # Now we put the images
        if wind_direction != 'n':
            window.blit(rotate_img(img_wind,wind_direction), img_wind_rect)
        
        if thunder :
            window.blit(img_thunder, img_thunder_rect)
        
        if rain:
            window.blit(img_rain, img_rain_rect)

        fill_grid(terrain) # We fill the grid with our simulation

        pygame.display.flip() # To refresh the screen

        pygame.time.wait(70) # To make it more fluid

        rain, time_rain = calculate_rain(rain, time_rain)

        wind_direction, time_wind = wind(wind_direction,wind_values,time_wind)

        thunder = propagation_incendie.simulation_step(terrain, turn_count, rain, wind_direction)

