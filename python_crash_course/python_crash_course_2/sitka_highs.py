import os
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# 获取当前文件所在位置，并读取csv文件位置
current_path = os.path.abspath(os.path.dirname(__file__))
filename_month = f"{current_path}/assets/sitka_weather_07-2018_simple.csv"
filename_year = f"{current_path}/assets/sitka_weather_2018_simple.csv"
# filename = f"{current_path}/assets/sitka_weather_2018_simple.csv"


def show_csv_plot(filename, title="2018年7月每日最高温度"):
    with open(filename) as f:
        # 与文件相关的阅读器
        reader = csv.reader(f)
        header_row = next(reader)

        # 输出位置和对应的值
        for index, column_header in enumerate(header_row):
            print(index, column_header)

        # 从文件中获取日期和最高温度、最低温度
        dates, highs, lows = [], [], []
        for row in reader:
            # 将字符串转换为时间对象
            # 第二列是日期，第六列是最高温度，第七列是最低温度
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            dates.append(current_date)
            high = int(row[5])
            highs.append(high)
            low = int(row[6])
            lows.append(low)

        # 根据最高温绘制图形
        plt.style.use("seaborn")
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c="red", alpha=0.5)
        ax.plot(dates, lows, c="blue", alpha=0.5)
        ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

        # 设置图形的格式
        ax.set_title(title, fontsize=24)
        ax.set_xlabel("", fontsize=16)
        # 日期比较长，作为x轴坐标，太长了。使用这个函数，会在日期互相压盖的时候，自动倾斜
        fig.autofmt_xdate()
        ax.set_ylabel("温度（F）", fontsize=16)
        # 设置图标x、y轴的刻度文字的样式
        # https://blog.csdn.net/chongbaikaishi/article/details/127231437
        ax.tick_params(axis="both", which="major", labelsize=16)

        plt.show()


# 月度
show_csv_plot(filename_month)
# 年度
show_csv_plot(filename_year, title="2018年每日最高温度")
