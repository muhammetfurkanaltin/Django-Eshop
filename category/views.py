from django.shortcuts import get_object_or_404, render
from .models import Category, Product


def details(request,slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product
    }
    return render(request, 'pages/details.html',context)

def getProductByCategory(request,slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)
    return render(request, 'pages/real.html', {'products': products})
