import matplotlib.pyplot as plt

# 绘制点图

plt.style.use("seaborn")

fig, ax = plt.subplots()

# 单个点绘制
# ax.scatter(2, 3, s=200)

# 一系列点绘制
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# ax.scatter(x_values, y_values, s=100)

# 自动计算数据
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]
# c: color 颜色 s: size 尺寸
# 下面分别是三种颜色方式:名称，RGB，颜色映射
# ax.scatter(x_values, y_values, s=10, c="red")
# ax.scatter(x_values, y_values, s=10, c=(0, 0.8, 0))
# 颜色映射，通过将c参数设置为y值列表，并通过cmap告诉pyplot使用哪个颜色映射，将较小的y值显示为浅蓝色，较大的显示深蓝色
# 而所有的颜色映射可以在这个网站上查询:　https://matplotlib.org/
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Blues)
# 设置每个坐标轴的取值范围
ax.axis([0, 1100, 0, 1100000])

# 设置图表标题并给坐标轴加标签
ax.set_title("Square number", fontsize=24)
ax.set_xlabel("value", fontsize=24)
ax.set_ylabel("Square of values", fontsize=24)

# 设置刻度标记的大小
ax.tick_params(axis="both", which="major", labelsize=14)

plt.show()

# 自动保存图表，将 plt.show() 注释掉，然后执行savefig就可以保存图表
# plt.savefig("squares_plot.png", bbox_inches="tight")
