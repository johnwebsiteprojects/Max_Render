# Generated by Django 3.2 on 2021-08-05 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20210805_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='profileImage',
            field=models.ImageField(blank=True, null=True, upload_to='images_profile'),
        ),
    ]
