from django.contrib import admin
from .models import Flat, Сomplaint, Owner


class FlatInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ['owner']


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner', ]
    readonly_fields = ['created_at', ]
    list_display = [
        'address', 'price', 'new_building',
        'construction_year', 'town',
    ]
    list_filter = ['new_building',
                   'rooms_number',
                   'has_balcony']
    raw_id_fields = ['who_likes']
    inlines = [FlatInline]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['author', 'flat_complaint']


class OwnerAdmin(admin.ModelAdmin):
    list_display = [
        'owner',
    ]
    raw_id_fields = ['flats']

admin.site.register(Flat, FlatAdmin)
admin.site.register(Сomplaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
