from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
        # Home and Search
        path('', views.home, name='home'),
        path('search/', views.search, name='search'),
        
        # Contact
        path('contacts/', views.contacts, name='contacts'),
        path('contact/<int:contact_id>/details/', views.single_contact, name='details'),
        path('contact/create/', views.create, name='create'),
        path('contact/<int:contact_id>/update/', views.update, name='update'),
        path('contact/<int:contact_id>/delete/', views.delete, name='delete'),

        # User
        path('user/create/', views.register, name='register'),
        path('user/login/', views.login_view, name='login_view'),
        path('user/logout/', views.logout_view, name='logout_view'),
]
        
