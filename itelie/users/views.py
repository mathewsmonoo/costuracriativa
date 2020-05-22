from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, RedirectView, TemplateView, UpdateView

from .forms import UserAdminCreationForm
from .models import User

User = get_user_model()

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/index.html'

class RegisterView(CreateView):
    model           = User
    template_name   = 'accounts/register.html'
    form_class      = UserAdminCreationForm
    success_url     = reverse_lazy('index')

class UserDetailView(LoginRequiredMixin, DetailView):
    model           = User
    slug_field      = "username"
    slug_url_kwarg  = "username"

class UserUpdateView(LoginRequiredMixin, UpdateView):
    fields = [
        "name",
        "dob",
        "cpf",
        "rg",
        "phone",
        "prefix",
    ]

    model = User

    def get_success_url(self):
        return reverse(
            "users:detail",
            kwargs={'username': self.request.user.username},
        )

    def get_object(self):
        # Only Get the User Record for the
        #   User Making the Request
        return User.objects.get(
            username=self.request.user.username
        )

class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse(
            "users:detail",
            kwargs={"username": self.request.user.username},
        )

index               = IndexView.as_view()
register            = RegisterView.as_view()
user_detail_view    = UserDetailView.as_view()
user_update_view    = UserUpdateView.as_view()
user_redirect_view  = UserRedirectView.as_view()
