# Generated by Django 2.0 on 2019-05-02 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_pet_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetAdmin',
            fields=[
                ('pet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pets.Pet')),
            ],
            bases=('pets.pet',),
        ),
        migrations.AddField(
            model_name='pet',
            name='allergies_info',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='pet',
            name='diseases_info',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='pet',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pet',
            name='preferences',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='pet',
            name='registration_number',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='pet',
            name='animal',
            field=models.CharField(blank=True, choices=[('강아지', 'DOG'), ('고양이', 'CAT'), ('기타', 'ETC')], max_length=50),
        ),
    ]
