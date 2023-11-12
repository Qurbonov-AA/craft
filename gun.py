import pygame
from os import path 


# otish metodlari

class Gun():

    def __init__(self, screen):
        """pushkani yaratish"""
        
        self.screen = screen
        self.image = pygame.image.load(path.join('img', 'craft.png'))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False
    

    def draw(self):
        """kosmik kemani chizish"""

        self.screen.blit(self.image, self.rect)
    

    def update(self):
        """holatini yangilash"""

        if self.mright and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.mleft and self.rect.left > 0:
            self.rect.centerx -= 1
