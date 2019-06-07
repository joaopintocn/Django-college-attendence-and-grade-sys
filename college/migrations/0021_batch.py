# Generated by Django 2.1.4 on 2019-03-24 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0020_auto_20190320_1001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.CharField(max_length=12, unique=True)),
                ('student', models.ManyToManyField(to='college.Student')),
            ],
        ),
    ]
