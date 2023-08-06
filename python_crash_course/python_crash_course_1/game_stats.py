"""跟踪游戏的统计信息"""


class GameStats:
    def __init__(self, ai_game):
        # 初始化统计信息
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
