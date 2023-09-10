<!-- @format -->

## 简述

将 0001 题生成的 200 个激活码（或者优惠券）保存到 **MySQL** 关系型数据库中。

需要引入之前创建的函数。因为不在统一目录下，可用以下方式（任选其一）：

1、将需要引用的目录添加到`python`路径下

```python
import sys
sys.path.append('/path/to/directory')

from main import ActivateCode
```

2、相对导入
使用点表示相对路径

```python
# 使用点表示路径
from ..demo01.main import ActivateCode
```

3、使用绝对路径导入

```python
# 使用绝对路径
from /path/to/directory/demo01.main import ActivateCode
```

同之前相同，创建虚拟环境 `db`

这里控制 `mysql` 数据库用的是 [`mysqlclient`](https://mysqlclient.readthedocs.io/)

```python
# 包虽然叫做 mysqlclient，引入的是 MySQLdb
import MySQLdb
```

## 运行结果

## 参考

1. [Python 文件 I/O](http://www.runoob.com/python/python-files-io.html)
2. [python 操作 mysql 数据库](http://www.runoob.com/python/python-mysql.html)
3. [Python 操作 MySQL 数据库的三种方法](http://blog.csdn.net/oscer2016/article/details/70257024)
4. [使用 mysql 命令行连接远程数据库 host 跳转](https://segmentfault.com/q/1010000010052719)
