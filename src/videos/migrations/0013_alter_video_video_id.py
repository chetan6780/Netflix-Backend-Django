# Generated by Django 3.2.6 on 2021-08-20 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0012_auto_20210820_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_id',
            field=models.CharField(max_length=220, unique=True),
        ),
    ]
