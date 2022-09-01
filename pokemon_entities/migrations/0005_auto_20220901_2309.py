# Generated by Django 3.1.14 on 2022-09-01 20:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0004_auto_20220901_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 1, 20, 9, 23, 881014, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='attack',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='defense',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 2, 20, 9, 23, 881014, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='stamina',
            field=models.IntegerField(default=0),
        ),
    ]
