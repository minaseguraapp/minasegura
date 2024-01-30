from django.db import models

from apps.mine.models import Mine


class Priority(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción', null=True, blank=True)
    color = models.CharField(max_length=10, verbose_name='Color')
    is_active = models.BooleanField(default=True, verbose_name='¿Activo?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    def __str__(self):
        return f'{self.name} - {self.color}'

    class Meta:
        verbose_name = 'Prioridad'
        verbose_name_plural = 'Prioridades'


class EquipmentType(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo de equipo'
        verbose_name_plural = 'Tipos de equipo'


class Equipment(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción', null=True, blank=True)
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.SET_NULL, null=True,
                                       verbose_name='Tipo de equipo')
    mine = models.ForeignKey(Mine, on_delete=models.SET_NULL, null=True, verbose_name='Mina')
    image = models.ImageField(upload_to='equipment', null=True, blank=True, verbose_name='Imagen')
    is_active = models.BooleanField(default=True, verbose_name='¿Activo?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'


class Maintenance(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.SET_NULL, null=True, verbose_name='Equipo')
    description = models.TextField(verbose_name='Descripción', null=True, blank=True)
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True, related_name='maintenance_priority',
                                 verbose_name='Prioridad')
    work_time = models.FloatField(default=0, verbose_name='Tiempo de trabajo')
    work_started_time = models.DateTimeField(blank=True, null=True, verbose_name='Hora de inicio de trabajo', )
    work_end_time = models.DateTimeField(blank=True, null=True, verbose_name='Hora de fin de trabajo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    def __str__(self):
        return f'{self.equipment} - {self.priority}'

    class Meta:
        verbose_name = 'Mantenimiento'
        verbose_name_plural = 'Mantenimientos'
