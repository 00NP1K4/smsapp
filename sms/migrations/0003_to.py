# Generated by Django 3.1 on 2020-11-23 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0002_auto_20201118_1230'),
    ]

    operations = [
        migrations.CreateModel(
            name='To',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50)),
            ],
        ),
    ]
