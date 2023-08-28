from rest_framework import serializers
from store.models.cart_model import CartModel
from store.serializers.Product_serializer import ProductSerializer



class CartSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = CartModel 

class CartListSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        fields = '__all__'
        model = CartModel 