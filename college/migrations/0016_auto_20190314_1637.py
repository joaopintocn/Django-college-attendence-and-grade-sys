# Generated by Django 2.1.4 on 2019-03-14 11:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0015_auto_20190314_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignments',
            name='deadline',
            field=models.DateTimeField(verbose_name=django.utils.timezone.now),
        ),
    ]
