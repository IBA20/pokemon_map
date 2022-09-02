from django.utils import timezone
from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.TextField(verbose_name='Название')
    title_en = models.TextField(
        default='',
        blank=True,
        verbose_name='Название (англ.)',
    )
    title_jp = models.TextField(
        default='',
        blank=True,
        verbose_name='Название (яп.)',
    )
    image = models.ImageField(
        upload_to='images/%Y/%m/%d/',
        null=True,
        blank=True,
        verbose_name='Картинка',
    )
    description = models.TextField(
        default='',
        blank=True,
        verbose_name='Описание',
    )
    previous_evolution = models.ForeignKey(
        'Pokemon',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='next_evolutions',
        verbose_name='Из кого эволюционировал',
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        related_name='entities',
        verbose_name='Тип покемона',
    )
    lat = models.FloatField(verbose_name='Широта')
    lng = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Время появления',
    )
    disappeared_at = models.DateTimeField(verbose_name='Время исчезновения')
    level = models.IntegerField(verbose_name='Уровень')
    health = models.IntegerField(verbose_name='Здоровье')
    attack = models.IntegerField(verbose_name='Атака')
    defense = models.IntegerField(verbose_name='Защита')
    stamina = models.IntegerField(verbose_name='Выносливость')

    def __str__(self):
        return f'{self.pokemon.title} в ({self.lat}, {self.lng})'
