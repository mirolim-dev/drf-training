from ast import ClassDef
from django.forms import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'content', 'price')