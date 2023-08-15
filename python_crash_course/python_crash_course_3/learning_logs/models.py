from django.db import models


# Create your models here.
class Topic(models.Model):
    # 用户学习的主题
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text
