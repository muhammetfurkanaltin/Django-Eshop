from django.shortcuts import get_object_or_404, render
from .models import Category, Product

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'pages/index.html', {'products': products, 'category': categories})

def details(request,slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product
    }
    return render(request, 'pages/details.html',context)

def getProductByCategory(request, category_slug):
    if category_slug == 'real-fur':
        category = Category.objects.get(slug='real-fur')
        products = Product.objects.filter(category=category)
        return render(request, 'pages/real.html', {'products': products})
    elif category_slug == 'faux-fur':
        category = Category.objects.get(slug='faux-fur')
        products = Product.objects.filter(category=category)
        return render(request, 'pages/faux.html', {'products': products})
    else:
        products = Product.objects.all()
    return render(request, 'pages/index.html', {'products': products})


    
