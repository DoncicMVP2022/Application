# Generated by Django 2.2.5 on 2022-01-10 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0018_task_data_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='date_change_status',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='date_finish_task',
        ),
        migrations.AddField(
            model_name='projects',
            name='data_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
