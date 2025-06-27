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
        path('user/', views.user_view, name='user_view'),
        path('user/register/', views.register, name='register'),
        path('user/login/', views.login_view, name='login_view'),
        path('user/logout/', views.logout_view, name='logout_view'),
        path('user/update/', views.user_update, name='user_update'),

        # Categories
        path('categories/', views.category_list, name='category_list'),
        path('categories/<int:category_id>/contacts/', views.contacts_by_category, name='contacts_by_category'),
        path('categories/create', views.category_create, name='category_create'),
       path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
       path('categories/<int:category_id>/edit', views.category_update, name='category_update'),
       path('categories/<int:category_id>/delete', views.category_delete, name='category_delete'),

]
        
