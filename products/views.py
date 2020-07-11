from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import AddProductForm


def products_list(request):
    products = Product.objects.all()
    return render(request, "products/products-list.html", {"products": products})


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/product-details.html", {'product': product})


def product_add(request):
    if request.method == "POST":
        form = AddProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(request, "products/product-add-successful.html", {'type': 'added'})
    else:
        form = AddProductForm()

    return render(request, "products/product-add.html", {'form': form, 'type': 'Add'})


def product_edit(request, pk):
    product = get_object_or_404(Product, id=pk)

    if request.method == "POST":
        form = AddProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            return render(request, "products/product-add-successful.html", {'type': 'edited'})
    else:
        form = AddProductForm(instance=product)

    return render(request, "products/product-add.html", {'form': form, 'type': 'Edit'})


def product_delete(request, pk):
    product = get_object_or_404(Product, id=pk)
    product.delete()

    return render(request, "products/product-add-successful.html", {'type': 'deleted'})
