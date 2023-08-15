<!-- @format -->

```shell
# 创建 ll_env 虚拟环境
python -m  venv ll_env

# 激活虚拟环境
# windows
ll_env\Scripts\activate
# mac os
source ll_env/bin/activate

# 虚拟环境激活后，会在命令行最开始展示（ll_env）,windows下类似于这个效果
# (ll_env) C:\Users\Administrator\Desktop\github\python-learning-demo\python_crash_course\python_crash_course_3>

# 在虚拟环境下，安装 django
pip install django

```

`venv` 是 `python`内部用于创建虚拟环境的模块。简单使用介绍可以参考: [什么是 Venv](https://zhuanlan.zhihu.com/p/285631652)

我是在`windows`下运行的，遇到了如下错误:

```text
ll_env\Scripts\Activate : 无法加载文件 C:\Users\Administrator\Desktop\github\python-learning-demo\python_crash_course\python_crash_course_3\ll_env\Scripts\Activate.ps1，因为在此系统上禁止运行脚本。有关详细信息，请参阅 https://go.microsoft.com/fwlink/?LinkID=135170 中的 about_Execution_Policies。
所在位置 行:1 字符: 1
+ ll_env\Scripts\Activate
+ ~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) []，PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```

查了下，是[运行脚本的权限不够](https://www.sharepointdiary.com/2014/03/fix-for-powershell-script-cannot-be-loaded-because-running-scripts-is-disabled-on-this-system.html)。启动命令行的时候记得以管理员身份运行即可。

![错误原因](./images/root_cause.png)

<p align='center'>错误原因</p>

<img src='./images/run_as_administrator.jpg' alt='以管理员身份运行' style='width: 60%; height: auto; text-align: center; margin-left: 20%;' />

<p align='center'>以管理员身份运行</p>

```shell
# 使用django创建项目
django-admin startproject learning_log .
```

<img src='./images/django_1.png' alt='django创建的文件' style='width: 40%; height: auto; text-align: center; margin-left: 30%;' />

<p align='center'>django创建的文件</p>

| 文件          | 作用                                                                                                |
| ------------- | --------------------------------------------------------------------------------------------------- |
| `settings.py` | 指定 `Django`如何与系统之间交互以及如何管理项目                                                     |
| `urls.py`     | 告诉 `Django` 应该创建哪些页面来响应浏览器的请求                                                    |
| `wsgi.py`     | 帮助 `Django` 向浏览器提供它创建的文件，是 web 服务器网关接口（web server gateway interface）的缩写 |
| `manage.py`   | 控制 `Django` 生成的网站，根据不同的子命令，选择进一步执行的任务                                    |

网站需要数据库存储数据，下面来创建数据库

```shell
python manage.py migrate
```

<img src='./images/sqlite_migrate.png' alt='创建数据库' style='width: 100%; height: auto; text-align: center; margin-left: 0%;' />

<p align='center'>创建数据库</p>

在使用 `SQLite`的新项目时，首次执行 `migrate`(迁移)命令时，`Django` 会创建新数据库

启动项目

```shell
python manage.py runserver
```

<img src='./images/runserver.png' alt='启动项目' style='width: 100%; height: auto; text-align: center; margin-left: 0%;' />

<p align='center'>启动项目</p>

<img src='./images/site_1.png' alt='网站样式' style='width: 80%; height: auto; text-align: center; margin-left: 10%;' />

<p align='center'>网站样式</p>

```shell
# 启动一个名为learning_logs的应用，这条命令会创建应用程序所需的基础设施
python manage.py startapp learning_logs
```
