from django.urls import path
from . import views
from costura.users.views import (
    admin_create_view,
    staff_create_view,
    user_redirect_view,
    user_update_view,
    user_detail_view,
)

app_name = "users"
urlpatterns = [
    path("adminsignup",     view= admin_create_view,     name="adminsignup"),
    path("staffsignup",     view= staff_create_view,     name="staffsignup"),
    path("~redirect/",      view=user_redirect_view,    name="redirect"),
    path("~update/",        view=user_update_view,      name="update"),
    path("<str:username>/", view=user_detail_view,      name="detail"),
]
