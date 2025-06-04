from django.contrib import admin
from contact import models

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'first_name', 'last_name', 'phone',
    ordering = '-id', 'first_name'
    search_fields = 'first_name', 'last_name', 'phone',
    list_per_page = 10
    list_max_show_all = 25
    list_display_links = 'first_name',
