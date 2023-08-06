import pygame
from pygame.sprite import Sprite


"""通过sprite对子弹进行编组"""
# TODO:(wsw) 这里Sprite是做什么的？


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_game):
        # 初始化外星人
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # 加载外星人图形并初始化其rect属性
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精确水平位置
        self.x = float(self.rect.x)

    def update(self):
        # 向左或右移动外星人
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        # 外星人处于边缘，返回True
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
