from rest_framework import serializers
from .models import Restaurant, Review

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id','title','adress','description','no_of_reviews', 'avg_review')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id','stars','user','restaurant')