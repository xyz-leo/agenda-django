from datetime import timezone
from django.db import models
from django.http.request import uploadhandler
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True) #type: ignore
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/%d')

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
