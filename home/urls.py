from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'), # "btn add to cart"
    path('clear-cart/', views.clear_cart, name='clear_cart'), # "btn clear cart"
    path('cart/', views.view_cart, name='cart'), # "/cart"
    path('update_quantity/<int:product_id>/', views.update_quantity, name='update_quantity'), # "- +"
    path('buy-now/', views.buy_now, name='buy_now'),
    
    path('create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),
    path('success/', views.success, name='success'),  # Success view ekleyin
    path('cancel/', views.cancel, name='cancel'),  # Cancel view ekleyin
    
]
