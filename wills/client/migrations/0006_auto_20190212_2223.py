# Generated by Django 2.1.5 on 2019-02-13 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_auto_20190205_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='adopted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='child',
            name='custody',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='child',
            name='legitimate',
            field=models.BooleanField(default=True),
        ),
    ]
