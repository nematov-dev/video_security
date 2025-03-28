# Generated by Django 5.1.7 on 2025-03-28 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_security_app', '0004_alter_worker_managers_alter_worker_is_staff'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='worker',
            options={'verbose_name': 'Worker', 'verbose_name_plural': 'Workers'},
        ),
        migrations.AddField(
            model_name='worker',
            name='is_user',
            field=models.BooleanField(default=False),
        ),
    ]
