import pygame
from os import path 

class Ino(pygame.sprite.Sprite):
    """uzga sayyoralik klasi"""

    def __init__(self, screen):
        """boshlangich holatini aniqlab olamiz"""
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(path.join("img", "ino.png"))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def draw(self):
        """uzga sayyoralikni ekranga chizish"""
        self.screen.blit(self.image, self.rect)
    

    def update(self):
        """uzga sayyoraliklarni pastga tushiradi"""
        self.y += 0.1
        self.rect.y = self.y
