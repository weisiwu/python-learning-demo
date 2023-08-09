import matplotlib.pyplot as plt
import numpy as np

# 绘制简单折线图

# 选择样式，使用前，先按照如下方式，确定本机可用的样式有哪些
"""
import matplotlib.pyplot as plt
plt.style.available
"""
plt.style.use("seaborn")

# plot 有绘制图表，绘制曲线的意思 pyplot 是 matplotlib下的模块
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
# subplots可以在一张图中绘制多张表， fig表示的是整张图，ax表示图中的各个表
# fig -> figure: 图、表  ax -> axes 轴、轴线
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# 设置图表标题和横纵坐标标签
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis="both", labelsize=14)

plt.show()

# 这是vscode注释里面对 pyplot 提供的demo，运行结果见 squares_2.png
# x = np.arange(0, 5, 0.1)
# y = np.sin(x)
# plt.plot(x, y)
# plt.show()
