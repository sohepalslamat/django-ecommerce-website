from django.shortcuts import render, get_object_or_404
from .models import Product


def products_list(request):
    products = Product.objects.all()
    return render(request, "products/products_list.html", {"products": products})


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/product_details.html", {'product': product})
