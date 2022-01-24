# Generated by Django 2.2.5 on 2021-11-28 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0009_auto_20211125_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_change_status',
            field=models.DateTimeField(blank=True,null=True, verbose_name='Дата изменения'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='tasktable',
            name='cooperator',
        ),
        migrations.AddField(
            model_name='tasktable',
            name='cooperator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tables.Cooperator'),
        ),
        migrations.RemoveField(
            model_name='tasktable',
            name='task',
        ),
        migrations.AddField(
            model_name='tasktable',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tables.Task'),
        ),
    ]
