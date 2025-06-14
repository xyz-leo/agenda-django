from datetime import timezone
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories' # The automatic Django plural makes a typo "Categorys", so we rename it with this Meta class.


class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True) #type: ignore
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


        
    # Used to show the objects by fname and lname
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
