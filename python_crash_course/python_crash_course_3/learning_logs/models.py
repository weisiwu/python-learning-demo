from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    # 用户学习的主题
    # django支持哪些类型，请参考该文档
    # https://docs.djangoproject.com/en/4.2/ref/models/fields/
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # 该函数返回的值，为最终Topic模块的展示
    def __str__(self) -> str:
        return self.text


# 学到的有关具体某个主题的知识
class Entry(models.Model):
    # 设置外键，并指定在主表(Topic)数据删除触发的时候，进行级联删除
    # 这是一种一对多关系中常见的策略，比如一个主题下有多个知识点，如果这个主题被删除了
    # 那么这些知识点也就不存在了（级联删除）
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # meta类用于管理模型的额外信息，这里的设置，让 django 在需要时用 entries 表示多个
    # 条目，而不是 entrys
    class Meta:
        # plural: adj. 复数的;多元的;复数形式的;多样的
        # n. (名词或动词的)复数，复数形式
        verbose_name_plural = "entries"

    def __str__(self) -> str:
        return f"{self.text[:50]}..."

    # 该函数返回的值，为最终Topic模块的展示
    def __str__(self) -> str:
        return self.text
