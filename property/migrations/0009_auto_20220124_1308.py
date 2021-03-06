# Generated by Django 2.2.24 on 2022-01-24 10:08

from django.db import migrations
import phonenumbers


def normalize_phone_number(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for real_estate_object in Flat.objects.all():
        normalize_number = phonenumbers.parse(
                                              real_estate_object.owners_phonenumber,
                                              'RU')
        if phonenumbers.is_valid_number(normalize_number):
            real_estate_object.owner_pure_phone = normalize_number
            real_estate_object.save()

def back_normalize_phone_number(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for real_estate_object in Flat.objects.all():
        normalize_number = phonenumbers.parse(
                                              real_estate_object.owners_phonenumber,
                                              'RU')
        if phonenumbers.is_valid_number(normalize_number):
            real_estate_object.owner_pure_phone = normalize_number
            real_estate_object.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20220124_0058'),
    ]

    operations = [
        migrations.RunPython(normalize_phone_number,
                             back_normalize_phone_number)
    ]
