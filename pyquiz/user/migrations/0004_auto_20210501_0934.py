# Generated by Django 3.1.6 on 2021-05-01 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_profile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='goal',
            field=models.TextField(max_length=500),
        ),
    ]
