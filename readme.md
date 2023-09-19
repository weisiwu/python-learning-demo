<!-- @format -->

## 简介

在学习 python 过程中，记录用于练手的项目。主要分为两部分

### **1、《python 编程：从入门到实践》 项目章节**

1. **[ 外星人入侵](./python_crash_course/python_crash_course_1/readme.md)**

2. **[数据可视化](./python_crash_course/python_crash_course_2/readme.md)**

3. **[web 应用程序](./python_crash_course/python_crash_course_3/readme.md)**

### **2、[Python 练习册，每天一个小程序][pythond-examples]个人实现**

Python 练习册，每天一个小程序。

不会出现诸如「打印九九乘法表」、「打印水仙花」之类的题目

> Talk is cheap. Show me the code.--Linus Torvalds

## 运行环境

```shell
# 拉取镜像
docker pull wei123098/python-learning-demo

# 查看本地所有镜像
docker images ls

# 运行镜像，生成容器
docker run --name learningPython alpine

# 以shell形式进入运行中的容器
docker exec -it a1bd26164e23 /bin/sh

# 或者直接链接到容器中
docker attach a1bd26164e23

docker commit silly_engelbart python-learning-demo:0.0.1
```

另外，为后续交流学习之便，同样将所有实现的代码用 docker 打包，便于下载运行。
[python-learning-demo](https://hub.docker.com/repository/docker/wei123098/python-learning-demo)

[pythond-examples]: https://github.com/Yixiaohan/show-me-the-code
[q0]: ./python_showmethecode/demo00/readme.md
[q1]: ./python_showmethecode/demo01/readme.md
[q2]: ./python_showmethecode/demo02/readme.md
