from django.urls import path
from .views import products_list, product_details, product_add, product_edit

urlpatterns = [
    path('', products_list, name="products_list"),
    path('<int:pk>', product_details, name="product_details"),
    path('add', product_add, name="product_add"),
    path('edit/<int:pk>', product_edit, name="product_edit"),
]
