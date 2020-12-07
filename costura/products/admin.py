from django.contrib import admin
from django.db.models import Count

from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display =['name','products_count']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.annotate(products_count=Count('products')).order_by('-products_count')
        return qs
    
    def products_count(self,product_instance):
        return product_instance.products_count

class ProductAdmin(admin.ModelAdmin):
    list_display  = ['name','is_active', 'price', 'discount_price','cost','time']
    search_fields = ['name','slug','category__name']

admin.site.register(Category,   CategoryAdmin)
admin.site.register(Product,    ProductAdmin)
