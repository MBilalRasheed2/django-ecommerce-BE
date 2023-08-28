from django.db import models
from store.models.category_model import CategoryModel


class ProductModel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, default=1, related_name='products')
    imageUrl = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
 