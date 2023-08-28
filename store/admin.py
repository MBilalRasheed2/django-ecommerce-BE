from django.contrib import admin
from store.models.product_model import ProductModel
from store.models.category_model import CategoryModel
from store.models.ratting_model import RatingModel
from store.models.cart_model import CartModel



@admin.register(ProductModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description', 'price')


@admin.register(RatingModel)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating', 'review')
    
@admin.register(CartModel)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'added_at')


admin.site.register(CategoryModel)
