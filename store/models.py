from django.db import models
from django.urls import reverse
# Create your models here.
from category.models import Category


class Product(models.Model):
    product_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=200, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to="photoes/products")
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        pass

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name
