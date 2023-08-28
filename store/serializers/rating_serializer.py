from rest_framework import serializers
from store.models.ratting_model import RatingModel



class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = RatingModel 