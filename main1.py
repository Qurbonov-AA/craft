# kerakli kutubxonalarni yuklaymiz
import pygame
import sys
from gun import Gun 


run = True

def run():
    global run
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("kosmik himoyachi")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
        
        screen.fill(bg_color)
        gun.draw()
        pygame.display.flip()




run()