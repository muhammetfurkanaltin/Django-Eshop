from django import forms
from category.models import Order  # Product yerine Order'ı import ediyoruz

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order  # Product yerine Order modelini kullanıyoruz

        fields = ['first_name', 'last_name', 'phone', 'email', 'address']
        labels = {
            'first_name': 'Ad',
            'last_name': 'Soyad',
            'phone': 'Telefon',
            'email': 'Email',
            'address': 'Adres'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        error_messages = {
            'first_name': {'required': 'Ad boş bırakılamaz.'},
            'last_name': {'required': 'Soyad boş bırakılamaz.'},
            'phone': {'required': 'Telefon boş bırakılamaz.'},
            'email': {'required': 'Email boş bırakılamaz.'},
            'address': {'required': 'Adres boş bırakılamaz.'},
        }