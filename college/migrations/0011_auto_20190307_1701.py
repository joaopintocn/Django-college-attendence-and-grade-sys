# Generated by Django 2.1.4 on 2019-03-07 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0010_auto_20190307_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[('5', 5), ('4', 4), ('6', 6), ('10', 10), ('3', 3), ('2', 2), ('7', 7), ('8', 8), ('1', 1), ('9', 9)], default=1),
        ),
    ]
