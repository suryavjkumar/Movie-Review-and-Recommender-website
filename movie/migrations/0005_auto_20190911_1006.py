# Generated by Django 2.2.4 on 2019-09-11 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20190910_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='helpful',
            field=models.BooleanField(null=True),
        ),
    ]
