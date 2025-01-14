from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'isStock', 'isFav']
    list_filter = ['category', 'isStock']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['isStock', 'isFav']
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)


