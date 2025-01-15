from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('basket/', views.view_basket, name='basket'),
    path('add-to-basket/', views.add_to_basket, name='add_to_basket'),
    path('update-basket/', views.update_basket, name='update_basket'),
    path('remove-from-basket/', views.remove_from_basket, name='remove_from_basket'),
]
