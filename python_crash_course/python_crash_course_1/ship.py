import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """管理飞船的类"""

    def __init__(self, ai_game):
        super().__init__()
        # 初始化飞船并设置初始位置
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.moving_left = False
        self.moving_right = False

        # 加载飞船图像并获取其外形
        self.image = pygame.image.load("./images/ship.bmp")
        self.rect = self.image.get_rect()
        # 在飞船的属性x中存储小数值
        self.x = float(self.rect.x)

        # 对于每搜飞船，都将其放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

    def update(self):
        # 根据移动标志调准飞船的位置
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        # 根据self.x更新rect对象
        self.rect.x = self.x

    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        # 让飞船在底部居中
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
