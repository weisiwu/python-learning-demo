import pygame
from pygame.sprite import Sprite


"""通过sprite对子弹进行编组"""


class Bullet(Sprite):
    """管理飞船所发射的子弹"""

    def __init__(self, ai_game):
        # 在飞船当前位置创建一个子弹
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # 在(0,0)处创建一个表示子弹的矩形，在设置正确的位置
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        self.rect.midtop = ai_game.ship.rect.midtop

        # 存储用小数点表示的子弹位置
        self.y = float(self.rect.y)

    def update(self):
        # 向上移动子弹
        self.y -= self.settings.bullet_speed
        # 根据self.x更新rect对象
        self.rect.y = self.y

    def draw_bullet(self):
        # 绘制子弹
        pygame.draw.rect(self.screen, self.color, self.rect)
