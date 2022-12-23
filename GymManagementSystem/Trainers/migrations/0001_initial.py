# Generated by Django 4.1.1 on 2022-12-19 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainer_name', models.CharField(max_length=30)),
                ('trainer_description', models.CharField(max_length=30)),
                ('trainer_image', models.ImageField(upload_to='trainerimage')),
            ],
        ),
    ]