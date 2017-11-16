"""
following question fetch sample
https://www.zhihu.com/api/v4/members/wei-si-wu/following-questions?
include=data[*].created,answer_count,follower_count,author
&offset=0
&limit=20
"""
import urllib
from urllib import request as fetch

# 拼接请求地址
url_base = 'https://www.zhihu.com/api/v4/members/wei-si-wu/following-questions?'
url_type = 'include=data[*].created,answer_count,follower_count,author'
url_arg_offset = '&offset=0'
url_arg_limit = '&limit=20'

fetch_url = url_base + url_type + url_arg_offset + url_arg_limit

req = fetch.Request(url=fetch_url, method='get')

with fetch.urlopen(req) as f:
  pass

print(f.status)