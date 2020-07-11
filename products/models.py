from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=75)
    description = models.CharField(max_length=500, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to="products/", null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('product_details', args=[str(self.id)])

    def __str__(self):
        return self.title
