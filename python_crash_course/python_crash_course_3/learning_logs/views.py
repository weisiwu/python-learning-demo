from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

# 这个应该是python的神奇路径标志，表示当前文件夹下的 models 文件
from .models import Topic
from .forms import TopicForm, EntryForm, Entry


# Create your views here.
def index(request):
    # 学习笔记主页
    # request: 请求对象
    # learning_logs/index.html: 用于创建页面的模板
    # 这个模板的实际位置在 templates 文件夹下
    return render(request, "learning_logs/index.html")


@login_required
def topics(request):
    # 显示所有主题: 象棋、攀岩
    topics = Topic.objects.filter(owner=request.user).order_by("date_added")
    context = {"topics": topics}
    return render(request, "learning_logs/topics.html", context)


# 作为views，实际上。返回具体视图和模板，并组装数据。
# 在运行topic函数前，先下运行 login_required
@login_required
def topic(request, topic_id):
    # 显示单个主题以及所有的条目
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        # raise 抛出异常
        raise Http404
    # date_added前面的-号，表示按降序排列
    entries = topic.entry_set.order_by("date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "learning_logs/topic.html", context)


@login_required
def new_topic(request):
    # 添加新主题
    if request.method != "POST":
        # 未提交数据，创建新表单
        form = TopicForm()
    else:
        # POST提交数据，对数据进行处理
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect("learning_logs:topics")

    # 显示空表单或指出表单数据无效
    context = {"form": form}
    return render(request, "learning_logs/new_topic.html", context)


@login_required
def new_entry(request, topic_id):
    # 在特定主题中添加新条目
    topic = Topic.objects.get(id=topic_id)
    if request.method != "POST":
        # 未提交数据，创建新表单
        form = EntryForm()
    else:
        # POST提交数据，对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            # commit = False 表示产生结果，但是不提交到数据库
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            # 再保存到数据库
            new_entry.save()
            return redirect("learning_logs:topic", topic_id=topic_id)

    # 显示空表单或指出表单数据无效
    context = {"topic": topic, "form": form}
    # 1参:要重定向的视图 2参:带往视图的参数
    return render(request, "learning_logs/new_entry.html", context)


@login_required
def edit_entry(request, entry_id):
    # 编辑既有条目
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if topic.owner != request.user:
        # raise 抛出异常
        raise Http404

    if request.method != "POST":
        # 初次请求
        form = EntryForm(instance=entry)
    else:
        # POST提交数据，处理数据
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("learnng_logs:topic", topic_id=topic.id)

    # 显示空表单或指出表单数据无效
    context = {"entry": entry, "topic": topic, "form": form}
    # 1参:要重定向的视图 2参:带往视图的参数
    return render(request, "learning_logs/edit_entry.html", context)
