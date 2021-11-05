from django.db import models

# Create your models here.


# 评价分组模型
class WorkGroup(models.Model):
    groupName = models.CharField(max_length=256, verbose_name='分组名称')
    groupDirector = models.CharField(max_length=256, verbose_name='分组主管')
    
    class Meta:
        verbose_name = '部门组别'
        verbose_name_plural = '部门组别'

    def __str__(self):
        return self.groupName


