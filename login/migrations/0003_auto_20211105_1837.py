# Generated by Django 3.2.8 on 2021-11-05 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_rename_polldata_departmentpolldata'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departmentpolldata',
            options={'verbose_name': '部门评价数据', 'verbose_name_plural': '部门评价数据'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '评价用户', 'verbose_name_plural': '评价用户'},
        ),
    ]