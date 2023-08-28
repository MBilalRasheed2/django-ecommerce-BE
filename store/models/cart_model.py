from django.db import models
from django.contrib.auth.models import User
from store.models.product_model import ProductModel

class CartModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='store_productmodel')
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)



