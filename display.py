import pygame
pygame.init() 

window = pygame.display.set_mode((1000,1000))

running  = True

color = (255,255,255)

pygame.display.set_caption('Fire Hazard Sim')

while running:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False

    window.fill(color)

    image = pygame.image.load('images/sun.png')

    window.blit(image,(1,1))

    pygame.time.wait(1000)

    ticks=pygame.time.get_ticks()

    print(ticks)

    pygame.display.flip()

    