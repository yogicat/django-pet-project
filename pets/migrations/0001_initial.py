# Generated by Django 2.0 on 2019-05-07 05:36

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('animal', models.CharField(blank=True, choices=[('Dog', 'Dog'), ('Cat', 'Cat'), ('Other', 'Other')], max_length=50)),
                ('photo', models.ImageField(blank=True, default='default.jpg', upload_to='pets')),
                ('registration_number', models.CharField(blank=True, max_length=50)),
                ('diseases_info', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, encoder='')),
                ('allergies_info', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, encoder='')),
                ('preferences', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, encoder='')),
                ('is_main', models.BooleanField(default=False)),
            ],
        ),
    ]