import os
import json
import plotly.express as px
import pandas as pd

# 探索数据结构
current_path = os.path.abspath(os.path.dirname(__file__))
# 全部折叠成一行的json文件
filename = f"{current_path}/assets/eq_data_1_day_m1.json"
filename_month = f"{current_path}/assets/eq_data_30_day_m1.json"


def show_json_file(filename):
    with open(filename) as f:
        all_eq_data = json.load(f)

    # 这些被注释掉的代码，是从json文件中读取数据，并写到另外一个文件中
    # # 重新写到文件中，格式化
    # readable_file = f"{current_path}/assets/readable_eq_data.json"
    # with open(readable_file, "w") as f:
    #     json.dump(all_eq_data, f, indent=4)

    all_eq_dicts = all_eq_data["features"]

    mags, titles, lons, lats = [], [], [], []
    for eq_dict in all_eq_dicts:
        mag = eq_dict["properties"]["mag"]
        title = eq_dict["properties"]["title"]
        lon = eq_dict["geometry"]["coordinates"][0]
        lat = eq_dict["geometry"]["coordinates"][1]
        mags.append(mag)
        titles.append(title)
        lons.append(lon)
        lats.append(lat)

    data = pd.DataFrame(
        data=zip(lons, lats, titles, mags), columns=["经度", "纬度", "位置", "震级"]
    )
    data.head()

    fig = px.scatter(
        data,
        x="经度",
        y="纬度",
        labels={"x": "经度", "y": "纬度"},
        range_x=[-200, 200],
        range_y=[-90, 90],
        width=800,
        height=800,
        size="震级",
        size_max=10,
        title="全球地震散点图",
        color="震级",
        hover_name="位置",
    )
    # 会生成一个本地server，并打开网页
    fig.write_html(f"{current_path}/gloabl_earthquakes.html")
    fig.show()


show_json_file(filename)

show_json_file(filename_month)
