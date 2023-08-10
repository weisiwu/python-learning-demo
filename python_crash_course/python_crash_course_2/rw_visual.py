import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 创建一个RandomWalk的实例
rw = RandomWalk()
rw.fill_walk()

# 将所有的点都绘制出来
plt.style.use("classic")
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
