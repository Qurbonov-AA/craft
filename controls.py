import pygame, sys
from bullet import Bullet
from ino import Ino

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

def update(bg_color, screen, gun, ino, bullets):
     """ekranni yangilash"""
     
     
     screen.fill(bg_color)
     for bullet in bullets.sprites():
          bullet.draw()
     gun.draw()
     ino.draw(screen)
     pygame.display.flip()

def update_ino(inos):
     """uzga sayyoraliklarni qayta chizadi"""
     inos.update()


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

#uqlarni chiqib ketganini uchiramiz
def remove_bullet(bullets,inos):
     bullets.update()
     for bullet in bullets.copy():
          if bullet.rect.bottom <= 0:
               bullets.remove(bullet)
     # uq va uzga sayyoraliklar tuqnashsa uchiramiz
     collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
