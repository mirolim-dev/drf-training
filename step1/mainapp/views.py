from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .models import Product
from .serializers import ProductSerializer
# Create your views here.

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    data = {}
    instance = Product.objects.all().order_by('?').first()
    if instance:
        # data['id'] = product_data.id
        # data['title'] = product_data.title
        # data['content'] = product_data.content
        # data['price'] = product_data.price

        data = ProductSerializer(instance).data
    return Response(data)