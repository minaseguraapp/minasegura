from django.contrib import admin

from .models import Priority, EquipmentType, Equipment, Maintenance


@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'color', 'is_active')
    search_fields = ('name', 'description', 'color')
    list_filter = ('is_active',)


@admin.register(EquipmentType)
class EquipmentTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'equipment_type', 'mine', 'is_active')
    search_fields = ('name', 'description', 'equipment_type__name', 'mine__name')
    list_filter = ('equipment_type', 'mine', 'is_active')


@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('equipment', 'description', 'priority', 'work_time', 'work_started_time', 'work_end_time')
    search_fields = ('equipment__name', 'description', 'priority__name')
    list_filter = ('priority',)
