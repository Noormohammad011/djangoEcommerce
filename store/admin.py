from store.models import Product
from django.contrib import admin

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'description', 'price',  'stock', 'is_available', 'category', 'created_time', 'updated_time', )
    prepopulated_fields = {'slug': ('product_name',)}
    
    
admin.site.register(Product, ProductAdmin)
    
