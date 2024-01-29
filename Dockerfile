# 使用官方 Python 运行时作为父镜像
FROM alpine:3.19
FROM python:3.10-slim-bookworm

LABEL maintainer="weisiwu <siwu.wsw@gmail.com>"

RUN mkdir -p /etc/apk

RUN echo 'http://mirrors.tuna.tsinghua.edu.cn/alpine/v3.19/main/' > /etc/apk/repositories \
    && echo 'http://mirrors.tuna.tsinghua.edu.cn/alpine/v3.19/community/' >> /etc/apk/repositories

RUN apt-get update && \
    apt-get install -y git vim

WORKDIR /python-learning-demo

# 将当前目录内容复制到位于 /app 的容器中
COPY . /python-learning-demo

# 安装 requirements.txt 中指定的任何所需包
RUN pip install --no-cache-dir -r requirements.txt

# 保持在后台持续运行
CMD ["sleep", "infinity"]
