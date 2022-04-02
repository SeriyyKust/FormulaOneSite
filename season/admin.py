from django.contrib import admin
from .models import *


class DriversAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fromCountry', 'wins', 'photo', 'teams', 'time_update', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'time_update')
    list_editable = ('is_published',)
    list_filter = ('time_update', 'wins')


admin.site.register(Drivers, DriversAdmin)
admin.site.register(Teams)



