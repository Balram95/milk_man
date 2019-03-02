# Generated by Django 2.1.7 on 2019-02-23 14:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0004_auto_20190223_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount', models.FloatField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entries.Customer')),
                ('milk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entries.Milk')),
            ],
        ),
    ]