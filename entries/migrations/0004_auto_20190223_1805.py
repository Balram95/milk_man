# Generated by Django 2.1.7 on 2019-02-23 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0003_auto_20190223_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='client',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='milk',
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
    ]
