import pygame, sys


def events(gun):
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
            elif event.type == pygame.KEYUP:
                 # ung tomonga
                 if event.key == pygame.K_d:
                      gun.mright = False
                 # chap tomonga
                 elif event.key == pygame.K_a:
                      gun.mleft = False