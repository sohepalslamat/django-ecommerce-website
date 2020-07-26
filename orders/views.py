from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Order
from .forms import AddAddress
from .utils import send_order_email


@login_required
def order(request):
    user = request.user
    items = user.cart.items.all()
    if items:
        if request.method == "POST":
            form = AddAddress(request.POST)

            if form.is_valid():

                order = Order(user=user,
                              address=request.POST['address'])
                order.save()
                order.products.set(items)
                user.cart.items.clear()
                send_order_email(user, order)
                return render(request, "orders/order-successful.html")
        else:
            form = AddAddress()

        return render(request, "orders/add-address.html", {'form': form})
    else:
        return redirect('cart')


def order_list(request):
    if request.user.is_authenticated and request.user.is_superuser:
        orders = Order.objects.all()
        return render(request, 'orders/order_list.html', {'orders': orders})
    else:
        redirect('prduct_list')
