import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
    # 显示得分信息
    def __init__(self, ai_game):
        self.ai_game = ai_game
        # 初始化得分相关属性
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # 显示得分的字体样式设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # 准备初始得分展示
        self.prep_score()
        # 展示最高得分
        self.prep_high_score()
        # 展示等级
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        # 将分数转为10的整数倍
        rounded_score = round(self.stats.score, -1)
        # 写法解释参考下面{:,} 把一个数展示为用,链接的数字（python仍然认为其是数字: 123,456）
        # https://realpython.com/python-formatted-output/
        score_str = "{:,}".format(rounded_score)
        # 将得分转化为图像
        score_str = str(self.stats.score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color
        )

        # 准备得分的位置属性
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        # 将分数转为10的整数倍
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        # 将得分转化为图像
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.bg_color
        )

        # 最高分放到屏幕中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        level_str = str(self.stats.level)
        # 将得分转化为图像
        self.level_image = self.font.render(
            level_str, True, self.text_color, self.settings.bg_color
        )

        # 等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def show_score(self):
        # 在屏幕上展示得分
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_ships(self):
        # 显示还剩余多少飞船
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
