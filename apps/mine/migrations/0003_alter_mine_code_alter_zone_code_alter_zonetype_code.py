# Generated by Django 5.0 on 2024-02-16 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mine', '0002_alter_mine_description_alter_zone_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mine',
            name='code',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='zone',
            name='code',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='zonetype',
            name='code',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Código'),
        ),
    ]
