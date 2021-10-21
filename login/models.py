from django.db import models

from poll.models import WorkGroup

# Create your models here.

# 用户模型
class User(models.Model):
    is_poll_choices = (
        ('T', 'True'),
        ('F', 'False'),
    )
    username = models.CharField(max_length=128, unique=True, verbose_name="用户名")
    password = models.CharField(max_length=256, verbose_name="密码")
    group = models.ForeignKey(WorkGroup, on_delete=models.CASCADE, verbose_name="组别")
    is_poll = models.CharField(max_length=128, choices=is_poll_choices, default='F', verbose_name="是否已经打分")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    last_kogin_time = models.DateTimeField(auto_now=True, verbose_name="最后一次登陆时间")

    def __str__(self):
        return self.username


# 评价数据模型
class PollData(models.Model):
    poll_grade_choices = (
        ('优秀', '优秀'),
        ('合格', '合格'),
        ('基本合格', '基本合格'),
        ('不合格', '不合格'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    group = models.ForeignKey(WorkGroup, on_delete=models.CASCADE, verbose_name='组别')
    question1 = models.CharField(max_length=16, choices=poll_grade_choices, verbose_name='德')
    question2 = models.CharField(max_length=16, choices=poll_grade_choices, verbose_name='能')
    question3 = models.CharField(max_length=16, choices=poll_grade_choices, verbose_name='勤')
    question4 = models.CharField(max_length=16, choices=poll_grade_choices, verbose_name='绩')
    question5 = models.CharField(max_length=16, choices=poll_grade_choices, verbose_name='廉')
    reason = models.CharField(max_length=2048, default='', blank=True, verbose_name='评价理由')

    def __str__(self):
        return str(self.group) + "----" + str(self.user) + " 的评价"