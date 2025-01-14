from django.shortcuts import render
from category.models import Category, Product

def home (request):
    products = Product.objects.filter(isFav=True)
    return render (request,'pages/home.html',{'products':products})
 
def about (request):
    return render (request,'pages/about.html')

def contact (request):
    return render (request,'pages/contact.html')
