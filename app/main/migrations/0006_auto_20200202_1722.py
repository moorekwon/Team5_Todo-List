# Generated by Django 2.2.9 on 2020-02-02 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200202_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='todo',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
