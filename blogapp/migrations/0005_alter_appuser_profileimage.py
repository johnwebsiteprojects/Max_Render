# Generated by Django 3.2 on 2021-08-11 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_auto_20210809_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='profileImage',
            field=models.ImageField(blank=True, null=True, upload_to='media/images_profile'),
        ),
    ]
