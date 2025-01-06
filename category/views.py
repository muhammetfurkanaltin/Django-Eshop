from django.shortcuts import render

def reel (request):
    return render (request,'pages/reel.html')
 
def fake (request):
    return render (request,'pages/fake.html')

