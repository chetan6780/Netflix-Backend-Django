# Generated by Django 3.2.6 on 2021-08-21 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0006_alter_playlist_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='videos',
        ),
    ]
