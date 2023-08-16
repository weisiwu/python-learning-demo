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

这里涉及到了 2 个级别: `project` `app`

需要将刚生成的 `app` `learning_logs` 加如到之前的 `project` `learning_log` 之中

同时需要为新创建的 `learning_logs`建立表来存储对应的数据。

```shell
# makemigrations命令让django根据app设置去确定如何修改数据库，并生成对应的python脚本
python manage.py makemigrations learning_logs
# 执行上面生成的python脚本，才能最终完成对数据库的修改
python manage.py migrate
```

<img src='./images/sqlite_migrate_1.png' alt='生成修改数据库的存储进程' style='width: 80%; height: auto; text-align: center; margin-left: 10%;' />

<p align='center'>生成修改数据库的存储进程</p>

<img src='./images/sqlite_migrate_2.png' alt='应用存储进程修改表' style='width: 80%; height: auto; text-align: center; margin-left: 10%;' />

<p align='center'>应用存储进程修改表</p>

上面称呼生成的 [python 脚本](./learning_logs/migrations/0001_initial.py) 为[存储进程](https://zh.wikipedia.org/zh-hans/%E5%AD%98%E5%82%A8%E7%A8%8B%E5%BA%8F)，只是因为它和通过 `mysql dump` 倒出的存储进程功能类似。

这里可以看到，`Topic`在书中被定义为学习笔记，每次要对学习笔记这个模型进行修改的时候，都需要通过 `manage.py` 先对 `learning_logs` app 执行 `makemigrations`，然后再执行生成的脚本去修改数据。

上面是如何通过`django`去一个一个实例模型的定义，定义好的模型和数据表，需要用户管理。先行创建一个超级用户:

```shell
python manage.py createsuperuser
```

<img src='./images/admin_user.png' alt='创建管理员' style='width: 80%; height: auto; text-align: center; margin-left: 10%;' />

<p align='center'>创建管理员</p>

`admin.py`: 将注册的模型，挂载到管理网站

`models.py`: 定义所需要的数据模型

```shell
# 启动服务器
python manage.py runserver
```

打开 [管理后台](http://localhost:8000/admin)，输入用户名和密码登录

<img src='./images/admin_user.png' alt='登录界面' style='width: 80%; height: auto; text-align: center; margin-left: 10%;' />

<p align='center'>登录界面</p>

<img src='./images/backend_1.png' alt='管理后台' style='width: 80%; height: auto; text-align: center; margin-left: 10%;' />

<p align='center'>管理后台</p>

后面书中又在 [models.py](./learning_logs/models.py) 中创建了 `Entry` 类，并进行了数据创建。

```shell
python manage.py makemigrations learning_logs
python manage.py migrate
```

`django`提供了交互式终端，可以用来实时查看数据。

```shell
python manage.py shell
# 进入python shell
>>> from leaning_logs.model import Topic
>>> Topic.objects.all()
# 获取所有主题
<QuerySet [<Topic: Chess>, <Topic: Rock Climbing>]>
>>> topics = Topic.objects.all()
>>> for topic in topics:
>>>     print(topic.id, topic)
# 遍历并输出
1 Chess
2 Rock Climbing
```
