# Generated by Django 2.1.4 on 2019-03-19 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0017_auto_20190314_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignments',
            name='deadline',
            field=models.TextField(max_length=11),
        ),
    ]