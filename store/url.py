from django.urls import path
from store.views.Category_view import CategoryListView
from store.views.Product_view import ProductListView, ProductCreateView
from store.views.cart_view import CreateCartView, CartListView


urlpatterns = [
    path('', CategoryListView.as_view(), name='Category list view'),
    path('products-create/', ProductCreateView.as_view(), name='Product create view'),
    path('products/', ProductListView.as_view(), name='Product list'),
    path('cart/', CreateCartView.as_view(), name='cart'),
    path('cartlist/', CartListView.as_view(), name='cart list')


]
