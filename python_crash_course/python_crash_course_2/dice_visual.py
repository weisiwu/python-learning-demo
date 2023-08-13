from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# 创建两个6面的骰子
die_1 = Die(6)
die_2 = Die(10)

# 投掷几次骰子,并存储结果到一个列表中
results = []

for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果,统计每个数字出现次数
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "结果", "dtick": 1}
y_axis_config = {"title": "结果频率"}
# my_layout = Layout(title="扔两个6面的筛子 1000次的结果", xaxis=x_axis_config, yaxis=y_axis_config)
my_layout = Layout(
    title="扔一个6面筛子和10面筛子 50000次的结果", xaxis=x_axis_config, yaxis=y_axis_config
)
# 绘制html
offline.plot({"data": data, "layout": my_layout}, filename="d6_d10.html")

# print(frequencies)
