from django.urls import path
from store.views.Category_view import CategoryListView
from store.views.Product_view import ProductList
from store.views.cart_view import CreateCartView, CartListView


urlpatterns = [
    path('', CategoryListView.as_view(), name='Category list view'),
    path('products/', ProductList.as_view(), name='Product list view'),
    path('products/?with_rating=1', ProductList.as_view(), name='Product by rating'),
    path('cart/', CreateCartView.as_view(), name='cart'),
    path('cartlist/', CartListView.as_view(), name='cart list')


]
