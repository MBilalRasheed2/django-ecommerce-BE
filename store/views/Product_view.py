from rest_framework import generics
from store.models.product_model import ProductModel
from store.serializers.Product_serializer import ProductSerializer, ProductSerializerWithRatting

class ProductList(generics.ListCreateAPIView):
    queryset = ProductModel.objects.all()

    def get_serializer_class(self):
        with_rating = self.request.query_params.get('with_ratings',None)
        if with_rating:
            return ProductSerializerWithRatting
        else:
            return ProductSerializer