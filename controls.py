import pygame, sys
from bullet import Bullet
from ino import Ino
import time

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


#pushkani uchirish
def gun_kill(stats, screen, gun, inos, bullets):
     stats.guns_left -= 1
     inos.empty()
     bullets.empty()
     create_army(screen, inos)
     gun.create_gun()
     time.sleep(2)



def update(bg_color, screen, gun, ino, bullets):
     """ekranni yangilash"""
     
     
     screen.fill(bg_color)
     for bullet in bullets.sprites():
          bullet.draw()
     gun.draw()
     ino.draw(screen)
     pygame.display.flip()

def update_ino(inos, stats, screen, gun, bullets):
     """uzga sayyoraliklarni qayta chizadi"""
     inos.update()
     if pygame.sprite.spritecollideany(gun, inos):
          gun_kill(stats, screen, gun, inos, bullets)
     inos_check(stats, screen, gun, inos, bullets)


def create_army(screen, inos):
     """armiya yaratish"""
     ino = Ino(screen)
     ino_width = ino.rect.width
     number_ino_x = int( (700 - 2 * ino_width) / ino_width )
     ino_height = ino.rect.height
     number_ino_y = int( (800 - 100 - 2 * ino_height) / ino_height  )

     for row_number in range(number_ino_y - 1 ):

          for ino_num in range(number_ino_x):
               ino = Ino(screen)
               ino.x = ino_width + ino_width * ino_num
               ino.y = ino_height + ino_height * row_number 
               ino.rect.x = ino.x
               ino.rect.y = ino.rect.height + ino.rect.height * row_number
               inos.add(ino)


def inos_check(stats, screen, gun, inos, bullets):
     """uzga sayyoraliklar ekranni pastki qismiga tegsa"""

     screen_rect = screen.get_rect()
     for ino in inos.sprites():
          if ino.rect.bottom >= screen_rect.bottom:
               gun_kill(stats, screen, gun, inos, bullets)
               break



#uqlarni chiqib ketganini uchiramiz
def remove_bullet(screen, bullets,inos):
     bullets.update()
     for bullet in bullets.copy():
          if bullet.rect.bottom <= 0:
               bullets.remove(bullet)
     # uq va uzga sayyoraliklar tuqnashsa uchiramiz
     collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
     if len(inos) == 0:
          bullets.empty()
          create_army(screen, inos)
