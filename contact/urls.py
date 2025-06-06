from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
        path('', views.home, name='home'),
        path('search/', views.search, name='search'),
        

        path('contacts/', views.contacts, name='contacts'),
        path('contact/<int:contact_id>/details/', views.single_contact, name='contact-details'),
        path('contact/create/', views.create, name='create'),
]
