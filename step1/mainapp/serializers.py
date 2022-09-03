from rest_framework import serializers, generics


from .models import Product
from .serializers import ProductSerializer


class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'content', 'price', 'sale_price', 'discount')

    def get_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
    

class ProductCreateApiView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)