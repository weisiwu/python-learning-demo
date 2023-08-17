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
]
