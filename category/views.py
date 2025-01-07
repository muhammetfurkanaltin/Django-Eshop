from django.shortcuts import render

def home (request):
    return render (request,'home/home.html')
 
def real (request):
    return render (request,'pages/real.html')
 
def fake (request):
    return render (request,'pages/fake.html')

