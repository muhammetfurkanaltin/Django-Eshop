from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from category.models import Category, Product


def home (request):
    products = Product.objects.filter(isFav=True)
    return render (request,'pages/home.html',{'products':products})
 
def about (request):
    return render (request,'pages/about.html')

def contact (request):
    return render (request,'pages/contact.html')

def user_login(request):
    return render(request,'pages/login.html')

def basket(request):
    return render(request,'pages/basket.html')

def view_basket(request):
    basket = request.session.get('basket', {})
    basket_items = []
    total_price = 0
    
    for product_id, quantity in basket.items():
        product = get_object_or_404(Product, id=product_id)
        total = product.price * quantity
        total_price += total
        
        basket_items.append({
            'products': product,
            'quantity': quantity,
            'total_price': total
        })
    
    context = {
        'basket_items': basket_items,
        'total_price': total_price
    }
    return render(request, 'pages/basket.html', context)

def add_to_basket(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        
        basket = request.session.get('basket', {})
        
        if product_id in basket:
            basket[product_id] += quantity
        else:
            basket[product_id] = quantity
        
        request.session['basket'] = basket
        messages.success(request, 'Ürün sepete eklendi.')
        
    return redirect('basket')

def update_basket(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        
        basket = request.session.get('basket', {})
        
        if quantity > 0:
            basket[product_id] = quantity
        else:
            basket.pop(product_id, None)
            
        request.session['basket'] = basket
        messages.success(request, 'Sepet güncellendi.')
        
    return redirect('basket')

def remove_from_basket(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        basket = request.session.get('basket', {})
        basket.pop(product_id, None)
        request.session['basket'] = basket
        messages.success(request, 'Ürün sepetten kaldırıldı.')
        
    return redirect('basket')