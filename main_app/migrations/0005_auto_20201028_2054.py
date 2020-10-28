# Generated by Django 3.1.2 on 2020-10-28 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20201027_2301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='producer',
            name='distributors',
            field=models.ManyToManyField(to='main_app.Distributor'),
        ),
    ]
