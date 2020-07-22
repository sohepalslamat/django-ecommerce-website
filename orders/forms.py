from django.forms import ModelForm
from .models import Order


class AddAddress(ModelForm):
    class Meta:
        model = Order
        fields = ('address',)
