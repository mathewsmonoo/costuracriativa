from django.forms import ModelForm as ModelForm
import django.forms as baseforms
from django.contrib.auth import  forms, get_user_model
from django.core.exceptions import ValidationError
from django.db import transaction
from django.utils.translation import gettext_lazy as _
from .models import Admin, Staff, Customer

User = get_user_model()

class UserCreationForm(forms.UserCreationForm):

    error_message = forms.UserCreationForm.error_messages.update(
        {"duplicate_user": _("Este nome de usuário já foi escolhido.")}
    )

    class Meta(forms.UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])

class MyCustomSignupForm(UserCreationForm):

    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = ('username','prefix','email','first_name','last_name','cpf','dob')

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(
            self.error_messages["duplicate_username"]
        )
        
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        return user


class UserChangeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].disabled = True
        self.fields['last_name'].disabled = True
        self.fields['email'].disabled = True
        self.fields['dob'].disabled = True
        self.fields['cpf'].disabled = True

    class Meta:
        model = User
        fields = ['prefix', 'first_name', 'last_name', 'email', 'cpf', 'dob']
        
class StaffChangeForm(forms.UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'

class StaffCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = ('username','email','first_name','last_name','cpf','dob')

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(
            self.error_messages["duplicate_username"]
        )
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_staff = True
        user.save()
        staff = Staff.objects.create(user=user)
        return user
    
class StaffChangeForm(forms.UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'

class AdminCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User

        fields = ('username','email','first_name','last_name','cpf','dob')

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(
            self.error_messages["duplicate_username"]
        )

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = True
        user.save()
        staff = Admin.objects.create(user=user)
        return user
