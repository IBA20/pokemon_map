# Generated by Django 3.1.14 on 2022-09-01 22:17

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0012_auto_20220902_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(null=True, upload_to='images/%Y/%m/%d/', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous_evolutions', to='pokemon_entities.pokemon', verbose_name='Из кого эволюционировал'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title',
            field=models.TextField(verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.TextField(blank=True, null=True, verbose_name='Название (англ.)'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.TextField(blank=True, null=True, verbose_name='Название (яп.)'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время появления'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='attack',
            field=models.IntegerField(default=0, verbose_name='Атака'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='defense',
            field=models.IntegerField(default=0, verbose_name='Защита'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 2, 22, 17, 40, 290224, tzinfo=utc), verbose_name='Время исчезновения'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(default=0, verbose_name='Здоровье'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='lat',
            field=models.FloatField(verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(default=0, verbose_name='Уровень'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='lng',
            field=models.FloatField(verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entities', to='pokemon_entities.pokemon', verbose_name='Тип покемона'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='stamina',
            field=models.IntegerField(default=0, verbose_name='Выносливость'),
        ),
    ]
