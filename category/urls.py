from django.urls import path
from .import views


urlpatterns = [
   path('',views.home),
   path('real',views.real),
   path('fake',views.fake),
]
