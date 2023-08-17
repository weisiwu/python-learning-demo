from django.shortcuts import render

# 这个应该是python的神奇路径标志，表示当前文件夹下的 models 文件
from .models import Topic


# Create your views here.
def index(request):
    # 学习笔记主页
    # request: 请求对象
    # learning_logs/index.html: 用于创建页面的模板
    # 这个模板的实际位置在 templates 文件夹下
    return render(request, "learning_logs/index.html")


def topics(request):
    # 显示所有主题: 象棋、攀岩
    topics = Topic.objects.order_by("date_added")
    context = {"topics": topics}
    return render(request, "learning_logs/topics.html", context)
