# Generated by Django 2.2.9 on 2020-02-02 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_todo_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='todo',
            name='start_date',
            field=models.DateField(),
        ),
    ]