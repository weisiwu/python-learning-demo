from django.urls import path, include
from . import views

app_name = "users"

urlpatterns = [
    # 默认身份验证的UR: 如 login/logout
    path("", include("django.contrib.auth.urls")),
    # 注册页面
    path("register/", views.register, name="register"),
]
