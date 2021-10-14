# Generated by Django 3.2.8 on 2021-10-10 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_poll',
            field=models.CharField(choices=[('T', 'True'), ('F', 'false')], default='F', max_length=128, verbose_name='是否已经打分'),
        ),
    ]