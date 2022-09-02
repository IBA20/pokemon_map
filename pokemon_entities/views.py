import folium

from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime

from pokemon_entities.models import PokemonEntity, Pokemon

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemon_entities = PokemonEntity.objects.select_related('pokemon').filter(
        appeared_at__lte=localtime(),
        disappeared_at__gte=localtime(),
    )
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lng,
            request.build_absolute_uri(pokemon_entity.pokemon.image.url)
        )

    pokemons_on_page = []
    for pokemon_entity in pokemon_entities:
        pokemons_on_page.append(
            {
                'pokemon_id': pokemon_entity.pokemon.id,
                'img_url': request.build_absolute_uri(
                    pokemon_entity.pokemon.image.url
                ),
                'title_ru': pokemon_entity.pokemon.title,
            }
        )

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),  # noqa F401
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)

    serialized_pokemon = {
        "pokemon_id": pokemon_id,
        "title_ru": pokemon.title,
        "img_url": request.build_absolute_uri(pokemon.image.url),
        "description": pokemon.description,
        "title_en": pokemon.title_en,
        "title_jp": pokemon.title_jp,
    }

    next_evolution = pokemon.next_evolutions.first()
    if next_evolution:
        serialized_pokemon["next_evolution"] = {
            "title_ru": next_evolution.title,
            "pokemon_id": next_evolution.id,
            "img_url": request.build_absolute_uri(
                next_evolution.image.url
            ),
        }

    previous_evolution = pokemon.previous_evolution
    if previous_evolution:
        serialized_pokemon["previous_evolution"] = {
            "title_ru": previous_evolution.title,
            "pokemon_id": previous_evolution.id,
            "img_url": request.build_absolute_uri(
                previous_evolution.image.url
            ),
        }

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemon_entities = PokemonEntity.objects.select_related('pokemon').filter(
        pokemon=pokemon,
        appeared_at__lte=localtime(),
        disappeared_at__gte=localtime(),
    )
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lng,
            request.build_absolute_uri(pokemon_entity.pokemon.image.url),
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(),  # noqa F401
        'pokemon': serialized_pokemon,
    })
