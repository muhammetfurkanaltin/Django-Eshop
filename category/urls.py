from django.urls import path
from . import views

urlpatterns = [
   path('<slug:slug>' , views.details),
   path('category/<slug:slug>', views.getProductByCategory, name='product_by_category'),
]
