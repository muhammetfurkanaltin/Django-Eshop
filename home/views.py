from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from category.models import Product
from home.forms import OrderForm
import stripe # type: ignore
from django.conf import settings
from django.shortcuts import redirect

stripe.api_key = settings.STRIPE_SECRET_KEY


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
            # Form verilerini oturuma kaydet (henüz veritabanına kaydetme)
            request.session["temp_order"] = {
                "cleaned_data": form.cleaned_data,
                "cart": request.session.get("cart", {}),
            }
            
            # Stripe Checkout Session oluştur
            YOUR_DOMAIN = "http://localhost:8000"
            cart = request.session["temp_order"]["cart"]
            line_items = []
            
            for product_id, item in cart.items():
                line_items.append({
                    "price_data": {
                        "currency": "usd",
                        "product_data": {"name": item["title"]},
                        "unit_amount": int(float(item["price"])),
                    },
                    "quantity": item["quantity"],
                })
            
            try:
                checkout_session = stripe.checkout.Session.create(
                    payment_method_types=["card"],
                    line_items=line_items,
                    mode="payment",
                    success_url=f"{YOUR_DOMAIN}/success/",
                    cancel_url=f"{YOUR_DOMAIN}/cancel/",
                )
                return redirect(checkout_session.url)
            except Exception as e:
                messages.error(request, f"Ödeme hatası: {str(e)}")
                return redirect("cart")
        else:
            # Form geçersizse hataları göster
            cart = request.session.get("cart", {})
            total_price = sum(item["price"] * item["quantity"] for item in cart.values())
            display_total_price = f"{total_price / 100:.2f}"
            return render(
                request,
                "pages/buy_now.html",
                {"form": form, "total_price": display_total_price},
            )
    else:
        form = OrderForm()
    
    cart = request.session.get("cart", {})
    total_price = sum(item["price"] * item["quantity"] for item in cart.values())
    display_total_price = f"{total_price / 100:.2f}"
    return render(
        request,
        "pages/buy_now.html",
        {"form": form, "total_price": display_total_price},
    )

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
    for item in cart.values():
        item['display_price'] = f"{item['price'] / 100:.2f}"  # Fiyatı dolar formatına çevir
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    display_total_price = f"{total_price / 100:.2f}"
    return render(request, 'pages/cart.html', {'cart': cart, 'total_price': display_total_price})

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

def success(request):
    # Oturumdaki geçici sipariş verilerini al
    temp_order = request.session.get("temp_order", None)
    
    if not temp_order:
        messages.error(request, "Geçersiz sipariş.")
        return redirect("cart")
    
    # Siparişi oluştur ve kaydet
    form = OrderForm(temp_order["cleaned_data"])
    if form.is_valid():
        order = form.save()  # Veritabanına kaydet
        
        # Ürünleri siparişe ekle
        cart = temp_order["cart"]
        for product_id, item in cart.items():
            product = Product.objects.get(id=int(product_id))
            order.products.add(product, through_defaults={"quantity": item["quantity"]})
        
        # Oturumu temizle
        del request.session["temp_order"]
        if "cart" in request.session:
            del request.session["cart"]
        request.session.modified = True
        
        messages.success(request, "Siparişiniz ve ödemeniz başarıyla tamamlandı!")
        return redirect("home")
    else:
        messages.error(request, "Sipariş oluşturulamadı.")
        return redirect("cart")
    
def cancel(request):
    # Geçici verileri temizle
    if "temp_order" in request.session:
        del request.session["temp_order"]
    request.session.modified = True
    messages.info(request, "Ödeme iptal edildi.")
    return redirect("cart")


