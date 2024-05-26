from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(
        max_length=100,
        required=True,
        disabled=True,
        label="نام کاربری",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    email = forms.EmailField(
        required=True,
        disabled=True,
        label="ایمیل",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    first_name = forms.CharField(
        required=True,
        label="نام",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    last_name = forms.CharField(
        required=True,
        label="نام خانوادگی",
        widget=forms.TextInput(attrs={"class": "form-control", "pattern": "[آ-ی]"}),
    )

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]
