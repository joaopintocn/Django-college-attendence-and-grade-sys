# Generated by Django 2.1.4 on 2019-03-14 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0016_auto_20190314_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignments',
            name='deadline',
            field=models.CharField(max_length=11),
        ),
    ]
