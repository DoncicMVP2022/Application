# Generated by Django 2.2.5 on 2021-11-21 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0002_taskstatus_tasktable'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskstatus',
            name='task_status',
            field=models.CharField(choices=[('Назначено', 'Назначено'), ('В работе', 'В работе'), ('Выполнено', 'Выполнено'), ('Проверено', 'Проверено')], max_length=200, null=True),
        ),
    ]
