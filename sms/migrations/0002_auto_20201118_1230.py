# Generated by Django 3.1 on 2020-11-18 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SentMessages',
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ('name',)},
        ),
    ]