from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
import re

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone', 'email', 'description', 'category',)

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if any(char.isdigit() for char in first_name):
            raise forms.ValidationError('First name cannot contain numbers.')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if any(char.isdigit() for char in last_name):
            raise forms.ValidationError('Last name cannot contain numbers.')
        return last_name


    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if not re.fullmatch(r'[\d\s()-]+', phone):
            raise forms.ValidationError('Phone must contain only numbers, spaces, parentheses and dashes (-).')

        return phone


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True, min_length=2, max_length=50)
    last_name = forms.CharField(required=True, min_length=2, max_length=50)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            self.add_error('email', ValidationError('Email already registered', code='Invalid'))

        return email
