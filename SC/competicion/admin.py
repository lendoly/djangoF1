from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Circuito)
admin.site.register(Persona)
admin.site.register(Escuderia)
admin.site.register(Piloto)
admin.site.register(Clasificacion)


class GranPremioAdmin(admin.ModelAdmin):
    list_display = ('circuito', 'fecha')
    list_filter = ['fecha']
    search_fields = ['circuito']

admin.site.register(GranPremio, GranPremioAdmin)
