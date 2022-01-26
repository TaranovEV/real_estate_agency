# Generated by Django 2.2.24 on 2022-01-23 21:02

from django.db import migrations


def fill_field_new_buildings(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for real_estate_object in Flat.objects.all():
        real_estate_object.new_building = (
            real_estate_object.construction_year >= 2015
        )
        real_estate_object.save()

def backward_fill_field_new_buildings(apps,
                                      schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for real_estate_object in Flat.objects.all():
        real_estate_object.new_building = (
            real_estate_object.construction_year >= 2015
        )
        real_estate_object.save()


    
class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(fill_field_new_buildings,
                             backward_fill_field_new_buildings)
    ]
