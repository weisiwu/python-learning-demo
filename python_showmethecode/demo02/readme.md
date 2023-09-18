<!-- @format -->

## 简述

将 0001 题生成的 200 个激活码（或者优惠券）保存到 **MySQL** 关系型数据库中。

本次依旧通过 `venv` 创建隔离环境`db`。创建成功激活虚拟环境

这里控制 `mysql` 数据库用的是 [`mysqlclient`](https://mysqlclient.readthedocs.io/)

```python
# 包虽然叫做 mysqlclient，引入的是 MySQLdb
import MySQLdb
```

运行程序

```python
python main.py
```

## 运行结果

## 参考

1. [Python 文件 I/O](http://www.runoob.com/python/python-files-io.html)
2. [python 操作 mysql 数据库](http://www.runoob.com/python/python-mysql.html)
3. [Python 操作 MySQL 数据库的三种方法](http://blog.csdn.net/oscer2016/article/details/70257024)
4. [使用 mysql 命令行连接远程数据库 host 跳转](https://segmentfault.com/q/1010000010052719)
