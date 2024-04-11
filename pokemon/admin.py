from django.contrib import admin
from django.utils.html import format_html

from .models import Pokemon, Movement, Perlevel

class PokemonAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["number", "name", "img"]}),
        ("Stats", {"fields": ["health", "physical_attack", "physical_defence", "speed", "special_attack", "special_defence", "gen1_special"]}),
    ]
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.img.url))

    image_tag.short_description = 'Image'

admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(Movement)
admin.site.register(Perlevel)