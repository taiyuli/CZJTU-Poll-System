# Generated by Django 3.2.8 on 2021-11-05 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20211105_1837'),
        ('independentPoll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='部门名称')),
                ('voter', models.ManyToManyField(to='login.User', verbose_name='投票人')),
            ],
            options={
                'verbose_name': '部门模型(独立)',
                'verbose_name_plural': '部门模型(独立)',
            },
        ),
        migrations.AlterModelOptions(
            name='leadermodel',
            options={'verbose_name': '领导模型(独立)', 'verbose_name_plural': '领导模型(独立)'},
        ),
        migrations.CreateModel(
            name='LeaderPollDataModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='independentPoll.leadermodel', verbose_name='领导')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.user', verbose_name='评价用户')),
            ],
            options={
                'verbose_name': '领导评价数据',
                'verbose_name_plural': '领导评价数据',
            },
        ),
        migrations.CreateModel(
            name='DepartmentPollDataModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='independentPoll.departmentmodel', verbose_name='部门')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.user', verbose_name='评价用户')),
            ],
            options={
                'verbose_name': '部门评价数据',
                'verbose_name_plural': '部门评价数据',
            },
        ),
    ]
