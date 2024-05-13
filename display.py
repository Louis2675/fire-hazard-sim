import pygame
import generation_terrain

if __name__ == "__main__":

    terrain = generation_terrain.generate_terrain()
    # initializing pygame
    pygame.font.init()

    pygame.font.get_init()

    taille = 800
    marge = taille//10
    taille_grille = taille - marge

    window = pygame.display.set_mode((taille*1.3,taille))

    running  = True

    color = (255,255,255)

    font1 = pygame.font.SysFont('freesanbold.ttf', 50)

    # The title for the sim
    text1 = font1.render('Welcome to the fire hazard simulator', True, (0, 0, 0))

    # create a rectangular object for the title
    textRect1 = text1.get_rect()

    # setting center for the title
    textRect1.center = (taille//2, 100)

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
        for event in pygame.event.get():  
            if event.type == pygame.QUIT :  
                running = False
            
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        window.fill((255,255,255))

        #    The grid is displayed by looking at the cell's type and showing a particular color for this type of cell
        for line in range (terrain.size):
            for col in range (terrain.size):

                if terrain.grid[line][col].burning == True :
                    pygame.draw.rect(window, colorB, pygame.Rect(marge//2 + col*(taille_grille//terrain.size), marge//2 + line*(taille_grille//terrain.size), taille_grille//terrain.size, taille_grille//terrain.size))
                
                elif terrain.grid[line][col].terrain_type == 'F':
                    pygame.draw.rect(window, colorF, pygame.Rect(marge//2 + col*(taille_grille//terrain.size), marge//2 + line*(taille_grille//terrain.size), taille_grille//terrain.size, taille_grille//terrain.size))
                
                elif terrain.grid[line][col].terrain_type == 'W':
                    pygame.draw.rect(window, colorW, pygame.Rect(marge//2 + col*(taille_grille//terrain.size), marge//2 + line*(taille_grille//terrain.size), taille_grille//terrain.size, taille_grille//terrain.size))
                
                elif terrain.grid[line][col].terrain_type == 'P':
                    pygame.draw.rect(window, colorP, pygame.Rect(marge//2 + col*(taille_grille//terrain.size), marge//2 + line*(taille_grille//terrain.size), taille_grille//terrain.size, taille_grille//terrain.size))
                
                elif terrain.grid[line][col].terrain_type == 'H':
                    pygame.draw.rect(window, colorH, pygame.Rect(marge//2 + col*(taille_grille//terrain.size), marge//2 + line*(taille_grille//terrain.size), taille_grille//terrain.size, taille_grille//terrain.size))
                
                elif terrain.grid[line][col].terrain_type == 'C':
                    pygame.draw.rect(window, colorC, pygame.Rect(marge//2 + col*(taille_grille//terrain.size), marge//2 + line*(taille_grille//terrain.size), taille_grille//terrain.size, taille_grille//terrain.size))



        pygame.display.flip()
    