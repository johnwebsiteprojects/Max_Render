# Generated by Django 3.2 on 2021-08-31 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0015_auto_20210831_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follower',
            name='follower',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='follower',
            name='user',
            field=models.CharField(max_length=200),
        ),
    ]
