from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# 创建一个6面的骰子
die = Die(6)

# 投掷几次骰子,并存储结果到一个列表中
results = []

for roll_num in range(100):
    result = die.roll()
    results.append(result)

# 分析结果,统计每个数字出现次数
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
x_values = list(range(1, die.num_sides))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result"}
y_axis_config = {"title": "Result Frequency"}
my_layout = Layout(title="扔一个6面的筛子 1000次的结果", xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({"data": data, "layout": my_layout}, filename="d6.html")

print(frequencies)
