# alien invasion
import os
import sys
import pygame
from time import sleep
from pygame.sprite import Sprite
from settings import Setting
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    def __init__(self):
        # 初始化游戏
        pygame.init()
        self.settings = Setting()

        # 移动标志
        self.moving_right = False
        self.moving_left = False

        # 创建显示窗口
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # 绘制飞船
        self.ship = Ship(self)

        # 绘制子弹
        self.bullets = pygame.sprite.Group()

        # 绘制外星人
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # 创建Play按钮
        self.play_button = Button(self, "Play")

        # 创建实例统计游戏信息
        self.stats = GameStats(self)

        # 创建计分板
        self.scoreboard = Scoreboard(self)

        # 设置背景色
        self.bg_color = self.settings.bg_color

    def run_game(self):
        # 开始游戏主循环
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._exit_game()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    # 按下按键
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            self._exit_game()

    # 松开按键
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    # 检查是否点击Play按钮
    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # 重置游戏统计信息
            self.stats.reset_stats()
            self.stats.game_active = True
            # 重置游戏设置
            self.settings.initialize_dynamic_settings()
            # 隐藏光学鼠标
            pygame.mouse.set_visible(False)

            # 清空余下外星人和子弹
            self.aliens.empty()
            self.bullets.empty()

            # 创建新外星人并恢复飞船位置
            self._create_fleet()
            self.ship.center_ship()

            # 重置得分 - 前面已经reset_stats
            self.scoreboard.prep_score()
            self.scoreboard.prep_level()
            self.scoreboard.prep_ships()

    def _update_bullets(self):
        self.bullets.update()

        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

        if not self.aliens:
            # 删除现有的子弹并新建一群外星人
            self.bullets.empty()
            self._create_fleet()

    def _check_bullet_alien_collisions(self):
        # 检查是否有子弹击中了外星人
        # 如果有，删除外星人和子弹
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        # 外星人被消灭完毕后，清空子弹，创建新外星人舰队
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            # 提高等级 - 整群外星人都被消灭掉
            self.stats.level += 1
            self.scoreboard.prep_level()

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.aline_points * len(aliens)
                self.scoreboard.prep_score()
                self.scoreboard.check_high_score()

    def _update_aliens(self):
        # 更新外星人群中所有外星人的位置
        self._check_fleet_edges()
        self.aliens.update()

        # 检测外星人和飞船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # 检查是否有外星人到达屏幕底端
        self._check_aliens_bottom()

    def _update_screen(self):
        # 重新绘制屏幕，并切换到新屏幕
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.scoreboard.show_score()

        # 如果游戏处于非激活态，则先绘制Play按钮
        if not self.stats.game_active:
            self.play_button.draw_button()

        # 让最近绘制的屏幕可见(擦去旧屏幕)
        pygame.display.flip()

    def _check_fleet_edges(self):
        # 有外星人到达边缘就采取相应的措施
        for aline in self.aliens.sprites():
            if aline.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        # 将整体外星人下移，并改变它们的方向
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        # 检查是否有外星人到达了屏幕底部
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # 像飞船被撞到一样处理
                self._ship_hit()
                break

    def _ship_hit(self):
        # 响应飞船被外星人控制
        # 清空余下的外星人和子弹
        self.aliens.empty()
        self.bullets.empty()

        # 创建一群外星人，并将飞船放到屏幕底端的中央
        self._create_fleet()
        self.ship.center_ship()

        # 响应飞船被外星人撞到
        if self.stats.ships_left > 0:
            # 将 ships_left 减1
            self.stats.ships_left -= 1
            self.scoreboard.prep_ships()
            # 暂停
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            # 创建子弹，并将之加入编组中
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_alien(self, aline_number, row_number):
        aline = Alien(self)
        aline_width, aline_height = aline.rect.size
        aline.x = aline_width + 2 * aline_width * aline_number
        aline.rect.x = aline.x
        aline.rect.y = aline.rect.height + 2 * aline.rect.height * row_number
        self.aliens.add(aline)

    def _create_fleet(self):
        aline = Alien(self)
        aline_width, aline_height = aline.rect.size

        available_space_x = self.settings.screen_width - (2 * aline_width)
        number_aliens_x = available_space_x // (2 * aline_width)

        ship_height = self.ship.rect.height
        available_space_y = (
            self.settings.screen_height - (3 * aline_height) - ship_height
        )
        number_aliens_y = available_space_y // (2 * aline_height)

        for row_number in range(number_aliens_y):
            for aline_number in range(number_aliens_x):
                self._create_alien(aline_number, row_number)

    def _exit_game(self):
        # https://stackoverflow.com/questions/19882415/closing-pygame-window
        pygame.display.quit()
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    # 切换目录到当前子目录（python_crash_course_1）
    cwd = os.path.dirname(os.path.abspath(__file__))
    os.chdir(cwd)

    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
