from rest_framework import generics
from store.models.category_model import CategoryModel
from store.serializers.Category_serializer import CategorySerializer

class CategoryListView(generics.ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

