# Generated by Django 2.2.5 on 2022-01-10 17:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0020_auto_20220110_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='data_created',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]