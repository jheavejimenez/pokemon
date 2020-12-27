from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(PokemonSpecies)
class PokemonSpeciesAdmin(admin.ModelAdmin):
    list_display = ('name', 'evolution_level', 'show_type', 'next_evolution')


@admin.register(PokemonType)
class PokemonTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):

    list_display = ('nickname', 'species', 'level', 'trainer')

    """def get_level(self):
        return "\n".join([evo.next_evolution for evo in self.next_evolution.all()])"""
