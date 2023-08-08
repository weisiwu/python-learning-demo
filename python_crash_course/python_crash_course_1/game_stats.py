"""跟踪游戏的统计信息"""


class GameStats:
    def __init__(self, ai_game):
        # 初始化统计信息
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.reset_stats()

        # 游戏默认处于非激活状态
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
