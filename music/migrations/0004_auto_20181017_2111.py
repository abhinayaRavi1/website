# Generated by Django 2.1.2 on 2018-10-18 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20181015_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='file_type',
        ),
        migrations.AddField(
            model_name='album',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='song',
            name='audio_file',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
