import pygame

pygame.init()

#make a main screen
WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Title of your window")
#event loop (infinite loop)
running = True

while running:
    #loop through all of the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

#broke out of the while loop
pygame.quit()