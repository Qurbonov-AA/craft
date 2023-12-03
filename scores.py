from pygame import font
import pygame


class Scores():
    """o'yin natijalarini chiqaradi"""

    def __init__(self, screen, stats):
        """natijani initsalizatsiya qiladi"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (139, 195, 74)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_high_score()
    
    def image_score(self):
        """tekstni rasm kurinishiga tasvirlash"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40 
        self.score_rect.top = 20


    def image_high_score(self):
        """yuqori natijani rasm kurinishida keltiradi"""
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (0, 0, 0))
        self.hight_score_rect = self.high_score_image.get_rect()
        self.hight_score_rect.centerx = self.screen_rect.centerx
        self.hight_score_rect.top = self.screen_rect.top + 20 
    
    def draw_score(self):
        """natijani ekranga chiqarish"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.hight_score_rect)

    
