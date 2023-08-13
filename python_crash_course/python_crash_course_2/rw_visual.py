import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 只要程序处于活动状态，就不断模拟随机漫步
while True:
    # 创建一个RandomWalk的实例
    rw = RandomWalk(50_000)  # 增多点的数量
    rw.fill_walk()
    # 将所有的点都绘制出来
    plt.style.use("classic")
    # 调整输出图片尺寸，matplotlib假定屏幕分辨率为100像素
    # 也可通过指定dpi，来调整输出图片尺寸
    fig, ax = plt.subplots(figsize=(15, 9), dpi=96)
    # 经过测试，如果是双屏幕，那么设置为100,100。生成的图片会铺满两个屏幕
    # fig, ax = plt.subplots(figsize=(100, 100))
    ax.scatter(rw.x_values, rw.y_values, s=15)
    point_numbers = range(rw.num_points)
    # 给点着色
    ax.scatter(
        rw.x_values,
        rw.y_values,
        c=point_numbers,
        cmap=plt.cm.Blues,
        edgecolors="none",
        # s=15,
        # 调小点的尺寸
        s=1,
    )
    # 突出起点和终点
    # 起点
    ax.scatter(0, 0, c="green", edgecolors="none", s=100)
    # 终点
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)
    # 隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n):")
    if keep_running == "n":
        break
