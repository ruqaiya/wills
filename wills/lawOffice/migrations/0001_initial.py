# Generated by Django 2.1.5 on 2019-02-04 21:21

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lawOffice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
