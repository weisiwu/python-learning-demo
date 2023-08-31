<!-- @format -->

# 项目介绍

**[Python 练习册，每天一个小程序][pythond-examples]** 我的实现。

下面是各题目描述和在线 demo 链接。

[**第 0000 题：**](demo00)

> 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
> 类似于图中效果

![头像](./images/000_demo.png)

[**第 0001 题：**](demo01)

> 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用**生成激活码**（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

[**第 0002 题:**](demo02)

> 将 0001 题生成的 200 个激活码（或者优惠券）保存到 **MySQL** 关系型数据库中。

[**第 0003 题：**](demo03)

> 将 0001 题生成的 200 个激活码（或者优惠券）保存到 **Redis** 非关系型数据库中。

[**第 0004 题：**](demo04)

> 任一个英文的纯文本文件，统计其中的单词出现的个数。

**第 0005 题：**

> 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

**第 0006 题：**

> 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

**第 0007 题：**

> 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

**第 0008 题：**

> 一个 HTML 文件，找出里面的**正文**。

**第 0009 题：**

> 一个 HTML 文件，找出里面的**链接**。

**第 0010 题：**

> 使用 Python 生成类似于下图中的**字母验证码图片**

![字母验证码](./images/010_demo.jpg)

- [阅读资料](http://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python)

**第 0011 题：**

> 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

```text
北京
程序员
公务员
领导
牛比
牛逼
你娘
你妈
love
sex
jiangge
```

**第 0012 题：**

> 敏感词文本文件 filtered_words.txt，里面的内容 和 0011 题一样，当用户输入敏感词语，则用 星号 \* 替换，例如当用户输入「北京是个好城市」，则变成「\*\*是个好城市」。

**第 0013 题：**

> 用 Python 写一个爬图片的程序，爬 [这个链接里的日本妹子图片 :-)](http://tieba.baidu.com/p/2166231880)

- [参考代码](http://www.v2ex.com/t/61686 '参考代码')

**第 0014 题：**

> 纯文本文件 student.txt 为学生信息, 里面的内容（包括花括号）如下所示：

```text
{
  "1":["张三",150,120,100],
  "2":["李四",90,99,95],
  "3":["王五",60,66,68]
}
```

> 请将上述内容写到 student.xls 文件中，如下图所示：

![student.xls](./images/014_demo.jpg)

- [阅读资料](http://www.cnblogs.com/skynet/archive/2013/05/06/3063245.html) 腾讯游戏开发 XML 和 Excel 内容相互转换

**第 0015 题：**

> 纯文本文件 city.txt 为城市信息, 里面的内容（包括花括号）如下所示：

```text
{
  "1" : "上海",
  "2" : "北京",
  "3" : "成都"
}
```

> 请将上述内容写到 city.xls 文件中，如下图所示：

![city.xls](./images/015_demo.png)

**第 0016 题：**

> 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

```text
[
  [1, 82, 65535],
  [20, 90, 13],
  [26, 809, 1024]
]
```

> 请将上述内容写到 numbers.xls 文件中，如下图所示：

![numbers.xls](./images/015_demo_1.png)

**第 0017 题：**

> 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如下所示：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<root>
<students>
<!-- 学生信息表 "id" : [名字, 数学, 语文, 英文] -->
{
  "1" : ["张三", 150, 120, 100],
  "2" : ["李四", 90, 99, 95],
  "3" : ["王五", 60, 66, 68]
}
</students>
</root>
```

**第 0018 题：**

> 将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中，如下所示：

```xml
<?xmlversion="1.0" encoding="UTF-8"?>
<root>
<cities>
<!-- 城市信息 -->
{
  "1" : "上海",
  "2" : "北京",
  "3" : "成都"
}
</cities>
</root>
```

**第 0019 题：**

> 将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中，如下所示：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<root>
<numbers>
<!-- 数字信息 -->

[
  [1, 82, 65535],
  [20, 90, 13],
  [26, 809, 1024]
]

</numbers>
</root>
```

**第 0020 题：**

> [登陆中国联通网上营业厅](http://iservice.10010.com/index_.html) 后选择「自助服务」 --> 「详单查询」，然后选择你要查询的时间段，点击「查询」按钮，查询结果页面的最下方，点击「导出」，就会生成类似于 2014 年 10 月 01 日～ 2014 年 10 月 31 日通话详单.xls 文件。写代码，对每月通话时间做个统计。

**第 0021 题：**

> 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。

- 阅读资料 [用户密码的存储与 Python 示例](http://zhuoqiang.me/password-storage-and-python-example.html)

- 阅读资料 [Hashing Strings with Python](http://www.pythoncentral.io/hashing-strings-with-python/)

- 阅读资料 [Python's safest method to store and retrieve passwords from a database](http://stackoverflow.com/questions/2572099/pythons-safest-method-to-store-and-retrieve-passwords-from-a-database)

**第 0022 题：**

> iPhone 6、iPhone 6 Plus 早已上市开卖。请查看你写得 第 0005 题的代码是否可以复用。

**第 0023 题：**

> 使用 Python 的 Web 框架，做一个 Web 版本 留言簿 应用。

[阅读资料：Python 有哪些 Web 框架](http://v2ex.com/t/151643#reply53)

- ![留言簿参考](./images/023_demo.jpg)

**第 0024 题：**

> 使用 Python 的 Web 框架，做一个 Web 版本 TodoList 应用。

- ![SpringSide 版TodoList](./images/024_demo.jpg)

**第 0025 题：**

> 使用 Python 实现：对着电脑吼一声,自动打开浏览器中的默认网站。
>
> 例如，对着笔记本电脑吼一声“百度”，浏览器自动打开百度首页。
>
> 关键字：Speech to Text
>
> 参考思路：  
> 1：获取电脑录音-->WAV 文件  
> python record wav
>
> 2：录音文件-->文本  
> STT: Speech to Text  
> STT API Google API
>
> 3:文本-->电脑命令

## 运行环境

1. [python 3.12-rc-slim](https://hub.docker.com/layers/library/python/3.12-rc-slim/images/sha256-9393b50e405b1717c79ea433339cb19b2b10d81d3b8dad18576b5b1818ab2853?context=explore)

另外，为后续交流学习之便，同样将所有实现的代码用 docker 打包，便于下载运行。

[pythond-examples]: https://github.com/Yixiaohan/show-me-the-code
[demo00]: ./python_showmethecode/demo00/readme.md
[demo01]: ./python_showmethecode/demo01/readme.md
[demo02]: ./python_showmethecode/demo02/readme.md
[demo03]: ./python_showmethecode/demo03/readme.md
[demo04]: ./python_showmethecode/demo04/readme.md
[demo05]: ./python_showmethecode/demo05/readme.md
[demo06]: ./python_showmethecode/demo06/readme.md
[demo07]: ./python_showmethecode/demo07/readme.md
[demo08]: ./python_showmethecode/demo08/readme.md
[demo09]: ./python_showmethecode/demo09/readme.md
[demo10]: ./python_showmethecode/demo10/readme.md
[demo11]: ./python_showmethecode/demo11/readme.md
[demo12]: ./python_showmethecode/demo12/readme.md
[demo13]: ./python_showmethecode/demo13/readme.md
[demo14]: ./python_showmethecode/demo14/readme.md
[demo15]: ./python_showmethecode/demo15/readme.md
[demo16]: ./python_showmethecode/demo16/readme.md
[demo17]: ./python_showmethecode/demo17/readme.md
[demo18]: ./python_showmethecode/demo18/readme.md
[demo19]: ./python_showmethecode/demo19/readme.md
[demo20]: ./python_showmethecode/demo20/readme.md
[demo21]: ./python_showmethecode/demo21/readme.md
[demo22]: ./python_showmethecode/demo22/readme.md
[demo23]: ./python_showmethecode/demo23/readme.md
[demo24]: ./python_showmethecode/demo24/readme.md
[demo25]: ./python_showmethecode/demo25/readme.md