from django.contrib import admin

# Register your models here.
from .models import Property , Category , Reserve



class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name' , 'property_type' , 'category' , 'area' , 'beds_number' , 'baths_number' , 'garages_number']
    search_fields = ['name' , 'property_type']
    list_filter = ['category' , 'property_type']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name' , 'image' ]
    search_fields = ['category_name' ]
    list_filter = ['category_name']

class ReserveAdmin(admin.ModelAdmin):
    list_display = ['name' , 'email', 'notes' ]
    search_fields = ['name' ]
    list_filter = ['name']

admin.site.register(Property , PropertyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Reserve, ReserveAdmin)