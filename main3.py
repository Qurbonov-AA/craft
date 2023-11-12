# kerakli kutubxonalarni yuklaymiz
import pygame, controls
from gun import Gun 
from pygame.sprite import Group


run = True

def run():
    global run
    pygame.init()
    screen = pygame.display.set_mode((700,800))
    pygame.display.set_caption("kosmik himoyachi")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()

    while run:
        
        controls.events(screen, gun, bullets)
        gun.update()
       
        controls.update(bg_color, screen, gun, bullets)
        controls.remove_bullet(bullets)




run()