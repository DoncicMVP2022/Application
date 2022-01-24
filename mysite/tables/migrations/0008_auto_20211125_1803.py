# Generated by Django 2.2.5 on 2021-11-25 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0007_auto_20211125_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_change_status',
            field=models.DateTimeField(null=True, blank=True, verbose_name='Дата изменения'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tasktable',
            name='cooperator',
            field=models.ManyToManyField(to='tables.Cooperator'),
        ),
    ]