from rest_framework import serializers
from store.models.category_model import CategoryModel

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = CategoryModel 