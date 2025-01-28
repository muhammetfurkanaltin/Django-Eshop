from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True) 

    def product_count(self):
        return self.products.count()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,related_name='products')
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField(default=0)
    isStock = models.BooleanField(default=True)
    isFav = models.BooleanField(default=False)
    imagUrl = models.CharField(null=True,max_length=50, blank=False)
    slug = models.SlugField(unique=True, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)
 

    def save(self, *args, **kwargs):
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
    
    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100 )


class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, through='OrderItem')

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

