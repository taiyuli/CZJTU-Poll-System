# Generated by Django 3.2.8 on 2021-10-10 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_auto_20211010_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workgroup',
            name='question1',
            field=models.CharField(blank=True, default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='workgroup',
            name='question10',
            field=models.CharField(blank=True, default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='workgroup',
            name='question2',
            field=models.CharField(blank=True, default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='workgroup',
            name='question3',
            field=models.CharField(blank=True, default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='workgroup',
            name='question4',
            field=models.CharField(blank=True, default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='workgroup',
            name='question5',
            field=models.CharField(blank=True, default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='workgroup',
            name='question6',
            field=models.CharField(blank=True, default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='workgroup',
            name='question7',
            field=models.CharField(blank=True, default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='workgroup',
            name='question8',
            field=models.CharField(blank=True, default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='workgroup',
            name='question9',
            field=models.CharField(blank=True, default='', max_length=512),
        ),
    ]
