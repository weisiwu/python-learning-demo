import os
import requests
from operator import itemgetter

current_path = os.path.abspath(os.path.dirname(__file__))

# 本段代码主要是用于演示，从一个信息聚合的网站如何获取数据。

# 执行API并存储响应
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status Code: {r.status_code}")

# 处理有关每篇文章的信息
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    # 对于每篇文章，都执行一个API调用
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    response_dict = r.json()

    # 对于每篇文章，都创建一个字典
    try:
        title = response_dict["title"]
        comments = response_dict["descendants"]
        submission_dict = {
            "title": title,
            "hn_link": f"https://news.ycombinator.com/item?id={submission_id}",
            "comments": comments,
        }
    except ValueError:
        print(f"Data ValueError: {response_dict}")
    else:
        submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter("comments"), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
