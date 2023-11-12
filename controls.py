import pygame, sys
from bullet import Bullet

def events(screen, gun, bullets):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                 # ung tomonga
                 if event.key == pygame.K_d:
                      gun.mright = True
                 # chap tomonga
                 elif event.key == pygame.K_a:
                      gun.mleft = True
                # uq otish
                 elif event.key == pygame.K_SPACE:
                      new_bullet = Bullet(screen, gun)
                      bullets.add(new_bullet)
            elif event.type == pygame.KEYUP:
                 # ung tomonga
                 if event.key == pygame.K_d:
                      gun.mright = False
                 # chap tomonga
                 elif event.key == pygame.K_a:
                      gun.mleft = False

def update(bg_color, screen, gun, bullets):
     """ekranni yangilash"""
     
     
     screen.fill(bg_color)
     for bullet in bullets.sprites():
          bullet.draw()
     gun.draw()
     pygame.display.flip()


#uqlarni chiqib ketganini uchiramiz
def remove_bullet(bullets):
     bullets.update()
     for bullet in bullets.copy():
          if bullet.rect.bottom <= 0:
               bullets.remove(bullet)