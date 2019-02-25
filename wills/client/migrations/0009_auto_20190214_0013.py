# Generated by Django 2.1.5 on 2019-02-14 00:13

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_auto_20190214_0001'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChildCareTaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('notes', models.TextField(blank=True, max_length=5000, null=True)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CareTaker', to='client.Child')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.ClientSession')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AddField(
            model_name='executor',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.ClientSession'),
        ),
    ]