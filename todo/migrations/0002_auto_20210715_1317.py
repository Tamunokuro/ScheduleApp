# Generated by Django 3.0.5 on 2021-07-15 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateField(default='2021-07-15'),
        ),
    ]
