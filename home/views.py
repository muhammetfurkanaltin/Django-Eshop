from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from category.models import Category, Product
from django.http import JsonResponse



def home (request):
    products = Product.objects.filter(isFav=True)
    return render (request,'pages/home.html',{'products':products})
 
def about (request):
    return render (request,'pages/about.html')

def contact (request):
    return render (request,'pages/contact.html')

def user_login(request):
    return render(request,'pages/login.html')

def view_basket(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'pages/basket.html', {'product': product})

def add_to_cart(request, product_id):
    # Sepeti oturumdan al
    cart = request.session.get('cart', {})
    
    # Eğer ürün sepette varsa miktarını artır
    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1  # Ürünü ilk kez ekliyoruz.
    
    # Sepeti oturuma geri kaydet
    request.session['cart'] = cart
    request.session.modified = True  # Oturumu günceller

    return JsonResponse({'success': True, 'cart': cart})

def view_cart(request):
    cart = request.session.get('cart', {})
    # Ürünleri database'den almak için
    products = Product.objects.filter(id__in=cart.keys())
    cart_items = [
        {'product': product, 'quantity': cart[str(product.id)]} 
        for product in products
    ]
    return render(request, 'cart.html', {'cart_items': cart_items})