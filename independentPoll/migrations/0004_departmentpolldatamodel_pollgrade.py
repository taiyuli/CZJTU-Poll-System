# Generated by Django 3.2.8 on 2021-11-05 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('independentPoll', '0003_leaderpolldatamodel_pollgrade'),
    ]

    operations = [
        migrations.AddField(
            model_name='departmentpolldatamodel',
            name='pollGrade',
            field=models.CharField(choices=[('优秀', '优秀'), ('合格', '合格'), ('基本合格', '基本合格'), ('不合格', '不合格')], default='合格', max_length=64, verbose_name='评价等级'),
        ),
    ]
