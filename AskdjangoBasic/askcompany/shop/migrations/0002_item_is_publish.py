# Generated by Django 3.2.5 on 2021-07-16 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_publish',
            field=models.BooleanField(default=False),
        ),
    ]
