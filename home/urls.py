from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('basket/<int:product_id>/', views.view_basket, name='basket'),
    path('login/', views.user_login, name='login'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    
]
