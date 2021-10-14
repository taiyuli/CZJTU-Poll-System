from django.db import models

import poll

# Create your models here.

# 用户模型
class User(models.Model):
    is_poll_choices = (
        ('T', 'True'),
        ('F', 'False'),
    )
    username = models.CharField(max_length=128, unique=True, verbose_name="用户名")
    password = models.CharField(max_length=256, verbose_name="密码")
    group = models.ForeignKey(poll.models.WorkGroup, on_delete=models.CASCADE, verbose_name="组别")
    is_poll = models.CharField(max_length=128, choices=is_poll_choices, default='F', verbose_name="是否已经打分")
    poll_result = models.DecimalField(default=0 ,max_digits=5, decimal_places=2, verbose_name="打分分数")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    last_kogin_time = models.DateTimeField(auto_now=True, verbose_name="最后一次登陆时间")

    def __str__(self):
        return self.username