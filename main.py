# kerakli kutubxonalarni yuklaymiz
import pygame, controls
from gun import Gun 
from pygame.sprite import Group
from ino import Ino
from stats import Stats
from scores import Scores


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
    stats = Stats()
    sc    = Scores(screen, stats)
    while run:
        
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update()
            bullets.update()
            controls.update(bg_color, screen, stats, sc, gun, inos, bullets)        
            controls.remove_bullet(screen, stats, sc, bullets,inos)
            controls.update_ino(inos, stats, screen, gun,  bullets)

 


run()  