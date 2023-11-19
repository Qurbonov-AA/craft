# kerakli kutubxonalarni yuklaymiz
import pygame, controls
from gun import Gun 
from pygame.sprite import Group
from ino import Ino


run = True

def run():
    global run
    pygame.init()
    screen = pygame.display.set_mode((700,800))
    pygame.display.set_caption("kosmik himoyachi")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)

    while run:
        
        controls.events(screen, gun, bullets)
        gun.update()
        bullets.update()
        controls.update(bg_color, screen, gun, inos, bullets)
        controls.remove_bullet(bullets,inos)
        controls.update_ino(inos)




run()