# 定义 APP leading_logs 的URL
from django.urls import path

# 从上级页面引入视图
from . import views

app_name = "learning_logs"
urlpatterns = [
    # 主页
    # 1参: 路径
    # 2参: 匹配路径后，调用的函数
    # 3参: 这个URL匹配规则，叫啥
    path("", views.index, name="index"),
    path("topics/", views.topics, name="topics"),
    # 特定主题的详细页面
    path("topics/<int:topic_id>/", views.topic, name="topic"),
    # 用于添加新主题的页面
    path("new_topic/", views.new_topic, name="new_topic"),
    # 用于添加新条目的页面
    path("new_entry/<int:topic_id>/", views.new_entry, name="new_entry"),
    # 用于编辑条目的页面
    path("edit_entry/<int:entry_id>/", views.edit_entry, name="edit_entry"),
]
