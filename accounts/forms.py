from .models import UserProfile
from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from datetime import datetime


class UserLoginForm(forms.Form):
    """
    Form used to log in user

    """

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserProfileForm(UserCreationForm):
    """
    Form used to register a new user profile
    """
    # Added email feild to make it required
    email = forms.EmailField(max_length=100)
    img = forms.ImageField(required=False, label="Profile Image")
    phone = forms.IntegerField(required=False, label="Phone number")
    description = forms.CharField(
        widget=forms.Textarea, required=False, label="Few things about you")
    terms = forms.BooleanField(label="Accept terms and conditions")

    class Meta:
        model = User

        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']

        def clean_email(self):
            email = self.cleaned_data.get('email')
            username = self.cleaned_data.get('username')
            if User.objects.filter(email=email).exclude(username=username):
                raise forms.ValidationError(
                    u'Email addresses must be unique.')
            return email

        def clean_password2(self):
            password1 = self.cleaned_data.get('password1')
            password2 = self.cleaned_data.get('password2')

            if not password1 or not password2:
                raise ValidationError("Password must not be empty")

            if password1 != password2:
                raise ValidationError("Passwords do not match")

            return password2
