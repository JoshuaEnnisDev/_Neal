import pygame, sys

pygame.init()

#make a main screen
WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Running game")

test_surface = pygame.Surface((100,200))
test_surface.fill("red")

#event loop (infinite loop)
running = True

while running:
    #loop through all of the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
         
    screen.blit(test_surface, (0,0))
    
    #super important to actually put things on screen!
    pygame.display.update()
            

#broke out of the while loop
pygame.quit()