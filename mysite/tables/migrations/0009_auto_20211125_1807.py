# Generated by Django 2.2.5 on 2021-11-25 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0008_auto_20211125_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_change_status',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата изменения'),
            preserve_default=False,
        ),
    ]
