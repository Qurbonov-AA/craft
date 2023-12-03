import pygame
from os import path 


# otish metodlari

class Gun():

    def __init__(self, screen):
        """pushkani yaratish"""
        
        self.screen = screen
        self.image = pygame.image.load(path.join('img', 'craft.png'))
        self.life_image = pygame.image.load(path.join('img', 'heart.png'))
        self.rect = self.image.get_rect()
        self.life_rect = self.life_image.get_rect()
        self.screen_rect = screen.get_rect()
        self.life_screen = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.life_rect.left = self.screen_rect.left
        self.life_rect.top   = self.screen_rect.top + 20
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    

    def draw(self):
        """kosmik kemani chizish"""

        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.life_image, self.life_rect)
    

    def update(self):
        """holatini yangilash"""

        if self.mright and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.mleft and self.rect.left > 0:
            self.rect.centerx -= 1


    def create_gun(self):
        """pushkani qayta yarataish"""
        self.center = self.screen_rect.center
        