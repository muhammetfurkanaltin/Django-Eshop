from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'product_count']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'slug', 'category_list', 'isStock']
    list_display_links = ['title']
    list_editable = ['isStock']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}


