from rest_framework import serializers
from store.models.product_model import ProductModel
from store.serializers.rating_serializer import RatingSerializer



class ProductSerializerWithRatting(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True, read_only=True, source='store_ratingmodel')
    class Meta:
        fields = '__all__'
        model = ProductModel 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ProductModel 