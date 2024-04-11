from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .models import Pokemon, Movement, Perlevel

# Create your views here.
def poke_list(response):
    data = Pokemon.display_properties()
    print('-->>')
    print(data)
    return JsonResponse({'data': data})

def poke_detail(response, number):
    pokemon = get_object_or_404(Pokemon, number=number)
    pokemon_format = Pokemon.objects.filter(number=number).values(*Pokemon.fields_to_display)
    movement_format = []

    for movement in pokemon.movement.all():
        perlevel = Perlevel.objects.get(pokemon=pokemon, movement=movement).level
        movement_format.append({'level': perlevel, 'name': movement.name, 'description': movement.description})

    return JsonResponse({'data': { 'pokemon': list(pokemon_format)[0], 'movement': movement_format}})