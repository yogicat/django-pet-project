# Generated by Django 2.0 on 2019-05-05 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_auto_20190503_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='photo',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='_pet_pics'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='animal',
            field=models.CharField(blank=True, choices=[('Dog', 'Dog'), ('Cat', 'Cat'), ('Other', 'Other')], max_length=50),
        ),
    ]
