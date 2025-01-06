from django.urls import path
from .import views

urlpatterns = [
   path('reel',views.reel),
   path('fake',views.fake),
]
