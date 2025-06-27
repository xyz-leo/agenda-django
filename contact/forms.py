from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
import re
from django.contrib.auth import password_validation

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


class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(min_length=2, max_length=30, required=True)
    last_name = forms.CharField(min_length=2, max_length=30, required=True)
    
    password1 = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}), help_text=password_validation.password_validators_help_text_html(), required=False)
    password2 = forms.CharField(label="Password Confirmation", strip=False, widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}), help_text=password_validation.password_validators_help_text_html(), required=False)


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)

        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()
        return user

    
    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 or password2:
            if password1 != password2:
                self.add_error('password2', ValidationError("Password confirmation failed"))
        return super().clean()


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError('Email already registered', code='Invalid')
        return email


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


    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error('password1', ValidationError(errors))
        return password1
