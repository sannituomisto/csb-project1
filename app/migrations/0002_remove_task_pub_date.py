# Generated by Django 4.2.7 on 2023-12-18 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='pub_date',
        ),
    ]