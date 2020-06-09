from django.contrib import admin
from django.db.models import Count

from .models import Category, Product, ProductImage, Variation, VariationImage


class CategoryAdmin(admin.ModelAdmin):
    list_display =['name','products_count']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.annotate(products_count=Count('products')).order_by('-products_count')
        return qs
    
    def products_count(self,variation_instance):
        return variation_instance.products_count

class VariationInLine(admin.TabularInline):
    model = Variation
    extra = 1

class ProductImageInLine(admin.TabularInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display  = ['name', 'price', 'sale_price']
    search_fields = ['name','slug','category__name']
    inlines = [
        ProductImageInLine,
        VariationInLine
    ]

class VariationImageInLine(admin.TabularInline):
    model = VariationImage

class VariationAdmin(admin.ModelAdmin):
    list_display = ['product','name','price','sale_price']
    inlines = [
        VariationImageInLine,
    ]

admin.site.register(Category,   CategoryAdmin)
admin.site.register(Product,    ProductAdmin)
admin.site.register(Variation,  VariationAdmin)
