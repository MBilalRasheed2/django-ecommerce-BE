from rest_framework import generics
from store.models.cart_model import CartModel
from store.serializers.cart_serializer import CartSerializer, CartListSerializer
from rest_framework.response import Response
from rest_framework import  status



class CreateCartView(generics.ListCreateAPIView):
    queryset = CartModel.objects.all()
    serializer_class = CartSerializer
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()  # Fetch the queryset
        serializer = CartSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def create(self, request, *args, **kwargs):
        product = request.data.get('product')
        quantity = request.data.get('quantity')
        user = request.data.get('user')

        try:
            cart = CartModel.objects.get(user=user, product=product)
            cart.quantity = int(quantity)
            cart.save()
            serializer = CartSerializer(cart)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CartModel.DoesNotExist:
            serializer = CartSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartListView(generics.ListAPIView):
    queryset = CartModel.objects.all()
    serializer_class = CartListSerializer
