from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(default="",null=False,unique=True,db_index=True,max_length=50)
    created_at = models.DateTimeField(auto_now_add=True) 
    

    def product_count(self):
        return self.products.count()  # Product modeli ile ilişki kurulduğunu varsayarak

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    isStock = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True)  # Slug alanı eklendi
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    

    def save(self, *args, **kwargs):
        if not self.id:
            super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def category_list(self):
        return self.category.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title