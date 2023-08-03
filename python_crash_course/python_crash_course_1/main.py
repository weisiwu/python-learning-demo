# alien invasion
import os
import sys
import pygame
from settings import Setting
from ship import Ship

# TODO:(wsw) 了解下 pygame
# https://www.pygame.org/

class AlienInvasion:
    def __init__(self):
        # 初始化游戏
        pygame.init()
        self.settings = Setting()
        
        # 创建显示窗口
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
    
        # 创建飞船
        self.ship = Ship(self)
    
        # 设置背景色
        self.bg_color = self.settings.bg_color
    
    def run_game(self):
        # 开始游戏主循环
        # TODO:(wsw) 这种会不会太快？ 无间隔的刷新？
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # 每次循环都重新绘制屏幕
            self.screen.fill(self.bg_color)
            self.ship.blitme()
            
            # 让最近绘制的屏幕可见(擦去旧屏幕)
            pygame.display.flip()
    

if __name__ == '__main__':
    # 切换目录到当前子目录（python_crash_course_1）
    cwd = os.path.dirname(os.path.abspath(__file__))
    os.chdir(cwd)

    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()