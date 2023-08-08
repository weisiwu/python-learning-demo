class Setting:
    def __init__(self):
        # 初始化游戏设置

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船
        self.ship_speed = 1.5  # 移速
        self.ship_limit = 3  # 生命

        # 子弹
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_speed = 1
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 10  # 弹匣有多少子弹（同时在屏幕内显示的子弹）

        # 外星人
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10  # 外星人舰队向下移速
        self.fleet_direction = 1  # fleet_direction为1表示右移，为-1表示左移

        # 加快游戏节奏
        self.speedup_scale = 1.1

        # 记分
        self.aline_points = 50
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # 初始化随着游戏进行而变化的变量
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1

    def increase_speed(self):
        # 提高速度设置
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.aline_points = int(self.aline_points * self.score_scale)
