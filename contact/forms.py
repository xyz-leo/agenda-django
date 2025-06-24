from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
    #def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    self.fields['email'].widget.attrs.update({'placeholder':'Enter your e-mail'})

    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone', 'email',)

        #widgets = {
        #        'email': forms.EmailInput(attrs={'placeholder': 'Enter your e-mail address'}),
        #        }
    #def clean(self):
    #    cleaned_data = self.cleaned_data
    #    self.add_error('first_name', ValidationError('Error message', code='Invalid'))
    #    return super().clean()


