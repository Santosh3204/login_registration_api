# Generated by Django 3.0.5 on 2020-09-19 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='user_id',
        ),
    ]
