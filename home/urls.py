from django.urls import path
from .import views

urlpatterns = [
   path('',views.home),
   path('about',views.about),
   path('contact',views.contact),
   path('test-mongodb/', views.test_mongodb_connection, name='test-mongodb'),
   
]
