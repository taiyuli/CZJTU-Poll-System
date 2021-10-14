from django.db import models

# Create your models here.


class WorkGroup(models.Model):
    groupName = models.CharField(max_length=256, verbose_name='分组名称')
    groupDirector = models.CharField(max_length=256, verbose_name='分组主管')
    question1 = models.CharField(max_length=512, default='', blank=True)
    question2 = models.CharField(max_length=512, default='', blank=True)
    question3 = models.CharField(max_length=512, default='', blank=True)
    question4 = models.CharField(max_length=512, default='', blank=True)
    question5 = models.CharField(max_length=512, default='', blank=True)
    question6 = models.CharField(max_length=512, default='', blank=True)
    question7 = models.CharField(max_length=512, default='', blank=True)
    question8 = models.CharField(max_length=512, default='', blank=True)
    question9 = models.CharField(max_length=512, default='', blank=True)
    question10 = models.CharField(max_length=512, default='', blank=True)
    
    def __str__(self):
        return self.groupName
