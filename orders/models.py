from django.db import models
from django.contrib.auth import get_user_model

from products.models import Product

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(
        User, related_name='orders', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    address = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created_at.date())

    def total_price(self):
        total = 0
        for item in self.products.all():
            total += item.price
        return total
