from django.shortcuts import get_object_or_404, render
from .models import Category, Product

def index(request):
    product = Product.objects.filter(isStock=True)
    categories = Category.objects.all()
    return render(request, 'pages/index.html', {'product': product, 'category': categories})

def details(request,slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product
    }
    return render(request, 'pages/details.html',context)

def getProductByCategory(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'pages/index.html', context)
    
