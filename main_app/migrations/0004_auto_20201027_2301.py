# Generated by Django 3.1.2 on 2020-10-27 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_wine'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wine',
            old_name='year',
            new_name='price',
        ),
    ]