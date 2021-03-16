from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from core.models import Account


class UsuarioForm(UserCreationForm):
    # email = forms.EmailField(max_length=100)
    name = forms.CharField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)


class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

        # model = Account
        # fields = ['nome', 'tel', 'dt_nasc']








from django import forms
# from django.contrib.auth.forms import UserChangeForm, UserCreationForm
#
# from .models import CustomUser
#
#
# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = (
#             "username",
#             "email",
#         )
#
#
# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = CustomUser
#         fields = "__all__"