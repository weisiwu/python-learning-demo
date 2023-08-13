import os
import requests
from plotly.graph_objs import Bar
from plotly import offline

current_path = os.path.abspath(os.path.dirname(__file__))
# 执行API调用并存储响应
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)

# 将API响应赋给一个变量
response_dict = r.json()

# 探索有关仓库的信息
repo_dicts = response_dict["items"]

repo_names, repo_links, stars, labels = [], [], [], []

for repo_dict in repo_dicts:
    repo_name = repo_dict["name"]
    repo_names.append(repo_name)
    repo_url = repo_dict["html_url"]
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict["stargazers_count"])
    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]
    label = f"{owner}<br />{description}"
    labels.append(label)

# 可视化
data = [
    {
        "type": "bar",
        # "x": repo_names,
        # 并不是直接替换为链接，而是替换为<a>name</a>的形式
        "x": repo_links,
        "y": stars,
        "hovertext": labels,
        # 指定条形的样式
        "marker": {
            # 指定背景色值
            "color": "rgba(60,100,150)",
            # 1.5px宽的深灰色轮廓
            "line": {"width": 1.5, "color": "rgba(25,25,25)"},
        },
        "opacity": 0.6,
    }
]
my_layout = {
    "title": "Github上最受欢迎的Python项目",
    "titlefont": {"size": 28},
    "xaxis": {
        "title": "Repository",
        "titlefont": {"size": 24},
        "tickfont": {"size": 14},
    },
    "yaxis": {"title": "Stars", "titlefont": {"size": 24}, "tickfont": {"size": 14}},
}

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename=f"{current_path}/python_repos.html")

print(f"\n stars: {stars}")
