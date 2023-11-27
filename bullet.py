import pygame
from os import path


# uqlar klasi
class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """stvolni ustida uq yaratamiz"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(path.join('img', 'bullet.png'))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.color = (168, 230, 29)
        self.speed = 2.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)
    
    def update(self):
        """uq harakati"""

        self.y -= self.speed
        self.rect.y = self.y
    

    def draw(self):
        """uqni ekranga chizamiz"""

        self.screen.blit(self.image, self.rect)
        #pygame.draw.rect(self.screen, self.color, self.rect)