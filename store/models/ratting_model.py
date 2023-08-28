from django.db import models
from django.contrib.auth.models import User
from store.models.product_model import ProductModel

class RatingModel(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='store_ratingmodel')
    rating = models.DecimalField(choices=RATING_CHOICES, decimal_places=2, max_digits=1000)
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f"{self.product.name} - {self.get_rating_display()}"

    class Meta:
        unique_together = ('user', 'product')