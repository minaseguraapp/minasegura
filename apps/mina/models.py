from django.db import models


class Mine(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.CharField(max_length=250, verbose_name='Descripción')
    manager = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, verbose_name='Encargado')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Mina'
        verbose_name_plural = 'Minas'


class ZoneType(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.CharField(max_length=250, verbose_name='Descripción')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo de zona'
        verbose_name_plural = 'Tipos de zona'


class Zone(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.CharField(max_length=250, verbose_name='Descripción')
    zone_type = models.ForeignKey(ZoneType, on_delete=models.SET_NULL, null=True, verbose_name='Tipo de zona')
    mine = models.ForeignKey(Mine, on_delete=models.SET_NULL, null=True, verbose_name='Mina')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Zona'
        verbose_name_plural = 'Zonas'
