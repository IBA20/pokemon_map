# Generated by Django 3.1.14 on 2022-09-01 22:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0011_auto_20220902_0041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='next_evolution',
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 2, 22, 0, 40, 665905, tzinfo=utc)),
        ),
    ]