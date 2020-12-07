from django.contrib import admin

from .models import Order, UserlessOrder
admin.site.register(Order)
admin.site.register(UserlessOrder)

