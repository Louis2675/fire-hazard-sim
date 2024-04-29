import pygame

# initializing pygame
pygame.font.init()

# check whether font is initialized
# or not
pygame.font.get_init()

window = pygame.display.set_mode((1000,1000))

running  = True

color = (255,255,255)

font1 = pygame.font.SysFont('freesanbold.ttf', 50)

# The title for the sim
text1 = font1.render('Welcome to the fire hazard simulator', True, (0, 0, 0))

# create a rectangular object for the title
textRect1 = text1.get_rect()

# setting center for the title
textRect1.center = (500, 100)

# We create the first image
image = pygame.image.load('images/sun.png')

imagerect = image.get_rect()

imagerect.center = (500, 500)

# Title of our window
pygame.display.set_caption('Fire Hazard Sim')

while running:

    for event in pygame.event.get():  
        if event.type == pygame.QUIT :  
            running = False
        
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_ESCAPE:
                running = False

    window.fill(color)

    window.blit(text1, textRect1)

    window.blit(image, imagerect)

    pygame.display.flip()

    