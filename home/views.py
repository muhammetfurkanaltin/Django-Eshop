from django.shortcuts import render
from django.http import HttpResponse

from mongoengine import connect
from mongoengine.connection import get_db

def home (request):
    return render (request,'pages/home.html')
 
def about (request):
    return render (request,'pages/about.html')

def contact (request):
    return render (request,'pages/contact.html')

def test_mongodb_connection(request):
    try:
        # Bağlantıyı test et
        db = get_db()
        # Eğer buraya kadar gelebildiyse bağlantı başarılı demektir
        return HttpResponse("MongoDB bağlantısı başarılı! Veritabanı adı: " + db.name)
    except Exception as e:
        return HttpResponse(f"MongoDB bağlantı hatası: {str(e)}")