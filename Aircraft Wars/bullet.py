import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,ai_setting,screen,ship):
        """在飞船所处的位置创建一个子弹对象"""
        super(Bullet,self).__init__()
        self.screen = screen
        #在（0.0）处 创建一个表示子弹的矩形，再设置到正确的位置
        self.rect = pygame.Rect(0,0,ai_setting.bullet_width,ai_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor
    def update(self):
        """向上移动子弹"""
        self.y -=self.speed_factor
        #更新表明的rect数量
        self.rect.y = self.y
        #更新表示子弹的rect位置
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
