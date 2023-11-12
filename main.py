# kerakli kutubxonalarni yuklaymiz
import pygame, controls
from gun import Gun 


run = True

def run():
    global run
    pygame.init()
    screen = pygame.display.set_mode((700,800))
    pygame.display.set_caption("kosmik himoyachi")
    bg_color = (0, 0, 0)
    gun = Gun(screen)

    while run:
        
        controls.events(gun)
        gun.update()
        screen.fill(bg_color)
        gun.draw()
        pygame.display.flip()




run()