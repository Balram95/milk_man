# Generated by Django 2.1.7 on 2019-02-27 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0011_auto_20190224_1954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='milk',
            old_name='type',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='milk',
            old_name='cost',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='milkreceive',
            old_name='type',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='milkreceive',
            old_name='cost',
            new_name='price',
        ),
    ]
