from django.contrib import admin

from .models import Flat, Сomplaint


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner',]
    readonly_fields = ['created_at',]
    list_display = [
        'address', 'price', 'new_building', 
        'construction_year', 'town',
        'owners_phonenumber', 'owner_pure_phone'
    ]
    list_filter = ['new_building',
                   'rooms_number',
                   'has_balcony']
    raw_id_fields = ['who_likes']


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['author', 'flat_complaint']

admin.site.register(Flat, FlatAdmin)
admin.site.register(Сomplaint, ComplaintAdmin)
