# Generated by Django 3.2.6 on 2021-08-19 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_videoproxy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videoproxy',
            options={'verbose_name': 'Published Video', 'verbose_name_plural': 'Published Videos'},
        ),
    ]
