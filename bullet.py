import pygame


# uqlar klasi
class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """stvolni ustida uq yaratamiz"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 4, 15)
        self.color = (168, 230, 29)
        self.speed = 1.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)
    
    def update(self):
        """uq harakati"""

        self.y -= self.speed
        self.rect.y = self.y
    

    def draw(self):
        """uqni ekranga chizamiz"""

        pygame.draw.rect(self.screen, self.color, self.rect)