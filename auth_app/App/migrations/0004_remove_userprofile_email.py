# Generated by Django 3.0.6 on 2020-05-12 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20200509_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
    ]