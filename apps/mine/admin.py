from django.contrib import admin

from .models import Mine, Zone, ZoneType


@admin.register(Mine)
class MineAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'manager')
    search_fields = ('name', 'description', 'manager__username')
    list_filter = ('manager',)


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'zone_type', 'mine')
    search_fields = ('name', 'description', 'zone_type__name', 'mine__name')
    list_filter = ('zone_type', 'mine')


@admin.register(ZoneType)
class ZoneTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
