from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    # 注册新用户
    if request.method != "POST":
        # 未提交数据，创建新表单
        form = UserCreationForm()
    else:
        # POST提交数据，对数据进行处理
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录，再重新定向到主页
            login(request, new_user)
            return redirect("learning_logs:index")

    # 显示空表单或指出表单数据无效
    context = {"form": form}
    return render(request, "registration/register.html", context)
