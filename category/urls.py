from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='category'),
    path('details/<slug:slug>/', views.details, name='details'),
    path('<slug:category_slug>/', views.getProductByCategory, name='product_by_category'),
]
