<!-- @format -->

# 项目介绍

[《python 编程：入门到实践》](https://www.ituring.com.cn/book/2784)第二版 第二部分项目，项目 1 射击小游戏：**外星人入侵**(游戏基于 [pygame](https://www.pygame.org/) 实现)。各章节如下

**第 12 章 武装飞船**
使用 `pygame` 创建游戏窗口，调试窗口样式，创建飞船，并监听用户键盘输入时间，控制飞船移动、发射子弹，并对子弹进行编组。

**第 13 章 外星人**
创建外星人舰队，设置移动方式并编组。设置子弹和外星人碰撞的效果：击杀外星人，并设置游戏结束条件： 是否全部击杀。

**第 14 章 记分**
在游戏界面上，设置更多操作按钮，响应用户操作。设置得分规则，并记录得分。存储得分最高记录。展示得分、历史最高分，以及飞船剩余数（生命数）。

# 运行

1、 安装 pygame

```shell
python -m pip install --user pygame
# 将依赖存储到文件中
pip freeze > requirements.txt
```

2、运行 alien_invasion.py

```shell
python aline_invasion.py
```

## 主要文件

当前目录下，各代码文件说明如下:

`alien_invasion.py` :

`alien.py` :

`bullet.py` :

`button.py` :

`game_stats.py` :

`scoreboard.py` :

`settings.py` :

`ship.py` :

# 效果

![初始化](./images/效果.png)

![得分](./images/效果2.png)

# 扩展

1.  添加游戏音乐: pygame.mixer
2.  外星人也可以向飞船射击
3.  飞船添加盾牌,格挡子弹
4.  按下 P 键开始游戏
5.  创建一组按钮，可以选择起始难度
6.  最高分保存在本地，方便下次运行继续读取
7.  保证游戏前几轮能够过,游戏难度逐渐上升

# Todolist

1. 按 Q 退出仍然有问题
2. 这里 Sprite 是做什么的？
3. 了解下 [pygame](https://www.pygame.org/)
