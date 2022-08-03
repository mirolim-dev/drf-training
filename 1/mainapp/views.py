from django.forms.models import model_to_dict
import json
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

from .models import Product

def api_view(request, *args, **kwargs):
    data = {}
    product_data = Product.objects.all().order_by('?').first()
    if product_data:
        # data['id'] = product_data.id
        # data['title'] = product_data.title
        # data['content'] = product_data.content
        # data['price'] = product_data.price

        data = model_to_dict(product_data)
    return JsonResponse(data)