from django.contrib import admin
from pokemon_entities.models import Pokemon, PokemonEntity


@admin.register(PokemonEntity)
class PokemonEntityAdmin(admin.ModelAdmin):
    list_select_related = True


admin.site.register(Pokemon)
