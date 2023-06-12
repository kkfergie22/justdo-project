from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=150,
        required=True,
        help_text="Enter your fullname",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First name"}
        ),
    )

    last_name = forms.CharField(
        max_length=150,
        required=True,
        help_text="Enter your surname",
        widget=forms.TextInput(
            attrs={"id": "lastName", "class": "form-control", "placeholder": "Surname"}
        ),
    )

    username = forms.CharField(
        max_length=150,
        required=True,
        help_text="Enter your fullname",
        widget=forms.TextInput(
            attrs={
                "id": "userName",
                "class": "form-control",
                "placeholder": "At least 6 characters",
            }
        ),
    )

    email = forms.EmailField(
        max_length=50,
        required=True,
        help_text="Enter your fullname",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "example@example.com"}
        ),
    )

    password1 = forms.CharField(
        max_length=100,
        required=True,
        help_text="Enter your fullname",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Create your password"}
        ),
    )

    password2 = forms.CharField(
        max_length=100,
        required=True,
        help_text="Enter your fullname",
        widget=forms.PasswordInput(
            attrs={"class": "form-control",
                   "placeholder": "Confirm your password"}
        ),
    )

    check = forms.BooleanField(required=True,
                               widget=forms.CheckboxInput(attrs={"class":
                                                                 "form-check-\
                                                                    input \
                                                                  me-2 mx-2"}))

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
            "check",
        ]
