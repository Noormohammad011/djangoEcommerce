from django.db import models
from django.urls import reverse
# from djangoEcommerce.utils import get_unique_slug
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(unique=True, max_length=50)
    slug = models.SlugField(blank=True, null=True, unique=True)
    description = models.TextField(max_length=50, blank=True)
    cat_image = models.ImageField(upload_to="photoes/categories", blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('product_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = get_unique_slug(self, 'category_name', 'slug')
    #     super().save(*args, **kwargs)
