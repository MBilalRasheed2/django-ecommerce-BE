from rest_framework import generics
from django.db.models import Q
from store.models.product_model import ProductModel
from store.serializers.Product_serializer import ProductSerializer, ProductSerializerWithRatting

class ProductListView(generics.ListAPIView):
    def get_serializer_class(self):
        with_rating = self.request.query_params.get('with_ratings',None)
        if with_rating:
            return ProductSerializerWithRatting
        else:
            return ProductSerializer
    
    def get_queryset(self):
        query_params = self.request.query_params
        if query_params and isinstance(query_params, dict):
            return filter_products(query_params)
        return ProductModel.objects.all()

class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()



def filter_products(query_params):
        query_params = query_params.items()

        filter_mapping ={
            'id' :('id',None),
            'category' :('category',None),
        }
        filters = Q()
        data = []
        for param, value in query_params:
            if param in filter_mapping:
                lookup, transform = filter_mapping[param]
                if transform:
                    val = query_params[param]
                    value = transform(val)
                filters &= Q(**{lookup: value}) 
        data = ProductModel.objects.filter(filters)
        return data;
    