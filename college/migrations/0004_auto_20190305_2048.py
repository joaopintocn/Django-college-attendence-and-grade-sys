# Generated by Django 2.1.4 on 2019-03-05 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0003_auto_20190305_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semestersub',
            name='professor',
        ),
        migrations.AlterField(
            model_name='professor',
            name='status',
            field=models.CharField(choices=[('student', 'student'), ('professor', 'professor')], default='professor', max_length=9),
        ),
    ]
