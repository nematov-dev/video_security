# Generated by Django 5.1.7 on 2025-03-27 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_security_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='title',
        ),
        migrations.AddField(
            model_name='worker',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
