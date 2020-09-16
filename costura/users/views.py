from allauth.account.views import PasswordChangeView as allauth_PasswordChangeView
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DetailView, RedirectView, TemplateView, UpdateView

from .decorators import admin_required, staff_required
from .forms import AdminCreationForm, StaffCreationForm, UserChangeForm

User = get_user_model()



class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"

class PasswordChangeView(LoginRequiredMixin, allauth_PasswordChangeView):
    
    def get_success_url(self):
        return reverse(
            "users:detail",
            kwargs={'username': self.request.user.username},
        )

password_change_view = PasswordChangeView.as_view()

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserChangeForm

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

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Credenciais Aualizadas com sucesso")
        )
        return super().form_valid(form)

class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse(
            "users:detail",
            kwargs={"username": self.request.user.username},
        )

user_detail_view   = UserDetailView.as_view()
user_update_view   = UserUpdateView.as_view()
user_redirect_view = UserRedirectView.as_view()

class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

class AdminCreateView(SuperUserRequiredMixin, CreateView):
    model = User
    form_class = AdminCreationForm
    template_name = 'account/signup_admin.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'admin'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('users:redirect')
    
admin_create_view = AdminCreateView.as_view()

class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_admin

class StaffCreateView(AdminRequiredMixin, CreateView):
    model = User
    form_class = StaffCreationForm
    template_name = 'account/signup_staff.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'staff'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('users:redirect')

staff_create_view = StaffCreateView.as_view()
