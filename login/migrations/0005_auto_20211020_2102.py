# Generated by Django 3.2.8 on 2021-10-20 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0005_auto_20211020_2102'),
        ('login', '0004_user_poll_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='poll_result',
        ),
        migrations.AlterField(
            model_name='user',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.workgroup', verbose_name='组别'),
        ),
        migrations.CreateModel(
            name='PollData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question1', models.CharField(max_length=16, verbose_name='德')),
                ('question2', models.CharField(max_length=16, verbose_name='能')),
                ('question3', models.CharField(max_length=16, verbose_name='勤')),
                ('question4', models.CharField(max_length=16, verbose_name='绩')),
                ('question5', models.CharField(max_length=16, verbose_name='廉')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.workgroup', verbose_name='组别')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.user', verbose_name='用户')),
            ],
        ),
    ]
