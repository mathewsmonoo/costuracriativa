# coding=utf-8
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from costura.users.forms import UserChangeForm, UserCreationForm, StaffChangeForm, StaffCreationForm
from .models import Staff

User = get_user_model()

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", {"fields": ("name",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "name","is_superuser","is_admin","is_staff","is_customer"]
    search_fields = ["name"]

admin.site.register(Staff)
