from django.urls import path
from .views import cart, add_to_cart, remove_from_cart, remove_all_from_cart

urlpatterns = [
    path('', cart, name="cart"),
    path('add/<int:product_id>', add_to_cart, name="add_to_cart"),
    path('remove/<int:product_id>',
         remove_from_cart, name="remove_from_cart"),
    path('remove_all/',
         remove_all_from_cart, name="remove_all_from_cart")
]
