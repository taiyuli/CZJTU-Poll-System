from django.db import models


from login.models import User

# Create your models here.

class LeaderModel(models.Model):
    name = models.CharField(max_length=256, verbose_name="姓名")
    voter = models.ManyToManyField(User, verbose_name="投票人")

    class Meta:
        verbose_name = '领导模型(独立)'
        verbose_name_plural = '领导模型(独立)'

    def __str__(self):
        return self.name


class LeaderPollDataModel(models.Model):
    poll_grade_choices = (
        ('优秀', '优秀'),
        ('合格', '合格'),
        ('基本合格', '基本合格'),
        ('不合格', '不合格'),
    )
    leader = models.ForeignKey(LeaderModel, on_delete=models.CASCADE, verbose_name="领导")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="评价用户")
    pollGrade = models.CharField(max_length=64, default='合格', choices=poll_grade_choices, verbose_name="评价等级")

    class Meta:
        verbose_name = '领导评价数据'
        verbose_name_plural = '领导评价数据'

    def __str__(self):
        return str(self.user) + " 对 " + str(self.leader) + " 的评价"


class DepartmentModel(models.Model):
    name = models.CharField(max_length=256, verbose_name="部门名称")
    voter = models.ManyToManyField(User, verbose_name="投票人")

    class Meta:
        verbose_name = '部门模型(独立)'
        verbose_name_plural = '部门模型(独立)'

    def __str__(self):
        return self.name


class DepartmentPollDataModel(models.Model):
    poll_grade_choices = (
        ('优秀', '优秀'),
        ('合格', '合格'),
        ('基本合格', '基本合格'),
        ('不合格', '不合格'),
    )
    department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE, verbose_name="部门")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="评价用户")
    pollGrade = models.CharField(max_length=64, default='合格', choices=poll_grade_choices, verbose_name="评价等级")

    class Meta:
        verbose_name = '部门评价数据'
        verbose_name_plural = '部门评价数据'

    def __str__(self):
        return str(self.user) + " 对 " + str(self.department) + " 的评价"