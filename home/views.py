from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Sum
from category.models import Product
from .forms import OrderForm

def home (request):
    products = Product.objects.filter(isFav=True)[:4]
    return render (request,'pages/home.html',{'products':products[:4]})
 
def about (request):
    return render (request,'pages/about.html')

def contact (request):
    return render (request,'pages/contact.html')

def buy_now(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            
            # Session'dan sepet bilgilerini al
            cart = request.session.get('cart', {})
            total_price = sum(item['price'] * item['quantity'] for item in cart.values())
            
            # Siparişe ürünleri ekle
            for product_id, item in cart.items():
                product = Product.objects.get(id=int(product_id))
                order.products.add(product, through_defaults={'quantity': item['quantity']})
            
            # Sepeti temizle
            if 'cart' in request.session:
                del request.session['cart']
            request.session.modified = True
            
            messages.success(request, "Siparişiniz başarıyla oluşturuldu!")
            return redirect("home")
    else:
        form = OrderForm()

    cart = request.session.get('cart', {})
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, "pages/buy_now.html", {"form": form, "total_price": total_price})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # Sepet mevcut mu? Eğer yoksa, boş bir sepet oluştur.
    cart = request.session.get('cart', {})
    
    product_price = float(product.price)

    # Eğer ürün zaten sepette varsa, miktarını artır.
    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        # Ürün bilgilerini sepete eklerken price ve quantity'yi de eklediğimize emin olalım
        cart[str(product_id)] = {'title': product.title, 'price': product_price, 'quantity': 1, 'imagUrl': product.imagUrl}
    
    # Sepeti session'a kaydet
    request.session['cart'] = cart
    messages.success(request, f"{product.title} başarıyla sepete eklendi!")
    # Sepet sayfasına yönlendir
    referer = request.META.get('HTTP_REFERER', '/')
    return redirect(referer)

def clear_cart(request):
    # Remove specific session keys
    if 'cart' in request.session:
        del request.session['cart']
    # Force session to be saved
    request.session.modified = True
    return redirect('cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())  # Toplam fiyat hesaplama
    return render(request, 'pages/cart.html', {'cart': cart, 'total_price': total_price})

def update_quantity(request, product_id):
    if request.method == 'POST':
        action = request.POST.get('action')
        cart = request.session.get('cart', {})

        if str(product_id) in cart:
            if action == 'increase':
                cart[str(product_id)]['quantity'] += 1
            elif action == 'decrease' and cart[str(product_id)]['quantity'] > 1:
                cart[str(product_id)]['quantity'] -= 1
            elif action == 'decrease' and cart[str(product_id)]['quantity'] == 1:
                del cart[str(product_id)]

        request.session['cart'] = cart
        request.session.modified = True

    return redirect('cart')




