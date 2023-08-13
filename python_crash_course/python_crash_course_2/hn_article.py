import os
import json
import requests

current_path = os.path.abspath(os.path.dirname(__file__))

# Hacker News，主要分享编程、技术方面的文章
# 执行API并存储响应
url = "https://hacker-news.firebaseio.com/v0/item/19155826.json"
r = requests.get(url)
print(f"Status Code: {r.status_code}")

# 探索数据结构
response_dict = r.json()
readable_file = f"{current_path}/readable_hn_data.json"
with open(readable_file, "w") as f:
    json.dump(response_dict, f, indent=4)
