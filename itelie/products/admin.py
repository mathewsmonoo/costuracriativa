from django.contrib import admin

from .models import Category, Product, Variation

class VariationInLine(admin.TabularInline):
    model = Variation
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'sale_price']
    #list_display = ['name', 'description', 'get_formatted_price', 'get_formatted_sale_price']
    inlines = [
        VariationInLine
    ]

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Variation)
