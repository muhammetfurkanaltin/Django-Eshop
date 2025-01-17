from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('basket/', views.view_basket, name='basket'),
    path('login/', views.user_login, name='login'),
]
