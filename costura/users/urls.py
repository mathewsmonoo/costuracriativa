from django.urls import path
from . import views
from costura.users.views import (
    admin_create_view,
    staff_create_view,
    staff_list_view,
    customer_list_view,
    user_redirect_view,
    user_update_view,
    user_detail_view,
    password_change_view,
)

app_name = "users"
urlpatterns = [
    path("adminsignup/",     view=admin_create_view,      name="adminsignup"),
    path("staff/",          view=staff_list_view,        name="stafflist"),
    path("staffsignup/",     view=staff_create_view,      name="staffsignup"),
    path("customers/",      view=customer_list_view,     name="customerlist"),
    path("~redirect/",      view=user_redirect_view,     name="redirect"),
    path("~update/",        view=user_update_view,       name="update"),
    path('~changepass/',    view=password_change_view,   name="change_password"),
    path("<str:username>/", view=user_detail_view,       name="detail"),
]
