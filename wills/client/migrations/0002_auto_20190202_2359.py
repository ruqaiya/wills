# Generated by Django 2.1.4 on 2019-02-03 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spouse',
            old_name='partnerSession',
            new_name='session',
        ),
        migrations.AlterField(
            model_name='child',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clientsession', to='client.ClientSession'),
        ),
    ]