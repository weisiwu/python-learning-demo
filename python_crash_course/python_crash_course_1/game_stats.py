"""跟踪游戏的统计信息"""


class GameStats:
    def __init__(self, ai_game):
        # 初始化统计信息
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.reset_stats()

        # 游戏默认处于非激活状态
        self.game_active = False

        # 游戏分数
        self.score = 0

        # 最高得分
        self.high_score = 0

        # 等级
        self.level = 1

        # 剩余飞船数量
        self.ships_left = self.settings.ship_limit

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
